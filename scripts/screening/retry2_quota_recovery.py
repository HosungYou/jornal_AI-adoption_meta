#!/usr/bin/env python3
"""
2차 retry: API 할당량 회복 후 실행
- A (250건): Codex + Gemini 둘 다 실패 → Codex spark retry 후 Gemini Flash retry
- B (1,575건): Gemini 실패, Codex uncertain → Gemini Flash retry
- C-T2 (3건): T2 Gemini uncertain, Codex 없음 → Codex retry
"""
import pandas as pd
import asyncio
import json
import re
import logging
import argparse
from pathlib import Path

logger = logging.getLogger(__name__)

CODEX_MODELS = ["gpt-5.1-codex-mini", "gpt-5.3-codex-spark"]
_codex_model_idx = 0


def build_prompt(row: pd.Series) -> str:
    title = row.get("title", "")
    abstract = row.get("abstract", "")
    return f"""You are screening academic papers for a meta-analysis on AI adoption in education.

INCLUSION CRITERIA:
1. Empirical quantitative study (survey, experiment, longitudinal)
2. AI-based tool/system in educational context
3. Measures adoption, acceptance, intention to use, or actual use of AI
4. Sample size >= 50
5. Reports statistical relationships (correlation, regression, SEM, etc.)

EXCLUSION CRITERIA:
- Qualitative studies only
- No adoption/acceptance measurement
- Not educational context
- Sample < 50
- Review papers, meta-analyses, theoretical only

Title: {title}
Abstract: {abstract}

Respond in JSON only:
{{"decision": "include|exclude|uncertain", "confidence": 0.0-1.0, "exclude_code": "E1-E5 or empty", "rationale": "brief reason"}}"""


def parse_ai_response(raw: str) -> dict:
    try:
        m = re.search(r'\{.*\}', raw, re.DOTALL)
        if m:
            return json.loads(m.group())
    except Exception:
        pass
    raw_lower = raw.lower()
    if "include" in raw_lower:
        return {"decision": "include", "confidence": 0.7, "exclude_code": "", "rationale": raw[:200]}
    if "exclude" in raw_lower:
        return {"decision": "exclude", "confidence": 0.7, "exclude_code": "", "rationale": raw[:200]}
    return {"decision": "uncertain", "confidence": 0.0, "exclude_code": "", "rationale": f"parse failed: {raw[:100]}"}


def normalize_decision(value: str) -> str:
    v = (value or "").strip().lower()
    if v in {"include", "included"}: return "include"
    if v in {"exclude", "excluded"}: return "exclude"
    return "uncertain"


def consensus(dec1: str, dec2: str) -> str:
    if dec1 == dec2 == "include": return "include"
    if dec1 == dec2 == "exclude": return "exclude"
    if {dec1, dec2} == {"include", "exclude"}: return "conflict"
    if "uncertain" in (dec1, dec2):
        other = dec1 if dec2 == "uncertain" else dec2
        return other if other in ("include", "exclude") else "uncertain"
    return "conflict"


async def _call_codex(model: str, prompt: str, timeout: int) -> tuple[str, str]:
    proc = await asyncio.create_subprocess_exec(
        "codex", "-m", model, "exec", prompt,
        stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await asyncio.wait_for(proc.communicate(), timeout=timeout)
    return stdout.decode("utf-8", errors="replace").strip(), stderr.decode("utf-8", errors="replace").strip()


async def screen_codex(prompt: str, timeout: int = 300) -> dict:
    global _codex_model_idx
    for attempt in range(_codex_model_idx, len(CODEX_MODELS)):
        model = CODEX_MODELS[attempt]
        try:
            raw, err = await _call_codex(model, prompt, timeout)
            if "usage limit" in err.lower() or "usage limit" in raw.lower():
                logger.warning(f"Codex {model} quota exhausted → fallback")
                _codex_model_idx = attempt + 1
                continue
            if not raw:
                return {"decision": "uncertain", "confidence": 0.0, "rationale": f"codex({model}) empty: {err[:100]}"}
            result = parse_ai_response(raw)
            result["_model"] = model
            return result
        except asyncio.TimeoutError:
            return {"decision": "uncertain", "confidence": 0.0, "rationale": f"codex({model}) timed out after {timeout}s"}
        except Exception as e:
            return {"decision": "uncertain", "confidence": 0.0, "rationale": f"codex({model}) failed: {str(e)[:100]}"}
    return {"decision": "uncertain", "confidence": 0.0, "rationale": "codex all models exhausted"}


async def screen_gemini_flash(prompt: str, timeout: int = 300) -> dict:
    try:
        proc = await asyncio.create_subprocess_exec(
            "gemini", "-m", "gemini-2.5-flash", "-p", prompt,
            stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await asyncio.wait_for(proc.communicate(), timeout=timeout)
        raw = stdout.decode("utf-8", errors="replace").strip()
        if not raw:
            return {"decision": "uncertain", "confidence": 0.0, "rationale": f"gemini-flash empty: {stderr.decode()[:100]}"}
        return parse_ai_response(raw)
    except asyncio.TimeoutError:
        return {"decision": "uncertain", "confidence": 0.0, "rationale": f"gemini-flash timed out after {timeout}s"}
    except Exception as e:
        return {"decision": "uncertain", "confidence": 0.0, "rationale": f"gemini-flash failed: {str(e)[:100]}"}


async def process_codex_retry(row: pd.Series, sem: asyncio.Semaphore, timeout: int) -> dict:
    async with sem:
        result = await screen_codex(build_prompt(row), timeout)
        return {
            "record_id": row["record_id"], "engine": "codex",
            "screen_decision_codex": normalize_decision(result.get("decision", "uncertain")),
            "screen_confidence_codex": result.get("confidence", 0.0),
            "exclude_code_codex": result.get("exclude_code", ""),
            "rationale_codex": result.get("rationale", ""),
            "_model": result.get("_model", "unknown"),
        }


async def process_gemini_retry(row: pd.Series, sem: asyncio.Semaphore, timeout: int) -> dict:
    async with sem:
        result = await screen_gemini_flash(build_prompt(row), timeout)
        return {
            "record_id": row["record_id"], "engine": "gemini-flash",
            "screen_decision_gemini": normalize_decision(result.get("decision", "uncertain")),
            "screen_confidence_gemini": result.get("confidence", 0.0),
            "exclude_code_gemini": result.get("exclude_code", ""),
            "rationale_gemini": result.get("rationale", ""),
        }


async def run_retry2(args):
    df = pd.read_csv(args.input)
    logger.info(f"Loaded {len(df)} records")

    unc = df[df["screen_consensus"] == "uncertain"].copy()
    codex_quota_fail = unc["rationale_codex"].str.contains(
        "exhausted|usage limit", case=False, na=False)
    gem_fail = unc["rationale_gemini"].str.contains(
        "failed|timed out|empty", case=False, na=False)
    other = unc[~codex_quota_fail & ~gem_fail]
    t2_codex_needed = other[other["rationale_codex"].str.contains("T2: single-AI", na=False)]

    # Groups:
    group_A = unc[codex_quota_fail & gem_fail]   # 둘 다 실패 → Codex 먼저, 그 다음 Gemini
    group_B = unc[~codex_quota_fail & gem_fail]  # Gemini만 실패 → Gemini retry
    group_C = t2_codex_needed                     # T2 Codex 없음 → Codex retry

    logger.info(f"Group A (Codex+Gemini retry): {len(group_A)}건")
    logger.info(f"Group B (Gemini retry only): {len(group_B)}건")
    logger.info(f"Group C (T2 Codex retry): {len(group_C)}건")

    sem = asyncio.Semaphore(args.workers)

    # Phase 1: Codex retry (A + C)
    codex_needed = pd.concat([group_A, group_C])
    codex_tasks = [process_codex_retry(row, sem, args.timeout) for _, row in codex_needed.iterrows()]
    codex_results = []
    for i, coro in enumerate(asyncio.as_completed(codex_tasks)):
        r = await coro
        codex_results.append(r)
        if (i + 1) % args.save_every == 0:
            logger.info(f"Codex retry: {i+1}/{len(codex_tasks)}")

    # Apply Codex results
    for r in codex_results:
        idx = df[df["record_id"] == r["record_id"]].index
        if len(idx) == 0: continue
        i = idx[0]
        df.loc[i, "screen_decision_codex"] = r["screen_decision_codex"]
        df.loc[i, "screen_confidence_codex"] = r["screen_confidence_codex"]
        df.loc[i, "exclude_code_codex"] = r["exclude_code_codex"]
        df.loc[i, "rationale_codex"] = r["rationale_codex"]
        df.loc[i, "codex_retry2_model"] = r["_model"]

    # Phase 2: Gemini retry (A + B)
    gemini_needed = pd.concat([group_A, group_B])
    gem_tasks = [process_gemini_retry(row, sem, args.timeout) for _, row in gemini_needed.iterrows()]
    gem_results = []
    for i, coro in enumerate(asyncio.as_completed(gem_tasks)):
        r = await coro
        gem_results.append(r)
        if (i + 1) % args.save_every == 0:
            logger.info(f"Gemini retry: {i+1}/{len(gem_tasks)}")

    # Apply Gemini results + recalculate consensus
    recovered = 0
    still_failed = 0
    for r in gem_results:
        idx = df[df["record_id"] == r["record_id"]].index
        if len(idx) == 0: continue
        i = idx[0]
        df.loc[i, "screen_decision_gemini"] = r["screen_decision_gemini"]
        df.loc[i, "screen_confidence_gemini"] = r["screen_confidence_gemini"]
        df.loc[i, "exclude_code_gemini"] = r["exclude_code_gemini"]
        df.loc[i, "rationale_gemini"] = r["rationale_gemini"]
        # Recalculate consensus
        codex_dec = str(df.loc[i, "screen_decision_codex"]).strip().lower()
        gemini_dec = r["screen_decision_gemini"]
        new_consensus = consensus(codex_dec, gemini_dec)
        df.loc[i, "screen_consensus"] = new_consensus
        is_fail = "failed" in r.get("rationale_gemini", "") or "timed out" in r.get("rationale_gemini", "")
        if is_fail: still_failed += 1
        else: recovered += 1

    df.to_csv(args.input, index=False)

    print(f"\n{'='*60}")
    print("RETRY 2 RESULTS")
    print(f"{'='*60}")
    print(f"Gemini recovered: {recovered}")
    print(f"Still failed: {still_failed}")
    print(f"\nFinal consensus:")
    print(df["screen_consensus"].value_counts().to_string())


def main():
    parser = argparse.ArgumentParser(description="2차 retry: quota recovery 후 실행")
    parser.add_argument("input", help="screening_ai_dual.csv path")
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--timeout", type=int, default=300)
    parser.add_argument("--save-every", type=int, default=50)
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    asyncio.run(run_retry2(args))


if __name__ == "__main__":
    main()
