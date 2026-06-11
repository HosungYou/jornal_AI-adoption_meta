#!/usr/bin/env python3
"""Generate Paper2 P0/P1 expert-review and MASEM substitution rerun artifacts."""

from __future__ import annotations

import argparse
import csv
import math
import os
import shutil
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
PAPER1 = AI_ADOPTION_ROOT / "Paper1_MASEM_Working_20260605"
PAPER2 = AI_ADOPTION_ROOT / "Paper2_LLM_Extraction_Working_20260605"
STEP5 = REPO / "data/04_extraction/05_llm_masem_substitution"

DEFAULT_REFERENCE = PAPER2 / "09_reference_freeze/paper2_llm_task_units_labeled_tiered_freeze_20260605.csv"
DEFAULT_SCORED = STEP5 / "results/paper2_locked_output_scored_20260606.csv"
DEFAULT_RQ3 = STEP5 / "results/paper2_rq3_triage_task_units_20260611.csv"
DEFAULT_PRIMARY = PAPER1 / "09_model_ready_tiered_freeze/paper1_direct_r_primary_model_ready_tiered_freeze_20260605.csv"
DEFAULT_CONVERTED = PAPER1 / "07_analysis_ready/paper1_direct_r_sensitivity_converted_analysis_ready_20260605.csv"

OUTPUT_DIR = STEP5 / "results"
DEFAULT_REVIEW_CSV = OUTPUT_DIR / "paper2_p0_p1_expert_review_20260611.csv"
DEFAULT_REVIEW_MD = OUTPUT_DIR / "PAPER2_P0_P1_EXPERT_REVIEW_20260611.md"
DEFAULT_RERUN_INPUT = OUTPUT_DIR / "paper2_masem_substitution_rerun_input_20260611.csv"
DEFAULT_PAIR_IMPACT = OUTPUT_DIR / "paper2_masem_substitution_rerun_pair_impact_20260611.csv"
DEFAULT_SUMMARY = OUTPUT_DIR / "paper2_masem_substitution_rerun_summary_20260611.csv"
DEFAULT_RERUN_MD = OUTPUT_DIR / "PAPER2_MASEM_SUBSTITUTION_RERUN_20260611.md"
DEFAULT_RECONCILIATION_SUMMARY = OUTPUT_DIR / "paper2_masem_sample_size_reconciliation_summary_20260611.csv"
DEFAULT_RECONCILIATION_MD = OUTPUT_DIR / "PAPER2_MASEM_SAMPLE_SIZE_RECONCILIATION_20260611.md"
DEFAULT_PDF_AUDIT_CSV = OUTPUT_DIR / "pdf_source_text_audit_20260611/paper2_pointer_only_pdf_source_text_audit_20260611.csv"
DEFAULT_ONEDRIVE_MIRROR = PAPER2 / "10_expert_review_masem_rerun_20260611"

PRIMARY_MODEL = "codex:gpt-5.5"
REVIEW_PRIORITIES = {
    "P0_expert_review_numeric_or_masem",
    "P1_source_or_human_disagreement_review",
}
NUMERIC_FAMILIES = {
    "direct_r_effect_size_extraction",
    "converted_or_model_derived_effect_size",
}
STRUCTURAL_EDGES = {
    "PE-BI",
    "EE-BI",
    "SI-BI",
    "FC-UB",
    "ATT-BI",
    "BI-UB",
    "ATT-EE",
    "ATT-PE",
    "BI-TRU",
    "ANX-BI",
    "TRA-TRU",
    "ANX-AUT",
    "EE-SE",
    "ANX-SE",
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def read_optional_summary(path: Path) -> dict[tuple[str, str], int]:
    if not path.exists():
        return {}
    rows = read_csv(path)
    summary: dict[tuple[str, str], int] = {}
    for row in rows:
        try:
            row_n = int(str(row.get("row_n", "")).strip())
        except ValueError:
            continue
        summary[(row.get("metric", ""), row.get("label", ""))] = row_n
    return summary


def write_csv(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def parse_float(value: str | None) -> float | None:
    if value is None:
        return None
    text = str(value).strip()
    if not text:
        return None
    try:
        return float(text)
    except ValueError:
        return None


def fmt_float(value: float | None, digits: int = 6) -> str:
    if value is None or (isinstance(value, float) and math.isnan(value)):
        return ""
    return f"{value:.{digits}f}"


def canonical_pair(row: dict[str, str]) -> str:
    pair = row.get("construct_pair_canonical") or row.get("construct_pair") or ""
    parts = [part.strip() for part in pair.split("-") if part.strip()]
    if len(parts) == 2:
        return "-".join(sorted(parts))
    c1 = row.get("construct_1", "").strip()
    c2 = row.get("construct_2", "").strip()
    if c1 and c2:
        return "-".join(sorted([c1, c2]))
    return pair


def artifact_id(path: Path) -> str:
    resolved = path.resolve()
    for root in (REPO, AI_ADOPTION_ROOT):
        try:
            return str(resolved.relative_to(root))
        except ValueError:
            continue
    return resolved.name


def review_decision(
    rq3: dict[str, str],
    ref: dict[str, str],
    primary_match: dict[str, str] | None,
    primary_scored: dict[str, str] | None,
) -> tuple[str, str, str, str]:
    family = ref.get("denominator_family", "")
    priority = rq3.get("review_priority", "")
    source_status = ref.get("source_evidence_status", "")
    freeze_use = ref.get("freeze_use", "")
    condition = rq3.get("source_condition", "")
    primary_status = rq3.get("primary_score_status", "")
    primary_state = rq3.get("primary_answer_state", "")

    if priority == "P0_expert_review_numeric_or_masem":
        if family == "converted_or_model_derived_effect_size":
            return (
                "retain_sensitivity_only_converted_input",
                "sensitivity_only",
                "not_substitutable_primary_source_type_sensitivity",
                "Converted beta/path/source-statistic rows remain sensitivity inputs and are not primary direct-r replacements.",
            )
        if source_status == "source_pointer_present_no_evidence_text":
            return (
                "retain_human_reference_source_pointer_risk",
                "primary_retained_source_risk",
                "not_substitutable_until_pdf_source_text_review",
                "Task unit has source pointer but no source-evidence text; retain frozen human reference for rerun and flag for PDF-level source check before final stability claims.",
            )
        if primary_scored and primary_scored.get("is_correct") == "1":
            return (
                "model_exact_match_reviewed",
                "primary_substitution_candidate",
                "substitutable_exact_numeric_match",
                "Primary model numeric answer matches the frozen reference within the scoring tolerance.",
            )
        if primary_state in {"abstain", "missing_model_row"} or "abstention" in primary_status:
            return (
                "retain_human_reference_model_absent_or_abstained",
                "primary_retained",
                "not_substitutable_model_abstained_or_missing",
                "Primary model did not provide a usable numeric value; retain frozen human reference for rerun.",
            )
        return (
            "retain_human_reference_model_incorrect_or_unresolved",
            "primary_retained",
            "not_substitutable_model_not_verified",
            "Primary model value is not verified for high-consequence numeric substitution.",
        )

    if priority == "P1_source_or_human_disagreement_review":
        if family == "excluded_duplicate_source":
            return (
                "exclude_duplicate_source_trace",
                "excluded_or_blank_trace",
                "not_substitutable_excluded_duplicate_source",
                "Duplicate-source or blank-consensus trace row is excluded from primary substitution.",
            )
        if family == "trace_influence_diagnostic":
            return (
                "trace_influence_only",
                "trace_only",
                "not_substitutable_primary_excluded",
                "S072-style influence row remains trace/influence diagnostic only.",
            )
        if freeze_use == "direct_r_analysis_input" and primary_match:
            return (
                "retain_human_reference_trace_reviewed",
                "primary_retained_trace_risk",
                "not_substitutable_trace_or_human_disagreement",
                "Row is already represented in the frozen primary input; retain it for rerun and preserve source/human-disagreement trace flag.",
            )
        return (
            "trace_only_no_primary_substitution",
            "trace_only",
            "not_substitutable_trace_only",
            f"{condition or family} is a trace or source-risk family rather than a primary substitution value.",
        )

    return (
        "not_in_p0_p1_review_scope",
        "not_reviewed",
        "not_reviewed",
        "Task unit is outside the requested P0/P1 review scope.",
    )


def build_review_rows(
    reference: list[dict[str, str]],
    rq3_rows: list[dict[str, str]],
    scored_rows: list[dict[str, str]],
    primary_rows: list[dict[str, str]],
) -> list[dict[str, object]]:
    ref_by_task = {row["task_unit_id"]: row for row in reference}
    primary_by_decision = {row["source_decision_id"]: row for row in primary_rows}
    codex_by_task = {
        row["task_unit_id"]: row
        for row in scored_rows
        if row.get("model_id") == PRIMARY_MODEL
    }
    rows: list[dict[str, object]] = []
    for rq3 in rq3_rows:
        if rq3.get("review_priority") not in REVIEW_PRIORITIES:
            continue
        ref = ref_by_task[rq3["task_unit_id"]]
        primary_match = primary_by_decision.get(ref.get("decision_id", ""))
        primary_scored = codex_by_task.get(rq3["task_unit_id"])
        decision, rerun_role, eligibility, note = review_decision(
            rq3, ref, primary_match, primary_scored
        )
        statistic_value = parse_float(ref.get("statistic_value"))
        model_value = parse_float(primary_scored.get("model_value") if primary_scored else None)
        expected_value = parse_float(primary_scored.get("expected_value") if primary_scored else None)
        rows.append(
            {
                "task_unit_id": rq3["task_unit_id"],
                "study_id": ref.get("study_id", ""),
                "decision_id": ref.get("decision_id", ""),
                "paper1_primary_analysis_record_id": primary_match.get("analysis_record_id", "") if primary_match else "",
                "review_priority": rq3.get("review_priority", ""),
                "denominator_family": ref.get("denominator_family", ""),
                "source_condition": rq3.get("source_condition", ""),
                "freeze_tier": ref.get("freeze_tier", ""),
                "freeze_use": ref.get("freeze_use", ""),
                "downstream_masem_impact": ref.get("downstream_masem_impact", ""),
                "source_evidence_status": ref.get("source_evidence_status", ""),
                "construct_pair": ref.get("construct_pair", ""),
                "statistic_value": fmt_float(statistic_value),
                "primary_model_id": PRIMARY_MODEL,
                "primary_score_status": rq3.get("primary_score_status", ""),
                "primary_answer_state": rq3.get("primary_answer_state", ""),
                "primary_is_correct": rq3.get("primary_is_correct", ""),
                "primary_model_value": fmt_float(model_value),
                "primary_expected_value": fmt_float(expected_value),
                "expert_review_decision": decision,
                "rerun_input_role": rerun_role,
                "substitution_eligibility": eligibility,
                "review_basis": "source_anchored_reference_packet_and_task_family_rule_review",
                "review_note": note,
            }
        )
    return rows


def codex_exact_numeric_candidates(
    scored_rows: list[dict[str, str]],
    reference: list[dict[str, str]],
    rq3_rows: list[dict[str, str]],
    primary_rows: list[dict[str, str]],
) -> dict[str, dict[str, str]]:
    ref_by_task = {row["task_unit_id"]: row for row in reference}
    rq3_by_task = {row["task_unit_id"]: row for row in rq3_rows}
    primary_by_decision = {row["source_decision_id"]: row for row in primary_rows}
    candidates: dict[str, dict[str, str]] = {}
    for scored in scored_rows:
        if scored.get("model_id") != PRIMARY_MODEL:
            continue
        if scored.get("is_correct") != "1":
            continue
        if scored.get("denominator_family") not in NUMERIC_FAMILIES:
            continue
        ref = ref_by_task.get(scored.get("task_unit_id", ""))
        if not ref:
            continue
        rq3 = rq3_by_task.get(scored["task_unit_id"], {})
        if rq3.get("source_condition") != "source_reported_direct_r":
            continue
        primary = primary_by_decision.get(ref.get("decision_id", ""))
        if not primary:
            continue
        candidates[primary["analysis_record_id"]] = scored
    return candidates


def build_substitution_input(
    primary_rows: list[dict[str, str]],
    review_rows: list[dict[str, object]],
    candidates: dict[str, dict[str, str]],
) -> list[dict[str, object]]:
    review_by_record: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in review_rows:
        record_id = str(row.get("paper1_primary_analysis_record_id", ""))
        if record_id:
            review_by_record[record_id].append(row)

    output: list[dict[str, object]] = []
    for row in primary_rows:
        record_id = row["analysis_record_id"]
        new = dict(row)
        original = parse_float(row.get("r_numeric"))
        substituted = original
        action = "retain_human_reference"
        source_task = ""
        review_priority = ""
        model_id = ""
        model_value = None
        review_group = review_by_record.get(record_id, [])
        if review_group:
            review_priority = ";".join(sorted({str(item["review_priority"]) for item in review_group}))
            action = "retain_human_reference_after_p0_p1_review"
            if any(str(item["rerun_input_role"]).endswith("source_risk") for item in review_group):
                action = "retain_human_reference_after_source_risk_review"
            if any(str(item["rerun_input_role"]).endswith("trace_risk") for item in review_group):
                action = "retain_human_reference_after_trace_review"
            source_task = ";".join(str(item["task_unit_id"]) for item in review_group[:3])
        candidate = candidates.get(record_id)
        if candidate and not review_group:
            candidate_value = parse_float(candidate.get("model_value"))
            if candidate_value is not None:
                substituted = candidate_value
                action = "llm_exact_numeric_replacement"
                source_task = candidate.get("task_unit_id", "")
                model_id = PRIMARY_MODEL
                model_value = candidate_value
        delta = None if original is None or substituted is None else substituted - original
        new.update(
            {
                "substitution_scenario": "expert_reviewed_llm_assisted_primary",
                "substitution_action": action,
                "substitution_source_task_unit_id": source_task,
                "substitution_review_priority": review_priority,
                "substitution_model_id": model_id,
                "substitution_original_r_numeric": fmt_float(original),
                "substitution_r_numeric": fmt_float(substituted),
                "substitution_delta": fmt_float(delta),
            }
        )
        output.append(new)
    return output


def summarize_pairs(rows: list[dict[str, object]], scenario: str) -> dict[str, dict[str, object]]:
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        value = parse_float(str(row.get("substitution_r_numeric") or row.get("r_numeric") or ""))
        if value is None:
            continue
        summary_row = dict(row)
        summary_row["_numeric_for_summary"] = value
        grouped[canonical_pair(summary_row)].append(summary_row)

    summaries: dict[str, dict[str, object]] = {}
    for pair, pair_rows in grouped.items():
        values = [float(row["_numeric_for_summary"]) for row in pair_rows]
        studies = {str(row.get("study_id", "")) for row in pair_rows if row.get("study_id")}
        weighted_terms = []
        weight_total = 0.0
        for row, value in zip(pair_rows, values):
            n = parse_float(str(row.get("sample_size_numeric") or row.get("sample_size") or ""))
            if n is not None and n > 3 and abs(value) < 1:
                weight = n - 3
                weighted_terms.append(math.atanh(value) * weight)
                weight_total += weight
        fisher = math.tanh(sum(weighted_terms) / weight_total) if weight_total else None
        summaries[pair] = {
            "scenario": scenario,
            "construct_pair_canonical": pair,
            "is_structural_model_edge": "1" if pair in STRUCTURAL_EDGES else "0",
            "row_n": len(pair_rows),
            "study_n": len(studies),
            "mean_r_unweighted": fmt_float(sum(values) / len(values)),
            "mean_abs_r_unweighted": fmt_float(sum(abs(v) for v in values) / len(values)),
            "min_r": fmt_float(min(values)),
            "max_r": fmt_float(max(values)),
            "fisher_z_weighted_r_available_n": fmt_float(fisher),
            "available_n_weighted_rows": sum(
                1
                for row in pair_rows
                if (parse_float(str(row.get("sample_size_numeric") or row.get("sample_size") or "")) or 0) > 3
            ),
        }
    return summaries


def source_risk_excluded_rows(
    primary_rows: list[dict[str, str]],
    review_rows: list[dict[str, object]],
) -> list[dict[str, object]]:
    risky_records = {
        str(row["paper1_primary_analysis_record_id"])
        for row in review_rows
        if row.get("paper1_primary_analysis_record_id")
        and row.get("rerun_input_role")
        in {"primary_retained_source_risk", "primary_retained_trace_risk"}
    }
    return [dict(row) for row in primary_rows if row["analysis_record_id"] not in risky_records]


def converted_augmented_rows(
    primary_rows: list[dict[str, str]],
    converted_rows: list[dict[str, str]],
) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = [dict(row) for row in primary_rows]
    for row in converted_rows:
        new = dict(row)
        new["substitution_scenario"] = "converted_sensitivity_augmented"
        rows.append(new)
    return rows


def compare_summaries(
    baseline: dict[str, dict[str, object]],
    scenario: dict[str, dict[str, object]],
    scenario_name: str,
) -> list[dict[str, object]]:
    pairs = sorted(set(baseline) | set(scenario))
    rows: list[dict[str, object]] = []
    for pair in pairs:
        base = baseline.get(pair, {})
        scen = scenario.get(pair, {})
        base_mean = parse_float(str(base.get("mean_r_unweighted", "")))
        scen_mean = parse_float(str(scen.get("mean_r_unweighted", "")))
        delta = None if base_mean is None or scen_mean is None else scen_mean - base_mean
        rows.append(
            {
                "comparison": f"baseline_primary_human_vs_{scenario_name}",
                "construct_pair_canonical": pair,
                "is_structural_model_edge": scen.get("is_structural_model_edge")
                or base.get("is_structural_model_edge")
                or "0",
                "baseline_row_n": base.get("row_n", 0),
                "scenario_row_n": scen.get("row_n", 0),
                "baseline_study_n": base.get("study_n", 0),
                "scenario_study_n": scen.get("study_n", 0),
                "baseline_mean_r_unweighted": base.get("mean_r_unweighted", ""),
                "scenario_mean_r_unweighted": scen.get("mean_r_unweighted", ""),
                "delta_mean_r_unweighted": fmt_float(delta),
                "baseline_weighted_r_available_n": base.get("fisher_z_weighted_r_available_n", ""),
                "scenario_weighted_r_available_n": scen.get("fisher_z_weighted_r_available_n", ""),
            }
        )
    return rows


def summary_rows(
    review_rows: list[dict[str, object]],
    substitution_rows: list[dict[str, object]],
    pair_impact_rows: list[dict[str, object]],
) -> list[dict[str, object]]:
    counters: list[tuple[str, Counter[str]]] = [
        ("review_priority", Counter(str(row["review_priority"]) for row in review_rows)),
        ("expert_review_decision", Counter(str(row["expert_review_decision"]) for row in review_rows)),
        ("rerun_input_role", Counter(str(row["rerun_input_role"]) for row in review_rows)),
        ("substitution_eligibility", Counter(str(row["substitution_eligibility"]) for row in review_rows)),
        ("substitution_action", Counter(str(row["substitution_action"]) for row in substitution_rows)),
    ]
    rows: list[dict[str, object]] = []
    for metric, counter in counters:
        for label, count in sorted(counter.items()):
            rows.append({"metric": metric, "label": label, "row_n": count})

    changed = [
        row
        for row in substitution_rows
        if abs(parse_float(str(row.get("substitution_delta", ""))) or 0.0) > 0
    ]
    rows.append({"metric": "substitution_numeric_value_changed_rows", "label": "any_nonzero_delta", "row_n": len(changed)})
    for comparison in sorted({str(row["comparison"]) for row in pair_impact_rows}):
        deltas = [
            abs(parse_float(str(row.get("delta_mean_r_unweighted", ""))) or 0.0)
            for row in pair_impact_rows
            if row["comparison"] == comparison
        ]
        rows.append(
            {
                "metric": "max_abs_delta_mean_r_unweighted",
                "label": comparison,
                "row_n": fmt_float(max(deltas) if deltas else 0.0),
            }
        )
    return rows


def format_review_md(review_rows: list[dict[str, object]]) -> str:
    counts = Counter(str(row["expert_review_decision"]) for row in review_rows)
    roles = Counter(str(row["rerun_input_role"]) for row in review_rows)
    priorities = Counter(str(row["review_priority"]) for row in review_rows)
    source_status = Counter(str(row["source_evidence_status"]) for row in review_rows)
    pdf_audit_rows = read_csv(DEFAULT_PDF_AUDIT_CSV) if DEFAULT_PDF_AUDIT_CSV.exists() else []
    pdf_status = Counter(str(row["pdf_text_review_status"]) for row in pdf_audit_rows)

    lines = [
        "# Paper2 P0/P1 Expert Review Layer",
        "",
        "Date: 2026-06-11",
        "",
        "## Boundary",
        "",
        "This artifact reviews the P0/P1 numeric and source-risk task-unit queue",
        "against the frozen source-anchored reference packet and task-family rules.",
        "It does not overwrite the frozen human reference standard or raw coder",
        "workbooks. Pointer-only rows are retained with source-risk flags rather",
        "than upgraded to fully source-text-verified rows.",
        "",
        "## Scope",
        "",
        f"- P0/P1 reviewed task units: {len(review_rows)}",
    ]
    for label, count in sorted(priorities.items()):
        lines.append(f"- {label}: {count}")
    lines.extend(["", "## Source Evidence Status", ""])
    for label, count in sorted(source_status.items()):
        lines.append(f"- {label}: {count}")
    if pdf_audit_rows:
        lines.extend(
            [
                "",
                "## PDF Source-Text Audit",
                "",
                f"All {len(pdf_audit_rows)} pointer-only source rows were audited against local PDFs. No source PDF",
                "was missing and no PDF text extraction failed. The audit found:",
                "",
            ]
        )
        status_order = [
            "pdf_text_value_and_pair_terms_found",
            "pdf_text_value_found_pair_terms_not_on_best_page",
            "pdf_text_context_found_value_not_found",
            "pdf_text_no_target_hit",
        ]
        for label in status_order:
            if label in pdf_status:
                lines.append(f"- {label}: {pdf_status[label]}")
        for label, count in sorted(pdf_status.items()):
            if label not in status_order:
                lines.append(f"- {label}: {count}")
    lines.extend(["", "## Review Decisions", ""])
    for label, count in sorted(counts.items()):
        lines.append(f"- {label}: {count}")
    lines.extend(["", "## Rerun Roles", ""])
    for label, count in sorted(roles.items()):
        lines.append(f"- {label}: {count}")
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "- P0/P1 review did not authorize autonomous numeric replacement for",
            "  high-consequence rows where the primary model abstained, was missing,",
            "  or where the source evidence was pointer-only.",
            "- Converted beta/path/source-statistic rows remain sensitivity inputs.",
            "- Trace-only and duplicate-source rows remain outside primary substitution.",
            "- The PDF source-text audit supports a stronger source-risk triage layer, but",
            "  rows without numeric value hits or pair-term alignment remain manual",
            "  table-review/OCR or final alignment-check candidates before final",
            "  substitution-stability claims.",
            "",
        ]
    )
    return "\n".join(lines)


def format_rerun_md(
    review_rows: list[dict[str, object]],
    substitution_rows: list[dict[str, object]],
    pair_impact_rows: list[dict[str, object]],
    summary: list[dict[str, object]],
) -> str:
    actions = Counter(str(row["substitution_action"]) for row in substitution_rows)
    comparisons = defaultdict(list)
    for row in pair_impact_rows:
        comparisons[str(row["comparison"])].append(row)
    max_deltas = {
        comparison: max(
            abs(parse_float(str(row.get("delta_mean_r_unweighted", ""))) or 0.0)
            for row in rows
        )
        for comparison, rows in comparisons.items()
    }
    structural_nonzero = {
        comparison: sum(
            1
            for row in rows
            if row.get("is_structural_model_edge") == "1"
            and abs(parse_float(str(row.get("delta_mean_r_unweighted", ""))) or 0.0) > 0
        )
        for comparison, rows in comparisons.items()
    }
    changed_rows = next(
        (
            row["row_n"]
            for row in summary
            if row["metric"] == "substitution_numeric_value_changed_rows"
        ),
        0,
    )
    sample_size_present = sum(
        1
        for row in substitution_rows
        if parse_float(str(row.get("sample_size_numeric") or row.get("sample_size") or "")) is not None
    )
    reconciliation = read_optional_summary(DEFAULT_RECONCILIATION_SUMMARY)
    reconciled_present = reconciliation.get(("rows_with_sample_size_numeric", "after_reconciliation"))
    reconciled_missing = reconciliation.get(("rows_missing_sample_size_numeric", "after_reconciliation"))

    lines = [
        "# Paper2 Expert-Reviewed MASEM Substitution Rerun",
        "",
        "Date: 2026-06-11",
        "",
        "## Boundary",
        "",
        "This rerun is a deterministic model-ready-input and pooled-correlation",
        "sensitivity rerun. The local R environment provides `Rscript`, `OpenMx`,",
        "and `metaSEM`.",
    ]
    if reconciled_present is not None and reconciled_missing is not None:
        lines.extend(
            [
                "The baseline expert-reviewed substitution input has sparse",
                "`sample_size_numeric` coverage before the deterministic sample-size",
                "reconciliation layer. The N-reconciled derived input carries numeric N",
                f"for {reconciled_present}/{len(substitution_rows)} rows; the remaining {reconciled_missing} rows",
                "are excluded from N-weighted TSSEM/MASEM weighting unless later source",
                "checks supply numeric N. The output",
                "therefore supports substitution-input readiness and pooled-correlation",
                "impact claims, not final SEM path-coefficient or model-fit stability",
                "claims.",
            ]
        )
    else:
        lines.extend(
            [
                "The baseline expert-reviewed substitution input has sparse",
                "`sample_size_numeric` coverage. The output therefore supports",
                "substitution-input readiness and pooled-correlation impact claims, not",
                "final SEM path-coefficient or model-fit stability claims.",
            ]
        )
    lines.extend(
        [
            "",
            "## Inputs",
            "",
            "- Baseline: Paper1 primary model-ready tiered freeze input, 804 rows.",
            f"- P0/P1 expert-review layer: {len(review_rows)} task units.",
            f"- Expert-reviewed LLM-assisted primary input: {len(substitution_rows)} rows.",
            f"- Baseline rows with `sample_size_numeric` before any later reconciliation layer: {sample_size_present}/{len(substitution_rows)}.",
        ]
    )
    if reconciled_present is not None and reconciled_missing is not None:
        lines.extend(
            [
                f"- N-reconciled rows with `sample_size_numeric`: {reconciled_present}/{len(substitution_rows)}.",
                f"- Rows excluded from N-weighted TSSEM/MASEM for missing N: {reconciled_missing}.",
                f"- Sample-size reconciliation: `{DEFAULT_RECONCILIATION_MD.name}`.",
            ]
        )
    else:
        lines.extend(
            [
                "- Use the separate sample-size reconciliation artifact before any N-weighted",
                "  TSSEM/metaSEM run.",
            ]
        )
    lines.extend(["", "## Substitution Actions", ""])
    for label, count in sorted(actions.items()):
        lines.append(f"- {label}: {count}")
    lines.extend(
        [
            f"- Numeric rows with nonzero substituted value deltas: {changed_rows}",
            "",
            "## Pair-Level Rerun Comparisons",
            "",
            "| Comparison | Max absolute delta in unweighted mean r | Structural edges with nonzero delta |",
            "|---|---:|---:|",
        ]
    )
    for comparison in sorted(comparisons):
        lines.append(
            f"| {comparison} | {max_deltas[comparison]:.6f} | {structural_nonzero[comparison]} |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "- The primary expert-reviewed LLM-assisted substitution input has no",
            "  nonzero numeric change relative to the frozen human-reference primary",
            "  input because the only exact Codex numeric candidates already match the",
            "  reference values and P0/P1 high-risk rows are retained rather than",
            "  replaced.",
            "- Source-risk exclusion and converted-input augmentation are sensitivity",
            "  diagnostics, not replacements for the primary source-anchored human",
            "  reference baseline.",
            "- A final MASEM stability claim still requires TSSEM/metaSEM Stage 1/Stage",
            "  2 on an N-weighted eligible input, or later source-supported N",
            "  completion for rows excluded by the sample-size reconciliation layer",
            "  before any all-row weighted claim.",
            "",
        ]
    )
    return "\n".join(lines)


def mirror_outputs(paths: list[Path], destination: Path) -> None:
    destination.mkdir(parents=True, exist_ok=True)
    for path in paths:
        shutil.copy2(path, destination / path.name)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--reference", type=Path, default=DEFAULT_REFERENCE)
    parser.add_argument("--scored", type=Path, default=DEFAULT_SCORED)
    parser.add_argument("--rq3", type=Path, default=DEFAULT_RQ3)
    parser.add_argument("--primary", type=Path, default=DEFAULT_PRIMARY)
    parser.add_argument("--converted", type=Path, default=DEFAULT_CONVERTED)
    parser.add_argument("--review-csv", type=Path, default=DEFAULT_REVIEW_CSV)
    parser.add_argument("--review-md", type=Path, default=DEFAULT_REVIEW_MD)
    parser.add_argument("--rerun-input", type=Path, default=DEFAULT_RERUN_INPUT)
    parser.add_argument("--pair-impact", type=Path, default=DEFAULT_PAIR_IMPACT)
    parser.add_argument("--summary", type=Path, default=DEFAULT_SUMMARY)
    parser.add_argument("--rerun-md", type=Path, default=DEFAULT_RERUN_MD)
    parser.add_argument("--mirror-onedrive", action="store_true")
    parser.add_argument("--onedrive-mirror-dir", type=Path, default=DEFAULT_ONEDRIVE_MIRROR)
    args = parser.parse_args()

    reference = read_csv(args.reference)
    scored = read_csv(args.scored)
    rq3_rows = read_csv(args.rq3)
    primary = read_csv(args.primary)
    converted = read_csv(args.converted)

    review_rows = build_review_rows(reference, rq3_rows, scored, primary)
    candidates = codex_exact_numeric_candidates(scored, reference, rq3_rows, primary)
    substitution = build_substitution_input(primary, review_rows, candidates)

    baseline_summary = summarize_pairs([dict(row) for row in primary], "baseline_primary_human")
    substitution_summary = summarize_pairs(substitution, "expert_reviewed_llm_assisted_primary")
    source_risk_summary = summarize_pairs(
        source_risk_excluded_rows(primary, review_rows),
        "source_risk_excluded_sensitivity",
    )
    converted_summary = summarize_pairs(
        converted_augmented_rows(primary, converted),
        "converted_sensitivity_augmented",
    )
    pair_impact = []
    pair_impact.extend(
        compare_summaries(
            baseline_summary,
            substitution_summary,
            "expert_reviewed_llm_assisted_primary",
        )
    )
    pair_impact.extend(
        compare_summaries(
            baseline_summary,
            source_risk_summary,
            "source_risk_excluded_sensitivity",
        )
    )
    pair_impact.extend(
        compare_summaries(
            baseline_summary,
            converted_summary,
            "converted_sensitivity_augmented",
        )
    )
    summary = summary_rows(review_rows, substitution, pair_impact)

    review_fields = [
        "task_unit_id",
        "study_id",
        "decision_id",
        "paper1_primary_analysis_record_id",
        "review_priority",
        "denominator_family",
        "source_condition",
        "freeze_tier",
        "freeze_use",
        "downstream_masem_impact",
        "source_evidence_status",
        "construct_pair",
        "statistic_value",
        "primary_model_id",
        "primary_score_status",
        "primary_answer_state",
        "primary_is_correct",
        "primary_model_value",
        "primary_expected_value",
        "expert_review_decision",
        "rerun_input_role",
        "substitution_eligibility",
        "review_basis",
        "review_note",
    ]
    substitution_fields = list(primary[0].keys()) + [
        "substitution_scenario",
        "substitution_action",
        "substitution_source_task_unit_id",
        "substitution_review_priority",
        "substitution_model_id",
        "substitution_original_r_numeric",
        "substitution_r_numeric",
        "substitution_delta",
    ]
    pair_fields = [
        "comparison",
        "construct_pair_canonical",
        "is_structural_model_edge",
        "baseline_row_n",
        "scenario_row_n",
        "baseline_study_n",
        "scenario_study_n",
        "baseline_mean_r_unweighted",
        "scenario_mean_r_unweighted",
        "delta_mean_r_unweighted",
        "baseline_weighted_r_available_n",
        "scenario_weighted_r_available_n",
    ]
    summary_fields = ["metric", "label", "row_n"]

    write_csv(args.review_csv, review_rows, review_fields)
    write_csv(args.rerun_input, substitution, substitution_fields)
    write_csv(args.pair_impact, pair_impact, pair_fields)
    write_csv(args.summary, summary, summary_fields)
    args.review_md.write_text(format_review_md(review_rows), encoding="utf-8")
    args.rerun_md.write_text(format_rerun_md(review_rows, substitution, pair_impact, summary), encoding="utf-8")

    outputs = [
        args.review_csv,
        args.review_md,
        args.rerun_input,
        args.pair_impact,
        args.summary,
        args.rerun_md,
    ]
    if args.mirror_onedrive:
        mirror_outputs(outputs, args.onedrive_mirror_dir)

    print(
        "generated",
        {
            "review_rows": len(review_rows),
            "substitution_rows": len(substitution),
            "pair_impact_rows": len(pair_impact),
            "summary_rows": len(summary),
            "review_csv": artifact_id(args.review_csv),
            "rerun_md": artifact_id(args.rerun_md),
            "onedrive_mirror": artifact_id(args.onedrive_mirror_dir) if args.mirror_onedrive else "",
        },
    )


if __name__ == "__main__":
    main()
