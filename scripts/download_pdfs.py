#!/usr/bin/env python3
"""
PDF Downloader for Meta-Analysis Studies
Uses Unpaywall + Semantic Scholar + OpenAlex (all free/legal OA APIs)
Output: S001.pdf, S002.pdf, ... in data/02_screening/pdfs/
"""

import csv
import json
import os
import re
import sys
import time
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.parse import quote

# ── Config ──
PROJECT_ROOT = Path(__file__).parent.parent
INCLUDES_CSV = PROJECT_ROOT / "data/02_screening/confirmed_includes.csv"
PDF_DIR = PROJECT_ROOT / "data/02_screening/pdfs"
LOG_FILE = PROJECT_ROOT / "data/02_screening/pdf_download_log.json"
EMAIL = "hosung@psu.edu"
MAX_WORKERS = 5
TIMEOUT = 30

PDF_DIR.mkdir(parents=True, exist_ok=True)

SESSION = requests.Session()
SESSION.headers.update({
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
    "Accept": "application/pdf,*/*",
})


def extract_doi(doi_url: str) -> str | None:
    if not doi_url:
        return None
    m = re.search(r'(10\.\d{4,}/[^\s]+)', doi_url)
    if m:
        return m.group(1).rstrip('.')
    return None


def try_unpaywall(doi: str) -> str | None:
    url = f"https://api.unpaywall.org/v2/{quote(doi, safe='')}?email={EMAIL}"
    try:
        r = SESSION.get(url, timeout=TIMEOUT)
        if r.status_code != 200:
            return None
        data = r.json()
        best = data.get("best_oa_location")
        if best and best.get("url_for_pdf"):
            return best["url_for_pdf"]
        for loc in data.get("oa_locations", []):
            if loc.get("url_for_pdf"):
                return loc["url_for_pdf"]
    except Exception:
        pass
    return None


def try_semantic_scholar(doi: str) -> str | None:
    url = f"https://api.semanticscholar.org/graph/v1/paper/DOI:{quote(doi, safe='')}?fields=openAccessPdf"
    try:
        r = SESSION.get(url, timeout=TIMEOUT)
        if r.status_code != 200:
            return None
        data = r.json()
        oa = data.get("openAccessPdf")
        if oa and oa.get("url"):
            return oa["url"]
    except Exception:
        pass
    return None


def try_openalex(doi: str) -> str | None:
    url = f"https://api.openalex.org/works/doi:{quote(doi, safe='')}?select=open_access,primary_location"
    try:
        r = SESSION.get(url, timeout=TIMEOUT,
                        headers={"User-Agent": f"mailto:{EMAIL}"})
        if r.status_code != 200:
            return None
        data = r.json()
        oa = data.get("open_access", {})
        if oa.get("oa_url"):
            oa_url = oa["oa_url"]
            if oa_url.endswith(".pdf"):
                return oa_url
        loc = data.get("primary_location", {})
        if loc and loc.get("pdf_url"):
            return loc["pdf_url"]
    except Exception:
        pass
    return None


def download_pdf(pdf_url: str, filepath: Path) -> bool:
    try:
        r = SESSION.get(pdf_url, timeout=60, allow_redirects=True, stream=True)
        if r.status_code != 200:
            return False

        content_type = r.headers.get("Content-Type", "")
        data = r.content

        if len(data) < 1000:
            return False
        if not data[:5].startswith(b'%PDF') and 'pdf' not in content_type.lower():
            if b'<html' in data[:500].lower() or b'<!doctype' in data[:500].lower():
                return False

        filepath.write_bytes(data)
        return True
    except Exception:
        return False


def process_study(idx: int, record: dict) -> dict:
    study_id = f"S{idx:03d}"
    filepath = PDF_DIR / f"{study_id}.pdf"
    doi = extract_doi(record['doi_url'])

    result = {
        "study_id": study_id,
        "record_id": record["record_id"],
        "doi": doi,
        "status": "failed",
        "source": None,
        "pdf_url": None,
    }

    if not doi:
        result["status"] = "no_doi"
        print(f"  [{study_id}] No DOI — skipped")
        return result

    if filepath.exists() and filepath.stat().st_size > 10000:
        result["status"] = "already_exists"
        print(f"  [{study_id}] Already exists — skipped")
        return result

    # Try APIs in order
    pdf_url = None
    source = None

    for api_name, api_func in [
        ("unpaywall", try_unpaywall),
        ("semantic_scholar", try_semantic_scholar),
        ("openalex", try_openalex),
    ]:
        pdf_url = api_func(doi)
        if pdf_url:
            source = api_name
            break
        time.sleep(0.15)

    if not pdf_url:
        result["status"] = "no_oa"
        print(f"  [{study_id}] {record['record_id']} — No OA PDF found")
        return result

    result["pdf_url"] = pdf_url
    result["source"] = source

    success = download_pdf(pdf_url, filepath)
    if success:
        size_kb = filepath.stat().st_size / 1024
        result["status"] = "downloaded"
        print(f"  [{study_id}] Downloaded ({size_kb:.0f} KB) via {source}")
    else:
        result["status"] = "download_failed"
        print(f"  [{study_id}] Download failed from {source}")

    return result


def main():
    with open(INCLUDES_CSV, 'r') as f:
        studies = list(csv.DictReader(f))

    studies.sort(key=lambda x: (-int(x['year']), x['record_id']))

    print(f"PDF Download — {len(studies)} studies")
    print(f"Output: {PDF_DIR}")
    print(f"APIs: Unpaywall → Semantic Scholar → OpenAlex")
    print("=" * 60)

    results = []

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {
            executor.submit(process_study, i + 1, study): i
            for i, study in enumerate(studies)
        }
        for future in as_completed(futures):
            results.append(future.result())

    results.sort(key=lambda x: x['study_id'])

    with open(LOG_FILE, 'w') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    from collections import Counter
    status_counts = Counter(r['status'] for r in results)
    print("\n" + "=" * 60)
    print("Summary:")
    for status, count in status_counts.most_common():
        print(f"  {status}: {count}")
    print(f"\nLog: {LOG_FILE}")


if __name__ == "__main__":
    main()
