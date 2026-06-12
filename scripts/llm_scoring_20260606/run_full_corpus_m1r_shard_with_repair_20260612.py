#!/usr/bin/env python3
"""Run one full-corpus M1-R shard and repair manifest-blocking row failures."""

from __future__ import annotations

import argparse
import csv
import subprocess
from collections import Counter
from pathlib import Path

from run_model_locked_output_batch import register_locked_output


REPO = Path(__file__).resolve().parents[2]
STEP5 = REPO / "data/04_extraction/05_llm_masem_substitution"
MODEL_RUNS = STEP5 / "locked_outputs/model_runs"
TEMPLATE = STEP5 / "locked_outputs/full_corpus_locked_output_template_20260609.csv"
MANIFEST = STEP5 / "locked_outputs/FULL_CORPUS_M1_R_FULL_RUN_MANIFEST_20260612.csv"
SOURCE_PACKETS = (
    REPO
    / "data/04_extraction/07_paper_c_harness_benchmark/private/"
    "source_renderings_20260609_full_coverage/source_packets"
)
RERUN_BUNDLES = REPO / "data/04_extraction/07_paper_c_harness_benchmark/06_rerun_bundles"

PROMPT_VERSION = "paper_b_step5_full_corpus_prompt_v1_20260609_source_packet_full_corpus"
PROCEDURE_ID = "raw_model_extraction_source_rendered_full_corpus"
BLOCKING_ERRORS = {"model_cli_error", "source_quote_policy_violation"}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def run_batch(run_id: str, offset: int | None, limit: int | None, task_ids_file: Path | None, chunk_size: int, register: bool) -> int:
    cmd = [
        "python3",
        "scripts/llm_scoring_20260606/run_model_locked_output_batch.py",
        "--provider",
        "codex",
        "--model-selector",
        "gpt-5.5",
        "--template",
        str(TEMPLATE.relative_to(REPO)),
        "--manifest",
        str(MANIFEST.relative_to(REPO)),
        "--source-packet-dir",
        str(SOURCE_PACKETS.relative_to(REPO)),
        "--require-source-packet",
        "--suppress-source-quotes",
        "--prompt-version",
        PROMPT_VERSION,
        "--procedure-id",
        PROCEDURE_ID,
        "--run-id",
        run_id,
        "--chunk-size",
        str(chunk_size),
        "--timeout",
        "900",
        "--fail-on-model-cli-error",
    ]
    if task_ids_file:
        cmd.extend(["--task-ids-file", str(task_ids_file.relative_to(REPO))])
    else:
        cmd.extend(["--offset", str(offset or 0), "--limit", str(limit or 0)])
    if register:
        cmd.append("--register")
    return subprocess.run(cmd, cwd=REPO).returncode


def blocking_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    return [
        row
        for row in rows
        if row.get("error_code") in BLOCKING_ERRORS or row.get("model_source_quote", "").strip()
    ]


def verify_rows(path: Path, expected_limit: int) -> list[dict[str, str]]:
    rows = read_csv(path)
    if len(rows) != expected_limit:
        raise SystemExit(f"{path.name}: expected {expected_limit} rows, found {len(rows)}")
    task_ids = [row.get("task_unit_id", "") for row in rows]
    if len(task_ids) != len(set(task_ids)):
        raise SystemExit(f"{path.name}: duplicate task_unit_id rows detected")
    failures = blocking_rows(rows)
    if failures:
        counts = Counter(row.get("error_code") or "source_quote_policy_violation" for row in failures)
        raise SystemExit(f"{path.name}: blocking failures remain: {dict(counts)}")
    return rows


def task_id_file_for(run_id: str, failures: list[dict[str, str]]) -> Path:
    path = RERUN_BUNDLES / f"{run_id}_repair_task_ids.csv"
    write_csv(path, [{"task_unit_id": row["task_unit_id"]} for row in failures], ["task_unit_id"])
    return path


def compose_clean(original: Path, repair: Path, output: Path, expected_limit: int) -> None:
    original_rows = read_csv(original)
    repair_rows = read_csv(repair)
    repair_by_task = {row["task_unit_id"]: row for row in repair_rows}
    output_rows = [repair_by_task.get(row["task_unit_id"], row) for row in original_rows]
    if len(output_rows) != expected_limit:
        raise SystemExit("composite row count mismatch")
    fields = list(original_rows[0].keys())
    for row in repair_rows:
        for key in row:
            if key not in fields:
                fields.append(key)
    write_csv(output, output_rows, fields)


def manifest_contains(path: Path) -> bool:
    if not MANIFEST.exists():
        return False
    rel = str(path.relative_to(REPO))
    return any(row.get("file") == rel for row in read_csv(MANIFEST))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--offset", type=int, required=True)
    parser.add_argument("--limit", type=int, required=True)
    parser.add_argument("--chunk-size", type=int, default=10)
    args = parser.parse_args()

    output = MODEL_RUNS / f"{args.run_id}.csv"
    if output.exists():
        rows = read_csv(output)
        failures = blocking_rows(rows)
        if not failures:
            verify_rows(output, args.limit)
            if not manifest_contains(output):
                register_locked_output(output, MANIFEST)
            print(f"shard_clean_existing file={output} rows={len(rows)}")
            return
    else:
        returncode = run_batch(args.run_id, args.offset, args.limit, None, args.chunk_size, register=True)
        if returncode not in {0, 2}:
            raise SystemExit(returncode)

    rows = read_csv(output)
    failures = blocking_rows(rows)
    if not failures:
        verify_rows(output, args.limit)
        if not manifest_contains(output):
            register_locked_output(output, MANIFEST)
        print(f"shard_clean file={output} rows={len(rows)}")
        return

    task_file = task_id_file_for(args.run_id, failures)
    repair_run_id = f"{args.run_id}_repair"
    repair_output = MODEL_RUNS / f"{repair_run_id}.csv"
    returncode = run_batch(repair_run_id, None, None, task_file, 1, register=False)
    if returncode != 0:
        raise SystemExit(returncode)

    repair_rows = verify_rows(repair_output, len(failures))
    if blocking_rows(repair_rows):
        raise SystemExit("repair output still contains manifest-blocking failures")

    clean_output = MODEL_RUNS / f"{args.run_id}_clean_repaired.csv"
    compose_clean(output, repair_output, clean_output, args.limit)
    clean_rows = verify_rows(clean_output, args.limit)
    register_locked_output(clean_output, MANIFEST)
    print(
        "shard_clean_repaired",
        f"file={clean_output}",
        f"rows={len(clean_rows)}",
        f"repaired={len(failures)}",
    )


if __name__ == "__main__":
    main()
