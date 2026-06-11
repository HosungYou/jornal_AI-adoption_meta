#!/usr/bin/env python3
"""Apply the post-freeze beta/path exception layer to full-corpus M1-R scores."""

from __future__ import annotations

import argparse
import csv
import re
from collections import Counter
from pathlib import Path


REPO = Path(__file__).resolve().parents[2]
NUMERIC_TOLERANCE = 0.005

POLICY_REFERENCE_CAVEAT = "reference_contract_caveat_no_in_place_freeze_change"
POLICY_MANUAL_REVIEW = "manual_source_reference_adjudication_required_no_in_place_freeze_change"
POLICY_NO_PATH_EVIDENCE = "exclude_until_explicit_structural_path_evidence_or_reference_correction"
POLICY_CONTRACT_AWARE = "contract_aware_converted_effect_scoring_allowed_after_layer_consumed"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def resolve_repo_path(path_text: str) -> Path:
    path = Path(path_text)
    if path.is_absolute():
        return path
    return REPO / path


def parse_numeric(value: str) -> float | None:
    match = re.search(r"[-+]?(?:\d+\.\d+|\d+|\.\d+)", str(value or ""))
    if not match:
        return None
    try:
        return float(match.group(0))
    except ValueError:
        return None


def truthy(value: str) -> bool:
    return str(value or "").strip().lower() in {"1", "true", "yes", "y"}


def manifest_output_rows(manifest: Path | None) -> dict[tuple[str, str], dict[str, str]]:
    if not manifest:
        return {}
    rows_by_key: dict[tuple[str, str], dict[str, str]] = {}
    for manifest_row in read_csv(manifest):
        if manifest_row.get("locked_status") != "locked_model_output":
            continue
        file_value = manifest_row.get("file", "").strip()
        if not file_value:
            continue
        for output_row in read_csv(resolve_repo_path(file_value)):
            key = (output_row.get("run_id", ""), output_row.get("task_unit_id", ""))
            rows_by_key.setdefault(key, output_row)
    return rows_by_key


def layer_fields(layer_row: dict[str, str]) -> dict[str, str]:
    return {
        "construct_pair": layer_row.get("construct_pair", ""),
        "exception_layer_policy": layer_row.get("exception_layer_policy", ""),
        "expected_value": layer_row.get("frozen_value", ""),
        "step5_scorer_instruction": layer_row.get("step5_scorer_instruction", ""),
    }


def raw_fields(raw_row: dict[str, str]) -> dict[str, str]:
    return {
        "raw_beta_value": raw_row.get("raw_beta_value", ""),
        "converted_effect_value": raw_row.get("converted_effect_value", ""),
        "abstained": raw_row.get("abstained", ""),
    }


def no_exception_row(scored_row: dict[str, str]) -> dict[str, object]:
    return {
        "run_id": scored_row.get("run_id", ""),
        "model_provider": scored_row.get("model_provider", ""),
        "model_id": scored_row.get("model_id", ""),
        "task_unit_id": scored_row.get("task_unit_id", ""),
        "study_id": scored_row.get("study_id", ""),
        "construct_pair": "",
        "exception_layer_policy": "",
        "generic_full_accuracy_included": "false",
        "contract_aware_beta_path_included": "false",
        "post_exception_score_status": "not_scored_no_exception_layer_record",
        "is_correct": "",
        "score_rule": "no_matching_exception_layer_record",
        "expected_value": "",
        "model_value": "",
        "absolute_error": "",
        "raw_beta_value": "",
        "converted_effect_value": "",
        "abstained": "",
        "step5_scorer_instruction": "",
    }


def exception_row(
    scored_row: dict[str, str],
    layer_row: dict[str, str],
    raw_row: dict[str, str],
) -> dict[str, object]:
    base: dict[str, object] = {
        "run_id": scored_row.get("run_id", ""),
        "model_provider": scored_row.get("model_provider", ""),
        "model_id": scored_row.get("model_id", ""),
        "task_unit_id": scored_row.get("task_unit_id", ""),
        "study_id": layer_row.get("study_id") or scored_row.get("study_id", ""),
        "generic_full_accuracy_included": "false",
        "contract_aware_beta_path_included": "false",
        "is_correct": "",
        "model_value": "",
        "absolute_error": "",
        **layer_fields(layer_row),
        **raw_fields(raw_row),
    }

    policy = layer_row.get("exception_layer_policy", "")
    if policy == POLICY_REFERENCE_CAVEAT:
        base.update(
            {
                "post_exception_score_status": "not_scored_reference_contract_caveat",
                "score_rule": "reference_contract_caveat_cold_storage",
            }
        )
        return base

    if policy == POLICY_MANUAL_REVIEW:
        base.update(
            {
                "post_exception_score_status": "not_scored_manual_source_reference_adjudication_required",
                "score_rule": "manual_adjudication_required_before_accuracy_gate",
            }
        )
        return base

    if policy == POLICY_NO_PATH_EVIDENCE:
        base.update(
            {
                "post_exception_score_status": "not_scored_no_explicit_structural_path_evidence",
                "score_rule": "explicit_structural_path_evidence_pending",
            }
        )
        return base

    if policy == POLICY_CONTRACT_AWARE:
        converted = raw_row.get("converted_effect_value", "")
        expected = layer_row.get("frozen_value", "")
        if not raw_row or raw_row.get("locked_answer_status", "") != "locked" or truthy(raw_row.get("abstained", "")):
            base.update(
                {
                    "post_exception_score_status": "not_scored_no_locked_answer",
                    "score_rule": "locked_answer_required",
                }
            )
            return base
        if not converted.strip():
            base.update(
                {
                    "post_exception_score_status": "not_scored_missing_converted_effect_value",
                    "score_rule": "converted_effect_value_required",
                }
            )
            return base

        converted_num = parse_numeric(converted)
        expected_num = parse_numeric(expected)
        if converted_num is None or expected_num is None:
            base.update(
                {
                    "post_exception_score_status": "not_scored_non_numeric_contract_value",
                    "score_rule": "numeric_contract_values_required",
                }
            )
            return base

        absolute_error = abs(converted_num - expected_num)
        base.update(
            {
                "contract_aware_beta_path_included": "true",
                "post_exception_score_status": "scored_contract_aware_converted_effect",
                "is_correct": "1" if absolute_error <= NUMERIC_TOLERANCE else "0",
                "score_rule": f"contract_aware_converted_effect_abs_error_le_{NUMERIC_TOLERANCE}",
                "model_value": converted,
                "absolute_error": f"{absolute_error:.6f}",
            }
        )
        return base

    base.update(
        {
            "post_exception_score_status": "not_scored_unknown_exception_layer_policy",
            "score_rule": "recognized_exception_layer_policy_required",
        }
    )
    return base


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True, help="Generic scored output to post-process.")
    parser.add_argument("--layer", type=Path, required=True, help="Beta/path exception-correction layer CSV.")
    parser.add_argument("--manifest", type=Path, default=None, help="Locked-output manifest for raw beta/converted fields.")
    parser.add_argument("--scored-output", type=Path, required=True)
    parser.add_argument("--summary-output", type=Path, required=True)
    args = parser.parse_args()

    scored_rows = read_csv(args.output)
    layer_by_task = {row.get("task_unit_id", ""): row for row in read_csv(args.layer) if row.get("task_unit_id")}
    raw_by_key = manifest_output_rows(args.manifest)

    output_rows: list[dict[str, object]] = []
    for scored_row in scored_rows:
        task_id = scored_row.get("task_unit_id", "")
        layer_row = layer_by_task.get(task_id)
        if not layer_row:
            output_rows.append(no_exception_row(scored_row))
            continue
        raw_row = raw_by_key.get((scored_row.get("run_id", ""), task_id), {})
        output_rows.append(exception_row(scored_row, layer_row, raw_row))

    fields = [
        "run_id",
        "model_provider",
        "model_id",
        "task_unit_id",
        "study_id",
        "construct_pair",
        "exception_layer_policy",
        "generic_full_accuracy_included",
        "contract_aware_beta_path_included",
        "post_exception_score_status",
        "is_correct",
        "score_rule",
        "expected_value",
        "model_value",
        "absolute_error",
        "raw_beta_value",
        "converted_effect_value",
        "abstained",
        "step5_scorer_instruction",
    ]
    write_csv(args.scored_output, output_rows, fields)

    status_counts = Counter(str(row["post_exception_score_status"]) for row in output_rows)
    policy_counts = Counter(str(row["exception_layer_policy"]) for row in output_rows if row["exception_layer_policy"])
    summary_rows: list[dict[str, object]] = [
        {"metric": "rows_input", "value": len(output_rows)},
        {"metric": "rows_in_exception_layer", "value": sum(1 for row in output_rows if row["exception_layer_policy"])},
        {"metric": "rows_not_in_exception_layer", "value": sum(1 for row in output_rows if not row["exception_layer_policy"])},
        {"metric": "generic_full_accuracy_included", "value": sum(1 for row in output_rows if row["generic_full_accuracy_included"] == "true")},
        {"metric": "contract_aware_beta_path_included", "value": sum(1 for row in output_rows if row["contract_aware_beta_path_included"] == "true")},
        {"metric": "contract_aware_scored", "value": status_counts["scored_contract_aware_converted_effect"]},
        {"metric": "contract_aware_correct", "value": sum(1 for row in output_rows if row["is_correct"] == "1")},
    ]
    for status, count in sorted(status_counts.items()):
        summary_rows.append({"metric": f"status:{status}", "value": count})
    for policy, count in sorted(policy_counts.items()):
        summary_rows.append({"metric": f"policy:{policy}", "value": count})
    write_csv(args.summary_output, summary_rows, ["metric", "value"])

    print(f"rows_input={len(output_rows)}")
    print(f"rows_in_exception_layer={summary_rows[1]['value']}")
    print(f"contract_aware_scored={status_counts['scored_contract_aware_converted_effect']}")
    print(args.scored_output)
    print(args.summary_output)


if __name__ == "__main__":
    main()
