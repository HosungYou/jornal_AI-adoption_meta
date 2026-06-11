#!/usr/bin/env python3
"""Run full-corpus M1-R scoring and apply the beta/path exception layer."""

from __future__ import annotations

import argparse
import csv
import re
import subprocess
from pathlib import Path
import shutil
from tempfile import NamedTemporaryFile

REPO = Path(__file__).resolve().parents[2]
STEP5 = REPO / "data/04_extraction/05_llm_masem_substitution"
RESULTS = STEP5 / "results"
DEFAULT_REFERENCE = STEP5 / "../04_reference_standard_freeze/full_corpus_reference_standard_frozen_20260609.csv"
DEFAULT_MANIFEST = STEP5 / "locked_outputs/FULL_CORPUS_LOCKED_OUTPUT_MANIFEST_20260609.csv"
DEFAULT_EXCEPTION_LAYER = STEP5 / "results/full_corpus_m1_r_beta_path_exception_correction_layer_20260611.csv"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def parse_reference_record_id(output_row: dict[str, str]) -> str:
    direct = (output_row.get("reference_record_id") or "").strip()
    if direct:
        return direct
    eval_text = output_row.get("evaluation_unit_text", "")
    match = re.search(r"Reference record:\s*([^|;\n]+)", eval_text)
    if match:
        return match.group(1).strip()
    return ""


def manifest_output_rows(manifest_path: Path) -> list[dict[str, str]]:
    manifest_rows = read_csv(manifest_path)
    output_rows: list[dict[str, str]] = []
    for row in manifest_rows:
        if row.get("locked_status") != "locked_model_output":
            continue
        file_value = row.get("file", "").strip()
        if not file_value:
            continue
        output_rows.extend(read_csv(REPO / file_value))
    return output_rows


def build_scoring_reference(reference_rows: list[dict[str, str]], output_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    ref_by_id = {row.get("reference_record_id", "").strip(): row for row in reference_rows}
    scored_reference_rows: list[dict[str, str]] = []
    seen_task_ids: set[str] = set()

    for output_row in output_rows:
        task_unit_id = (output_row.get("task_unit_id") or "").strip()
        if not task_unit_id or task_unit_id in seen_task_ids:
            continue

        ref_id = parse_reference_record_id(output_row)
        ref_row = ref_by_id.get(ref_id, {})

        scored_reference_rows.append(
            {
                "study_id": output_row.get("study_id", ""),
                "reference_record_id": ref_id,
                "task_unit_id": task_unit_id,
                "scoring_eligibility": output_row.get("scoring_eligibility", ""),
                "denominator_family": output_row.get("denominator_family", ""),
                "expected_answer_type": output_row.get("expected_answer_type", ""),
                "statistic_value": ref_row.get("r_value", ""),
                "consensus_value": ref_row.get("r_value", ""),
                "decision_label": "",
            }
        )
        seen_task_ids.add(task_unit_id)

    return scored_reference_rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--reference", type=Path, default=DEFAULT_REFERENCE)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--exception-layer", type=Path, default=DEFAULT_EXCEPTION_LAYER)
    parser.add_argument("--output-dir", type=Path, default=RESULTS)
    parser.add_argument("--scored-output", type=Path, default=None)
    parser.add_argument("--summary-output", type=Path, default=None)
    parser.add_argument("--exception-scored-output", type=Path, default=None)
    parser.add_argument("--exception-summary-output", type=Path, default=None)
    parser.add_argument("--score-script", type=Path, default=REPO / "scripts/llm_scoring_20260606/score_locked_outputs.py")
    parser.add_argument("--apply-script", type=Path, default=REPO / "scripts/llm_scoring_20260606/apply_beta_path_exception_layer.py")
    args = parser.parse_args()

    scored_output = args.scored_output or (args.output_dir / "paper_b_full_corpus_m1_raw_scored_20260611.csv")
    summary_output = args.summary_output or (args.output_dir / "paper_b_full_corpus_m1_raw_score_summary_20260611.csv")
    exception_scored_output = args.exception_scored_output or (args.output_dir / "paper_b_full_corpus_m1_raw_exception_layer_scored_20260611.csv")
    exception_summary_output = args.exception_summary_output or (args.output_dir / "paper_b_full_corpus_m1_raw_exception_layer_scored_summary_20260611.csv")

    output_rows = manifest_output_rows(args.manifest)
    if not output_rows:
        raise SystemExit("No locked full-corpus output rows found in manifest.")

    reference_rows = read_csv(args.reference)
    if not reference_rows:
        raise SystemExit(f"Reference is empty: {args.reference}")

    scoring_reference_rows = build_scoring_reference(reference_rows, output_rows)
    if not scoring_reference_rows:
        raise SystemExit("No task-unit mappings could be built from manifest outputs.")

    with NamedTemporaryFile("w", suffix=".csv", delete=False, encoding="utf-8") as tmp_file:
        temp_reference = Path(tmp_file.name)
    write_csv(
        temp_reference,
        scoring_reference_rows,
        [
            "study_id",
            "reference_record_id",
            "task_unit_id",
            "scoring_eligibility",
            "denominator_family",
            "expected_answer_type",
            "statistic_value",
            "consensus_value",
            "decision_label",
        ],
    )

    status_path = args.output_dir / "SCORING_STATUS_20260606.md"
    status_backup = None
    if status_path.exists():
        status_backup = status_path.with_suffix(".backup_20260611.md")
        shutil.copy2(status_path, status_backup)

    try:
        score_cmd = [
            "python3",
            str(args.score_script),
            "--reference",
            str(temp_reference),
            "--manifest",
            str(args.manifest),
            "--output-dir",
            str(args.output_dir),
            "--scored-output",
            str(scored_output),
            "--summary-output",
            str(summary_output),
        ]
        subprocess.run(score_cmd, check=True)
    finally:
        if status_backup and status_backup.exists():
            shutil.move(status_backup, status_path)
        elif status_path.exists():
            status_path.unlink(missing_ok=True)

    layer_rows = read_csv(args.exception_layer)
    layer_task_ids = {row["task_unit_id"] for row in layer_rows if row.get("task_unit_id")}
    if not layer_task_ids:
        raise SystemExit("Exception layer is empty; cannot apply post-score wrapper")

    scored_rows = read_csv(scored_output)
    if not scored_rows:
        raise SystemExit("No rows were scored; cannot apply exception layer.")

    with NamedTemporaryFile("w", suffix=".csv", delete=False, encoding="utf-8") as tmp_file:
        tmp_path = Path(tmp_file.name)
    write_csv(tmp_path, scored_rows, list(scored_rows[0].keys()))

    apply_cmd = [
        "python3",
        str(args.apply_script),
        "--output",
        str(tmp_path),
        "--layer",
        str(args.exception_layer),
        "--manifest",
        str(args.manifest),
        "--scored-output",
        str(exception_scored_output),
        "--summary-output",
        str(exception_summary_output),
    ]
    subprocess.run(apply_cmd, check=True)

    temp_reference.unlink(missing_ok=True)
    tmp_path.unlink(missing_ok=True)

    print(f"scored_output={scored_output}")
    print(f"summary_output={summary_output}")
    print(f"exception_layer_scored_output={exception_scored_output}")
    print(f"exception_layer_summary_output={exception_summary_output}")
    print(f"layer_task_ids={len(layer_task_ids)}")
    print(f"scored_rows={len(scored_rows)}")


if __name__ == "__main__":
    main()
