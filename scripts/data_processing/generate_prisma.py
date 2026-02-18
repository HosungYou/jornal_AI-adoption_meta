#!/usr/bin/env python3
"""
Generate PRISMA 2020 counts/diagram from screening outputs.
"""

from __future__ import annotations

import argparse
import json
import logging
from pathlib import Path
from typing import Any

import pandas as pd

logger = logging.getLogger(__name__)

EXCLUDE_CODES = [f"E{i}" for i in range(1, 13)]


def counts_from_screening_csv(df: pd.DataFrame, identified_total: int, duplicates_removed: int) -> dict[str, Any]:
    screened = len(df)
    human_excluded = int((df.get("adjudicated_final_decision", "") == "exclude").sum())
    included = int((df.get("adjudicated_final_decision", "") == "include").sum())
    unresolved = screened - human_excluded - included

    conflict_count = int((df.get("screen_consensus", "") == "conflict").sum())
    codex_excludes = int((df.get("screen_decision_codex", "") == "exclude").sum())
    gemini_excludes = int((df.get("screen_decision_gemini", "") == "exclude").sum())

    exclude_code_counts = {}
    for code in EXCLUDE_CODES:
        exclude_code_counts[code] = int((df.get("exclude_code", "") == code).sum())

    return {
        "identified_records": int(identified_total),
        "duplicates_removed": int(duplicates_removed),
        "after_dedup": int(identified_total - duplicates_removed),
        "screened_title_abstract": screened,
        "ai_conflicts": conflict_count,
        "codex_excluded_candidates": codex_excludes,
        "gemini_excluded_candidates": gemini_excludes,
        "excluded_title_abstract_final": human_excluded,
        "full_text_assessed": included + unresolved,
        "included_for_extraction": included,
        "unresolved_screening": unresolved,
        "exclude_code_counts": exclude_code_counts,
    }


def render_prisma_text(counts: dict[str, Any]) -> str:
    code_lines = [
        f"{code}: {counts['exclude_code_counts'].get(code, 0):,}" for code in EXCLUDE_CODES
    ]
    code_block = "\n".join(code_lines)
    return f"""PRISMA 2020 FLOW SUMMARY
================================================================================
IDENTIFICATION
- Records identified: {counts['identified_records']:,}
- Duplicates removed: {counts['duplicates_removed']:,}
- Records after deduplication: {counts['after_dedup']:,}

TITLE/ABSTRACT SCREENING (AI + HUMAN)
- Records screened: {counts['screened_title_abstract']:,}
- Codex exclude candidates: {counts['codex_excluded_candidates']:,}
- Gemini exclude candidates: {counts['gemini_excluded_candidates']:,}
- AI disagreement/conflict records: {counts['ai_conflicts']:,}
- Final excluded after human adjudication: {counts['excluded_title_abstract_final']:,}

ELIGIBILITY / FULL-TEXT QUEUE
- Records carried forward to full-text assessment: {counts['full_text_assessed']:,}
- Included for extraction/coding: {counts['included_for_extraction']:,}
- Unresolved screening records: {counts['unresolved_screening']:,}

EXCLUSION CODES (FINAL HUMAN DECISIONS)
{code_block}
================================================================================
"""


def write_outputs(counts: dict[str, Any], output_prefix: Path) -> None:
    output_prefix.parent.mkdir(parents=True, exist_ok=True)

    counts_path = output_prefix.with_suffix(".json")
    counts_path.write_text(json.dumps(counts, indent=2), encoding="utf-8")

    text_path = output_prefix.with_suffix(".txt")
    text_path.write_text(render_prisma_text(counts), encoding="utf-8")

    rows = [
        {"Stage": "Identification", "Metric": "Records identified", "Count": counts["identified_records"]},
        {"Stage": "Identification", "Metric": "Duplicates removed", "Count": counts["duplicates_removed"]},
        {"Stage": "Identification", "Metric": "After dedup", "Count": counts["after_dedup"]},
        {"Stage": "Screening", "Metric": "Screened title/abstract", "Count": counts["screened_title_abstract"]},
        {"Stage": "Screening", "Metric": "AI conflicts", "Count": counts["ai_conflicts"]},
        {"Stage": "Screening", "Metric": "Final excluded", "Count": counts["excluded_title_abstract_final"]},
        {"Stage": "Eligibility", "Metric": "Full text assessed", "Count": counts["full_text_assessed"]},
        {"Stage": "Included", "Metric": "Included for extraction", "Count": counts["included_for_extraction"]},
    ]
    rows.extend(
        {
            "Stage": "Exclusion Codes",
            "Metric": code,
            "Count": counts["exclude_code_counts"].get(code, 0),
        }
        for code in EXCLUDE_CODES
    )
    pd.DataFrame(rows).to_csv(output_prefix.with_suffix(".csv"), index=False)

    logger.info("Wrote PRISMA outputs: %s.[json|txt|csv]", output_prefix)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate PRISMA summary from screening CSV")
    parser.add_argument("--screening-csv", type=str, required=True)
    parser.add_argument("--identified-total", type=int, required=True)
    parser.add_argument("--duplicates-removed", type=int, required=True)
    parser.add_argument("--output-prefix", type=str, default="supplementary/prisma/prisma_flow_input")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    df = pd.read_csv(args.screening_csv)
    counts = counts_from_screening_csv(
        df=df,
        identified_total=args.identified_total,
        duplicates_removed=args.duplicates_removed,
    )
    write_outputs(counts, Path(args.output_prefix))


if __name__ == "__main__":
    main()
