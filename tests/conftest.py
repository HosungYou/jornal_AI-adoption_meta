import pytest
import pandas as pd
import tempfile
from pathlib import Path

@pytest.fixture
def project_root():
    return Path("/Users/hosung/jornal_AI-adoption_meta")

@pytest.fixture
def sample_screening_csv(tmp_path):
    """Create a small screening CSV with 10 records for testing."""
    records = []
    for i in range(1, 11):
        db = ["WoS", "Scopus", "PsycINFO", "IEEE"][i % 4]
        records.append({
            "record_id": i,
            "title": f"Test study {i} on AI adoption in education",
            "abstract": f"Abstract for study {i} examining AI technology acceptance.",
            "authors": f"Author{i}, A.; Coauthor{i}, B.",
            "year": 2020 + (i % 6),
            "journal": f"Journal of Test {i}",
            "doi": f"10.1234/test{i:04d}" if i <= 8 else "",
            "volume": str(i),
            "issue": str(i % 4 + 1),
            "pages": f"{i*10}-{i*10+15}",
            "language": "English",
            "keywords": "AI; education; adoption",
            "issn": f"1234-{5000+i}",
            "doc_type": "article",
            "source_database": db,
        })
    df = pd.DataFrame(records)
    path = tmp_path / "test_screening.csv"
    df.to_csv(path, index=False)
    return path

@pytest.fixture
def sample_ai_results_csv(tmp_path):
    """Create a sample AI screening results CSV."""
    records = []
    for i in range(1, 11):
        records.append({
            "record_id": i,
            "title": f"Test study {i}",
            "year": 2020 + (i % 6),
            "search_source": ["WoS", "Scopus", "PsycINFO", "IEEE"][i % 4],
            "screen_decision_codex": "include" if i % 3 != 0 else "exclude",
            "screen_confidence_codex": 0.85 + (i % 10) * 0.01,
            "exclude_code_codex": "NA" if i % 3 != 0 else "E4",
            "rationale_codex": f"Codex rationale for {i}",
            "screen_decision_gemini": "include" if i % 4 != 0 else "exclude",
            "screen_confidence_gemini": 0.80 + (i % 10) * 0.01,
            "exclude_code_gemini": "NA" if i % 4 != 0 else "E3",
            "rationale_gemini": f"Gemini rationale for {i}",
            "screen_consensus": "include" if (i % 3 != 0 and i % 4 != 0) else ("exclude" if (i % 3 == 0 and i % 4 == 0) else "conflict"),
            "oauth_auth_method_codex": "oauth",
            "oauth_auth_method_gemini": "oauth",
            "human1_decision": "",
            "human2_decision": "",
            "adjudicated_final_decision": "",
            "exclude_code": "",
            "decision_rationale": "",
            "adjudicator_id": "",
        })
    df = pd.DataFrame(records)
    path = tmp_path / "test_ai_results.csv"
    df.to_csv(path, index=False)
    return path
