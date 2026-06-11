#!/usr/bin/env python3
"""Prepare share-safe materialization batches for source PDFs that failed rendering."""

from __future__ import annotations

import argparse
import csv
import hashlib
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


REPO = Path(__file__).resolve().parents[2]
PAPER_C = REPO / "data/04_extraction/07_paper_c_harness_benchmark"
DEFAULT_COVERAGE_MANIFEST = PAPER_C / "00_manifest/source_rendering_full_coverage_manifest_20260609.csv"
DEFAULT_GAP_OUTPUT = PAPER_C / "00_manifest/source_pdf_materialization_gap_manifest_20260609.csv"
DEFAULT_BATCH_OUTPUT = PAPER_C / "06_rerun_bundles/source_pdf_materialization_batches_20260609.csv"
DEFAULT_STATUS_OUTPUT = PAPER_C / "00_manifest/SOURCE_PDF_MATERIALIZATION_PLAN_20260609.md"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def is_rendered(row: dict[str, str]) -> bool:
    return row.get("private_packet_ref") == "local_private_packet_not_committed"


def failure_mode(row: dict[str, str]) -> str:
    notes = row.get("notes", "")
    if "Operation timed out" in notes:
        return "onedrive_read_timeout"
    if "No extractable text" in notes:
        return "no_extractable_text"
    return row.get("status", "unknown_failure")


def split_families(value: str) -> list[str]:
    return [item for item in value.split(";") if item]


def build_gap_rows(rows: list[dict[str, str]], batch_size: int, batch_prefix: str) -> list[dict[str, str]]:
    failed = [row for row in rows if not is_rendered(row)]
    failed.sort(key=lambda row: (-int(row["target_task_count"]), row["study_id"]))

    gap_rows: list[dict[str, str]] = []
    for index, row in enumerate(failed, start=1):
        batch_number = ((index - 1) // batch_size) + 1
        pdf_count = int(row.get("available_source_pdf_count") or 0)
        gap_rows.append(
            {
                "batch_id": f"{batch_prefix}-{batch_number:02d}",
                "batch_order": str(batch_number),
                "priority_rank": str(index),
                "study_id": row["study_id"],
                "target_task_count": row["target_task_count"],
                "denominator_families": row["denominator_families"],
                "archive_filename_coverage_status": "filename_match_present" if pdf_count else "no_filename_match",
                "available_source_pdf_count": row.get("available_source_pdf_count", "0"),
                "previous_render_status": row.get("status", ""),
                "failure_mode": failure_mode(row),
                "materialization_needed": "true",
                "post_materialization_check": "run check_source_pdf_materialization.py, then rerun build_source_rendering_packets.py full coverage audit",
                "notes": "Share-safe study-level materialization request; no PDF path, source text, human value, or human adjudication locator is included.",
            }
        )
    return gap_rows


def build_batch_rows(gap_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    batches: dict[str, list[dict[str, str]]] = {}
    for row in gap_rows:
        batches.setdefault(row["batch_id"], []).append(row)

    batch_rows: list[dict[str, str]] = []
    for batch_id in sorted(batches, key=lambda item: int(item.rsplit("-", 1)[1])):
        rows = batches[batch_id]
        family_studies = Counter()
        family_tasks = Counter()
        for row in rows:
            for family in split_families(row["denominator_families"]):
                family_studies[family] += 1
                family_tasks[family] += int(row["target_task_count"])
        batch_rows.append(
            {
                "batch_id": batch_id,
                "batch_order": rows[0]["batch_order"],
                "study_count": str(len(rows)),
                "target_task_count": str(sum(int(row["target_task_count"]) for row in rows)),
                "study_ids": ";".join(row["study_id"] for row in rows),
                "family_study_counts": ";".join(f"{family}={count}" for family, count in sorted(family_studies.items())),
                "family_task_counts": ";".join(f"{family}={count}" for family, count in sorted(family_tasks.items())),
                "recommended_action": "Materialize these study PDFs locally, then run the materialization checker for this batch.",
            }
        )
    return batch_rows


def write_status(
    path: Path,
    source_rows: list[dict[str, str]],
    gap_rows: list[dict[str, str]],
    batch_rows: list[dict[str, str]],
    gap_output: Path,
    batch_output: Path,
) -> None:
    rendered_rows = [row for row in source_rows if is_rendered(row)]
    failed_rows = [row for row in source_rows if not is_rendered(row)]
    failure_counts = Counter(row["failure_mode"] for row in gap_rows)
    family_studies = Counter()
    family_tasks = Counter()
    for row in gap_rows:
        for family in split_families(row["denominator_families"]):
            family_studies[family] += 1
            family_tasks[family] += int(row["target_task_count"])

    lines = [
        "# Source PDF Materialization Plan",
        "",
        "Date: 2026-06-09",
        "",
        "Status: materialization action package prepared. This artifact does not authorize any additional model run or any smaller-scope result claim.",
        "",
        "## Scope",
        "",
        f"- Target studies in source rendering coverage manifest: {len(source_rows)}",
        f"- Studies already source-rendered into private packets: {len(rendered_rows)}",
        f"- Studies requiring local PDF materialization/readability resolution: {len(failed_rows)}",
        f"- Target rows already source-rendered: {sum(int(row['target_task_count']) for row in rendered_rows)}",
        f"- Target rows still blocked by materialization/readability: {sum(int(row['target_task_count']) for row in failed_rows)}",
        f"- Materialization batches prepared: {len(batch_rows)}",
        "",
        "## Failure Mode Counts",
        "",
    ]
    for mode, count in sorted(failure_counts.items()):
        lines.append(f"- `{mode}`: {count}")
    lines.extend(["", "## Blocked Rows by Denominator Family", ""])
    for family in sorted(family_tasks):
        lines.append(f"- `{family}`: {family_studies[family]} studies / {family_tasks[family]} target rows")
    lines.extend(
        [
            "",
            "## Prepared Artifacts",
            "",
            f"- `{gap_output.relative_to(REPO)}`: study-level materialization gap manifest, prioritized by target-row burden.",
            f"- `{batch_output.relative_to(REPO)}`: batch-level materialization worklist.",
            "- `scripts/llm_scoring_20260606/check_source_pdf_materialization.py`: share-safe local readability checker for hydrated PDFs.",
            "",
            "## Procedure Boundary",
            "",
            "- The archive has study-ID filename coverage for the full 194-study target shell, but filename coverage is not enough for source-rendered model prompts.",
            "- The current blocker is local OneDrive materialization/readability: most files time out when a PDF reader attempts to open them.",
            "- Do not run full-corpus `M1-R`, `M1-P`, `M2-R`, or optional `M3-R` until materialization checks and source-rendering coverage are clean for the intended target scope.",
            "- Do not use human reference values, human adjudication rationales, or human-adjudicated source locators to make model prompts.",
            "- Keep PDFs, rendered source packets, and raw model transcripts out of Git.",
            "",
            "## Next Gate",
            "",
            "After the OneDrive PDFs are locally materialized, run the checker on the relevant batch or full gap manifest. Then rerun the source-rendering coverage audit. A balanced source-rendered smoke is only eligible after rendered private packets cover the intended scope.",
            "",
            "## Integrity",
            "",
            f"- `{gap_output.name}` sha256: `{sha256(gap_output)}`",
            f"- `{batch_output.name}` sha256: `{sha256(batch_output)}`",
            f"- Generated at UTC: `{datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')}`",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--coverage-manifest", type=Path, default=DEFAULT_COVERAGE_MANIFEST)
    parser.add_argument("--gap-output", type=Path, default=DEFAULT_GAP_OUTPUT)
    parser.add_argument("--batch-output", type=Path, default=DEFAULT_BATCH_OUTPUT)
    parser.add_argument("--status-output", type=Path, default=DEFAULT_STATUS_OUTPUT)
    parser.add_argument("--batch-size", type=int, default=20)
    parser.add_argument("--batch-prefix", default="PDFMAT-20260609")
    args = parser.parse_args()

    rows = read_csv(args.coverage_manifest)
    gap_rows = build_gap_rows(rows, args.batch_size, args.batch_prefix)
    batch_rows = build_batch_rows(gap_rows)

    gap_fields = [
        "batch_id",
        "batch_order",
        "priority_rank",
        "study_id",
        "target_task_count",
        "denominator_families",
        "archive_filename_coverage_status",
        "available_source_pdf_count",
        "previous_render_status",
        "failure_mode",
        "materialization_needed",
        "post_materialization_check",
        "notes",
    ]
    batch_fields = [
        "batch_id",
        "batch_order",
        "study_count",
        "target_task_count",
        "study_ids",
        "family_study_counts",
        "family_task_counts",
        "recommended_action",
    ]
    write_csv(args.gap_output, gap_rows, gap_fields)
    write_csv(args.batch_output, batch_rows, batch_fields)
    write_status(args.status_output, rows, gap_rows, batch_rows, args.gap_output, args.batch_output)
    print(
        {
            "gap_studies": len(gap_rows),
            "gap_target_rows": sum(int(row["target_task_count"]) for row in gap_rows),
            "batches": len(batch_rows),
        }
    )


if __name__ == "__main__":
    main()
