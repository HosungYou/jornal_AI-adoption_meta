# Systematic Literature Search Execution Guide

**Project:** AI Adoption in Education Meta-Analysis (MASEM)
**Date:** 2026-02-17
**Time Span:** January 2015 - December 2025
**Target:** 7 databases

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
| 4 | PsycINFO | pending | - | - | - |
| 5 | ACM DL | pending | - | - | - |
| 6 | ERIC | pending | - | - | - |
| 7 | Education Source | pending | - | - | - |
| | **Total (before dedup)** | **14,421+** | | | |

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

## Database 4: PsycINFO (via EBSCO)

**URL:** Via institutional EBSCO portal
**Status:** PENDING

### Query (v3, EBSCO Advanced Search - 4 rows)
```
Row 1 (TX All Text):
"artificial intelligence" OR "AI" OR "machine learning" OR "deep learning" OR "intelligent tutoring system" OR "ITS" OR "chatbot" OR "generative AI" OR "ChatGPT" OR "GPT-4" OR "GPT" OR "large language model" OR "LLM" OR "natural language processing" OR "automated grading" OR "adaptive learning" OR "conversational AI" OR "AI tutor" OR "AI agent" OR "agentic AI"

Row 2 (AND):
"higher education" OR university OR "post-secondary" OR "tertiary education" OR college OR undergraduate OR "graduate student" OR faculty OR professor OR instructor

Row 3 (AND):
adoption OR acceptance OR intention OR TAM OR UTAUT OR "technology acceptance" OR "user acceptance" OR "behavioral intention" OR "perceived usefulness" OR "perceived ease of use" OR "self-efficacy"

Row 4 (AND):
survey OR questionnaire OR "structural equation" OR SEM OR correlation OR "path analysis" OR regression OR "factor analysis" OR "meta-analysis" OR MASEM
```

### Limiters
- Publication Date: January 2015 - December 2025
- Language: English
- Source Types: Academic Journals
- Export: RIS format → `PsycINFO_export_YYYYMMDD.ris`

---

## Database 5: ACM Digital Library

**URL:** https://dl.acm.org/
**Status:** PENDING

### Query (v3, Advanced Search)
```
[[All: "artificial intelligence"] OR [All: "machine learning"] OR [All: "deep learning"] OR [All: "intelligent tutoring system"] OR [All: "chatbot"] OR [All: "generative ai"] OR [All: "chatgpt"] OR [All: "large language model"] OR [All: "LLM"] OR [All: "adaptive learning"] OR [All: "conversational AI"] OR [All: "AI agent"]] AND [[All: "higher education"] OR [All: university] OR [All: college] OR [All: undergraduate] OR [All: "graduate student"] OR [All: faculty] OR [All: professor]] AND [[All: adoption] OR [All: acceptance] OR [All: intention] OR [All: TAM] OR [All: UTAUT] OR [All: "technology acceptance"] OR [All: "behavioral intention"] OR [All: "perceived usefulness"] OR [All: survey] OR [All: questionnaire] OR [All: "structural equation"] OR [All: SEM]]
```
- Published Between: January 2015 - December 2025
- Export: BibTeX → `ACM_export_YYYYMMDD.bib`

---

## Database 6: ERIC

**URL:** https://eric.ed.gov/
**Status:** PENDING

### Query (v3, Boolean/Phrase)
```
("artificial intelligence" OR "AI" OR "machine learning" OR "deep learning" OR "intelligent tutoring system" OR "chatbot" OR "generative AI" OR "ChatGPT" OR "GPT" OR "large language model" OR "LLM" OR "adaptive learning" OR "conversational AI" OR "AI agent" OR "agentic AI") AND ("higher education" OR university OR college OR undergraduate OR "graduate student" OR faculty OR professor) AND (adoption OR acceptance OR intention OR TAM OR UTAUT OR "technology acceptance" OR "behavioral intention" OR "perceived usefulness" OR "perceived ease of use" OR "self-efficacy") AND (survey OR questionnaire OR "structural equation" OR SEM OR "path analysis" OR regression)
```
- Since 2015, Peer Reviewed, Journal Articles
- Export: CSV → `ERIC_export_YYYYMMDD.csv`

---

## Database 7: Education Source (via EBSCO)

**URL:** Via institutional EBSCO portal
**Status:** PENDING

Same 4-row query as PsycINFO above. Select "Education Source" database in EBSCO.
- Limiters: 2015-2025, English, Academic Journals, Peer Reviewed
- Export: RIS → `EduSource_export_YYYYMMDD.ris`

---

## Post-Search Steps

### 1. Deduplication
```bash
# All exports placed in:
/tmp/jornal_AI-adoption_meta/data/raw/search_results/

# Python/R deduplication:
# - Merge all exports
# - Remove duplicates by DOI and title similarity
# - Generate deduplicated master list
```

### 2. AI-Assisted Screening
```bash
# Title/Abstract screening with multi-model consensus
```

### 3. PRISMA Flow Diagram Data
Record numbers for PRISMA 2020 flow diagram at each stage.

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v1 | 2026-02-17 | Initial 3-cluster broad query |
| v2 | 2026-02-17 | +8 AI terms (Cluster 1), +6 TAM/UTAUT constructs (Cluster 3) |
| **v3 (EXECUTED)** | **2026-02-17** | **Narrowed to higher education (Cluster 2), removed broad words (Cluster 3), added quantitative methodology filter (Cluster 4), added article type filter (Cluster 5)** |

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

---

## Troubleshooting

**Q: Too many results in a database?**
- All 5 clusters are already applied. Check that Article type filter is active.

**Q: IEEE results much larger than WoS/Scopus?**
- IEEE "All Metadata" searches full text including references. This is expected. Deduplication will remove overlaps.

**Q: Institutional access not working?**
- Use university VPN or library portal proxy (ezproxy).
