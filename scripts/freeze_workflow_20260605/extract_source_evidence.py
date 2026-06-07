#!/usr/bin/env python3
import json
import re
from pathlib import Path
from typing import Optional

from pypdf import PdfReader

REPO = Path.cwd()
AI_ADOPTION = Path(
    "/Users/newhosung/Library/CloudStorage/OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity/AI Adoption Meta Analysis - Documents/Meta/AI Adoption"
)
PDF_DIRS = [
    AI_ADOPTION / "PDFs",
    AI_ADOPTION / "R1/PDFs",
    AI_ADOPTION / "R2/PDFs",
    AI_ADOPTION / "R3/PDFs",
    AI_ADOPTION / "R4/PDFs",
]

TARGETS = {
    "S014": ["Table 4", "Path analysis", "perceived risk", "indirect"],
    "S021": ["Supplementary Table S4", "Table S4", "pre-course", "post-course", "path"],
    "S056": ["Table 3", "Path significance", "coefficients", "ChatGPT"],
    "S072": ["correlation", "Anxiety", "Effort", "Table", "1.000"],
    "S092": ["Table 3", "Structural Equation", "ChatGPT", "standardized"],
    "S097": ["correlation", "Table", "artificial intelligence", "attitude"],
    "S121": ["PLS-SEM", "path coefficient", "generative AI", "intention"],
    "S146": ["correlation", "Table", "ChatGPT", "self-efficacy"],
    "S195": ["PLSR", "component loading", "Table 3", "Table 4", "correlation"],
    "S184": ["correlation", "Table", "facilitating", "social influence"],
    "S202": ["Table 4", "Table 5", "Fornell", "structural equation"],
    "S206": ["PLSR", "component loading", "Table 3", "Table 4", "correlation"],
}


def find_pdf(study_id: str) -> Optional[Path]:
    name = f"{study_id}.pdf"
    for directory in PDF_DIRS:
        candidate = directory / name
        if candidate.exists():
            return candidate
    return None


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def page_hits(pdf_path: Path, terms: list[str]) -> list[dict]:
    reader = PdfReader(str(pdf_path))
    hits = []
    for index, page in enumerate(reader.pages, start=1):
        try:
            text = normalize(page.extract_text() or "")
        except Exception as exc:
            hits.append({"page": index, "error": str(exc), "matches": [], "snippet": ""})
            continue
        lower = text.lower()
        matches = [term for term in terms if term.lower() in lower]
        if matches:
            snippets = []
            for term in matches[:4]:
                pos = lower.find(term.lower())
                start = max(0, pos - 160)
                end = min(len(text), pos + 360)
                snippets.append(text[start:end])
            hits.append(
                {
                    "page": index,
                    "matches": matches,
                    "snippet": " ... ".join(snippets)[:1200],
                }
            )
    return hits


def main() -> None:
    output = {}
    for study_id, terms in TARGETS.items():
        pdf = find_pdf(study_id)
        if not pdf:
            output[study_id] = {"pdf": None, "status": "missing_pdf", "hits": []}
            continue
        output[study_id] = {
            "pdf": str(pdf),
            "status": "pdf_found",
            "hits": page_hits(pdf, terms)[:12],
        }
    out_path = (
        REPO
        / "data/04_extraction/03_source_document_adjudication/phase2/source_pdf_evidence_snippets_20260605.json"
    )
    out_path.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(out_path)
    for study_id, data in output.items():
        print(study_id, data["status"], "hits", len(data["hits"]), data["pdf"])


if __name__ == "__main__":
    main()
