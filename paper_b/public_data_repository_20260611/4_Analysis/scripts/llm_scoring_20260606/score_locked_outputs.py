#!/usr/bin/env python3
"""Score locked Paper2 LLM outputs against the tiered reference layer."""

from __future__ import annotations

import argparse
import csv
import os
import math
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
DEFAULT_MANIFEST = STEP5 / "locked_outputs/LOCKED_OUTPUT_MANIFEST_20260606.csv"
RESULTS = STEP5 / "results"

SCORABLE_PREFIX = "eligible_after_locked_llm_output"
NUMERIC_TOLERANCE = 0.005


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


def expected_value(reference: dict[str, str]) -> str:
    for key in ("statistic_value", "consensus_value", "decision_label"):
        value = reference.get(key, "")
        if value:
            return value
    return reference.get("consensus_value", "")


def score_one(reference: dict[str, str], output: dict[str, str]) -> dict[str, object]:
    eligibility = reference["scoring_eligibility"]
    if not eligibility.startswith(SCORABLE_PREFIX):
        return {
            "score_status": "not_scorable_reference_tier",
            "is_correct": "",
            "score_rule": "excluded_by_scoring_eligibility",
            "expected_value": expected_value(reference),
            "model_value": output.get("model_answer_normalized") or output.get("model_answer", ""),
            "absolute_error": "",
        }

    locked_status = output.get("locked_answer_status", "")
    model_value = output.get("model_answer_normalized") or output.get("model_answer", "")
    if locked_status != "locked":
        return {
            "score_status": "not_scored_no_locked_answer",
            "is_correct": "",
            "score_rule": "locked_answer_required",
            "expected_value": expected_value(reference),
            "model_value": model_value,
            "absolute_error": "",
        }

    if normalize(output.get("abstained", "")) in {"1", "true", "yes", "y"}:
        return {
            "score_status": "scored_abstention",
            "is_correct": "0",
            "score_rule": "abstention_counts_incorrect_for_scorable_rows",
            "expected_value": expected_value(reference),
            "model_value": model_value,
            "absolute_error": "",
        }

    if not model_value.strip():
        return {
            "score_status": "not_scored_no_locked_answer",
            "is_correct": "",
            "score_rule": "locked_answer_required",
            "expected_value": expected_value(reference),
            "model_value": model_value,
            "absolute_error": "",
        }

    expected = expected_value(reference)
    expected_num = parse_numeric(reference.get("statistic_value", "") or expected)
    model_num = parse_numeric(model_value)
    expected_type = reference.get("expected_answer_type", "")
    if expected_num is not None and model_num is not None and "numeric" in expected_type:
        absolute_error = abs(model_num - expected_num)
        return {
            "score_status": "scored",
            "is_correct": "1" if absolute_error <= NUMERIC_TOLERANCE else "0",
            "score_rule": f"numeric_abs_error_le_{NUMERIC_TOLERANCE}",
            "expected_value": expected,
            "model_value": model_value,
            "absolute_error": f"{absolute_error:.6f}",
        }

    correct = normalize(expected) == normalize(model_value)
    return {
        "score_status": "scored",
        "is_correct": "1" if correct else "0",
        "score_rule": "normalized_exact_match",
        "expected_value": expected,
        "model_value": model_value,
        "absolute_error": "",
    }


def manifest_output_files(manifest: Path) -> list[Path]:
    files = []
    if not manifest.exists():
        return files
    for row in read_csv(manifest):
        path_text = row.get("file", "")
        locked_status = row.get("locked_status", "")
        if not path_text or locked_status != "locked_model_output":
            continue
        files.append(Path(path_text))
    return files


def repo_artifact(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(REPO))
    except ValueError:
        return path.name


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--reference", type=Path, default=DEFAULT_REFERENCE)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--output-dir", type=Path, default=RESULTS)
    args = parser.parse_args()

    references = {row["task_unit_id"]: row for row in read_csv(args.reference)}
    output_files = manifest_output_files(args.manifest)
    scored_rows: list[dict[str, object]] = []

    for output_file in output_files:
        for output in read_csv(output_file):
            task_id = output.get("task_unit_id", "")
            reference = references.get(task_id)
            if not reference:
                scored_rows.append(
                    {
                        "run_id": output.get("run_id", ""),
                        "model_provider": output.get("model_provider", ""),
                        "model_id": output.get("model_id", ""),
                        "task_unit_id": task_id,
                        "study_id": output.get("study_id", ""),
                        "denominator_family": "",
                        "scoring_eligibility": "",
                        "score_status": "not_scored_unknown_task_unit_id",
                        "is_correct": "",
                        "score_rule": "task_unit_id_not_in_reference",
                        "expected_value": "",
                        "model_value": output.get("model_answer_normalized") or output.get("model_answer", ""),
                        "absolute_error": "",
                    }
                )
                continue
            score = score_one(reference, output)
            scored_rows.append(
                {
                    "run_id": output.get("run_id", ""),
                    "model_provider": output.get("model_provider", ""),
                    "model_id": output.get("model_id", ""),
                    "task_unit_id": task_id,
                    "study_id": reference.get("study_id", ""),
                    "denominator_family": reference["denominator_family"],
                    "scoring_eligibility": reference["scoring_eligibility"],
                    **score,
                }
            )

    args.output_dir.mkdir(parents=True, exist_ok=True)
    scored_path = args.output_dir / "paper2_locked_output_scored_20260606.csv"
    summary_path = args.output_dir / "paper2_locked_output_score_summary_20260606.csv"
    status_path = args.output_dir / "SCORING_STATUS_20260606.md"

    scored_fields = [
        "run_id",
        "model_provider",
        "model_id",
        "task_unit_id",
        "study_id",
        "denominator_family",
        "scoring_eligibility",
        "score_status",
        "is_correct",
        "score_rule",
        "expected_value",
        "model_value",
        "absolute_error",
    ]
    write_csv(scored_path, scored_rows, scored_fields)

    groups: dict[tuple[str, str, str, str], list[dict[str, object]]] = defaultdict(list)
    for row in scored_rows:
        groups[
            (
                str(row["run_id"]),
                str(row["model_provider"]),
                str(row["model_id"]),
                str(row["denominator_family"]),
            )
        ].append(row)

    summary_rows = []
    for (run_id, provider, model_id, family), rows in sorted(groups.items()):
        scored = [row for row in rows if row["score_status"] in {"scored", "scored_abstention"}]
        correct = sum(1 for row in scored if row["is_correct"] == "1")
        summary_rows.append(
            {
                "run_id": run_id,
                "model_provider": provider,
                "model_id": model_id,
                "denominator_family": family,
                "scored_n": len(scored),
                "correct_n": correct,
                "accuracy": "" if not scored else f"{correct / len(scored):.6f}",
                "not_scored_n": len(rows) - len(scored),
            }
        )
    write_csv(
        summary_path,
        summary_rows,
        [
            "run_id",
            "model_provider",
            "model_id",
            "denominator_family",
            "scored_n",
            "correct_n",
            "accuracy",
            "not_scored_n",
        ],
    )

    reference_counts = Counter(row["scoring_eligibility"] for row in references.values())
    locked_count = len(output_files)
    scored_count = sum(1 for row in scored_rows if row["score_status"] in {"scored", "scored_abstention"})
    status = "blocked_no_locked_model_outputs" if locked_count == 0 else "scored_locked_outputs"
    status_path.write_text(
        "\n".join(
            [
                "# Paper2 Locked Output Scoring Status",
                "",
                "Date: 2026-06-11",
                "",
                f"Status: `{status}`",
                "",
                f"- Reference task units: {len(references)}",
                f"- Locked output files in manifest: {locked_count}",
                f"- Row-level output rows: {len(scored_rows)}",
                f"- Scored rows: {scored_count}",
                f"- Scored output: `{repo_artifact(scored_path)}`",
                f"- Summary output: `{repo_artifact(summary_path)}`",
                "",
                "## Boundary",
                "",
                "Do not report final LLM accuracy or MASEM substitution claims unless locked output files are listed with `locked_status=locked_model_output` in the manifest and scored by denominator family.",
                "",
                "## Reference scoring eligibility counts",
                "",
                *[f"- {key}: {value}" for key, value in sorted(reference_counts.items())],
                "",
            ]
        ),
        encoding="utf-8",
    )

    print(f"status={status}")
    print(f"locked_output_files={locked_count}")
    print(f"scored_rows={scored_count}")
    print(scored_path)
    print(summary_path)
    print(status_path)


if __name__ == "__main__":
    main()
