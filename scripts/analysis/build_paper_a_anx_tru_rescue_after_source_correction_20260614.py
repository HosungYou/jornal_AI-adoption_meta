#!/usr/bin/env python3
"""Build Paper A ANX-TRU rescue/boundary artifacts after S004/S048 correction.

This script is intentionally diagnostic. It does not mutate frozen reference
files or raw coder workbooks. It creates a researcher-review packet and a
source-corrected-plus-ANX-TRU diagnostic input so that the full 10-construct
coverage consequence can be inspected without promoting rows into the final
Paper A input.
"""

from __future__ import annotations

import csv
import itertools
import shutil
from pathlib import Path


REPO = Path(__file__).resolve().parents[2]
PRIVATE_ROOT = "<PRIVATE_AI_ADOPTION_DOCUMENTS_ROOT>"
ONEDRIVE = Path(
    "/Users/newhosung/Library/CloudStorage/OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity/"
    "AI Adoption Meta Analysis - Documents"
)

BASE_INPUT = REPO / (
    "data/04_extraction/05_llm_masem_substitution/results/"
    "paper_a_source_corrected_s004_s048_20260614/"
    "paper_a_source_corrected_s004_s048_input_20260614.csv"
)
FROZEN_REFERENCE = REPO / (
    "data/04_extraction/04_reference_standard_freeze/"
    "full_corpus_reference_standard_frozen_20260609.csv"
)

OUT_DIR = REPO / (
    "data/04_extraction/05_llm_masem_substitution/results/"
    "paper_a_anx_tru_rescue_after_source_correction_20260614"
)
ONEDRIVE_DIR = ONEDRIVE / (
    "Meta/AI Adoption/03_source_adjudication/Paper_A/"
    "2026-06-14_anx_tru_rescue_after_source_correction"
)

TARGET_CONSTRUCTS = ["PE", "EE", "SI", "FC", "TRU", "ANX", "SE", "ATT", "BI", "UB"]
TARGET_SET = set(TARGET_CONSTRUCTS)
REQUIRED_PAIRS = {
    "-".join(sorted(pair)) for pair in itertools.combinations(TARGET_CONSTRUCTS, 2)
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def canonical_pair(a: str, b: str) -> str:
    return "-".join(sorted([a, b]))


def row_pair(row: dict[str, str]) -> str:
    pair = row.get("construct_pair_canonical") or row.get("construct_pair") or ""
    if pair:
        return pair
    return canonical_pair(row.get("construct_1", ""), row.get("construct_2", ""))


def primary_ready(row: dict[str, str]) -> bool:
    marker = row.get("include_primary_model_ready") or row.get("include_primary") or ""
    return marker in {"1", "TRUE", "True", "true", "yes", "Y"}


def coverage(rows: list[dict[str, str]]) -> dict[str, object]:
    observed_pairs: set[str] = set()
    by_study: dict[str, set[str]] = {}
    for row in rows:
        if not primary_ready(row):
            continue
        c1 = row.get("construct_1", "")
        c2 = row.get("construct_2", "")
        if c1 not in TARGET_SET or c2 not in TARGET_SET or c1 == c2:
            continue
        pair = row_pair(row)
        if pair not in REQUIRED_PAIRS:
            continue
        observed_pairs.add(pair)
        by_study.setdefault(row.get("study_id", ""), set()).add(pair)

    complete = sorted(sid for sid, pairs in by_study.items() if REQUIRED_PAIRS <= pairs)
    top = []
    for sid, pairs in sorted(by_study.items(), key=lambda item: (-len(item[1]), item[0])):
        missing = sorted(REQUIRED_PAIRS - pairs)
        top.append(
            {
                "study_id": sid,
                "observed_pair_count": str(len(pairs)),
                "missing_pair_count": str(len(missing)),
                "has_anx_tru": str("ANX-TRU" in pairs),
                "missing_pairs": ";".join(missing),
            }
        )
    return {
        "observed_pairs": observed_pairs,
        "missing_pairs": sorted(REQUIRED_PAIRS - observed_pairs),
        "complete_cases": complete,
        "top_studies": top,
        "study_count": len(by_study),
    }


def frozen_anx_tru_rows() -> dict[str, dict[str, str]]:
    rows = read_csv(FROZEN_REFERENCE)
    out: dict[str, dict[str, str]] = {}
    for row in rows:
        if row.get("construct_1") == "ANX" and row.get("construct_2") == "TRU":
            out[row["study_id"]] = row
    return out


def diagnostic_row(
    template: dict[str, str],
    frozen: dict[str, str],
    idx: int,
    statistic_family: str,
    confidence: str,
    notes: str,
) -> dict[str, str]:
    row = {key: "" for key in template}
    sid = frozen["study_id"]
    row.update(
        {
            "analysis_record_id": f"P1-ANXTRU-RESCUE-{idx:05d}",
            "analysis_set": "paper_a_source_corrected_plus_anx_tru_diagnostic",
            "analysis_role": "diagnostic source-confirmed ANX-TRU row pending researcher promotion",
            "input_id": f"ANXTRU-RESCUE-{sid}",
            "source_decision_id": frozen.get("reference_record_id", ""),
            "source_pair": "full_corpus_reference_standard_frozen_20260609",
            "study_id": sid,
            "construct_1": "ANX",
            "construct_2": "TRU",
            "construct_pair": "ANX-TRU",
            "construct_pair_canonical": "ANX-TRU",
            "construct_pair_direction": "as_reported; correlation analyses should use canonical key",
            "r_value": frozen.get("r_value", ""),
            "r_numeric": frozen.get("r_value", ""),
            "r_abs": str(abs(float(frozen.get("r_value", "0")))),
            "r_source": frozen.get("r_source", ""),
            "statistic_family": statistic_family,
            "evidence_type": frozen.get("evidence_type", ""),
            "is_source_reported_or_direct": "1",
            "is_model_derived_or_converted": "0",
            "include_primary": "1",
            "include_expanded": "1",
            "include_sensitivity": "0",
            "sample_size": frozen.get("n", ""),
            "sample_size_numeric": frozen.get("n", ""),
            "sample_size_original": frozen.get("n", ""),
            "sample_size_numeric_original": frozen.get("n", ""),
            "significance": "NR",
            "confidence": confidence,
            "consensus_basis": frozen.get("decision_status", ""),
            "conversion_rule": "none",
            "override_rule": "anx_tru_rescue_diagnostic_not_final_promotion",
            "source_location": frozen.get("source_location", ""),
            "source_artifact": f"{PRIVATE_ROOT}/Meta/AI Adoption/PDFs/{sid}.pdf",
            "source_locator": frozen.get("source_location", ""),
            "notes": notes,
            "freeze_tier": "diagnostic_from_frozen_reference_pending_paper_a_promotion",
            "include_primary_model_ready": "1",
            "freeze_decision": "diagnostic_only_pending_researcher_promotion",
            "substitution_scenario": "source_corrected_plus_anx_tru_diagnostic",
            "substitution_action": "add_diagnostic_source_confirmed_anx_tru",
            "substitution_source_task_unit_id": f"ANXTRU-RESCUE-{sid}",
            "substitution_review_priority": "P0_anx_tru_full10_coverage_gate",
            "substitution_model_id": "",
            "substitution_original_r_numeric": "",
            "substitution_r_numeric": frozen.get("r_value", ""),
            "substitution_delta": "",
            "sample_size_reconciliation_status": "filled_from_frozen_reference",
            "sample_size_reconciliation_source": frozen.get("reference_record_id", ""),
            "sample_size_reconciliation_rule": "study_pair_single_n_from_frozen_reference",
            "sample_size_reconciliation_note": "Diagnostic row uses N from frozen full-corpus reference.",
            "masem_n_weighted_eligibility": "include_n_weighted_masem_diagnostic",
            "sample_size_pdf_override_original_status": "not_checked_in_this_script",
            "sample_size_pdf_override_value": "",
            "sample_size_pdf_override_source": "",
            "sample_size_pdf_override_status": "not_needed_for_diagnostic_reference_row",
            "sample_size_pdf_override_note": "N inherited from frozen full-corpus reference row.",
        }
    )
    return row


def build_review_rows(frozen: dict[str, dict[str, str]]) -> list[dict[str, str]]:
    return [
        {
            "study_id": "S036",
            "construct_pair": "ANX-TRU",
            "source_value": "-0.260",
            "n": frozen["S036"].get("n", ""),
            "source_location": "S036.pdf Table 4 Fornell-Larcker findings",
            "source_text_evidence": "Table 4 row PT, column AI-ANX = -0.260; constructs are AI-ANX and perceived trust.",
            "source_policy_decision": "source_confirmed_add_candidate_for_diagnostic_primary",
            "analytic_role": "primary-plausible direct/latent correlation candidate",
            "promotion_status": "diagnostic_only_pending_researcher_promotion",
            "rationale": "Human/frozen row exists and PDF table confirms a same-matrix numeric ANX-TRU cell. No beta/path conversion.",
        },
        {
            "study_id": "S102",
            "construct_pair": "ANX-TRU",
            "source_value": "0.027",
            "n": frozen["S102"].get("n", ""),
            "source_location": "S102.pdf Tab. 4 Fornell-Larcker criterion",
            "source_text_evidence": "Tab. 4 row T, column TS = 0.027; note defines TS as technostress and T as trust.",
            "source_policy_decision": "source_confirmed_add_candidate_for_diagnostic_primary_with_mapping_caveat",
            "analytic_role": "primary-plausible latent correlation candidate if technostress->ANX mapping is retained",
            "promotion_status": "diagnostic_only_pending_researcher_promotion",
            "rationale": "Frozen reference accepted technostress->ANX with caveat; PDF confirms same-matrix numeric TS-T value.",
        },
        {
            "study_id": "S066",
            "construct_pair": "ANX-TRU",
            "source_value": "0.19 in frozen reference; PDF-visible Table 7 path PT->TANX = 0.140",
            "n": frozen["S066"].get("n", ""),
            "source_location": "S066.pdf Table 7 path analysis; Table 3 HTMT",
            "source_text_evidence": "Table 7 reports Perceived Trust -> Technological Anxiety path coefficient, not a zero-order/latent correlation.",
            "source_policy_decision": "exclude_source_type_mismatch_for_primary",
            "analytic_role": "sensitivity/secondary only",
            "promotion_status": "not_added_to_primary_diagnostic_input",
            "rationale": "Frozen row is beta/path converted with retained caveat; active primary route should not use path conversion as direct correlation.",
        },
        {
            "study_id": "S142",
            "construct_pair": "ANX-TRU",
            "source_value": "",
            "n": "",
            "source_location": "S142.pdf Table 3 and construct list",
            "source_text_evidence": "Study constructs include ATAI, FCs, PE, PTAI, TCs, USEAI; no source-confirmed trust and anxiety target pair.",
            "source_policy_decision": "exclude_ai_false_positive_target_construct_mismatch",
            "analytic_role": "exclude from ANX-TRU rescue",
            "promotion_status": "not_added_to_primary_diagnostic_input",
            "rationale": "Prejudice toward AI and teaching concerns are not approved ANX-TRU target construct mapping for this rescue.",
        },
    ]


def write_report(
    path: Path,
    review_rows: list[dict[str, str]],
    before: dict[str, object],
    after: dict[str, object],
) -> None:
    top_after = after["top_studies"][:10]  # type: ignore[index]
    lines = [
        "# Paper A ANX-TRU Rescue After S004/S048 Source Correction",
        "",
        "Date: 2026-06-14",
        "",
        "## Bottom line",
        "",
        "- `ANX-TRU` was not absent from the source corpus: source/frozen rows exist for `S036`, `S066`, and `S102`.",
        "- For the active primary direct/latent-correlation route, only `S036` and `S102` are diagnostic-add candidates.",
        "- `S066` remains sensitivity-only because the frozen value is beta/path converted.",
        "- `S142` is excluded from this rescue because the source constructs do not support an approved `ANX-TRU` target mapping.",
        "- Adding `S036` and `S102` restores full10 pair coverage from 44/45 to 45/45, but it does not create any full10 complete-case study.",
        "",
        "## Candidate decisions",
        "",
        "| study | value | decision | rationale |",
        "| --- | ---: | --- | --- |",
    ]
    for row in review_rows:
        lines.append(
            f"| {row['study_id']} | {row['source_value']} | "
            f"{row['source_policy_decision']} | {row['rationale']} |"
        )

    lines.extend(
        [
            "",
            "## Coverage consequence",
            "",
            f"- Before rescue: observed full10 pairs `{len(before['observed_pairs'])}/45`; missing `{';'.join(before['missing_pairs']) or 'none'}`.",
            f"- After diagnostic rescue: observed full10 pairs `{len(after['observed_pairs'])}/45`; missing `{';'.join(after['missing_pairs']) or 'none'}`.",
            f"- Full10 complete-case studies after rescue: `{len(after['complete_cases'])}`.",
            "",
            "## Highest-coverage studies after diagnostic rescue",
            "",
            "| study | observed pairs | missing pairs | has ANX-TRU |",
            "| --- | ---: | ---: | --- |",
        ]
    )
    for row in top_after:
        lines.append(
            f"| {row['study_id']} | {row['observed_pair_count']} | "
            f"{row['missing_pair_count']} | {row['has_anx_tru']} |"
        )

    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "The immediate `ANX-TRU` issue is a pipeline/input-boundary problem, not a PDF-access problem. "
            "The pair exists in the frozen full-corpus reference and is PDF-visible for `S036` and `S102`, "
            "but those rows were not present in the current Paper A source-corrected input.",
            "",
            "This rescue alone is not enough for the primary full 10-construct MASEM route. "
            "It closes pair-level coverage, but full10 still has zero complete-case studies and the prior sparse partial-matrix TSSEM route failed with non-positive-definite implied covariance. "
            "The next defensible work is therefore to densify same-study matrices for high-coverage studies or to define a defensible missing-data TSSEM/MASEM strategy before manuscript-level full10 claims.",
            "",
            "## Artifact status",
            "",
            "- This is a diagnostic/review packet only.",
            "- It does not mutate raw coder workbooks.",
            "- It does not mutate the frozen reference standard.",
            "- It does not constitute final Paper A row promotion until the researcher explicitly approves the promotion.",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n")


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    ONEDRIVE_DIR.mkdir(parents=True, exist_ok=True)

    base_rows = read_csv(BASE_INPUT)
    if not base_rows:
        raise RuntimeError(f"No rows in {BASE_INPUT}")

    headers = list(base_rows[0].keys())
    before = coverage(base_rows)
    frozen = frozen_anx_tru_rows()

    diagnostic_adds = [
        diagnostic_row(
            {key: "" for key in headers},
            frozen["S036"],
            1,
            "source_reported_direct_r",
            "high",
            "Diagnostic rescue row: S036 PDF Table 4 confirms AI-ANX/PT Fornell-Larcker off-diagonal value -0.260; frozen reference carries coder-agreed direct correlation.",
        ),
        diagnostic_row(
            {key: "" for key in headers},
            frozen["S102"],
            2,
            "source_reported_latent_correlation",
            "medium",
            "Diagnostic rescue row: S102 PDF Tab. 4 confirms TS/T Fornell-Larcker off-diagonal value 0.027; technostress->ANX caveat retained from frozen reference.",
        ),
    ]
    diagnostic_rows = base_rows + diagnostic_adds
    after = coverage(diagnostic_rows)

    review_rows = build_review_rows(frozen)

    review_path = OUT_DIR / "paper_a_anx_tru_rescue_candidates_20260614.csv"
    input_path = OUT_DIR / "paper_a_source_corrected_plus_anx_tru_diagnostic_input_20260614.csv"
    coverage_path = OUT_DIR / "paper_a_source_corrected_plus_anx_tru_coverage_20260614.csv"
    top_path = OUT_DIR / "paper_a_source_corrected_plus_anx_tru_top_study_missing_pairs_20260614.csv"
    report_path = OUT_DIR / "PAPER_A_ANX_TRU_RESCUE_AFTER_SOURCE_CORRECTION_20260614.md"

    write_csv(review_path, review_rows, list(review_rows[0].keys()))
    write_csv(input_path, diagnostic_rows, headers)
    write_csv(
        coverage_path,
        [
            {
                "state": "before_anx_tru_rescue",
                "observed_full10_pairs": str(len(before["observed_pairs"])),
                "missing_full10_pairs": ";".join(before["missing_pairs"]),  # type: ignore[arg-type]
                "complete_case_count": str(len(before["complete_cases"])),
                "complete_case_ids": ";".join(before["complete_cases"]),  # type: ignore[arg-type]
                "study_count": str(before["study_count"]),
            },
            {
                "state": "after_s036_s102_diagnostic_rescue",
                "observed_full10_pairs": str(len(after["observed_pairs"])),
                "missing_full10_pairs": ";".join(after["missing_pairs"]),  # type: ignore[arg-type]
                "complete_case_count": str(len(after["complete_cases"])),
                "complete_case_ids": ";".join(after["complete_cases"]),  # type: ignore[arg-type]
                "study_count": str(after["study_count"]),
            },
        ],
        [
            "state",
            "observed_full10_pairs",
            "missing_full10_pairs",
            "complete_case_count",
            "complete_case_ids",
            "study_count",
        ],
    )
    write_csv(
        top_path,
        after["top_studies"],  # type: ignore[arg-type]
        ["study_id", "observed_pair_count", "missing_pair_count", "has_anx_tru", "missing_pairs"],
    )
    write_report(report_path, review_rows, before, after)

    for path in [review_path, input_path, coverage_path, top_path, report_path]:
        shutil.copy2(path, ONEDRIVE_DIR / path.name)

    print(f"wrote {len(review_rows)} ANX-TRU rescue candidate decisions")
    print(f"wrote diagnostic input rows: {len(diagnostic_rows)}")
    print(
        "coverage before/after:",
        f"{len(before['observed_pairs'])}/45 -> {len(after['observed_pairs'])}/45",
    )
    print("complete cases after:", len(after["complete_cases"]))
    print(f"repo_out={OUT_DIR}")
    print(f"onedrive_out={ONEDRIVE_DIR}")


if __name__ == "__main__":
    main()
