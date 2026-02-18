#!/usr/bin/env python3
"""
Standardize column names across database exports, merge, and deduplicate.
Produces a unified CSV ready for screening (AI or Rayyan import).

Databases handled: WoS (XLS), Scopus (CSV), IEEE (CSV), PsycINFO/ProQuest (CSV)
"""

import pandas as pd
import numpy as np
from pathlib import Path
from difflib import SequenceMatcher
import logging
import re
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent.parent.parent
RAW_DIR = BASE_DIR / "data" / "raw" / "search_results"
OUTPUT_DIR = BASE_DIR / "data" / "processed"


def load_wos(directory: Path) -> pd.DataFrame:
    """Load and standardize Web of Science XLS files."""
    xls_files = sorted(directory.glob("*.xls"))
    if not xls_files:
        logger.warning("No WoS XLS files found")
        return pd.DataFrame()

    dfs = []
    for f in xls_files:
        df = pd.read_excel(f)
        dfs.append(df)
        logger.info(f"  WoS: loaded {len(df)} records from {f.name}")

    combined = pd.concat(dfs, ignore_index=True)

    standardized = pd.DataFrame({
        'title': combined.get('Article Title', combined.get('Title', '')),
        'abstract': combined.get('Abstract', ''),
        'authors': combined.get('Authors', combined.get('Author Full Names', '')),
        'year': combined.get('Publication Year', ''),
        'journal': combined.get('Source Title', ''),
        'doi': combined.get('DOI', ''),
        'volume': combined.get('Volume', ''),
        'issue': combined.get('Issue', ''),
        'pages': combined.get('Start Page', '').astype(str) + '-' + combined.get('End Page', '').astype(str),
        'language': combined.get('Language', ''),
        'keywords': combined.get('Author Keywords', ''),
        'issn': combined.get('ISSN', ''),
        'doc_type': combined.get('Document Type', ''),
        'source_database': 'WoS'
    })

    logger.info(f"WoS: {len(standardized)} records standardized")
    return standardized


def load_scopus(filepath: Path) -> pd.DataFrame:
    """Load and standardize Scopus CSV."""
    df = pd.read_csv(filepath)

    standardized = pd.DataFrame({
        'title': df.get('Title', ''),
        'abstract': df.get('Abstract', ''),
        'authors': df.get('Authors', ''),
        'year': df.get('Year', ''),
        'journal': df.get('Source title', ''),
        'doi': df.get('DOI', ''),
        'volume': df.get('Volume', ''),
        'issue': df.get('Issue', ''),
        'pages': df.get('Page start', '').astype(str) + '-' + df.get('Page end', '').astype(str),
        'language': df.get('Language of Original Document', ''),
        'keywords': df.get('Author Keywords', ''),
        'issn': df.get('ISSN', ''),
        'doc_type': df.get('Document Type', ''),
        'source_database': 'Scopus'
    })

    logger.info(f"Scopus: {len(standardized)} records standardized")
    return standardized


def load_ieee(filepath: Path) -> pd.DataFrame:
    """Load and standardize IEEE CSV."""
    df = pd.read_csv(filepath)

    standardized = pd.DataFrame({
        'title': df.get('Document Title', ''),
        'abstract': df.get('Abstract', ''),
        'authors': df.get('Authors', ''),
        'year': df.get('Publication Year', ''),
        'journal': df.get('Publication Title', ''),
        'doi': df.get('DOI', ''),
        'volume': df.get('Volume', ''),
        'issue': df.get('Issue', ''),
        'pages': df.get('Start Page', '').astype(str) + '-' + df.get('End Page', '').astype(str),
        'language': '',
        'keywords': df.get('Author Keywords', ''),
        'issn': df.get('ISSN', ''),
        'doc_type': 'Article',
        'source_database': 'IEEE'
    })

    logger.info(f"IEEE: {len(standardized)} records standardized")
    return standardized


def load_psycinfo(filepath: Path) -> pd.DataFrame:
    """Load and standardize PsycINFO/ProQuest CSV."""
    df = pd.read_csv(filepath)

    # Extract year from PubDate
    year = df.get('PubDate', df.get('AlphaDate', '')).astype(str)
    year = year.apply(lambda x: re.search(r'(20\d{2})', str(x)).group(1)
                      if re.search(r'(20\d{2})', str(x)) else '')

    standardized = pd.DataFrame({
        'title': df.get('Title', ''),
        'abstract': df.get('Abstract', ''),
        'authors': df.get('Author', ''),
        'year': year,
        'journal': df.get('Publication', ''),
        'doi': df.get('DOI', ''),
        'volume': df.get('Volume', ''),
        'issue': df.get('Issue', ''),
        'pages': df.get('StartPage', df.get('PageRange', '')).astype(str),
        'language': df.get('Language', ''),
        'keywords': '',
        'issn': df.get('ISSN', ''),
        'doc_type': df.get('SourceType', ''),
        'source_database': 'PsycINFO'
    })

    logger.info(f"PsycINFO: {len(standardized)} records standardized")
    return standardized


def normalize_doi(doi_val) -> str:
    """Normalize DOI for comparison."""
    if pd.isna(doi_val) or str(doi_val).strip() == '':
        return ''
    doi = str(doi_val).strip().lower()
    doi = re.sub(r'^https?://doi\.org/', '', doi)
    doi = re.sub(r'^doi:\s*', '', doi)
    return doi


def normalize_title(title: str) -> str:
    """Normalize title for fuzzy comparison."""
    if pd.isna(title):
        return ''
    t = str(title).lower()
    t = ''.join(c if c.isalnum() or c.isspace() else ' ' for c in t)
    t = ' '.join(t.split())
    return t


def deduplicate(df: pd.DataFrame, title_threshold: float = 0.90) -> pd.DataFrame:
    """Two-pass deduplication: exact DOI match, then fuzzy title match."""
    logger.info(f"=== DEDUPLICATION START: {len(df)} records ===")

    # Normalize DOIs
    df['doi_norm'] = df['doi'].apply(normalize_doi)

    # --- Pass 1: DOI dedup ---
    has_doi = df[df['doi_norm'] != ''].copy()
    no_doi = df[df['doi_norm'] == ''].copy()

    before = len(has_doi)
    # Keep first occurrence, but track which databases contributed
    doi_groups = has_doi.groupby('doi_norm')
    keep_rows = []
    for doi_val, group in doi_groups:
        first = group.iloc[0].copy()
        if len(group) > 1:
            first['source_database'] = '; '.join(group['source_database'].unique())
        keep_rows.append(first)

    has_doi_dedup = pd.DataFrame(keep_rows)
    doi_dupes = before - len(has_doi_dedup)
    logger.info(f"Pass 1 (DOI): removed {doi_dupes} duplicates ({before} -> {len(has_doi_dedup)})")

    combined = pd.concat([has_doi_dedup, no_doi], ignore_index=True)

    # --- Pass 2: Fuzzy title dedup ---
    combined['title_norm'] = combined['title'].apply(normalize_title)

    keep_mask = [True] * len(combined)
    title_dupes = 0

    # Group by first 30 chars of normalized title to reduce O(n^2) comparisons
    combined['title_prefix'] = combined['title_norm'].str[:30]

    for prefix, group in combined.groupby('title_prefix'):
        if len(group) < 2:
            continue
        indices = group.index.tolist()
        for i_pos, i in enumerate(indices):
            if not keep_mask[i]:
                continue
            for j in indices[i_pos + 1:]:
                if not keep_mask[j]:
                    continue
                sim = SequenceMatcher(None, combined.at[i, 'title_norm'],
                                      combined.at[j, 'title_norm']).ratio()
                if sim >= title_threshold:
                    keep_mask[j] = False
                    title_dupes += 1
                    # Merge source databases
                    src_i = combined.at[i, 'source_database']
                    src_j = combined.at[j, 'source_database']
                    if src_j not in src_i:
                        combined.at[i, 'source_database'] = f"{src_i}; {src_j}"

    logger.info(f"Pass 2 (Title): removed {title_dupes} fuzzy duplicates")

    deduped = combined[keep_mask].drop(columns=['doi_norm', 'title_norm', 'title_prefix']).reset_index(drop=True)
    logger.info(f"=== DEDUPLICATION COMPLETE: {len(deduped)} unique records ===")

    return deduped, doi_dupes, title_dupes


def generate_report(original_counts: dict, final_df: pd.DataFrame,
                    doi_dupes: int, title_dupes: int, output_path: Path):
    """Generate PRISMA-compatible deduplication report."""
    total_original = sum(original_counts.values())
    total_removed = total_original - len(final_df)

    lines = [
        "=" * 70,
        "DEDUPLICATION REPORT — AI Adoption in Education MASEM",
        "=" * 70,
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "IDENTIFICATION (PRISMA 2020 Box 1)",
        "-" * 70,
        "Records identified from databases:",
    ]

    for db, count in original_counts.items():
        lines.append(f"  {db:.<30} {count:>6,}")

    lines.extend([
        f"  {'TOTAL':.<30} {total_original:>6,}",
        "",
        "DUPLICATE REMOVAL",
        "-" * 70,
        f"  DOI exact match duplicates:    {doi_dupes:>6,}",
        f"  Fuzzy title duplicates:        {title_dupes:>6,}",
        f"  Total duplicates removed:      {total_removed:>6,}",
        f"  Deduplication rate:            {total_removed / total_original * 100:>5.1f}%",
        "",
        "RECORDS AFTER DEDUPLICATION",
        "-" * 70,
        f"  Unique records for screening:  {len(final_df):>6,}",
        "",
        "SOURCE DISTRIBUTION (after dedup)",
        "-" * 70,
    ])

    # Count unique sources (some records have multiple sources)
    for db in original_counts.keys():
        count = final_df['source_database'].str.contains(db).sum()
        lines.append(f"  Records contributed by {db:.<20} {count:>6,}")

    lines.extend([
        "",
        "RECORDS WITH MISSING DATA",
        "-" * 70,
        f"  Missing DOI:                   {(final_df['doi'].isna() | (final_df['doi'] == '')).sum():>6,}",
        f"  Missing abstract:              {(final_df['abstract'].isna() | (final_df['abstract'] == '')).sum():>6,}",
        f"  Missing year:                  {(final_df['year'].isna() | (final_df['year'] == '')).sum():>6,}",
        "",
        "=" * 70,
    ])

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w') as f:
        f.write('\n'.join(lines))

    logger.info(f"Report saved: {output_path}")


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # --- Load all databases ---
    logger.info("Loading database exports...")

    wos_df = load_wos(RAW_DIR / "wos")
    scopus_df = load_scopus(next((RAW_DIR / "scopus").glob("*.csv")))
    ieee_df = load_ieee(next((RAW_DIR / "ieee").glob("*.csv")))
    psycinfo_df = load_psycinfo(next((RAW_DIR / "psycinfo").glob("*.csv")))

    original_counts = {
        'WoS': len(wos_df),
        'Scopus': len(scopus_df),
        'IEEE': len(ieee_df),
        'PsycINFO': len(psycinfo_df),
    }

    # --- Merge ---
    merged = pd.concat([wos_df, scopus_df, ieee_df, psycinfo_df], ignore_index=True)
    logger.info(f"Total merged: {len(merged)} records")

    # --- Save merged (pre-dedup) ---
    merged.to_csv(OUTPUT_DIR / "merged_all_databases.csv", index=False)

    # --- Deduplicate ---
    deduped, doi_dupes, title_dupes = deduplicate(merged)

    # --- Save deduplicated ---
    timestamp = datetime.now().strftime('%Y%m%d')
    dedup_path = OUTPUT_DIR / f"deduplicated_{len(deduped)}_{timestamp}.csv"
    deduped.to_csv(dedup_path, index=False)
    logger.info(f"Deduplicated file saved: {dedup_path}")

    # --- Generate report ---
    report_path = OUTPUT_DIR / f"dedup_report_{timestamp}.txt"
    generate_report(original_counts, deduped, doi_dupes, title_dupes, report_path)

    # --- Summary ---
    total = sum(original_counts.values())
    logger.info(f"\n{'='*50}")
    logger.info(f"SUMMARY")
    logger.info(f"  Total records:     {total:,}")
    logger.info(f"  Duplicates removed: {total - len(deduped):,}")
    logger.info(f"  Unique records:    {len(deduped):,}")
    logger.info(f"  Ready for screening: {dedup_path}")
    logger.info(f"{'='*50}")


if __name__ == "__main__":
    main()
