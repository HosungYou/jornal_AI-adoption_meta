#!/usr/bin/env python3
"""Reconcile Paper2 MASEM rerun sample sizes from the frozen reference."""

from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path


REPO = Path(__file__).resolve().parents[2]
DATE_TAG = "20260611"
STEP5_RESULTS = REPO / "data/04_extraction/05_llm_masem_substitution/results"
DEFAULT_INPUT = STEP5_RESULTS / f"paper2_masem_substitution_rerun_input_{DATE_TAG}.csv"
DEFAULT_REFERENCE = (
    REPO
    / "data/04_extraction/04_reference_standard_freeze/full_corpus_reference_standard_frozen_20260609.csv"
)
DEFAULT_RECONCILED = STEP5_RESULTS / f"paper2_masem_substitution_rerun_input_n_reconciled_{DATE_TAG}.csv"
DEFAULT_ELIGIBLE = STEP5_RESULTS / f"paper2_masem_substitution_rerun_input_n_weighted_eligible_{DATE_TAG}.csv"
DEFAULT_AUDIT = STEP5_RESULTS / f"paper2_masem_sample_size_reconciliation_{DATE_TAG}.csv"
DEFAULT_SUMMARY = STEP5_RESULTS / f"paper2_masem_sample_size_reconciliation_summary_{DATE_TAG}.csv"
DEFAULT_REPORT = STEP5_RESULTS / f"PAPER2_MASEM_SAMPLE_SIZE_RECONCILIATION_{DATE_TAG}.md"

EXTRA_FIELDS = [
    "sample_size_original",
    "sample_size_numeric_original",
    "sample_size_reconciliation_status",
    "sample_size_reconciliation_source",
    "sample_size_reconciliation_rule",
    "sample_size_reconciliation_note",
    "masem_n_weighted_eligibility",
]


def read_csv(path: Path) -> tuple[list[dict[str, str]], list[str]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        return list(reader), list(reader.fieldnames or [])


def write_csv(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def fmt_n(value: str) -> tuple[str, str]:
    text = str(value).strip()
    if not text:
        return "", ""
    try:
        numeric = float(text)
    except ValueError:
        return text, text
    if numeric.is_integer():
        return str(int(numeric)), f"{numeric:.1f}"
    return str(numeric), str(numeric)


def numeric_n(value: str) -> str:
    text = str(value).strip()
    if not text:
        return ""
    try:
        numeric = float(text)
    except ValueError:
        return ""
    if numeric <= 3:
        return ""
    return str(int(numeric)) if numeric.is_integer() else str(numeric)


def canonical_pair(row: dict[str, str]) -> str:
    c1 = row.get("construct_1", "").strip()
    c2 = row.get("construct_2", "").strip()
    if c1 and c2:
        return "-".join(sorted([c1, c2]))
    pair = row.get("construct_pair_canonical") or row.get("construct_pair") or row.get("pair") or ""
    parts = [part.strip() for part in pair.replace("_", "-").split("-") if part.strip()]
    return "-".join(sorted(parts)) if len(parts) == 2 else pair


def ref_index(reference_rows: list[dict[str, str]]) -> tuple[dict[tuple[str, str], list[dict[str, str]]], dict[str, set[str]]]:
    by_study_pair: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    by_study_n: dict[str, set[str]] = defaultdict(set)
    for row in reference_rows:
        n = numeric_n(row.get("n", ""))
        if not n:
            continue
        study_id = row.get("study_id", "")
        by_study_pair[(study_id, canonical_pair(row))].append(row)
        by_study_n[study_id].add(n)
    return by_study_pair, by_study_n


def single_n(candidates: list[dict[str, str]]) -> tuple[str, list[dict[str, str]]]:
    n_values = sorted({numeric_n(row.get("n", "")) for row in candidates if numeric_n(row.get("n", ""))})
    if len(n_values) == 1:
        return n_values[0], candidates
    return "", candidates


def s121_stratum_candidates(
    row: dict[str, str],
    by_study_pair: dict[tuple[str, str], list[dict[str, str]]],
) -> list[dict[str, str]]:
    study_id = row.get("study_id", "")
    if study_id == "S121-1":
        stratum = "students"
    elif study_id == "S121-2":
        stratum = "teachers"
    else:
        return []
    locator = " ".join(
        [
            row.get("source_location", ""),
            row.get("source_locator", ""),
            row.get("notes", ""),
        ]
    ).lower()
    if "student" in locator:
        stratum = "students"
    elif "teacher" in locator:
        stratum = "teachers"
    return [
        candidate
        for candidate in by_study_pair.get(("S121", canonical_pair(row)), [])
        if candidate.get("sample_or_stratum") == stratum
    ]


def apply_reconciliation(
    input_rows: list[dict[str, str]],
    reference_rows: list[dict[str, str]],
) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    by_study_pair, by_study_n = ref_index(reference_rows)
    reconciled: list[dict[str, object]] = []
    audit_rows: list[dict[str, object]] = []

    for row in input_rows:
        new = dict(row)
        original_sample = row.get("sample_size", "")
        original_numeric = row.get("sample_size_numeric", "")
        new["sample_size_original"] = original_sample
        new["sample_size_numeric_original"] = original_numeric

        status = "missing_n_excluded_from_n_weighted_masem"
        source = ""
        rule = "exclude_missing_n_from_n_weighted_tssem"
        note = "No source-supported N found in the frozen full-corpus reference."
        n_value = str(original_numeric or original_sample).strip()

        if n_value:
            status = "retained_existing_input_n"
            source = row.get("source_decision_id", "") or row.get("analysis_record_id", "")
            rule = "preserve_existing_sample_size"
            note = "Existing rerun-input sample size retained; no raw workbook overwrite."
        else:
            key = (row.get("study_id", ""), canonical_pair(row))
            candidates = by_study_pair.get(key, [])
            n_value, source_candidates = single_n(candidates)
            if n_value:
                status = "filled_from_full_corpus_reference_pair"
                source = ";".join(sorted({c.get("reference_record_id", "") for c in source_candidates if c.get("reference_record_id", "")})[:3])
                rule = "study_pair_single_n_from_frozen_reference"
                note = "Filled from study+construct-pair match in the 2026-06-09 frozen full-corpus reference."
            else:
                candidates = s121_stratum_candidates(row, by_study_pair)
                n_value, source_candidates = single_n(candidates)
                if n_value:
                    status = "filled_from_s121_stratum_reference"
                    source = ";".join(sorted({c.get("reference_record_id", "") for c in source_candidates if c.get("reference_record_id", "")})[:3])
                    rule = "s121_student_teacher_stratum_from_source_location"
                    note = "Filled from S121 student/teacher source-location mapping in the frozen full-corpus reference."
                else:
                    study_values = sorted(by_study_n.get(row.get("study_id", ""), set()))
                    if len(study_values) == 1:
                        n_value = study_values[0]
                        status = "filled_from_full_corpus_reference_study_unique"
                        source = row.get("study_id", "")
                        rule = "study_single_n_from_frozen_reference"
                        note = "Filled from unique study-level N in the 2026-06-09 frozen full-corpus reference."

        sample, numeric = fmt_n(n_value)
        if sample and status != "missing_n_excluded_from_n_weighted_masem":
            new["sample_size"] = sample
            new["sample_size_numeric"] = numeric
            eligibility = "include_n_weighted_masem"
        else:
            eligibility = "exclude_missing_n"

        new["sample_size_reconciliation_status"] = status
        new["sample_size_reconciliation_source"] = source
        new["sample_size_reconciliation_rule"] = rule
        new["sample_size_reconciliation_note"] = note
        new["masem_n_weighted_eligibility"] = eligibility
        reconciled.append(new)

        audit_rows.append(
            {
                "analysis_record_id": row.get("analysis_record_id", ""),
                "study_id": row.get("study_id", ""),
                "construct_pair_canonical": canonical_pair(row),
                "sample_size_original": original_sample,
                "sample_size_numeric_original": original_numeric,
                "sample_size_reconciled": new.get("sample_size", ""),
                "sample_size_numeric_reconciled": new.get("sample_size_numeric", ""),
                "sample_size_reconciliation_status": status,
                "sample_size_reconciliation_source": source,
                "sample_size_reconciliation_rule": rule,
                "masem_n_weighted_eligibility": eligibility,
            }
        )
    return reconciled, audit_rows


def summary_rows(reconciled: list[dict[str, object]], audit_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    rows.append({"metric": "total_rows", "label": "all", "row_n": len(reconciled)})
    rows.append(
        {
            "metric": "rows_with_sample_size_numeric",
            "label": "after_reconciliation",
            "row_n": sum(1 for row in reconciled if str(row.get("sample_size_numeric", "")).strip()),
        }
    )
    rows.append(
        {
            "metric": "rows_missing_sample_size_numeric",
            "label": "after_reconciliation",
            "row_n": sum(1 for row in reconciled if not str(row.get("sample_size_numeric", "")).strip()),
        }
    )
    for status, count in sorted(Counter(str(row["sample_size_reconciliation_status"]) for row in audit_rows).items()):
        rows.append({"metric": "sample_size_reconciliation_status", "label": status, "row_n": count})
    for study_id, count in sorted(
        Counter(
            str(row["study_id"])
            for row in audit_rows
            if row["sample_size_reconciliation_status"] == "missing_n_excluded_from_n_weighted_masem"
        ).items()
    ):
        rows.append({"metric": "missing_n_excluded_study", "label": study_id, "row_n": count})
    return rows


def report_text(summary: list[dict[str, object]], audit_rows: list[dict[str, object]], eligible_rows: list[dict[str, object]]) -> str:
    metrics = {(row["metric"], row["label"]): row["row_n"] for row in summary}
    status_counts = [
        row
        for row in summary
        if row["metric"] == "sample_size_reconciliation_status"
    ]
    missing = [
        row
        for row in summary
        if row["metric"] == "missing_n_excluded_study"
    ]
    lines = [
        "# Paper2 MASEM Sample-Size Reconciliation",
        "",
        "Date: 2026-06-11",
        "",
        "## Boundary",
        "",
        "This reconciliation does not overwrite raw coder workbooks or the frozen",
        "human reference standard. It creates a derived MASEM rerun input that",
        "copies source-supported `n` values from the 2026-06-09 frozen full-corpus",
        "reference where the mapping is deterministic.",
        "",
        "## Result",
        "",
        f"- Input rows: {metrics.get(('total_rows', 'all'), 0)}",
        f"- Rows with `sample_size_numeric` after reconciliation: {metrics.get(('rows_with_sample_size_numeric', 'after_reconciliation'), 0)}",
        f"- Rows missing `sample_size_numeric` after reconciliation: {metrics.get(('rows_missing_sample_size_numeric', 'after_reconciliation'), 0)}",
        f"- N-weighted eligible rows written: {len(eligible_rows)}",
        "",
        "## Reconciliation Status Counts",
        "",
    ]
    for row in status_counts:
        lines.append(f"- {row['label']}: {row['row_n']}")
    lines.extend(["", "## Missing-N Exclusion Rule", ""])
    lines.append(
        "Rows that still lack source-supported `sample_size_numeric` after this "
        "deterministic merge are excluded from N-weighted TSSEM/MASEM weighting "
        "until a later PDF-level source check supplies N. They may still be used "
        "for unweighted descriptive or audit-only sensitivity summaries when "
        "clearly labeled."
    )
    if missing:
        lines.extend(["", "## Remaining Missing-N Studies", ""])
        for row in missing:
            lines.append(f"- {row['label']}: {row['row_n']} rows")
    lines.extend(
        [
            "",
            "## Outputs",
            "",
            f"- `{DEFAULT_RECONCILED.relative_to(REPO)}`",
            f"- `{DEFAULT_ELIGIBLE.relative_to(REPO)}`",
            f"- `{DEFAULT_AUDIT.relative_to(REPO)}`",
            f"- `{DEFAULT_SUMMARY.relative_to(REPO)}`",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--reference", type=Path, default=DEFAULT_REFERENCE)
    parser.add_argument("--reconciled-output", type=Path, default=DEFAULT_RECONCILED)
    parser.add_argument("--eligible-output", type=Path, default=DEFAULT_ELIGIBLE)
    parser.add_argument("--audit-output", type=Path, default=DEFAULT_AUDIT)
    parser.add_argument("--summary-output", type=Path, default=DEFAULT_SUMMARY)
    parser.add_argument("--report-output", type=Path, default=DEFAULT_REPORT)
    args = parser.parse_args()

    input_rows, input_fields = read_csv(args.input)
    reference_rows, _ = read_csv(args.reference)
    reconciled, audit_rows = apply_reconciliation(input_rows, reference_rows)
    eligible_rows = [
        row
        for row in reconciled
        if row.get("masem_n_weighted_eligibility") == "include_n_weighted_masem"
    ]
    fields = input_fields + [field for field in EXTRA_FIELDS if field not in input_fields]
    summary = summary_rows(reconciled, audit_rows)

    write_csv(args.reconciled_output, reconciled, fields)
    write_csv(args.eligible_output, eligible_rows, fields)
    write_csv(args.audit_output, audit_rows, list(audit_rows[0].keys()) if audit_rows else [])
    write_csv(args.summary_output, summary, ["metric", "label", "row_n"])
    args.report_output.write_text(report_text(summary, audit_rows, eligible_rows), encoding="utf-8")
    print(
        "sample_size_reconciliation_complete",
        f"input_rows={len(input_rows)}",
        f"eligible_rows={len(eligible_rows)}",
        f"missing_rows={len(input_rows) - len(eligible_rows)}",
    )


if __name__ == "__main__":
    main()
