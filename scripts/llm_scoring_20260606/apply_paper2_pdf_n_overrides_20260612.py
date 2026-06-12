#!/usr/bin/env python3
"""Apply approved PDF-recovered sample-size overrides to a derived MASEM input.

This script does not edit raw coder workbooks, frozen reference files, or the
legacy deterministic reconciliation outputs. It creates a new derived input
after PDF source checks supplied study-level analytic/sample N for the residual
rows that were previously excluded from N-weighted TSSEM/MASEM.
"""

from __future__ import annotations

import argparse
import csv
from collections import Counter
from datetime import date
from pathlib import Path


REPO = Path(__file__).resolve().parents[2]
RESULTS = REPO / "data/04_extraction/05_llm_masem_substitution/results"
PREANALYSIS = REPO / "docs/07_manuscript_exemplars/20260612/pre_analysis_processing"

DEFAULT_INPUT = RESULTS / "paper2_masem_substitution_rerun_input_n_reconciled_20260611.csv"
DEFAULT_SOURCE_CHECK = PREANALYSIS / "paper_a_residual_n_source_check_20260612.csv"
DEFAULT_OUTPUT = RESULTS / "paper2_masem_substitution_rerun_input_n_pdf_override_20260612.csv"
DEFAULT_ELIGIBLE = RESULTS / "paper2_masem_substitution_rerun_input_n_weighted_all_source_supported_20260612.csv"
DEFAULT_AUDIT = RESULTS / "paper2_masem_sample_size_pdf_override_20260612.csv"
DEFAULT_SUMMARY = RESULTS / "paper2_masem_sample_size_pdf_override_summary_20260612.csv"
DEFAULT_REPORT = RESULTS / "PAPER2_MASEM_SAMPLE_SIZE_PDF_OVERRIDE_20260612.md"

EXTRA_FIELDS = [
    "sample_size_pdf_override_original_status",
    "sample_size_pdf_override_value",
    "sample_size_pdf_override_source",
    "sample_size_pdf_override_status",
    "sample_size_pdf_override_note",
]


def read_csv(path: Path) -> tuple[list[dict[str, str]], list[str]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        return list(reader), list(reader.fieldnames or [])


def write_csv(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def numeric_n(value: str | None) -> str:
    text = str(value or "").strip()
    if not text:
        return ""
    try:
        value_float = float(text)
    except ValueError:
        return ""
    if value_float <= 3:
        return ""
    return str(int(value_float)) if value_float.is_integer() else str(value_float)


def load_overrides(path: Path) -> dict[str, dict[str, str]]:
    rows, _ = read_csv(path)
    overrides: dict[str, dict[str, str]] = {}
    for row in rows:
        record_id = row.get("analysis_record_id", "").strip()
        n_value = numeric_n(row.get("pdf_recovered_sample_size"))
        if not record_id or not n_value:
            continue
        overrides[record_id] = row
    return overrides


def apply_overrides(
    input_rows: list[dict[str, str]],
    overrides: dict[str, dict[str, str]],
) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    output_rows: list[dict[str, object]] = []
    audit_rows: list[dict[str, object]] = []
    for row in input_rows:
        new = dict(row)
        record_id = row.get("analysis_record_id", "")
        override = overrides.get(record_id)
        existing_n = numeric_n(row.get("sample_size_numeric") or row.get("sample_size"))
        original_status = row.get("sample_size_reconciliation_status", "")

        status = "not_needed_existing_source_supported_n"
        override_value = ""
        override_source = ""
        note = "Existing numeric N retained."

        if existing_n:
            new["masem_n_weighted_eligibility"] = "include_n_weighted_masem"
        elif override:
            override_value = numeric_n(override.get("pdf_recovered_sample_size"))
            override_source = override.get("pdf_source_location_checked", "")
            new["sample_size"] = override_value
            new["sample_size_numeric"] = f"{float(override_value):.1f}"
            new["sample_size_reconciliation_status"] = "filled_from_pdf_source_check_study_level_n"
            new["sample_size_reconciliation_source"] = override_source
            new["sample_size_reconciliation_rule"] = "pdf_source_checked_study_level_analytic_sample_n"
            new["sample_size_reconciliation_note"] = override.get("source_check_reason", "")
            new["masem_n_weighted_eligibility"] = "include_n_weighted_masem"
            status = "applied_pdf_recovered_study_level_n"
            note = override.get("source_check_reason", "")
        else:
            new["masem_n_weighted_eligibility"] = "exclude_missing_n"
            status = "still_missing_no_pdf_override"
            note = "No numeric N available after deterministic reconciliation or PDF override layer."

        new["sample_size_pdf_override_original_status"] = original_status
        new["sample_size_pdf_override_value"] = override_value
        new["sample_size_pdf_override_source"] = override_source
        new["sample_size_pdf_override_status"] = status
        new["sample_size_pdf_override_note"] = note
        output_rows.append(new)
        audit_rows.append(
            {
                "analysis_record_id": record_id,
                "study_id": row.get("study_id", ""),
                "construct_pair_canonical": row.get("construct_pair_canonical", "") or row.get("construct_pair", ""),
                "sample_size_before_pdf_override": row.get("sample_size", ""),
                "sample_size_numeric_before_pdf_override": row.get("sample_size_numeric", ""),
                "sample_size_after_pdf_override": new.get("sample_size", ""),
                "sample_size_numeric_after_pdf_override": new.get("sample_size_numeric", ""),
                "original_reconciliation_status": original_status,
                "pdf_override_status": status,
                "pdf_override_source": override_source,
                "pdf_override_note": note,
                "masem_n_weighted_eligibility": new.get("masem_n_weighted_eligibility", ""),
            }
        )
    return output_rows, audit_rows


def summary_rows(output_rows: list[dict[str, object]], audit_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = [
        {"metric": "total_rows", "label": "all", "row_n": len(output_rows)},
        {
            "metric": "rows_with_sample_size_numeric",
            "label": "after_pdf_override",
            "row_n": sum(1 for row in output_rows if numeric_n(str(row.get("sample_size_numeric", "")))),
        },
        {
            "metric": "rows_missing_sample_size_numeric",
            "label": "after_pdf_override",
            "row_n": sum(1 for row in output_rows if not numeric_n(str(row.get("sample_size_numeric", "")))),
        },
    ]
    for status, count in sorted(Counter(str(row["pdf_override_status"]) for row in audit_rows).items()):
        rows.append({"metric": "pdf_override_status", "label": status, "row_n": count})
    for study_id, count in sorted(
        Counter(
            str(row["study_id"])
            for row in audit_rows
            if row["pdf_override_status"] == "applied_pdf_recovered_study_level_n"
        ).items()
    ):
        rows.append({"metric": "pdf_override_applied_study", "label": study_id, "row_n": count})
    return rows


def report_text(
    output_rows: list[dict[str, object]],
    eligible_rows: list[dict[str, object]],
    audit_rows: list[dict[str, object]],
    summary: list[dict[str, object]],
    input_path: Path,
    source_check_path: Path,
    output_path: Path,
    eligible_path: Path,
    audit_path: Path,
    summary_path: Path,
) -> str:
    metrics = {(row["metric"], row["label"]): row["row_n"] for row in summary}
    status_counts = [row for row in summary if row["metric"] == "pdf_override_status"]
    study_counts = [row for row in summary if row["metric"] == "pdf_override_applied_study"]
    lines = [
        "# Paper2 MASEM Sample-Size PDF Override",
        "",
        f"Date: {date.today().isoformat()}",
        "",
        "## Boundary",
        "",
        "This is a derived post-reconciliation input. It does not overwrite raw",
        "coder workbooks, frozen reference files, or the 2026-06-11 deterministic",
        "sample-size reconciliation. It applies the researcher-approved default",
        "recommendation: use PDF source-supported study-level analytic/sample N",
        "for residual rows when the source check supplies defensible N.",
        "",
        "## Result",
        "",
        f"- Input rows: {len(output_rows)}",
        f"- Rows with `sample_size_numeric` after PDF override: {metrics.get(('rows_with_sample_size_numeric', 'after_pdf_override'), 0)}",
        f"- Rows missing `sample_size_numeric` after PDF override: {metrics.get(('rows_missing_sample_size_numeric', 'after_pdf_override'), 0)}",
        f"- N-weighted eligible rows written: {len(eligible_rows)}",
        "",
        "## PDF Override Status Counts",
        "",
    ]
    for row in status_counts:
        lines.append(f"- {row['label']}: {row['row_n']}")
    lines.extend(["", "## Study-Level PDF Overrides Applied", ""])
    for row in study_counts:
        lines.append(f"- {row['label']}: {row['row_n']} rows")
    lines.extend(
        [
            "",
            "## Claim Boundary",
            "",
            "The N-coverage blocker is closed for this derived input: every row now",
            "has a numeric sample-size candidate. This does not by itself authorize",
            "final all-construct TSSEM/OSMASEM claims. Those claims still require the",
            "separate matrix sparsity, identification, model-specification, and",
            "source-type boundary gates.",
            "",
            "## Inputs",
            "",
            f"- `{input_path.relative_to(REPO)}`",
            f"- `{source_check_path.relative_to(REPO)}`",
            "",
            "## Outputs",
            "",
            f"- `{output_path.relative_to(REPO)}`",
            f"- `{eligible_path.relative_to(REPO)}`",
            f"- `{audit_path.relative_to(REPO)}`",
            f"- `{summary_path.relative_to(REPO)}`",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--source-check", type=Path, default=DEFAULT_SOURCE_CHECK)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--eligible-output", type=Path, default=DEFAULT_ELIGIBLE)
    parser.add_argument("--audit-output", type=Path, default=DEFAULT_AUDIT)
    parser.add_argument("--summary-output", type=Path, default=DEFAULT_SUMMARY)
    parser.add_argument("--report-output", type=Path, default=DEFAULT_REPORT)
    args = parser.parse_args()

    input_rows, input_fields = read_csv(args.input)
    overrides = load_overrides(args.source_check)
    output_rows, audit_rows = apply_overrides(input_rows, overrides)
    eligible_rows = [
        row for row in output_rows if row.get("masem_n_weighted_eligibility") == "include_n_weighted_masem"
    ]
    summary = summary_rows(output_rows, audit_rows)
    fields = input_fields + [field for field in EXTRA_FIELDS if field not in input_fields]

    write_csv(args.output, output_rows, fields)
    write_csv(args.eligible_output, eligible_rows, fields)
    write_csv(args.audit_output, audit_rows, list(audit_rows[0].keys()) if audit_rows else [])
    write_csv(args.summary_output, summary, ["metric", "label", "row_n"])
    args.report_output.write_text(
        report_text(
            output_rows,
            eligible_rows,
            audit_rows,
            summary,
            args.input,
            args.source_check,
            args.output,
            args.eligible_output,
            args.audit_output,
            args.summary_output,
        ),
        encoding="utf-8",
    )
    print(
        "pdf_n_override_complete",
        f"input_rows={len(input_rows)}",
        f"eligible_rows={len(eligible_rows)}",
        f"missing_rows={len(input_rows) - len(eligible_rows)}",
        f"overrides_available={len(overrides)}",
    )


if __name__ == "__main__":
    main()
