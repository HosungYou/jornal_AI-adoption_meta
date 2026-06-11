#!/usr/bin/env python3
"""Generate Paper2 RQ3 human-review triage and cross-model sensitivity outputs."""

from __future__ import annotations

import argparse
import csv
import os
import re
from collections import Counter, defaultdict
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
DEFAULT_REFERENCE = (
    AI_ADOPTION_ROOT
    / "Paper2_LLM_Extraction_Working_20260605/09_reference_freeze/"
    "paper2_llm_task_units_labeled_tiered_freeze_20260605.csv"
)
STEP5 = REPO / "data/04_extraction/05_llm_masem_substitution"
DEFAULT_SCORED = STEP5 / "results/paper2_locked_output_scored_20260606.csv"
DEFAULT_TASK_OUTPUT = STEP5 / "results/paper2_rq3_triage_task_units_20260611.csv"
DEFAULT_SUMMARY_OUTPUT = STEP5 / "results/paper2_rq3_triage_summary_20260611.csv"
DEFAULT_OUTPUT_MD = STEP5 / "results/PAPER2_RQ3_TRIAGE_CROSS_MODEL_SENSITIVITY_20260611.md"

MODEL_IDS = {
    "codex:gpt-5.5",
    "gemini:gemini-3-flash-preview",
    "claude:sonnet",
}
PRIMARY_MODEL = "codex:gpt-5.5"
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


def normalize_answer(value: str) -> str:
    text = normalize(value)
    text = text.replace("&", " and ")
    text = re.sub(r"[_/\-]+", " ", text)
    text = re.sub(r"[^a-z0-9.+-]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def source_condition(ref: dict[str, str]) -> str:
    family = ref.get("denominator_family", "")
    notes = normalize(ref.get("notes", ""))
    stat_source = normalize(ref.get("statistic_source_type", ""))
    evidence_status = ref.get("source_evidence_status", "") or "source_evidence_status_missing"
    if evidence_status == "source_pointer_present_no_evidence_text":
        if family == "direct_r_effect_size_extraction":
            return "source_pointer_only_direct_r"
        if family == "converted_or_model_derived_effect_size":
            return f"source_pointer_only_converted_or_source_statistic_{stat_source or 'untyped'}"
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
    if family == "trace_influence_diagnostic":
        return "trace_influence_diagnostic"
    return evidence_status


def answer_state(row: dict[str, str] | None) -> str:
    if row is None:
        return "missing_model_row"
    if row.get("score_status") == "scored_abstention":
        return "abstain"
    if row.get("score_status", "").startswith("not_scored"):
        return row.get("score_status") or "not_scored"
    answer = normalize_answer(row.get("model_value", ""))
    return answer or "blank_answer"


def status_for(row: dict[str, str] | None, key: str) -> str:
    if row is None:
        return ""
    return row.get(key, "")


def signals_for(
    ref: dict[str, str],
    by_model: dict[str, dict[str, str]],
    answer_states: dict[str, str],
    disagreement: bool,
) -> list[str]:
    family = ref.get("denominator_family", "")
    condition = source_condition(ref)
    evidence_status = ref.get("source_evidence_status", "")
    primary = by_model.get(PRIMARY_MODEL)
    signals: list[str] = []
    if not by_model:
        signals.append("reference_only_no_locked_model_row")
    if family in NUMERIC_FAMILIES:
        signals.append("high_consequence_numeric")
    if evidence_status == "source_pointer_present_no_evidence_text":
        signals.append("source_pointer_only_no_evidence_text")
    if condition in {
        "source_blank_direct_r",
        "source_absence_decision",
        "human_disagreement_trace",
        "trace_influence_diagnostic",
        "not_derivable_trace",
        "excluded_duplicate_source",
    } or condition.startswith("converted_or_source_statistic_"):
        signals.append("source_or_trace_risk")
    if condition.startswith("source_pointer_only_"):
        signals.append("source_or_trace_risk")
    if family == "absence_or_blank_consensus":
        signals.append("blank_behavior_family")
    if family == "human_disagreement_trace":
        signals.append("human_disagreement_trace")
    if primary is None:
        signals.append("primary_missing_model_row")
    else:
        if primary.get("score_status") == "scored_abstention":
            signals.append("primary_abstention")
        if primary.get("is_correct") == "0":
            signals.append("primary_incorrect")
        if primary.get("score_status", "").startswith("not_scored"):
            signals.append("primary_not_scored")
    if disagreement:
        signals.append("cross_model_behavior_disagreement")
    if by_model and len(set(answer_states.values())) == 1 and answer_states:
        only = next(iter(answer_states.values()))
        if only == "abstain":
            signals.append("all_available_models_abstained")
    return sorted(set(signals))


def review_priority(family: str, signals: list[str]) -> str:
    signal_set = set(signals)
    if family == "absence_or_blank_consensus":
        return "P2_blank_behavior_audit"
    if "high_consequence_numeric" in signal_set and (
        "primary_incorrect" in signal_set
        or "primary_abstention" in signal_set
        or "primary_missing_model_row" in signal_set
        or "source_or_trace_risk" in signal_set
    ):
        return "P0_expert_review_numeric_or_masem"
    if "source_or_trace_risk" in signal_set or "human_disagreement_trace" in signal_set:
        return "P1_source_or_human_disagreement_review"
    if "cross_model_behavior_disagreement" in signal_set or "primary_incorrect" in signal_set:
        return "P1_review_signal"
    if family == "absence_or_blank_consensus":
        return "P2_blank_behavior_audit"
    if "primary_not_scored" in signal_set or "primary_missing_model_row" in signal_set:
        return "P2_scoring_completeness_check"
    return "P3_low_priority_after_primary_check"


def build_task_rows(scored: list[dict[str, str]], reference: dict[str, dict[str, str]]) -> list[dict[str, object]]:
    grouped: dict[str, dict[str, dict[str, str]]] = defaultdict(dict)
    for row in scored:
        model_id = row.get("model_id", "")
        if model_id in MODEL_IDS:
            grouped[row["task_unit_id"]][model_id] = row

    task_rows: list[dict[str, object]] = []
    for task_id, ref in sorted(reference.items()):
        by_model = grouped.get(task_id, {})
        answer_states = {model: answer_state(row) for model, row in by_model.items()}
        disagreement = len(set(answer_states.values())) > 1
        signals = signals_for(ref, by_model, answer_states, disagreement)
        family = ref.get("denominator_family", "")
        priority = review_priority(family, signals)
        correct_models = sorted(model for model, row in by_model.items() if row.get("is_correct") == "1")
        abstaining_models = sorted(model for model, row in by_model.items() if row.get("score_status") == "scored_abstention")
        incorrect_models = sorted(model for model, row in by_model.items() if row.get("is_correct") == "0")
        primary = by_model.get(PRIMARY_MODEL)
        primary_score_status = (
            status_for(primary, "score_status") if primary else "reference_only_no_locked_model_row"
        )
        primary_is_correct = status_for(primary, "is_correct") if primary else ""
        primary_answer_state = answer_state(primary)
        task_rows.append(
            {
                "task_unit_id": task_id,
                "study_id": ref.get("study_id", ""),
                "denominator_family": family,
                "source_condition": source_condition(ref),
                "field_key": ref.get("field_key", ""),
                "construct_pair": ref.get("construct_pair", ""),
                "expected_answer_type": ref.get("expected_answer_type", ""),
                "available_model_count": len(by_model),
                "available_models": ";".join(sorted(by_model)),
                "model_coverage_status": "locked_model_row_available" if by_model else "reference_only_no_locked_model_row",
                "answer_state_count": len(set(answer_states.values())),
                "cross_model_behavior_disagreement": "1" if disagreement else "0",
                "correct_models": ";".join(correct_models),
                "incorrect_models": ";".join(incorrect_models),
                "abstaining_models": ";".join(abstaining_models),
                "primary_score_status": primary_score_status,
                "primary_is_correct": primary_is_correct,
                "primary_answer_state": primary_answer_state,
                "review_priority": priority,
                "triage_signals": ";".join(signals),
            }
        )
    return task_rows


def summarize(task_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    groups: dict[tuple[str, str, str, str], list[dict[str, object]]] = defaultdict(list)
    for row in task_rows:
        available_models = set(str(row["available_models"]).split(";")) if row["available_models"] else set()
        if not available_models:
            scope = "reference_only_no_locked_model_row"
        elif available_models == MODEL_IDS:
            scope = "three_model_overlap"
        elif available_models == {"codex:gpt-5.5", "gemini:gemini-3-flash-preview"}:
            scope = "two_model_codex_gemini_nonoverlap"
        else:
            scope = "partial_model_coverage"
        groups[
            (
                scope,
                str(row["review_priority"]),
                str(row["denominator_family"]),
                str(row["source_condition"]),
            )
        ].append(row)

    output: list[dict[str, object]] = []
    for (scope, priority, family, condition), rows in sorted(groups.items()):
        disagreement_n = sum(int(row["cross_model_behavior_disagreement"]) for row in rows)
        primary_incorrect_n = sum(1 for row in rows if row["primary_is_correct"] == "0")
        primary_abstention_n = sum(1 for row in rows if row["primary_score_status"] == "scored_abstention")
        primary_missing_n = sum(
            1 for row in rows if row["primary_score_status"] == "reference_only_no_locked_model_row"
        )
        all_available_abstained_n = sum(
            1
            for row in rows
            if row["available_models"]
            and set(str(row["abstaining_models"]).split(";")) == set(str(row["available_models"]).split(";"))
        )
        output.append(
            {
                "comparison_scope": scope,
                "review_priority": priority,
                "denominator_family": family,
                "source_condition": condition,
                "task_n": len(rows),
                "cross_model_behavior_disagreement_n": disagreement_n,
                "primary_incorrect_n": primary_incorrect_n,
                "primary_abstention_n": primary_abstention_n,
                "primary_missing_model_row_n": primary_missing_n,
                "all_available_models_abstained_n": all_available_abstained_n,
            }
        )
    return output


def md_table(rows: list[dict[str, object]], fields: list[str], limit: int = 50) -> list[str]:
    lines = [
        "| " + " | ".join(fields) + " |",
        "|" + "|".join("---" for _ in fields) + "|",
    ]
    for row in rows[:limit]:
        lines.append("| " + " | ".join(str(row.get(field, "")) for field in fields) + " |")
    return lines


def format_md(task_rows: list[dict[str, object]], summary_rows: list[dict[str, object]]) -> str:
    priority_counts = Counter(row["review_priority"] for row in task_rows)
    signal_counts: Counter[str] = Counter()
    for row in task_rows:
        for signal in str(row["triage_signals"]).split(";"):
            if signal:
                signal_counts[signal] += 1
    top_summary = sorted(summary_rows, key=lambda r: (-int(r["task_n"]), r["review_priority"]))

    lines = [
        "# Paper2 RQ3 Human-Review Triage and Cross-Model Sensitivity",
        "",
        "Date: 2026-06-11",
        "",
        "## Boundary",
        "",
        "RQ3 starts from the full 8,783 task-unit reference universe and left-joins",
        "locked model rows where available. Model behavior is used as",
        "review-prioritization evidence. It does not",
        "rank vendors. Cross-model disagreement is a supplementary triage signal",
        "for identifying task units that need expert review.",
        "",
        "## Priority Counts",
        "",
        "| Review priority | Task units |",
        "|---|---:|",
    ]
    for priority, count in priority_counts.most_common():
        lines.append(f"| {priority} | {count} |")
    lines.extend(["", "## Signal Counts", "", "| Signal | Task units |", "|---|---:|"])
    for signal, count in signal_counts.most_common():
        lines.append(f"| {signal} | {count} |")
    lines.extend(["", "## Summary by Priority, Family, and Source Condition", ""])
    lines.extend(
        md_table(
            top_summary,
            [
                "comparison_scope",
                "review_priority",
                "denominator_family",
                "source_condition",
                "task_n",
                "cross_model_behavior_disagreement_n",
                "primary_incorrect_n",
                "primary_abstention_n",
                "primary_missing_model_row_n",
                "all_available_models_abstained_n",
            ],
            limit=70,
        )
    )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "- P0 rows are high-consequence numeric or downstream MASEM rows where the",
            "  primary workflow abstained, was incorrect, or the source condition itself",
            "  requires expert review.",
            "- P1 rows include source-risk, human-disagreement, or cross-model behavior",
            "  disagreement signals.",
            "- P2 blank-behavior rows are split from generic P1 review signals because",
            "  they describe triage behavior, not final evidence-content accuracy.",
            "- Reference-only rows without locked model output remain in the task-unit",
            "  universe and are marked as model-coverage gaps rather than dropped.",
            "- Cross-model disagreement is used only to prioritize review load; it is not",
            "  a model or vendor ranking.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scored", type=Path, default=DEFAULT_SCORED)
    parser.add_argument("--reference", type=Path, default=DEFAULT_REFERENCE)
    parser.add_argument("--task-output", type=Path, default=DEFAULT_TASK_OUTPUT)
    parser.add_argument("--summary-output", type=Path, default=DEFAULT_SUMMARY_OUTPUT)
    parser.add_argument("--output-md", type=Path, default=DEFAULT_OUTPUT_MD)
    args = parser.parse_args()

    reference = {row["task_unit_id"]: row for row in read_csv(args.reference)}
    task_rows = build_task_rows(read_csv(args.scored), reference)
    summary_rows = summarize(task_rows)

    task_fields = [
        "task_unit_id",
        "study_id",
        "denominator_family",
        "source_condition",
        "field_key",
        "construct_pair",
        "expected_answer_type",
        "available_model_count",
        "available_models",
        "model_coverage_status",
        "answer_state_count",
        "cross_model_behavior_disagreement",
        "correct_models",
        "incorrect_models",
        "abstaining_models",
        "primary_score_status",
        "primary_is_correct",
        "primary_answer_state",
        "review_priority",
        "triage_signals",
    ]
    summary_fields = [
        "comparison_scope",
        "review_priority",
        "denominator_family",
        "source_condition",
        "task_n",
        "cross_model_behavior_disagreement_n",
        "primary_incorrect_n",
        "primary_abstention_n",
        "primary_missing_model_row_n",
        "all_available_models_abstained_n",
    ]
    write_csv(args.task_output, task_rows, task_fields)
    write_csv(args.summary_output, summary_rows, summary_fields)
    args.output_md.write_text(format_md(task_rows, summary_rows), encoding="utf-8")
    print(f"rq3_task_rows={len(task_rows)}")
    print(f"rq3_summary_rows={len(summary_rows)}")
    print(args.task_output)
    print(args.summary_output)
    print(args.output_md)


if __name__ == "__main__":
    main()
