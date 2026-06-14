#!/usr/bin/env python3
"""Build the Paper A source-clean submission input layer.

This layer uses researcher-approved source corrections and ANX-TRU promotions
without mutating raw coder workbooks or frozen Paper B reference files.
"""

from __future__ import annotations

import csv
import shutil
from itertools import combinations
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
ONEDRIVE = Path(
    "/Users/newhosung/Library/CloudStorage/OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity/"
    "AI Adoption Meta Analysis - Documents"
)
INPUT = REPO / (
    "data/04_extraction/05_llm_masem_substitution/results/"
    "paper_a_researcher_approved_anx_tru_supplement_20260614/"
    "paper_a_source_corrected_plus_researcher_approved_anx_tru_input_20260614.csv"
)
OUT_DIR = REPO / (
    "data/04_extraction/05_llm_masem_substitution/results/"
    "paper_a_source_clean_submission_input_20260614"
)
ONEDRIVE_DIR = ONEDRIVE / (
    "Meta/AI Adoption/04_analysis_strategy/Paper_A/"
    "2026-06-14_source_clean_submission_input"
)
FULL10 = ["PE", "EE", "SI", "FC", "ATT", "SE", "TRU", "ANX", "BI", "UB"]
CORE7 = ["PE", "EE", "SI", "FC", "ATT", "BI", "UB"]
TRUST6 = ["PE", "EE", "SI", "TRU", "BI", "UB"]


def canonical_pair(a: str, b: str) -> str:
    return "-".join(sorted([a, b]))


def read_csv(path: Path) -> tuple[list[dict[str, str]], list[str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return list(reader), list(reader.fieldnames or [])


def write_csv(path: Path, rows: list[dict[str, str]], headers: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=headers, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def observed_pairs(rows: list[dict[str, str]], constructs: list[str]) -> set[str]:
    allowed = set(constructs)
    out = set()
    for row in rows:
        c1 = row.get("construct_1", "")
        c2 = row.get("construct_2", "")
        if c1 in allowed and c2 in allowed and c1 != c2 and row.get("r_numeric", "") not in ("", "NA"):
            out.add(canonical_pair(c1, c2))
    return out


def complete_case_ids(rows: list[dict[str, str]], constructs: list[str]) -> list[str]:
    required = {canonical_pair(a, b) for a, b in combinations(constructs, 2)}
    by_study: dict[str, set[str]] = {}
    allowed = set(constructs)
    for row in rows:
        sid = row.get("study_id", "")
        c1 = row.get("construct_1", "")
        c2 = row.get("construct_2", "")
        if sid and c1 in allowed and c2 in allowed and c1 != c2 and row.get("r_numeric", "") not in ("", "NA"):
            by_study.setdefault(sid, set()).add(canonical_pair(c1, c2))
    return sorted([sid for sid, pairs in by_study.items() if required.issubset(pairs)])


def main() -> None:
    rows, headers = read_csv(INPUT)
    if "analysis_set" not in headers:
        headers.append("analysis_set")
    if "analysis_role" not in headers:
        headers.append("analysis_role")
    if "submission_input_rule" not in headers:
        headers.append("submission_input_rule")

    clean_rows = []
    for row in rows:
        row = dict(row)
        row["analysis_set"] = "paper_a_source_clean_submission_input_20260614"
        row["analysis_role"] = "source-clean Paper A model-family MASEM submission input"
        row["submission_input_rule"] = (
            "S048 source correction included; S036/S102 ANX-TRU researcher-approved; "
            "S004 PKC->SE rejected; beta/path/HTMT/loading/theory-only evidence excluded from primary input"
        )
        clean_rows.append(row)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    ONEDRIVE_DIR.mkdir(parents=True, exist_ok=True)
    out_csv = OUT_DIR / "paper_a_source_clean_submission_input_20260614.csv"
    write_csv(out_csv, clean_rows, headers)

    route_rows = []
    for name, constructs in [
        ("full10_theory_target", FULL10),
        ("core7_att_mediation", CORE7),
        ("trust6_mechanism", TRUST6),
    ]:
        required = {canonical_pair(a, b) for a, b in combinations(constructs, 2)}
        obs = observed_pairs(clean_rows, constructs)
        complete = complete_case_ids(clean_rows, constructs)
        route_rows.append({
            "route": name,
            "constructs": ",".join(constructs),
            "required_pairs": str(len(required)),
            "observed_pairs": str(len(obs)),
            "missing_pairs": ";".join(sorted(required - obs)),
            "complete_case_count": str(len(complete)),
            "complete_case_ids": ";".join(complete),
        })
    coverage_csv = OUT_DIR / "paper_a_source_clean_submission_input_route_coverage_20260614.csv"
    write_csv(coverage_csv, route_rows, list(route_rows[0].keys()))

    report = OUT_DIR / "PAPER_A_SOURCE_CLEAN_SUBMISSION_INPUT_20260614.md"
    report.write_text(
        "\n".join([
            "# Paper A source-clean submission input",
            "",
            "Date: 2026-06-14",
            "",
            "## Input rule",
            "",
            "This layer is the Paper A source-clean input for the model-family MASEM submission run.",
            "It includes researcher-approved S036/S102 ANX-TRU promotions and the S048 source correction, while preserving the S004 PKC->SE rejection and excluding beta/path, HTMT, loading, and theory-only evidence from the primary input.",
            "",
            "It does not mutate raw coder workbooks, PDFs, or frozen Paper B reference files.",
            "",
            "## Route coverage",
            "",
            "| Route | Required pairs | Observed pairs | Missing pairs | Complete-case studies | Complete-case IDs |",
            "| --- | ---: | ---: | --- | ---: | --- |",
            *[
                f"| {r['route']} | {r['required_pairs']} | {r['observed_pairs']} | {r['missing_pairs'] or 'none'} | {r['complete_case_count']} | {r['complete_case_ids'] or 'none'} |"
                for r in route_rows
            ],
            "",
            "## Next action",
            "",
            "Use this input for the Paper A model-family MASEM submission run: core7 and trust6 are empirical primary model-family members; full10 remains the theory target/evidence map unless later estimable under a validated missing-data strategy.",
        ]) + "\n",
        encoding="utf-8",
    )

    for path in [out_csv, coverage_csv, report]:
        shutil.copy2(path, ONEDRIVE_DIR / path.name)

    print(f"input_rows={len(clean_rows)}")
    print(f"repo_out={OUT_DIR}")
    print(f"onedrive_out={ONEDRIVE_DIR}")
    for r in route_rows:
        print(f"{r['route']}: observed={r['observed_pairs']}/{r['required_pairs']} complete={r['complete_case_count']}")


if __name__ == "__main__":
    main()
