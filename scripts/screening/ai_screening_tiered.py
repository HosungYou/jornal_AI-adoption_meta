#!/usr/bin/env python3
"""
Three-tier accelerated screening for systematic review.

Tier 1 (instant):   Keyword pre-filter — auto-exclude records with no AI terms
Tier 2 (single AI): Records with AI + partial match → Gemini only (faster, 0 timeouts)
Tier 3 (dual AI):   Records with AI + education + adoption → Codex + Gemini concurrent

Validated on 104-record pilot: 0 false negatives from keyword filter.
Expected speedup: ~50x over naive sequential (147h → ~2.5h).
"""

from __future__ import annotations

import argparse
import asyncio
import json
import logging
import re
import time
from pathlib import Path
from typing import Any

import pandas as pd
import yaml

logger = logging.getLogger(__name__)

# ──────────────────────────────────────────────────────────────────────
# Screening prompt (shared across tiers)
# ──────────────────────────────────────────────────────────────────────

SCREENING_PROMPT = """You are screening studies for an educational AI adoption meta-analysis.

Apply these criteria:
1) Empirical quantitative study with primary data
2) AI technology is focal (not general ICT/IT)
3) Educational setting/population (students, instructors, administrators)
4) Adoption/acceptance/intention/use is measured
5) Correlation matrix or standardized beta/path data appears available or likely
6) English language
7) Publication window target: 2015-2025
8) Sample size n >= 50 (if stated or inferable from abstract)
9) Peer-reviewed journal article or full conference paper

Exclude codes:
E1=Not empirical/quantitative, E2=AI not focal, E3=Not education context,
E4=No adoption/acceptance outcome, E5=No effect size data,
E6=Not English, E7=Outside 2015-2025, E8=n<50, E9=Not peer-reviewed,
E10=Duplicate sample, E11=Qualitative/review only, E12=Other

Return strict JSON:
{{
  "decision": "include|exclude|uncertain",
  "confidence": 0.0,
  "exclude_code": "E1|E2|E3|E4|E5|E6|E7|E8|E9|E10|E11|E12|NA",
  "criteria_flags": {{
    "quantitative": "yes|no|unclear",
    "ai_focal": "yes|no|unclear",
    "education_context": "yes|no|unclear",
    "adoption_outcome": "yes|no|unclear",
    "effect_size_reported": "yes|no|unclear",
    "english": "yes|no|unclear",
    "sample_size_adequate": "yes|no|unclear"
  }},
  "rationale": "1-2 sentences"
}}

Title: {title}
Abstract: {abstract}
Keywords: {keywords}
Year: {year}
Source: {source}
"""

# ──────────────────────────────────────────────────────────────────────
# Keyword patterns for Tier 1 pre-filter
# ──────────────────────────────────────────────────────────────────────

AI_PATTERN = re.compile(
    r"\b("
    r"artificial intelligence|machine learning|deep learning|"
    r"intelligent tutoring|chatbot|ChatGPT|GPT-4|GPT-3|"
    r"large language model|LLM|natural language processing|NLP|"
    r"automated grading|adaptive learning|conversational AI|"
    r"AI tutor|AI agent|agentic AI|neural network|"
    r"computer vision|generative AI|Copilot|Gemini|Claude|Bard|"
    r"reinforcement learning|intelligent agent|recommendation system|"
    r"predictive model|text mining|sentiment analysis|"
    r"speech recognition|virtual assistant|robot\w*"
    r")\b"
    r"|"
    r"\bAI\b",
    re.IGNORECASE,
)

EDU_PATTERN = re.compile(
    r"\b("
    r"education|student|teacher|instructor|faculty|professor|"
    r"university|college|school|classroom|pedagogy|learning|"
    r"academic|K-12|higher education|undergraduate|graduate|"
    r"curriculum|MOOC|e-learning|online learning|blended learning|"
    r"tutoring|learner|teaching|coursework|semester"
    r")\b",
    re.IGNORECASE,
)

ADOPT_PATTERN = re.compile(
    r"\b("
    r"adopt\w*|acceptance|intention|TAM|UTAUT|"
    r"technology acceptance|perceived usefulness|perceived ease|"
    r"self-efficacy|behavioral intention|trust|resistance|"
    r"usage|satisfaction|continuance|willingness|readiness|"
    r"attitude|motivation|engagement|barrier"
    r")\b",
    re.IGNORECASE,
)


def classify_tier(text: str) -> tuple[str, str]:
    """Classify a record into T1/T2/T3 and return (tier, exclude_reason)."""
    has_ai = bool(AI_PATTERN.search(text))
    if not has_ai:
        return ("T1", "E2:no_ai_terms")
    has_edu = bool(EDU_PATTERN.search(text))
    has_adopt = bool(ADOPT_PATTERN.search(text))
    if has_edu and has_adopt:
        return ("T3", "")
    if has_edu:
        return ("T2", "")  # AI + education but no adoption terms
    if has_adopt:
        return ("T2", "")  # AI + adoption but no education terms
    return ("T1", "E2+E3:ai_no_edu_no_adopt")  # AI but neither edu nor adopt


# ──────────────────────────────────────────────────────────────────────
# JSON extraction / normalization (shared)
# ──────────────────────────────────────────────────────────────────────

def try_extract_json(text: str) -> dict[str, Any]:
    text = text.strip()
    if not text:
        raise ValueError("Empty model output")
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    codeblock = re.search(r"```json\s*(\{.*?\})\s*```", text, flags=re.DOTALL)
    if codeblock:
        return json.loads(codeblock.group(1))
    obj = re.search(r"(\{.*\})", text, flags=re.DOTALL)
    if obj:
        return json.loads(obj.group(1))
    raise ValueError("No JSON object found in output")


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
    return "conflict"


def build_prompt(row: pd.Series) -> str:
    return SCREENING_PROMPT.format(
        title=str(row.get("title", "")),
        abstract=str(row.get("abstract", "")),
        keywords=str(row.get("keywords", "")),
        year=str(row.get("year", "")),
        source=str(row.get("search_source", row.get("source_database", ""))),
    )


# ──────────────────────────────────────────────────────────────────────
# Tier 1: instant keyword auto-exclude
# ──────────────────────────────────────────────────────────────────────

def tier1_auto_exclude(row: pd.Series, exclude_reason: str) -> dict[str, Any]:
    # Parse exclude codes from reason string (e.g. "E2:no_ai_terms" or "E2+E3:ai_no_edu_no_adopt")
    code_part = exclude_reason.split(":")[0] if ":" in exclude_reason else "E2"
    reason_part = exclude_reason.split(":", 1)[1] if ":" in exclude_reason else exclude_reason

    rationale_map = {
        "no_ai_terms": "T1 keyword pre-filter: no AI-related terms found in title/abstract/keywords",
        "ai_no_edu_no_adopt": "T1 keyword pre-filter: AI terms present but no education context AND no adoption/acceptance constructs",
    }
    rationale = rationale_map.get(reason_part, f"T1 keyword pre-filter: {exclude_reason}")

    # For compound codes like "E2+E3", use primary code
    primary_code = code_part.split("+")[0]

    return {
        "record_id": row["record_id"],
        "title": row.get("title", ""),
        "year": row.get("year", ""),
        "search_source": row.get("search_source", row.get("source_database", "")),
        "screen_decision_codex": "exclude",
        "screen_decision_gemini": "exclude",
        "screen_confidence_codex": 1.0,
        "screen_confidence_gemini": 1.0,
        "exclude_code_codex": primary_code,
        "exclude_code_gemini": primary_code,
        "rationale_codex": rationale,
        "rationale_gemini": rationale,
        "screen_consensus": "exclude",
        "screening_tier": f"T1_keyword({code_part})",
        "oauth_auth_method_codex": "keyword_filter",
        "oauth_auth_method_gemini": "keyword_filter",
        "human1_decision": "",
        "human2_decision": "",
        "adjudicated_final_decision": "",
        "exclude_code": "",
        "decision_rationale": "",
        "adjudicator_id": "",
    }


# ──────────────────────────────────────────────────────────────────────
# Async provider invocation
# ──────────────────────────────────────────────────────────────────────

async def invoke_provider_async(
    provider_name: str, cmd: list[str], prompt: str, timeout_s: int
) -> dict[str, Any]:
    full_cmd = [part.replace("{prompt}", prompt) for part in cmd]
    try:
        proc = await asyncio.create_subprocess_exec(
            *full_cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout_bytes, stderr_bytes = await asyncio.wait_for(
            proc.communicate(), timeout=timeout_s
        )
        stdout = stdout_bytes.decode("utf-8", errors="replace")

        if proc.returncode != 0:
            stderr = stderr_bytes.decode("utf-8", errors="replace")
            return {
                "decision": "uncertain", "confidence": 0.0,
                "exclude_code": "NA", "criteria_flags": {},
                "rationale": f"{provider_name} failed: {stderr.strip()[:200]}",
            }

        try:
            payload = try_extract_json(stdout)
        except Exception as exc:
            return {
                "decision": "uncertain", "confidence": 0.0,
                "exclude_code": "NA", "criteria_flags": {},
                "rationale": f"JSON parse error from {provider_name}: {exc}",
            }

        payload["decision"] = normalize_decision(str(payload.get("decision", "uncertain")))
        payload["confidence"] = float(payload.get("confidence", 0.0) or 0.0)
        payload["exclude_code"] = payload.get("exclude_code", "NA") or "NA"
        payload["rationale"] = str(payload.get("rationale", "")).strip()
        return payload

    except asyncio.TimeoutError:
        logger.warning("%s timed out after %ss", provider_name, timeout_s)
        return {
            "decision": "uncertain", "confidence": 0.0,
            "exclude_code": "NA", "criteria_flags": {},
            "rationale": f"{provider_name} timed out after {timeout_s}s",
        }


# ──────────────────────────────────────────────────────────────────────
# Tier 2: single AI (Gemini only — faster, 0 timeouts in pilot)
# ──────────────────────────────────────────────────────────────────────

async def tier2_single_ai(
    row: pd.Series, gemini_cmd: list[str], timeout_s: int, sem: asyncio.Semaphore,
) -> dict[str, Any]:
    async with sem:
        prompt = build_prompt(row)
        gemini_r = await invoke_provider_async("gemini", gemini_cmd, prompt, timeout_s)

        return {
            "record_id": row["record_id"],
            "title": row.get("title", ""),
            "year": row.get("year", ""),
            "search_source": row.get("search_source", row.get("source_database", "")),
            "screen_decision_codex": "N/A",
            "screen_decision_gemini": gemini_r["decision"],
            "screen_confidence_codex": 0.0,
            "screen_confidence_gemini": gemini_r["confidence"],
            "exclude_code_codex": "N/A",
            "exclude_code_gemini": gemini_r["exclude_code"],
            "rationale_codex": "T2: single-AI tier, Gemini only",
            "rationale_gemini": gemini_r["rationale"],
            "screen_consensus": gemini_r["decision"],  # single AI = its decision
            "screening_tier": "T2_single_ai",
            "oauth_auth_method_codex": "N/A",
            "oauth_auth_method_gemini": "oauth",
            "human1_decision": "",
            "human2_decision": "",
            "adjudicated_final_decision": "",
            "exclude_code": "",
            "decision_rationale": "",
            "adjudicator_id": "",
        }


# ──────────────────────────────────────────────────────────────────────
# Tier 3: dual AI (Codex + Gemini concurrent)
# ──────────────────────────────────────────────────────────────────────

async def tier3_dual_ai(
    row: pd.Series,
    codex_cmd: list[str],
    gemini_cmd: list[str],
    timeout_s: int,
    sem: asyncio.Semaphore,
) -> dict[str, Any]:
    async with sem:
        prompt = build_prompt(row)
        codex_r, gemini_r = await asyncio.gather(
            invoke_provider_async("codex", codex_cmd, prompt, timeout_s),
            invoke_provider_async("gemini", gemini_cmd, prompt, timeout_s),
        )

        return {
            "record_id": row["record_id"],
            "title": row.get("title", ""),
            "year": row.get("year", ""),
            "search_source": row.get("search_source", row.get("source_database", "")),
            "screen_decision_codex": codex_r["decision"],
            "screen_decision_gemini": gemini_r["decision"],
            "screen_confidence_codex": codex_r["confidence"],
            "screen_confidence_gemini": gemini_r["confidence"],
            "exclude_code_codex": codex_r["exclude_code"],
            "exclude_code_gemini": gemini_r["exclude_code"],
            "rationale_codex": codex_r["rationale"],
            "rationale_gemini": gemini_r["rationale"],
            "screen_consensus": consensus(codex_r["decision"], gemini_r["decision"]),
            "screening_tier": "T3_dual_ai",
            "oauth_auth_method_codex": "oauth",
            "oauth_auth_method_gemini": "oauth",
            "human1_decision": "",
            "human2_decision": "",
            "adjudicated_final_decision": "",
            "exclude_code": "",
            "decision_rationale": "",
            "adjudicator_id": "",
        }


# ──────────────────────────────────────────────────────────────────────
# Checkpoint management
# ──────────────────────────────────────────────────────────────────────

def save_checkpoint(results: list[dict], output_path: Path) -> None:
    pd.DataFrame(results).to_csv(output_path, index=False)


# ──────────────────────────────────────────────────────────────────────
# Main orchestrator
# ──────────────────────────────────────────────────────────────────────

async def run_tiered_screening(args: argparse.Namespace) -> None:
    config_path = Path(args.config)
    with open(config_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    codex_block = config.get("screening_cli", {}).get("codex", {})
    gemini_block = config.get("screening_cli", {}).get("gemini", {})
    codex_cmd = codex_block.get("screen_cmd", ["codex", "exec", "{prompt}"])
    gemini_cmd = gemini_block.get("screen_cmd", ["gemini", "-p", "{prompt}"])

    records = pd.read_csv(args.input)
    if "record_id" not in records.columns:
        records.insert(0, "record_id", range(1, len(records) + 1))

    output_path = Path(args.output)
    results: list[dict] = []

    if args.resume and output_path.exists():
        existing = pd.read_csv(output_path)
        done_ids = set(existing["record_id"].astype(str).tolist())
        records_todo = records[~records["record_id"].astype(str).isin(done_ids)].copy()
        results = existing.to_dict("records")
        logger.info("Resume: %s done, %s remaining", len(done_ids), len(records_todo))
    else:
        records_todo = records

    if len(records_todo) == 0:
        logger.info("All records already screened.")
        return

    # ── Classify tiers ──
    records_todo = records_todo.copy()
    records_todo["_text"] = (
        records_todo["title"].fillna("")
        + " " + records_todo["abstract"].fillna("")
        + " " + records_todo["keywords"].fillna("")
    )
    tier_info = records_todo["_text"].apply(classify_tier)
    records_todo["_tier"] = tier_info.apply(lambda x: x[0])
    records_todo["_exclude_reason"] = tier_info.apply(lambda x: x[1])

    t1 = records_todo[records_todo["_tier"] == "T1"]
    t2 = records_todo[records_todo["_tier"] == "T2"]
    t3 = records_todo[records_todo["_tier"] == "T3"]

    logger.info(
        "Tier distribution: T1=%s (auto-exclude), T2=%s (single AI), T3=%s (dual AI)",
        len(t1), len(t2), len(t3),
    )

    # ── Tier 1: instant ──
    t_start = time.monotonic()
    t1_results = [tier1_auto_exclude(row, row["_exclude_reason"]) for _, row in t1.iterrows()]
    results.extend(t1_results)
    t1_elapsed = time.monotonic() - t_start
    logger.info("T1 done: %s records in %.1fs", len(t1_results), t1_elapsed)
    save_checkpoint(results, output_path)
    logger.info("Checkpoint after T1: %s total rows", len(results))

    # ── Tier 2: single AI (Gemini) ──
    if len(t2) > 0:
        sem2 = asyncio.Semaphore(args.workers)
        t2_start = time.monotonic()
        t2_tasks = [
            tier2_single_ai(row, gemini_cmd, args.timeout, sem2)
            for _, row in t2.iterrows()
        ]

        completed_t2 = 0
        for coro in asyncio.as_completed(t2_tasks):
            result = await coro
            results.append(result)
            completed_t2 += 1
            if completed_t2 % args.save_every == 0:
                save_checkpoint(results, output_path)
                logger.info("T2 checkpoint: %s/%s", completed_t2, len(t2))
            if completed_t2 % 100 == 0:
                elapsed = time.monotonic() - t2_start
                rate = completed_t2 / elapsed if elapsed > 0 else 0
                logger.info("T2 progress: %s/%s (%.1f/min)", completed_t2, len(t2), rate * 60)

        t2_elapsed = time.monotonic() - t2_start
        logger.info("T2 done: %s records in %.1f min", len(t2), t2_elapsed / 60)
        save_checkpoint(results, output_path)

    # ── Tier 3: dual AI (Codex + Gemini) ──
    if len(t3) > 0:
        sem3 = asyncio.Semaphore(args.workers)
        t3_start = time.monotonic()
        t3_tasks = [
            tier3_dual_ai(row, codex_cmd, gemini_cmd, args.timeout, sem3)
            for _, row in t3.iterrows()
        ]

        completed_t3 = 0
        for coro in asyncio.as_completed(t3_tasks):
            result = await coro
            results.append(result)
            completed_t3 += 1
            if completed_t3 % args.save_every == 0:
                save_checkpoint(results, output_path)
                logger.info("T3 checkpoint: %s/%s", completed_t3, len(t3))
            if completed_t3 % 100 == 0:
                elapsed = time.monotonic() - t3_start
                rate = completed_t3 / elapsed if elapsed > 0 else 0
                remaining = (len(t3) - completed_t3) / rate if rate > 0 else 0
                logger.info(
                    "T3 progress: %s/%s (%.1f/min, ~%.0fm left)",
                    completed_t3, len(t3), rate * 60, remaining / 60,
                )

        t3_elapsed = time.monotonic() - t3_start
        logger.info("T3 done: %s records in %.1f min", len(t3), t3_elapsed / 60)

    # ── Final save ──
    save_checkpoint(results, output_path)
    total_elapsed = time.monotonic() - t_start
    logger.info(
        "ALL DONE. %s records in %.1f min. Output: %s",
        len(results), total_elapsed / 60, output_path,
    )

    # Summary
    df_out = pd.DataFrame(results)
    if "screening_tier" in df_out.columns:
        logger.info("Tier summary:\n%s", df_out["screening_tier"].value_counts().to_string())
    logger.info("Consensus summary:\n%s", df_out["screen_consensus"].value_counts().to_string())


def main() -> None:
    _default_config = str(Path(__file__).resolve().parent.parent / "ai_coding_pipeline" / "config.yaml")
    parser = argparse.ArgumentParser(description="Three-tier accelerated screening")
    parser.add_argument("input", type=str, help="Input CSV")
    parser.add_argument("output", type=str, help="Output CSV")
    parser.add_argument("--config", type=str, default=_default_config)
    parser.add_argument("--workers", type=int, default=8, help="Concurrent workers per tier")
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--save-every", type=int, default=50)
    parser.add_argument("--timeout", type=int, default=300)
    parser.add_argument("--auto-login", action="store_true")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    asyncio.run(run_tiered_screening(args))


if __name__ == "__main__":
    main()
