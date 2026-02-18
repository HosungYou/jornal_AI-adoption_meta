"""Tests for scripts/screening/ai_screening.py"""

import sys
import pytest
import pandas as pd
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts" / "screening"))

from ai_screening import (
    try_extract_json,
    normalize_decision,
    consensus,
    prepare_record_id,
    build_prompt,
    SCREENING_PROMPT,
)


# ---------------------------------------------------------------------------
# try_extract_json
# ---------------------------------------------------------------------------

def test_try_extract_json_clean():
    """Valid JSON string parsed directly."""
    payload = '{"decision": "include", "confidence": 0.9}'
    result = try_extract_json(payload)
    assert result["decision"] == "include"
    assert result["confidence"] == 0.9


def test_try_extract_json_codeblock():
    """JSON inside ```json ... ``` fences extracted correctly."""
    text = '```json\n{"decision": "exclude", "confidence": 0.75}\n```'
    result = try_extract_json(text)
    assert result["decision"] == "exclude"
    assert result["confidence"] == 0.75


def test_try_extract_json_mixed():
    """JSON embedded in surrounding prose text extracted correctly."""
    text = 'Here is my analysis: {"decision": "uncertain", "confidence": 0.5} end of response.'
    result = try_extract_json(text)
    assert result["decision"] == "uncertain"


def test_try_extract_json_empty():
    """Empty string must raise ValueError."""
    with pytest.raises(ValueError, match="Empty model output"):
        try_extract_json("")


def test_try_extract_json_no_json():
    """Text with no JSON object must raise ValueError."""
    with pytest.raises(ValueError, match="No JSON object found"):
        try_extract_json("This is plain text with no JSON whatsoever.")


# ---------------------------------------------------------------------------
# normalize_decision
# ---------------------------------------------------------------------------

def test_normalize_decision_include():
    assert normalize_decision("include") == "include"


def test_normalize_decision_included():
    assert normalize_decision("included") == "include"


def test_normalize_decision_include_mixed_case():
    assert normalize_decision("INCLUDE") == "include"


def test_normalize_decision_exclude():
    assert normalize_decision("exclude") == "exclude"


def test_normalize_decision_excluded():
    assert normalize_decision("excluded") == "exclude"


def test_normalize_decision_unknown():
    assert normalize_decision("maybe") == "uncertain"


def test_normalize_decision_empty():
    assert normalize_decision("") == "uncertain"


# ---------------------------------------------------------------------------
# consensus
# ---------------------------------------------------------------------------

def test_consensus_both_include():
    assert consensus("include", "include") == "include"


def test_consensus_both_exclude():
    assert consensus("exclude", "exclude") == "exclude"


def test_consensus_conflict_include_exclude():
    assert consensus("include", "exclude") == "conflict"


def test_consensus_conflict_exclude_include():
    assert consensus("exclude", "include") == "conflict"


def test_consensus_conflict_uncertain():
    assert consensus("include", "uncertain") == "conflict"


# ---------------------------------------------------------------------------
# prepare_record_id
# ---------------------------------------------------------------------------

def test_prepare_record_id_adds_when_missing():
    """record_id column inserted at position 0 when absent."""
    df = pd.DataFrame({"title": ["A", "B", "C"]})
    result = prepare_record_id(df)
    assert "record_id" in result.columns
    assert list(result["record_id"]) == [1, 2, 3]
    assert result.columns[0] == "record_id"


def test_prepare_record_id_preserves_existing():
    """Existing record_id column not altered."""
    df = pd.DataFrame({"record_id": [10, 20], "title": ["A", "B"]})
    result = prepare_record_id(df)
    assert list(result["record_id"]) == [10, 20]


# ---------------------------------------------------------------------------
# build_prompt
# ---------------------------------------------------------------------------

def test_build_prompt_contains_title_and_abstract():
    """Prompt must embed the title and abstract from the row."""
    row = pd.Series({
        "title": "AI acceptance in universities",
        "abstract": "This study examines TAM in higher education.",
        "keywords": "AI; TAM; education",
        "year": "2023",
        "search_source": "WoS",
    })
    prompt = build_prompt(row)
    assert "AI acceptance in universities" in prompt
    assert "This study examines TAM in higher education." in prompt


def test_build_prompt_uses_source_database_fallback():
    """When search_source absent, source_database is used instead."""
    row = pd.Series({
        "title": "Some study",
        "abstract": "Abstract text",
        "keywords": "",
        "year": "2022",
        "source_database": "Scopus",
    })
    prompt = build_prompt(row)
    assert "Scopus" in prompt


def test_build_prompt_returns_string():
    row = pd.Series({"title": "T", "abstract": "A", "keywords": "", "year": "", "search_source": ""})
    assert isinstance(build_prompt(row), str)
