#!/usr/bin/env python3
"""Prepare locked-output templates for Paper2 task-family scoring."""

from __future__ import annotations

import csv
import hashlib
import os
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
REFERENCE = (
    AI_ADOPTION_ROOT
    / "Paper2_LLM_Extraction_Working_20260605/09_reference_freeze/"
    "paper2_llm_task_units_labeled_tiered_freeze_20260605.csv"
)
STEP5 = REPO / "data/04_extraction/05_llm_masem_substitution"
LOCKED = STEP5 / "locked_outputs"
SCHEMAS = STEP5 / "schemas"
RESULTS = STEP5 / "results"

TEMPLATE = LOCKED / "paper2_locked_output_template_20260606.csv"
MANIFEST = LOCKED / "LOCKED_OUTPUT_MANIFEST_20260606.csv"
MODEL_MATRIX = LOCKED / "MODEL_RUN_MATRIX_20260606.csv"


OUTPUT_FIELDS = [
    "run_id",
    "model_provider",
    "model_id",
    "model_version",
    "procedure_id",
    "prompt_version",
    "run_timestamp_utc",
    "temperature",
    "seed",
    "task_unit_id",
    "study_id",
    "llm_task_family",
    "denominator_family",
    "scoring_eligibility",
    "expected_answer_type",
    "evaluation_unit_text",
    "model_input_text",
    "model_answer",
    "model_answer_normalized",
    "model_source_locator",
    "model_source_quote",
    "model_confidence",
    "abstained",
    "error_code",
    "raw_output_ref",
    "locked_answer_status",
    "lock_timestamp_utc",
    "locked_by",
    "notes",
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def main() -> None:
    for directory in (LOCKED, SCHEMAS, RESULTS):
        directory.mkdir(parents=True, exist_ok=True)

    with REFERENCE.open(newline="", encoding="utf-8") as handle:
        reference_rows = list(csv.DictReader(handle))

    template_rows = []
    for row in reference_rows:
        model_input_text = (
            f"Study: {row['study_id']} | Task family: {row['llm_task_family']} | "
            f"Field/construct pair: {row.get('field_key') or row.get('construct_pair')} | "
            f"Expected answer type: {row['expected_answer_type']} | "
            f"Source locator: {row.get('source_locator', '')} | "
            f"Source evidence: {row.get('source_evidence', '')} | "
            f"Notes: {row.get('notes', '')}"
        )
        template_rows.append(
            {
                "run_id": "",
                "model_provider": "",
                "model_id": "",
                "model_version": "",
                "procedure_id": "",
                "prompt_version": "",
                "run_timestamp_utc": "",
                "temperature": "",
                "seed": "",
                "task_unit_id": row["task_unit_id"],
                "study_id": row["study_id"],
                "llm_task_family": row["llm_task_family"],
                "denominator_family": row["denominator_family"],
                "scoring_eligibility": row["scoring_eligibility"],
                "expected_answer_type": row["expected_answer_type"],
                "evaluation_unit_text": row["evaluation_unit_text"],
                "model_input_text": model_input_text,
                "model_answer": "",
                "model_answer_normalized": "",
                "model_source_locator": "",
                "model_source_quote": "",
                "model_confidence": "",
                "abstained": "",
                "error_code": "",
                "raw_output_ref": "",
                "locked_answer_status": "template_unlocked",
                "lock_timestamp_utc": "",
                "locked_by": "",
                "notes": "",
            }
        )
    write_csv(TEMPLATE, template_rows, OUTPUT_FIELDS)

    model_rows = [
        {
            "run_id": "paper2_codex_gpt_candidate_YYYYMMDD",
            "model_provider": "openai",
            "model_id": "codex_gpt_candidate",
            "model_version": "fill_exact_version_or_session_surface",
            "procedure_id": "raw_model_extraction_or_stateful_harness",
            "prompt_version": "paper2_task_family_prompt_v1_20260606",
            "temperature": "0",
            "seed": "",
            "run_status": "planned",
            "locked_output_path": "",
            "raw_output_storage": "private_or_local_raw_outputs_not_committed",
            "notes": "Codex CLI is present, but 2026-06-06 noninteractive smoke was not stable enough to score; use only after a locked output export is verified.",
        },
        {
            "run_id": "paper2_claude_smoke_direct_r_20260606",
            "model_provider": "anthropic",
            "model_id": "claude_code",
            "model_version": "2.1.165 (Claude Code)",
            "procedure_id": "raw_model_extraction_smoke",
            "prompt_version": "paper2_task_family_prompt_v1_20260606",
            "temperature": "0",
            "seed": "",
            "run_status": "smoke_locked_scored",
            "locked_output_path": str(LOCKED / "model_runs/paper2_claude_smoke_direct_r_20260606.csv"),
            "raw_output_storage": "private_or_local_raw_outputs_not_committed",
            "notes": "Claude CLI smoke generated one locked direct-r row and scored abstention as incorrect for scorable rows.",
        },
        {
            "run_id": "paper2_gemini_smoke_direct_r_20260606",
            "model_provider": "google",
            "model_id": "gemini_cli",
            "model_version": "0.45.1",
            "procedure_id": "raw_model_extraction_smoke",
            "prompt_version": "paper2_task_family_prompt_v1_20260606",
            "temperature": "0",
            "seed": "",
            "run_status": "smoke_locked_scored",
            "locked_output_path": str(LOCKED / "model_runs/paper2_gemini_smoke_direct_r_20260606.csv"),
            "raw_output_storage": "private_or_local_raw_outputs_not_committed",
            "notes": "Gemini CLI smoke generated one locked direct-r row and scored abstention as incorrect for scorable rows.",
        },
    ]
    write_csv(
        MODEL_MATRIX,
        model_rows,
        [
            "run_id",
            "model_provider",
            "model_id",
            "model_version",
            "procedure_id",
            "prompt_version",
            "temperature",
            "seed",
            "run_status",
            "locked_output_path",
            "raw_output_storage",
            "notes",
        ],
    )

    existing_locked_outputs = []
    if MANIFEST.exists():
        existing_locked_outputs = [
            row for row in read_csv(MANIFEST)
            if row.get("locked_status") == "locked_model_output"
        ]

    manifest_rows = []
    for artifact in (REFERENCE, TEMPLATE, MODEL_MATRIX):
        manifest_rows.append(
            {
                "artifact_role": "reference" if artifact == REFERENCE else "locked_output_shell",
                "file": str(artifact),
                "bytes": str(artifact.stat().st_size),
                "sha256": sha256(artifact),
                "locked_status": "reference_frozen" if artifact == REFERENCE else "template_unlocked",
                "notes": "No model answers are locked in the template.",
            }
        )
    write_csv(
        MANIFEST,
        manifest_rows + existing_locked_outputs,
        ["artifact_role", "file", "bytes", "sha256", "locked_status", "notes"],
    )

    print(f"reference_rows={len(reference_rows)}")
    print(TEMPLATE)
    print(MODEL_MATRIX)
    print(MANIFEST)


if __name__ == "__main__":
    main()
