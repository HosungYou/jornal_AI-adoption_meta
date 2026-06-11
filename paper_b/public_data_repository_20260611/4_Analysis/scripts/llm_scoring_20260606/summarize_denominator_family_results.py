#!/usr/bin/env python3
"""Summarize Paper2 locked LLM scores by denominator family.

This report intentionally avoids an overall accuracy denominator. It separates
model-specific coverage from the Codex/Claude/Gemini overlap set so model-explicit
comparisons are not distorted by different row ranges.
"""

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path


REPO = Path(__file__).resolve().parents[2]
STEP5 = REPO / "data/04_extraction/05_llm_masem_substitution"
DEFAULT_SCORED = STEP5 / "results/paper2_locked_output_scored_20260606.csv"
DEFAULT_OUTPUT_CSV = STEP5 / "results/paper2_model_explicit_denominator_family_summary_20260607.csv"
DEFAULT_OUTPUT_MD = STEP5 / "results/PAPER2_MODEL_EXPLICIT_DENOMINATOR_FAMILY_SUMMARY_20260607.md"

MODEL_EXPLICIT_IDS = {
    "codex:gpt-5.5",
    "claude:sonnet",
    "gemini:gemini-3-flash-preview",
}
SCORED_STATUSES = {"scored", "scored_abstention"}

INTERPRETATION_TIER = {
    "direct_r_effect_size_extraction": "primary_numeric_evidence",
    "converted_or_model_derived_effect_size": "source_type_sensitivity",
    "metadata_extraction": "primary_metadata_evidence",
    "eligibility_or_exclusion_decision": "review_decision",
    "construct_or_sample_mapping_decision": "review_decision",
    "statistic_type_policy_decision": "review_decision",
    "structured_human_review_decision": "review_decision",
    "absence_or_blank_consensus": "triage_or_blank_behavior",
    "source_absence_decision": "triage_or_blank_behavior",
    "human_disagreement_trace": "trace_only_not_primary_accuracy",
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def summarize(rows: list[dict[str, str]], scope: str) -> list[dict[str, object]]:
    groups: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        groups[(row["model_id"], row["denominator_family"])].append(row)

    output = []
    for (model_id, family), group_rows in sorted(groups.items()):
        scored = [row for row in group_rows if row["score_status"] in SCORED_STATUSES]
        correct = sum(1 for row in scored if row["is_correct"] == "1")
        abstentions = sum(1 for row in scored if row["score_status"] == "scored_abstention")
        output.append(
            {
                "comparison_scope": scope,
                "model_id": model_id,
                "denominator_family": family,
                "interpretation_tier": INTERPRETATION_TIER.get(family, "unclassified"),
                "row_n": len(group_rows),
                "scored_n": len(scored),
                "correct_n": correct,
                "abstention_n": abstentions,
                "accuracy": "" if not scored else f"{correct / len(scored):.6f}",
                "not_scored_n": len(group_rows) - len(scored),
            }
        )
    return output


def format_md(rows: list[dict[str, object]]) -> str:
    lines = [
        "# Paper2 Model-Explicit Denominator-Family Summary",
        "",
        "Date: 2026-06-11",
        "",
        "## Boundary",
        "",
        "This is not an overall LLM accuracy table. Paper2 task units are split by",
        "`denominator_family` and interpretation tier. Trace, blank/absence, and",
        "source-type sensitivity rows should not be collapsed into a single",
        "substitution-validity claim.",
        "",
        "## Model Coverage",
        "",
        "- `codex:gpt-5.5`: model-explicit full range `0000-7858`.",
        "- `claude:sonnet`: model-explicit full range `0000-7858`; `0000-3999`",
        "  was backfilled as Sonnet on 2026-06-11 and the legacy",
        "  default-unspecified Claude Code rows are retained only as audit",
        "  provenance.",
        "- `gemini:gemini-3-flash-preview`: model-explicit full range",
        "  `0000-7858`; `0000-7249` used Gemini CLI and the tail used Gemini API",
        "  after CLI capacity exhaustion.",
        "- `overlap_codex_gpt55_claude_sonnet_gemini3flash`: only task units",
        "  present in all three model-explicit outputs; use this for direct",
        "  model comparison.",
        "",
        "## Summary Table",
        "",
        "| Scope | Model | Family | Tier | Rows | Scored | Correct | Abstain | Accuracy | Not scored |",
        "|---|---|---|---|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            "| {comparison_scope} | {model_id} | {denominator_family} | "
            "{interpretation_tier} | {row_n} | {scored_n} | {correct_n} | "
            "{abstention_n} | {accuracy} | {not_scored_n} |".format(**row)
        )
    lines.extend(
        [
            "",
            "## Interpretation Notes",
            "",
            "- Use `direct_r_effect_size_extraction` as the cleanest primary numeric",
            "  evidence family.",
            "- Use `metadata_extraction` as a primary metadata evidence family,",
            "  but report it separately from direct-r because it uses normalized",
            "  exact-match rather than numeric tolerance scoring.",
            "- Treat `converted_or_model_derived_effect_size` as a source-type",
            "  sensitivity family, not as direct-r equivalence.",
            "- Treat `absence_or_blank_consensus`, `source_absence_decision`, and",
            "  `human_disagreement_trace` as triage/trace behavior unless a later",
            "  protocol defines a separate metric.",
            "- Current zero-heavy accuracy patterns should be interpreted against the",
            "  redacted evidence available to the model and the task-family scoring",
            "  rule, not as a standalone model-quality verdict.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scored", type=Path, default=DEFAULT_SCORED)
    parser.add_argument("--output-csv", type=Path, default=DEFAULT_OUTPUT_CSV)
    parser.add_argument("--output-md", type=Path, default=DEFAULT_OUTPUT_MD)
    args = parser.parse_args()

    all_rows = [row for row in read_csv(args.scored) if row["model_id"] in MODEL_EXPLICIT_IDS]
    task_models: dict[str, set[str]] = defaultdict(set)
    for row in all_rows:
        task_models[row["task_unit_id"]].add(row["model_id"])
    overlap_ids = {
        task_id
        for task_id, model_ids in task_models.items()
        if MODEL_EXPLICIT_IDS.issubset(model_ids)
    }

    summary_rows = []
    summary_rows.extend(summarize(all_rows, "model_explicit_available_rows"))
    summary_rows.extend(
        summarize(
            [row for row in all_rows if row["task_unit_id"] in overlap_ids],
            "overlap_codex_gpt55_claude_sonnet_gemini3flash",
        )
    )

    fields = [
        "comparison_scope",
        "model_id",
        "denominator_family",
        "interpretation_tier",
        "row_n",
        "scored_n",
        "correct_n",
        "abstention_n",
        "accuracy",
        "not_scored_n",
    ]
    write_csv(args.output_csv, summary_rows, fields)
    args.output_md.write_text(format_md(summary_rows), encoding="utf-8")
    print(f"summary_rows={len(summary_rows)}")
    print(args.output_csv)
    print(args.output_md)


if __name__ == "__main__":
    main()
