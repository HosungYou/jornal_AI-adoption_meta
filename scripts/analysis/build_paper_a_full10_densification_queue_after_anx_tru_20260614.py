#!/usr/bin/env python3
"""Build a bounded Paper A full10 densification queue after ANX-TRU rescue.

The queue separates source-densification candidates from studies that are
structurally unable to become full 10-construct complete cases because target
constructs were not measured. It does not edit analytic inputs.
"""

from __future__ import annotations

import csv
import itertools
import shutil
from collections import defaultdict
from pathlib import Path


REPO = Path(__file__).resolve().parents[2]
ONEDRIVE = Path(
    "/Users/newhosung/Library/CloudStorage/OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity/"
    "AI Adoption Meta Analysis - Documents"
)
INPUT = REPO / (
    "data/04_extraction/05_llm_masem_substitution/results/"
    "paper_a_anx_tru_rescue_after_source_correction_20260614/"
    "paper_a_source_corrected_plus_anx_tru_diagnostic_input_20260614.csv"
)
OUT_DIR = REPO / (
    "data/04_extraction/05_llm_masem_substitution/results/"
    "paper_a_full10_densification_queue_after_anx_tru_20260614"
)
ONEDRIVE_DIR = ONEDRIVE / (
    "Meta/AI Adoption/03_source_adjudication/Paper_A/"
    "2026-06-14_full10_densification_queue_after_anx_tru"
)

TARGET_CONSTRUCTS = ["PE", "EE", "SI", "FC", "TRU", "ANX", "SE", "ATT", "BI", "UB"]
TARGET_SET = set(TARGET_CONSTRUCTS)
REQUIRED_PAIRS = {
    "-".join(sorted(pair)) for pair in itertools.combinations(TARGET_CONSTRUCTS, 2)
}

SOURCE_INFORMED_OVERRIDES = {
    "S048": {
        "source_review_status": "source_checked_20260614",
        "densification_decision": "not_full10_completable_from_source",
        "source_basis": "PDF measurement/correlation tables support PE, EE, SI, FC, TRU, ATT, BI, UB plus non-target constructs; anxiety and self-efficacy are not measured target constructs.",
        "next_action": "Do not spend more full10 rescue time on S048 unless researcher opens a new construct-mapping rule for ANX or SE.",
    },
    "S176": {
        "source_review_status": "source_checked_20260614",
        "densification_decision": "not_full10_completable_from_source",
        "source_basis": "PDF instrument/results support PE, EE, SI, FC, TRU, BI, UB and adjacent non-target constructs such as HM/HA/PI; anxiety and self-efficacy are not measured target constructs.",
        "next_action": "Do not spend more full10 rescue time on S176 unless researcher opens a new construct-mapping rule for ANX or SE.",
    },
}


def canonical_pair(a: str, b: str) -> str:
    return "-".join(sorted([a, b]))


def primary_ready(row: dict[str, str]) -> bool:
    marker = row.get("include_primary_model_ready") or row.get("include_primary") or ""
    return marker in {"1", "TRUE", "True", "true", "yes", "Y"}


def main() -> None:
    by_construct: dict[str, set[str]] = defaultdict(set)
    by_pair: dict[str, set[str]] = defaultdict(set)
    with INPUT.open(newline="") as f:
        for row in csv.DictReader(f):
            if not primary_ready(row):
                continue
            sid = row.get("study_id", "")
            c1 = row.get("construct_1", "")
            c2 = row.get("construct_2", "")
            if c1 in TARGET_SET:
                by_construct[sid].add(c1)
            if c2 in TARGET_SET:
                by_construct[sid].add(c2)
            if c1 in TARGET_SET and c2 in TARGET_SET and c1 != c2:
                by_pair[sid].add(row.get("construct_pair_canonical") or canonical_pair(c1, c2))

    rows: list[dict[str, str]] = []
    for sid in sorted(by_construct, key=lambda s: (-len(by_pair[s]), -len(by_construct[s]), s)):
        constructs = by_construct[sid]
        pairs = by_pair[sid]
        missing_constructs = sorted(TARGET_SET - constructs)
        missing_pairs = sorted(REQUIRED_PAIRS - pairs)
        override = SOURCE_INFORMED_OVERRIDES.get(sid, {})
        if override:
            decision = override["densification_decision"]
            review_status = override["source_review_status"]
            source_basis = override["source_basis"]
            next_action = override["next_action"]
        elif missing_constructs:
            decision = "source_review_needed_before_full10_claim"
            review_status = "not_source_checked_in_this_queue"
            source_basis = "Current diagnostic input lacks at least one full10 target construct; source PDF must be checked before considering densification."
            next_action = "Review source only if this study is prioritized after S048/S176; classify missing constructs before extracting pair cells."
        elif missing_pairs:
            decision = "pair_level_densification_candidate"
            review_status = "not_source_checked_in_this_queue"
            source_basis = "All target constructs appear in current input, but some pair cells are missing."
            next_action = "Check source correlation matrix for missing pair cells."
        else:
            decision = "complete_case_available"
            review_status = "not_applicable"
            source_basis = "All target pairs are present in diagnostic input."
            next_action = "Eligible for complete-case route."

        rows.append(
            {
                "study_id": sid,
                "observed_construct_count": str(len(constructs)),
                "observed_constructs": ";".join(sorted(constructs)),
                "missing_constructs": ";".join(missing_constructs),
                "observed_pair_count": str(len(pairs)),
                "missing_pair_count": str(len(missing_pairs)),
                "has_anx_tru": str("ANX-TRU" in pairs),
                "source_review_status": review_status,
                "densification_decision": decision,
                "source_basis": source_basis,
                "next_action": next_action,
                "missing_pairs": ";".join(missing_pairs),
            }
        )

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    ONEDRIVE_DIR.mkdir(parents=True, exist_ok=True)

    queue_path = OUT_DIR / "paper_a_full10_densification_queue_after_anx_tru_20260614.csv"
    with queue_path.open("w", newline="") as f:
        fieldnames = list(rows[0].keys())
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    report_path = OUT_DIR / "PAPER_A_FULL10_DENSIFICATION_QUEUE_AFTER_ANX_TRU_20260614.md"
    top = rows[:12]
    lines = [
        "# Paper A Full10 Densification Queue After ANX-TRU Rescue",
        "",
        "Date: 2026-06-14",
        "",
        "## Bottom line",
        "",
        "- `S048` and `S176` are the densest studies in the current diagnostic input, each with 28/45 full10 pairs.",
        "- Both are structurally blocked for full10 complete-case use because the source does not measure target `ANX` and target `SE` constructs.",
        "- Therefore the full10 route should not be pursued by repeatedly retrying TSSEM on the same sparse partial matrix.",
        "- The next defensible decision is whether Paper A's primary route remains full10 with a new missing-data strategy, or whether full10 is framed as theory target while reduced routes carry the empirical MASEM results.",
        "",
        "## Top queue",
        "",
        "| study | constructs | pairs | missing constructs | decision |",
        "| --- | ---: | ---: | --- | --- |",
    ]
    for row in top:
        lines.append(
            f"| {row['study_id']} | {row['observed_construct_count']}/10 | "
            f"{row['observed_pair_count']}/45 | {row['missing_constructs'] or 'none'} | "
            f"{row['densification_decision']} |"
        )

    lines.extend(
        [
            "",
            "## Source-checked high-density studies",
            "",
            "### S048",
            "",
            "Current diagnostic input has `PE, EE, SI, FC, TRU, ATT, BI, UB` and 28/45 pairs. "
            "PDF table/instrument evidence supports those constructs and adjacent non-target constructs, but does not provide measured target `ANX` or `SE`. "
            "Full10 completion would require unsupported construct remapping, not simple cell extraction.",
            "",
            "### S176",
            "",
            "Current diagnostic input has `PE, EE, SI, FC, TRU, ATT, BI, UB` and 28/45 pairs. "
            "PDF evidence supports trust and UTAUT-related constructs plus adjacent constructs such as hedonic motivation, habit, and personal innovativeness; it does not provide measured target `ANX` or `SE`. "
            "Full10 completion would require unsupported construct remapping, not simple cell extraction.",
            "",
            "## Implication for Paper A",
            "",
            "The evidence now distinguishes two separate issues:",
            "",
            "1. Pair-level `ANX-TRU` coverage can be rescued diagnostically using S036/S102.",
            "2. Full10 complete-case MASEM remains blocked because the densest studies do not measure all full10 target constructs.",
            "",
            "Recommended next step: write Paper A analysis plan/manuscript language that treats full10 as the theoretical target and reports reduced, source-defensible complete-case MASEM routes as empirical sensitivity/mechanism models unless a missing-data TSSEM strategy is explicitly adopted and validated.",
        ]
    )
    report_path.write_text("\n".join(lines) + "\n")

    for path in [queue_path, report_path]:
        shutil.copy2(path, ONEDRIVE_DIR / path.name)

    print(f"wrote queue rows: {len(rows)}")
    print(f"repo_out={OUT_DIR}")
    print(f"onedrive_out={ONEDRIVE_DIR}")
    print("top_decisions:")
    for row in rows[:5]:
        print(row["study_id"], row["observed_pair_count"], row["missing_constructs"], row["densification_decision"])


if __name__ == "__main__":
    main()
