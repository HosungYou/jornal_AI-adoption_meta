#!/usr/bin/env python3
"""Check local source PDF materialization without writing PDF paths or source text."""

from __future__ import annotations

import argparse
import csv
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


REPO = Path(__file__).resolve().parents[2]
PROJECT_DOCS_ROOT = REPO.parents[1]
PAPER_C = REPO / "data/04_extraction/07_paper_c_harness_benchmark"
DEFAULT_GAP_MANIFEST = PAPER_C / "00_manifest/source_pdf_materialization_gap_manifest_20260609.csv"
DEFAULT_OUTPUT = PAPER_C / "00_manifest/source_pdf_materialization_check_20260609.csv"
DEFAULT_SOURCE_PDF_DIRS = [
    REPO / "data/04_extraction/03_source_document_adjudication/source_pdfs",
    PROJECT_DOCS_ROOT / "Meta/AI Adoption/PDFs",
    PROJECT_DOCS_ROOT / "Meta/AI Adoption/R1/PDFs",
    PROJECT_DOCS_ROOT / "Meta/AI Adoption/R2/PDFs",
    PROJECT_DOCS_ROOT / "Meta/AI Adoption/R3/PDFs",
    PROJECT_DOCS_ROOT / "Meta/AI Adoption/R4/PDFs",
    PROJECT_DOCS_ROOT / "Meta/source_pdfs/table36_62",
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def find_pdfs_for_study(study_id: str, source_pdf_dirs: list[Path], include_supplements: bool) -> list[Path]:
    selected: list[Path] = []
    seen: set[Path] = set()
    for source_pdf_dir in source_pdf_dirs:
        exact = source_pdf_dir / f"{study_id}.pdf"
        if exact.exists():
            selected.append(exact)
            seen.add(exact.resolve())
            break
    if not selected:
        for source_pdf_dir in source_pdf_dirs:
            matches = sorted(source_pdf_dir.glob(f"{study_id}*.pdf"))
            if matches:
                selected.append(matches[0])
                seen.add(matches[0].resolve())
                break
    if include_supplements:
        for source_pdf_dir in source_pdf_dirs:
            for supplement in sorted(source_pdf_dir.glob(f"{study_id}_*.pdf")):
                resolved = supplement.resolve()
                if resolved not in seen:
                    selected.append(supplement)
                    seen.add(resolved)
    return selected


def magic_probe(path: Path, timeout: int) -> tuple[str, int, bool, str]:
    code = (
        "from pathlib import Path\n"
        "import sys\n"
        "p = Path(sys.argv[1])\n"
        "data = p.open('rb').read(4096)\n"
        "print(len(data))\n"
        "print('1' if data.startswith(b'%PDF-') else '0')\n"
    )
    try:
        result = subprocess.run(
            [sys.executable, "-c", code, str(path)],
            check=False,
            capture_output=True,
            text=True,
            timeout=timeout,
        )
    except subprocess.TimeoutExpired:
        return "timeout", 0, False, "first-byte read timed out"
    if result.returncode != 0:
        error_text = (result.stderr or result.stdout).strip()
        if "TimeoutError" in error_text or "Operation timed out" in error_text or "Errno 60" in error_text:
            return "timeout", 0, False, "first-byte read returned Operation timed out"
        return "error", 0, False, "first-byte read failed"
    lines = result.stdout.splitlines()
    byte_count = int(lines[0]) if lines else 0
    is_pdf = len(lines) > 1 and lines[1] == "1"
    return "ok", byte_count, is_pdf, ""


def text_probe(path: Path, timeout: int, max_chars: int) -> tuple[str, int, str]:
    pdftotext = shutil.which("pdftotext")
    if not pdftotext:
        return "pdftotext_unavailable", 0, "pdftotext CLI not available"
    try:
        result = subprocess.run(
            [pdftotext, "-f", "1", "-l", "2", str(path), "-"],
            check=False,
            capture_output=True,
            text=True,
            timeout=timeout,
        )
    except subprocess.TimeoutExpired:
        return "timeout", 0, "pdftotext timed out"
    if result.returncode != 0:
        return "error", 0, (result.stderr or result.stdout).strip()[:200]
    text = " ".join(result.stdout.split())
    return ("text_extractable" if text else "no_text_extracted"), min(len(text), max_chars), ""


def materialization_status(magic_status: str, magic_is_pdf: bool, text_status: str) -> str:
    if magic_status == "missing":
        return "missing_source_pdf_match"
    if magic_status == "timeout":
        return "not_materialized_or_read_timeout"
    if magic_status != "ok":
        return "read_error"
    if not magic_is_pdf:
        return "not_pdf_or_unavailable"
    if text_status == "text_extractable":
        return "materialized_text_extractable"
    if text_status == "timeout":
        return "pdf_magic_ok_text_probe_timeout"
    if text_status == "no_text_extracted":
        return "pdf_magic_ok_no_text_extracted"
    if text_status == "pdftotext_unavailable":
        return "pdf_magic_ok_text_probe_not_run"
    return "pdf_magic_ok_text_probe_error"


def check_rows(args: argparse.Namespace) -> list[dict[str, str]]:
    source_dirs = args.source_pdf_dir or DEFAULT_SOURCE_PDF_DIRS
    rows = read_csv(args.gap_manifest)
    if args.batch_id:
        rows = [row for row in rows if row["batch_id"] == args.batch_id]
    if args.study_id:
        wanted = set(args.study_id)
        rows = [row for row in rows if row["study_id"] in wanted]
    if args.max_studies:
        rows = rows[: args.max_studies]

    checked_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    output_rows: list[dict[str, str]] = []
    for row in rows:
        study_id = row["study_id"]
        pdfs = find_pdfs_for_study(study_id, source_dirs, args.include_supplements)
        if not pdfs:
            magic_status, magic_bytes, magic_is_pdf, magic_notes = "missing", 0, False, "No matching PDF filename in supplied source directories."
            text_status, text_chars, text_notes = "not_run", 0, ""
            basename = ""
        else:
            first_pdf = pdfs[0]
            basename = first_pdf.name
            magic_status, magic_bytes, magic_is_pdf, magic_notes = magic_probe(first_pdf, args.timeout_seconds)
            if magic_status == "ok" and magic_is_pdf:
                text_status, text_chars, text_notes = text_probe(first_pdf, args.timeout_seconds, args.max_reported_text_chars)
            else:
                text_status, text_chars, text_notes = "not_run", 0, ""
        output_rows.append(
            {
                "study_id": study_id,
                "batch_id": row["batch_id"],
                "priority_rank": row["priority_rank"],
                "target_task_count": row["target_task_count"],
                "denominator_families": row["denominator_families"],
                "source_pdf_match_count": str(len(pdfs)),
                "first_match_basename": basename,
                "magic_probe_status": magic_status,
                "magic_probe_bytes": str(magic_bytes),
                "magic_probe_is_pdf": "true" if magic_is_pdf else "false",
                "text_probe_status": text_status,
                "text_probe_chars_first_two_pages_capped": str(text_chars),
                "materialization_status": materialization_status(magic_status, magic_is_pdf, text_status),
                "checked_at_utc": checked_at,
                "notes": "; ".join(note for note in (magic_notes, text_notes) if note),
            }
        )
    return output_rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--gap-manifest", type=Path, default=DEFAULT_GAP_MANIFEST)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--source-pdf-dir", type=Path, action="append", default=None)
    parser.add_argument("--batch-id")
    parser.add_argument("--study-id", action="append")
    parser.add_argument("--max-studies", type=int, default=0)
    parser.add_argument("--timeout-seconds", type=int, default=8)
    parser.add_argument("--max-reported-text-chars", type=int, default=2000)
    parser.add_argument("--include-supplements", action=argparse.BooleanOptionalAction, default=True)
    args = parser.parse_args()

    rows = check_rows(args)
    fields = [
        "study_id",
        "batch_id",
        "priority_rank",
        "target_task_count",
        "denominator_families",
        "source_pdf_match_count",
        "first_match_basename",
        "magic_probe_status",
        "magic_probe_bytes",
        "magic_probe_is_pdf",
        "text_probe_status",
        "text_probe_chars_first_two_pages_capped",
        "materialization_status",
        "checked_at_utc",
        "notes",
    ]
    write_csv(args.output, rows, fields)
    summary: dict[str, int] = {}
    for row in rows:
        summary[row["materialization_status"]] = summary.get(row["materialization_status"], 0) + 1
    print({"checked_studies": len(rows), "status_counts": summary})


if __name__ == "__main__":
    main()
