#!/usr/bin/env python3
"""Trace ANX-TRU candidates across repo, OneDrive, and mounted SSD CSV files."""

from __future__ import annotations

import csv
from collections import Counter
from datetime import date
from pathlib import Path


REPO = Path(__file__).resolve().parents[2]
RESULTS = REPO / "data/04_extraction/05_llm_masem_substitution/results"
ONEDRIVE = (
    Path("/Users/newhosung/Library/CloudStorage/OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity")
    / "AI Adoption Meta Analysis - Documents"
)
SSD_ROOTS = [
    Path("/Volumes/External SSD/Projects/Meta-Analysis/journal_AI-adoption_meta"),
    Path("/Volumes/External SSD/Projects/Meta-Analysis/dissertation_AI-adoption_meta"),
    Path("/Volumes/External SSD/Projects/Research/AI-Adoption"),
    Path("/Volumes/External SSD/Projects/GoogleDrive/Academic"),
]

TRACE_CSV = RESULTS / "paper_a_anx_tru_source_trace_extended_20260612.csv"
UNIQUE_CSV = RESULTS / "paper_a_anx_tru_unique_candidate_trace_extended_20260612.csv"
REPORT_MD = RESULTS / "PAPER_A_ANX_TRU_SOURCE_TRACE_EXTENDED_20260612.md"

SKIP_PARTS = {
    ".git",
    "__pycache__",
    "node_modules",
    "source_packets",
    "source_renderings_20260609_full_coverage",
    "model_runs",
    "render_paper_a_apa7_intro_method_results_20260611_qa3",
    "render_paper_b_apa7_intro_method_results_20260611_qa3",
}
MAX_BYTES = 250_000_000


def should_skip(path: Path) -> bool:
    if path.name.lower().startswith("paper_a_anx_tru") or path.name.lower().startswith("paper2_anx_tru"):
        return True
    if path.name.upper().startswith("PAPER_A_ANX_TRU"):
        return True
    if any(part in SKIP_PARTS for part in path.parts):
        return True
    try:
        return path.stat().st_size > MAX_BYTES
    except OSError:
        return True


def iter_csv_files(root: Path) -> list[Path]:
    if not root.exists():
        return []
    files: list[Path] = []
    for path in root.rglob("*"):
        if should_skip(path):
            continue
        if path.suffix.lower() in {".csv", ".tsv"}:
            files.append(path)
    return files


def normalize_pair(value: str) -> str:
    text = value.strip().upper().replace("_", "-").replace(" ", "-")
    if text in {"ANX-TRU", "TRU-ANX"}:
        return "ANX-TRU"
    return ""


def row_pair(row: dict[str, str]) -> str:
    for key in (
        "construct_pair",
        "pair",
        "pair_key",
        "canonical_pair",
        "construct_pair_key",
        "reference_construct_pair",
        "source_construct_pair",
        "analysis_construct_pair",
    ):
        pair = normalize_pair(row.get(key, ""))
        if pair:
            return pair

    left_keys = ("construct_1", "construct_a", "from_construct", "predictor_construct", "x_construct")
    right_keys = ("construct_2", "construct_b", "to_construct", "outcome_construct", "y_construct")
    for left_key in left_keys:
        for right_key in right_keys:
            left = row.get(left_key, "").strip().upper()
            right = row.get(right_key, "").strip().upper()
            if {left, right} == {"ANX", "TRU"}:
                return "ANX-TRU"

    for value in row.values():
        pair = normalize_pair(str(value))
        if pair:
            return pair
    return ""


def collection_for(path: Path) -> str:
    if path.is_relative_to(REPO):
        return "current_repo"
    if path.is_relative_to(ONEDRIVE):
        return "onedrive_documents"
    for root in SSD_ROOTS:
        if root.exists() and path.is_relative_to(root):
            return f"ssd:{root.name}"
    return "other"


def read_rows(path: Path) -> list[dict[str, str]]:
    delimiter = "\t" if path.suffix.lower() == ".tsv" else ","
    with path.open(newline="", encoding="utf-8-sig", errors="replace") as handle:
        reader = csv.DictReader(handle, delimiter=delimiter)
        if not reader.fieldnames:
            return []
        return list(reader)


def source_type(row: dict[str, str]) -> str:
    for key in (
        "source_type",
        "r_source",
        "reference_r_source",
        "statistic_family",
        "evidence_type",
        "reference_evidence_type",
        "denominator_family",
        "source_type_class",
    ):
        value = row.get(key, "").strip()
        if value:
            return value
    return ""


def numeric_value(row: dict[str, str]) -> str:
    for key in (
        "r_numeric",
        "r",
        "value",
        "reference_r_value",
        "r_numeric_or_reference",
        "effect_size",
        "beta",
        "path_coefficient",
        "final_value",
        "adjudicated_value",
        "consensus_value",
    ):
        value = row.get(key, "").strip()
        if value:
            return value
    return ""


def classify(row: dict[str, str], path: Path) -> str:
    name = path.name.lower()
    stype = source_type(row).lower()
    denom = row.get("denominator_family", "").lower()
    include_primary = row.get("include_primary", "").strip().lower()
    if "absence" in stype or "blank" in stype:
        return "absence_or_blank_trace"
    if not numeric_value(row) and not stype and not denom:
        return "absence_or_blank_trace"
    if "primary_model_ready" in name or "primary_analysis_ready" in name or include_primary in {"1", "true", "yes"}:
        return "legacy_or_current_primary_candidate"
    if "direct" in stype or "direct_r" in denom or "source-r" in denom:
        return "direct_r_like_candidate"
    if "latent" in stype or "fornell" in stype or "latent" in denom:
        return "latent_source_flagged_candidate"
    if "converted" in stype or "beta" in stype or "path" in stype or "converted" in denom or "beta" in denom:
        return "beta_path_or_source_statistic_converted_candidate"
    if "template" in name or "shell" in name:
        return "template_or_shell_trace"
    return "candidate_review_required"


def md_table(rows: list[dict[str, object]], cols: list[str]) -> str:
    lines = ["| " + " | ".join(cols) + " |", "| " + " | ".join(["---"] * len(cols)) + " |"]
    for row in rows:
        lines.append("| " + " | ".join(str(row.get(col, "")) for col in cols) + " |")
    return "\n".join(lines)


def main() -> None:
    roots = [
        REPO,
        ONEDRIVE / "Meta/AI Adoption/Paper1_MASEM_Working_20260605",
        ONEDRIVE / "Meta/AI Adoption/Paper2_Human_Final_Consensus_20260605_v2",
        ONEDRIVE / "Meta/AI Adoption/Paper2_LLM_Extraction_Working_20260605",
        ONEDRIVE / "Meta/AI Adoption/Paper2_Analysis_Input_20260530",
        ONEDRIVE / "Git/journal_AI-adoption_meta",
        *SSD_ROOTS,
    ]

    trace_rows: list[dict[str, object]] = []
    scanned_files = 0
    failed_files: list[str] = []
    for root in roots:
        for path in iter_csv_files(root):
            scanned_files += 1
            try:
                rows = read_rows(path)
            except (OSError, csv.Error, UnicodeDecodeError) as exc:
                failed_files.append(f"{path}: {type(exc).__name__}")
                continue
            for index, row in enumerate(rows, start=2):
                pair = row_pair(row)
                if pair != "ANX-TRU":
                    continue
                trace_rows.append(
                    {
                        "collection": collection_for(path),
                        "source_file": str(path),
                        "file_name": path.name,
                        "line_or_row": index,
                        "study_id": row.get("study_id") or row.get("Study ID") or row.get("study") or "",
                        "analysis_record_id": row.get("analysis_record_id", ""),
                        "task_unit_id": row.get("task_unit_id", ""),
                        "reference_record_id": row.get("reference_record_id", ""),
                        "construct_pair": pair,
                        "numeric_value": numeric_value(row),
                        "source_type": source_type(row),
                        "denominator_family": row.get("denominator_family", ""),
                        "include_primary": row.get("include_primary", ""),
                        "include_expanded": row.get("include_expanded", ""),
                        "include_sensitivity": row.get("include_sensitivity", ""),
                        "classification": classify(row, path),
                    }
                )

    fields = [
        "collection",
        "source_file",
        "file_name",
        "line_or_row",
        "study_id",
        "analysis_record_id",
        "task_unit_id",
        "reference_record_id",
        "construct_pair",
        "numeric_value",
        "source_type",
        "denominator_family",
        "include_primary",
        "include_expanded",
        "include_sensitivity",
        "classification",
    ]
    RESULTS.mkdir(parents=True, exist_ok=True)
    with TRACE_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(trace_rows)

    unique: dict[tuple[str, str, str, str, str], dict[str, object]] = {}
    for row in trace_rows:
        if str(row["classification"]) == "absence_or_blank_trace":
            continue
        if not str(row["numeric_value"]).strip():
            continue
        key = (
            str(row["study_id"]),
            str(row["construct_pair"]),
            str(row["numeric_value"]),
            str(row["source_type"]),
            str(row["classification"]),
        )
        if key not in unique:
            unique[key] = {
                "study_id": row["study_id"],
                "construct_pair": row["construct_pair"],
                "numeric_value": row["numeric_value"],
                "source_type": row["source_type"],
                "classification": row["classification"],
                "collections": set(),
                "source_files": set(),
            }
        unique[key]["collections"].add(row["collection"])
        unique[key]["source_files"].add(row["file_name"])

    unique_rows: list[dict[str, object]] = []
    for row in unique.values():
        unique_rows.append(
            {
                "study_id": row["study_id"],
                "construct_pair": row["construct_pair"],
                "numeric_value": row["numeric_value"],
                "source_type": row["source_type"],
                "classification": row["classification"],
                "collections": ";".join(sorted(row["collections"])),
                "source_files": ";".join(sorted(row["source_files"])),
            }
        )
    unique_rows.sort(key=lambda row: (str(row["study_id"]), str(row["classification"]), str(row["numeric_value"])))

    unique_fields = [
        "study_id",
        "construct_pair",
        "numeric_value",
        "source_type",
        "classification",
        "collections",
        "source_files",
    ]
    with UNIQUE_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=unique_fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(unique_rows)

    candidate_trace_rows = [
        row
        for row in trace_rows
        if str(row["classification"]) != "absence_or_blank_trace" and str(row["numeric_value"]).strip()
    ]
    absence_trace_rows = [row for row in trace_rows if str(row["classification"]) == "absence_or_blank_trace"]
    by_collection = Counter(str(row["collection"]) for row in trace_rows)
    by_candidate_collection = Counter(str(row["collection"]) for row in candidate_trace_rows)
    by_classification = Counter(str(row["classification"]) for row in unique_rows)
    by_study = Counter(str(row["study_id"]) for row in unique_rows if row["study_id"])

    report = f"""# Paper A ANX-TRU Extended Source Trace

Date: {date.today().isoformat()}

## Purpose

This trace answers why `ANX-TRU` could have appeared to have available rows
while still being absent from the legacy 2026-06-05 Paper A primary direct-r
matrix. The search is restricted to CSV/TSV artifacts that the analysis
pipeline can actually consume. Raw XLSX workbooks are preserved as raw coder
records and are not used directly as final model inputs.

## Search Scope

- Current repo: `{REPO}`
- OneDrive Paper1/Paper2 working and consensus folders under `{ONEDRIVE}`
- Mounted SSD candidate folders: `{'; '.join(str(p) for p in SSD_ROOTS if p.exists())}`

Scanned CSV/TSV files: {scanned_files}
Files skipped or unreadable: {len(failed_files)}
Raw trace rows including blank/absence traces: {len(trace_rows)}
Blank/absence trace rows separated from candidates: {len(absence_trace_rows)}
Numeric source-type candidate trace rows: {len(candidate_trace_rows)}
Deduplicated numeric source-type candidates: {len(unique_rows)}

## Trace Hits by Collection

{md_table([{"collection": k, "rows": v} for k, v in sorted(by_collection.items())], ["collection", "rows"])}

## Numeric Candidate Hits by Collection

{md_table([{"collection": k, "rows": v} for k, v in sorted(by_candidate_collection.items())], ["collection", "rows"])}

## Unique Candidate Classes

{md_table([{"classification": k, "unique_candidates": v} for k, v in sorted(by_classification.items())], ["classification", "unique_candidates"])}

## Unique Studies

{md_table([{"study_id": k, "unique_candidates": v} for k, v in sorted(by_study.items())], ["study_id", "unique_candidates"])}

## Interpretation

The trace distinguishes evidence presence from primary-model eligibility. A row
can be present in a post-freeze shell, public metadata copy, latent-correlation
stratum, or converted beta/path stratum and still be absent from the 2026-06-05
legacy primary direct-r model-ready file. Therefore `ANX-TRU` should be reported
as a corpus-version and source-type boundary rather than as a simple literature
absence.

For the manuscript spine, the defensible action is to keep `ANX-TRU` in the
main results space as a source-type comparison panel, while not pooling direct-r,
latent, and converted-effect candidates into one primary TSSEM/OSMASEM estimate.

## Outputs

- `{TRACE_CSV.relative_to(REPO)}`
- `{UNIQUE_CSV.relative_to(REPO)}`
"""
    REPORT_MD.write_text(report, encoding="utf-8")
    print(
        "anx_tru_extended_trace_complete",
        f"scanned_files={scanned_files}",
        f"trace_rows={len(trace_rows)}",
        f"unique_candidates={len(unique_rows)}",
        f"failed_files={len(failed_files)}",
    )


if __name__ == "__main__":
    main()
