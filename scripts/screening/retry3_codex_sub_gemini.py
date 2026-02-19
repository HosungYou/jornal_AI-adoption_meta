#!/usr/bin/env python3
"""
retry3: Codex를 Gemini 대체로 사용 (685건 Gemini 잔여 실패)
- screen_decision_gemini = Codex 재판단 결과
- rationale_gemini = "Codex-sub: {rationale}"
- screen_consensus 재계산
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
                return {"decision": "uncertain", "confidence": 0.0, "rationale": f"codex({model}) empty: {err[:100]}", "_model": model}
            result = parse_ai_response(raw)
            result["_model"] = model
            return result
        except asyncio.TimeoutError:
            return {"decision": "uncertain", "confidence": 0.0, "rationale": f"codex({model}) timed out after {timeout}s", "_model": model}
        except Exception as e:
            return {"decision": "uncertain", "confidence": 0.0, "rationale": f"codex({model}) failed: {str(e)[:100]}", "_model": model}
    return {"decision": "uncertain", "confidence": 0.0, "rationale": "codex all models exhausted", "_model": "none"}


async def process_record(row: pd.Series, sem: asyncio.Semaphore, timeout: int) -> dict:
    async with sem:
        result = await screen_codex(build_prompt(row), timeout)
        return {
            "record_id": row["record_id"],
            "decision": normalize_decision(result.get("decision", "uncertain")),
            "confidence": result.get("confidence", 0.0),
            "exclude_code": result.get("exclude_code", ""),
            "rationale": result.get("rationale", ""),
            "_model": result.get("_model", "unknown"),
        }


async def run_retry3(args):
    df = pd.read_csv(args.input)
    logger.info(f"Loaded {len(df)} records")

    unc = df[df["screen_consensus"] == "uncertain"]
    gem_fail_mask = unc["rationale_gemini"].str.contains(
        "failed|timed out|empty", case=False, na=False)
    targets = unc[gem_fail_mask].copy()
    logger.info(f"Gemini-failed targets: {len(targets)}건 → Codex 대체 처리")

    sem = asyncio.Semaphore(args.workers)
    tasks = [process_record(row, sem, args.timeout) for _, row in targets.iterrows()]

    results = []
    for i, coro in enumerate(asyncio.as_completed(tasks)):
        r = await coro
        results.append(r)
        if (i + 1) % args.save_every == 0:
            logger.info(f"Codex-sub progress: {i+1}/{len(tasks)}")

    # Apply results: use Codex result as Gemini substitute
    recovered = 0
    still_uncertain = 0
    for r in results:
        idx = df[df["record_id"] == r["record_id"]].index
        if len(idx) == 0:
            continue
        i = idx[0]
        # Update Gemini slot with Codex substitution
        df.loc[i, "screen_decision_gemini"] = r["decision"]
        df.loc[i, "screen_confidence_gemini"] = r["confidence"]
        df.loc[i, "exclude_code_gemini"] = r["exclude_code"]
        df.loc[i, "rationale_gemini"] = f"Codex-sub({r['_model']}): {r['rationale']}"
        # Recalculate consensus
        codex_dec = str(df.loc[i, "screen_decision_codex"]).strip().lower()
        new_consensus = consensus(codex_dec, r["decision"])
        df.loc[i, "screen_consensus"] = new_consensus
        if r["decision"] in ("include", "exclude"):
            recovered += 1
        else:
            still_uncertain += 1

    df.to_csv(args.input, index=False)

    print(f"\n{'='*60}")
    print("RETRY 3 (Codex sub for Gemini) RESULTS")
    print(f"{'='*60}")
    print(f"Codex sub recovered (include/exclude): {recovered}")
    print(f"Still uncertain: {still_uncertain}")
    print(f"\nFinal consensus:")
    print(df["screen_consensus"].value_counts().to_string())


def main():
    parser = argparse.ArgumentParser(description="retry3: Codex as Gemini substitute for failed records")
    parser.add_argument("input", help="screening_ai_dual.csv path")
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--timeout", type=int, default=300)
    parser.add_argument("--save-every", type=int, default=50)
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    asyncio.run(run_retry3(args))


if __name__ == "__main__":
    main()
