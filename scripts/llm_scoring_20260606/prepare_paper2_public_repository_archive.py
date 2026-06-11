#!/usr/bin/env python3
"""Prepare a share-safe Paper 2 public repository archive.

The archive is a local OSF/Zenodo-ready folder. It intentionally excludes raw
PDFs, raw human coder workbooks, and private OneDrive-only files. It preserves
model provenance instead of relabeling older runs.
"""

from __future__ import annotations

import csv
import hashlib
import shutil
from dataclasses import dataclass
from pathlib import Path


REPO = Path(__file__).resolve().parents[2]
DATE = "20260611"
ARCHIVE = REPO / f"paper_b/public_data_repository_{DATE}"
OSF_URL = "https://osf.io/mkrgd/overview"
TEXT_SUFFIXES = {
    ".csv",
    ".json",
    ".md",
    ".py",
    ".r",
    ".R",
    ".sh",
    ".txt",
    ".yaml",
    ".yml",
}


@dataclass(frozen=True)
class ArchiveItem:
    source: Path
    target: Path
    share_class: str
    role: str
    notes: str = ""


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def copy_item(item: ArchiveItem) -> dict[str, str]:
    target = ARCHIVE / item.target
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(item.source, target)
    sanitize_public_text_file(target)
    return {
        "archive_path": str(item.target),
        "source_path": str(item.source.relative_to(REPO)),
        "bytes": str(target.stat().st_size),
        "sha256": sha256(target),
        "share_class": item.share_class,
        "role": item.role,
        "notes": item.notes,
    }


def sanitize_public_text_file(path: Path) -> None:
    if path.suffix not in TEXT_SUFFIXES:
        return
    try:
        text = path.read_text(encoding="utf-8-sig")
    except UnicodeDecodeError:
        return
    private_docs_root = (
        Path.home()
        / "Library/CloudStorage/OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity"
        / "AI Adoption Meta Analysis - Documents"
    )
    replacements = {
        str(private_docs_root): "<PRIVATE_AI_ADOPTION_DOCUMENTS_ROOT>",
        str(REPO): "<REPO_ROOT>",
        str(Path.home()): "<USER_HOME>",
        "Library/CloudStorage/OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity": "<PRIVATE_ONEDRIVE_SHARED_LIBRARY>",
        "OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity": "<PRIVATE_ONEDRIVE_SHARED_LIBRARY>",
    }
    sanitized = text
    for old, new in replacements.items():
        sanitized = sanitized.replace(old, new)
    if sanitized != text:
        with path.open("w", encoding="utf-8", newline="") as handle:
            handle.write(sanitized)


def existing(paths: list[Path]) -> list[Path]:
    return [path for path in paths if path.exists() and path.is_file()]


def glob_files(pattern: str) -> list[Path]:
    return sorted(path for path in REPO.glob(pattern) if path.is_file())


def locked_model_outputs_from_manifest() -> list[Path]:
    manifest = (
        REPO
        / "data/04_extraction/05_llm_masem_substitution/locked_outputs/LOCKED_OUTPUT_MANIFEST_20260606.csv"
    )
    if not manifest.exists():
        return []
    paths: list[Path] = []
    with manifest.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            if row.get("artifact_role") != "locked_model_output":
                continue
            if row.get("locked_status") != "locked_model_output":
                continue
            path = Path(row.get("file", ""))
            if not path.is_absolute():
                path = REPO / path
            if path.exists() and path.is_file() and path.parent.name == "model_runs":
                paths.append(path)
    return sorted(set(paths))


def locked_full_corpus_outputs_from_manifest() -> list[Path]:
    manifest = (
        REPO
        / "data/04_extraction/05_llm_masem_substitution/locked_outputs/FULL_CORPUS_LOCKED_OUTPUT_MANIFEST_20260609.csv"
    )
    if not manifest.exists():
        return []
    paths: list[Path] = []
    with manifest.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            if row.get("artifact_role") != "locked_model_output":
                continue
            if row.get("locked_status") != "locked_model_output":
                continue
            path = Path(row.get("file", ""))
            if not path.is_absolute():
                path = REPO / path
            if path.exists() and path.is_file() and path.parent.name == "model_runs":
                paths.append(path)
    return sorted(set(paths))


def model_run_notes(path: Path) -> str:
    name = path.name
    if "paper_b_full_corpus_m1_raw_bounded_shard_0090" in name:
        return "Codex GPT-5.5 bounded 90-row M1-R diagnostic shard with private source packets; not a full-corpus replacement claim."
    if "paper_b_full_corpus_m1_raw_source_rendered_beta_path_contract_probe" in name:
        return "Codex GPT-5.5 beta/path source-rendered contract probe; diagnostic exception-layer evidence only."
    if "paper_b_full_corpus_m1_raw_source_rendered" in name or "paper_b_full_corpus_m1_raw_smoke" in name:
        return "Codex GPT-5.5 full-corpus M1-R smoke/probe output; pipeline validation only."
    if "gemini3flash_api_humandisagree_probe_7400" in name:
        return "Gemini 3 Flash API tail row; legacy probe filename but manifest-registered as clean locked output."
    if "probe" in name:
        return "Manifest-registered clean probe or smoke file; use as pipeline validation unless a decision record states it is part of final coverage."
    if "claude_sonnet" in name:
        return "Claude Sonnet locked output shard; use for Claude primary comparison when full coverage is complete."
    if "claude_full_allfamilies" in name:
        return "Legacy Claude Code default-unspecified shard; retained for audit provenance, not relabeled as Sonnet."
    if "codex_gpt55" in name:
        return "Codex GPT-5.5 locked output shard."
    if "gemini3flash" in name:
        return "Gemini 3 Flash locked output shard."
    return "Locked model output shard or probe; see model run matrix before analysis use."


def build_items() -> list[ArchiveItem]:
    items: list[ArchiveItem] = []

    for path in glob_files("paper_b/prompts/*.md"):
        items.append(
            ArchiveItem(path, Path("1_Prompts") / path.name, "public", "prompt_module")
        )
    for path in glob_files("data/04_extraction/05_llm_masem_substitution/schemas/*"):
        items.append(
            ArchiveItem(
                path,
                Path("1_Prompts/schemas") / path.name,
                "public",
                "locked_output_schema",
            )
        )
    for path in glob_files("data/04_extraction/05_llm_masem_substitution/scoring_rules/*"):
        items.append(
            ArchiveItem(
                path,
                Path("1_Prompts/scoring_rules") / path.name,
                "public",
                "scoring_rule",
            )
        )

    locked_root = Path("data/04_extraction/05_llm_masem_substitution/locked_outputs")
    for path in existing(
        [
            REPO / locked_root / "LOCKED_OUTPUT_MANIFEST_20260606.csv",
            REPO / locked_root / "MODEL_RUN_MATRIX_20260606.csv",
            REPO / locked_root / "paper2_locked_output_template_20260606.csv",
            REPO / locked_root / "FULL_CORPUS_LOCKED_OUTPUT_MANIFEST_20260609.csv",
            REPO / locked_root / "FULL_CORPUS_MODEL_PROCEDURE_RUN_MATRIX_20260609.csv",
            REPO / locked_root / "FULL_CORPUS_PRE_RUN_AUTHORIZATION_PACKET_20260609.md",
            REPO / locked_root / "full_corpus_locked_output_template_20260609.csv",
        ]
    ):
        items.append(
            ArchiveItem(
                path,
                Path("2_Raw_AI_Outputs/metadata") / path.name,
                "public",
                "locked_output_metadata",
            )
        )
    for path in locked_model_outputs_from_manifest():
        items.append(
            ArchiveItem(
                path,
                Path("2_Raw_AI_Outputs/model_runs") / path.name,
                "public_with_provenance",
                "locked_model_output",
                model_run_notes(path),
            )
        )
    for path in locked_full_corpus_outputs_from_manifest():
        items.append(
            ArchiveItem(
                path,
                Path("2_Raw_AI_Outputs/full_corpus_model_runs") / path.name,
                "public_with_provenance",
                "locked_model_output",
                model_run_notes(path),
            )
        )

    result_patterns = [
        "data/04_extraction/05_llm_masem_substitution/results/paper2_*.csv",
        "data/04_extraction/05_llm_masem_substitution/results/PAPER2_*.md",
        "data/04_extraction/05_llm_masem_substitution/results/SCORING_STATUS_20260606.md",
        "data/04_extraction/05_llm_masem_substitution/results/full_corpus_*.csv",
        "data/04_extraction/05_llm_masem_substitution/results/FULL_CORPUS_*.md",
        "data/04_extraction/05_llm_masem_substitution/results/paper_b_full_corpus_*.csv",
        "data/04_extraction/05_llm_masem_substitution/results/pdf_source_text_audit_20260611/PAPER2_POINTER_ONLY_PDF_SOURCE_TEXT_AUDIT_20260611.md",
        "data/04_extraction/05_llm_masem_substitution/results/r_masem_readiness_20260611/*",
        "data/04_extraction/05_llm_masem_substitution/results/r_masem_readiness_n_reconciled_20260611/*",
        "data/04_extraction/05_llm_masem_substitution/results/r_tssem_substitution_20260611/*.csv",
        "data/04_extraction/05_llm_masem_substitution/results/r_tssem_substitution_20260611/*.md",
    ]
    for pattern in result_patterns:
        for path in glob_files(pattern):
            items.append(
                ArchiveItem(
                    path,
                    Path("4_Analysis_Outputs") / path.relative_to(REPO / "data/04_extraction/05_llm_masem_substitution/results"),
                    "public_derived",
                    "analysis_output",
                )
            )

    source_rendering_files = [
        "data/04_extraction/07_paper_c_harness_benchmark/00_manifest/SOURCE_RENDERING_BOUNDED_M1R_SHARD_PACKET_STATUS_20260611.md",
        "data/04_extraction/07_paper_c_harness_benchmark/00_manifest/source_rendering_bounded_m1r_shard_packet_manifest_20260611.csv",
        "data/04_extraction/07_paper_c_harness_benchmark/06_rerun_bundles/source_rendered_bounded_m1r_shard_task_ids_20260611.csv",
        "data/04_extraction/07_paper_c_harness_benchmark/06_rerun_bundles/source_rendered_bounded_m1r_shard_packet_smoke_task_ids_20260611.csv",
    ]
    for path in existing([REPO / rel for rel in source_rendering_files]):
        items.append(
            ArchiveItem(
                path,
                Path("3_Source_Rendering_Audit") / path.relative_to(
                    REPO / "data/04_extraction/07_paper_c_harness_benchmark"
                ),
                "public_derived",
                "source_rendering_manifest_or_task_bundle",
                "Share-safe manifest or task bundle; private packet text and PDF paths are excluded.",
            )
        )

    for path in glob_files("scripts/llm_scoring_20260606/*.py"):
        items.append(
            ArchiveItem(path, Path("4_Analysis/scripts/llm_scoring_20260606") / path.name, "public", "analysis_script")
        )
    for path in glob_files("paper_b/scripts/*"):
        items.append(
            ArchiveItem(path, Path("4_Analysis/scripts/paper_b") / path.name, "public", "analysis_script")
        )

    for path in glob_files("paper_b/checklists/*.md"):
        items.append(
            ArchiveItem(path, Path("5_Checklists") / path.name, "public", "reporting_checklist")
        )

    protocol_files = [
        "paper_b/ANALYSIS_PLAN.md",
        "paper_b/CODING_PROTOCOL.md",
        "paper_b/PAPER_B_DOCUMENT_GENERATION_PLAN.md",
        "paper_b/PAPER_B_TASK_CONTINGENT_AUGMENTATION_MEMO.md",
        "paper_b/PAPER_B_TOLERANCE_AND_DECISION_RULES.md",
        "paper_b/manuscript/README.md",
        "paper_b/manuscript/PAPER_B_METHODS_RESULTS_DRAFT_20260611.md",
        "docs/06_decisions/2026-04-25_Reference_Standard_and_Disagreement_Analysis.md",
        "docs/06_decisions/2026-05-28_Paper_B_Tolerance_Bands_and_Decision_Rules.md",
        "docs/06_decisions/2026-06-11_Paper_B_Canonical_Reference_and_Model_Framing.md",
        "data/04_extraction/README.md",
        "data/04_extraction/WORKFLOW_STATUS_LOG.md",
        "data/04_extraction/04_reference_standard_freeze/paper2_reference_standard_freeze_note.md",
        "data/04_extraction/05_llm_masem_substitution/README.md",
        "data/04_extraction/05_llm_masem_substitution/RUNBOOK_20260606.md",
        "data/04_extraction/05_llm_masem_substitution/MODEL_FAMILY_EXTENSION_PLAN_20260607.md",
    ]
    for path in existing([REPO / rel for rel in protocol_files]):
        items.append(
            ArchiveItem(
                path,
                Path("6_Protocol_and_Decisions") / path.relative_to(REPO),
                "public_context",
                "protocol_or_decision_record",
            )
        )

    return items


def write_text_files(manifest_rows: list[dict[str, str]]) -> None:
    ARCHIVE.mkdir(parents=True, exist_ok=True)
    readme = f"""# Paper 2 Public Data Repository Archive

Date prepared: 2026-06-11

This local archive is prepared for the OSF public repository:
{OSF_URL}. It contains share-safe prompts, schemas, locked model output metadata,
manifest-registered locked model output CSVs, derived analysis outputs, scripts, reporting checklists, and
decision records for the Paper 2 LLM-assisted MASEM extraction study.

The human reference should be described as the source-anchored adjudicated human
reference standard. Do not describe it as a gold standard. Raw PDFs, raw human
coder workbooks, and private OneDrive-only materials are excluded from this
archive.

Public copies of text artifacts replace local machine and OneDrive paths with
placeholders such as `<REPO_ROOT>` and `<PRIVATE_AI_ADOPTION_DOCUMENTS_ROOT>`.

## Top-Level Structure

- `1_Prompts/`: prompt modules, scoring rules, and locked-output schemas.
- `2_Raw_AI_Outputs/`: manifest-registered locked model output shards and
  provenance metadata.
- `3_Source_Rendering_Audit/`: share-safe source-rendering manifests and task
  bundles; private packet text and PDF paths are excluded.
- `4_Analysis_Outputs/`: RQ1-RQ3 outputs, expert-review layers, MASEM bridge
  outputs, and redacted PDF source-text audit summaries. Row-level PDF text
  snippets and local PDF paths are excluded.
- `4_Analysis/scripts/`: scripts needed to recreate scoring and derived outputs.
- `5_Checklists/`: reporting checklist materials.
- `6_Protocol_and_Decisions/`: methods, decision logs, and workflow records.

## Provenance Boundary

Claude output provenance is preserved exactly. Shards with `claude_code` or
`claude_full_allfamilies` names are legacy default-unspecified Claude Code
outputs and are not relabeled as Sonnet. Shards with `claude_sonnet` in the
run ID are Sonnet runs. The 2026-06-11 Sonnet backfill shards for `0000-3999`
plus the existing Sonnet continuation shards should be used for the Claude
Sonnet comparison. Legacy default Claude runs are retained only as audit
provenance.

## Manifest

`MANIFEST.csv` and `CHECKSUMS_SHA256.csv` list every copied/generated file and
checksum. Copied source file count before generated archive documentation:
{len(manifest_rows)}. The final manifest also includes the generated archive
documentation files.
"""
    (ARCHIVE / "README.md").write_text(readme, encoding="utf-8")

    data_statement = f"""# Data Availability Statement

The public repository contains prompts, schemas, scoring rules,
manifest-registered locked model output CSVs, derived scoring outputs,
redacted source-text audit summaries, R/metaSEM readiness and bounded TSSEM
diagnostic outputs, analysis scripts, reporting checklists, and decision records
sufficient to inspect and reproduce the Paper 2 LLM evaluation and
substitution-stability pipeline.

Repository URL: {OSF_URL}

Raw article PDFs, raw human coder workbooks, row-level PDF text snippets, and
local PDF paths are not redistributed because they are copyrighted or private
project materials. Text artifacts in this archive use placeholder paths rather
than local machine or OneDrive locations. The analysis uses a source-anchored
adjudicated human reference standard derived from human review; public release
of any row-level human reference file must preserve source boundaries and
exclude copyrighted source text.

Downstream MASEM claims require explicit sample-size handling. As of this
archive, the deterministic reconciliation fills numeric `sample_size_numeric`
for 741 of 804 substitution rerun rows. The remaining 63 rows are excluded from
N-weighted TSSEM/MASEM weighting unless a later source check supplies numeric
N. R/metaSEM readiness, eligible-subset inputs, and a bounded core-6
complete-case TSSEM diagnostic are included, but final all-construct/all-row
structural-path or model-fit claims still require the final approved model
specification and documented handling of excluded missing-N rows.
"""
    (ARCHIVE / "DATA_AVAILABILITY_STATEMENT.md").write_text(data_statement, encoding="utf-8")

    exclusions = """# Excluded Private Or Restricted Materials

The following materials are intentionally excluded from this public archive:

- Raw PDFs and article files.
- Raw human coder workbooks, including `.xlsx` freeze-candidate files.
- OneDrive-only private source packets and working folders.
- Large rendered manuscript QA folders unless explicitly prepared for public
  sharing.
- Any credential, API key, local cache, or `.longtable` runtime state.

Use the manifest to identify share-safe derived artifacts. Do not add raw source
documents to a public repository without rights review.
"""
    (ARCHIVE / "EXCLUDED_PRIVATE_MATERIALS.md").write_text(exclusions, encoding="utf-8")

    boundary = f"""# Claim Boundary and Provenance Note

Repository URL: {OSF_URL}

This archive supports a paper claim that a prespecified LLM workflow can be
evaluated against a source-anchored adjudicated human reference standard and can
be used for bounded substitution-stability diagnostics.

The 2026-06-11 bounded 90-row full-corpus M1-R shard is diagnostic evidence for
the source-rendered extraction path. It is not a full-corpus LLM accuracy or
replacement claim.

It does not support an unrestricted replacement claim. Model performance must be
reported by denominator family and source condition. Pointer-only source rows
require the PDF source-text audit boundary. Rows where the audit did not locate
the numeric value in extracted PDF text require manual table review or OCR
before they can be upgraded.

Claude provenance must remain exact: default-unspecified Claude Code outputs are
not Sonnet outputs. The 2026-06-11 Sonnet-labeled `0000-3999` backfill plus the
existing Sonnet continuation provide the Claude Sonnet comparison rows; legacy
default-unspecified Claude Code rows are audit provenance only.
"""
    (ARCHIVE / "PROVENANCE_AND_CLAIM_BOUNDARY.md").write_text(boundary, encoding="utf-8")


def write_manifest(rows: list[dict[str, str]]) -> None:
    fields = ["archive_path", "source_path", "bytes", "sha256", "share_class", "role", "notes"]
    with (ARCHIVE / "MANIFEST.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    with (ARCHIVE / "CHECKSUMS_SHA256.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["sha256", "archive_path", "bytes"])
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    "sha256": row["sha256"],
                    "archive_path": row["archive_path"],
                    "bytes": row["bytes"],
                }
            )


def main() -> None:
    if ARCHIVE.exists():
        shutil.rmtree(ARCHIVE)
    ARCHIVE.mkdir(parents=True)

    rows = [copy_item(item) for item in build_items()]
    rows.sort(key=lambda row: row["archive_path"])
    write_text_files(rows)

    for generated in [
        ARCHIVE / "README.md",
        ARCHIVE / "DATA_AVAILABILITY_STATEMENT.md",
        ARCHIVE / "EXCLUDED_PRIVATE_MATERIALS.md",
        ARCHIVE / "PROVENANCE_AND_CLAIM_BOUNDARY.md",
    ]:
        rows.append(
            {
                "archive_path": generated.name,
                "source_path": "generated",
                "bytes": str(generated.stat().st_size),
                "sha256": sha256(generated),
                "share_class": "public_context",
                "role": "archive_documentation",
                "notes": "Generated by prepare_paper2_public_repository_archive.py.",
            }
        )

    rows.sort(key=lambda row: row["archive_path"])
    write_manifest(rows)
    print({"archive": str(ARCHIVE), "files": len(rows)})


if __name__ == "__main__":
    main()
