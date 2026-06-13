#!/usr/bin/env python3
"""Build pre-analysis processing gates for Paper A and Paper B.

The outputs are share-safe audit summaries. They do not edit source workbooks,
frozen references, PDFs, private source packets, or model outputs.
"""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path


REPO = Path(__file__).resolve().parents[2]
OUT = REPO / "docs" / "07_manuscript_exemplars" / "20260612" / "pre_analysis_processing"

PAPER_A_PRIMARY = Path(
    "/Users/newhosung/Library/CloudStorage/OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity/"
    "AI Adoption Meta Analysis - Documents/Meta/AI Adoption/"
    "Paper1_MASEM_Working_20260605/09_model_ready_tiered_freeze/"
    "paper1_direct_r_primary_model_ready_tiered_freeze_20260605.csv"
)

PAPER_B_SHELL = REPO / "data/04_extraction/05_llm_masem_substitution/full_corpus_step5_task_unit_shell_20260609.csv"
PAPER_B_TEMPLATE = REPO / "data/04_extraction/05_llm_masem_substitution/locked_outputs/full_corpus_locked_output_template_20260609.csv"
PAPER_B_MANIFEST = REPO / "data/04_extraction/07_paper_c_harness_benchmark/00_manifest/source_rendering_full_coverage_manifest_20260609.csv"
PAPER_B_PACKET_DIR = REPO / "data/04_extraction/07_paper_c_harness_benchmark/private/source_renderings_20260609_full_coverage/source_packets"
PAPER_B_EXCEPTION_LAYER = REPO / "data/04_extraction/05_llm_masem_substitution/results/full_corpus_m1_r_beta_path_exception_correction_layer_20260611.csv"
PAPER_A_EXISTING_N_RECON = REPO / "data/04_extraction/05_llm_masem_substitution/results/paper2_masem_sample_size_reconciliation_20260611.csv"
EXTERNAL_SSD_REPO = Path("/Volumes/External SSD/Projects/Meta-Analysis/jornal_AI-adoption_meta")
EXTERNAL_SSD_DISSERTATION = Path("/Volumes/External SSD/Projects/Meta-Analysis/dissertation_AI-adoption_meta")

TARGET_CONSTRUCTS = ["PE", "EE", "SI", "FC", "ATT", "SE", "TRU", "ANX", "BI", "UB"]

PAPER_A_RESIDUAL_N_SOURCE_CHECKS = {
    "S028": {
        "pdf_recovered_sample_size": "508",
        "pdf_source_location_checked": "S028.pdf sample/response reporting and Table 4 source context",
        "source_check_status": "pdf_study_level_n_candidate_found",
        "source_check_reason": "PDF reports 508 valid responses for the analytic survey sample; residual rows share the same study-level correlation table context.",
    },
    "S100": {
        "pdf_recovered_sample_size": "682",
        "pdf_source_location_checked": "S100.pdf Study 1 participant/sample reporting and Table 6 source context",
        "source_check_status": "pdf_study_level_n_candidate_found",
        "source_check_reason": "PDF reports 682 valid Study 1 survey responses; residual correlations are from the Study 1 quantitative table.",
    },
    "S145": {
        "pdf_recovered_sample_size": "374",
        "pdf_source_location_checked": "S145.pdf method/sample characteristics and Table 3 source context",
        "source_check_status": "pdf_study_level_n_candidate_found",
        "source_check_reason": "PDF reports 374 students in the survey sample; residual rows share the same model validity/correlation table context.",
    },
    "S185": {
        "pdf_recovered_sample_size": "298",
        "pdf_source_location_checked": "S185.pdf sample and collection/basic sample data plus Table 3 source context",
        "source_check_status": "pdf_study_level_n_candidate_found",
        "source_check_reason": "PDF reports N = 298 in the basic sample data; residual correlations are from the same questionnaire dataset.",
    },
    "S194": {
        "pdf_recovered_sample_size": "469",
        "pdf_source_location_checked": "S194.pdf data collection/sample-size reporting and Table 3 source context",
        "source_check_status": "pdf_study_level_n_candidate_found",
        "source_check_reason": "PDF reports 469 responses as the SmartPLS analytic sample; residual rows share the same correlation/table context.",
    },
    "S208": {
        "pdf_recovered_sample_size": "526",
        "pdf_source_location_checked": "S208.pdf participants section and Table 2 source context",
        "source_check_status": "pdf_study_level_n_candidate_found",
        "source_check_reason": "PDF reports 526 valid students after exclusions; residual rows share the same valid-sample analysis context.",
    },
    "S218": {
        "pdf_recovered_sample_size": "242",
        "pdf_source_location_checked": "S218.pdf participants section and Table 1 source context",
        "source_check_status": "pdf_study_level_n_candidate_found",
        "source_check_reason": "PDF reports 242 doctoral students participating in the study; residual rows share the same TAM survey dataset.",
    },
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, object]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row.get(k, "") for k in fieldnames})


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def parse_float(value: str | None) -> float | None:
    if value is None:
        return None
    value = str(value).strip()
    if not value:
        return None
    try:
        return float(value)
    except ValueError:
        return None


def pair_key(c1: str, c2: str) -> str:
    return "-".join(sorted([c1, c2]))


def row_construct_pair(row: dict[str, str]) -> str:
    c1 = row.get("construct_1") or row.get("Construct 1") or row.get("construct1") or ""
    c2 = row.get("construct_2") or row.get("Construct 2") or row.get("construct2") or ""
    if c1 and c2:
        return pair_key(c1.strip(), c2.strip())
    for key in ("construct_pair", "construct_pair_canonical", "source_pair", "field_or_construct_pair"):
        value = row.get(key, "").strip()
        if value in {"ANX-TRU", "TRU-ANX"}:
            return "ANX-TRU"
    return ""


def contains_anx_tru(row: dict[str, str]) -> bool:
    if row_construct_pair(row) == "ANX-TRU":
        return True
    values = "\t".join(str(v) for v in row.values())
    return "ANX-TRU" in values or "TRU-ANX" in values


def expected_pairs() -> list[str]:
    pairs: list[str] = []
    for i, c1 in enumerate(TARGET_CONSTRUCTS):
        for c2 in TARGET_CONSTRUCTS[i + 1 :]:
            pairs.append(pair_key(c1, c2))
    return sorted(pairs)


def md_table(rows: list[dict[str, object]], cols: list[str]) -> str:
    lines = ["| " + " | ".join(cols) + " |", "| " + " | ".join(["---"] * len(cols)) + " |"]
    for row in rows:
        lines.append("| " + " | ".join(str(row.get(c, "")) for c in cols) + " |")
    return "\n".join(lines)


def build_paper_a() -> dict[str, object]:
    rows = read_csv(PAPER_A_PRIMARY)
    recon_rows = read_csv(PAPER_A_EXISTING_N_RECON) if PAPER_A_EXISTING_N_RECON.exists() else []
    recon_by_record = {r.get("analysis_record_id", ""): r for r in recon_rows}
    expected = expected_pairs()
    expected_set = set(expected)

    usable: list[dict[str, str]] = []
    for row in rows:
        c1 = row.get("construct_1", "").strip()
        c2 = row.get("construct_2", "").strip()
        r_value = parse_float(row.get("r_numeric"))
        if c1 in TARGET_CONSTRUCTS and c2 in TARGET_CONSTRUCTS and r_value is not None and abs(r_value) <= 1:
            row = dict(row)
            row["_pair"] = pair_key(c1, c2)
            row["_n"] = parse_float(row.get("sample_size_numeric"))
            recon = recon_by_record.get(row.get("analysis_record_id", ""))
            row["_n_reconciled"] = parse_float(recon.get("sample_size_numeric_reconciled") if recon else None)
            row["_n_recon_status"] = recon.get("sample_size_reconciliation_status", "no_reconciliation_record") if recon else "no_reconciliation_record"
            row["_n_recon_source"] = recon.get("sample_size_reconciliation_source", "") if recon else ""
            row["_n_eligibility"] = recon.get("masem_n_weighted_eligibility", "") if recon else ""
            row["_n_pdf_recovered"] = (
                parse_float(PAPER_A_RESIDUAL_N_SOURCE_CHECKS.get(row.get("study_id", ""), {}).get("pdf_recovered_sample_size"))
                if row["_n_reconciled"] is None
                else None
            )
            usable.append(row)

    pair_groups: dict[str, list[dict[str, str]]] = defaultdict(list)
    study_groups: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in usable:
        pair_groups[row["_pair"]].append(row)
        study_groups[row.get("study_id", "")].append(row)

    pair_rows: list[dict[str, object]] = []
    for pair in expected:
        group = pair_groups.get(pair, [])
        n_present = [r for r in group if r["_n"] is not None]
        n_reconciled = [r for r in group if r["_n_reconciled"] is not None]
        n_reconciled_or_pdf = [r for r in group if r["_n_reconciled"] is not None or r["_n_pdf_recovered"] is not None]
        if group and len(n_reconciled) == len(group):
            primary_gate = "n_reconciled_ready"
        elif group and len(n_reconciled_or_pdf) == len(group):
            primary_gate = "pdf_n_override_candidate_pending_confirmation"
        elif group:
            primary_gate = "needs_residual_source_n_check"
        else:
            primary_gate = "not_estimable_without_imputation_or_model_reduction"
        pair_rows.append(
            {
                "construct_pair": pair,
                "rows": len(group),
                "studies": len({r.get("study_id", "") for r in group if r.get("study_id", "")}),
                "rows_with_numeric_n": len(n_present),
                "rows_missing_numeric_n": len(group) - len(n_present),
                "rows_with_reconciled_numeric_n": len(n_reconciled),
                "rows_missing_after_reconciliation": len(group) - len(n_reconciled),
                "rows_with_reconciled_or_pdf_n_candidate": len(n_reconciled_or_pdf),
                "rows_missing_after_pdf_source_check": len(group) - len(n_reconciled_or_pdf),
                "n_status": "ready" if group and len(n_present) == len(group) else ("missing_n" if group else "no_rows"),
                "primary_gate": primary_gate,
            }
        )

    study_rows: list[dict[str, object]] = []
    for study_id, group in sorted(study_groups.items()):
        pairs = {r["_pair"] for r in group}
        n_values = sorted({str(r["_n"]) for r in group if r["_n"] is not None})
        n_reconciled_values = sorted({str(r["_n_reconciled"]) for r in group if r["_n_reconciled"] is not None})
        study_rows.append(
            {
                "study_id": study_id,
                "rows": len(group),
                "construct_pairs": len(pairs),
                "complete_10_construct_matrix": "yes" if len(pairs & expected_set) == len(expected) else "no",
                "pairs_missing_from_10_construct_target": len(expected_set - pairs),
                "rows_with_numeric_n": sum(1 for r in group if r["_n"] is not None),
                "rows_missing_numeric_n": sum(1 for r in group if r["_n"] is None),
                "rows_with_reconciled_numeric_n": sum(1 for r in group if r["_n_reconciled"] is not None),
                "rows_missing_after_reconciliation": sum(1 for r in group if r["_n_reconciled"] is None),
                "numeric_n_values_seen": ";".join(n_values),
                "reconciled_numeric_n_values_seen": ";".join(n_reconciled_values),
                "preanalysis_action": "residual_pdf_or_source_n_check_required" if any(r["_n_reconciled"] is None for r in group) else "n_ready_for_matrix_audit",
            }
        )

    row_recon_rows: list[dict[str, object]] = []
    for row in usable:
        row_recon_rows.append(
            {
                "analysis_record_id": row.get("analysis_record_id", ""),
                "study_id": row.get("study_id", ""),
                "construct_pair": row.get("_pair", ""),
                "sample_size_numeric_original": row.get("sample_size_numeric", ""),
                "sample_size_numeric_reconciled": "" if row["_n_reconciled"] is None else row["_n_reconciled"],
                "sample_size_reconciliation_status": row["_n_recon_status"],
                "sample_size_reconciliation_source": row["_n_recon_source"],
                "masem_n_weighted_eligibility": row["_n_eligibility"],
                "preanalysis_action": "include_n_weighted_subset_candidate" if row["_n_reconciled"] is not None else "residual_source_n_check_before_primary",
            }
        )

    write_csv(
        OUT / "paper_a_n_matrix_pair_audit_20260612.csv",
        pair_rows,
        [
            "construct_pair",
            "rows",
            "studies",
            "rows_with_numeric_n",
            "rows_missing_numeric_n",
            "rows_with_reconciled_numeric_n",
            "rows_missing_after_reconciliation",
            "rows_with_reconciled_or_pdf_n_candidate",
            "rows_missing_after_pdf_source_check",
            "n_status",
            "primary_gate",
        ],
    )
    write_csv(
        OUT / "paper_a_n_matrix_study_audit_20260612.csv",
        study_rows,
        [
            "study_id",
            "rows",
            "construct_pairs",
            "complete_10_construct_matrix",
            "pairs_missing_from_10_construct_target",
            "rows_with_numeric_n",
            "rows_missing_numeric_n",
            "rows_with_reconciled_numeric_n",
            "rows_missing_after_reconciliation",
            "numeric_n_values_seen",
            "reconciled_numeric_n_values_seen",
            "preanalysis_action",
        ],
    )
    write_csv(
        OUT / "paper_a_n_reconciliation_adoption_audit_20260612.csv",
        row_recon_rows,
        [
            "analysis_record_id",
            "study_id",
            "construct_pair",
            "sample_size_numeric_original",
            "sample_size_numeric_reconciled",
            "sample_size_reconciliation_status",
            "sample_size_reconciliation_source",
            "masem_n_weighted_eligibility",
            "preanalysis_action",
        ],
    )

    residual_row_queue = [row for row in row_recon_rows if row["preanalysis_action"] == "residual_source_n_check_before_primary"]
    residual_row_queue_enriched: list[dict[str, object]] = []
    source_lookup = {row.get("analysis_record_id", ""): row for row in usable}
    for row in residual_row_queue:
        source = source_lookup.get(str(row["analysis_record_id"]), {})
        n_source_check = PAPER_A_RESIDUAL_N_SOURCE_CHECKS.get(str(row["study_id"]), {})
        residual_row_queue_enriched.append(
            {
                **row,
                "source_location": source.get("source_location", ""),
                "source_artifact": source.get("source_artifact", ""),
                "source_locator": source.get("source_locator", ""),
                "current_gate_reason": "not filled by deterministic reconciliation; PDF source check required before any primary exclusion",
                "pdf_recovered_sample_size": n_source_check.get("pdf_recovered_sample_size", ""),
                "pdf_source_location_checked": n_source_check.get("pdf_source_location_checked", ""),
                "source_check_status": n_source_check.get("source_check_status", "pdf_source_check_not_yet_resolved"),
                "source_check_reason": n_source_check.get("source_check_reason", ""),
                "researcher_confirmation_required": "yes_before_applying_pdf_n_override_or_exclusion",
                "recommended_action_after_source_check": (
                    "apply_pdf_study_level_n_override_to_primary_n_weighted_masem"
                    if n_source_check
                    else "exclude_from_primary_n_weighted_tssem_masem_retain_in_sensitivity_ledger"
                ),
                "recommended_default_if_unresolved": "exclude_from_primary_n_weighted_tssem_masem_retain_in_sensitivity_ledger",
            }
        )

    residual_study_rows: list[dict[str, object]] = []
    residual_by_study: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in residual_row_queue_enriched:
        residual_by_study[str(row["study_id"])].append(row)
    for study_id, group in sorted(residual_by_study.items()):
        residual_study_rows.append(
            {
                "study_id": study_id,
                "residual_rows": len(group),
                "construct_pairs": ";".join(sorted({str(row["construct_pair"]) for row in group})),
                "source_artifacts": ";".join(sorted({str(row["source_artifact"]) for row in group if row["source_artifact"]})),
                "source_locations": ";".join(sorted({str(row["source_location"]) for row in group if row["source_location"]})),
                "pdf_recovered_sample_size": ";".join(sorted({str(row["pdf_recovered_sample_size"]) for row in group if row.get("pdf_recovered_sample_size")})),
                "source_check_status": ";".join(sorted({str(row["source_check_status"]) for row in group if row.get("source_check_status")})),
                "source_check_reason": "; ".join(sorted({str(row["source_check_reason"]) for row in group if row.get("source_check_reason")})),
                "gate_question_to_researcher": "Approve applying the PDF-recovered study-level N to these residual rows, instead of excluding them from primary N-weighted TSSEM/MASEM?",
                "why_question_is_required": "N changes TSSEM/MASEM weighting; applying a study-level PDF override or excluding the rows is a claim-boundary decision that must be explicit.",
                "recommended_action_after_source_check": ";".join(sorted({str(row["recommended_action_after_source_check"]) for row in group})),
                "recommended_default_if_unresolved": "exclude_from_primary_n_weighted_tssem_masem_retain_in_sensitivity_ledger",
            }
        )

    write_csv(
        OUT / "paper_a_residual_missing_n_row_queue_20260612.csv",
        residual_row_queue_enriched,
        [
            "analysis_record_id",
            "study_id",
            "construct_pair",
            "sample_size_numeric_original",
            "sample_size_numeric_reconciled",
            "sample_size_reconciliation_status",
            "sample_size_reconciliation_source",
            "masem_n_weighted_eligibility",
            "preanalysis_action",
            "source_location",
            "source_artifact",
            "source_locator",
            "current_gate_reason",
            "pdf_recovered_sample_size",
            "pdf_source_location_checked",
            "source_check_status",
            "source_check_reason",
            "researcher_confirmation_required",
            "recommended_action_after_source_check",
            "recommended_default_if_unresolved",
        ],
    )
    write_csv(
        OUT / "paper_a_residual_n_source_check_20260612.csv",
        residual_row_queue_enriched,
        [
            "analysis_record_id",
            "study_id",
            "construct_pair",
            "source_location",
            "pdf_recovered_sample_size",
            "pdf_source_location_checked",
            "source_check_status",
            "source_check_reason",
            "researcher_confirmation_required",
            "recommended_action_after_source_check",
        ],
    )
    write_csv(
        OUT / "paper_a_residual_missing_n_study_queue_20260612.csv",
        residual_study_rows,
        [
            "study_id",
            "residual_rows",
            "construct_pairs",
            "source_artifacts",
            "source_locations",
            "pdf_recovered_sample_size",
            "source_check_status",
            "source_check_reason",
            "gate_question_to_researcher",
            "why_question_is_required",
            "recommended_action_after_source_check",
            "recommended_default_if_unresolved",
        ],
    )

    metrics = {
        "input_rows": len(rows),
        "target_construct_usable_rows": len(usable),
        "rows_with_numeric_n": sum(1 for r in usable if r["_n"] is not None),
        "rows_missing_numeric_n": sum(1 for r in usable if r["_n"] is None),
        "rows_with_reconciled_numeric_n": sum(1 for r in usable if r["_n_reconciled"] is not None),
        "rows_missing_after_reconciliation": sum(1 for r in usable if r["_n_reconciled"] is None),
        "rows_with_pdf_recovered_n_candidate": sum(
            1 for r in residual_row_queue_enriched if r.get("pdf_recovered_sample_size")
        ),
        "rows_still_missing_after_pdf_source_check": sum(
            1 for r in residual_row_queue_enriched if not r.get("pdf_recovered_sample_size")
        ),
        "studies_with_pdf_recovered_n_candidate": len(
            {r.get("study_id") for r in residual_row_queue_enriched if r.get("pdf_recovered_sample_size")}
        ),
        "studies": len(study_groups),
        "covered_pairs": sum(1 for row in pair_rows if row["rows"]),
        "expected_pairs": len(expected),
        "complete_10_construct_studies": sum(1 for row in study_rows if row["complete_10_construct_matrix"] == "yes"),
        "studies_with_15_or_more_pairs": sum(1 for row in study_rows if int(row["construct_pairs"]) >= 15),
    }

    weakest = sorted(pair_rows, key=lambda r: (int(r["rows"]), int(r["studies"]), r["construct_pair"]))[:12]
    missing_studies = Counter(r.get("study_id", "") for r in usable if r["_n_reconciled"] is None)
    recon_status = Counter(r["_n_recon_status"] for r in usable)
    residual_source_check_studies = [
        {
            "study_id": row["study_id"],
            "residual_rows": row["residual_rows"],
            "pdf_recovered_sample_size": row["pdf_recovered_sample_size"],
            "source_check_status": row["source_check_status"],
            "recommended_action_after_source_check": row["recommended_action_after_source_check"],
        }
        for row in residual_study_rows
    ]

    report = f"""# Paper A Pre-Analysis N/Matrix Gate

Date: {date.today().isoformat()}

## Locked Recommendations

- Keep the 10-construct model as the theory target.
- Use pairwise source-supported N when available; otherwise use source-supported analytic sample N.
- If no defensible N can be recovered, exclude the row from primary N-weighted TSSEM/OSMASEM and retain it only in sensitivity/readiness ledgers.
- Exclude converted beta/path/source-statistic rows from the primary model; use them only in sensitivity analyses.
- Run a matrix sparsity and identification audit before any final TSSEM/OSMASEM claim.

## Input

`{PAPER_A_PRIMARY}`

## Current Gate Metrics

{md_table([
    {"metric": "Input rows", "value": metrics["input_rows"]},
    {"metric": "Usable 10-construct rows with valid r", "value": metrics["target_construct_usable_rows"]},
    {"metric": "Rows with numeric N", "value": metrics["rows_with_numeric_n"]},
    {"metric": "Rows missing numeric N", "value": metrics["rows_missing_numeric_n"]},
    {"metric": "Rows with reconciled numeric N", "value": metrics["rows_with_reconciled_numeric_n"]},
    {"metric": "Rows missing after reconciliation", "value": metrics["rows_missing_after_reconciliation"]},
    {"metric": "Rows with PDF-recovered N candidate", "value": metrics["rows_with_pdf_recovered_n_candidate"]},
    {"metric": "Rows still missing after PDF source check", "value": metrics["rows_still_missing_after_pdf_source_check"]},
    {"metric": "Studies with PDF-recovered N candidate", "value": metrics["studies_with_pdf_recovered_n_candidate"]},
    {"metric": "Studies represented", "value": metrics["studies"]},
    {"metric": "Construct-pair coverage", "value": f'{metrics["covered_pairs"]}/{metrics["expected_pairs"]}'},
    {"metric": "Complete 10-construct studies", "value": metrics["complete_10_construct_studies"]},
    {"metric": "Studies with >=15 pairs", "value": metrics["studies_with_15_or_more_pairs"]},
], ["metric", "value"])}

## Weakest Pair Coverage

{md_table(weakest, ["construct_pair", "rows", "studies", "rows_with_numeric_n", "rows_missing_numeric_n", "rows_with_reconciled_numeric_n", "rows_missing_after_reconciliation", "rows_with_reconciled_or_pdf_n_candidate", "rows_missing_after_pdf_source_check", "primary_gate"])}

## Existing N Reconciliation Adoption

The repo already contains a deterministic N reconciliation derived from the 2026-06-09 frozen full-corpus reference:

`{PAPER_A_EXISTING_N_RECON.relative_to(REPO)}`

{md_table([{"status": k, "rows": v} for k, v in sorted(recon_status.items())], ["status", "rows"])}

## Residual Missing-N Studies After Reconciliation

{md_table([{"study_id": k, "rows": v} for k, v in sorted(missing_studies.items())], ["study_id", "rows"])}

## PDF Source-Check Result for Residual N

{md_table(residual_source_check_studies, ["study_id", "residual_rows", "pdf_recovered_sample_size", "source_check_status", "recommended_action_after_source_check"])}

## Researcher Confirmation Gate

The missing-N exclusion rule remains the default only when no defensible source
N can be recovered. The PDF source check found study-level analytic/sample N
candidates for all 63 residual rows across 7 studies. Before final model input
mutation, the researcher must approve applying these PDF-recovered study-level
N values. The reason is methodological: N changes TSSEM/MASEM weighting, so
either applying a study-level override or excluding rows is a claim-boundary
decision that must be explicit.

## Stop Condition

All-row primary N-weighted TSSEM/OSMASEM is no longer blocked by source
availability for N, but it remains blocked until the researcher approves the
PDF-recovered N override. If approved, all 796 usable 10-construct rows have a
numeric N candidate before the separate matrix/identification gate.

## Outputs

- `paper_a_n_matrix_pair_audit_20260612.csv`
- `paper_a_n_matrix_study_audit_20260612.csv`
- `paper_a_n_reconciliation_adoption_audit_20260612.csv`
- `paper_a_residual_n_source_check_20260612.csv`
- `paper_a_residual_missing_n_row_queue_20260612.csv`
- `paper_a_residual_missing_n_study_queue_20260612.csv`
"""
    write_text(OUT / "PAPER_A_PREANALYSIS_N_MATRIX_GATE_20260612.md", report)
    metrics["residual_missing_n_studies"] = len(residual_study_rows)
    return metrics


def build_paper_b() -> dict[str, object]:
    shell = read_csv(PAPER_B_SHELL)
    template = read_csv(PAPER_B_TEMPLATE)
    manifest = read_csv(PAPER_B_MANIFEST)
    exception_rows = read_csv(PAPER_B_EXCEPTION_LAYER)

    denom_rows: list[dict[str, object]] = []
    denom_keys = sorted({r.get("denominator_family", "") for r in shell})
    for denom in denom_keys:
        group = [r for r in shell if r.get("denominator_family", "") == denom]
        by_score = Counter(r.get("scoring_eligibility", "") for r in group)
        by_evidence = Counter(r.get("evidence_family", "") for r in group)
        denom_rows.append(
            {
                "denominator_family": denom,
                "rows": len(group),
                "studies": len({r.get("study_id", "") for r in group}),
                "evidence_families": ";".join(f"{k}:{v}" for k, v in sorted(by_evidence.items())),
                "scoring_eligibility": ";".join(f"{k}:{v}" for k, v in sorted(by_score.items())),
                "preanalysis_action": "keep_separate_denominator_never_pool",
            }
        )

    actual_packets = {p.name for p in PAPER_B_PACKET_DIR.glob("*_source_packet_20260609.txt")} if PAPER_B_PACKET_DIR.exists() else set()
    packet_rows: list[dict[str, object]] = []
    for row in manifest:
        study_id = row.get("study_id", "")
        expected_packet = f"{study_id}_source_packet_20260609.txt"
        present = expected_packet in actual_packets
        packet_rows.append(
            {
                "study_id": study_id,
                "target_task_count": row.get("target_task_count", ""),
                "denominator_families": row.get("denominator_families", ""),
                "manifest_status": row.get("status", ""),
                "expected_packet": expected_packet,
                "packet_present_in_workspace": "yes" if present else "no",
                "preanalysis_action": "ready_for_require_source_packet_run" if present else "restore_or_regenerate_private_source_packet",
            }
        )

    exception_summary = Counter(r.get("exception_layer_policy", "") for r in exception_rows)
    generic_gate_summary = Counter(r.get("generic_full_accuracy_gate_status", "") for r in exception_rows)
    contract_gate_summary = Counter(r.get("contract_aware_beta_path_gate_status", "") for r in exception_rows)

    write_csv(
        OUT / "paper_b_denominator_summary_20260612.csv",
        denom_rows,
        [
            "denominator_family",
            "rows",
            "studies",
            "evidence_families",
            "scoring_eligibility",
            "preanalysis_action",
        ],
    )
    write_csv(
        OUT / "paper_b_source_packet_audit_20260612.csv",
        packet_rows,
        [
            "study_id",
            "target_task_count",
            "denominator_families",
            "manifest_status",
            "expected_packet",
            "packet_present_in_workspace",
            "preanalysis_action",
        ],
    )

    missing_packet_queue = sorted(
        [row for row in packet_rows if row["packet_present_in_workspace"] == "no"],
        key=lambda row: (-int(row["target_task_count"] or 0), str(row["study_id"])),
    )
    for index, row in enumerate(missing_packet_queue, start=1):
        row["restore_priority"] = index
        row["why_required"] = "full-corpus M1-R must use source-rendered packets with --require-source-packet; otherwise accuracy claims are source-detached"
        row["recommended_action"] = "restore_existing_private_packet_else_regenerate_from_local_pdf"

    write_csv(
        OUT / "paper_b_missing_source_packet_queue_20260612.csv",
        missing_packet_queue,
        [
            "restore_priority",
            "study_id",
            "target_task_count",
            "denominator_families",
            "manifest_status",
            "expected_packet",
            "packet_present_in_workspace",
            "preanalysis_action",
            "why_required",
            "recommended_action",
        ],
    )

    metrics = {
        "shell_rows": len(shell),
        "template_rows": len(template),
        "manifest_studies": len(manifest),
        "packets_present": sum(1 for row in packet_rows if row["packet_present_in_workspace"] == "yes"),
        "packets_missing": sum(1 for row in packet_rows if row["packet_present_in_workspace"] == "no"),
        "exception_rows": len(exception_rows),
    }
    source_packet_stop_condition = (
        "Full-corpus M1-R source packet availability gate is closed: all manifest "
        "studies have private rendered source packets in the workspace. Full-corpus "
        "M1-R accuracy and all-row substitution claims remain blocked until the larger "
        "M1-R run is scored with the exception-aware wrapper."
        if metrics["packets_missing"] == 0
        else
        "Full-corpus M1-R accuracy and all-row substitution claims remain blocked until "
        "the missing private source packets are restored or regenerated and the larger "
        "M1-R run is scored with the exception-aware wrapper."
    )

    report = f"""# Paper B Pre-Analysis Denominator/Source-Packet Gate

Date: {date.today().isoformat()}

## Locked Recommendations

- Use the post-freeze 213-study full-corpus Step 5 universe.
- Keep denominator families separate; do not report one pooled accuracy denominator.
- Prioritize restoring/regenerating full-corpus private source packets before submission-grade full-corpus M1-R claims.
- Keep Codex M1-R as the primary workflow condition.
- Retain Claude Sonnet and Gemini as supplementary triage/cross-model disagreement evidence, not as vendor ranking.
- Apply the S009/S010 exception layer in the same scoring pass that scores larger M1-R runs.
- Count abstention on scorable rows as incorrect while reporting abstention as workflow behavior.
- Split pointer-only, source-absence, not-derivable, duplicate-source, and status-only records out of generic numeric accuracy claims.

## Inputs

- `{PAPER_B_SHELL.relative_to(REPO)}`
- `{PAPER_B_TEMPLATE.relative_to(REPO)}`
- `{PAPER_B_MANIFEST.relative_to(REPO)}`
- `{PAPER_B_EXCEPTION_LAYER.relative_to(REPO)}`

## Current Gate Metrics

{md_table([
    {"metric": "Full-corpus task shell rows", "value": metrics["shell_rows"]},
    {"metric": "Locked-output template rows", "value": metrics["template_rows"]},
    {"metric": "Manifest study packets expected", "value": metrics["manifest_studies"]},
    {"metric": "Private packets present in workspace", "value": metrics["packets_present"]},
    {"metric": "Private packets missing in workspace", "value": metrics["packets_missing"]},
    {"metric": "Exception-layer rows", "value": metrics["exception_rows"]},
], ["metric", "value"])}

## Denominator Families

{md_table(denom_rows, ["denominator_family", "rows", "studies", "scoring_eligibility", "preanalysis_action"])}

## Exception-Layer Policy Counts

{md_table([{"policy": k, "rows": v} for k, v in sorted(exception_summary.items())], ["policy", "rows"])}

## Generic Full-Accuracy Gate Counts

{md_table([{"status": k, "rows": v} for k, v in sorted(generic_gate_summary.items())], ["status", "rows"])}

## Contract-Aware Gate Counts

{md_table([{"status": k, "rows": v} for k, v in sorted(contract_gate_summary.items())], ["status", "rows"])}

## Stop Condition

{source_packet_stop_condition}

## Outputs

- `paper_b_denominator_summary_20260612.csv`
- `paper_b_source_packet_audit_20260612.csv`
- `paper_b_missing_source_packet_queue_20260612.csv`
"""
    write_text(OUT / "PAPER_B_PREANALYSIS_DENOMINATOR_SOURCE_GATE_20260612.md", report)
    return metrics


def build_anx_tru_trace() -> dict[str, object]:
    paper_a_base = (
        Path("/Users/newhosung/Library/CloudStorage/OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity/")
        / "AI Adoption Meta Analysis - Documents/Meta/AI Adoption/Paper1_MASEM_Working_20260605"
    )
    search_files = [
        paper_a_base / "02_consensus_analysis_inputs/reference_consensus_v2/Paper2_Primary_SourceReported_Direct_R_Input_20260605_v2.csv",
        paper_a_base / "02_consensus_analysis_inputs/reference_consensus_v2/Paper2_Unified_Direct_R_Analysis_Input_20260605_v2.csv",
        paper_a_base / "02_consensus_analysis_inputs/reference_consensus_v2/Paper2_Converted_Beta_Path_SourceStatistic_Sensitivity_Input_20260605_v2.csv",
        paper_a_base / "07_analysis_ready/paper1_direct_r_primary_analysis_ready_20260605.csv",
        paper_a_base / "07_analysis_ready/paper1_direct_r_expanded_analysis_ready_20260605.csv",
        paper_a_base / "07_analysis_ready/paper1_direct_r_sensitivity_converted_analysis_ready_20260605.csv",
        paper_a_base / "07_analysis_ready/paper1_direct_r_all_sets_long_20260605.csv",
        paper_a_base / "09_model_ready_tiered_freeze/paper1_direct_r_primary_model_ready_tiered_freeze_20260605.csv",
        PAPER_B_SHELL,
        PAPER_B_TEMPLATE,
        REPO / "paper_b/public_data_repository_20260611/2_Raw_AI_Outputs/metadata/full_corpus_locked_output_template_20260609.csv",
    ]
    trace_rows: list[dict[str, object]] = []
    for path in search_files:
        if not path.exists():
            continue
        rows = read_csv(path)
        hit_rows = [row for row in rows if contains_anx_tru(row)]
        for row in hit_rows:
            trace_rows.append(
                {
                    "source_collection": "repo" if str(path).startswith(str(REPO)) else "onedrive",
                    "source_file": str(path),
                    "file_name": path.name,
                    "study_id": row.get("study_id", ""),
                    "analysis_record_id": row.get("analysis_record_id", ""),
                    "task_unit_id": row.get("task_unit_id", ""),
                    "reference_record_id": row.get("reference_record_id", ""),
                    "construct_pair": row_construct_pair(row) or ("ANX-TRU" if contains_anx_tru(row) else ""),
                    "r_numeric_or_reference": row.get("r_numeric") or row.get("reference_r_value") or "",
                    "source_type": row.get("r_source") or row.get("reference_r_source") or row.get("statistic_family") or "",
                    "evidence_type": row.get("evidence_type") or row.get("reference_evidence_type") or row.get("evidence_family") or "",
                    "denominator_family": row.get("denominator_family", ""),
                    "include_primary": row.get("include_primary", ""),
                    "include_expanded": row.get("include_expanded", ""),
                    "include_sensitivity": row.get("include_sensitivity", ""),
                    "source_location": row.get("source_location", ""),
                    "notes": row.get("notes", ""),
                    "interpretation": "",
                }
            )

    for row in trace_rows:
        if row["file_name"] == "paper1_direct_r_primary_model_ready_tiered_freeze_20260605.csv":
            row["interpretation"] = "present_in_legacy_primary_freeze"
        elif row["file_name"] in {
            "Paper2_Primary_SourceReported_Direct_R_Input_20260605_v2.csv",
            "paper1_direct_r_primary_analysis_ready_20260605.csv",
        }:
            row["interpretation"] = "legacy_primary_direct_r_source"
        elif row["source_type"] == "coder_agreed_direct_correlation":
            row["interpretation"] = "post_freeze_full_corpus_direct_r_candidate_not_in_20260605_paper_a_primary"
        elif row["denominator_family"] == "primary_latent_or_construct_correlation_with_source_type_flag":
            row["interpretation"] = "post_freeze_full_corpus_latent_correlation_candidate_main_text_separate_panel"
        elif row["denominator_family"] == "secondary_beta_or_path_converted_effect_size":
            row["interpretation"] = "post_freeze_full_corpus_converted_effect_candidate_compare_alongside_primary_not_pooled"
        elif row["source_type"] == "secondary_source_statistic_converted_by_human_consensus":
            row["interpretation"] = "legacy_expanded_or_sensitivity_only_source_statistic_review_candidate"
        else:
            row["interpretation"] = "trace_candidate_review_required"

    write_csv(
        OUT / "paper_a_anx_tru_source_trace_20260612.csv",
        trace_rows,
        [
            "source_collection",
            "source_file",
            "file_name",
            "study_id",
            "analysis_record_id",
            "task_unit_id",
            "reference_record_id",
            "construct_pair",
            "r_numeric_or_reference",
            "source_type",
            "evidence_type",
            "denominator_family",
            "include_primary",
            "include_expanded",
            "include_sensitivity",
            "source_location",
            "notes",
            "interpretation",
        ],
    )

    unique_candidates: dict[tuple[object, ...], dict[str, object]] = {}
    for row in trace_rows:
        if row["interpretation"] == "trace_candidate_review_required":
            continue
        if not str(row["r_numeric_or_reference"]).strip():
            continue
        key = (
            row["study_id"],
            row["construct_pair"],
            row["r_numeric_or_reference"],
            row["source_type"],
            row["evidence_type"],
            row["denominator_family"],
            row["interpretation"],
        )
        if key not in unique_candidates:
            unique_candidates[key] = {
                "study_id": row["study_id"],
                "construct_pair": row["construct_pair"],
                "r_numeric_or_reference": row["r_numeric_or_reference"],
                "source_type": row["source_type"],
                "evidence_type": row["evidence_type"],
                "denominator_family": row["denominator_family"],
                "interpretation": row["interpretation"],
                "source_files": set(),
            }
        unique_candidates[key]["source_files"].add(row["file_name"])

    unique_candidate_rows: list[dict[str, object]] = []
    for row in unique_candidates.values():
        unique_candidate_rows.append({**row, "source_files": ";".join(sorted(row["source_files"]))})
    unique_candidate_rows.sort(key=lambda row: (str(row["study_id"]), str(row["interpretation"])))

    write_csv(
        OUT / "paper_a_anx_tru_unique_candidate_trace_20260612.csv",
        unique_candidate_rows,
        [
            "study_id",
            "construct_pair",
            "r_numeric_or_reference",
            "source_type",
            "evidence_type",
            "denominator_family",
            "interpretation",
            "source_files",
        ],
    )

    by_interpretation = Counter(str(row["interpretation"]) for row in unique_candidate_rows)
    by_study = Counter(str(row["study_id"]) for row in unique_candidate_rows if row["study_id"])
    report = f"""# Paper A ANX-TRU Source Trace

Date: {date.today().isoformat()}

## Why ANX-TRU Was Flagged

The pre-analysis N/matrix gate showed `ANX-TRU` as 0 rows in the 2026-06-05
Paper A primary direct-r model-ready freeze. The researcher noted that this
seemed inconsistent with prior memory of available rows, so the pair was traced
across the legacy Paper A package, the post-freeze full-corpus Step 5 shell, the
public metadata package, and the mounted External SSD repo copies.

## Current Finding

The 0-row result is not evidence that the literature has no `ANX-TRU` data. It
means the 2026-06-05 Paper A primary direct-r freeze contains no eligible
`ANX-TRU` row. After deduplicating shell/template/public-metadata traces, the
broader 2026-06-09 full-corpus reference and legacy expanded/sensitivity files
contain unique `ANX-TRU` candidate evidence in separate source-type strata:

{md_table([{"interpretation": k, "rows": v} for k, v in sorted(by_interpretation.items())], ["interpretation", "rows"])}

## Studies Found

{md_table([{"study_id": k, "rows": v} for k, v in sorted(by_study.items())], ["study_id", "rows"])}

## Method Decision

For Paper A primary direct-r TSSEM/OSMASEM, `ANX-TRU` remains not estimable from
the 2026-06-05 primary direct-r freeze. For the revised manuscript spine, this
pair should not simply be labeled absent. It should be handled as a source-type
and corpus-version boundary:

- `S036` is a post-freeze full-corpus direct-r candidate.
- `S102` is a post-freeze latent/Fornell-Larcker off-diagonal candidate.
- `S066` is a post-freeze beta/path-converted candidate.
- `S142` appears only in the legacy expanded/sensitivity source-statistic path.

The next analysis step is therefore to decide whether Paper A should be rebuilt
from the 2026-06-09 full-corpus reference for final claims, rather than relying
on the 2026-06-05 legacy primary freeze alone.

## SSD Check

The mounted External SSD contains repo copies, but the checked
`jornal_AI-adoption_meta` copy is shallower than the current workspace and did
not add ANX-TRU rows. The `dissertation_AI-adoption_meta` CSVs also did not
contain additional ANX-TRU rows. Current best evidence is therefore the
post-freeze full-corpus reference in this workspace.

## Output

- `paper_a_anx_tru_source_trace_20260612.csv`
- `paper_a_anx_tru_unique_candidate_trace_20260612.csv`
"""
    write_text(OUT / "PAPER_A_ANX_TRU_SOURCE_TRACE_20260612.md", report)
    return {
        "anx_tru_trace_rows": len(trace_rows),
        "anx_tru_unique_candidates": len(unique_candidate_rows),
        "anx_tru_trace_studies": len(by_study),
    }


def build_contract(paper_a: dict[str, object], paper_b: dict[str, object], anx_tru: dict[str, object]) -> None:
    paper_a_n_status = (
        "pdf_n_override_applied_derived_input_full10_not_identified"
        if paper_a["rows_still_missing_after_pdf_source_check"] == 0
        else "n_eligible_subset_ready_full_all_row_still_blocked"
    )
    paper_b_packet_status = (
        "source_packet_gate_closed_full_run_ready"
        if paper_b["packets_missing"] == 0
        else "blocked_until_packet_restoration"
    )
    paper_b_denominator_status = (
        "dedicated_manifest_and_9_shard_plan_ready"
        if paper_b["packets_missing"] == 0
        else "waiting_for_source_packet_gate"
    )
    text = f"""# Pre-Analysis Processing Contract

Date: {date.today().isoformat()}

## Purpose

This contract locks the pre-analysis processing decisions that must be completed before claim-carrying table and figure spine redesign. It converts the researcher's accepted recommendations into executable gates.

## Paper A Decisions

1. Primary N rule: use pairwise source-supported N when available; otherwise use source-supported analytic sample N.
2. Rows without recoverable N: report the row-level source-check reason to the researcher before final primary exclusion; if still unresolved, exclude from primary N-weighted TSSEM/OSMASEM and retain in sensitivity/readiness ledgers only.
3. Construct scope: keep the 10 constructs as the theory target.
4. Model strategy: run matrix sparsity/identification audit before deciding whether final analysis can support the full 10-construct model or needs a staged core-plus-extension structure.
5. Converted beta/path/source-statistic rows: keep in the main results space as a source-type comparison panel beside primary direct-r evidence, but do not silently pool them into the direct-r primary estimate.
6. ANX-TRU: do not treat the current 0-row primary result as simple absence until corpus-version and source-type rescue checks are reported. Current trace shows post-freeze full-corpus candidates that are outside the 2026-06-05 primary direct-r freeze.

## Paper B Decisions

1. Corpus: use the post-freeze 213-study full-corpus Step 5 universe.
2. Denominators: keep direct-r, latent/source-flagged, beta/path-converted, source-absence/not-derivable, duplicate-source, and status-only strata separate.
3. Source packets: restore/regenerate full private source-packet coverage before full-corpus M1-R accuracy claims.
4. Main-text model comparison: Codex M1-R remains the primary workflow condition, while Claude Sonnet and Gemini must appear in the main text as cross-model robustness/triage evidence. The framing is workflow validation, not vendor ranking.
5. Exception layer: S009/S010 exception logic must be consumed in the scoring pass.
6. Abstention: count abstention on scorable rows as incorrect and report separately as workflow behavior.
7. Converted-effect comparison: beta/path-converted rows belong in the main results space alongside primary numeric extraction as a separate comparison panel. They must not be silently pooled with direct-r rows, but the comparison itself is a substantive finding because it shows how source-type recovery choices can affect downstream meta-analytic evidence.
8. Downstream substitution: run core-6 diagnostic first; full-10/all-row substitution claims require matrix/N/coverage sufficiency.
9. Claim boundary: Paper B is a source-anchored workflow validation and downstream substitution-risk study, not an LLM replacement paper.

## Current Gate Snapshot

{md_table([
    {"gate": "Paper A N/matrix", "current_state": f'{paper_a["rows_with_reconciled_numeric_n"] + paper_a["rows_with_pdf_recovered_n_candidate"]} rows carry source-supported N after PDF override; {paper_a["complete_10_construct_studies"]} complete 10-construct studies', "status": paper_a_n_status},
    {"gate": "Paper A ANX-TRU", "current_state": f'{anx_tru["anx_tru_unique_candidates"]} post-freeze full-corpus candidates across {anx_tru["anx_tru_trace_studies"]} studies; source-type comparison required', "status": "source_type_panel_ready_do_not_pool_with_legacy_primary"},
    {"gate": "Paper B source packets", "current_state": f'{paper_b["packets_present"]}/{paper_b["manifest_studies"]} private packets present', "status": paper_b_packet_status},
    {"gate": "Paper B denominator shell", "current_state": f'{paper_b["shell_rows"]} full-corpus task rows', "status": paper_b_denominator_status},
    {"gate": "Paper B exception layer", "current_state": f'{paper_b["exception_rows"]} exception-layer rows', "status": "must_be_consumed_by_larger_scoring_pass"},
], ["gate", "current_state", "status"])}

## Non-Claims Until Gates Close

- Do not claim Paper A final path estimates, indirect effects, or fit.
- Do not claim Paper B full-corpus M1-R accuracy.
- Do not claim all-row or full-10 downstream substitution stability.
- Do not pool Paper B heterogeneous task units into one accuracy denominator.

## Next Execution Order

1. Execute the dedicated Paper B full-corpus M1-R shards only with source packets required and source quotes suppressed.
2. Apply exception-aware scoring to the dedicated full-corpus M1-R manifest.
3. Produce Paper B denominator-family and source-type comparison tables; do not use one pooled denominator.
4. Use Paper A core-6/core-7/core-8 as the immediate SEM diagnostic lane unless a source-type-approved full model rebuild is specified.
5. Produce claim-carrying table/figure specifications from closed gates only.
"""
    write_text(OUT / "PRE_ANALYSIS_PROCESSING_CONTRACT_20260612.md", text)


def build_researcher_decisions() -> None:
    text = f"""# Researcher-Approved Pre-Analysis Decisions

Date: {date.today().isoformat()}

## Decisions Recorded

1. Missing sample-size rows: approved default rule is to use source-supported
   PDF-recovered analytic/sample N when recoverable; exclude only rows that
   remain unresolved after source checking. The 63 residual rows now have
   derived PDF-supported N, so the current 804-row rerun input is N-complete.
2. Paper A model boundary: approved and essential. Keep the 10-construct theory
   target, but final claims must follow the matrix/identification evidence.
3. ANX-TRU: approved to mark not estimable only if source tracing confirms no
   defensible primary input. Because the researcher expected more rows, the
   pair must be traced across current repo, OneDrive, and mounted SSD data before
   final model reduction.
4. Paper B source packets: approved as mandatory. Full-corpus M1-R claims require
   source packets restored or regenerated. The current source-packet gate is
   closed at 194/194 studies for the 2,043-row full-corpus shell.
5. Claude/Gemini: include in the main text. They should be framed as cross-model
   robustness, disagreement, and triage evidence within the workflow-validation
   study, not as vendor ranking.
6. Denominator families: approved. Keep separate denominator-family reporting.
7. Beta/path-converted effects: include in the same main-results space as primary
   extraction for explicit comparison, because the comparison can be a substantive
   methodological contribution for other meta-analyses. Do not silently pool
   converted effects with direct-r rows.
8. Claim boundary: approved. Paper B is about source-anchored workflow validation
   and downstream substitution risk, not LLM replacement.

## Implementation Consequence

The claim-carrying table/figure spine must be built around panels and gates:

- Paper A: N eligibility, matrix coverage, ANX-TRU source-type/corpus boundary,
  final estimability decision.
- Paper B: direct-r, latent/source-flagged, beta/path-converted, abstention,
  source-risk, and cross-model robustness panels.
- Downstream: core-6 diagnostic first; all-row/full-10 only after source and
  matrix sufficiency are proven.

## Current Execution State

- PDF-supported N override has been applied only as a derived input; raw
  workbooks and frozen reference files were not overwritten.
- The current matrix audit supports core-6/core-7/core-8 diagnostic lanes, but
  not a complete-case full 10-construct TSSEM/OSMASEM model.
- ANX-TRU is recoverable only as a post-freeze source-type comparison panel in
  the current evidence, not as a legacy primary direct-r matrix rescue.
- The dedicated full-corpus M1-R manifest and nine-shard run script are ready;
  full-corpus accuracy remains unclaimed until those shards are locked and
  exception-aware scored.
- Claude Sonnet and Gemini belong in the main text as cross-model robustness and
  triage evidence from the clean model-explicit package; the Codex source-
  packet-required M1-R branch remains the primary claim-bearing workflow gate
  until equivalent source-packet full-corpus runs are deliberately added.
"""
    write_text(OUT / "RESEARCHER_APPROVED_PREANALYSIS_DECISIONS_20260612.md", text)


def build_goal_plan() -> None:
    text = f"""# Detailed Goal Plan: Pre-Analysis Processing Before Manuscript Spine Redesign

Date: {date.today().isoformat()}

## G001: Lock Pre-Analysis Contract

Status: completed for current decisions; keep open only for later scope changes.

Deliverables:

- `PRE_ANALYSIS_PROCESSING_CONTRACT_20260612.md`
- Paper A N/matrix gate
- Paper B denominator/source-packet gate

Completion evidence:

- Contract lists accepted decisions and non-claims.
- Gate reports are generated from current authoritative files.

## G002: Paper A Source-Supported N Reconciliation

Status: completed for the derived 804-row rerun input.

Deliverables:

- Adopt and verify the existing deterministic N reconciliation table.
- Residual 7-study missing-N source/PDF check queue with row-level reasons.
- Researcher-facing confirmation packet before final primary exclusion of unresolved N rows.
- Rebuilt primary model input or subset input with `primary_n_status`.

Completion evidence:

- Rows entering the derived 804-row TSSEM/OSMASEM input have numeric N and provenance.
- The residual 63 rows were not silently excluded; PDF source checking supplied defensible study-level N in a derived override file.
- Raw workbooks and frozen reference files remain untouched.

## G002B: Paper A ANX-TRU Rescue/Boundary Audit

Status: completed as a source-type boundary panel; not completed as a legacy-primary full-model rescue.

Deliverables:

- ANX-TRU source trace across the 2026-06-05 Paper A package, the 2026-06-09 full-corpus reference, OneDrive, and mounted SSD copies.
- Decision whether ANX-TRU is not estimable in final Paper A, or recoverable through a post-freeze full-corpus rebuild/source-type panel.

Completion evidence:

- `ANX-TRU` is no longer treated as a generic 0-row absence without source/corpus explanation.
- Recovered post-freeze rows are assigned to direct-r-like, latent/source-flagged, or converted-effect strata before modeling.
- Direct-r, latent, and converted-effect candidates are compared as a main results source-type panel and are not silently pooled into the legacy primary estimate.

## G003: Paper A Matrix/Identification Audit

Status: completed for the current N-complete derived input.

Deliverables:

- Construct-pair coverage heatmap data.
- Study-level matrix completeness data.
- Core-plus-extension recommendation if full 10-construct model is not estimable.

Completion evidence:

- Full 10-construct complete-case TSSEM/OSMASEM is not identified from the current legacy primary direct-r matrix because `ANX-TRU` is absent.
- Core-6, core-7, and core-8 remain the immediate bounded diagnostic lanes.

## G004: Paper B Full-Corpus Source-Packet Restoration

Status: completed for the 194-study / 2,043-row full-corpus shell.

Deliverables:

- 194-study source-packet coverage check.
- Missing-packet exception list if any packet cannot be restored.

Completion evidence:

- M1-R can run with `--require-source-packet`; the current missing-packet count is 0.
- A dedicated empty full-run manifest and nine-shard command script have been generated.

## G005: Paper B Exception-Aware M1-R Scoring

Status: ready for execution; not yet claim-complete.

Deliverables:

- Larger/full M1-R locked output shards.
- Exception-aware scoring outputs by denominator family.
- Abstention/source-risk/not-derivable reporting strata.
- Main-text cross-model comparison for Codex, Claude Sonnet, and Gemini, framed as robustness/triage rather than vendor ranking.
- Main-results comparison panel for beta/path-converted effects beside direct-r/latent rows, without pooled-denominator claims.

Completion evidence:

- RQ1-RQ3 can be reported without pooled heterogeneous denominators only after the dedicated full-run manifest is locked and exception-aware scored.
- The next executable gate is the nine-shard full-corpus M1-R run, followed by `score_full_corpus_m1_r_with_exception_layer.py`.

## G006: Downstream Substitution Diagnostic Gate

Status: partially completed for core-6; full-10/all-row claims blocked.

Deliverables:

- Core-6 diagnostic update.
- Full-10/all-row eligibility decision.
- Delta tables for pooled r, paths, indirect effects, fit, and claim consequences where estimable.

Completion evidence:

- RQ4 is populated only within verified eligibility boundaries.

## G007: Claim-Carrying Table/Figure Spine Redesign

Status: not started; must consume only closed or explicitly bounded gates.

Deliverables:

- Paper A table/figure specification.
- Paper B table/figure specification.
- Source-data and script path for every table/figure.

Completion evidence:

- Every main table/figure has a named RQ, input data, script/output, and claim boundary.

## G008: Full Manuscript Rebuild

Status: not started for the revised claim-carrying version.

Deliverables:

- Paper A target-journal draft with real result tables/figures or explicit diagnostic boundary.
- Paper B target-journal draft with denominator-family results and source-governed limitations.
- Team writing briefs for Literature Review and Discussion only.

Completion evidence:

- No result placeholder is presented as a manuscript claim.
"""
    write_text(OUT / "DETAILED_GOAL_PLAN_PREANALYSIS_20260612.md", text)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    paper_a = build_paper_a()
    paper_b = build_paper_b()
    anx_tru = build_anx_tru_trace()
    build_contract(paper_a, paper_b, anx_tru)
    build_researcher_decisions()
    build_goal_plan()
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
