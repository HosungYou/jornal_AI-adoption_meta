#!/usr/bin/env python3
"""Prepare post-freeze Step 5 locked-output and Paper C planning artifacts."""

from __future__ import annotations

import csv
import hashlib
from collections import Counter
from pathlib import Path


REPO = Path(__file__).resolve().parents[2]
STEP5 = REPO / "data/04_extraction/05_llm_masem_substitution"
LOCKED = STEP5 / "locked_outputs"
PAPER_C_BENCH = REPO / "data/04_extraction/07_paper_c_harness_benchmark"

TASK_SHELL = STEP5 / "full_corpus_step5_task_unit_shell_20260609.csv"
STATUS_ONLY_SHELL = STEP5 / "full_corpus_step5_status_only_shell_20260609.csv"
REFERENCE = REPO / "data/04_extraction/04_reference_standard_freeze/full_corpus_reference_standard_frozen_20260609.csv"
CAVEAT_REGISTER = REPO / "data/04_extraction/04_reference_standard_freeze/full_corpus_reference_standard_freeze_caveat_register_20260609.csv"
DISAGREEMENT_QUEUE = (
    REPO
    / "data/04_extraction/02_pre_adjudication_disagreement/combined/derived/combined_correlation_review_queue_20260525.csv"
)

LOCKED_TEMPLATE = LOCKED / "full_corpus_locked_output_template_20260609.csv"
RUN_MATRIX = LOCKED / "FULL_CORPUS_MODEL_PROCEDURE_RUN_MATRIX_20260609.csv"
MANIFEST = LOCKED / "FULL_CORPUS_LOCKED_OUTPUT_MANIFEST_20260609.csv"
AUTH_PACKET = LOCKED / "FULL_CORPUS_PRE_RUN_AUTHORIZATION_PACKET_20260609.md"
SCHEMA = STEP5 / "schemas/FULL_CORPUS_LOCKED_OUTPUT_SCHEMA_20260609.md"
SOURCE_RENDERING = PAPER_C_BENCH / "00_manifest/source_rendering_chunking_manifest_20260609.csv"
REPEATABILITY_SUBSET = PAPER_C_BENCH / "06_rerun_bundles/repeatability_subset_manifest_20260609.csv"


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


RUN_MATRIX_FIELDS = [
    "condition_code",
    "run_id_pattern",
    "comparison_role",
    "model_provider",
    "model_id",
    "model_selector",
    "model_version_lock",
    "procedure_id",
    "procedure_label",
    "prompt_version",
    "schema_version",
    "source_rendering_manifest",
    "chunking_policy_id",
    "task_template_path",
    "task_count",
    "denominator_families",
    "temperature",
    "seed",
    "repeatability_subset_id",
    "budget_cap_usd",
    "expected_locked_output_path_pattern",
    "raw_output_storage",
    "run_status",
    "authorization_status",
    "notes",
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=fields,
            extrasaction="ignore",
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def expected_answer_type(row: dict[str, str]) -> str:
    family = row["denominator_family"]
    if family == "primary_direct_r_or_source_reported_correlation":
        return "numeric_r_effect_size"
    if family == "primary_latent_or_construct_correlation_with_source_type_flag":
        return "numeric_correlation_with_source_type"
    if family == "secondary_beta_or_path_converted_effect_size":
        return "numeric_effect_size_with_source_type"
    return "numeric_effect_size_with_source_type"


def evaluation_text(row: dict[str, str]) -> str:
    return (
        f"Study: {row['study_id']} | Reference record: {row['reference_record_id']} | "
        f"Sample/stratum: {row['sample_or_stratum']} | N: {row['n']} | "
        f"Construct pair: {row['construct_1']}-{row['construct_2']} | "
        f"Human reference r: {row['reference_r_value']} | "
        f"Reference source type: {row['reference_r_source']} | "
        f"Evidence type: {row['reference_evidence_type']} | "
        f"Source location: {row['source_location']} | Caveats: {row['caveat_ids']} | "
        f"Notes: {row['notes']}"
    )


def model_input_text(row: dict[str, str]) -> str:
    return (
        f"Study: {row['study_id']} | Sample/stratum: {row['sample_or_stratum']} | "
        f"Construct pair: {row['construct_1']}-{row['construct_2']} | "
        f"Expected answer type: {expected_answer_type(row)} | "
        f"Evidence family to recover: {row['evidence_family']} | "
        "Use only the locked source-document rendering/chunks for the authorized run condition. "
        "This task stub intentionally excludes the human reference value."
    )


def prepare_locked_template(task_rows: list[dict[str, str]]) -> None:
    rows = []
    for row in task_rows:
        rows.append(
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
                "llm_task_family": row["evidence_family"],
                "denominator_family": row["denominator_family"],
                "scoring_eligibility": row["scoring_eligibility"],
                "expected_answer_type": expected_answer_type(row),
                "evaluation_unit_text": evaluation_text(row),
                "model_input_text": model_input_text(row),
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
                "notes": "Generated from full-corpus post-freeze task shell; model run not authorized.",
            }
        )
    write_csv(LOCKED_TEMPLATE, rows, OUTPUT_FIELDS)


def prepare_run_matrix(task_rows: list[dict[str, str]]) -> None:
    task_count = str(len(task_rows))
    families = ";".join(sorted({row["denominator_family"] for row in task_rows}))
    locked_pattern = (
        "data/04_extraction/05_llm_masem_substitution/locked_outputs/model_runs/"
        "{run_id}.csv"
    )
    common = {
        "prompt_version": "paper_b_step5_full_corpus_prompt_v1_20260609",
        "schema_version": "full_corpus_locked_output_schema_v1_20260609",
        "source_rendering_manifest": str(SOURCE_RENDERING.relative_to(REPO)),
        "chunking_policy_id": "source_rendering_policy_v1_no_reference_value",
        "task_template_path": str(LOCKED_TEMPLATE.relative_to(REPO)),
        "task_count": task_count,
        "denominator_families": families,
        "temperature": "0",
        "seed": "unsupported_or_provider_default",
        "repeatability_subset_id": "paper_c_repeatability_subset_v1_20260609",
        "budget_cap_usd": "pending_researcher_authorization",
        "expected_locked_output_path_pattern": locked_pattern,
        "raw_output_storage": "private_or_local_raw_outputs_not_committed",
        "run_status": "planned_not_run",
        "authorization_status": "pending_researcher_approval",
    }
    rows = [
        {
            **common,
            "condition_code": "M1-R",
            "run_id_pattern": "paper_b_full_corpus_m1_raw_YYYYMMDD",
            "comparison_role": "primary_raw_model_baseline",
            "model_provider": "openai",
            "model_id": "codex_gpt_candidate",
            "model_selector": "gpt-5.5_or_current_codex_selector_to_verify",
            "model_version_lock": "record_exact_cli_api_surface_and_model_snapshot_before_run",
            "procedure_id": "raw_model_extraction",
            "procedure_label": "Raw model extraction with locked prompt/schema and source rendering",
            "notes": "Recommended first smoke/full condition because prior legacy scaffold has Codex GPT-5.5 coverage; selector must be reverified before execution.",
        },
        {
            **common,
            "condition_code": "M1-P",
            "run_id_pattern": "paper_b_full_corpus_m1_stateful_harness_YYYYMMDD",
            "comparison_role": "same_model_procedure_contrast",
            "model_provider": "openai",
            "model_id": "codex_gpt_candidate",
            "model_selector": "same_as_M1-R_after_verification",
            "model_version_lock": "must_match_M1-R_model_snapshot_or_be_logged_as_separate_condition",
            "procedure_id": "stateful_research_harness",
            "procedure_label": "Stateful provenance-preserving research procedure",
            "notes": "Paper C procedure contrast; do not run until raw condition and harness protocol are approved.",
        },
        {
            **common,
            "condition_code": "M2-R",
            "run_id_pattern": "paper_b_full_corpus_m2_raw_YYYYMMDD",
            "comparison_role": "cross_model_raw_comparison",
            "model_provider": "anthropic",
            "model_id": "claude_sonnet_candidate",
            "model_selector": "sonnet_or_current_claude_sonnet_selector_to_verify",
            "model_version_lock": "record_exact_cli_api_surface_and_model_snapshot_before_run",
            "procedure_id": "raw_model_extraction",
            "procedure_label": "Raw model extraction with locked prompt/schema and source rendering",
            "notes": "Cross-model raw condition; complete only if resources allow comparable full-corpus coverage.",
        },
        {
            **common,
            "condition_code": "M3-R",
            "run_id_pattern": "paper_b_full_corpus_m3_raw_optional_YYYYMMDD",
            "comparison_role": "optional_third_family_raw_comparison",
            "model_provider": "google",
            "model_id": "gemini_flash_candidate",
            "model_selector": "gemini-3-flash-preview_or_current_verified_selector",
            "model_version_lock": "record_exact_cli_api_surface_and_model_snapshot_before_run",
            "procedure_id": "raw_model_extraction",
            "procedure_label": "Raw model extraction with locked prompt/schema and source rendering",
            "notes": "Optional third-family robustness condition; lower priority than M1-R, M1-P, and M2-R.",
        },
        {
            **common,
            "condition_code": "M1-R-SMOKE",
            "run_id_pattern": "paper_b_full_corpus_m1_raw_smoke_YYYYMMDD",
            "comparison_role": "schema_and_source_rendering_smoke_test",
            "model_provider": "openai",
            "model_id": "codex_gpt_candidate",
            "model_selector": "same_as_M1-R_after_verification",
            "model_version_lock": "record_exact_cli_api_surface_and_model_snapshot_before_run",
            "procedure_id": "raw_model_extraction_smoke",
            "procedure_label": "Small stratified preflight before full-corpus run",
            "task_count": "30",
            "denominator_families": "stratified_smoke_subset_from_all_denominator_families",
            "budget_cap_usd": "pending_researcher_authorization_small_cap",
            "notes": "Recommended first executable unit after approval; intended to catch schema/source-rendering failures before full run.",
        },
    ]
    write_csv(RUN_MATRIX, rows, RUN_MATRIX_FIELDS)


def prepare_source_rendering_manifest() -> None:
    fields = [
        "manifest_id",
        "condition_scope",
        "source_document_policy",
        "pdf_path_policy",
        "source_text_policy",
        "chunking_policy_id",
        "chunk_unit",
        "max_chunk_chars",
        "overlap_chars",
        "table_handling",
        "source_location_leakage_policy",
        "human_reference_leakage_policy",
        "private_output_policy",
        "status",
        "notes",
    ]
    rows = [
        {
            "manifest_id": "source_rendering_policy_v1_20260609",
            "condition_scope": "all_post_freeze_step5_conditions",
            "source_document_policy": "use_local_source_pdfs_from_ignored_paths_or_share_safe_text_renderings",
            "pdf_path_policy": "do_not_commit_pdf_paths_or_pdf_files",
            "source_text_policy": "commit_no_private_source_text; store raw renderings locally only",
            "chunking_policy_id": "source_rendering_policy_v1_no_reference_value",
            "chunk_unit": "study_level_source_packet_then_table_or_section_chunks",
            "max_chunk_chars": "pending_preflight",
            "overlap_chars": "pending_preflight",
            "table_handling": "preserve table labels/row-column context when rendered; no human reference value inserted",
            "source_location_leakage_policy": "model prompt must not include human-adjudicated source_location unless a separate source-locator-aided condition is explicitly created",
            "human_reference_leakage_policy": "exclude reference_r_value, decision_status, adjudication rationale, and human consensus from model prompt",
            "private_output_policy": "raw transcripts/renderings stay local; commit only locked structured outputs and redacted summaries",
            "status": "planned_not_run",
            "notes": "Prepared for approval; no source rendering was executed by this artifact.",
        }
    ]
    write_csv(SOURCE_RENDERING, rows, fields)


def disagreement_scores() -> dict[str, int]:
    if not DISAGREEMENT_QUEUE.exists():
        return {}
    rows = read_csv(DISAGREEMENT_QUEUE)
    scores: dict[str, int] = {}
    for row in rows:
        try:
            score = int(row.get("n_difference_rows") or 0)
        except ValueError:
            score = 0
        scores[row["study_id"]] = score
    return scores


def select_repeatability_subset(task_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    scores = disagreement_scores()
    by_family: dict[str, list[dict[str, str]]] = {}
    for row in task_rows:
        by_family.setdefault(row["denominator_family"], []).append(row)

    selected: dict[str, tuple[dict[str, str], str]] = {}

    def add_to(
        family_selected: dict[str, tuple[dict[str, str], str]],
        row: dict[str, str],
        reason: str,
    ) -> None:
        family_selected.setdefault(row["task_unit_id"], (row, reason))

    # Add caveat-bearing, high-disagreement, and clean rows with a 40/40/40
    # denominator-family target so repeatability is not dominated by direct-r rows.
    for family, rows in sorted(by_family.items()):
        family_selected: dict[str, tuple[dict[str, str], str]] = {}

        # Keep all rows for the small but important source-corrected N caveat.
        for row in rows:
            if "CAV002" in row["caveat_ids"]:
                add_to(family_selected, row, "source_corrected_sample_size_all_rows")

        caveat_rows = [row for row in rows if row["caveat_ids"] != "none"]
        caveat_rows.sort(key=lambda r: (-scores.get(r["study_id"], 0), r["study_id"], r["task_unit_id"]))
        for row in caveat_rows:
            if len(family_selected) >= 20:
                break
            add_to(family_selected, row, f"caveat_priority_{family}")

        high_disagreement = sorted(rows, key=lambda r: (-scores.get(r["study_id"], 0), r["study_id"], r["task_unit_id"]))
        for row in high_disagreement:
            if len(family_selected) >= 30:
                break
            add_to(family_selected, row, f"high_disagreement_queue_priority_{family}")

        clean_rows = [row for row in rows if row["caveat_ids"] == "none"]
        clean_rows.sort(key=lambda r: (r["phase_block"], r["study_id"], r["task_unit_id"]))
        step = max(1, len(clean_rows) // 20)
        for row in clean_rows[::step]:
            if len(family_selected) >= 40:
                break
            add_to(family_selected, row, f"clean_stratified_spacing_{family}")

        for row in rows:
            if len(family_selected) >= 40:
                break
            add_to(family_selected, row, f"deterministic_fill_{family}")

        for task_unit_id, item in family_selected.items():
            selected[task_unit_id] = item

    final = list(selected.values())
    final.sort(
        key=lambda item: (
            item[0]["denominator_family"],
            0 if "source_corrected" in item[1] else 1 if "caveat" in item[1] else 2 if "high_disagreement" in item[1] else 3,
            -scores.get(item[0]["study_id"], 0),
            item[0]["study_id"],
            item[0]["task_unit_id"],
        )
    )

    output_rows = []
    for row, reason in final:
        output_rows.append(
            {
                "subset_id": "paper_c_repeatability_subset_v1_20260609",
                "subset_version": "v1",
                "task_unit_id": row["task_unit_id"],
                "study_id": row["study_id"],
                "reference_record_id": row["reference_record_id"],
                "phase_block": row["phase_block"],
                "pair": row["pair"],
                "denominator_family": row["denominator_family"],
                "evidence_family": row["evidence_family"],
                "construct_pair": f"{row['construct_1']}-{row['construct_2']}",
                "caveat_ids": row["caveat_ids"],
                "selection_stratum": reason,
                "pre_adjudication_difference_rows": str(scores.get(row["study_id"], "")),
                "repeatability_role": "repeated_run_stability_subset",
                "notes": "No model run authorized; subset freezes task IDs only.",
            }
        )
    return output_rows


def prepare_repeatability_subset(task_rows: list[dict[str, str]]) -> None:
    fields = [
        "subset_id",
        "subset_version",
        "task_unit_id",
        "study_id",
        "reference_record_id",
        "phase_block",
        "pair",
        "denominator_family",
        "evidence_family",
        "construct_pair",
        "caveat_ids",
        "selection_stratum",
        "pre_adjudication_difference_rows",
        "repeatability_role",
        "notes",
    ]
    write_csv(REPEATABILITY_SUBSET, select_repeatability_subset(task_rows), fields)


def prepare_manifest() -> None:
    fields = ["artifact_role", "file", "bytes", "sha256", "locked_status", "notes"]
    artifacts = [
        ("frozen_reference", REFERENCE, "reference_frozen", "Current 2026-06-09 full-corpus human reference."),
        ("post_freeze_task_shell", TASK_SHELL, "task_shell_frozen", "No model answers."),
        ("status_only_shell", STATUS_ONLY_SHELL, "corpus_accounting_frozen", "No target task rows."),
        ("caveat_register", CAVEAT_REGISTER, "caveat_register_frozen", "Downstream caveats retained."),
        ("locked_output_template", LOCKED_TEMPLATE, "template_unlocked", "Model answer fields are blank."),
        ("model_procedure_run_matrix", RUN_MATRIX, "planned_not_run", "Run conditions pending researcher authorization."),
        ("source_rendering_manifest", SOURCE_RENDERING, "planned_not_run", "Source rendering policy only; no private source text."),
        ("repeatability_subset_manifest", REPEATABILITY_SUBSET, "subset_frozen_not_run", "Repeatability task IDs only."),
        ("locked_output_schema", SCHEMA, "schema_prepared", "Post-freeze schema and leakage boundary."),
        ("pre_run_authorization_packet", AUTH_PACKET, "approval_pending", "Researcher approval checklist; no model run authorized."),
    ]
    rows = []
    for role, path, status, notes in artifacts:
        if not path.exists():
            continue
        rows.append(
            {
                "artifact_role": role,
                "file": str(path.relative_to(REPO)),
                "bytes": str(path.stat().st_size),
                "sha256": sha256(path),
                "locked_status": status,
                "notes": notes,
            }
        )
    write_csv(MANIFEST, rows, fields)


def main() -> None:
    task_rows = read_csv(TASK_SHELL)
    prepare_locked_template(task_rows)
    prepare_run_matrix(task_rows)
    prepare_source_rendering_manifest()
    prepare_repeatability_subset(task_rows)
    prepare_manifest()

    repeatability_rows = read_csv(REPEATABILITY_SUBSET)
    print(f"task_rows={len(task_rows)}")
    print(f"locked_template={LOCKED_TEMPLATE.relative_to(REPO)}")
    print(f"run_matrix={RUN_MATRIX.relative_to(REPO)}")
    print(f"repeatability_subset_rows={len(repeatability_rows)}")
    print("denominator_family_counts=", dict(Counter(row["denominator_family"] for row in task_rows)))


if __name__ == "__main__":
    main()
