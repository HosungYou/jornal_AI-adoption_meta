#!/usr/bin/env python3
"""Score the S009/S010 beta/path contract probe as a diagnostic gate."""

from __future__ import annotations

import argparse
import csv
import re
from collections import Counter
from pathlib import Path


REPO = Path(__file__).resolve().parents[2]
STEP5 = REPO / "data/04_extraction/05_llm_masem_substitution"
DEFAULT_AUDIT = STEP5 / "results/full_corpus_m1_r_beta_path_contract_review_20260611.csv"
RESULTS = STEP5 / "results"
NUMERIC_TOLERANCE = 0.005


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def normalize(value: str) -> str:
    return re.sub(r"\s+", " ", (value or "").strip().lower())


def parse_numeric(value: str) -> float | None:
    if value is None:
        return None
    match = re.search(r"[-+]?(?:\d+\.\d+|\d+|\.\d+)", str(value))
    if not match:
        return None
    try:
        return float(match.group(0))
    except ValueError:
        return None


def matches(left: float | None, right: float | None, tolerance: float) -> str:
    if left is None or right is None:
        return ""
    return "1" if abs(left - right) <= tolerance else "0"


def is_true(value: str) -> bool:
    return normalize(value) in {"1", "true", "yes", "y"}


def status_for(issue_class: str, raw_ref: str, raw_pb: str, converted_ref: str) -> tuple[str, str]:
    if issue_class == "prompt_outputs_raw_beta_but_reference_scores_converted_value":
        if raw_pb == "1" and converted_ref == "1":
            return "contract_pass_raw_and_converted", "Raw beta matches Peterson-Brown implied raw beta and converted effect matches frozen reference value."
        if raw_pb == "1":
            return "raw_recovered_conversion_missing_or_wrong", "Raw beta matches the implied source beta but the converted effect is missing or does not match the frozen value."
        return "contract_fail_or_source_ambiguity", "The probe did not recover the expected raw-beta and converted-effect contract."

    if issue_class in {
        "source_path_not_recovered_or_construct_mapping_alias_needed",
        "path_direction_overlay_reversed_relative_to_source_direction",
        "path_direction_overlay_reversed_and_source_path_not_recovered",
    }:
        if raw_ref == "1":
            return "source_directed_raw_recovered_reference_contract_caveat", "Raw source beta matches the frozen value; keep the reference-conversion caveat before full accuracy use."
        if raw_pb == "1" and converted_ref == "1":
            return "source_directed_converted_contract_recovered", "Raw beta and converted effect align with the Peterson-Brown contract."
        return "source_directed_path_still_unresolved", "The source-directed path was not recovered under the contract probe."

    if issue_class == "reference_behaves_like_raw_beta_despite_beta_converted_label":
        if raw_ref == "1":
            return "raw_recovered_reference_contract_caveat", "Raw source beta matches the frozen value but the frozen source label remains a reference-contract caveat."
        return "reference_contract_caveat_unresolved", "The row still needs source/reference QA before accuracy use."

    if issue_class in {
        "directed_value_mismatch_not_resolved_by_prompt_alias",
        "source_table_ambiguity_or_ipma_not_path_coefficient",
    }:
        if raw_ref == "1" or raw_pb == "1" or converted_ref == "1":
            return "source_value_reference_qa_required", "Some numeric component was recovered but the row remains a source/reference QA caveat."
        return "source_value_reference_qa_unresolved", "Do not use this row as an accuracy gate without source/reference QA."

    return "needs_manual_contract_review", "Issue class is outside the contract-probe scorer rules."


def score_row(output: dict[str, str], audit: dict[str, str], tolerance: float) -> dict[str, object]:
    model_raw_value = output.get("raw_beta_value", "") or output.get("model_answer", "")
    model_converted_value = output.get("converted_effect_value", "") or output.get("model_answer_normalized", "")
    raw_num = parse_numeric(model_raw_value)
    converted_num = parse_numeric(model_converted_value)
    reference_num = parse_numeric(audit.get("reference_value", ""))
    pb_raw_num = parse_numeric(audit.get("peterson_brown_implied_raw_beta_from_reference", ""))

    raw_matches_reference = matches(raw_num, reference_num, tolerance)
    raw_matches_pb = matches(raw_num, pb_raw_num, tolerance)
    converted_matches_reference = matches(converted_num, reference_num, tolerance)

    if output.get("locked_answer_status", "") and output.get("locked_answer_status") != "locked":
        status = "not_scored_no_locked_answer"
        note = "Locked output status is not locked."
    elif is_true(output.get("abstained", "")):
        status = "scored_abstention"
        note = "Abstention counts as unresolved for this diagnostic gate."
    elif raw_num is None and converted_num is None:
        status = "not_scored_no_numeric_probe_value"
        note = "No numeric raw beta or converted effect was returned."
    else:
        status, note = status_for(
            audit.get("issue_class", ""),
            raw_matches_reference,
            raw_matches_pb,
            converted_matches_reference,
        )

    return {
        "run_id": output.get("run_id", ""),
        "model_provider": output.get("model_provider", ""),
        "model_id": output.get("model_id", ""),
        "task_unit_id": output.get("task_unit_id", ""),
        "study_id": output.get("study_id", ""),
        "issue_class": audit.get("issue_class", ""),
        "abstained": output.get("abstained", ""),
        "model_raw_beta_value": model_raw_value,
        "model_converted_effect_value": model_converted_value,
        "conversion_method": output.get("conversion_method", ""),
        "reference_value": audit.get("reference_value", ""),
        "peterson_brown_implied_raw_beta_from_reference": audit.get("peterson_brown_implied_raw_beta_from_reference", ""),
        "raw_beta_matches_reference_value": raw_matches_reference,
        "raw_beta_matches_pb_implied_beta": raw_matches_pb,
        "converted_effect_matches_reference_value": converted_matches_reference,
        "contract_probe_status": status,
        "contract_probe_note": note,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True, help="Locked beta/path contract probe output CSV.")
    parser.add_argument("--audit", type=Path, default=DEFAULT_AUDIT)
    parser.add_argument("--scored-output", type=Path, default=None)
    parser.add_argument("--summary-output", type=Path, default=None)
    parser.add_argument("--tolerance", type=float, default=NUMERIC_TOLERANCE)
    args = parser.parse_args()

    audit_by_task = {row["task_unit_id"]: row for row in read_csv(args.audit)}
    scored_rows: list[dict[str, object]] = []

    for output in read_csv(args.output):
        task_id = output.get("task_unit_id", "")
        audit = audit_by_task.get(task_id)
        if not audit:
            scored_rows.append(
                {
                    "run_id": output.get("run_id", ""),
                    "model_provider": output.get("model_provider", ""),
                    "model_id": output.get("model_id", ""),
                    "task_unit_id": task_id,
                    "study_id": output.get("study_id", ""),
                    "issue_class": "",
                    "abstained": output.get("abstained", ""),
                    "model_raw_beta_value": output.get("raw_beta_value", "") or output.get("model_answer", ""),
                    "model_converted_effect_value": output.get("converted_effect_value", "") or output.get("model_answer_normalized", ""),
                    "conversion_method": output.get("conversion_method", ""),
                    "reference_value": "",
                    "peterson_brown_implied_raw_beta_from_reference": "",
                    "raw_beta_matches_reference_value": "",
                    "raw_beta_matches_pb_implied_beta": "",
                    "converted_effect_matches_reference_value": "",
                    "contract_probe_status": "not_scored_unknown_contract_probe_task",
                    "contract_probe_note": "Task is not present in the 2026-06-11 beta/path contract audit.",
                }
            )
            continue
        scored_rows.append(score_row(output, audit, args.tolerance))

    scored_output = args.scored_output or RESULTS / f"{args.output.stem}_beta_path_contract_probe_scored.csv"
    summary_output = args.summary_output or RESULTS / f"{args.output.stem}_beta_path_contract_probe_summary.csv"

    fields = [
        "run_id",
        "model_provider",
        "model_id",
        "task_unit_id",
        "study_id",
        "issue_class",
        "abstained",
        "model_raw_beta_value",
        "model_converted_effect_value",
        "conversion_method",
        "reference_value",
        "peterson_brown_implied_raw_beta_from_reference",
        "raw_beta_matches_reference_value",
        "raw_beta_matches_pb_implied_beta",
        "converted_effect_matches_reference_value",
        "contract_probe_status",
        "contract_probe_note",
    ]
    write_csv(scored_output, scored_rows, fields)

    status_counts = Counter(str(row["contract_probe_status"]) for row in scored_rows)
    summary_rows = [
        {"metric": "rows_scored", "value": str(len(scored_rows))},
        {"metric": "tolerance", "value": str(args.tolerance)},
    ]
    summary_rows.extend(
        {"metric": f"status:{status}", "value": str(count)}
        for status, count in sorted(status_counts.items())
    )
    write_csv(summary_output, summary_rows, ["metric", "value"])

    print(scored_output)
    print(summary_output)
    print(f"rows={len(scored_rows)}")


if __name__ == "__main__":
    main()
