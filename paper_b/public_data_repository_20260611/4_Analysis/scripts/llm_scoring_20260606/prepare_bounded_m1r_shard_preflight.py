#!/usr/bin/env python3
"""Prepare a bounded post-freeze M1-R shard and run-readiness report.

This script does not execute a model. It creates a deterministic shard candidate
for the next source-rendered M1-R run, excludes known beta/path exception rows
from generic scoring, and checks whether the ignored private source packets
needed for a defensible run are present in the current workspace.
"""

from __future__ import annotations

import csv
import hashlib
import argparse
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path


REPO = Path(__file__).resolve().parents[2]
STEP5 = REPO / "data/04_extraction/05_llm_masem_substitution"
BENCH = REPO / "data/04_extraction/07_paper_c_harness_benchmark"
TASK_SHELL = STEP5 / "full_corpus_step5_task_unit_shell_20260609.csv"
FULL_MANIFEST = STEP5 / "locked_outputs/FULL_CORPUS_LOCKED_OUTPUT_MANIFEST_20260609.csv"
EXCEPTION_LAYER = STEP5 / "results/full_corpus_m1_r_beta_path_exception_correction_layer_20260611.csv"
BUNDLE_DIR = BENCH / "06_rerun_bundles"
RESULTS_DIR = STEP5 / "results"
DEFAULT_SOURCE_PACKET_DIR = BENCH / "private/source_renderings_20260609_full_coverage/source_packets"

TASK_ID_OUTPUT = BUNDLE_DIR / "source_rendered_bounded_m1r_shard_task_ids_20260611.csv"
PREFLIGHT_CSV = RESULTS_DIR / "full_corpus_m1_r_bounded_shard_preflight_20260611.csv"
PREFLIGHT_MD = RESULTS_DIR / "FULL_CORPUS_M1_R_BOUNDED_SHARD_PREFLIGHT_20260611.md"

DENOMINATOR_FAMILIES = [
    "primary_direct_r_or_source_reported_correlation",
    "primary_latent_or_construct_correlation_with_source_type_flag",
    "secondary_beta_or_path_converted_effect_size",
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rel(path: Path) -> str:
    return str(path.relative_to(REPO))


def locked_task_ids(manifest: Path) -> set[str]:
    ids: set[str] = set()
    if not manifest.exists():
        return ids
    for entry in read_csv(manifest):
        file_value = entry.get("file", "")
        if not file_value or "locked_outputs/model_runs/" not in file_value:
            continue
        path = REPO / file_value
        if not path.exists():
            continue
        try:
            for row in read_csv(path):
                task_id = row.get("task_unit_id", "")
                if task_id:
                    ids.add(task_id)
        except csv.Error:
            continue
    return ids


def exception_excluded_task_ids(exception_layer: Path) -> set[str]:
    excluded: set[str] = set()
    if not exception_layer.exists():
        return excluded
    for row in read_csv(exception_layer):
        task_id = row.get("task_unit_id", "")
        gate = row.get("generic_full_accuracy_gate_status", "")
        eligible = row.get("larger_m1_r_eligible_before_layer_consumed", "")
        if task_id and (gate.startswith("exclude_") or eligible.lower() == "false"):
            excluded.add(task_id)
    return excluded


def existing_task_ids(path: Path) -> list[str]:
    if not path.exists():
        return []
    task_ids = []
    for row in read_csv(path):
        task_id = row.get("task_unit_id", "")
        if task_id:
            task_ids.append(task_id)
    return task_ids


def select_existing_task_bundle(rows: list[dict[str, str]], task_ids: list[str]) -> list[dict[str, str]]:
    by_id = {row.get("task_unit_id", ""): row for row in rows}
    selected: list[dict[str, str]] = []
    missing: list[str] = []
    for task_id in task_ids:
        row = by_id.get(task_id)
        if row is None:
            missing.append(task_id)
        else:
            selected.append(row)
    if missing:
        raise SystemExit(
            "Existing bounded shard task bundle references task IDs absent from "
            f"{rel(TASK_SHELL)}: {', '.join(missing[:20])}"
        )
    return selected


def select_shard(rows: list[dict[str, str]], per_family: int, refresh_selection: bool) -> tuple[list[dict[str, str]], str]:
    if not refresh_selection:
        task_ids = existing_task_ids(TASK_ID_OUTPUT)
        if task_ids:
            return select_existing_task_bundle(rows, task_ids), "reused_existing_task_id_bundle"

    seen = locked_task_ids(FULL_MANIFEST)
    excluded = exception_excluded_task_ids(EXCEPTION_LAYER)
    buckets: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        family = row.get("denominator_family", "")
        if family not in DENOMINATOR_FAMILIES:
            continue
        if not row.get("scoring_eligibility", "").startswith("eligible_after_locked_llm_output"):
            continue
        if row.get("task_unit_id") in seen or row.get("task_unit_id") in excluded:
            continue
        if len(buckets[family]) < per_family:
            buckets[family].append(row)
    selected: list[dict[str, str]] = []
    for family in DENOMINATOR_FAMILIES:
        selected.extend(buckets[family])
    return selected, "selected_new_excluding_prior_locked_outputs"


def source_packet_present(source_packet_dir: Path, study_id: str) -> bool:
    if not source_packet_dir.exists():
        return False
    patterns = [
        f"{study_id}_source_packet*.txt",
        f"{study_id}.txt",
    ]
    return any(any(source_packet_dir.glob(pattern)) for pattern in patterns)


def write_task_bundle(selected: list[dict[str, str]], source_packet_dir: Path, selection_mode: str) -> None:
    rows = []
    family_index = Counter()
    for row in selected:
        family = row["denominator_family"]
        family_index[family] += 1
        study_id = row["study_id"]
        rows.append(
            {
                "task_unit_id": row["task_unit_id"],
                "study_id": study_id,
                "reference_record_id": row["reference_record_id"],
                "denominator_family": family,
                "bounded_shard_family_index": str(family_index[family]),
                "source_packet_required": "true",
                "source_packet_present_current_workspace": str(source_packet_present(source_packet_dir, study_id)).lower(),
                "exception_layer_generic_exclusion": "false",
                "previous_locked_output_excluded": str(selection_mode == "selected_new_excluding_prior_locked_outputs").lower(),
                "selection_mode": selection_mode,
                "notes": "Canonical bounded shard task ID bundle; reruns reuse this bundle unless --refresh-selection is passed.",
            }
        )
    write_csv(
        TASK_ID_OUTPUT,
        rows,
        [
            "task_unit_id",
            "study_id",
            "reference_record_id",
            "denominator_family",
            "bounded_shard_family_index",
            "source_packet_required",
            "source_packet_present_current_workspace",
            "exception_layer_generic_exclusion",
            "previous_locked_output_excluded",
            "selection_mode",
            "notes",
        ],
    )


def write_preflight(selected: list[dict[str, str]], source_packet_dir: Path, selection_mode: str) -> None:
    selected_studies = sorted({row["study_id"] for row in selected})
    present_studies = [study_id for study_id in selected_studies if source_packet_present(source_packet_dir, study_id)]
    missing_studies = [study_id for study_id in selected_studies if study_id not in set(present_studies)]
    by_family = Counter(row["denominator_family"] for row in selected)
    status = "blocked_missing_private_source_packets" if missing_studies else "ready_for_authorized_model_run"

    summary_rows = [
        {"metric": "status", "value": status},
        {"metric": "task_rows", "value": str(len(selected))},
        {"metric": "unique_studies", "value": str(len(selected_studies))},
        {"metric": "source_packet_dir", "value": rel(source_packet_dir) if source_packet_dir.is_relative_to(REPO) else str(source_packet_dir)},
        {"metric": "source_packet_dir_exists", "value": str(source_packet_dir.exists()).lower()},
        {"metric": "studies_with_source_packet", "value": str(len(present_studies))},
        {"metric": "studies_missing_source_packet", "value": str(len(missing_studies))},
        {"metric": "selection_mode", "value": selection_mode},
        {"metric": "previous_locked_task_ids_excluded", "value": str(len(locked_task_ids(FULL_MANIFEST)))},
        {"metric": "generic_exception_task_ids_excluded", "value": str(len(exception_excluded_task_ids(EXCEPTION_LAYER)))},
    ]
    for family in DENOMINATOR_FAMILIES:
        summary_rows.append({"metric": f"selected_{family}", "value": str(by_family[family])})
    write_csv(PREFLIGHT_CSV, summary_rows, ["metric", "value"])

    command = f"""run_id=paper_b_full_corpus_m1_raw_bounded_shard_0090_20260611
python3 scripts/llm_scoring_20260606/run_model_locked_output_batch.py \\
  --provider codex \\
  --model-selector gpt-5.5 \\
  --template data/04_extraction/05_llm_masem_substitution/locked_outputs/full_corpus_locked_output_template_20260609.csv \\
  --manifest data/04_extraction/05_llm_masem_substitution/locked_outputs/FULL_CORPUS_LOCKED_OUTPUT_MANIFEST_20260609.csv \\
  --task-ids-file {rel(TASK_ID_OUTPUT)} \\
  --source-packet-dir {rel(source_packet_dir)} \\
  --require-source-packet \\
  --suppress-source-quotes \\
  --prompt-version paper_b_step5_full_corpus_prompt_v1_20260609_source_packet_bounded_shard \\
  --procedure-id raw_model_extraction_source_rendered_bounded_shard \\
  --run-id "$run_id" \\
  --chunk-size 10 \\
  --timeout 900 \\
  --register \\
  --fail-on-model-cli-error

python3 scripts/llm_scoring_20260606/score_full_corpus_m1_r_with_exception_layer.py \\
  --manifest data/04_extraction/05_llm_masem_substitution/locked_outputs/FULL_CORPUS_LOCKED_OUTPUT_MANIFEST_20260609.csv
"""

    missing_preview = ", ".join(missing_studies[:20]) if missing_studies else "none"
    if missing_studies:
        gate_lines = [
            "A new bounded `M1-R` shard should not be executed from this current",
            "workspace until the ignored private source packet directory is restored",
            "or regenerated. Running without `--require-source-packet` would turn the",
            "run into a source-absent abstention diagnostic rather than a defensible",
            "post-freeze source-rendered shard.",
        ]
    else:
        gate_lines = [
            "The required private source packets are present in this workspace.",
            "The bounded `M1-R` shard may be executed with `--require-source-packet`,",
            "`--suppress-source-quotes`, and the exception-aware scorer. This remains",
            "a staged shard gate, not full-corpus accuracy or substitution evidence.",
        ]
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    PREFLIGHT_MD.write_text(
        "\n".join(
            [
                "# Full-Corpus M1-R Bounded Shard Preflight",
                "",
                f"Date: {now[:10]}",
                "",
                "## Scope",
                "",
                "This artifact prepares a bounded post-freeze `M1-R` source-rendered",
                "shard candidate after the beta/path exception-aware scorer was wired.",
                "It does not execute a model and does not support an accuracy, model-",
                "comparison, or MASEM substitution claim.",
                "",
                "## Candidate Shard",
                "",
                f"- Task rows: `{len(selected)}`",
                f"- Unique studies: `{len(selected_studies)}`",
                f"- Direct/source r rows: `{by_family['primary_direct_r_or_source_reported_correlation']}`",
                f"- Latent/construct correlation rows: `{by_family['primary_latent_or_construct_correlation_with_source_type_flag']}`",
                f"- Beta/path converted-effect rows: `{by_family['secondary_beta_or_path_converted_effect_size']}`",
                f"- Selection mode: `{selection_mode}`",
                f"- Previous locked-output task IDs excluded: `{len(locked_task_ids(FULL_MANIFEST))}`",
                f"- Generic beta/path exception task IDs excluded: `{len(exception_excluded_task_ids(EXCEPTION_LAYER))}`",
                "",
                "Candidate task bundle:",
                "",
                f"- `{rel(TASK_ID_OUTPUT)}`",
                "",
                "## Source Packet Preflight",
                "",
                f"- Source packet directory checked: `{rel(source_packet_dir) if source_packet_dir.is_relative_to(REPO) else source_packet_dir}`",
                f"- Directory exists: `{str(source_packet_dir.exists()).lower()}`",
                f"- Studies with packet in this workspace: `{len(present_studies)}`",
                f"- Studies missing packet in this workspace: `{len(missing_studies)}`",
                f"- Missing study preview: `{missing_preview}`",
                "",
                "## Gate Decision",
                "",
                f"Status: `{status}`.",
                "",
                *gate_lines,
                "",
                "## Recovery Command After Private Packets Are Restored",
                "",
                "```sh",
                command.rstrip(),
                "```",
                "",
                "The follow-up scoring command must remain exception-aware. Do not report",
                "full-corpus accuracy or substitution stability from this bounded shard",
                "alone; report it as a staged source-rendered run with denominator-family",
                "and exception-layer boundaries.",
                "",
            ]
        ),
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--refresh-selection",
        action="store_true",
        help="Select a new bounded shard instead of reusing the canonical task-id bundle if present.",
    )
    args = parser.parse_args()
    task_rows = read_csv(TASK_SHELL)
    selected, selection_mode = select_shard(task_rows, per_family=30, refresh_selection=args.refresh_selection)
    write_task_bundle(selected, DEFAULT_SOURCE_PACKET_DIR, selection_mode)
    write_preflight(selected, DEFAULT_SOURCE_PACKET_DIR, selection_mode)
    print(f"wrote {rel(TASK_ID_OUTPUT)}")
    print(f"wrote {rel(PREFLIGHT_CSV)}")
    print(f"wrote {rel(PREFLIGHT_MD)}")
    print(f"task_rows={len(selected)} sha256={sha256(TASK_ID_OUTPUT)}")


if __name__ == "__main__":
    main()
