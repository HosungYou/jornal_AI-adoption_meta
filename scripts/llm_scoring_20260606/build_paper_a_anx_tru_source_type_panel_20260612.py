#!/usr/bin/env python3
"""Build an ANX-TRU source-type boundary panel for Paper A."""

from __future__ import annotations

import argparse
import csv
from datetime import date
from pathlib import Path


REPO = Path(__file__).resolve().parents[2]
PREANALYSIS = REPO / "docs/07_manuscript_exemplars/20260612/pre_analysis_processing"
RESULTS = REPO / "data/04_extraction/05_llm_masem_substitution/results"

DEFAULT_TRACE = PREANALYSIS / "paper_a_anx_tru_unique_candidate_trace_20260612.csv"
DEFAULT_PANEL = RESULTS / "paper_a_anx_tru_source_type_panel_20260612.csv"
DEFAULT_REPORT = RESULTS / "PAPER_A_ANX_TRU_SOURCE_TYPE_PANEL_20260612.md"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def classify_candidate(row: dict[str, str]) -> tuple[str, str, str, str]:
    interpretation = row.get("interpretation", "")
    source_type = row.get("source_type", "")
    evidence_type = row.get("evidence_type", "")
    if "direct_r_candidate" in interpretation:
        return (
            "post_freeze_direct_r_candidate",
            "main_text_source_type_panel_primary_like_not_legacy_freeze",
            "compare_against_legacy_primary_absence",
            "Potential direct-r rescue candidate from 2026-06-09 full-corpus reference; not present in the 2026-06-05 primary direct-r freeze.",
        )
    if "latent_correlation" in interpretation or "latent" in evidence_type:
        return (
            "post_freeze_latent_correlation_candidate",
            "main_text_separate_latent_panel",
            "compare_not_pool_with_observed_direct_r",
            "Latent/Fornell-Larcker off-diagonal candidate; report separately from observed direct-r rows.",
        )
    if "converted_effect" in interpretation or "converted" in source_type or "beta" in source_type:
        return (
            "post_freeze_converted_effect_candidate",
            "main_text_converted_effect_comparison_panel",
            "compare_not_pool_with_direct_r",
            "Beta/path-converted candidate; include in same main-results space as a separate comparison panel, not as pooled primary direct-r.",
        )
    return (
        "legacy_expanded_or_sensitivity_source_statistic_candidate",
        "sensitivity_or_trace_only",
        "do_not_use_for_primary_direct_r",
        "Legacy expanded/sensitivity candidate requires source-statistic review and is not a primary direct-r row.",
    )


def md_table(rows: list[dict[str, object]], cols: list[str]) -> str:
    lines = ["| " + " | ".join(cols) + " |", "| " + " | ".join(["---"] * len(cols)) + " |"]
    for row in rows:
        lines.append("| " + " | ".join(str(row.get(col, "")) for col in cols) + " |")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--trace", type=Path, default=DEFAULT_TRACE)
    parser.add_argument("--panel-output", type=Path, default=DEFAULT_PANEL)
    parser.add_argument("--report-output", type=Path, default=DEFAULT_REPORT)
    args = parser.parse_args()

    panel_rows: list[dict[str, object]] = []
    for row in read_csv(args.trace):
        source_type_class, manuscript_role, modeling_action, rationale = classify_candidate(row)
        panel_rows.append(
            {
                "study_id": row.get("study_id", ""),
                "construct_pair": row.get("construct_pair", "ANX-TRU") or "ANX-TRU",
                "r_numeric_or_reference": row.get("r_numeric_or_reference", ""),
                "source_type_class": source_type_class,
                "source_type": row.get("source_type", ""),
                "evidence_type": row.get("evidence_type", ""),
                "denominator_family": row.get("denominator_family", ""),
                "source_location": row.get("source_location", ""),
                "source_file": row.get("file_name", ""),
                "manuscript_role": manuscript_role,
                "modeling_action": modeling_action,
                "rationale": rationale,
            }
        )

    role_counts: dict[str, int] = {}
    for row in panel_rows:
        role_counts[str(row["source_type_class"])] = role_counts.get(str(row["source_type_class"]), 0) + 1
    count_rows = [{"source_type_class": key, "rows": value} for key, value in sorted(role_counts.items())]
    write_csv(
        args.panel_output,
        panel_rows,
        [
            "study_id",
            "construct_pair",
            "r_numeric_or_reference",
            "source_type_class",
            "source_type",
            "evidence_type",
            "denominator_family",
            "source_location",
            "source_file",
            "manuscript_role",
            "modeling_action",
            "rationale",
        ],
    )

    lines = [
        "# Paper A ANX-TRU Source-Type Panel",
        "",
        f"Date: {date.today().isoformat()}",
        "",
        "## Boundary",
        "",
        "`ANX-TRU` is absent from the 2026-06-05 Paper A primary direct-r freeze,",
        "but it is not absent from the broader evidence trail. The post-freeze",
        "full-corpus reference contains source-type-specific candidates. They should",
        "be reported as a corpus/source-type boundary, not silently pooled into the",
        "legacy primary matrix.",
        "",
        "## Source-Type Counts",
        "",
        md_table(count_rows, ["source_type_class", "rows"]),
        "",
        "## Candidate Panel",
        "",
        md_table(
            panel_rows,
            [
                "study_id",
                "r_numeric_or_reference",
                "source_type_class",
                "manuscript_role",
                "modeling_action",
            ],
        ),
        "",
        "## Recommended Claim Boundary",
        "",
        "- Legacy 2026-06-05 primary direct-r model: `ANX-TRU` remains not estimable.",
        "- Revised manuscript: describe `ANX-TRU` as recoverable only through the",
        "  post-freeze full-corpus source-type panel.",
        "- Do not pool direct-r, latent, and converted-effect candidates in one primary",
        "  estimate. The comparison itself is a methodological result.",
        "",
        "## Output",
        "",
        f"- `{args.panel_output.relative_to(REPO)}`",
    ]
    args.report_output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("anx_tru_source_type_panel_complete", f"rows={len(panel_rows)}")


if __name__ == "__main__":
    main()
