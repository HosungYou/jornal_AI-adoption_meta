#!/usr/bin/env python3
"""Audit Paper2/Paper A MASEM matrix coverage after sample-size completion."""

from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from datetime import date
from itertools import combinations
from pathlib import Path


REPO = Path(__file__).resolve().parents[2]
RESULTS = REPO / "data/04_extraction/05_llm_masem_substitution/results"
DEFAULT_INPUT = RESULTS / "paper2_masem_substitution_rerun_input_n_pdf_override_20260612.csv"
DEFAULT_PAIR_AUDIT = RESULTS / "paper2_masem_matrix_pair_coverage_after_n_override_20260612.csv"
DEFAULT_STUDY_SET_AUDIT = RESULTS / "paper2_masem_matrix_construct_set_completeness_20260612.csv"
DEFAULT_STUDY_PAIR_AUDIT = RESULTS / "paper2_masem_matrix_study_pair_coverage_20260612.csv"
DEFAULT_REPORT = RESULTS / "PAPER2_MASEM_MATRIX_IDENTIFICATION_AUDIT_20260612.md"

TARGET_10 = ["PE", "EE", "SI", "FC", "ATT", "SE", "TRU", "ANX", "BI", "UB"]
CONSTRUCT_SETS = {
    "core6_legacy_tssem_diagnostic": ["PE", "EE", "SI", "FC", "BI", "UB"],
    "core7_add_att": ["PE", "EE", "SI", "FC", "ATT", "BI", "UB"],
    "core8_add_tru": ["PE", "EE", "SI", "FC", "ATT", "TRU", "BI", "UB"],
    "core9_add_anx": ["PE", "EE", "SI", "FC", "ATT", "TRU", "ANX", "BI", "UB"],
    "theory_target_10": TARGET_10,
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def parse_float(value: str | None) -> float | None:
    text = str(value or "").strip()
    if not text:
        return None
    try:
        return float(text)
    except ValueError:
        return None


def pair(c1: str, c2: str) -> str:
    return "-".join(sorted([c1, c2]))


def row_pair(row: dict[str, str]) -> str:
    c1 = row.get("construct_1", "").strip()
    c2 = row.get("construct_2", "").strip()
    if c1 and c2:
        return pair(c1, c2)
    parts = [
        part.strip()
        for part in (row.get("construct_pair_canonical") or row.get("construct_pair") or "").replace("_", "-").split("-")
        if part.strip()
    ]
    if len(parts) == 2:
        return pair(parts[0], parts[1])
    return ""


def expected_pairs(constructs: list[str]) -> list[str]:
    return sorted(pair(c1, c2) for c1, c2 in combinations(constructs, 2))


def md_table(rows: list[dict[str, object]], cols: list[str]) -> str:
    lines = ["| " + " | ".join(cols) + " |", "| " + " | ".join(["---"] * len(cols)) + " |"]
    for row in rows:
        lines.append("| " + " | ".join(str(row.get(col, "")) for col in cols) + " |")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--pair-audit-output", type=Path, default=DEFAULT_PAIR_AUDIT)
    parser.add_argument("--study-set-output", type=Path, default=DEFAULT_STUDY_SET_AUDIT)
    parser.add_argument("--study-pair-output", type=Path, default=DEFAULT_STUDY_PAIR_AUDIT)
    parser.add_argument("--report-output", type=Path, default=DEFAULT_REPORT)
    args = parser.parse_args()

    rows = []
    for row in read_csv(args.input):
        r_value = parse_float(row.get("r_numeric"))
        n_value = parse_float(row.get("sample_size_numeric"))
        c1 = row.get("construct_1", "").strip()
        c2 = row.get("construct_2", "").strip()
        if c1 in TARGET_10 and c2 in TARGET_10 and r_value is not None and abs(r_value) <= 1:
            new = dict(row)
            new["_pair"] = row_pair(row)
            new["_has_n"] = n_value is not None and n_value > 3
            rows.append(new)

    by_pair: dict[str, list[dict[str, object]]] = defaultdict(list)
    by_study: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        by_pair[str(row["_pair"])].append(row)
        by_study[row.get("study_id", "")].append(row)

    pair_rows: list[dict[str, object]] = []
    for expected_pair in expected_pairs(TARGET_10):
        group = by_pair.get(expected_pair, [])
        n_ready = [row for row in group if row["_has_n"]]
        pair_rows.append(
            {
                "construct_pair": expected_pair,
                "rows": len(group),
                "studies": len({row.get("study_id", "") for row in group}),
                "rows_with_numeric_n": len(n_ready),
                "studies_with_numeric_n": len({row.get("study_id", "") for row in n_ready}),
                "gate_status": (
                    "no_effect_rows"
                    if not group
                    else "n_ready_pairwise"
                    if len(n_ready) == len(group)
                    else "n_incomplete"
                ),
            }
        )

    study_pair_rows: list[dict[str, object]] = []
    for study_id, group in sorted(by_study.items()):
        observed_pairs = {str(row["_pair"]) for row in group}
        n_ready_pairs = {str(row["_pair"]) for row in group if row["_has_n"]}
        study_pair_rows.append(
            {
                "study_id": study_id,
                "rows": len(group),
                "construct_pairs": len(observed_pairs),
                "n_ready_construct_pairs": len(n_ready_pairs),
                "pairs": ";".join(sorted(observed_pairs)),
                "n_ready_pairs": ";".join(sorted(n_ready_pairs)),
            }
        )

    set_rows: list[dict[str, object]] = []
    for set_name, constructs in CONSTRUCT_SETS.items():
        pairs_needed = set(expected_pairs(constructs))
        complete_studies = [
            study_id
            for study_id, group in sorted(by_study.items())
            if pairs_needed <= {str(row["_pair"]) for row in group if row["_has_n"]}
        ]
        pair_counts = [
            len({row.get("study_id", "") for row in by_pair.get(pair_id, []) if row["_has_n"]})
            for pair_id in pairs_needed
        ]
        missing_pairs = sorted(pair_id for pair_id in pairs_needed if not by_pair.get(pair_id))
        set_rows.append(
            {
                "construct_set": set_name,
                "constructs": ";".join(constructs),
                "construct_count": len(constructs),
                "required_pairs": len(pairs_needed),
                "covered_pairs": len([pair_id for pair_id in pairs_needed if by_pair.get(pair_id)]),
                "missing_pairs": ";".join(missing_pairs),
                "min_pair_study_count": min(pair_counts) if pair_counts else 0,
                "complete_case_studies": len(complete_studies),
                "complete_case_study_ids": ";".join(complete_studies),
                "identification_gate": (
                    "eligible_for_bounded_tssem_diagnostic"
                    if complete_studies and not missing_pairs
                    else "not_identified_as_complete_case_model"
                ),
            }
        )

    write_csv(
        args.pair_audit_output,
        pair_rows,
        ["construct_pair", "rows", "studies", "rows_with_numeric_n", "studies_with_numeric_n", "gate_status"],
    )
    write_csv(
        args.study_set_output,
        set_rows,
        [
            "construct_set",
            "constructs",
            "construct_count",
            "required_pairs",
            "covered_pairs",
            "missing_pairs",
            "min_pair_study_count",
            "complete_case_studies",
            "complete_case_study_ids",
            "identification_gate",
        ],
    )
    write_csv(
        args.study_pair_output,
        study_pair_rows,
        ["study_id", "rows", "construct_pairs", "n_ready_construct_pairs", "pairs", "n_ready_pairs"],
    )

    weakest = sorted(pair_rows, key=lambda row: (int(row["studies_with_numeric_n"]), row["construct_pair"]))[:12]
    status_counts = Counter(str(row["identification_gate"]) for row in set_rows)
    recommended = next(row for row in set_rows if row["construct_set"] == "core6_legacy_tssem_diagnostic")
    full10 = next(row for row in set_rows if row["construct_set"] == "theory_target_10")
    lines = [
        "# Paper2/Paper A MASEM Matrix Identification Audit",
        "",
        f"Date: {date.today().isoformat()}",
        "",
        "## Boundary",
        "",
        "This audit is run after PDF-recovered N completion. It checks matrix",
        "coverage and complete-case identification only; it does not estimate final",
        "TSSEM/OSMASEM paths or authorize substantive SEM claims.",
        "",
        "## Result",
        "",
        f"- Input rows audited: {len(rows)}",
        f"- Studies represented: {len(by_study)}",
        f"- Target construct-pair coverage: {sum(1 for row in pair_rows if row['rows'])}/45",
        f"- Rows with numeric N: {sum(1 for row in rows if row['_has_n'])}/{len(rows)}",
        f"- Core-6 complete-case studies: {recommended['complete_case_studies']}",
        f"- Full 10-construct complete-case studies: {full10['complete_case_studies']}",
        f"- Full 10 missing pairs: {full10['missing_pairs'] or 'none'}",
        "",
        "## Construct-Set Identification Gates",
        "",
        md_table(
            set_rows,
            [
                "construct_set",
                "construct_count",
                "required_pairs",
                "covered_pairs",
                "missing_pairs",
                "complete_case_studies",
                "identification_gate",
            ],
        ),
        "",
        "## Weakest Pair Coverage",
        "",
        md_table(weakest, ["construct_pair", "rows", "studies", "studies_with_numeric_n", "gate_status"]),
        "",
        "## Gate Interpretation",
        "",
        "- N coverage is complete in this derived input.",
        "- The theory target still lacks `ANX-TRU` in the legacy primary direct-r matrix.",
        "- The bounded core-6 set remains the defensible immediate TSSEM diagnostic lane.",
        "- Full 10-construct claims require resolving the ANX-TRU corpus/source-type boundary or explicitly reducing the model.",
        "",
        "## Outputs",
        "",
        f"- `{args.pair_audit_output.relative_to(REPO)}`",
        f"- `{args.study_set_output.relative_to(REPO)}`",
        f"- `{args.study_pair_output.relative_to(REPO)}`",
    ]
    args.report_output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(
        "matrix_identification_audit_complete",
        f"rows={len(rows)}",
        f"studies={len(by_study)}",
        f"core6_complete={recommended['complete_case_studies']}",
        f"full10_complete={full10['complete_case_studies']}",
    )


if __name__ == "__main__":
    main()
