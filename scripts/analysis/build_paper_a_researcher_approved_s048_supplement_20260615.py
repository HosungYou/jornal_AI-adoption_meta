#!/usr/bin/env python3
"""Stage researcher-approved S048 Table 2 values for Paper A analysis.

This script does not mutate the Paper B reference standard. It creates a
Paper A supplemental analysis input in which the seven S048 source-visible
Pearson correlations approved by the researcher on 2026-06-15 are explicitly
marked as researcher-approved. The latest upstream input already contains the
seven S048 values from the source-correction layer, so the normal path is an
in-place provenance/status promotion rather than duplicate row insertion.
"""

from __future__ import annotations

import csv
import json
import shutil
from copy import deepcopy
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
RESULTS = REPO / "data/04_extraction/05_llm_masem_substitution/results"
INPUT = RESULTS / "paper_a_researcher_approved_pe_se_s121_supplement_20260614/paper_a_source_corrected_plus_researcher_approved_anx_tru_pe_se_input_20260614.csv"
SHORTLIST = RESULTS / "paper_a_ai_candidate_source_trace_20260614/paper_a_C_remaining_full10_batch_review_shortlist_20260615.csv"
TEMPLATE = RESULTS / "paper_a_ai_candidate_source_trace_20260614/paper_a_human_confirmation_template_from_ai_trace_20260614.csv"
OUT_DIR = RESULTS / "paper_a_researcher_approved_s048_supplement_20260615"
OUT_INPUT = OUT_DIR / "paper_a_source_corrected_plus_researcher_approved_anx_tru_pe_se_s048_input_20260615.csv"
OUT_APPROVED_ROWS = OUT_DIR / "paper_a_researcher_approved_s048_rows_20260615.csv"
OUT_DECISIONS = OUT_DIR / "paper_a_researcher_approved_s048_promotion_decisions_20260615.csv"
OUT_FILLED_TEMPLATE = OUT_DIR / "paper_a_human_confirmation_template_s048_approved_20260615.csv"
OUT_REPORT = OUT_DIR / "PAPER_A_RESEARCHER_APPROVED_S048_SUPPLEMENT_20260615.md"
OUT_MANIFEST = OUT_DIR / "manifest.json"
ONEDRIVE_OUT = Path("/Users/newhosung/Library/CloudStorage/OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity/AI Adoption Meta Analysis - Documents/Meta/AI Adoption/03_source_adjudication/Paper_A/2026-06-15_researcher_approved_s048_supplement")

APPROVAL_DATE = "2026-06-15"
ANALYSIS_SET = "paper_a_source_corrected_plus_researcher_approved_anx_tru_pe_se_s048_20260615"
PAIR_ORDER = ["BI-FC", "BI-PE", "BI-SI", "EE-UB", "FC-UB", "SI-UB", "TRU-UB"]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, str]], fieldnames: list[str] | None = None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if fieldnames is None:
        fieldnames = list(rows[0].keys()) if rows else []
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def canonical_pair(a: str, b: str) -> str:
    return "-".join(sorted([a, b]))


def split_pair(pair: str) -> tuple[str, str]:
    a, b = pair.split("-", 1)
    return a, b


def as_float(value: str) -> float:
    return float(str(value).strip())


def fmt(value: float) -> str:
    return f"{value:.3f}".rstrip("0").rstrip(".")


def promotion_fields(row: dict[str, str], decision: dict[str, str], index: int, inserted: bool) -> dict[str, str]:
    pair = decision["missing_pair"]
    c1, c2 = split_pair(pair)
    value = fmt(as_float(decision["candidate_value"]))
    row = deepcopy(row)
    row.update({
        "analysis_set": ANALYSIS_SET,
        "analysis_role": "researcher-approved supplemental Paper A S048 Table 2 source row",
        "source_decision_id": f"PAPER-A-S048-APPROVED-20260615-{index:03d}",
        "source_pair": "researcher_approved_s048_batch",
        "study_id": "S048",
        "construct_1": c1,
        "construct_2": c2,
        "construct_pair": pair,
        "construct_pair_canonical": canonical_pair(c1, c2),
        "construct_pair_direction": "as_reported_from_S048_Table_2; correlation analyses use canonical key",
        "r_value": value,
        "r_numeric": value,
        "r_abs": fmt(abs(as_float(decision["candidate_value"]))),
        "r_source": "direct/table",
        "statistic_family": "source_reported_direct_r",
        "evidence_type": "source-reported Pearson correlation matrix",
        "is_source_reported_or_direct": "1",
        "is_model_derived_or_converted": "0",
        "include_primary": "1",
        "include_expanded": "1",
        "include_sensitivity": "0",
        "sample_size": row.get("sample_size") or "355",
        "sample_size_numeric": row.get("sample_size_numeric") or "355",
        "confidence": "high",
        "consensus_basis": "researcher_approved_s048_source_visible_values_20260615",
        "conversion_rule": "explicit_source_reported_zero_order_r_no_conversion",
        "override_rule": "researcher_approved_20260615_s048_supplement",
        "source_location": "S048.pdf Table 2 descriptive statistics and correlations",
        "source_artifact": "S048_source_packet_20260609.txt; S048.pdf",
        "source_locator": decision["source_locator"],
        "notes": "Researcher approved this source-visible S048 Table 2 Pearson r on 2026-06-15 after batch triage; Paper B reference standard is not mutated.",
        "freeze_tier": "paper_a_supplement_researcher_approved_source_checked",
        "include_primary_model_ready": "1",
        "freeze_decision": "researcher_approved_supplemental_paper_a_promotion",
        "substitution_scenario": ANALYSIS_SET,
        "substitution_action": "add_researcher_approved_s048_source_visible_value" if inserted else "promote_existing_s048_source_correction_to_researcher_approved",
        "substitution_source_task_unit_id": "C_remaining_full10_batch_shortlist_20260615",
        "substitution_review_priority": decision["full10_pair_order_label"],
        "substitution_model_id": "researcher_approval_not_ai_model_output",
        "substitution_original_r_numeric": row.get("substitution_original_r_numeric") or "",
        "substitution_r_numeric": value,
        "substitution_delta": row.get("substitution_delta") or "",
        "sample_size_reconciliation_status": row.get("sample_size_reconciliation_status") or "confirmed_for_supplemental_input",
        "sample_size_reconciliation_source": row.get("sample_size_reconciliation_source") or "S048 source packet / existing source-corrected input",
        "sample_size_reconciliation_rule": row.get("sample_size_reconciliation_rule") or "retain source-visible N used in existing S048 source-corrected input",
        "sample_size_reconciliation_note": row.get("sample_size_reconciliation_note") or "N=355 retained for S048 supplemental correlations",
        "masem_n_weighted_eligibility": row.get("masem_n_weighted_eligibility") or "eligible_source_reported_r_with_n",
    })
    if not row.get("analysis_record_id"):
        row["analysis_record_id"] = f"P1-SUPP-S048-20260615-{index:03d}"
    if not row.get("input_id"):
        row["input_id"] = f"S048-SUPP-{pair}-20260615"
    return row


def make_insert_row(fieldnames: list[str], template_row: dict[str, str] | None, decision: dict[str, str], index: int) -> dict[str, str]:
    row = {field: "" for field in fieldnames}
    if template_row:
        for field in fieldnames:
            row[field] = template_row.get(field, "")
    row["analysis_record_id"] = f"P1-SUPP-S048-20260615-{index:03d}"
    row["input_id"] = f"S048-SUPP-{decision['missing_pair']}-20260615"
    return promotion_fields(row, decision, index, inserted=True)


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    rows = read_csv(INPUT)
    shortlist = [r for r in read_csv(SHORTLIST) if r.get("study_id") == "S048" and r.get("missing_pair") in PAIR_ORDER]
    shortlist.sort(key=lambda r: PAIR_ORDER.index(r["missing_pair"]))
    if len(shortlist) != 7:
        raise SystemExit(f"Expected 7 S048 shortlist rows, found {len(shortlist)}")

    fieldnames = list(rows[0].keys())
    existing_s048 = next((r for r in rows if r.get("study_id") == "S048"), None)
    by_key: dict[tuple[str, str], int] = {}
    for i, row in enumerate(rows):
        if row.get("study_id") != "S048":
            continue
        key = (row.get("study_id", ""), canonical_pair(row.get("construct_1", ""), row.get("construct_2", "")))
        by_key[key] = i

    approved_rows: list[dict[str, str]] = []
    decision_rows: list[dict[str, str]] = []
    inserted_count = 0
    updated_count = 0
    for idx, decision in enumerate(shortlist, start=1):
        pair = decision["missing_pair"]
        key = ("S048", canonical_pair(*split_pair(pair)))
        if key in by_key:
            target_index = by_key[key]
            rows[target_index] = promotion_fields(rows[target_index], decision, idx, inserted=False)
            approved = rows[target_index]
            updated_count += 1
            row_status = "existing_row_promoted_to_researcher_approved"
        else:
            approved = make_insert_row(fieldnames, existing_s048, decision, idx)
            rows.append(approved)
            inserted_count += 1
            row_status = "new_researcher_approved_supplemental_row_inserted"
        approved_rows.append(approved)
        d = dict(decision)
        d.update({
            "human_decision": "approve",
            "human_decision_date": APPROVAL_DATE,
            "human_reviewer": "researcher",
            "final_value_if_confirmed": fmt(as_float(decision["candidate_value"])),
            "evidence_type_confirmed": "source-reported Pearson correlation matrix",
            "source_location_confirmed": decision["source_locator"],
            "promote_to_supplemental_input": "yes",
            "promotion_status": row_status,
            "paper_b_boundary": "paper_a_supplement_only_paper_b_reference_standard_not_mutated",
        })
        decision_rows.append(d)

    write_csv(OUT_INPUT, rows, fieldnames)
    write_csv(OUT_APPROVED_ROWS, approved_rows, fieldnames)
    write_csv(OUT_DECISIONS, decision_rows)

    template_rows = read_csv(TEMPLATE)
    template_fields = list(template_rows[0].keys()) if template_rows else [
        "human_decision", "human_decision_date", "human_reviewer", "study_id", "pair",
        "candidate_value_or_human_value", "final_value_if_confirmed", "evidence_type",
        "source_location_confirmed", "decision_rationale", "promote_to_supplemental_input",
    ]
    filled = []
    for d in decision_rows:
        filled.append({
            "human_decision": "approve",
            "human_decision_date": APPROVAL_DATE,
            "human_reviewer": "researcher",
            "study_id": "S048",
            "pair": d["missing_pair"],
            "candidate_value_or_human_value": d["candidate_value"],
            "final_value_if_confirmed": d["final_value_if_confirmed"],
            "evidence_type": d["evidence_type_confirmed"],
            "source_location_confirmed": d["source_location_confirmed"],
            "decision_rationale": "Both constructs are human/reference-supported and S048 Table 2 reports a source-visible Pearson r cell; approved by researcher for Paper A supplemental analysis only.",
            "promote_to_supplemental_input": "yes",
        })
    write_csv(OUT_FILLED_TEMPLATE, filled, template_fields)

    workbook_path = None
    try:
        import pandas as pd
        import xlsxwriter  # type: ignore  # noqa: F401
        workbook_path = OUT_DIR / "PAPER_A_S048_RESEARCHER_APPROVAL_WORKBOOK_20260615.xlsx"
        with pd.ExcelWriter(workbook_path, engine="xlsxwriter") as writer:
            pd.DataFrame(decision_rows).to_excel(writer, sheet_name="S048_approved", index=False)
            pd.DataFrame(approved_rows).to_excel(writer, sheet_name="analysis_rows", index=False)
            pd.DataFrame(filled).to_excel(writer, sheet_name="confirmation", index=False)
    except Exception:
        workbook_path = None

    pair_lines = [f"- `{r['missing_pair']}` = `{r['candidate_value']}` ({r['source_locator']})" for r in shortlist]
    report = [
        "# Paper A researcher-approved S048 supplemental staging",
        "",
        "Date: 2026-06-15",
        "",
        "## Decision recorded",
        "",
        "The researcher approved the seven S048 source-visible Pearson correlation cells from Table 2 for Paper A supplemental analysis. This does not mutate the Paper B source-anchored adjudicated human reference standard.",
        "",
        "## Approved S048 values",
        "",
        *pair_lines,
        "",
        "## Staging result",
        "",
        f"- Upstream input rows: `{len(read_csv(INPUT))}`",
        f"- Output input rows: `{len(rows)}`",
        f"- Existing S048 rows promoted: `{updated_count}`",
        f"- New supplemental rows inserted: `{inserted_count}`",
        f"- Analysis input: `{OUT_INPUT.relative_to(REPO)}`",
        f"- Approved rows: `{OUT_APPROVED_ROWS.relative_to(REPO)}`",
        f"- Decision table: `{OUT_DECISIONS.relative_to(REPO)}`",
        f"- Filled confirmation template: `{OUT_FILLED_TEMPLATE.relative_to(REPO)}`",
        "",
        "## Boundary",
        "",
        "These rows are eligible for Paper A model-family MASEM reruns as researcher-approved supplemental input. Rejected or held mappings remain excluded: S004 PKC->SE, S121 threat appraisal->ANX, and S072 construct-mapping audit rows.",
    ]
    if workbook_path:
        report.extend([f"- Workbook: `{workbook_path.relative_to(REPO)}`"])
    OUT_REPORT.write_text("\n".join(report) + "\n", encoding="utf-8")

    manifest = {
        "date": APPROVAL_DATE,
        "input": str(INPUT.relative_to(REPO)),
        "output_input": str(OUT_INPUT.relative_to(REPO)),
        "approved_pairs": PAIR_ORDER,
        "updated_existing_rows": updated_count,
        "inserted_rows": inserted_count,
        "row_count": len(rows),
        "paper_b_reference_mutated": False,
    }
    OUT_MANIFEST.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    ONEDRIVE_OUT.mkdir(parents=True, exist_ok=True)
    for path in [OUT_INPUT, OUT_APPROVED_ROWS, OUT_DECISIONS, OUT_FILLED_TEMPLATE, OUT_REPORT, OUT_MANIFEST]:
        shutil.copy2(path, ONEDRIVE_OUT / path.name)
    if workbook_path:
        shutil.copy2(workbook_path, ONEDRIVE_OUT / workbook_path.name)

    print(json.dumps(manifest, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
