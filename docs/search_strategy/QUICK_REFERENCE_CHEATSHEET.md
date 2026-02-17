# Quick Reference Cheat Sheet — v3 EXECUTED

**Project:** AI Adoption in Education MASEM | **Date Range:** 2015-2025
**Executed:** 2026-02-17 | **5-Cluster Query** | Higher Education Focus

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

## DB4: PsycINFO (EBSCO, 4 rows) — PENDING

**Row 1 (TX All Text):** `"artificial intelligence" OR "AI" OR "machine learning" OR "deep learning" OR "intelligent tutoring system" OR "ITS" OR "chatbot" OR "generative AI" OR "ChatGPT" OR "GPT-4" OR "GPT" OR "large language model" OR "LLM" OR "natural language processing" OR "automated grading" OR "adaptive learning" OR "conversational AI" OR "AI tutor" OR "AI agent" OR "agentic AI"`

**Row 2 (AND):** `"higher education" OR university OR "post-secondary" OR "tertiary education" OR college OR undergraduate OR "graduate student" OR faculty OR professor OR instructor`

**Row 3 (AND):** `adoption OR acceptance OR intention OR TAM OR UTAUT OR "technology acceptance" OR "user acceptance" OR "behavioral intention" OR "perceived usefulness" OR "perceived ease of use" OR "self-efficacy"`

**Row 4 (AND):** `survey OR questionnaire OR "structural equation" OR SEM OR correlation OR "path analysis" OR regression OR "factor analysis" OR "meta-analysis" OR MASEM`

- Limiters: 2015-2025, English, Academic Journals
- Export: RIS

---

## DB5: ACM Digital Library — PENDING

**Field 1 (Anywhere):** `"artificial intelligence" OR "machine learning" OR "deep learning" OR "intelligent tutoring system" OR "chatbot" OR "generative AI" OR "ChatGPT" OR "large language model" OR "adaptive learning" OR "conversational AI" OR "AI agent"`

**AND Field 2:** `"higher education" OR university OR college OR undergraduate OR "graduate student" OR faculty OR professor`

**AND Field 3:** `adoption OR acceptance OR intention OR TAM OR UTAUT OR "technology acceptance" OR "behavioral intention" OR "perceived usefulness" OR survey OR questionnaire OR "structural equation" OR SEM`

- 2015-2025, Export: BibTeX

---

## DB6: ERIC — PENDING

```
("artificial intelligence" OR "AI" OR "machine learning" OR "deep learning" OR "intelligent tutoring system" OR "chatbot" OR "generative AI" OR "ChatGPT" OR "GPT" OR "large language model" OR "LLM" OR "adaptive learning" OR "conversational AI" OR "AI agent" OR "agentic AI") AND ("higher education" OR university OR college OR undergraduate OR "graduate student" OR faculty OR professor) AND (adoption OR acceptance OR intention OR TAM OR UTAUT OR "technology acceptance" OR "behavioral intention" OR "perceived usefulness" OR "perceived ease of use" OR "self-efficacy") AND (survey OR questionnaire OR "structural equation" OR SEM OR "path analysis" OR regression)
```
- Since 2015, Peer Reviewed, Journal Articles
- Export: CSV

---

## DB7: Education Source (EBSCO) — PENDING

Same 4-row query as PsycINFO. Select "Education Source" database.
- Limiters: 2015-2025, English, Academic Journals, Peer Reviewed
- Export: RIS

---

## Results Log

| DB | Hits | Exported | File | Date |
|----|:----:|:--------:|------|------|
| Web of Science | 6,897 | 6,897 | 7x .xls | 2026-02-17 |
| Scopus | 7,363 | 7,363 | 1x .csv | 2026-02-17 |
| IEEE Xplore | 161 | 161 | 1x .csv | 2026-02-17 |
| PsycINFO | pending | - | - | - |
| ACM DL | pending | - | - | - |
| ERIC | pending | - | - | - |
| Education Source | pending | - | - | - |
| **TOTAL** | **14,421+** | | | |

---

## Export File Destination
```
/tmp/jornal_AI-adoption_meta/data/raw/search_results/
├── wos/          (7 .xls files)
├── scopus/       (1 .csv file)
├── ieee/         (pending)
├── psycinfo/     (pending)
├── acm/          (pending)
├── eric/         (pending)
└── edusource/    (pending)
```
