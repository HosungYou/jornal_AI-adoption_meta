#!/usr/bin/env python3
"""Audit Paper2 pointer-only source evidence rows against local PDF text.

This script does not mutate frozen reference files. It creates a row-level audit
layer for P0/P1 rows whose frozen task units had source pointers but no evidence
text. The output is intentionally conservative: a PDF text hit is evidence for
source-text availability, not a new human adjudication.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import subprocess
from collections import Counter
from pathlib import Path

from pypdf import PdfReader


REPO = Path(__file__).resolve().parents[2]
AI_ADOPTION_ROOT = Path(
    os.environ.get(
        "AI_ADOPTION_META_ROOT",
        str(
            Path.home()
            / "<PRIVATE_ONEDRIVE_SHARED_LIBRARY>"
            / "AI Adoption Meta Analysis - Documents/Meta/AI Adoption"
        ),
    )
)

STEP5_RESULTS = REPO / "data/04_extraction/05_llm_masem_substitution/results"
DEFAULT_REVIEW = STEP5_RESULTS / "paper2_p0_p1_expert_review_20260611.csv"
DEFAULT_REFERENCE = (
    AI_ADOPTION_ROOT
    / "Paper2_LLM_Extraction_Working_20260605/09_reference_freeze/paper2_llm_task_units_labeled_tiered_freeze_20260605.csv"
)
DEFAULT_RERUN_INPUT = STEP5_RESULTS / "paper2_masem_substitution_rerun_input_20260611.csv"
DEFAULT_OUTPUT_DIR = STEP5_RESULTS / "pdf_source_text_audit_20260611"

PDF_DIRS = [
    AI_ADOPTION_ROOT / "PDFs",
    AI_ADOPTION_ROOT / "R1/PDFs",
    AI_ADOPTION_ROOT / "R2/PDFs",
    AI_ADOPTION_ROOT / "R3/PDFs",
    AI_ADOPTION_ROOT / "R4/PDFs",
    REPO / "data/02_screening/pdfs",
    REPO / "data/04_extraction/03_source_document_adjudication/source_pdfs",
]

CONSTRUCT_TERMS = {
    "PE": ["performance expectancy", "perceived usefulness", "usefulness", "PU"],
    "EE": ["effort expectancy", "perceived ease of use", "ease of use", "PEOU"],
    "SI": ["social influence", "subjective norm", "social norm", "SN"],
    "FC": ["facilitating condition", "facilitating conditions", "perceived behavioral control", "PBC"],
    "BI": ["behavioral intention", "behavioural intention", "intention to use", "continuance intention", "BI"],
    "UB": ["use behavior", "use behaviour", "actual use", "usage behavior", "usage behaviour", "UB"],
    "ATT": ["attitude", "attitudes", "ATT"],
    "SE": ["self-efficacy", "self efficacy", "computer self-efficacy", "SE"],
    "TRU": ["trust", "AI trust", "TRU"],
    "ANX": ["anxiety", "computer anxiety", "technology anxiety", "ANX"],
    "TRA": ["transparency", "explainability", "TRA"],
    "AUT": ["autonomy", "perceived autonomy", "AUT"],
}

SOURCE_TYPE_TERMS = {
    "direct_r_effect_size_extraction": ["correlation", "correlations", "pearson", "matrix", "r ="],
    "converted_or_model_derived_effect_size": ["path coefficient", "path coefficients", "beta", "structural model", "PLS", "SEM"],
    "trace_influence_diagnostic": ["correlation", "path", "anxiety", "effort"],
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def study_pdf_id(study_id: str) -> str:
    return re.sub(r"[-_].*$", "", study_id.strip())


def find_pdf(study_id: str) -> Path | None:
    pdf_id = study_pdf_id(study_id)
    candidates = [f"{study_id}.pdf", f"{pdf_id}.pdf"]
    for directory in PDF_DIRS:
        for name in candidates:
            candidate = directory / name
            if candidate.exists():
                return candidate
    return None


def normalize_text(text: str) -> str:
    text = text.replace("\u2212", "-").replace("\u2013", "-").replace("\u2014", "-")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def extract_with_pdftotext(pdf_path: Path) -> list[tuple[int, str]]:
    try:
        completed = subprocess.run(
            ["pdftotext", "-layout", str(pdf_path), "-"],
            text=True,
            capture_output=True,
            timeout=120,
        )
    except Exception:
        return []
    if completed.returncode != 0 or not completed.stdout.strip():
        return []
    pages = completed.stdout.split("\f")
    return [(index, normalize_text(page)) for index, page in enumerate(pages, start=1) if page.strip()]


def extract_with_pypdf(pdf_path: Path) -> list[tuple[int, str]]:
    pages: list[tuple[int, str]] = []
    reader = PdfReader(str(pdf_path))
    for index, page in enumerate(reader.pages, start=1):
        try:
            text = normalize_text(page.extract_text() or "")
        except Exception:
            text = ""
        if text:
            pages.append((index, text))
    return pages


def extract_pages(pdf_path: Path) -> list[tuple[int, str]]:
    pages = extract_with_pdftotext(pdf_path)
    if pages:
        return pages
    return extract_with_pypdf(pdf_path)


def numeric_variants(value: str) -> list[str]:
    if value is None:
        return []
    text = str(value).strip()
    if not text:
        return []
    variants = {text}
    try:
        number = float(text)
    except ValueError:
        return sorted(variants)
    variants.add(f"{number:.3f}")
    variants.add(f"{number:.2f}")
    variants.add(f"{number:.1f}")
    if -1 < number < 1 and number != 0:
        for digits in (3, 2, 1):
            formatted = f"{abs(number):.{digits}f}"
            no_leading = formatted[1:] if formatted.startswith("0") else formatted
            variants.add(("-" if number < 0 else "") + no_leading)
    return sorted(variants, key=len, reverse=True)


def contains_term(text_lower: str, term: str) -> bool:
    term_lower = term.lower()
    if len(term_lower) <= 4 and term_lower.isalpha():
        return re.search(rf"\b{re.escape(term_lower)}\b", text_lower) is not None
    return term_lower in text_lower


def construct_hits(text_lower: str, construct: str) -> list[str]:
    hits = []
    for term in CONSTRUCT_TERMS.get(construct, [construct]):
        if contains_term(text_lower, term):
            hits.append(term)
    return hits


def source_type_hits(text_lower: str, denominator_family: str) -> list[str]:
    return [
        term
        for term in SOURCE_TYPE_TERMS.get(denominator_family, [])
        if contains_term(text_lower, term)
    ]


def value_hit(text: str, value: str) -> str:
    normalized = text.replace("\u2212", "-")
    for variant in numeric_variants(value):
        if re.search(rf"(?<!\d){re.escape(variant)}(?!\d)", normalized):
            return variant
    return ""


def snippet_around(text: str, needle: str, fallback_terms: list[str]) -> str:
    lower = text.lower()
    pos = -1
    if needle:
        pos = lower.find(needle.lower())
    if pos < 0:
        for term in fallback_terms:
            pos = lower.find(term.lower())
            if pos >= 0:
                break
    if pos < 0:
        return text[:900]
    start = max(0, pos - 320)
    end = min(len(text), pos + 720)
    return text[start:end]


def summarize_row(row: dict[str, str], ref: dict[str, str], pages: list[tuple[int, str]]) -> dict[str, object]:
    construct_1 = row.get("construct_pair", "").split("-")[0] if "-" in row.get("construct_pair", "") else ref.get("construct_1", "")
    construct_2 = row.get("construct_pair", "").split("-")[1] if "-" in row.get("construct_pair", "") else ref.get("construct_2", "")
    value = row.get("statistic_value") or ref.get("statistic_value") or ref.get("consensus_value", "")
    best = {
        "page": "",
        "value_variant": "",
        "construct_1_terms": [],
        "construct_2_terms": [],
        "source_type_terms": [],
        "snippet": "",
    }

    for page_number, text in pages:
        lower = text.lower()
        vhit = value_hit(text, value)
        c1_hits = construct_hits(lower, construct_1)
        c2_hits = construct_hits(lower, construct_2)
        st_hits = source_type_hits(lower, row.get("denominator_family", ""))
        score = (5 if vhit else 0) + (2 if c1_hits else 0) + (2 if c2_hits else 0) + (1 if st_hits else 0)
        current_score = (
            (5 if best["value_variant"] else 0)
            + (2 if best["construct_1_terms"] else 0)
            + (2 if best["construct_2_terms"] else 0)
            + (1 if best["source_type_terms"] else 0)
        )
        if score > current_score:
            terms = c1_hits[:2] + c2_hits[:2] + st_hits[:2]
            best = {
                "page": page_number,
                "value_variant": vhit,
                "construct_1_terms": c1_hits,
                "construct_2_terms": c2_hits,
                "source_type_terms": st_hits,
                "snippet": snippet_around(text, vhit, terms),
            }

    if best["value_variant"] and best["construct_1_terms"] and best["construct_2_terms"]:
        status = "pdf_text_value_and_pair_terms_found"
        decision = "source_text_candidate_supports_pointer_value_requires_final_human_alignment_check"
    elif best["value_variant"]:
        status = "pdf_text_value_found_pair_terms_not_on_best_page"
        decision = "source_text_value_found_requires_manual_pair_alignment"
    elif best["construct_1_terms"] or best["construct_2_terms"] or best["source_type_terms"]:
        status = "pdf_text_context_found_value_not_found"
        decision = "source_text_context_found_but_numeric_value_requires_manual_table_review"
    else:
        status = "pdf_text_no_target_hit"
        decision = "no_pdf_text_hit_requires_manual_pdf_table_review_or_ocr"

    return {
        "pdf_text_review_status": status,
        "pdf_text_review_decision": decision,
        "pdf_page": best["page"],
        "matched_value_variant": best["value_variant"],
        "construct_1_terms_found": "|".join(best["construct_1_terms"][:4]),
        "construct_2_terms_found": "|".join(best["construct_2_terms"][:4]),
        "source_type_terms_found": "|".join(best["source_type_terms"][:4]),
        "pdf_text_snippet": best["snippet"][:1200],
    }


def write_markdown(path: Path, rows: list[dict[str, object]], study_count: int) -> None:
    status_counts = Counter(row["pdf_text_review_status"] for row in rows)
    decision_counts = Counter(row["pdf_text_review_decision"] for row in rows)
    lines = [
        "# Paper2 Pointer-Only PDF Source-Text Audit",
        "",
        "Date: 2026-06-11",
        "",
        "## Boundary",
        "",
        "This is a row-level PDF text audit for P0/P1 task units that previously had",
        "`source_pointer_present_no_evidence_text`. It does not overwrite the frozen",
        "source-anchored adjudicated human reference standard. Automated text hits are",
        "treated as source-text candidates and retain a final alignment-check boundary.",
        "",
        "## Scope",
        "",
        f"- Pointer-only rows audited: {len(rows)}",
        f"- Unique studies audited: {study_count}",
        "",
        "## PDF Text Review Status",
        "",
    ]
    for key, value in sorted(status_counts.items()):
        lines.append(f"- {key}: {value}")
    lines.extend(["", "## Review Decisions", ""])
    for key, value in sorted(decision_counts.items()):
        lines.append(f"- {key}: {value}")
    lines.extend(
        [
            "",
            "## Claim Boundary",
            "",
            "Rows with `pdf_text_value_and_pair_terms_found` have candidate source text",
            "support in the local PDF extraction layer, but final manuscript claims should",
            "still cite the source-anchored human reference and preserve the audit file.",
            "Rows without numeric value hits require manual table review or OCR before they",
            "can be upgraded from source-risk status.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--review", type=Path, default=DEFAULT_REVIEW)
    parser.add_argument("--reference", type=Path, default=DEFAULT_REFERENCE)
    parser.add_argument("--rerun-input", type=Path, default=DEFAULT_RERUN_INPUT)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    args = parser.parse_args()

    review_rows = read_csv(args.review)
    reference_rows = read_csv(args.reference)
    rerun_rows = read_csv(args.rerun_input) if args.rerun_input.exists() else []

    ref_by_task = {row["task_unit_id"]: row for row in reference_rows}
    rerun_by_task = {row.get("substitution_source_task_unit_id", ""): row for row in rerun_rows}
    pointer_rows = [
        row
        for row in review_rows
        if row.get("source_evidence_status") == "source_pointer_present_no_evidence_text"
    ]

    args.output_dir.mkdir(parents=True, exist_ok=True)
    page_cache: dict[str, list[tuple[int, str]]] = {}
    pdf_cache: dict[str, Path | None] = {}
    output_rows: list[dict[str, object]] = []

    for row in pointer_rows:
        ref = ref_by_task.get(row["task_unit_id"], {})
        study_id = row["study_id"]
        pdf_path = pdf_cache.setdefault(study_id, find_pdf(study_id))
        if not pdf_path:
            audit = {
                "pdf_text_review_status": "pdf_missing",
                "pdf_text_review_decision": "missing_pdf_requires_source_retrieval",
                "pdf_page": "",
                "matched_value_variant": "",
                "construct_1_terms_found": "",
                "construct_2_terms_found": "",
                "source_type_terms_found": "",
                "pdf_text_snippet": "",
            }
            pdf_pages = ""
        else:
            cache_key = str(pdf_path)
            if cache_key not in page_cache:
                page_cache[cache_key] = extract_pages(pdf_path)
            pages = page_cache[cache_key]
            pdf_pages = len(pages)
            if pages:
                audit = summarize_row(row, ref, pages)
            else:
                audit = {
                    "pdf_text_review_status": "pdf_text_extract_failed",
                    "pdf_text_review_decision": "pdf_present_but_text_extraction_failed_requires_ocr",
                    "pdf_page": "",
                    "matched_value_variant": "",
                    "construct_1_terms_found": "",
                    "construct_2_terms_found": "",
                    "source_type_terms_found": "",
                    "pdf_text_snippet": "",
                }

        rerun = rerun_by_task.get(row["task_unit_id"], {})
        output_rows.append(
            {
                "task_unit_id": row["task_unit_id"],
                "study_id": study_id,
                "decision_id": row["decision_id"],
                "analysis_record_id": row.get("paper1_primary_analysis_record_id", ""),
                "review_priority": row["review_priority"],
                "denominator_family": row["denominator_family"],
                "rerun_input_role": row["rerun_input_role"],
                "expert_review_decision": row["expert_review_decision"],
                "construct_pair": row["construct_pair"],
                "statistic_value": row["statistic_value"],
                "source_locator": ref.get("source_locator", "") or rerun.get("source_locator", ""),
                "source_location": ref.get("source_evidence", "") or rerun.get("source_location", ""),
                "pdf_path": "" if not pdf_path else str(pdf_path),
                "pdf_text_pages_extracted": pdf_pages,
                **audit,
            }
        )

    fields = [
        "task_unit_id",
        "study_id",
        "decision_id",
        "analysis_record_id",
        "review_priority",
        "denominator_family",
        "rerun_input_role",
        "expert_review_decision",
        "construct_pair",
        "statistic_value",
        "source_locator",
        "source_location",
        "pdf_path",
        "pdf_text_pages_extracted",
        "pdf_text_review_status",
        "pdf_text_review_decision",
        "pdf_page",
        "matched_value_variant",
        "construct_1_terms_found",
        "construct_2_terms_found",
        "source_type_terms_found",
        "pdf_text_snippet",
    ]
    csv_path = args.output_dir / "paper2_pointer_only_pdf_source_text_audit_20260611.csv"
    md_path = args.output_dir / "PAPER2_POINTER_ONLY_PDF_SOURCE_TEXT_AUDIT_20260611.md"
    write_csv(csv_path, output_rows, fields)
    write_markdown(md_path, output_rows, len({row["study_id"] for row in output_rows}))
    print(
        {
            "rows": len(output_rows),
            "studies": len({row["study_id"] for row in output_rows}),
            "status_counts": dict(Counter(row["pdf_text_review_status"] for row in output_rows)),
            "csv": str(csv_path),
            "md": str(md_path),
        }
    )


if __name__ == "__main__":
    main()
