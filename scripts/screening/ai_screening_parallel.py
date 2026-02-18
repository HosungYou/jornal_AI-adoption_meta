#!/usr/bin/env python3
"""
Parallel dual-AI title/abstract screening using asyncio.

Acceleration strategy:
1. Codex + Gemini run concurrently per record (asyncio.gather)
2. Multiple records processed in parallel via semaphore (default: 4 workers)
3. Periodic checkpoint saves with thread-safe locking
"""

from __future__ import annotations

import argparse
import asyncio
import csv
import json
import logging
import re
import sys
import time
from pathlib import Path
from typing import Any

import pandas as pd
import yaml

logger = logging.getLogger(__name__)

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
        stderr = stderr_bytes.decode("utf-8", errors="replace")

        if proc.returncode != 0:
            return {
                "decision": "uncertain",
                "confidence": 0.0,
                "exclude_code": "NA",
                "criteria_flags": {},
                "rationale": f"{provider_name} failed: {stderr.strip()[:200]}",
            }

        try:
            payload = try_extract_json(stdout)
        except Exception as exc:
            return {
                "decision": "uncertain",
                "confidence": 0.0,
                "exclude_code": "NA",
                "criteria_flags": {},
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
            "decision": "uncertain",
            "confidence": 0.0,
            "exclude_code": "NA",
            "criteria_flags": {},
            "rationale": f"{provider_name} timed out after {timeout_s}s",
        }


async def screen_one_record(
    row: pd.Series,
    codex_cmd: list[str],
    gemini_cmd: list[str],
    timeout_s: int,
    semaphore: asyncio.Semaphore,
) -> dict[str, Any]:
    async with semaphore:
        prompt = build_prompt(row)
        t0 = time.monotonic()

        # Run Codex and Gemini concurrently
        codex_result, gemini_result = await asyncio.gather(
            invoke_provider_async("codex", codex_cmd, prompt, timeout_s),
            invoke_provider_async("gemini", gemini_cmd, prompt, timeout_s),
        )

        elapsed = time.monotonic() - t0
        logger.debug("%s done in %.1fs", row["record_id"], elapsed)

        return {
            "record_id": row["record_id"],
            "title": row.get("title", ""),
            "year": row.get("year", ""),
            "search_source": row.get("search_source", row.get("source_database", "")),
            "screen_decision_codex": codex_result["decision"],
            "screen_decision_gemini": gemini_result["decision"],
            "screen_confidence_codex": codex_result["confidence"],
            "screen_confidence_gemini": gemini_result["confidence"],
            "exclude_code_codex": codex_result["exclude_code"],
            "exclude_code_gemini": gemini_result["exclude_code"],
            "rationale_codex": codex_result["rationale"],
            "rationale_gemini": gemini_result["rationale"],
            "screen_consensus": consensus(codex_result["decision"], gemini_result["decision"]),
            "oauth_auth_method_codex": "oauth",
            "oauth_auth_method_gemini": "oauth",
            "human1_decision": "",
            "human2_decision": "",
            "adjudicated_final_decision": "",
            "exclude_code": "",
            "decision_rationale": "",
            "adjudicator_id": "",
        }


def save_checkpoint(results: list[dict], output_path: Path) -> None:
    pd.DataFrame(results).to_csv(output_path, index=False)
    logger.info("Checkpoint saved: %s rows", len(results))


async def run_screening(args: argparse.Namespace) -> None:
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
        todo = records[~records["record_id"].astype(str).isin(done_ids)].copy()
        results = existing.to_dict("records")
        logger.info("Resume: %s done, %s remaining", len(done_ids), len(todo))
    else:
        todo = records

    if len(todo) == 0:
        logger.info("Nothing to process. All records already screened.")
        return

    logger.info(
        "Starting parallel screening: %s records, %s workers, %ss timeout",
        len(todo), args.workers, args.timeout,
    )

    semaphore = asyncio.Semaphore(args.workers)
    completed_count = len(results)
    t_start = time.monotonic()

    tasks = []
    row_list = [row for _, row in todo.iterrows()]

    for row in row_list:
        task = asyncio.ensure_future(
            screen_one_record(row, codex_cmd, gemini_cmd, args.timeout, semaphore)
        )
        tasks.append(task)

    for i, coro in enumerate(asyncio.as_completed(tasks)):
        result = await coro
        results.append(result)
        completed_count += 1

        if completed_count % args.save_every == 0:
            save_checkpoint(results, output_path)

        if completed_count % 100 == 0:
            elapsed = time.monotonic() - t_start
            rate = (completed_count - (len(results) - len(todo))) / elapsed if elapsed > 0 else 0
            remaining = (len(todo) - (completed_count - (len(results) - len(todo)))) / rate if rate > 0 else 0
            logger.info(
                "Progress: %s/%s total (%.1f rec/min, ~%.0fh remaining)",
                completed_count, len(records), rate * 60, remaining / 3600,
            )

    save_checkpoint(results, output_path)
    elapsed = time.monotonic() - t_start
    logger.info(
        "Done. %s records in %.0f minutes (%.1f rec/min). Output: %s",
        len(results), elapsed / 60, len(todo) / (elapsed / 60) if elapsed > 0 else 0, output_path,
    )


def main() -> None:
    _default_config = str(Path(__file__).resolve().parent.parent / "ai_coding_pipeline" / "config.yaml")
    parser = argparse.ArgumentParser(description="Parallel dual-AI screening (Codex + Gemini)")
    parser.add_argument("input", type=str, help="Input CSV")
    parser.add_argument("output", type=str, help="Output CSV")
    parser.add_argument("--config", type=str, default=_default_config)
    parser.add_argument("--workers", type=int, default=4, help="Concurrent record workers (default: 4)")
    parser.add_argument("--resume", action="store_true", help="Resume from existing output")
    parser.add_argument("--save-every", type=int, default=50, help="Checkpoint interval")
    parser.add_argument("--timeout", type=int, default=300, help="Per-provider timeout (seconds)")
    parser.add_argument("--auto-login", action="store_true")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

    asyncio.run(run_screening(args))


if __name__ == "__main__":
    main()
