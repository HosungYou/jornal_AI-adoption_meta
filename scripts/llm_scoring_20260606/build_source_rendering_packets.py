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
STEP5 = REPO / "data/04_extraction/05_llm_masem_substitution"
PAPER_C = REPO / "data/04_extraction/07_paper_c_harness_benchmark"
DEFAULT_TEMPLATE = STEP5 / "locked_outputs/full_corpus_locked_output_template_20260609.csv"
DEFAULT_SOURCE_PDF_DIR = REPO / "data/04_extraction/03_source_document_adjudication/source_pdfs"
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
    return {term for term in terms if len(term) >= 2}


def score_chunk(text: str, terms: set[str]) -> int:
    lowered = text.lower()
    score = 0
    for term in terms:
        if term in lowered:
            score += 3 if len(term) <= 3 else 1
    for high_value in ("table", "path coefficient", "direct effect", "hypothesis", "structural model"):
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


def build_packet(study_id: str, chunks: list[Chunk], rows: list[dict[str, str]], max_packet_chars: int) -> tuple[str, int]:
    selected: list[Chunk] = []
    char_count = 0
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
        "Rendered source chunks:",
    ]
    for chunk in sorted(selected, key=lambda item: (item.doc_ref, item.page, item.chunk_index)):
        parts.append(f"[{chunk.doc_ref} page {chunk.page} chunk {chunk.chunk_index} score {chunk.score}]")
        parts.append(chunk.text)
        parts.append("")
    return "\n".join(parts).strip() + "\n", len(selected)


def render_packets(args: argparse.Namespace) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    rows = [
        row for row in read_csv(args.template)
        if row["scoring_eligibility"].startswith("eligible_after_locked_llm_output")
    ]
    rows_by_study: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        rows_by_study.setdefault(row["study_id"], []).append(row)

    manifest_rows = []
    rendered_study_ids = []
    args.private_output_dir.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")

    for study_id in sorted(rows_by_study):
        pdfs = sorted(args.source_pdf_dir.glob(f"{study_id}*.pdf"))
        non_pdf_supplements = sorted(
            path for path in args.source_pdf_dir.glob(f"{study_id}*")
            if path.suffix.lower() != ".pdf"
        )
        if not pdfs:
            continue
        study_rows = rows_by_study[study_id]
        terms = task_terms(study_rows)
        chunks = []
        for doc_index, pdf_path in enumerate(pdfs, start=1):
            chunks.extend(extract_pdf_chunks(pdf_path, f"{study_id}_doc{doc_index}", terms, args.max_chunk_chars, args.overlap_chars))
        if not chunks:
            continue
        packet_text, selected_chunk_count = build_packet(study_id, chunks, study_rows, args.max_packet_chars)
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
                "max_chunk_chars": str(args.max_chunk_chars),
                "overlap_chars": str(args.overlap_chars),
                "max_packet_chars": str(args.max_packet_chars),
                "packet_chars": str(packet_path.stat().st_size),
                "packet_sha256": sha256(packet_path),
                "private_packet_ref": "local_private_packet_not_committed",
                "render_timestamp_utc": now,
                "status": "packet_rendered_private",
                "notes": "Share-safe manifest only; rendered source text remains in ignored private storage.",
            }
        )

    smoke_rows = []
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
    lines = [
        "# Source Rendering Preflight Status",
        "",
        "Date: 2026-06-09",
        "",
        "Status: partial source-rendering preflight prepared. Local source PDFs are currently available only for a small subset of the post-freeze target rows, so this artifact does not authorize a full-corpus model run.",
        "",
        "## Rendered Private Packets",
        "",
        f"- Studies with private rendered packets: {len(manifest_rows)}",
        f"- Target rows covered by rendered packets: {sum(int(row['target_task_count']) for row in manifest_rows)}",
        f"- Source-rendered smoke task rows selected: {len(smoke_rows)}",
        "",
        "## Smoke Task Family Counts",
        "",
    ]
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
            "Run the source-rendered smoke on the selected task IDs. If the runner exports a clean locked output without source quotes or CLI errors, record that this validates the prompt/source-packet path only. Full-corpus `M1-R` remains blocked until source PDFs or share-safe source renderings are available for the full 2,043-row target shell.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--template", type=Path, default=DEFAULT_TEMPLATE)
    parser.add_argument("--source-pdf-dir", type=Path, default=DEFAULT_SOURCE_PDF_DIR)
    parser.add_argument("--private-output-dir", type=Path, default=DEFAULT_PRIVATE_OUTPUT_DIR)
    parser.add_argument("--manifest-output", type=Path, default=DEFAULT_MANIFEST_OUTPUT)
    parser.add_argument("--smoke-task-output", type=Path, default=DEFAULT_SMOKE_TASK_OUTPUT)
    parser.add_argument("--status-output", type=Path, default=DEFAULT_STATUS_OUTPUT)
    parser.add_argument("--max-chunk-chars", type=int, default=3500)
    parser.add_argument("--overlap-chars", type=int, default=350)
    parser.add_argument("--max-packet-chars", type=int, default=22000)
    parser.add_argument("--smoke-rows-per-study", type=int, default=2)
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
        "max_chunk_chars",
        "overlap_chars",
        "max_packet_chars",
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
    print(json.dumps({"rendered_studies": len(manifest_rows), "smoke_rows": len(smoke_rows)}, sort_keys=True))


if __name__ == "__main__":
    main()
