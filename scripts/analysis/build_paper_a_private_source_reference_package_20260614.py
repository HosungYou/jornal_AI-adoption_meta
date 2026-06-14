#!/usr/bin/env python3
"""Build a private canonical PDF/source-reference package for Paper A review.

The package is intentionally under ignored private storage. It copies PDFs and
source packets into one local folder so human review and AI source tracing use
the same source universe. Do not commit the generated package.
"""
from __future__ import annotations

import csv
import hashlib
import re
import shutil
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
PACKAGE = REPO / "data/04_extraction/07_paper_c_harness_benchmark/private/paper_a_source_reference_package_20260614"
PDF_OUT = PACKAGE / "pdfs"
PACKET_OUT = PACKAGE / "source_packets"
MANIFEST_OUT = PACKAGE / "manifests"
REVIEW_OUT = PACKAGE / "review_inputs"
SOURCE_PACKET_DIR = REPO / "data/04_extraction/07_paper_c_harness_benchmark/private/source_renderings_20260609_full_coverage/source_packets"
AI_TRACE_DIR = REPO / "data/04_extraction/05_llm_masem_substitution/results/paper_a_ai_candidate_source_trace_20260614"
PDF_ROOTS = [
    Path("/Users/newhosung/Library/CloudStorage/OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity/AI Adoption Meta Analysis - Documents/Meta/AI Adoption/PDFs"),
    Path("/Users/newhosung/Library/CloudStorage/OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity/AI Adoption Meta Analysis - Documents/Meta/AI Adoption/R1/PDFs"),
    Path("/Users/newhosung/Library/CloudStorage/OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity/AI Adoption Meta Analysis - Documents/Meta/AI Adoption/R2/PDFs"),
    Path("/Users/newhosung/Library/CloudStorage/OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity/AI Adoption Meta Analysis - Documents/Meta/AI Adoption/R3/PDFs"),
    Path("/Users/newhosung/Library/CloudStorage/OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity/AI Adoption Meta Analysis - Documents/Meta/AI Adoption/R4/PDFs"),
    REPO / "data/02_screening/pdfs",
]
REVIEW_FILES = [
    "PAPER_A_AI_CANDIDATE_SOURCE_TRACE_PACKET_20260614.md",
    "paper_a_ai_candidate_source_trace_existing_human_values_20260614.csv",
    "paper_a_ai_candidate_full10_densification_trace_20260614.csv",
    "paper_a_human_confirmation_template_from_ai_trace_20260614.csv",
    "paper_a_ai_candidate_source_trace_summary_20260614.csv",
]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def base_study_id(study_id: str) -> str:
    m = re.match(r"^(S\d+)", str(study_id).strip())
    return m.group(1) if m else str(study_id).strip()


def find_pdf(study_id: str) -> tuple[Path | None, str, str]:
    base = base_study_id(study_id)
    candidates = [study_id]
    if base not in candidates:
        candidates.append(base)
    for stem in candidates:
        for root in PDF_ROOTS:
            p = root / f"{stem}.pdf"
            if p.exists():
                return p, stem, str(root)
    return None, "", ""


def write_csv(path: Path, rows: list[dict], fieldnames: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)

for d in [PDF_OUT, PACKET_OUT, MANIFEST_OUT, REVIEW_OUT]:
    d.mkdir(parents=True, exist_ok=True)

packet_files = sorted(SOURCE_PACKET_DIR.glob("S*_source_packet_20260609.txt"))
study_ids = [p.name.split("_source_packet_20260609.txt")[0] for p in packet_files]
manifest_rows = []
alias_rows = []

for packet in packet_files:
    sid = packet.name.split("_source_packet_20260609.txt")[0]
    base = base_study_id(sid)
    copied_packet = PACKET_OUT / packet.name
    shutil.copy2(packet, copied_packet)
    pdf, matched_stem, pdf_root = find_pdf(sid)
    copied_pdf = ""
    pdf_sha = ""
    pdf_bytes = ""
    if pdf:
        dest = PDF_OUT / f"{matched_stem}.pdf"
        if not dest.exists() or sha256(dest) != sha256(pdf):
            shutil.copy2(pdf, dest)
        copied_pdf = str(dest.relative_to(PACKAGE))
        pdf_sha = sha256(dest)
        pdf_bytes = str(dest.stat().st_size)
    manifest_rows.append({
        "study_id": sid,
        "base_study_id": base,
        "source_packet_file": str(copied_packet.relative_to(PACKAGE)),
        "source_packet_sha256": sha256(copied_packet),
        "source_packet_bytes": str(copied_packet.stat().st_size),
        "pdf_found": "true" if pdf else "false",
        "pdf_matched_stem": matched_stem,
        "pdf_file": copied_pdf,
        "pdf_sha256": pdf_sha,
        "pdf_bytes": pdf_bytes,
        "pdf_source_root": pdf_root,
        "notes": "canonical_private_reference_package_for_human_and_ai_source_review",
    })
    if sid != base or matched_stem != sid:
        alias_rows.append({
            "analysis_study_id": sid,
            "base_study_id": base,
            "pdf_matched_stem": matched_stem,
            "source_packet_matched_stem": sid,
            "notes": "analysis split/sample suffix maps to base study PDF when needed",
        })

for fn in REVIEW_FILES:
    src = AI_TRACE_DIR / fn
    if src.exists():
        shutil.copy2(src, REVIEW_OUT / fn)

write_csv(
    MANIFEST_OUT / "paper_a_source_reference_package_manifest_20260614.csv",
    manifest_rows,
    ["study_id", "base_study_id", "source_packet_file", "source_packet_sha256", "source_packet_bytes", "pdf_found", "pdf_matched_stem", "pdf_file", "pdf_sha256", "pdf_bytes", "pdf_source_root", "notes"],
)
write_csv(
    MANIFEST_OUT / "paper_a_source_reference_package_alias_manifest_20260614.csv",
    alias_rows,
    ["analysis_study_id", "base_study_id", "pdf_matched_stem", "source_packet_matched_stem", "notes"],
)

readme = f"""# Paper A Private Source Reference Package

Date: 2026-06-14

This private package is the canonical local source universe for Paper A human review and AI source-trace work.

## Boundary

- Private/local package. Do not commit PDFs or source packets to Git.
- AI traces remain `candidate_only` until human confirmation.
- Paper B frozen human reference is not modified by this package.

## Contents

- `pdfs/`: copied local PDFs matched by study/base-study ID.
- `source_packets/`: copied source packets from the full-coverage source-rendering set.
- `review_inputs/`: current AI candidate-only source-trace review packet and human confirmation template.
- `manifests/paper_a_source_reference_package_manifest_20260614.csv`: checksums and source roots.
- `manifests/paper_a_source_reference_package_alias_manifest_20260614.csv`: split/sample ID mappings such as `S121-1 -> S121.pdf`.

## Counts

- Source packets copied: {len(packet_files)}
- PDFs found/copied: {sum(r['pdf_found'] == 'true' for r in manifest_rows)}
- Missing PDFs: {sum(r['pdf_found'] != 'true' for r in manifest_rows)}
- Alias rows: {len(alias_rows)}

## Use

Use this folder as the single starting point for human source review and AI source tracing. If a script needs source text or PDFs, point it here first instead of mixed OneDrive/R1/R2/R3/R4 paths.
"""
(PACKAGE / "README.md").write_text(readme, encoding="utf-8")
print(readme)
