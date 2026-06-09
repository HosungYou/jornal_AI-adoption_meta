#!/usr/bin/env python3
"""Build private source-rendering packets and share-safe manifests for Step 5."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


REPO = Path(__file__).resolve().parents[2]
PROJECT_DOCS_ROOT = REPO.parents[1]
STEP5 = REPO / "data/04_extraction/05_llm_masem_substitution"
PAPER_C = REPO / "data/04_extraction/07_paper_c_harness_benchmark"
DEFAULT_TEMPLATE = STEP5 / "locked_outputs/full_corpus_locked_output_template_20260609.csv"
DEFAULT_SOURCE_PDF_DIRS = [
    REPO / "data/04_extraction/03_source_document_adjudication/source_pdfs",
    PROJECT_DOCS_ROOT / "Meta/AI Adoption/PDFs",
    PROJECT_DOCS_ROOT / "Meta/AI Adoption/R1/PDFs",
    PROJECT_DOCS_ROOT / "Meta/AI Adoption/R2/PDFs",
    PROJECT_DOCS_ROOT / "Meta/AI Adoption/R3/PDFs",
    PROJECT_DOCS_ROOT / "Meta/AI Adoption/R4/PDFs",
    PROJECT_DOCS_ROOT / "Meta/source_pdfs/table36_62",
]
DEFAULT_PRIVATE_OUTPUT_DIR = PAPER_C / "private/source_renderings_20260609/source_packets"
DEFAULT_MANIFEST_OUTPUT = PAPER_C / "00_manifest/source_rendering_available_pdf_manifest_20260609.csv"
DEFAULT_SMOKE_TASK_OUTPUT = PAPER_C / "06_rerun_bundles/source_rendered_smoke_task_ids_20260609.csv"
DEFAULT_STATUS_OUTPUT = PAPER_C / "00_manifest/SOURCE_RENDERING_PREFLIGHT_STATUS_20260609.md"


@dataclass
class Chunk:
    doc_ref: str
    page: int
    chunk_index: int
    text: str
    score: int


@dataclass
class TableBlock:
    doc_ref: str
    page: int
    table_index: int
    text: str
    score: int


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


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def task_terms(rows: list[dict[str, str]]) -> set[str]:
    terms = {
        "correlation",
        "correlations",
        "flc",
        "fornell",
        "fornell-larcker",
        "discriminant",
        "validity",
        "path",
        "coefficient",
        "coefficients",
        "beta",
        "structural",
        "model",
        "table",
        "results",
        "hypothesis",
        "direct",
        "effect",
        "pls",
        "sem",
        "regression",
    }
    for row in rows:
        text = row.get("model_input_text", "")
        terms.update(term.lower() for term in re.findall(r"\b[A-Z]{2,5}\b", text))
        terms.update(term.lower() for term in re.findall(r"\bT[0-9]\b", text))
        for pair in re.findall(r"\b[A-Z]{2,5}-[A-Z]{2,5}\b", text):
            terms.update(part.lower() for part in pair.split("-"))
    abbreviation_terms = {
        "att": ["attitude", "attitudes"],
        "bi": ["behavioral intention", "behavioural intention", "intention"],
        "ee": ["effort expectancy", "ease of use", "perceived ease"],
        "fc": ["facilitating condition", "facilitating conditions"],
        "hm": ["hedonic motivation"],
        "pe": ["performance expectancy", "perceived performance", "usefulness"],
        "si": ["social influence"],
        "ub": ["use behavior", "usage behavior", "use behaviour", "adoption"],
    }
    expanded_terms = set(terms)
    for term in terms:
        expanded_terms.update(abbreviation_terms.get(term, []))
    return {term for term in expanded_terms if len(term) >= 2}


def score_chunk(text: str, terms: set[str]) -> int:
    lowered = text.lower()
    score = 0
    for term in terms:
        if term in lowered:
            score += 3 if len(term) <= 3 else 1
    for high_value in (
        "table",
        "flc",
        "fornell",
        "fornell-larcker",
        "path coefficient",
        "path coefficients",
        "direct effect",
        "hypothesis",
        "structural model",
    ):
        if high_value in lowered:
            score += 5
    return score


def chunk_page_text(text: str, max_chunk_chars: int, overlap_chars: int) -> list[str]:
    text = normalize_text(text)
    if not text:
        return []
    chunks = []
    start = 0
    while start < len(text):
        end = min(len(text), start + max_chunk_chars)
        chunks.append(text[start:end])
        if end == len(text):
            break
        start = max(0, end - overlap_chars)
    return chunks


def extract_pdf_chunks(pdf_path: Path, doc_ref: str, terms: set[str], max_chunk_chars: int, overlap_chars: int) -> list[Chunk]:
    try:
        import pdfplumber
    except ImportError as exc:
        raise SystemExit("pdfplumber is required to build source-rendering packets") from exc

    chunks: list[Chunk] = []
    with pdfplumber.open(pdf_path) as pdf:
        for page_index, page in enumerate(pdf.pages, start=1):
            text = page.extract_text() or ""
            for chunk_index, chunk_text in enumerate(chunk_page_text(text, max_chunk_chars, overlap_chars), start=1):
                chunks.append(
                    Chunk(
                        doc_ref=doc_ref,
                        page=page_index,
                        chunk_index=chunk_index,
                        text=chunk_text,
                        score=score_chunk(chunk_text, terms),
                    )
                )
    return chunks


def format_table(table: list[list[str | None]]) -> str:
    lines = []
    for row_index, row in enumerate(table, start=1):
        cells = [normalize_text(cell or "") for cell in row]
        if any(cells):
            lines.append(f"row {row_index}: " + " | ".join(cells))
    return "\n".join(lines)


def extract_pdf_tables(pdf_path: Path, doc_ref: str, terms: set[str]) -> list[TableBlock]:
    try:
        import pdfplumber
    except ImportError as exc:
        raise SystemExit("pdfplumber is required to build source-rendering packets") from exc

    table_blocks: list[TableBlock] = []
    with pdfplumber.open(pdf_path) as pdf:
        for page_index, page in enumerate(pdf.pages, start=1):
            try:
                tables = page.extract_tables() or []
            except Exception:
                tables = []
            for table_index, table in enumerate(tables, start=1):
                table_text = format_table(table)
                if not table_text:
                    continue
                score = score_chunk(table_text, terms)
                if score > 0:
                    score += 10
                table_blocks.append(
                    TableBlock(
                        doc_ref=doc_ref,
                        page=page_index,
                        table_index=table_index,
                        text=table_text,
                        score=score,
                    )
                )
    return table_blocks


def select_table_blocks(tables: list[TableBlock], max_table_chars: int) -> list[TableBlock]:
    if not tables:
        return []
    selected: list[TableBlock] = []
    char_count = 0
    ranked = sorted(tables, key=lambda item: (-item.score, item.doc_ref, item.page, item.table_index))
    for table in ranked:
        if table.score <= 0 and selected:
            continue
        block = f"[{table.doc_ref} page {table.page} table {table.table_index} score {table.score}]\n{table.text}\n"
        if char_count + len(block) > max_table_chars and selected:
            continue
        selected.append(table)
        char_count += len(block)
        if char_count >= max_table_chars:
            break
    if not selected:
        selected = ranked[: max(1, min(2, len(ranked)))]
    return selected


def build_packet(
    study_id: str,
    chunks: list[Chunk],
    tables: list[TableBlock],
    rows: list[dict[str, str]],
    max_packet_chars: int,
    max_table_chars: int,
) -> tuple[str, int, int]:
    selected: list[Chunk] = []
    selected_tables = select_table_blocks(tables, max_table_chars)
    char_count = sum(
        len(f"[{table.doc_ref} page {table.page} table {table.table_index} score {table.score}]\n{table.text}\n")
        for table in selected_tables
    )
    ranked = sorted(chunks, key=lambda item: (-item.score, item.doc_ref, item.page, item.chunk_index))
    for chunk in ranked:
        if chunk.score <= 0 and selected:
            continue
        block = f"[{chunk.doc_ref} page {chunk.page} chunk {chunk.chunk_index} score {chunk.score}]\n{chunk.text}\n"
        if char_count + len(block) > max_packet_chars and selected:
            continue
        selected.append(chunk)
        char_count += len(block)
        if char_count >= max_packet_chars:
            break
    if not selected:
        selected = chunks[: max(1, min(3, len(chunks)))]

    task_stub = "\n".join(
        f"- {row['task_unit_id']}: {row['model_input_text']}"
        for row in rows
    )
    parts = [
        f"Source packet for study_id={study_id}",
        "Policy: rendered from local source PDFs; no human reference value, human adjudication rationale, or human-adjudicated source locator is inserted.",
        "Use only page/chunk labels in model_source_locator. Do not quote source text in share-safe locked outputs when suppress_source_quotes is active.",
        "",
        "Target task stubs:",
        task_stub,
        "",
        "Extracted table blocks:",
    ]
    if selected_tables:
        for table in sorted(selected_tables, key=lambda item: (item.doc_ref, item.page, item.table_index)):
            parts.append(f"[{table.doc_ref} page {table.page} table {table.table_index} score {table.score}]")
            parts.append(table.text)
            parts.append("")
    else:
        parts.append("No extractable PDF table blocks selected.")
        parts.append("")
    parts.extend(
        [
        "Rendered source chunks:",
        ]
    )
    for chunk in sorted(selected, key=lambda item: (item.doc_ref, item.page, item.chunk_index)):
        parts.append(f"[{chunk.doc_ref} page {chunk.page} chunk {chunk.chunk_index} score {chunk.score}]")
        parts.append(chunk.text)
        parts.append("")
    return "\n".join(parts).strip() + "\n", len(selected), len(selected_tables)


def pdfs_for_study(study_id: str, source_pdf_dirs: list[Path], include_supplements: bool) -> list[Path]:
    selected: list[Path] = []
    for source_pdf_dir in source_pdf_dirs:
        exact = source_pdf_dir / f"{study_id}.pdf"
        if exact.exists():
            selected.append(exact)
            break
    if not selected:
        for source_pdf_dir in source_pdf_dirs:
            matches = sorted(source_pdf_dir.glob(f"{study_id}*.pdf"))
            if matches:
                selected.append(matches[0])
                break
    if include_supplements:
        selected_paths = {path.resolve() for path in selected}
        for source_pdf_dir in source_pdf_dirs:
            for supplement in sorted(source_pdf_dir.glob(f"{study_id}_*.pdf")):
                if supplement.resolve() not in selected_paths:
                    selected.append(supplement)
                    selected_paths.add(supplement.resolve())
    return selected


def render_packets(args: argparse.Namespace) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    rows = [
        row for row in read_csv(args.template)
        if row["scoring_eligibility"].startswith("eligible_after_locked_llm_output")
    ]
    if args.study_id:
        wanted_studies = set(args.study_id)
        rows = [row for row in rows if row["study_id"] in wanted_studies]
    rows_by_study: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        rows_by_study.setdefault(row["study_id"], []).append(row)

    manifest_rows = []
    rendered_study_ids = []
    args.private_output_dir.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    source_pdf_dirs = args.source_pdf_dir or DEFAULT_SOURCE_PDF_DIRS

    for study_id in sorted(rows_by_study):
        pdfs = pdfs_for_study(study_id, source_pdf_dirs, args.include_supplements)
        non_pdf_supplements = []
        for source_pdf_dir in source_pdf_dirs:
            non_pdf_supplements.extend(
                path for path in source_pdf_dir.glob(f"{study_id}*")
                if path.suffix.lower() != ".pdf"
            )
        if not pdfs:
            continue
        study_rows = rows_by_study[study_id]
        terms = task_terms(study_rows)
        chunks = []
        tables = []
        extraction_errors = []
        for doc_index, pdf_path in enumerate(pdfs, start=1):
            try:
                chunks.extend(
                    extract_pdf_chunks(
                        pdf_path,
                        f"{study_id}_doc{doc_index}",
                        terms,
                        args.max_chunk_chars,
                        args.overlap_chars,
                    )
                )
                tables.extend(extract_pdf_tables(pdf_path, f"{study_id}_doc{doc_index}", terms))
            except Exception as exc:
                extraction_errors.append(f"{pdf_path.name}: {exc}")
        if not chunks:
            manifest_rows.append(
                {
                    "study_id": study_id,
                    "target_task_count": str(len(study_rows)),
                    "denominator_families": ";".join(sorted({row["denominator_family"] for row in study_rows})),
                    "available_source_pdf_count": str(len(pdfs)),
                    "included_source_pdf_count": "0",
                    "non_pdf_supplement_count": str(len(non_pdf_supplements)),
                    "rendered_chunk_count": "0",
                    "rendered_table_count": "0",
                    "max_chunk_chars": str(args.max_chunk_chars),
                    "overlap_chars": str(args.overlap_chars),
                    "max_packet_chars": str(args.max_packet_chars),
                    "max_table_chars": str(args.max_table_chars),
                    "packet_chars": "",
                    "packet_sha256": "",
                    "private_packet_ref": "no_private_packet_created",
                    "render_timestamp_utc": now,
                    "status": "render_failed_no_extractable_text",
                    "notes": "; ".join(extraction_errors)[:500] or "No extractable text chunks produced.",
                }
            )
            continue
        packet_text, selected_chunk_count, selected_table_count = build_packet(
            study_id,
            chunks,
            tables,
            study_rows,
            args.max_packet_chars,
            args.max_table_chars,
        )
        packet_path = args.private_output_dir / f"{study_id}_source_packet_20260609.txt"
        packet_path.write_text(packet_text, encoding="utf-8")
        rendered_study_ids.append(study_id)
        manifest_rows.append(
            {
                "study_id": study_id,
                "target_task_count": str(len(study_rows)),
                "denominator_families": ";".join(sorted({row["denominator_family"] for row in study_rows})),
                "available_source_pdf_count": str(len(pdfs)),
                "included_source_pdf_count": str(len(pdfs)),
                "non_pdf_supplement_count": str(len(non_pdf_supplements)),
                "rendered_chunk_count": str(selected_chunk_count),
                "rendered_table_count": str(selected_table_count),
                "max_chunk_chars": str(args.max_chunk_chars),
                "overlap_chars": str(args.overlap_chars),
                "max_packet_chars": str(args.max_packet_chars),
                "max_table_chars": str(args.max_table_chars),
                "packet_chars": str(packet_path.stat().st_size),
                "packet_sha256": sha256(packet_path),
                "private_packet_ref": "local_private_packet_not_committed",
                "render_timestamp_utc": now,
                "status": "packet_rendered_private_with_partial_pdf_errors" if extraction_errors else "packet_rendered_private",
                "notes": ("Partial PDF extraction errors: " + "; ".join(extraction_errors)[:450]) if extraction_errors else "Share-safe manifest only; rendered source text remains in ignored private storage.",
            }
        )

    smoke_rows = []
    rendered_study_id_set = set(rendered_study_ids)
    if args.smoke_stratified_per_family:
        family_counts: dict[str, int] = {}
        for row in rows:
            if row["study_id"] not in rendered_study_id_set:
                continue
            family = row["denominator_family"]
            if family_counts.get(family, 0) >= args.smoke_stratified_per_family:
                continue
            smoke_rows.append(
                {
                    "task_unit_id": row["task_unit_id"],
                    "study_id": row["study_id"],
                    "denominator_family": row["denominator_family"],
                    "expected_answer_type": row["expected_answer_type"],
                    "selection_reason": "source_pdf_available_stratified_by_denominator_family",
                }
            )
            family_counts[family] = family_counts.get(family, 0) + 1
    else:
        for study_id in rendered_study_ids:
            for row in rows_by_study[study_id][: args.smoke_rows_per_study]:
                smoke_rows.append(
                    {
                        "task_unit_id": row["task_unit_id"],
                        "study_id": row["study_id"],
                        "denominator_family": row["denominator_family"],
                        "expected_answer_type": row["expected_answer_type"],
                        "selection_reason": "source_pdf_available_first_rows_per_study",
                    }
                )
    return manifest_rows, smoke_rows


def write_status(path: Path, manifest_rows: list[dict[str, str]], smoke_rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    by_family: dict[str, int] = {}
    for row in smoke_rows:
        by_family[row["denominator_family"]] = by_family.get(row["denominator_family"], 0) + 1
    rendered_rows = [
        row for row in manifest_rows
        if row.get("private_packet_ref") == "local_private_packet_not_committed"
    ]
    failed_rows = [row for row in manifest_rows if row not in rendered_rows]
    status_counts: dict[str, int] = {}
    for row in manifest_rows:
        status_counts[row["status"]] = status_counts.get(row["status"], 0) + 1
    lines = [
        "# Source Rendering Preflight Status",
        "",
        "Date: 2026-06-09",
        "",
        "Status: source-rendering coverage preflight prepared. This artifact does not authorize a full-corpus model run.",
        "",
        "## Rendered Private Packets",
        "",
        f"- Studies in coverage manifest: {len(manifest_rows)}",
        f"- Studies with private rendered packets: {len(rendered_rows)}",
        f"- Studies without rendered packets: {len(failed_rows)}",
        f"- Target rows covered by rendered packets: {sum(int(row['target_task_count']) for row in rendered_rows)}",
        f"- Target rows not yet source-rendered: {sum(int(row['target_task_count']) for row in failed_rows)}",
        f"- Source-rendered smoke task rows selected: {len(smoke_rows)}",
        "",
        "## Rendering Status Counts",
        "",
    ]
    for status, count in sorted(status_counts.items()):
        lines.append(f"- `{status}`: {count}")
    lines.extend(
        [
            "",
        "## Smoke Task Family Counts",
        "",
        ]
    )
    for family, count in sorted(by_family.items()):
        lines.append(f"- `{family}`: {count}")
    lines.extend(
        [
            "",
            "## Safety Boundary",
            "",
            "- PDF files and rendered source text remain local/private and are not committed.",
            "- Share-safe artifacts record study IDs, task IDs, counts, packet hashes, and status only.",
            "- Human reference values, adjudication rationales, and human-adjudicated source locators are not inserted into source packets.",
            "- The source-rendered smoke should suppress `model_source_quote` so locked CSV output does not commit source-document text.",
            "",
            "## Next Gate",
            "",
            "Run a source-rendered smoke only if the selected task IDs all have private rendered source packets. Full-corpus `M1-R` remains blocked until source PDFs are locally materialized or share-safe source renderings are available for the full 2,043-row target shell.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--template", type=Path, default=DEFAULT_TEMPLATE)
    parser.add_argument("--source-pdf-dir", type=Path, action="append", default=None)
    parser.add_argument("--private-output-dir", type=Path, default=DEFAULT_PRIVATE_OUTPUT_DIR)
    parser.add_argument("--manifest-output", type=Path, default=DEFAULT_MANIFEST_OUTPUT)
    parser.add_argument("--smoke-task-output", type=Path, default=DEFAULT_SMOKE_TASK_OUTPUT)
    parser.add_argument("--status-output", type=Path, default=DEFAULT_STATUS_OUTPUT)
    parser.add_argument("--study-id", action="append", default=None)
    parser.add_argument("--max-chunk-chars", type=int, default=3500)
    parser.add_argument("--overlap-chars", type=int, default=350)
    parser.add_argument("--max-packet-chars", type=int, default=22000)
    parser.add_argument("--max-table-chars", type=int, default=12000)
    parser.add_argument("--smoke-rows-per-study", type=int, default=2)
    parser.add_argument("--smoke-stratified-per-family", type=int, default=0)
    parser.add_argument("--include-supplements", action=argparse.BooleanOptionalAction, default=True)
    args = parser.parse_args()

    manifest_rows, smoke_rows = render_packets(args)
    manifest_fields = [
        "study_id",
        "target_task_count",
        "denominator_families",
        "available_source_pdf_count",
        "included_source_pdf_count",
        "non_pdf_supplement_count",
        "rendered_chunk_count",
        "rendered_table_count",
        "max_chunk_chars",
        "overlap_chars",
        "max_packet_chars",
        "max_table_chars",
        "packet_chars",
        "packet_sha256",
        "private_packet_ref",
        "render_timestamp_utc",
        "status",
        "notes",
    ]
    smoke_fields = ["task_unit_id", "study_id", "denominator_family", "expected_answer_type", "selection_reason"]
    write_csv(args.manifest_output, manifest_rows, manifest_fields)
    write_csv(args.smoke_task_output, smoke_rows, smoke_fields)
    write_status(args.status_output, manifest_rows, smoke_rows)
    rendered_studies = sum(
        row.get("private_packet_ref") == "local_private_packet_not_committed"
        for row in manifest_rows
    )
    print(
        json.dumps(
            {
                "coverage_manifest_studies": len(manifest_rows),
                "rendered_studies": rendered_studies,
                "failed_studies": len(manifest_rows) - rendered_studies,
                "smoke_rows": len(smoke_rows),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
