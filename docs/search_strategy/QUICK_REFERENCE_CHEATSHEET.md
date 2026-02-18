# Quick Reference Cheat Sheet — v3 FINAL

**Project:** AI Adoption in Education MASEM | **Date Range:** 2015-2025
**Search Completed:** 2026-02-17 | **5-Cluster Query** | Higher Education Focus
**Databases:** 4 of 7 searched (WoS, Scopus, IEEE, PsycINFO) | 3 skipped (ACM, ERIC, Education Source)
**Final Dataset:** 16,189 unique records (REC_00001 ~ REC_16189)

---

## Cluster Structure (v3)

| # | Cluster | Terms | Key Change from v2 |
|---|---------|:-----:|---------------------|
| 1 | AI Technology | 20 | Unchanged |
| 2 | Higher Education | 10 | Narrowed from broad "education" |
| 3 | Adoption/Acceptance | 11 | Removed: trust, resistance, behavior, attitude, usage |
| 4 | Quantitative Methods | 10 | NEW |
| 5 | Article Type | DB-specific | NEW |

---

## DB1: Web of Science — 6,897 hits

```
TS=("artificial intelligence" OR "AI" OR "machine learning" OR "deep learning" OR "intelligent tutoring system" OR "ITS" OR "chatbot" OR "generative AI" OR "ChatGPT" OR "GPT-4" OR "GPT" OR "large language model" OR "LLM" OR "natural language processing" OR "automated grading" OR "adaptive learning" OR "conversational AI" OR "AI tutor" OR "AI agent" OR "agentic AI") AND TS=("higher education" OR university OR "post-secondary" OR "tertiary education" OR college OR undergraduate OR "graduate student" OR faculty OR professor OR instructor*) AND TS=(adoption OR acceptance OR intention OR TAM OR UTAUT OR "technology acceptance" OR "user acceptance" OR "behavioral intention" OR "perceived usefulness" OR "perceived ease of use" OR "self-efficacy") AND TS=(survey OR questionnaire OR "structural equation" OR SEM OR correlation OR "path analysis" OR regression OR "factor analysis" OR "meta-analysis" OR MASEM) AND DT=(Article)
```
- Timespan: 2015-01-01 ~ 2025-12-31
- Export: Excel (.xls), Full Record, 1000/batch x 7 files

---

## DB2: Scopus — 7,363 hits

```
TITLE-ABS-KEY("artificial intelligence" OR "AI" OR "machine learning" OR "deep learning" OR "intelligent tutoring system" OR "ITS" OR "chatbot" OR "generative AI" OR "ChatGPT" OR "GPT-4" OR "GPT" OR "large language model" OR "LLM" OR "natural language processing" OR "automated grading" OR "adaptive learning" OR "conversational AI" OR "AI tutor" OR "AI agent" OR "agentic AI") AND TITLE-ABS-KEY("higher education" OR university OR "post-secondary" OR "tertiary education" OR college OR undergraduate OR "graduate student" OR faculty OR professor OR instructor) AND TITLE-ABS-KEY(adoption OR acceptance OR intention OR TAM OR UTAUT OR "technology acceptance" OR "user acceptance" OR "behavioral intention" OR "perceived usefulness" OR "perceived ease of use" OR "self-efficacy") AND TITLE-ABS-KEY(survey OR questionnaire OR "structural equation" OR SEM OR correlation OR "path analysis" OR regression OR "factor analysis" OR "meta-analysis" OR MASEM) AND DOCTYPE(ar) AND PUBYEAR > 2014 AND PUBYEAR < 2026
```
- Export: CSV, Full Record, single file

---

## DB3: IEEE Xplore — 161 hits

Command Search, **Abstract** field (not All Metadata), Journals only, 2015-2025:

```
("Abstract":"artificial intelligence" OR "Abstract":"AI" OR "Abstract":"machine learning" OR ... OR "Abstract":"agentic AI") AND ("Abstract":"higher education" OR "Abstract":university OR ... OR "Abstract":instructor) AND ("Abstract":adoption OR "Abstract":acceptance OR ... OR "Abstract":regression)
```

- Field changed from "All Metadata" (20,846) to "Abstract" (161) — matches WoS/Scopus scope
- Export: CSV, single file (161 records)

---

## DB4: PsycINFO (via ProQuest) — 7,745 hits

```
("artificial intelligence" OR "AI" OR "machine learning" OR "deep learning" OR "intelligent tutoring system" OR "ITS" OR "chatbot" OR "generative AI" OR "ChatGPT" OR "GPT-4" OR "GPT" OR "large language model" OR "LLM" OR "natural language processing" OR "automated grading" OR "adaptive learning" OR "conversational AI" OR "AI tutor" OR "AI agent" OR "agentic AI") AND ("higher education" OR university OR "post-secondary" OR "tertiary education" OR college OR undergraduate OR "graduate student" OR faculty OR professor OR instructor*) AND (adoption OR acceptance OR intention OR TAM OR UTAUT OR "technology acceptance" OR "user acceptance" OR "behavioral intention" OR "perceived usefulness" OR "perceived ease of use" OR "self-efficacy") AND (survey OR questionnaire OR "structural equation" OR SEM OR correlation OR "path analysis" OR regression OR "factor analysis" OR "meta-analysis" OR MASEM)
```

- Platform: ProQuest APA PsycInfo® (Penn State University Libraries)
- Limiters: Peer reviewed, 2015-2025
- Export: CSV with abstracts (bulk Export Results feature)

---

## DB5: ACM Digital Library — SKIPPED

Sufficient coverage from 4 databases (22,166 records before dedup).

---

## DB6: ERIC — SKIPPED

Sufficient coverage from 4 databases.

---

## DB7: Education Source (EBSCO) — SKIPPED

Sufficient coverage from 4 databases.

---

## Results Log

| DB | Hits | Exported | File | Date |
|----|:----:|:--------:|------|------|
| Web of Science | 6,897 | 6,897 | 7x .xls | 2026-02-17 |
| Scopus | 7,363 | 7,363 | 1x .csv | 2026-02-17 |
| IEEE Xplore | 161 | 161 | 1x .csv | 2026-02-17 |
| PsycINFO (ProQuest) | 7,745 | 7,745 | 1x .csv | 2026-02-17 |
| ACM DL | SKIPPED | - | - | - |
| ERIC | SKIPPED | - | - | - |
| Education Source | SKIPPED | - | - | - |
| **TOTAL (raw)** | **22,166** | **22,166** | | |
| **After dedup** | **16,189** | | `screening_master_16189_20260217.csv` | 2026-02-17 |

---

## File Structure
```
data/
├── raw/search_results/           # Raw database exports
│   ├── wos/                      (7 .xls files, 6,897 records)
│   ├── scopus/                   (1 .csv file, 7,363 records)
│   ├── ieee/                     (1 .csv file, 161 records)
│   └── psycinfo/                 (1 .csv file, 7,745 records)
└── processed/                    # Processed files
    ├── merged_all_databases.csv          (22,166 records, pre-dedup)
    ├── deduplicated_16189_20260217.csv   (16,189 records, post-dedup)
    ├── screening_master_16189_20260217.csv (16,189 records, REC_00001~REC_16189)
    └── dedup_report_20260217.txt         (PRISMA dedup report)
```

## Deduplication Summary
```
Total identified ............ 22,166
  DOI duplicates removed .... -5,737
  Title duplicates removed .. -  240
                              ------
Unique records .............. 16,189  (REC_00001 ~ REC_16189)
  Deduplication rate: 27.0%
  With abstract: 100%
  With DOI: 95.0%
```
