#!/usr/bin/env python3
"""Promote researcher-approved Paper A ANX-TRU supplement rows.

Researcher approval on 2026-06-14:
- S036 ANX-TRU is approved for Paper A supplemental input.
- S102 ANX-TRU is approved for Paper A supplemental input with the retained
  technostress->ANX mapping caveat.

This script creates a new supplemental layer. It does not mutate the frozen
reference, raw coder workbooks, or earlier diagnostic inputs.
"""

from __future__ import annotations

import csv
import shutil
from pathlib import Path


REPO = Path(__file__).resolve().parents[2]
ONEDRIVE = Path(
    "/Users/newhosung/Library/CloudStorage/OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity/"
    "AI Adoption Meta Analysis - Documents"
)
DIAGNOSTIC_INPUT = REPO / (
    "data/04_extraction/05_llm_masem_substitution/results/"
    "paper_a_anx_tru_rescue_after_source_correction_20260614/"
    "paper_a_source_corrected_plus_anx_tru_diagnostic_input_20260614.csv"
)
DIAGNOSTIC_REVIEW = REPO / (
    "data/04_extraction/05_llm_masem_substitution/results/"
    "paper_a_anx_tru_rescue_after_source_correction_20260614/"
    "paper_a_anx_tru_rescue_candidates_20260614.csv"
)
OUT_DIR = REPO / (
    "data/04_extraction/05_llm_masem_substitution/results/"
    "paper_a_researcher_approved_anx_tru_supplement_20260614"
)
ONEDRIVE_DIR = ONEDRIVE / (
    "Meta/AI Adoption/03_source_adjudication/Paper_A/"
    "2026-06-14_researcher_approved_anx_tru_supplement"
)

APPROVED = {"S036", "S102"}


def read_csv(path: Path) -> tuple[list[dict[str, str]], list[str]]:
    with path.open(newline="") as f:
        reader = csv.DictReader(f)
        return list(reader), list(reader.fieldnames or [])


def write_csv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    rows, headers = read_csv(DIAGNOSTIC_INPUT)
    review_rows, review_headers = read_csv(DIAGNOSTIC_REVIEW)

    promoted_rows: list[dict[str, str]] = []
    for row in rows:
        if row.get("study_id") in APPROVED and row.get("construct_pair_canonical") == "ANX-TRU":
            row = dict(row)
            row["analysis_set"] = "paper_a_researcher_approved_anx_tru_supplement"
            row["analysis_role"] = "researcher-approved supplemental Paper A ANX-TRU source row"
            row["override_rule"] = "researcher_approved_20260614_anx_tru_supplement"
            row["freeze_tier"] = "paper_a_supplement_researcher_approved_source_checked"
            row["freeze_decision"] = "researcher_approved_supplemental_paper_a_promotion"
            row["substitution_scenario"] = "source_corrected_plus_researcher_approved_anx_tru"
            row["substitution_action"] = "add_researcher_approved_source_confirmed_anx_tru"
            row["substitution_review_priority"] = "P0_researcher_approved_anx_tru_full10_coverage_gate"
            row["notes"] = (
                row.get("notes", "")
                + " Researcher approved promotion on 2026-06-14 for Paper A supplemental input; "
                + "not a mutation of the frozen Paper B reference."
            ).strip()
            promoted_rows.append(row)
        else:
            row = dict(row)
            if row.get("analysis_set") == "paper_a_source_corrected_plus_anx_tru_diagnostic":
                row["analysis_set"] = "paper_a_researcher_approved_anx_tru_supplement"
                row["substitution_scenario"] = "source_corrected_plus_researcher_approved_anx_tru"
            promoted_rows.append(row)

    approved_review_rows: list[dict[str, str]] = []
    for row in review_rows:
        row = dict(row)
        if row.get("study_id") in APPROVED:
            row["promotion_status"] = "researcher_approved_for_paper_a_supplement_20260614"
            row["source_policy_decision"] = row["source_policy_decision"].replace(
                "source_confirmed_add_candidate", "researcher_approved_source_confirmed_add"
            )
            row["rationale"] = (
                row.get("rationale", "")
                + " Researcher approval recorded on 2026-06-14."
            ).strip()
        approved_review_rows.append(row)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    ONEDRIVE_DIR.mkdir(parents=True, exist_ok=True)

    approved_input = OUT_DIR / "paper_a_source_corrected_plus_researcher_approved_anx_tru_input_20260614.csv"
    approved_review = OUT_DIR / "paper_a_researcher_approved_anx_tru_promotion_decisions_20260614.csv"
    report = OUT_DIR / "PAPER_A_RESEARCHER_APPROVED_ANX_TRU_SUPPLEMENT_20260614.md"

    write_csv(approved_input, promoted_rows, headers)
    write_csv(approved_review, approved_review_rows, review_headers)

    report.write_text(
        "\n".join(
            [
                "# Paper A Researcher-Approved ANX-TRU Supplement",
                "",
                "Date: 2026-06-14",
                "",
                "## Researcher approval",
                "",
                "The researcher approved promotion of the source-confirmed `ANX-TRU` rows for Paper A supplemental input:",
                "",
                "- `S036`: `ANX-TRU = -0.260`, `n = 480`, source `S036.pdf Table 4 Fornell-Larcker findings`.",
                "- `S102`: `ANX-TRU = 0.027`, `n = 284`, source `S102.pdf Tab. 4 Fornell-Larcker criterion`; retains the `technostress -> ANX` mapping caveat.",
                "",
                "Excluded rows remain excluded:",
                "",
                "- `S066`: beta/path converted; sensitivity-only, not primary direct/latent correlation.",
                "- `S142`: target construct mismatch for this `ANX-TRU` rescue.",
                "",
                "## Boundary",
                "",
                "This supplement does not alter the Paper B frozen source-anchored adjudicated human reference standard and does not mutate raw coder workbooks. It creates a Paper A supplemental input layer.",
                "",
                "## Analysis consequence",
                "",
                "The approved supplement closes the full10 pair-level gap (`ANX-TRU`) but does not create a full10 complete-case matrix and does not resolve sparse partial-matrix TSSEM non-positive-definite estimation failures.",
            ]
        )
        + "\n"
    )

    for path in [approved_input, approved_review, report]:
        shutil.copy2(path, ONEDRIVE_DIR / path.name)

    print("approved_promotions=S036,S102")
    print(f"approved_input_rows={len(promoted_rows)}")
    print(f"repo_out={OUT_DIR}")
    print(f"onedrive_out={ONEDRIVE_DIR}")


if __name__ == "__main__":
    main()
