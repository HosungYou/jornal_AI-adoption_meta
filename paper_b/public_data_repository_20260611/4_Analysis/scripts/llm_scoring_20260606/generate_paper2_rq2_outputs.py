#!/usr/bin/env python3
"""Generate Paper2 RQ2 error taxonomy and source-condition summaries."""

from __future__ import annotations

import argparse
import csv
import os
import re
from collections import defaultdict
from pathlib import Path


REPO = Path(__file__).resolve().parents[2]
AI_ADOPTION_ROOT = Path(
    os.environ.get(
        "AI_ADOPTION_META_ROOT",
        str(
            Path.home()
            / "<PRIVATE_ONEDRIVE_SHARED_LIBRARY>"
            / "AI Adoption Meta Analysis - Documents/Meta/AI Adoption"
        ),
    )
)
DEFAULT_REFERENCE = (
    AI_ADOPTION_ROOT
    / "Paper2_LLM_Extraction_Working_20260605/09_reference_freeze/"
    "paper2_llm_task_units_labeled_tiered_freeze_20260605.csv"
)
STEP5 = REPO / "data/04_extraction/05_llm_masem_substitution"
DEFAULT_SCORED = STEP5 / "results/paper2_locked_output_scored_20260606.csv"
DEFAULT_OUTPUT_CSV = STEP5 / "results/paper2_rq2_error_taxonomy_source_conditions_20260611.csv"
DEFAULT_OUTPUT_MD = STEP5 / "results/PAPER2_RQ2_ERROR_TAXONOMY_SOURCE_CONDITIONS_20260611.md"

MODEL_ROLES = {
    "codex:gpt-5.5": "primary_prespecified_workflow",
    "gemini:gemini-3-flash-preview": "supplementary_cross_model_sensitivity",
    "claude:sonnet": "supplementary_cross_model_sensitivity",
}
SCORED_STATUSES = {"scored", "scored_abstention"}
NUMERIC_FAMILIES = {
    "direct_r_effect_size_extraction",
    "converted_or_model_derived_effect_size",
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


def normalize(value: str) -> str:
    return re.sub(r"\s+", " ", (value or "").strip().lower())


def normalize_relaxed(value: str) -> str:
    text = (value or "").strip().lower()
    text = text.replace("&", " and ")
    text = re.sub(r"[_/\-]+", " ", text)
    text = re.sub(r"[^a-z0-9.]+", " ", text)
    text = re.sub(r"\b(n a|n/a|not applicable|not reported|not available)\b", "na", text)
    return re.sub(r"\s+", " ", text).strip()


def parse_float(value: str) -> float | None:
    match = re.search(r"[-+]?(?:\d+\.\d+|\d+|\.\d+)", value or "")
    if not match:
        return None
    try:
        return float(match.group(0))
    except ValueError:
        return None


def ratio(num: int, den: int) -> str:
    return "" if den == 0 else f"{num / den:.6f}"


def source_condition(row: dict[str, str]) -> str:
    family = row.get("denominator_family", "")
    notes = normalize(row.get("reference_notes", ""))
    stat_source = normalize(row.get("statistic_source_type", ""))
    evidence_status = row.get("source_evidence_status", "") or "source_evidence_status_missing"
    if family == "direct_r_effect_size_extraction" and "source_blank" in notes:
        return "source_blank_direct_r"
    if family == "direct_r_effect_size_extraction":
        return "source_reported_direct_r"
    if family == "converted_or_model_derived_effect_size":
        return f"converted_or_source_statistic_{stat_source or 'untyped'}"
    if family == "absence_or_blank_consensus":
        return "blank_or_absence_consensus"
    if family == "human_disagreement_trace":
        return "human_disagreement_trace"
    if family == "source_absence_decision":
        return "source_absence_decision"
    if family == "not_derivable_trace":
        return "not_derivable_trace"
    if family == "excluded_duplicate_source":
        return "excluded_duplicate_source"
    return evidence_status


def task_stratum(row: dict[str, str]) -> str:
    family = row.get("denominator_family", "")
    if family == "metadata_extraction":
        field = normalize_relaxed(row.get("field_key", "")) or "metadata_unspecified"
        return f"metadata_{field.replace(' ', '_')}"
    return source_condition(row)


def error_consequence(row: dict[str, str]) -> str:
    family = row.get("denominator_family", "")
    impact = normalize(row.get("downstream_masem_impact", ""))
    if family in {"direct_r_effect_size_extraction", "converted_or_model_derived_effect_size"}:
        return "high_numeric_or_masem_input"
    if "masem" in impact:
        return "high_masem_related"
    if family in {"metadata_extraction", "construct_or_sample_mapping_decision"}:
        return "moderate_metadata_or_mapping"
    if family in {"absence_or_blank_consensus", "human_disagreement_trace", "source_absence_decision"}:
        return "triage_or_trace"
    return "review_decision"


def classify_error(row: dict[str, str]) -> str:
    family = row.get("denominator_family", "")
    status = row.get("score_status", "")
    expected = row.get("expected_value", "")
    observed = row.get("model_value", "")
    if status not in SCORED_STATUSES:
        return status or "not_scored"
    if status == "scored_abstention":
        if family == "absence_or_blank_consensus":
            return "blank_consensus_abstention"
        return "abstention_on_scorable_row"
    if row.get("is_correct") == "1":
        if family == "metadata_extraction":
            return "metadata_strict_match"
        if family in NUMERIC_FAMILIES:
            return "numeric_within_0_005"
        return "exact_or_policy_match"
    if family in NUMERIC_FAMILIES:
        expected_num = parse_float(expected)
        observed_num = parse_float(observed)
        abs_error = parse_float(row.get("absolute_error", ""))
        if expected_num is None or observed_num is None:
            return "numeric_unparseable_answer"
        if expected_num * observed_num < 0 and abs(expected_num) > 0 and abs(observed_num) > 0:
            return "numeric_sign_reversal"
        if abs_error is None:
            return "numeric_unparseable_answer"
        if abs_error <= 0.020:
            return "numeric_minor_over_0_005"
        if abs_error <= 0.050:
            return "numeric_material_0_020_to_0_050"
        return "numeric_high_priority_over_0_050"
    if family == "metadata_extraction":
        if normalize_relaxed(expected) == normalize_relaxed(observed):
            return "metadata_relaxed_match_only"
        return "metadata_mismatch"
    if family == "absence_or_blank_consensus":
        return "blank_consensus_nonblank_answer"
    if family in {"human_disagreement_trace", "source_absence_decision"}:
        return "trace_response_behavior"
    return "policy_or_label_mismatch"


def enrich_rows(scored: list[dict[str, str]], reference: dict[str, dict[str, str]]) -> list[dict[str, str]]:
    output = []
    for row in scored:
        model_id = row.get("model_id", "")
        if model_id not in MODEL_ROLES:
            continue
        ref = reference.get(row.get("task_unit_id", ""), {})
        enriched = dict(row)
        enriched.update(
            {
                "analysis_role": MODEL_ROLES[model_id],
                "reference_notes": ref.get("notes", ""),
                "field_key": ref.get("field_key", ""),
                "construct_pair": ref.get("construct_pair", ""),
                "expected_answer_type": ref.get("expected_answer_type", ""),
                "statistic_source_type": ref.get("statistic_source_type", ""),
                "source_evidence_status": ref.get("source_evidence_status", ""),
                "downstream_masem_impact": ref.get("downstream_masem_impact", ""),
            }
        )
        enriched["source_condition"] = source_condition(enriched)
        enriched["task_stratum"] = task_stratum(enriched)
        enriched["error_class"] = classify_error(enriched)
        enriched["error_consequence"] = error_consequence(enriched)
        output.append(enriched)
    return output


def summarize(rows: list[dict[str, str]], scope: str) -> list[dict[str, object]]:
    groups: dict[tuple[str, str, str, str, str, str], list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        groups[
            (
                row["model_id"],
                row["denominator_family"],
                row["task_stratum"],
                row["source_condition"],
                row["error_class"],
                row["error_consequence"],
            )
        ].append(row)

    output: list[dict[str, object]] = []
    for (model_id, family, stratum, condition, error_class, consequence), group in sorted(groups.items()):
        scored_n = sum(1 for row in group if row.get("score_status") in SCORED_STATUSES)
        incorrect_n = sum(1 for row in group if row.get("is_correct") == "0")
        correct_n = sum(1 for row in group if row.get("is_correct") == "1")
        output.append(
            {
                "comparison_scope": scope,
                "analysis_role": MODEL_ROLES[model_id],
                "model_id": model_id,
                "denominator_family": family,
                "task_stratum": stratum,
                "source_condition": condition,
                "error_class": error_class,
                "error_consequence": consequence,
                "row_n": len(group),
                "scored_n": scored_n,
                "incorrect_n": incorrect_n,
                "correct_n": correct_n,
                "incorrect_rate_within_group": ratio(incorrect_n, scored_n),
            }
        )
    return output


def aggregate_for_md(rows: list[dict[str, object]], model_id: str) -> list[dict[str, object]]:
    totals: dict[tuple[str, str, str], dict[str, object]] = {}
    for row in rows:
        if row["comparison_scope"] != "model_explicit_available_rows" or row["model_id"] != model_id:
            continue
        key = (row["denominator_family"], row["source_condition"], row["error_class"])
        if key not in totals:
            totals[key] = {
                "denominator_family": row["denominator_family"],
                "source_condition": row["source_condition"],
                "error_class": row["error_class"],
                "row_n": 0,
                "scored_n": 0,
                "incorrect_n": 0,
                "correct_n": 0,
            }
        totals[key]["row_n"] += int(row["row_n"])
        totals[key]["scored_n"] += int(row["scored_n"])
        totals[key]["incorrect_n"] += int(row["incorrect_n"])
        totals[key]["correct_n"] += int(row["correct_n"])
    out = list(totals.values())
    out.sort(key=lambda r: (-int(r["incorrect_n"]), r["denominator_family"], r["source_condition"], r["error_class"]))
    return out


def md_table(rows: list[dict[str, object]], fields: list[str], limit: int = 40) -> list[str]:
    lines = [
        "| " + " | ".join(fields) + " |",
        "|" + "|".join("---" for _ in fields) + "|",
    ]
    for row in rows[:limit]:
        lines.append("| " + " | ".join(str(row.get(field, "")) for field in fields) + " |")
    return lines


def format_md(summary_rows: list[dict[str, object]]) -> str:
    codex_errors = aggregate_for_md(summary_rows, "codex:gpt-5.5")
    overlap_errors = [
        row
        for row in summary_rows
        if row["comparison_scope"] == "overlap_codex_gpt55_claude_sonnet_gemini3flash"
        and row["error_class"] in {"abstention_on_scorable_row", "numeric_high_priority_over_0_050", "metadata_mismatch"}
    ]

    lines = [
        "# Paper2 RQ2 Error Taxonomy and Source Conditions",
        "",
        "Date: 2026-06-11",
        "",
        "## Boundary",
        "",
        "RQ2 describes error classes and source conditions. It is not a vendor",
        "ranking and not a single accuracy denominator. Codex GPT-5.5 is the",
        "primary workflow; Claude/Gemini rows are sensitivity evidence.",
        "",
        "## Primary Codex Error Classes by Source Condition",
        "",
    ]
    lines.extend(
        md_table(
            codex_errors,
            [
                "denominator_family",
                "source_condition",
                "error_class",
                "row_n",
                "scored_n",
                "incorrect_n",
                "correct_n",
            ],
            limit=60,
        )
    )
    lines.extend(["", "## Selected Three-Model Overlap Error Classes", ""])
    lines.extend(
        md_table(
            overlap_errors,
            [
                "model_id",
                "denominator_family",
                "task_stratum",
                "source_condition",
                "error_class",
                "row_n",
                "incorrect_n",
            ],
            limit=60,
        )
    )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "- The dominant RQ2 pattern is abstention on scorable rows, which should be",
            "  reported as model behavior and not treated as missing data.",
            "- `source_blank_direct_r` is retained in primary direct-r extraction but",
            "  marked as weaker source-evidence quality.",
            "- Converted beta/path/source-statistic rows are high-consequence numeric",
            "  extraction strata with source-type separation.",
            "- Trace and blank-consensus families describe review/triage behavior rather",
            "  than final evidence-content accuracy.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scored", type=Path, default=DEFAULT_SCORED)
    parser.add_argument("--reference", type=Path, default=DEFAULT_REFERENCE)
    parser.add_argument("--output-csv", type=Path, default=DEFAULT_OUTPUT_CSV)
    parser.add_argument("--output-md", type=Path, default=DEFAULT_OUTPUT_MD)
    args = parser.parse_args()

    reference = {row["task_unit_id"]: row for row in read_csv(args.reference)}
    rows = enrich_rows(read_csv(args.scored), reference)
    task_models: dict[str, set[str]] = defaultdict(set)
    for row in rows:
        task_models[row["task_unit_id"]].add(row["model_id"])
    overlap_ids = {
        task_id for task_id, models in task_models.items() if set(MODEL_ROLES).issubset(models)
    }

    summary_rows = []
    summary_rows.extend(summarize(rows, "model_explicit_available_rows"))
    summary_rows.extend(
        summarize(
            [row for row in rows if row["task_unit_id"] in overlap_ids],
            "overlap_codex_gpt55_claude_sonnet_gemini3flash",
        )
    )

    fields = [
        "comparison_scope",
        "analysis_role",
        "model_id",
        "denominator_family",
        "task_stratum",
        "source_condition",
        "error_class",
        "error_consequence",
        "row_n",
        "scored_n",
        "incorrect_n",
        "correct_n",
        "incorrect_rate_within_group",
    ]
    write_csv(args.output_csv, summary_rows, fields)
    args.output_md.write_text(format_md(summary_rows), encoding="utf-8")
    print(f"rq2_summary_rows={len(summary_rows)}")
    print(args.output_csv)
    print(args.output_md)


if __name__ == "__main__":
    main()
