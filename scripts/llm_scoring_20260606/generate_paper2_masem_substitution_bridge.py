#!/usr/bin/env python3
"""Generate the Paper2-to-Paper1 MASEM substitution bridge artifact."""

from __future__ import annotations

import argparse
import csv
import os
from collections import Counter
from pathlib import Path


REPO = Path(__file__).resolve().parents[2]
AI_ADOPTION_ROOT = Path(
    os.environ.get(
        "AI_ADOPTION_META_ROOT",
        str(
            Path.home()
            / "Library/CloudStorage/OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity"
            / "AI Adoption Meta Analysis - Documents/Meta/AI Adoption"
        ),
    )
)
PAPER1 = AI_ADOPTION_ROOT / "Paper1_MASEM_Working_20260605"
PAPER2_REF = (
    AI_ADOPTION_ROOT
    / "Paper2_LLM_Extraction_Working_20260605/09_reference_freeze/"
    "paper2_llm_task_units_labeled_tiered_freeze_20260605.csv"
)
STEP5 = REPO / "data/04_extraction/05_llm_masem_substitution"
DEFAULT_RQ1 = STEP5 / "results/paper2_rq1_extraction_validity_20260611.csv"
DEFAULT_RQ3 = STEP5 / "results/paper2_rq3_triage_task_units_20260611.csv"
DEFAULT_OUTPUT_CSV = STEP5 / "results/paper2_masem_substitution_bridge_20260611.csv"
DEFAULT_OUTPUT_MD = STEP5 / "results/PAPER2_MASEM_SUBSTITUTION_BRIDGE_20260611.md"

PRIMARY_MODEL = "codex:gpt-5.5"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def count_rows(path: Path) -> int:
    return len(read_csv(path))


def artifact_id(path: Path) -> str:
    path = path.resolve()
    for root in (REPO, AI_ADOPTION_ROOT):
        try:
            return str(path.relative_to(root))
        except ValueError:
            continue
    return path.name


def rq1_codex_core(rq1_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    return [
        row
        for row in rq1_rows
        if row["comparison_scope"] == "model_explicit_available_rows"
        and row["model_id"] == PRIMARY_MODEL
        and row["denominator_family"]
        in {"direct_r_effect_size_extraction", "converted_or_model_derived_effect_size"}
    ]


def build_rows(rq1_rows: list[dict[str, str]], rq3_rows: list[dict[str, str]], reference_rows: list[dict[str, str]]) -> list[dict[str, object]]:
    analysis_ready = PAPER1 / "07_analysis_ready"
    tiered = PAPER1 / "09_model_ready_tiered_freeze"
    paper1_files = [
        (
            "paper1_pre_tier_primary_analysis_ready",
            analysis_ready / "paper1_direct_r_primary_analysis_ready_20260605.csv",
            "audit_pre_tier_primary",
            "no",
            "Pre-tiered primary direct-r file; retained for audit, not final model-ready baseline.",
        ),
        (
            "paper1_primary_model_ready_tiered_freeze",
            tiered / "paper1_direct_r_primary_model_ready_tiered_freeze_20260605.csv",
            "human_reference_baseline",
            "yes",
            "Primary human-reference MASEM baseline after tiered exclusions; use before any LLM substitution.",
        ),
        (
            "paper1_expanded_analysis_ready",
            analysis_ready / "paper1_direct_r_expanded_analysis_ready_20260605.csv",
            "human_expanded_sensitivity",
            "sensitivity_only",
            "Expanded human-consensus direct-r-form file; not the primary baseline.",
        ),
        (
            "paper1_sensitivity_converted_analysis_ready",
            analysis_ready / "paper1_direct_r_sensitivity_converted_analysis_ready_20260605.csv",
            "converted_source_type_sensitivity",
            "sensitivity_only",
            "Converted beta/path/source-statistic input; source-type sensitivity only.",
        ),
        (
            "paper1_all_sets_long",
            analysis_ready / "paper1_direct_r_all_sets_long_20260605.csv",
            "stacked_audit",
            "no",
            "Long stacked audit file containing primary, expanded, and converted sensitivity rows.",
        ),
    ]

    rows: list[dict[str, object]] = []
    for component, path, role, usable, notes in paper1_files:
        rows.append(
            {
                "bridge_component": component,
                "source_artifact": artifact_id(path),
                "role": role,
                "row_n": count_rows(path),
                "usable_for_primary_masem": usable,
                "substitution_status": "human_reference_or_sensitivity_input",
                "notes": notes,
            }
        )

    for row in rq1_codex_core(rq1_rows):
        family = row["denominator_family"]
        stratum = row["task_stratum"]
        correct = int(row["correct_n"])
        abstain = int(row["abstention_n"])
        row_n = int(row["row_n"])
        usable = "candidate_after_expert_review" if correct else "no"
        status = "not_sufficient_for_autonomous_substitution"
        if family == "direct_r_effect_size_extraction" and stratum == "source_reported_direct_r" and correct:
            status = "limited_exact_numeric_candidates_only"
        rows.append(
            {
                "bridge_component": f"paper2_codex_{family}_{stratum}",
                "source_artifact": artifact_id(DEFAULT_RQ1),
                "role": "primary_llm_numeric_substitution_candidate",
                "row_n": row_n,
                "usable_for_primary_masem": usable,
                "substitution_status": status,
                "notes": (
                    f"Codex scored_n={row['scored_n']}; correct_n={correct}; "
                    f"abstention_n={abstain}; accuracy={row['accuracy']}."
                ),
            }
        )

    priority_counts = Counter(row["review_priority"] for row in rq3_rows)
    for priority, count in sorted(priority_counts.items()):
        rows.append(
            {
                "bridge_component": f"paper2_triage_{priority}",
                "source_artifact": artifact_id(DEFAULT_RQ3),
                "role": "review_queue_for_llm_assisted_input",
                "row_n": count,
                "usable_for_primary_masem": "requires_expert_review",
                "substitution_status": "review_queue",
                "notes": "Task-unit review priority from RQ3 triage.",
            }
        )

    ref_counts = Counter(row["denominator_family"] for row in reference_rows)
    rows.append(
        {
            "bridge_component": "paper2_trace_influence_s072",
            "source_artifact": artifact_id(PAPER2_REF),
            "role": "trace_influence_diagnostic",
            "row_n": ref_counts.get("trace_influence_diagnostic", 0),
            "usable_for_primary_masem": "no",
            "substitution_status": "primary_exclusion_trace_only",
            "notes": "S072 ANX-EE r=1.0 remains excluded from primary and retained only as trace/influence diagnostic.",
        }
    )
    return rows


def format_md(rows: list[dict[str, object]], rq1_rows: list[dict[str, str]], rq3_rows: list[dict[str, str]]) -> str:
    component = {row["bridge_component"]: row for row in rows}
    codex_numeric = rq1_codex_core(rq1_rows)
    p0_count = sum(1 for row in rq3_rows if row["review_priority"] == "P0_expert_review_numeric_or_masem")
    p3_count = sum(1 for row in rq3_rows if row["review_priority"] == "P3_low_priority_after_primary_check")

    lines = [
        "# Paper2 MASEM Substitution Bridge",
        "",
        "Date: 2026-06-11",
        "",
        "## Boundary",
        "",
        "This bridge prepares the downstream substitution analysis. It does not claim",
        "that final MASEM substitution has been run, and it does not treat current",
        "LLM locked outputs as autonomous replacements for the human-reference input.",
        "",
        "## Baseline Inputs",
        "",
        "| Component | Rows | Primary MASEM use | Notes |",
        "|---|---:|---|---|",
    ]
    for key in [
        "paper1_pre_tier_primary_analysis_ready",
        "paper1_primary_model_ready_tiered_freeze",
        "paper1_expanded_analysis_ready",
        "paper1_sensitivity_converted_analysis_ready",
        "paper1_all_sets_long",
    ]:
        row = component[key]
        lines.append(
            f"| {key} | {row['row_n']} | {row['usable_for_primary_masem']} | {row['notes']} |"
        )
    lines.extend(
        [
            "",
            "## Current Codex Numeric Substitution Readiness",
            "",
            "| Family | Stratum | Rows | Correct | Abstentions | Status |",
            "|---|---|---:|---:|---:|---|",
        ]
    )
    for row in codex_numeric:
        status = "limited candidate" if int(row["correct_n"]) else "review required"
        lines.append(
            f"| {row['denominator_family']} | {row['task_stratum']} | {row['row_n']} | "
            f"{row['correct_n']} | {row['abstention_n']} | {status} |"
        )
    lines.extend(
        [
            "",
            "## Bridge Conclusion",
            "",
            f"- The human-reference baseline is the tiered Paper1 primary model-ready file with {component['paper1_primary_model_ready_tiered_freeze']['row_n']} rows.",
            f"- Current primary Codex locked outputs create {p0_count} P0 numeric/MASEM review tasks and only {p3_count} low-priority task units after the primary check.",
            "- Therefore the next empirical step is not to substitute all Codex outputs",
            "  directly. The next step is to construct an expert-reviewed",
            "  LLM-assisted input file by replacing only source-verified eligible rows,",
            "  then rerun the MASEM pipeline against the human-reference baseline.",
            "- S072 ANX-EE `r = 1.0` remains primary-excluded and may only be used as",
            "  trace/influence diagnostic.",
            "",
            "## Rerun Contract",
            "",
            "1. Fit the human-reference MASEM baseline from",
            "   `paper1_direct_r_primary_model_ready_tiered_freeze_20260605.csv`.",
            "2. Build a locked LLM-assisted substitution input only after expert review of",
            "   P0/P1 numeric and source-risk rows.",
            "3. Compare pooled correlations, Stage 2 path coefficients, indirect effects,",
            "   model-fit decisions, and substantive conclusions.",
            "4. Report converted beta/path/source-statistic rows as source-type sensitivity,",
            "   not as source-reported direct-r equivalence.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--rq1", type=Path, default=DEFAULT_RQ1)
    parser.add_argument("--rq3", type=Path, default=DEFAULT_RQ3)
    parser.add_argument("--reference", type=Path, default=PAPER2_REF)
    parser.add_argument("--output-csv", type=Path, default=DEFAULT_OUTPUT_CSV)
    parser.add_argument("--output-md", type=Path, default=DEFAULT_OUTPUT_MD)
    args = parser.parse_args()

    rq1_rows = read_csv(args.rq1)
    rq3_rows = read_csv(args.rq3)
    reference_rows = read_csv(args.reference)
    rows = build_rows(rq1_rows, rq3_rows, reference_rows)
    fields = [
        "bridge_component",
        "source_artifact",
        "role",
        "row_n",
        "usable_for_primary_masem",
        "substitution_status",
        "notes",
    ]
    write_csv(args.output_csv, rows, fields)
    args.output_md.write_text(format_md(rows, rq1_rows, rq3_rows), encoding="utf-8")
    print(f"bridge_rows={len(rows)}")
    print(args.output_csv)
    print(args.output_md)


if __name__ == "__main__":
    main()
