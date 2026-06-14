#!/usr/bin/env python3
"""Build Paper A priority-15 source review artifacts for 2026-06-14.

This script records a conservative source-review pass over the 15 broader AI
candidate rows that survived the construct-support triage gate. It does not
modify analytic inputs, workbooks, or frozen reference files.
"""

from __future__ import annotations

import csv
from dataclasses import dataclass
from itertools import combinations
from pathlib import Path


REPO = Path("/Users/newhosung/Academic/2026/AI Adoption Meta Analysis")
ONEDRIVE = Path(
    "/Users/newhosung/Library/CloudStorage/OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity/"
    "AI Adoption Meta Analysis - Documents"
)
OUT_DIR = ONEDRIVE / (
    "Meta/AI Adoption/03_source_adjudication/Paper_A/"
    "2026-06-14_priority15_detailed_source_review"
)
REPO_POINTER_DIR = REPO / (
    "data/04_extraction/05_llm_masem_substitution/results/"
    "paper_a_priority15_detailed_source_review_20260614"
)
FROZEN_REFERENCE = REPO / (
    "data/04_extraction/04_reference_standard_freeze/"
    "full_corpus_reference_standard_frozen_20260609.csv"
)


def pair(a: str, b: str) -> tuple[str, str]:
    return tuple(sorted((a, b)))


@dataclass(frozen=True)
class CandidateDecision:
    study_id: str
    construct_1: str
    construct_2: str
    decision: str
    r_value: str
    source_location: str
    evidence_type: str
    source_construct_1: str
    source_construct_2: str
    mapping_basis: str
    reason: str
    next_required_action: str


S004_SOURCE_APPROVED = {
    pair("PE", "EE"): 0.697,
    pair("PE", "SI"): 0.637,
    pair("PE", "FC"): 0.676,
    pair("PE", "TRU"): 0.541,
    pair("PE", "BI"): 0.667,
    pair("PE", "UB"): 0.607,
    pair("EE", "SI"): 0.610,
    pair("EE", "FC"): 0.664,
    pair("EE", "TRU"): 0.520,
    pair("EE", "BI"): 0.582,
    pair("EE", "UB"): 0.607,
    pair("SI", "FC"): 0.590,
    pair("SI", "TRU"): 0.563,
    pair("SI", "BI"): 0.668,
    pair("SI", "UB"): 0.644,
    pair("FC", "TRU"): 0.533,
    pair("FC", "BI"): 0.644,
    pair("FC", "UB"): 0.601,
    pair("TRU", "BI"): 0.630,
    pair("TRU", "UB"): 0.599,
    pair("BI", "UB"): 0.751,
}

S004_REJECTED_PKC_AS_SE_VALUES = {
    pair("BI", "SE"): 0.625,
    pair("EE", "SE"): 0.700,
    pair("FC", "SE"): 0.691,
    pair("SE", "SI"): 0.584,
    pair("SE", "TRU"): 0.591,
    pair("SE", "UB"): 0.621,
    pair("PE", "SE"): 0.627,
}

S048_SOURCE = {
    pair("PE", "EE"): 0.536,
    pair("PE", "SI"): 0.433,
    pair("PE", "FC"): 0.471,
    pair("PE", "TRU"): 0.481,
    pair("PE", "ATT"): 0.677,
    pair("PE", "BI"): 0.659,
    pair("PE", "UB"): 0.596,
    pair("EE", "SI"): 0.310,
    pair("EE", "FC"): 0.659,
    pair("EE", "TRU"): 0.391,
    pair("EE", "ATT"): 0.468,
    pair("EE", "BI"): 0.453,
    pair("EE", "UB"): 0.398,
    pair("SI", "FC"): 0.323,
    pair("SI", "TRU"): 0.436,
    pair("SI", "ATT"): 0.575,
    pair("SI", "BI"): 0.626,
    pair("SI", "UB"): 0.589,
    pair("FC", "TRU"): 0.364,
    pair("FC", "ATT"): 0.385,
    pair("FC", "BI"): 0.424,
    pair("FC", "UB"): 0.340,
    pair("TRU", "ATT"): 0.512,
    pair("TRU", "BI"): 0.527,
    pair("TRU", "UB"): 0.442,
    pair("ATT", "BI"): 0.820,
    pair("ATT", "UB"): 0.769,
    pair("BI", "UB"): 0.829,
}

PRIORITY_CANDIDATE_PAIRS = {
    ("S004", pair("BI", "SE")),
    ("S004", pair("EE", "SE")),
    ("S004", pair("FC", "SE")),
    ("S004", pair("SE", "SI")),
    ("S004", pair("SE", "TRU")),
    ("S004", pair("SE", "UB")),
    ("S048", pair("BI", "FC")),
    ("S048", pair("BI", "PE")),
    ("S048", pair("BI", "SI")),
    ("S048", pair("EE", "UB")),
    ("S048", pair("FC", "UB")),
    ("S048", pair("SI", "UB")),
    ("S048", pair("TRU", "UB")),
}


def read_frozen_rows() -> dict[str, dict[tuple[str, str], float]]:
    out: dict[str, dict[tuple[str, str], float]] = {}
    with FROZEN_REFERENCE.open(newline="", encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            sid = row["study_id"]
            if sid not in {"S004", "S048", "S072"}:
                continue
            try:
                rv = float(row["r_value"])
            except ValueError:
                continue
            out.setdefault(sid, {})[pair(row["construct_1"], row["construct_2"])] = rv
    return out


def decisions() -> list[CandidateDecision]:
    s004_loc = "S004.pdf Table 4; correlation matrix and square root of AVE; text lines 727-738"
    s048_loc = "S048.pdf Table 2; correlation and descriptive statistics; PDF page 326 / rendered page 13"
    s072_loc = "S072.pdf Table 2; Discriminant validity Fornell-Larcker criterion; text lines 522-539"

    rows: list[CandidateDecision] = [
        CandidateDecision(
            "S004",
            "BI",
            "SE",
            "exclude_ai_false_positive",
            "0.625",
            s004_loc,
            "latent_construct_correlation",
            "IU",
            "PKC",
            "Researcher decision on 2026-06-14: PKC is not approved as SE.",
            "The numeric off-diagonal cell IU-PKC is visible, but PKC is not an approved self-efficacy construct.",
            "Do not promote; remove or reopen PKC-derived SE rows if they appear in frozen inputs.",
        ),
        CandidateDecision(
            "S004",
            "EE",
            "SE",
            "exclude_ai_false_positive",
            "0.700",
            s004_loc,
            "latent_construct_correlation",
            "EE",
            "PKC",
            "Researcher decision on 2026-06-14: PKC is not approved as SE.",
            "The numeric off-diagonal cell EE-PKC is visible, but PKC is not an approved self-efficacy construct.",
            "Do not promote.",
        ),
        CandidateDecision(
            "S004",
            "FC",
            "SE",
            "exclude_ai_false_positive",
            "0.691",
            s004_loc,
            "latent_construct_correlation",
            "FC",
            "PKC",
            "Researcher decision on 2026-06-14: PKC is not approved as SE.",
            "The numeric off-diagonal cell FC-PKC is visible, but PKC is not an approved self-efficacy construct.",
            "Do not promote.",
        ),
        CandidateDecision(
            "S004",
            "SE",
            "SI",
            "exclude_ai_false_positive",
            "0.584",
            s004_loc,
            "latent_construct_correlation",
            "PKC",
            "SI",
            "Researcher decision on 2026-06-14: PKC is not approved as SE.",
            "The numeric off-diagonal cell PKC-SI is visible, but PKC is not an approved self-efficacy construct.",
            "Do not promote.",
        ),
        CandidateDecision(
            "S004",
            "SE",
            "TRU",
            "exclude_ai_false_positive",
            "0.591",
            s004_loc,
            "latent_construct_correlation",
            "PKC",
            "TC",
            "Researcher decision on 2026-06-14: PKC is not approved as SE.",
            "The numeric off-diagonal cell PKC-TC is visible, but PKC is not an approved self-efficacy construct.",
            "Do not promote.",
        ),
        CandidateDecision(
            "S004",
            "SE",
            "UB",
            "exclude_ai_false_positive",
            "0.621",
            s004_loc,
            "latent_construct_correlation",
            "PKC",
            "UB",
            "Researcher decision on 2026-06-14: PKC is not approved as SE.",
            "The numeric off-diagonal cell PKC-UB is visible, but PKC is not an approved self-efficacy construct.",
            "Do not promote.",
        ),
        CandidateDecision(
            "S048",
            "BI",
            "FC",
            "source_confirmed_add_candidate",
            "0.424",
            s048_loc,
            "pearson_correlation",
            "INT",
            "FC",
            "S048 note defines INT as behavioural intention and FC as facilitating conditions.",
            "The Pearson r cell INT-FC is visible in Table 2.",
            "Promote only with an S048 reference correction pass; existing frozen rows show column/row shift mismatches.",
        ),
        CandidateDecision(
            "S048",
            "BI",
            "PE",
            "source_confirmed_add_candidate",
            "0.659",
            s048_loc,
            "pearson_correlation",
            "INT",
            "PE",
            "S048 note defines INT as behavioural intention and PE as performance expectancy.",
            "The Pearson r cell INT-PE is visible in Table 2.",
            "Promote only with an S048 reference correction pass.",
        ),
        CandidateDecision(
            "S048",
            "BI",
            "SI",
            "source_confirmed_add_candidate",
            "0.626",
            s048_loc,
            "pearson_correlation",
            "INT",
            "SI",
            "S048 note defines INT as behavioural intention and SI as social influence.",
            "The Pearson r cell INT-SI is visible in Table 2.",
            "Promote only with an S048 reference correction pass.",
        ),
        CandidateDecision(
            "S048",
            "EE",
            "UB",
            "source_confirmed_add_candidate",
            "0.398",
            s048_loc,
            "pearson_correlation",
            "EE",
            "USE",
            "S048 note defines USE as use behaviour and EE as effort expectancy.",
            "The Pearson r cell USE-EE is visible in Table 2.",
            "Promote only with an S048 reference correction pass.",
        ),
        CandidateDecision(
            "S048",
            "FC",
            "UB",
            "source_confirmed_add_candidate",
            "0.340",
            s048_loc,
            "pearson_correlation",
            "FC",
            "USE",
            "S048 note defines USE as use behaviour and FC as facilitating conditions.",
            "The Pearson r cell USE-FC is visible in Table 2.",
            "Promote only with an S048 reference correction pass.",
        ),
        CandidateDecision(
            "S048",
            "SI",
            "UB",
            "source_confirmed_add_candidate",
            "0.589",
            s048_loc,
            "pearson_correlation",
            "SI",
            "USE",
            "S048 note defines USE as use behaviour and SI as social influence.",
            "The Pearson r cell USE-SI is visible in Table 2.",
            "Promote only with an S048 reference correction pass.",
        ),
        CandidateDecision(
            "S048",
            "TRU",
            "UB",
            "source_confirmed_add_candidate",
            "0.442",
            s048_loc,
            "pearson_correlation",
            "TRU",
            "USE",
            "S048 note defines USE as use behaviour and TRU as trust.",
            "The Pearson r cell USE-TRU is visible in Table 2.",
            "Promote only with an S048 reference correction pass.",
        ),
        CandidateDecision(
            "S072",
            "ANX",
            "ATT",
            "human_excluded",
            "",
            s072_loc,
            "latent_construct_correlation",
            "PC/HM",
            "",
            "Frozen S072 notes explicitly rejected PC->ANX and HM->ATT mappings.",
            "The source table contains PC and HM, not approved ANX or ATT constructs for this draft.",
            "Do not promote unless the researcher explicitly reopens the S072 construct mapping decision.",
        ),
        CandidateDecision(
            "S072",
            "ATT",
            "UB",
            "human_excluded",
            "",
            s072_loc,
            "latent_construct_correlation",
            "HM/VU",
            "",
            "Frozen S072 notes explicitly rejected HM->ATT; VU maps to use but ATT is not approved.",
            "The source table contains HM and VU, not an approved ATT-UB target pair.",
            "Do not promote unless the researcher explicitly reopens the S072 construct mapping decision.",
        ),
    ]
    return rows


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def build_integrity_flags(frozen: dict[str, dict[tuple[str, str], float]]) -> list[dict[str, str]]:
    flags: list[dict[str, str]] = []
    source_by_study = {
        "S004": S004_SOURCE_APPROVED,
        "S048": S048_SOURCE,
    }
    source_locations = {
        "S004": "S004.pdf Table 4",
        "S048": "S048.pdf Table 2",
    }
    for sid, source in source_by_study.items():
        frozen_pairs = frozen.get(sid, {})
        for pp, src_val in sorted(source.items()):
            frozen_val = frozen_pairs.get(pp)
            if frozen_val is None:
                if (sid, pp) in PRIORITY_CANDIDATE_PAIRS:
                    continue
                flags.append(
                    {
                        "study_id": sid,
                        "construct_1": pp[0],
                        "construct_2": pp[1],
                        "flag": "source_pair_missing_from_frozen_reference",
                        "frozen_r_value": "",
                        "source_r_value": f"{src_val:.3f}",
                        "source_location": source_locations[sid],
                        "recommended_action": "Reopen source adjudication for this study before matrix densification.",
                    }
                )
                continue
            if abs(frozen_val - src_val) > 0.001:
                flags.append(
                    {
                        "study_id": sid,
                        "construct_1": pp[0],
                        "construct_2": pp[1],
                        "flag": "frozen_value_differs_from_source_table",
                        "frozen_r_value": f"{frozen_val:.3f}",
                        "source_r_value": f"{src_val:.3f}",
                        "source_location": source_locations[sid],
                        "recommended_action": "Do not add AI candidates alone; correct or adjudicate the existing frozen row alignment first.",
                    }
                )
        for pp, frozen_val in sorted(frozen_pairs.items()):
            if pp in source:
                continue
            flags.append(
                {
                    "study_id": sid,
                    "construct_1": pp[0],
                    "construct_2": pp[1],
                    "flag": "frozen_pair_not_supported_after_mapping_decision",
                    "frozen_r_value": f"{frozen_val:.3f}",
                    "source_r_value": "",
                    "source_location": source_locations[sid],
                    "recommended_action": "Remove from corrected source-adjudication proposal unless another source establishes this approved target pair.",
                }
            )
    return flags


def build_correction_proposal(frozen: dict[str, dict[tuple[str, str], float]]) -> list[dict[str, str]]:
    source_by_study = {
        "S004": S004_SOURCE_APPROVED,
        "S048": S048_SOURCE,
    }
    source_locations = {
        "S004": "S004.pdf Table 4",
        "S048": "S048.pdf Table 2",
    }
    mappings = {
        "S004": "TC->TRU; IU->BI; UB->UB; PE/EE/SI/FC unchanged; PKC->SE rejected by researcher on 2026-06-14",
        "S048": "INT->BI; USE->UB; PE/EE/SI/FC/TRU/ATT unchanged",
    }
    rows: list[dict[str, str]] = []
    for sid, source in source_by_study.items():
        for pp, src_val in sorted(source.items()):
            frozen_val = frozen.get(sid, {}).get(pp)
            if frozen_val is None:
                action = "add_priority_candidate" if (sid, pp) in PRIORITY_CANDIDATE_PAIRS else "add_source_visible_non_candidate"
            elif abs(frozen_val - src_val) > 0.001:
                action = "correct_existing_frozen_value"
            else:
                action = "keep_existing_frozen_value"
            rows.append(
                {
                    "study_id": sid,
                    "construct_1": pp[0],
                    "construct_2": pp[1],
                    "action": action,
                    "current_frozen_r_value": "" if frozen_val is None else f"{frozen_val:.3f}",
                    "proposed_source_r_value": f"{src_val:.3f}",
                    "source_location": source_locations[sid],
                    "source_mapping": mappings[sid],
                    "researcher_confirmation_required": "yes",
                }
            )
        for pp, frozen_val in sorted(frozen.get(sid, {}).items()):
            if pp in source:
                continue
            rows.append(
                {
                    "study_id": sid,
                    "construct_1": pp[0],
                    "construct_2": pp[1],
                    "action": "remove_unapproved_or_source_unsupported_pair",
                    "current_frozen_r_value": f"{frozen_val:.3f}",
                    "proposed_source_r_value": "",
                    "source_location": source_locations[sid],
                    "source_mapping": mappings[sid],
                    "researcher_confirmation_required": "yes",
                }
            )
        if sid == "S004":
            for pp, src_val in sorted(S004_REJECTED_PKC_AS_SE_VALUES.items()):
                if pp in frozen.get(sid, {}):
                    continue
                rows.append(
                    {
                        "study_id": sid,
                        "construct_1": pp[0],
                        "construct_2": pp[1],
                        "action": "reject_priority_candidate_unapproved_mapping",
                        "current_frozen_r_value": "",
                        "proposed_source_r_value": f"{src_val:.3f}",
                        "source_location": "S004.pdf Table 4",
                        "source_mapping": mappings[sid],
                        "researcher_confirmation_required": "decision_recorded_pkc_not_se",
                    }
                )
    return rows


def write_markdown(path: Path, decision_rows: list[CandidateDecision], flags: list[dict[str, str]]) -> None:
    add_rows = [r for r in decision_rows if r.decision == "source_confirmed_add_candidate"]
    excluded = [r for r in decision_rows if r.decision != "source_confirmed_add_candidate"]
    s004_add = [r for r in add_rows if r.study_id == "S004"]
    s048_add = [r for r in add_rows if r.study_id == "S048"]
    s004_flags = [r for r in flags if r["study_id"] == "S004"]
    s048_flags = [r for r in flags if r["study_id"] == "S048"]

    lines = [
        "# Paper A priority-15 detailed source review",
        "",
        "Date: 2026-06-14",
        "",
        "## Boundary",
        "",
        "- This is a source-review evidence artifact, not an analytic matrix update.",
        "- No workbook, supplemental input, or frozen reference file was modified.",
        "- AI/source-trace candidates remain researcher-review evidence until confirmed.",
        "",
        "## Decision summary",
        "",
        f"- Priority candidates reviewed: {len(decision_rows)}",
        f"- Source-confirmed add candidates: {len(add_rows)}",
        f"- Excluded by prior adjudication/construct mapping: {len(excluded)}",
        f"- Existing frozen-reference integrity flags: {len(flags)}",
        "",
        "Interpretation: 7 S048 candidate cells are visible in an acceptable Pearson correlation matrix and should move forward as a source-correction proposal. S004 PKC-derived SE candidates are rejected because the researcher did not approve PKC as self-efficacy. S072 remains excluded because the frozen reference already rejected the required construct remaps.",
        "",
        "## Candidate decisions",
        "",
        "| study | pair | decision | source r | source constructs | source |",
        "| --- | --- | --- | ---: | --- | --- |",
    ]
    for r in decision_rows:
        source_pair = f"{r.source_construct_1}-{r.source_construct_2}".strip("-")
        lines.append(
            f"| {r.study_id} | {r.construct_1}-{r.construct_2} | {r.decision} | {r.r_value or ''} | {source_pair} | {r.source_location} |"
        )

    lines += [
        "",
        "## Study-level findings",
        "",
        "### S004",
        "",
        "- Source table: S004.pdf Table 4, correlation matrix and square root of AVE.",
        "- Approved source labels after researcher decision: TC -> TRU, IU -> BI, UB -> UB.",
        "- Rejected source mapping: PKC -> SE.",
        f"- Source-confirmed candidate cells: {len(s004_add)}.",
        f"- Additional integrity flags: {len(s004_flags)}.",
        "- Main caution: S004 should not contribute SE rows unless another source construct establishes self-efficacy. Existing PKC-derived PE-SE should be removed or reopened. FC-UB should be corrected to the visible UB-FC value, and FC-TRU is source-visible as an approved target pair.",
        "",
        "### S048",
        "",
        "- Source table: S048.pdf Table 2, Pearson correlation and descriptive statistics.",
        "- Approved source labels: INT -> BI, USE -> UB.",
        f"- Source-confirmed candidate cells: {len(s048_add)}.",
        f"- Existing frozen-reference mismatch flags: {len(s048_flags)}.",
        "- Main caution: the seven candidate cells are visible, but many existing frozen rows appear shifted against the actual Table 2 row/column layout. S048 should be reopened as a whole matrix correction item before adding candidates.",
        "",
        "### S072",
        "",
        "- Source table: S072.pdf Table 2, Fornell-Larcker latent variable correlations.",
        "- The frozen reference note states that PC->ANX and HM->ATT mappings were rejected for this draft.",
        "- Therefore ANX-ATT and ATT-UB remain excluded unless the researcher explicitly reopens the construct-mapping decision.",
        "",
        "## Recommended next step",
        "",
        "1. Treat S004 and S048 as source-adjudication correction items, not simple AI additions.",
        "2. Produce a corrected S004/S048 matrix patch for researcher confirmation.",
        "3. After confirmation, update the Paper A supplemental densification input and rerun the full10/trust6 matrix coverage and MASEM feasibility checks.",
        "",
        "## Files",
        "",
        f"- Candidate decision CSV: `{OUT_DIR / 'paper_a_priority15_detailed_source_review_20260614.csv'}`",
        f"- Integrity flag CSV: `{OUT_DIR / 'paper_a_priority15_reference_integrity_flags_20260614.csv'}`",
        f"- Correction proposal CSV: `{OUT_DIR / 'paper_a_s004_s048_source_correction_proposal_20260614.csv'}`",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    decision_rows = decisions()
    frozen = read_frozen_rows()
    flags = build_integrity_flags(frozen)
    correction_rows = build_correction_proposal(frozen)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    decision_dicts = [r.__dict__ for r in decision_rows]
    write_csv(OUT_DIR / "paper_a_priority15_detailed_source_review_20260614.csv", decision_dicts)
    write_csv(OUT_DIR / "paper_a_priority15_reference_integrity_flags_20260614.csv", flags)
    write_csv(OUT_DIR / "paper_a_s004_s048_source_correction_proposal_20260614.csv", correction_rows)
    write_markdown(OUT_DIR / "PAPER_A_PRIORITY15_DETAILED_SOURCE_REVIEW_20260614.md", decision_rows, flags)

    REPO_POINTER_DIR.mkdir(parents=True, exist_ok=True)
    (REPO_POINTER_DIR / "README.md").write_text(
        "# Paper A priority-15 detailed source review\n\n"
        "Canonical human-facing artifacts are stored in OneDrive:\n\n"
        f"`{OUT_DIR}`\n\n"
        "This repo directory is a pointer only; private PDFs and source packages are not copied here.\n",
        encoding="utf-8",
    )

    print(f"wrote {len(decision_rows)} candidate decisions")
    print(f"wrote {len(flags)} reference integrity flags")
    print(f"wrote {len(correction_rows)} S004/S048 correction proposal rows")
    print(f"output_dir={OUT_DIR}")


if __name__ == "__main__":
    main()
