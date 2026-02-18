#!/usr/bin/env python3
"""
Retry Gemini-failed records from screening_ai_dual.csv.
Only re-runs Gemini for records where rationale_gemini contains 'failed' or 'exhausted'.
Preserves all existing Codex results.
"""
import pandas as pd
import asyncio
import subprocess
import json
import re
import logging
import argparse
import time
from pathlib import Path

logger = logging.getLogger(__name__)


def load_config(config_path: str) -> dict:
    import yaml
    with open(config_path) as f:
        return yaml.safe_load(f)


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


async def screen_gemini(prompt: str, timeout: int = 300) -> dict:
    try:
        proc = await asyncio.create_subprocess_exec(
            "gemini", "-p", prompt,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await asyncio.wait_for(proc.communicate(), timeout=timeout)
        raw = stdout.decode("utf-8", errors="replace").strip()
        if not raw:
            return {"decision": "uncertain", "confidence": 0.0, "rationale": f"gemini empty response: {stderr.decode()[:100]}"}
        return parse_ai_response(raw)
    except asyncio.TimeoutError:
        return {"decision": "uncertain", "confidence": 0.0, "rationale": f"gemini timed out after {timeout}s"}
    except Exception as e:
        return {"decision": "uncertain", "confidence": 0.0, "rationale": f"gemini failed: {str(e)[:100]}"}


def consensus(codex_dec: str, gemini_dec: str) -> str:
    if codex_dec == gemini_dec:
        return codex_dec
    if {codex_dec, gemini_dec} == {"include", "exclude"}:
        return "conflict"
    if "uncertain" in (codex_dec, gemini_dec):
        other = codex_dec if gemini_dec == "uncertain" else gemini_dec
        return other if other in ("include", "exclude") else "uncertain"
    return "conflict"


async def process_one(row: pd.Series, sem: asyncio.Semaphore, timeout: int) -> dict:
    async with sem:
        prompt = build_prompt(row)
        result = await screen_gemini(prompt, timeout)
        return {
            "record_id": row["record_id"],
            "screen_decision_gemini": result.get("decision", "uncertain"),
            "screen_confidence_gemini": result.get("confidence", 0.0),
            "exclude_code_gemini": result.get("exclude_code", ""),
            "rationale_gemini": result.get("rationale", ""),
        }


async def run_retry(args):
    df = pd.read_csv(args.input)
    logger.info(f"Loaded {len(df)} records")

    # Find Gemini failures
    fail_mask = df["rationale_gemini"].str.contains(
        r"failed|exhausted|timed out|empty response", case=False, na=False
    )
    failures = df[fail_mask].copy()
    logger.info(f"Found {len(failures)} Gemini failures to retry")

    if len(failures) == 0:
        logger.info("No failures to retry. Exiting.")
        return

    sem = asyncio.Semaphore(args.workers)
    tasks = [process_one(row, sem, args.timeout) for _, row in failures.iterrows()]

    completed = 0
    results = []
    for coro in asyncio.as_completed(tasks):
        result = await coro
        results.append(result)
        completed += 1
        if completed % args.save_every == 0:
            logger.info(f"Retry progress: {completed}/{len(failures)}")

    # Update original dataframe
    success_count = 0
    still_failed = 0
    for r in results:
        idx = df[df["record_id"] == r["record_id"]].index
        if len(idx) == 0:
            continue
        i = idx[0]
        df.loc[i, "screen_decision_gemini"] = r["screen_decision_gemini"]
        df.loc[i, "screen_confidence_gemini"] = r["screen_confidence_gemini"]
        df.loc[i, "exclude_code_gemini"] = r["exclude_code_gemini"]
        df.loc[i, "rationale_gemini"] = r["rationale_gemini"]

        # Recalculate consensus
        codex_dec = df.loc[i, "screen_decision_codex"]
        gemini_dec = r["screen_decision_gemini"]
        df.loc[i, "screen_consensus"] = consensus(codex_dec, gemini_dec)

        if "failed" not in r["rationale_gemini"] and "timed out" not in r["rationale_gemini"]:
            success_count += 1
        else:
            still_failed += 1

    df.to_csv(args.input, index=False)
    logger.info(f"Retry complete: {success_count} recovered, {still_failed} still failed")

    # Summary
    print(f"\nRetry Results:")
    print(f"  Total retried: {len(failures)}")
    print(f"  Recovered: {success_count}")
    print(f"  Still failed: {still_failed}")
    print(f"\nUpdated consensus:")
    print(df["screen_consensus"].value_counts().to_string())


def main():
    _default_config = str(Path(__file__).resolve().parent.parent / "ai_coding_pipeline" / "config.yaml")
    parser = argparse.ArgumentParser(description="Retry Gemini failures in screening results")
    parser.add_argument("input", type=str, help="screening_ai_dual.csv path")
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--timeout", type=int, default=300)
    parser.add_argument("--save-every", type=int, default=50)
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    asyncio.run(run_retry(args))


if __name__ == "__main__":
    main()
