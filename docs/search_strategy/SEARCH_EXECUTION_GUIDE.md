# Systematic Literature Search Execution Guide

**Project:** AI Adoption in Education Meta-Analysis (MASEM)
**Date:** 2026-02-17
**Time Span:** January 2015 - December 2025
**Target:** 4 databases

---

## OAuth Setup for AI Screening

Run these once per session before AI-assisted screening:

```bash
# Codex CLI OAuth login (OpenAI)
codex --login
codex exec "Say OK."

# Gemini CLI OAuth login (Google)
gemini auth login
gemini -p "Say OK."
```

If these checks fail, refresh login before batch screening.

---

## Five Concept Clusters (Executed Query) — v3 (2026-02-17)

```
Cluster 1 - AI Technology (20 terms, unchanged from v2):
("artificial intelligence" OR "AI" OR "machine learning" OR "deep learning" OR "intelligent tutoring system" OR "ITS" OR "chatbot" OR "generative AI" OR "ChatGPT" OR "GPT-4" OR "GPT" OR "large language model" OR "LLM" OR "natural language processing" OR "automated grading" OR "adaptive learning" OR "conversational AI" OR "AI tutor" OR "AI agent" OR "agentic AI")

Cluster 2 - Higher Education Context (10 terms — narrowed from broad "education"):
("higher education" OR university OR "post-secondary" OR "tertiary education" OR college OR undergraduate OR "graduate student" OR faculty OR professor OR instructor*)

Cluster 3 - Adoption/Acceptance (11 terms — refined, broad words removed):
(adoption OR acceptance OR intention OR TAM OR UTAUT OR "technology acceptance" OR "user acceptance" OR "behavioral intention" OR "perceived usefulness" OR "perceived ease of use" OR "self-efficacy")

Cluster 4 - Quantitative Methodology (10 terms — NEW):
(survey OR questionnaire OR "structural equation" OR SEM OR correlation OR "path analysis" OR regression OR "factor analysis" OR "meta-analysis" OR MASEM)

Cluster 5 - Article Type Filter:
  WoS: DT=(Article)
  Scopus: DOCTYPE(ar)
  IEEE: Content Type → Journals

Combined: Cluster 1 AND Cluster 2 AND Cluster 3 AND Cluster 4 AND Cluster 5
Date Range: 2015-01-01 to 2025-12-31
```

### v3 Changes from v2
- **Cluster 2:** Narrowed from broad education terms (education*, student*, teacher*, learning, pedagogy, classroom, university, "higher education", "K-12", academic) to **higher education only** (removed K-12, pedagogy, classroom, added post-secondary, tertiary, undergraduate, graduate student, faculty, professor)
- **Cluster 3:** Removed broad single words (trust, resistance, behavior, attitude, usage) that inflated results
- **Cluster 4:** Added quantitative methodology filter to target MASEM-relevant studies
- **Cluster 5:** Added article type filter to exclude reviews, conference abstracts, etc.
- **Impact:** WoS reduced from 247,087 → 6,897; maintained high relevance

---

## Executed Search Results Summary

| # | Database | Hits | Export Format | Export Files | Date |
|---|----------|:----:|:------------:|-------------|------|
| 1 | Web of Science | 6,897 | Excel (.xls) | WoS_1-1000 through WoS_6001-6897 (7 files) | 2026-02-17 |
| 2 | Scopus | 7,363 | CSV | Scopus_7363_20250217.csv | 2026-02-17 |
| 3 | IEEE Xplore | 161 | CSV | IEEE_161_20260217.csv | 2026-02-17 |
| 4 | PsycINFO (via ProQuest) | 7,745 | CSV | PsycINFO_7745_20260217.csv | 2026-02-17 |
| 5 | ACM DL | SKIPPED | - | - | - |
| 6 | ERIC | SKIPPED | - | - | - |
| 7 | Education Source | SKIPPED | - | - | - |
| | **Total (before dedup)** | **22,166** | | | |
| | **After deduplication** | **16,189** | | | |

---

## Database 1: Web of Science Core Collection

**URL:** https://www.webofscience.com/
**Status:** COMPLETED (2026-02-17)

### Executed Query (v3)
```
TS=("artificial intelligence" OR "AI" OR "machine learning" OR "deep learning" OR "intelligent tutoring system" OR "ITS" OR "chatbot" OR "generative AI" OR "ChatGPT" OR "GPT-4" OR "GPT" OR "large language model" OR "LLM" OR "natural language processing" OR "automated grading" OR "adaptive learning" OR "conversational AI" OR "AI tutor" OR "AI agent" OR "agentic AI") AND TS=("higher education" OR university OR "post-secondary" OR "tertiary education" OR college OR undergraduate OR "graduate student" OR faculty OR professor OR instructor*) AND TS=(adoption OR acceptance OR intention OR TAM OR UTAUT OR "technology acceptance" OR "user acceptance" OR "behavioral intention" OR "perceived usefulness" OR "perceived ease of use" OR "self-efficacy") AND TS=(survey OR questionnaire OR "structural equation" OR SEM OR correlation OR "path analysis" OR regression OR "factor analysis" OR "meta-analysis" OR MASEM) AND DT=(Article)
```

> `TS` = Topic (Title, Abstract, Author Keywords, Keywords Plus)
> Timespan: 2015-01-01 ~ 2025-12-31
> Result: **6,897 records**

### Export Details
- Format: Excel (.xls), Full Record
- Batch size: 1,000 records per file
- Files: 7 batches (WoS_1-1000 through WoS_6001-6897)
- Location: `data/raw/search_results/wos/`

---

## Database 2: Scopus

**URL:** https://www.scopus.com/
**Status:** COMPLETED (2026-02-17)

### Executed Query (v3)
```
TITLE-ABS-KEY("artificial intelligence" OR "AI" OR "machine learning" OR "deep learning" OR "intelligent tutoring system" OR "ITS" OR "chatbot" OR "generative AI" OR "ChatGPT" OR "GPT-4" OR "GPT" OR "large language model" OR "LLM" OR "natural language processing" OR "automated grading" OR "adaptive learning" OR "conversational AI" OR "AI tutor" OR "AI agent" OR "agentic AI") AND TITLE-ABS-KEY("higher education" OR university OR "post-secondary" OR "tertiary education" OR college OR undergraduate OR "graduate student" OR faculty OR professor OR instructor) AND TITLE-ABS-KEY(adoption OR acceptance OR intention OR TAM OR UTAUT OR "technology acceptance" OR "user acceptance" OR "behavioral intention" OR "perceived usefulness" OR "perceived ease of use" OR "self-efficacy") AND TITLE-ABS-KEY(survey OR questionnaire OR "structural equation" OR SEM OR correlation OR "path analysis" OR regression OR "factor analysis" OR "meta-analysis" OR MASEM) AND DOCTYPE(ar) AND PUBYEAR > 2014 AND PUBYEAR < 2026
```

> `TITLE-ABS-KEY` = Title, Abstract, and Keywords
> Result: **7,363 records**

### Export Details
- Format: CSV, Full Record (Citation + Bibliographic + Abstract & Keywords)
- Files: 1 file (Scopus_7363_20250217.csv)
- Location: `data/raw/search_results/scopus/`

---

## Database 3: IEEE Xplore

**URL:** https://ieeexplore.ieee.org/
**Status:** COMPLETED (2026-02-17)

### Executed Query (v4, Command Search — Abstract field)
```
("Abstract":"artificial intelligence" OR "Abstract":"AI" OR "Abstract":"machine learning" OR "Abstract":"deep learning" OR "Abstract":"intelligent tutoring system" OR "Abstract":"chatbot" OR "Abstract":"generative AI" OR "Abstract":"ChatGPT" OR "Abstract":"GPT" OR "Abstract":"large language model" OR "Abstract":"LLM" OR "Abstract":"natural language processing" OR "Abstract":"adaptive learning" OR "Abstract":"conversational AI" OR "Abstract":"AI agent" OR "Abstract":"agentic AI") AND ("Abstract":"higher education" OR "Abstract":university OR "Abstract":"post-secondary" OR "Abstract":"tertiary education" OR "Abstract":college OR "Abstract":undergraduate OR "Abstract":"graduate student" OR "Abstract":faculty OR "Abstract":professor OR "Abstract":instructor) AND ("Abstract":adoption OR "Abstract":acceptance OR "Abstract":intention OR "Abstract":TAM OR "Abstract":UTAUT OR "Abstract":"technology acceptance" OR "Abstract":"behavioral intention" OR "Abstract":"perceived usefulness" OR "Abstract":"perceived ease of use" OR "Abstract":survey OR "Abstract":questionnaire OR "Abstract":"structural equation" OR "Abstract":SEM OR "Abstract":"path analysis" OR "Abstract":regression)
```

> Field: **Abstract** (changed from "All Metadata" which searched full text and inflated results to 20,846)
> Filters Applied: Journals, Year 2015-2025
> Result: **161 records**

### Export Details
- Format: CSV, Full Record (all 161 records in single file)
- Files: 1 file (IEEE_161_20260217.csv)
- Location: `data/raw/search_results/ieee/`

---

## Database 4: PsycINFO (via ProQuest)

**URL:** https://www.proquest.com/psycinfo/ (Penn State University Libraries)
**Status:** COMPLETED (2026-02-17)

> **Note:** Penn State provides PsycINFO via ProQuest, not EBSCO. The search was executed on ProQuest's APA PsycInfo® platform using Command Line mode.

### Executed Query (v3, ProQuest Command Line)
```
("artificial intelligence" OR "AI" OR "machine learning" OR "deep learning" OR "intelligent tutoring system" OR "ITS" OR "chatbot" OR "generative AI" OR "ChatGPT" OR "GPT-4" OR "GPT" OR "large language model" OR "LLM" OR "natural language processing" OR "automated grading" OR "adaptive learning" OR "conversational AI" OR "AI tutor" OR "AI agent" OR "agentic AI") AND ("higher education" OR university OR "post-secondary" OR "tertiary education" OR college OR undergraduate OR "graduate student" OR faculty OR professor OR instructor*) AND (adoption OR acceptance OR intention OR TAM OR UTAUT OR "technology acceptance" OR "user acceptance" OR "behavioral intention" OR "perceived usefulness" OR "perceived ease of use" OR "self-efficacy") AND (survey OR questionnaire OR "structural equation" OR SEM OR correlation OR "path analysis" OR regression OR "factor analysis" OR "meta-analysis" OR MASEM)
```

> Limiters: Peer reviewed, Date: January 2015 - December 2025
> Result: **7,745 records**

### Export Details
- Format: CSV (via ProQuest "Export Results" bulk export, includes abstracts)
- Fields: Title, Subtitle, Author, Publication, SourceType, Publisher, Volume, Issue, PubDate, AlphaDate, StartPage, EndPage, PageRange, ISSN, EISSN, ISBN, Language, Abstract, DocumentUrl, DOI
- Files: 1 file (PsycINFO_7745_20260217.csv)
- Location: `data/raw/search_results/psycinfo/`

---

## Database 5: ACM Digital Library

**URL:** https://dl.acm.org/
**Status:** SKIPPED — Sufficient coverage achieved from 4 databases (22,166 records, 16,189 after dedup)

### Query (v3, Advanced Search)
```
[[All: "artificial intelligence"] OR [All: "machine learning"] OR [All: "deep learning"] OR [All: "intelligent tutoring system"] OR [All: "chatbot"] OR [All: "generative ai"] OR [All: "chatgpt"] OR [All: "large language model"] OR [All: "LLM"] OR [All: "adaptive learning"] OR [All: "conversational AI"] OR [All: "AI agent"]] AND [[All: "higher education"] OR [All: university] OR [All: college] OR [All: undergraduate] OR [All: "graduate student"] OR [All: faculty] OR [All: professor]] AND [[All: adoption] OR [All: acceptance] OR [All: intention] OR [All: TAM] OR [All: UTAUT] OR [All: "technology acceptance"] OR [All: "behavioral intention"] OR [All: "perceived usefulness"] OR [All: survey] OR [All: questionnaire] OR [All: "structural equation"] OR [All: SEM]]
```
- Published Between: January 2015 - December 2025
- Export: BibTeX → `ACM_export_YYYYMMDD.bib`

**Note (2026-02-17):** ACM, ERIC, and Education Source were considered but excluded per Decision #50 in the decision log. The 4-DB set (WoS, Scopus, PsycINFO, IEEE) provides sufficient coverage for this study's scope.

---

## Database 6: ERIC

**URL:** https://eric.ed.gov/
**Status:** SKIPPED — Sufficient coverage achieved from 4 databases

### Query (v3, Boolean/Phrase)
```
("artificial intelligence" OR "AI" OR "machine learning" OR "deep learning" OR "intelligent tutoring system" OR "chatbot" OR "generative AI" OR "ChatGPT" OR "GPT" OR "large language model" OR "LLM" OR "adaptive learning" OR "conversational AI" OR "AI agent" OR "agentic AI") AND ("higher education" OR university OR college OR undergraduate OR "graduate student" OR faculty OR professor) AND (adoption OR acceptance OR intention OR TAM OR UTAUT OR "technology acceptance" OR "behavioral intention" OR "perceived usefulness" OR "perceived ease of use" OR "self-efficacy") AND (survey OR questionnaire OR "structural equation" OR SEM OR "path analysis" OR regression)
```
- Since 2015, Peer Reviewed, Journal Articles
- Export: CSV → `ERIC_export_YYYYMMDD.csv`

---

## Database 7: Education Source (via EBSCO)

**URL:** Via institutional EBSCO portal
**Status:** SKIPPED — Sufficient coverage achieved from 4 databases

Same 4-row query as PsycINFO above. Select "Education Source" database in EBSCO.
- Limiters: 2015-2025, English, Academic Journals, Peer Reviewed
- Export: RIS → `EduSource_export_YYYYMMDD.ris`

---

## Post-Search Steps

### 1. Deduplication — COMPLETED (2026-02-17)

**Script:** `scripts/screening/standardize_and_dedup.py`

**Process:**
1. Standardized column names across 4 databases (WoS XLS, Scopus CSV, IEEE CSV, PsycINFO CSV)
2. Pass 1: DOI exact match → removed 5,737 duplicates
3. Pass 2: Fuzzy title matching (90% threshold, prefix-grouped) → removed 240 duplicates

**Results:**
| Metric | Count |
|--------|------:|
| Total records (4 databases) | 22,166 |
| DOI duplicates removed | 5,737 |
| Title duplicates removed | 240 |
| **Unique records for screening** | **16,189** |
| Deduplication rate | 27.0% |
| Records with abstracts | 16,189 (100%) |
| Records with DOI | 15,380 (95.0%) |
| Multi-source records (overlap) | 5,078 |

**Output Files:**
- `data/processed/screening_master_16189_20260217.csv` — Final numbered dataset (REC_00001 ~ REC_16189)
- `data/processed/dedup_report_20260217.txt` — PRISMA-compatible deduplication report
- `data/processed/merged_all_databases.csv` — Pre-dedup merged file (22,166 records)

### 2. Next: Title/Abstract Screening (Phase 1)

**Input:** `screening_master_16189_20260217.csv` (16,189 records, REC_00001 ~ REC_16189)

**Tools available:**
- `scripts/screening/ai_screening.py` — Claude API-based screening
- Rayyan QCRI — Web-based collaborative human screening

### 3. PRISMA 2020 Flow Diagram Numbers

**Identification:**
- WoS: 6,897
- Scopus: 7,363
- IEEE Xplore: 161
- PsycINFO (ProQuest): 7,745
- Total identified: 22,166
- Duplicates removed: 5,977
- **Records screened: 16,189**

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v1 | 2026-02-17 | Initial 3-cluster broad query |
| v2 | 2026-02-17 | +8 AI terms (Cluster 1), +6 TAM/UTAUT constructs (Cluster 3) |
| **v3 (EXECUTED)** | **2026-02-17** | **Narrowed to higher education (Cluster 2), removed broad words (Cluster 3), added quantitative methodology filter (Cluster 4), added article type filter (Cluster 5)** |
| **v3 FINAL** | **2026-02-17** | **Search concluded at 4/7 databases (WoS, Scopus, IEEE, PsycINFO). ACM DL, ERIC, Education Source skipped — sufficient coverage with 22,166 raw / 16,189 unique records. Deduplication completed (27.0% rate). Screening master dataset generated: REC_00001 ~ REC_16189.** |

### Superseded v2 Queries (for reference)
<details>
<summary>Click to expand v2 queries (not executed)</summary>

**v2 WoS:**
```
TS=("artificial intelligence" OR "AI" OR "machine learning" OR "deep learning" OR "intelligent tutoring system" OR "ITS" OR "chatbot" OR "generative AI" OR "ChatGPT" OR "GPT-4" OR "GPT" OR "large language model" OR "LLM" OR "natural language processing" OR "automated grading" OR "adaptive learning" OR "conversational AI" OR "AI tutor" OR "AI agent" OR "agentic AI") AND TS=(education* OR student* OR instructor* OR teacher* OR learning OR pedagogy OR classroom OR university OR "higher education" OR "K-12" OR academic) AND TS=(adoption OR acceptance OR intention OR usage OR behavior OR attitude OR TAM OR UTAUT OR "technology acceptance" OR "user acceptance" OR "behavioral intention" OR "perceived usefulness" OR "perceived ease of use" OR "self-efficacy" OR trust OR resistance)
```

**v2 Scopus:**
```
TITLE-ABS-KEY("artificial intelligence" OR "AI" OR "machine learning" OR "deep learning" OR "intelligent tutoring system" OR "ITS" OR "chatbot" OR "generative AI" OR "ChatGPT" OR "GPT-4" OR "GPT" OR "large language model" OR "LLM" OR "natural language processing" OR "automated grading" OR "adaptive learning" OR "conversational AI" OR "AI tutor" OR "AI agent" OR "agentic AI") AND TITLE-ABS-KEY(education* OR student* OR instructor* OR teacher* OR learning OR pedagogy OR classroom OR university OR "higher education" OR "K-12" OR academic) AND TITLE-ABS-KEY(adoption OR acceptance OR intention OR usage OR behavior OR attitude OR TAM OR UTAUT OR "technology acceptance" OR "user acceptance" OR "behavioral intention" OR "perceived usefulness" OR "perceived ease of use" OR "self-efficacy" OR trust OR resistance) AND PUBYEAR > 2014 AND PUBYEAR < 2026
```
</details>

### 2. AI-Assisted Screening (Codex CLI + Gemini CLI)
```bash
python3 scripts/screening/ai_screening.py \
  data/processed/screening_master_16189_20260217.csv \
  data/01_extracted/screening_ai_dual.csv \
  --engine both \
  --auto-login \
  --save-every 50
```

### 3. PRISMA Flow Diagram Data
Record these numbers for the PRISMA 2020 flow diagram:
- Records identified from each database (4 numbers: WoS, Scopus, PsycINFO, IEEE)
- Total records before dedup
- Duplicates removed
- Records screened (title/abstract)
- Records excluded at screening
- Full-text articles assessed
- Full-text excluded (with reasons)
- Studies included in final synthesis

---

## Troubleshooting

**Q: Too many results in a database?**
- All 5 clusters are already applied. Check that Article type filter is active.

**Q: IEEE results much larger than WoS/Scopus?**
- IEEE "All Metadata" searches full text including references. This is expected. Deduplication will remove overlaps.

**Q: Institutional access not working?**
- Use university VPN or library portal proxy (ezproxy).
