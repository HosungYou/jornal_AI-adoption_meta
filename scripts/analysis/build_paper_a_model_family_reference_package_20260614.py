#!/usr/bin/env python3
"""Build a copyright-safe source reference package for Paper A model-family MASEM.

The package stores original metadata endpoints and machine-readable citation
records, not copyrighted article full text. For each reference, the script tries
to collect Crossref JSON and DOI BibTeX through official DOI/Crossref routes.
"""

from __future__ import annotations

import csv
import json
import re
import shutil
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
SOURCE_CSV = REPO_ROOT / "paper_a" / "analysis_strategy" / "PAPER_A_MODEL_FAMILY_MASEM_REFERENCE_BANK_20260614.csv"
OUT_DIR = REPO_ROOT / "references" / "paper_a_model_family_masem_20260614"
ONEDRIVE_DIR = Path("/Users/newhosung/Library/CloudStorage/OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity/AI Adoption Meta Analysis - Documents/Meta/AI Adoption/04_analysis_strategy/Paper_A/2026-06-14_model_family_masem/references")
USER_AGENT = "journal-ai-adoption-meta-reference-packager/20260614 (metadata-only; mailto:not-provided@example.com)"


def safe_slug(text: str, fallback: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "_", text).strip("_")
    text = re.sub(r"_+", "_", text)
    return text[:90] or fallback


def doi_from_url(value: str) -> str:
    value = (value or "").strip()
    if not value:
        return ""
    m = re.match(r"https?://(?:dx\.)?doi\.org/(.+)$", value, flags=re.I)
    if m:
        return urllib.parse.unquote(m.group(1).strip())
    if value.lower().startswith("doi:"):
        return value[4:].strip()
    if re.match(r"^10\.\S+/.+", value):
        return value
    return ""


def first_author_year(citation: str) -> str:
    author = citation.split(",", 1)[0].strip() or "reference"
    year = "nodate"
    m = re.search(r"\((\d{4})\)", citation)
    if m:
        year = m.group(1)
    return f"{author}_{year}"


def fetch_url(url: str, accept: str = "application/json", timeout: int = 12) -> tuple[bool, str, str]:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": accept})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            data = response.read().decode("utf-8", errors="replace")
            final_url = response.geturl()
        return True, data, final_url
    except (urllib.error.URLError, TimeoutError, ValueError) as exc:
        return False, str(exc), ""


def strip_abstracts(value):
    if isinstance(value, dict):
        return {k: strip_abstracts(v) for k, v in value.items() if k.lower() != "abstract"}
    if isinstance(value, list):
        return [strip_abstracts(v) for v in value]
    return value


def fallback_bibtex(row: dict[str, str], key: str, doi: str) -> str:
    title = row["citation"].replace("\n", " ").strip()
    url = row["doi_or_url"].strip()
    fields = [f"  title = {{{title}}}"]
    if doi:
        fields.append(f"  doi = {{{doi}}}")
    if url:
        fields.append(f"  url = {{{url}}}")
    fields.append("  note = {Fallback metadata generated from project reference bank; verify before final bibliography}")
    return "@misc{" + key + ",\n" + ",\n".join(fields) + "\n}\n"


def md_escape(text: str) -> str:
    return (text or "").replace("|", "\\|").replace("\n", " ")


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    rows = list(csv.DictReader(SOURCE_CSV.open(newline="", encoding="utf-8")))
    manifest_rows: list[dict[str, str]] = []
    combined_bib: list[str] = []

    for idx, row in enumerate(rows, start=1):
        citation = row["citation"].strip()
        doi = doi_from_url(row.get("doi_or_url", ""))
        category = safe_slug(row.get("category", "uncategorized"), "uncategorized")
        base_slug = safe_slug(first_author_year(citation), f"ref_{idx:03d}")
        slug = f"{idx:03d}_{base_slug}"
        ref_dir = OUT_DIR / category / slug
        ref_dir.mkdir(parents=True, exist_ok=True)

        key = safe_slug(base_slug, f"ref_{idx:03d}")
        landing_url = f"https://doi.org/{doi}" if doi else row.get("doi_or_url", "").strip()
        (ref_dir / "doi.txt").write_text((doi + "\n") if doi else "", encoding="utf-8")
        (ref_dir / "landing_page.url").write_text(landing_url + "\n", encoding="utf-8")
        (ref_dir / "project_reference_row.json").write_text(json.dumps(row, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

        crossref_ok = False
        crossref_final = ""
        crossref_note = "no_doi"
        if doi:
            encoded = urllib.parse.quote(doi, safe="")
            ok, payload, final_url = fetch_url(f"https://api.crossref.org/works/{encoded}", accept="application/json")
            crossref_ok = ok
            crossref_final = final_url
            crossref_note = "ok" if ok else payload[:300]
            if ok:
                try:
                    parsed = json.loads(payload)
                    parsed = strip_abstracts(parsed)
                    payload = json.dumps(parsed, ensure_ascii=False, indent=2)
                except json.JSONDecodeError:
                    pass
            (ref_dir / "crossref.json").write_text(payload + "\n", encoding="utf-8")
            time.sleep(0.08)

        bib_ok = False
        bib_final = ""
        bib_note = "no_doi"
        if doi:
            ok, payload, final_url = fetch_url(f"https://doi.org/{urllib.parse.quote(doi, safe='/')}", accept="application/x-bibtex")
            bib_ok = ok and payload.lstrip().startswith("@")
            bib_final = final_url
            bib_note = "ok" if bib_ok else payload[:300]
            bibtex = payload if bib_ok else fallback_bibtex(row, key, doi)
        else:
            bibtex = fallback_bibtex(row, key, doi)
        if not bibtex.endswith("\n"):
            bibtex += "\n"
        (ref_dir / "citation.bib").write_text(bibtex, encoding="utf-8")
        combined_bib.append(bibtex)

        readme = f"""# Reference {idx:03d}: {citation}

Category: {row.get('category','')}
Model family: {row.get('model_family','')}
Status: {row.get('status','')}

## Source pointers

- DOI: {doi or 'not available'}
- Landing page: {landing_url or 'not available'}
- Crossref metadata: {'collected' if crossref_ok else 'not collected'}
- DOI BibTeX: {'collected' if bib_ok else 'fallback generated from project reference bank'}

## Paper A use

{row.get('use_in_paper','')}

## Note

{row.get('note','')}

## Copyright boundary

This folder stores citation metadata and official source pointers only. It does not store copyrighted article full text unless a future researcher explicitly adds an open-license file after checking rights.
"""
        (ref_dir / "README.md").write_text(readme, encoding="utf-8")

        manifest_rows.append({
            "index": str(idx),
            "category": row.get("category", ""),
            "model_family": row.get("model_family", ""),
            "citation": citation,
            "doi": doi,
            "landing_url": landing_url,
            "status": row.get("status", ""),
            "reference_dir": str(ref_dir.relative_to(REPO_ROOT)),
            "crossref_ok": str(crossref_ok).lower(),
            "crossref_note": crossref_note,
            "bibtex_ok": str(bib_ok).lower(),
            "bibtex_note": bib_note,
        })

    with (OUT_DIR / "MANIFEST.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(manifest_rows[0].keys()))
        writer.writeheader()
        writer.writerows(manifest_rows)

    (OUT_DIR / "all_references.bib").write_text("\n".join(combined_bib), encoding="utf-8")

    core_rows = [r for r in manifest_rows if r["status"] == "core"]
    readme_lines = [
        "# Paper A model-family MASEM reference package",
        "",
        "Date: 2026-06-14",
        "",
        "This folder is a copyright-safe reference source package for the Paper A model-family MASEM route.",
        "It stores DOI/Crossref/BibTeX metadata and official landing-page pointers, not copyrighted full text.",
        "Crossref `abstract` fields are intentionally stripped before storage.",
        "",
        "## Contents",
        "",
        f"- Total references: {len(manifest_rows)}",
        f"- Core references: {len(core_rows)}",
        "- Combined BibTeX: `all_references.bib`",
        "- Machine manifest: `MANIFEST.csv`",
        "",
        "## Core references",
        "",
        "| # | Category | Citation | DOI/URL |",
        "| ---: | --- | --- | --- |",
    ]
    for r in core_rows:
        readme_lines.append(f"| {r['index']} | {md_escape(r['category'])} | {md_escape(r['citation'])} | {md_escape(r['landing_url'])} |")
    readme_lines.extend([
        "",
        "## Use rule",
        "",
        "Use this package as the source-citation backbone for Paper A Methods, Results, and reviewer-defense text.",
        "Before final submission, verify publisher metadata and target-journal bibliography style against the final manuscript manager.",
    ])
    (OUT_DIR / "README.md").write_text("\n".join(readme_lines) + "\n", encoding="utf-8")

    if ONEDRIVE_DIR.exists():
        shutil.rmtree(ONEDRIVE_DIR)
    shutil.copytree(OUT_DIR, ONEDRIVE_DIR)

    print(f"references={len(manifest_rows)}")
    print(f"core_references={len(core_rows)}")
    print(f"out_dir={OUT_DIR}")
    print(f"onedrive_dir={ONEDRIVE_DIR}")


if __name__ == "__main__":
    main()
