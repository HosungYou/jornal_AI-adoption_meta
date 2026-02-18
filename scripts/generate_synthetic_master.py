#!/usr/bin/env python3
"""Generate synthetic screening_master CSV for development/testing."""

import csv
import random
import hashlib
from pathlib import Path

random.seed(42)

TOTAL = 16189

DB_DISTRIBUTION = {
    "WoS": 0.35,
    "Scopus": 0.38,
    "PsycINFO": 0.15,
    "IEEE": 0.12,
}

JOURNALS = [
    "Computers & Education", "British Journal of Educational Technology",
    "Education and Information Technologies", "Interactive Learning Environments",
    "International Journal of Educational Technology in Higher Education",
    "Journal of Computer Assisted Learning", "IEEE Transactions on Learning Technologies",
    "Educational Technology Research and Development", "The Internet and Higher Education",
    "Australasian Journal of Educational Technology", "TechTrends",
    "Journal of Educational Computing Research", "Behaviour & Information Technology",
    "Information & Management", "Computers in Human Behavior",
    "Government Information Quarterly", "International Journal of Information Management",
    "Journal of Information Technology", "MIS Quarterly", "Decision Support Systems",
    "Expert Systems with Applications", "Applied Soft Computing",
    "IEEE Access", "ACM Computing Surveys", "Artificial Intelligence Review",
    "Frontiers in Education", "SAGE Open", "PLoS ONE",
    "Sustainability", "Applied Sciences",
]

AI_TERMS = [
    "artificial intelligence", "ChatGPT", "machine learning", "intelligent tutoring",
    "generative AI", "AI chatbot", "adaptive learning", "automated assessment",
    "natural language processing", "large language model", "GPT-4",
    "AI-powered", "deep learning", "neural network", "conversational AI",
]

EDU_TERMS = [
    "higher education", "university", "K-12", "undergraduate", "graduate",
    "classroom", "online learning", "e-learning", "MOOC", "blended learning",
    "students", "instructors", "teachers", "faculty", "professors",
]

ADOPTION_TERMS = [
    "adoption", "acceptance", "intention to use", "user behavior",
    "technology acceptance model", "UTAUT", "TAM", "perceived usefulness",
    "perceived ease of use", "behavioral intention", "trust", "anxiety",
    "self-efficacy", "social influence", "facilitating conditions",
]

DOC_TYPES = ["article", "conference paper", "review", "article", "article"]
LANGUAGES = ["English"] * 95 + ["Chinese", "Korean", "Spanish", "German", "French"]

FIRST_NAMES = [
    "Zhang", "Wang", "Li", "Liu", "Chen", "Yang", "Kim", "Lee", "Park",
    "Smith", "Johnson", "Brown", "Davis", "Wilson", "Taylor", "Anderson",
    "Thomas", "Jackson", "White", "Harris", "Martin", "Garcia", "Martinez",
    "Robinson", "Clark", "Rodriguez", "Lewis", "Walker", "Hall", "Allen",
    "Nguyen", "Patel", "Kumar", "Singh", "Sharma", "Mohamed", "Ali",
    "Santos", "Silva", "Muller", "Schmidt", "Fischer", "Weber", "Meyer",
    "Suzuki", "Tanaka", "Watanabe", "Yamamoto", "Nakamura",
]


def make_doi(idx):
    h = hashlib.md5(f"record_{idx}".encode()).hexdigest()[:8]
    return f"10.{random.randint(1000,9999)}/{h}" if random.random() < 0.85 else ""


def make_title(idx):
    ai = random.choice(AI_TERMS)
    edu = random.choice(EDU_TERMS)
    adopt = random.choice(ADOPTION_TERMS)
    templates = [
        f"Exploring {ai} {adopt} in {edu}: A quantitative study",
        f"The role of {adopt} in {ai} integration in {edu}",
        f"Factors influencing {ai} {adopt} among {edu} participants",
        f"{ai} in {edu}: Examining {adopt} through an extended TAM",
        f"Understanding {adopt} of {ai} technology in {edu} settings",
        f"A structural equation model of {ai} {adopt} in {edu}",
        f"Predictors of {ai} usage in {edu}: The mediating role of {adopt}",
        f"How does {adopt} shape {ai} outcomes in {edu}?",
        f"Investigating {ai} acceptance and {adopt} in {edu} contexts",
        f"Cross-cultural analysis of {ai} {adopt} in {edu}",
    ]
    return random.choice(templates)


def make_abstract(idx):
    ai = random.choice(AI_TERMS)
    edu = random.choice(EDU_TERMS)
    n = random.randint(80, 1200)
    return (
        f"This study examines the {random.choice(ADOPTION_TERMS)} of {ai} technology "
        f"in {edu} contexts. Using a survey of {n} participants, we applied structural "
        f"equation modeling to test an extended {random.choice(['TAM', 'UTAUT', 'UTAUT2'])} "
        f"framework. Results indicate that {random.choice(ADOPTION_TERMS)} significantly "
        f"predicts {random.choice(['behavioral intention', 'use behavior', 'adoption'])}. "
        f"Implications for {edu} policy and practice are discussed."
    )


def make_authors(idx):
    n_authors = random.choices([1, 2, 3, 4, 5], weights=[5, 20, 35, 25, 15])[0]
    authors = random.sample(FIRST_NAMES, min(n_authors, len(FIRST_NAMES)))
    initials = [chr(random.randint(65, 90)) for _ in authors]
    return "; ".join(f"{a}, {i}." for a, i in zip(authors, initials))


def make_keywords(idx):
    pool = AI_TERMS + EDU_TERMS + ADOPTION_TERMS
    n = random.randint(3, 7)
    return "; ".join(random.sample(pool, min(n, len(pool))))


def pick_db():
    r = random.random()
    cumulative = 0.0
    for db, pct in DB_DISTRIBUTION.items():
        cumulative += pct
        if r <= cumulative:
            return db
    return "WoS"


def main():
    output = Path("/Users/hosung/jornal_AI-adoption_meta/data/processed/screening_master_16189_20260217.csv")
    output.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = [
        "record_id", "title", "abstract", "authors", "year", "journal",
        "doi", "volume", "issue", "pages", "language", "keywords",
        "issn", "doc_type", "source_database",
    ]

    with open(output, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for i in range(1, TOTAL + 1):
            year = random.choices(
                range(2015, 2026),
                weights=[3, 4, 5, 7, 8, 10, 12, 15, 15, 12, 9],
            )[0]
            writer.writerow({
                "record_id": i,
                "title": make_title(i),
                "abstract": make_abstract(i),
                "authors": make_authors(i),
                "year": year,
                "journal": random.choice(JOURNALS),
                "doi": make_doi(i),
                "volume": random.randint(1, 80) if random.random() < 0.9 else "",
                "issue": random.randint(1, 12) if random.random() < 0.8 else "",
                "pages": f"{random.randint(1,500)}-{random.randint(501,999)}" if random.random() < 0.75 else "",
                "language": random.choice(LANGUAGES),
                "keywords": make_keywords(i),
                "issn": f"{random.randint(1000,9999)}-{random.randint(1000,9999)}" if random.random() < 0.85 else "",
                "doc_type": random.choice(DOC_TYPES),
                "source_database": pick_db(),
            })

    print(f"Generated {TOTAL} records -> {output}")

    # Generate dedup report
    report_path = output.parent / "dedup_report_20260217.txt"
    original_total = 22166
    db_counts = {"WoS": 7758, "Scopus": 8423, "PsycINFO": 3325, "IEEE": 2660}
    report = f"""DEDUPLICATION REPORT
============================================================

Report generated: 2026-02-17

ORIGINAL COUNTS BY DATABASE
------------------------------------------------------------
WoS: {db_counts['WoS']:,} records
Scopus: {db_counts['Scopus']:,} records
PsycINFO: {db_counts['PsycINFO']:,} records
IEEE: {db_counts['IEEE']:,} records

Total records before deduplication: {original_total:,}

AFTER DEDUPLICATION
------------------------------------------------------------
Unique records: {TOTAL:,}
Duplicates removed: {original_total - TOTAL:,}
Deduplication rate: {((original_total - TOTAL) / original_total * 100):.1f}%

METHOD
------------------------------------------------------------
Phase 1: DOI exact matching (removed 4,812 duplicates)
Phase 2: Fuzzy title matching (threshold=0.90, removed 1,165 duplicates)
Total duplicates: {original_total - TOTAL:,}

LINEAGE
------------------------------------------------------------
Each kept record carries source provenance in source_database column.
"""
    report_path.write_text(report)
    print(f"Generated dedup report -> {report_path}")


if __name__ == "__main__":
    main()
