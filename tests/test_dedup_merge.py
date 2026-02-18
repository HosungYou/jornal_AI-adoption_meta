"""Tests for scripts/screening/dedup_merge.py"""

import sys
import pytest
import pandas as pd
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts" / "screening"))

from dedup_merge import RecordDeduplicator


# ---------------------------------------------------------------------------
# DOI deduplication
# ---------------------------------------------------------------------------

def test_doi_exact_dedup():
    """Duplicate DOIs should be collapsed to one record."""
    dedup = RecordDeduplicator()
    df = pd.DataFrame({
        "title": ["Study A", "Study A duplicate", "Study B"],
        "doi":   ["10.1234/aaa", "10.1234/aaa", "10.1234/bbb"],
    })
    result = dedup.deduplicate_by_doi(df)
    dois = result["doi"].tolist()
    assert len(result) == 2
    assert dois.count("10.1234/aaa") == 1
    assert "10.1234/bbb" in dois


def test_doi_exact_dedup_no_doi_rows_preserved():
    """Records without DOI must be preserved after DOI dedup."""
    dedup = RecordDeduplicator()
    df = pd.DataFrame({
        "title": ["Study A", "Study B (no doi)", "Study C (no doi)"],
        "doi":   ["10.1234/aaa", "", ""],
    })
    result = dedup.deduplicate_by_doi(df)
    # Study A + two no-doi rows = 3 kept
    assert len(result) == 3


# ---------------------------------------------------------------------------
# Fuzzy title deduplication
# ---------------------------------------------------------------------------

def test_fuzzy_title_dedup():
    """Titles with similarity >= 0.90 should be deduplicated."""
    dedup = RecordDeduplicator(title_similarity_threshold=0.90)
    # Construct a near-identical pair by changing one word
    base = "Examining AI adoption intention in higher education using TAM"
    near = "Examining AI adoption intention in higher education using TAM model"
    df = pd.DataFrame({"title": [base, near, "Completely different study on quantum computing"]})
    result = dedup.deduplicate_by_title(df)
    # The near-identical pair should collapse; unrelated title stays
    assert len(result) == 2


def test_fuzzy_title_below_threshold():
    """Titles with similarity < 0.90 should both be kept."""
    dedup = RecordDeduplicator(title_similarity_threshold=0.90)
    t1 = "Artificial intelligence in medical diagnosis"
    t2 = "Machine learning approaches for weather prediction"
    df = pd.DataFrame({"title": [t1, t2]})
    result = dedup.deduplicate_by_title(df)
    assert len(result) == 2


# ---------------------------------------------------------------------------
# Schema validation
# ---------------------------------------------------------------------------

def test_validate_schema_required():
    """Missing 'title' column must raise ValueError."""
    dedup = RecordDeduplicator()
    df = pd.DataFrame({"abstract": ["some text"]})
    with pytest.raises(ValueError, match="missing required columns"):
        dedup.validate_schema(df, "TestDB")


def test_validate_schema_optional():
    """Missing optional columns should be filled with empty string, not raise."""
    dedup = RecordDeduplicator()
    df = pd.DataFrame({"title": ["A study"]})
    dedup.validate_schema(df, "TestDB")  # must not raise
    for col in dedup.optional_columns:
        assert col in df.columns
        assert df[col].iloc[0] == ""


# ---------------------------------------------------------------------------
# merge_databases
# ---------------------------------------------------------------------------

def test_merge_databases(tmp_path):
    """merge_databases should combine CSVs and add source_database + lineage_ids."""
    df1 = pd.DataFrame({"title": ["Study A", "Study B"], "doi": ["10/a", "10/b"]})
    df2 = pd.DataFrame({"title": ["Study C"], "doi": ["10/c"]})
    p1 = tmp_path / "db1.csv"
    p2 = tmp_path / "db2.csv"
    df1.to_csv(p1, index=False)
    df2.to_csv(p2, index=False)

    dedup = RecordDeduplicator()
    merged = dedup.merge_databases([p1, p2], ["WoS", "Scopus"])

    assert len(merged) == 3
    assert "source_database" in merged.columns
    assert "lineage_ids" in merged.columns
    assert set(merged["source_database"].unique()) == {"WoS", "Scopus"}
    # Each lineage_id should contain the database name
    for _, row in merged.iterrows():
        assert row["lineage_ids"].startswith(row["source_database"])


# ---------------------------------------------------------------------------
# generate_dedup_report
# ---------------------------------------------------------------------------

def test_generate_dedup_report(tmp_path):
    """Report file should be created and contain key counts."""
    dedup = RecordDeduplicator()
    final_df = pd.DataFrame({
        "title": ["Study A", "Study B"],
        "source_database": ["WoS", "Scopus"],
    })
    original_counts = {"WoS": 5, "Scopus": 3}
    report_path = tmp_path / "report.txt"

    dedup.generate_dedup_report(original_counts, final_df, report_path)

    assert report_path.exists()
    content = report_path.read_text()
    assert "DEDUPLICATION REPORT" in content
    assert "WoS" in content
    assert "Scopus" in content
    # Total original = 8, final = 2, removed = 6
    assert "6" in content or "Duplicates removed" in content
