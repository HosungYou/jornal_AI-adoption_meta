#!/usr/bin/env python3
"""
Retry Gemini-failed records from screening_ai_dual.csv.

Strategy by tier:
  T2 (single AI): Gemini failed → re-screen with Codex (gpt-5)
  T3 (dual AI):   Gemini failed → retry with Gemini 2.5 Flash

Preserves all existing successful results.
"""
import pandas as pd
import asyncio
import json
import re
import logging
import argparse
from pathlib import Path

logger = logging.getLogger(__name__)


def build_prompt(row: pd.Series) -> str:
    title = row.get("title", "")
    abstract = row.get("abstract", "")
    keywords = row.get("keywords", "")
    source = row.get("source_database", "unknown")
    return f"""You are screening studies for an educational AI adoption meta-analysis.

Apply these inclusion criteria:
1. Empirical quantitative study (surveys, experiments, quasi-experiments, SEM/path analysis)
2. Focuses on AI tools in education (ChatGPT, AI tutors, intelligent tutoring, generative AI, LLM-based tools)
3. Measures adoption/acceptance constructs (TAM, UTAUT, intention, perceived usefulness, self-efficacy, trust)
4. Participants are students, teachers, or educational staff
5. Published 2015-2025 in English
6. Reports usable effect sizes (correlations, regression, SEM paths)

Respond in JSON: {{"decision":"include|exclude|uncertain","confidence":0.0-1.0,"exclude_code":"E1-E8 or empty","rationale":"1-2 sentences"}}

Exclude codes: E1=not empirical, E2=not AI-focused, E3=not education, E4=no adoption constructs, E5=qualitative only, E6=no effect sizes, E7=duplicate/secondary, E8=not English/not 2015-2025

---
Title: {title}
Abstract: {abstract}
Keywords: {keywords}
Source: {source}"""


def parse_ai_response(raw: str) -> dict:
    patterns = [
        r'\{[^{}]*"decision"[^{}]*\}',
        r'```json\s*(\{.*?\})\s*```',
    ]
    for pat in patterns:
        m = re.search(pat, raw, re.DOTALL)
        if m:
            try:
                text = m.group(1) if m.lastindex else m.group(0)
                return json.loads(text)
            except json.JSONDecodeError:
                continue
    return {"decision": "uncertain", "confidence": 0.0, "exclude_code": "", "rationale": f"parse failed: {raw[:100]}"}


def normalize_decision(value: str) -> str:
    v = (value or "").strip().lower()
    if v in {"include", "included"}:
        return "include"
    if v in {"exclude", "excluded"}:
        return "exclude"
    return "uncertain"


def consensus(dec1: str, dec2: str) -> str:
    if dec1 == dec2 == "include":
        return "include"
    if dec1 == dec2 == "exclude":
        return "exclude"
    if {dec1, dec2} == {"include", "exclude"}:
        return "conflict"
    if "uncertain" in (dec1, dec2):
        other = dec1 if dec2 == "uncertain" else dec2
        return other if other in ("include", "exclude") else "uncertain"
    return "conflict"


# ──────────────────────────────────────────────────────────────────────
# Provider async callers
# ──────────────────────────────────────────────────────────────────────

# Codex model fallback chain: mini (cheaper) → spark (fallback if quota hit)
CODEX_MODELS = ["gpt-5.1-codex-mini", "gpt-5.3-codex-spark"]
_codex_model_idx = 0  # Track current model globally


async def _call_codex(model: str, prompt: str, timeout: int) -> tuple[str, str]:
    """Raw Codex CLI call. Returns (stdout, stderr)."""
    proc = await asyncio.create_subprocess_exec(
        "codex", "-m", model, "exec", prompt,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await asyncio.wait_for(proc.communicate(), timeout=timeout)
    return stdout.decode("utf-8", errors="replace").strip(), stderr.decode("utf-8", errors="replace").strip()


async def screen_codex(prompt: str, timeout: int = 300) -> dict:
    """Screen with Codex CLI using fallback chain: mini → spark."""
    global _codex_model_idx

    for attempt in range(_codex_model_idx, len(CODEX_MODELS)):
        model = CODEX_MODELS[attempt]
        try:
            raw, err = await _call_codex(model, prompt, timeout)
            # Detect quota exhaustion → switch to next model
            if "usage limit" in err.lower() or "usage limit" in raw.lower():
                logger.warning(f"Codex {model} quota exhausted, falling back to next model")
                _codex_model_idx = attempt + 1
                continue
            if not raw:
                return {"decision": "uncertain", "confidence": 0.0,
                        "rationale": f"codex({model}) empty: {err[:100]}"}
            result = parse_ai_response(raw)
            result["_model"] = model
            return result
        except asyncio.TimeoutError:
            return {"decision": "uncertain", "confidence": 0.0,
                    "rationale": f"codex({model}) timed out after {timeout}s"}
        except Exception as e:
            return {"decision": "uncertain", "confidence": 0.0,
                    "rationale": f"codex({model}) failed: {str(e)[:100]}"}

    return {"decision": "uncertain", "confidence": 0.0,
            "rationale": "codex all models exhausted (mini + spark)"}


async def screen_gemini_flash(prompt: str, timeout: int = 300) -> dict:
    """Screen with Gemini 2.5 Flash."""
    try:
        proc = await asyncio.create_subprocess_exec(
            "gemini", "-m", "gemini-2.5-flash", "-p", prompt,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await asyncio.wait_for(proc.communicate(), timeout=timeout)
        raw = stdout.decode("utf-8", errors="replace").strip()
        if not raw:
            return {"decision": "uncertain", "confidence": 0.0, "rationale": f"gemini-flash empty response: {stderr.decode()[:100]}"}
        return parse_ai_response(raw)
    except asyncio.TimeoutError:
        return {"decision": "uncertain", "confidence": 0.0, "rationale": f"gemini-flash timed out after {timeout}s"}
    except Exception as e:
        return {"decision": "uncertain", "confidence": 0.0, "rationale": f"gemini-flash failed: {str(e)[:100]}"}


# ──────────────────────────────────────────────────────────────────────
# Per-record processors
# ──────────────────────────────────────────────────────────────────────

async def process_t2_with_codex(row: pd.Series, sem: asyncio.Semaphore, timeout: int) -> dict:
    """T2 Gemini failure → screen with Codex instead."""
    async with sem:
        prompt = build_prompt(row)
        result = await screen_codex(prompt, timeout)
        decision = normalize_decision(result.get("decision", "uncertain"))
        return {
            "record_id": row["record_id"],
            "engine": "codex",
            "screen_decision_codex": decision,
            "screen_confidence_codex": result.get("confidence", 0.0),
            "exclude_code_codex": result.get("exclude_code", ""),
            "rationale_codex": result.get("rationale", ""),
        }


async def process_t3_with_flash(row: pd.Series, sem: asyncio.Semaphore, timeout: int) -> dict:
    """T3 Gemini failure → retry with Gemini 2.5 Flash."""
    async with sem:
        prompt = build_prompt(row)
        result = await screen_gemini_flash(prompt, timeout)
        decision = normalize_decision(result.get("decision", "uncertain"))
        return {
            "record_id": row["record_id"],
            "engine": "gemini-flash",
            "screen_decision_gemini": decision,
            "screen_confidence_gemini": result.get("confidence", 0.0),
            "exclude_code_gemini": result.get("exclude_code", ""),
            "rationale_gemini": result.get("rationale", ""),
        }


# ──────────────────────────────────────────────────────────────────────
# Main retry logic
# ──────────────────────────────────────────────────────────────────────

async def run_retry(args):
    df = pd.read_csv(args.input)
    logger.info(f"Loaded {len(df)} records")

    # Identify Gemini failures
    fail_mask = df["rationale_gemini"].str.contains(
        r"failed|exhausted|timed out|empty response", case=False, na=False
    )
    failures = df[fail_mask].copy()
    logger.info(f"Total Gemini failures: {len(failures)}")

    # Split by tier
    t2_fails = failures[failures["screening_tier"].str.startswith("T2", na=False)]
    t3_fails = failures[failures["screening_tier"].str.startswith("T3", na=False)]
    logger.info(f"T2 failures (→ Codex): {len(t2_fails)}")
    logger.info(f"T3 failures (→ Gemini Flash): {len(t3_fails)}")

    sem = asyncio.Semaphore(args.workers)

    # Build task lists
    t2_tasks = [process_t2_with_codex(row, sem, args.timeout) for _, row in t2_fails.iterrows()]
    t3_tasks = [process_t3_with_flash(row, sem, args.timeout) for _, row in t3_fails.iterrows()]
    all_tasks = t2_tasks + t3_tasks

    if not all_tasks:
        logger.info("No failures to retry. Exiting.")
        return

    # Execute all concurrently
    completed = 0
    results = []
    t2_ok, t2_fail, t3_ok, t3_fail = 0, 0, 0, 0

    for coro in asyncio.as_completed(all_tasks):
        result = await coro
        results.append(result)
        completed += 1
        if completed % args.save_every == 0:
            logger.info(f"Retry progress: {completed}/{len(all_tasks)}")

    # Apply results
    for r in results:
        idx = df[df["record_id"] == r["record_id"]].index
        if len(idx) == 0:
            continue
        i = idx[0]

        if r["engine"] == "codex":
            # T2: Codex replaces the missing Gemini screening
            # Store Codex result and recalculate consensus using Gemini's original + Codex
            df.loc[i, "screen_decision_codex"] = r["screen_decision_codex"]
            df.loc[i, "screen_confidence_codex"] = r["screen_confidence_codex"]
            df.loc[i, "exclude_code_codex"] = r["exclude_code_codex"]
            df.loc[i, "rationale_codex"] = r["rationale_codex"]
            df.loc[i, "oauth_auth_method_codex"] = "retry_codex_for_t2"
            # Consensus: Codex result stands alone for T2 (Gemini already failed)
            # Use Codex as primary, keep Gemini failure as-is
            df.loc[i, "screen_consensus"] = r["screen_decision_codex"]
            is_fail = "failed" in r.get("rationale_codex", "") or "timed out" in r.get("rationale_codex", "")
            if is_fail:
                t2_fail += 1
            else:
                t2_ok += 1

        elif r["engine"] == "gemini-flash":
            # T3: Update Gemini result with Flash retry
            df.loc[i, "screen_decision_gemini"] = r["screen_decision_gemini"]
            df.loc[i, "screen_confidence_gemini"] = r["screen_confidence_gemini"]
            df.loc[i, "exclude_code_gemini"] = r["exclude_code_gemini"]
            df.loc[i, "rationale_gemini"] = r["rationale_gemini"]
            df.loc[i, "oauth_auth_method_gemini"] = "retry_gemini-2.5-flash"
            # Recalculate consensus with existing Codex + new Gemini
            codex_dec = str(df.loc[i, "screen_decision_codex"]).strip().lower()
            gemini_dec = r["screen_decision_gemini"]
            df.loc[i, "screen_consensus"] = consensus(codex_dec, gemini_dec)
            is_fail = "failed" in r.get("rationale_gemini", "") or "timed out" in r.get("rationale_gemini", "")
            if is_fail:
                t3_fail += 1
            else:
                t3_ok += 1

    # Save
    df.to_csv(args.input, index=False)

    # Summary
    logger.info(f"Retry complete!")
    print(f"\n{'='*60}")
    print(f"RETRY RESULTS")
    print(f"{'='*60}")
    print(f"T2 (Codex retry):       {t2_ok} recovered, {t2_fail} still failed (of {len(t2_fails)})")
    print(f"T3 (Gemini Flash retry): {t3_ok} recovered, {t3_fail} still failed (of {len(t3_fails)})")
    print(f"\nUpdated consensus distribution:")
    print(df["screen_consensus"].value_counts().to_string())
    print(f"\nInclude: {len(df[df['screen_consensus']=='include'])}")
    print(f"Exclude: {len(df[df['screen_consensus']=='exclude'])}")
    print(f"Conflict: {len(df[df['screen_consensus']=='conflict'])}")
    print(f"Uncertain: {len(df[df['screen_consensus']=='uncertain'])}")


def main():
    parser = argparse.ArgumentParser(description="Retry Gemini failures: T2→Codex, T3→Gemini Flash")
    parser.add_argument("input", type=str, help="screening_ai_dual.csv path")
    parser.add_argument("--workers", type=int, default=8, help="Concurrent workers")
    parser.add_argument("--timeout", type=int, default=300, help="Per-record timeout (seconds)")
    parser.add_argument("--save-every", type=int, default=50, help="Log progress interval")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    asyncio.run(run_retry(args))


if __name__ == "__main__":
    main()
