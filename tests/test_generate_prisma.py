"""Tests for scripts/data_processing/generate_prisma.py"""

import sys
import json
import pytest
import pandas as pd
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts" / "data_processing"))

from generate_prisma import (
    counts_from_screening_csv,
    render_prisma_text,
    write_outputs,
    EXCLUDE_CODES,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_df(n_include=5, n_exclude=3, n_conflict=2, exclude_code="E1"):
    """Build a minimal screening DataFrame."""
    records = []
    for i in range(n_include):
        records.append({
            "adjudicated_final_decision": "include",
            "screen_consensus": "include",
            "screen_decision_codex": "include",
            "screen_decision_gemini": "include",
            "exclude_code": "NA",
        })
    for i in range(n_exclude):
        records.append({
            "adjudicated_final_decision": "exclude",
            "screen_consensus": "exclude",
            "screen_decision_codex": "exclude",
            "screen_decision_gemini": "exclude",
            "exclude_code": exclude_code,
        })
    for i in range(n_conflict):
        records.append({
            "adjudicated_final_decision": "",
            "screen_consensus": "conflict",
            "screen_decision_codex": "include",
            "screen_decision_gemini": "exclude",
            "exclude_code": "",
        })
    return pd.DataFrame(records)


# ---------------------------------------------------------------------------
# counts_from_screening_csv
# ---------------------------------------------------------------------------

def test_counts_basic():
    df = _make_df(n_include=5, n_exclude=3, n_conflict=2)
    counts = counts_from_screening_csv(df, identified_total=20, duplicates_removed=10)

    assert counts["identified_records"] == 20
    assert counts["duplicates_removed"] == 10
    assert counts["after_dedup"] == 10
    assert counts["screened_title_abstract"] == 10  # 5+3+2
    assert counts["included_for_extraction"] == 5
    assert counts["excluded_title_abstract_final"] == 3
    assert counts["ai_conflicts"] == 2


def test_counts_codex_gemini_excludes():
    df = _make_df(n_include=4, n_exclude=4, n_conflict=2)
    counts = counts_from_screening_csv(df, identified_total=15, duplicates_removed=5)
    # exclude group: both codex+gemini="exclude" (4 each)
    # conflict group: codex="include", gemini="exclude" (0 codex, 2 gemini)
    assert counts["codex_excluded_candidates"] == 4
    assert counts["gemini_excluded_candidates"] == 6


def test_counts_full_text_assessed():
    """full_text_assessed = included + unresolved (conflict rows)."""
    df = _make_df(n_include=6, n_exclude=2, n_conflict=2)
    counts = counts_from_screening_csv(df, identified_total=20, duplicates_removed=10)
    # unresolved = screened - human_excluded - included = 10 - 2 - 6 = 2
    assert counts["full_text_assessed"] == 6 + 2


# ---------------------------------------------------------------------------
# render_prisma_text
# ---------------------------------------------------------------------------

def test_render_prisma_text_key_sections():
    df = _make_df(n_include=5, n_exclude=3, n_conflict=2)
    counts = counts_from_screening_csv(df, identified_total=20, duplicates_removed=10)
    text = render_prisma_text(counts)

    assert "IDENTIFICATION" in text
    assert "TITLE/ABSTRACT SCREENING" in text
    assert "ELIGIBILITY" in text
    assert "EXCLUSION CODES" in text
    assert "Records identified: 20" in text
    assert "Duplicates removed: 10" in text


def test_render_prisma_text_is_string():
    df = _make_df()
    counts = counts_from_screening_csv(df, identified_total=10, duplicates_removed=0)
    assert isinstance(render_prisma_text(counts), str)


# ---------------------------------------------------------------------------
# write_outputs
# ---------------------------------------------------------------------------

def test_write_outputs_creates_three_files(tmp_path):
    df = _make_df(n_include=3, n_exclude=2, n_conflict=1)
    counts = counts_from_screening_csv(df, identified_total=10, duplicates_removed=4)
    prefix = tmp_path / "prisma_output"
    write_outputs(counts, prefix)

    assert prefix.with_suffix(".json").exists()
    assert prefix.with_suffix(".txt").exists()
    assert prefix.with_suffix(".csv").exists()


def test_write_outputs_json_content(tmp_path):
    df = _make_df(n_include=4, n_exclude=2, n_conflict=0)
    counts = counts_from_screening_csv(df, identified_total=12, duplicates_removed=6)
    prefix = tmp_path / "prisma"
    write_outputs(counts, prefix)

    data = json.loads(prefix.with_suffix(".json").read_text())
    assert data["identified_records"] == 12
    assert data["duplicates_removed"] == 6
    assert "exclude_code_counts" in data


def test_write_outputs_csv_content(tmp_path):
    df = _make_df()
    counts = counts_from_screening_csv(df, identified_total=10, duplicates_removed=0)
    prefix = tmp_path / "prisma"
    write_outputs(counts, prefix)

    result_df = pd.read_csv(prefix.with_suffix(".csv"))
    assert "Stage" in result_df.columns
    assert "Metric" in result_df.columns
    assert "Count" in result_df.columns
    # Identification rows present
    assert "Identification" in result_df["Stage"].values


# ---------------------------------------------------------------------------
# exclude_code_counts
# ---------------------------------------------------------------------------

def test_exclude_code_counts_per_code():
    """Each EXCLUDE_CODE should be counted independently."""
    records = []
    for code in ["E1", "E1", "E2", "E3"]:
        records.append({
            "adjudicated_final_decision": "exclude",
            "screen_consensus": "exclude",
            "screen_decision_codex": "exclude",
            "screen_decision_gemini": "exclude",
            "exclude_code": code,
        })
    df = pd.DataFrame(records)
    counts = counts_from_screening_csv(df, identified_total=10, duplicates_removed=6)
    ecc = counts["exclude_code_counts"]
    assert ecc["E1"] == 2
    assert ecc["E2"] == 1
    assert ecc["E3"] == 1
    assert ecc["E4"] == 0


def test_all_exclude_codes_present_in_counts():
    df = _make_df()
    counts = counts_from_screening_csv(df, identified_total=10, duplicates_removed=0)
    for code in EXCLUDE_CODES:
        assert code in counts["exclude_code_counts"]
