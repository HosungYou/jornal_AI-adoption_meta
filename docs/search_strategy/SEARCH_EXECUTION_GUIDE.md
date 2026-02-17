# Systematic Literature Search Execution Guide

**Project:** AI Adoption in Education Meta-Analysis (MASEM)
**Date:** 2026-02-17
**Time Span:** January 2015 - December 2025
**Target:** 7 databases

---

## Three Concept Clusters (Base Query)

```
Cluster 1 - AI Technology:
("artificial intelligence" OR "AI" OR "machine learning" OR "intelligent tutoring system" OR "ITS" OR "chatbot" OR "generative AI" OR "ChatGPT" OR "GPT-4" OR "natural language processing" OR "automated grading" OR "adaptive learning")

Cluster 2 - Educational Context:
(education* OR student* OR instructor* OR teacher* OR learning OR pedagogy OR classroom OR university OR "higher education" OR "K-12" OR academic)

Cluster 3 - Adoption/Acceptance:
(adoption OR acceptance OR intention OR usage OR behavior OR attitude OR TAM OR UTAUT OR "technology acceptance" OR "user acceptance")

Combined: Cluster 1 AND Cluster 2 AND Cluster 3
```

---

## Database 1: Web of Science Core Collection

**URL:** https://www.webofscience.com/

### Step-by-Step
1. Log in via institutional access
2. Click "Advanced Search"
3. Paste the query below
4. Set Timespan: 2015-01-01 to 2025-12-31
5. Select "Web of Science Core Collection" only
6. Click "Search"

### Query (Advanced Search)
```
TS=("artificial intelligence" OR "AI" OR "machine learning" OR "intelligent tutoring system" OR "ITS" OR "chatbot" OR "generative AI" OR "ChatGPT" OR "GPT-4" OR "natural language processing" OR "automated grading" OR "adaptive learning") AND TS=(education* OR student* OR instructor* OR teacher* OR learning OR pedagogy OR classroom OR university OR "higher education" OR "K-12" OR academic) AND TS=(adoption OR acceptance OR intention OR usage OR behavior OR attitude OR TAM OR UTAUT OR "technology acceptance" OR "user acceptance")
```

> `TS` = Topic (searches Title, Abstract, Author Keywords, Keywords Plus)

### Export Instructions
1. Select "Export" -> "Other File Formats"
2. Record Range: "All records" (or in batches of 1,000 if >1,000)
3. Record Content: "Full Record and Cited References"
4. File Format: **Tab-delimited (Win, UTF-8)** or **Plain Text**
5. Save as: `WoS_export_YYYYMMDD.txt`

### Alternative: If Advanced Search is not available
Use "Basic Search" with 3 separate rows:
- Row 1: Topic = `"artificial intelligence" OR "AI" OR "machine learning" OR "intelligent tutoring system" OR "chatbot" OR "generative AI" OR "ChatGPT" OR "GPT-4" OR "natural language processing" OR "automated grading" OR "adaptive learning"`
- Row 2 (AND): Topic = `education* OR student* OR instructor* OR teacher* OR learning OR pedagogy OR classroom OR university OR "higher education" OR "K-12" OR academic`
- Row 3 (AND): Topic = `adoption OR acceptance OR intention OR usage OR behavior OR attitude OR TAM OR UTAUT OR "technology acceptance" OR "user acceptance"`

---

## Database 2: Scopus

**URL:** https://www.scopus.com/

### Step-by-Step
1. Log in via institutional access
2. Click "Advanced document search"
3. Paste the query below
4. Click "Search"

### Query (Advanced Search)
```
TITLE-ABS-KEY("artificial intelligence" OR "AI" OR "machine learning" OR "intelligent tutoring system" OR "ITS" OR "chatbot" OR "generative AI" OR "ChatGPT" OR "GPT-4" OR "natural language processing" OR "automated grading" OR "adaptive learning") AND TITLE-ABS-KEY(education* OR student* OR instructor* OR teacher* OR learning OR pedagogy OR classroom OR university OR "higher education" OR "K-12" OR academic) AND TITLE-ABS-KEY(adoption OR acceptance OR intention OR usage OR behavior OR attitude OR TAM OR UTAUT OR "technology acceptance" OR "user acceptance") AND PUBYEAR > 2014 AND PUBYEAR < 2026
```

> `TITLE-ABS-KEY` = searches Title, Abstract, and Keywords

### Export Instructions
1. Select all results (or "Export all")
2. Export format: **CSV** or **BibTeX**
3. Information: "Citation information" + "Bibliographical information" + "Abstract & keywords"
4. Save as: `Scopus_export_YYYYMMDD.csv`

---

## Database 3: PsycINFO (via APA PsycNet or EBSCO)

**URL:** https://www.ebsco.com/ (via institutional EBSCO portal) or https://psycnet.apa.org/

### If via EBSCO:

### Step-by-Step
1. Log in via institutional library portal -> EBSCO -> Select "PsycINFO"
2. Click "Advanced Search"
3. Enter each cluster in separate search boxes

### Query (EBSCO Advanced Search - 3 rows)
```
Row 1 (Select "AB Abstract" or "TX All Text"):
"artificial intelligence" OR "AI" OR "machine learning" OR "intelligent tutoring system" OR "ITS" OR "chatbot" OR "generative AI" OR "ChatGPT" OR "GPT-4" OR "natural language processing" OR "automated grading" OR "adaptive learning"

Row 2 (AND):
education* OR student* OR instructor* OR teacher* OR learning OR pedagogy OR classroom OR university OR "higher education" OR "K-12" OR academic

Row 3 (AND):
adoption OR acceptance OR intention OR usage OR behavior OR attitude OR TAM OR UTAUT OR "technology acceptance" OR "user acceptance"
```

### Limiters
- Publication Date: January 2015 - December 2025
- Language: English
- Source Types: Academic Journals, Conference Materials

### Export Instructions
1. Select all results -> "Share" -> "Export"
2. Format: **RIS** (for reference managers) or **Direct Export to EndNote/Zotero**
3. Save as: `PsycINFO_export_YYYYMMDD.ris`

---

## Database 4: IEEE Xplore

**URL:** https://ieeexplore.ieee.org/

### Step-by-Step
1. Go to IEEE Xplore (institutional access auto-detects)
2. Click "Advanced Search" (Command Search)
3. Paste the query below

### Query (Command Search)
```
("All Metadata":"artificial intelligence" OR "All Metadata":"AI" OR "All Metadata":"machine learning" OR "All Metadata":"intelligent tutoring system" OR "All Metadata":"chatbot" OR "All Metadata":"generative AI" OR "All Metadata":"ChatGPT" OR "All Metadata":"natural language processing" OR "All Metadata":"adaptive learning") AND ("All Metadata":"education" OR "All Metadata":"student" OR "All Metadata":"teacher" OR "All Metadata":"learning" OR "All Metadata":"university" OR "All Metadata":"higher education" OR "All Metadata":"K-12" OR "All Metadata":"academic") AND ("All Metadata":"adoption" OR "All Metadata":"acceptance" OR "All Metadata":"intention" OR "All Metadata":"TAM" OR "All Metadata":"UTAUT" OR "All Metadata":"technology acceptance")
```

### Alternative: If Command Search is complex, use Advanced Search GUI
- Search Field 1: "All Metadata" contains `artificial intelligence OR AI OR machine learning OR chatbot OR generative AI OR ChatGPT OR adaptive learning`
- AND Search Field 2: "All Metadata" contains `education OR student OR teacher OR learning OR university OR higher education`
- AND Search Field 3: "All Metadata" contains `adoption OR acceptance OR intention OR TAM OR UTAUT OR technology acceptance`
- Date Range: 2015-2025

### Export Instructions
1. Select all results (max 2,000 per export)
2. Click "Export" -> "CSV" or "BibTeX"
3. Include: Citation, Abstract
4. Save as: `IEEE_export_YYYYMMDD.csv`

---

## Database 5: ACM Digital Library

**URL:** https://dl.acm.org/

### Step-by-Step
1. Go to ACM DL (institutional access auto-detects)
2. Click "Advanced Search"
3. Use the query below

### Query (Advanced Search)
```
[[All: "artificial intelligence"] OR [All: "machine learning"] OR [All: "intelligent tutoring system"] OR [All: "chatbot"] OR [All: "generative ai"] OR [All: "chatgpt"] OR [All: "adaptive learning"] OR [All: "natural language processing"]] AND [[All: education] OR [All: student] OR [All: teacher] OR [All: learning] OR [All: university] OR [All: "higher education"]] AND [[All: adoption] OR [All: acceptance] OR [All: intention] OR [All: "TAM"] OR [All: "UTAUT"] OR [All: "technology acceptance"]]
```

### Alternative: Use "Search Within" GUI
- Field 1 (Anywhere): `"artificial intelligence" OR "machine learning" OR "intelligent tutoring system" OR "chatbot" OR "generative AI" OR "ChatGPT" OR "adaptive learning"`
- AND Field 2 (Anywhere): `education OR student OR teacher OR learning OR university OR "higher education"`
- AND Field 3 (Anywhere): `adoption OR acceptance OR intention OR TAM OR UTAUT OR "technology acceptance"`
- Published Between: January 2015 - December 2025

### Export Instructions
1. Select results
2. Export: **BibTeX** or **EndNote**
3. Save as: `ACM_export_YYYYMMDD.bib`

---

## Database 6: ERIC (Education Resources Information Center)

**URL:** https://eric.ed.gov/ (free, no institutional access required)

### Step-by-Step
1. Go to https://eric.ed.gov/
2. Click "Advanced Search" (Thesaurus Search)
3. Use Boolean/Phrase mode

### Query (Advanced Search - Boolean/Phrase)
```
("artificial intelligence" OR "AI" OR "machine learning" OR "intelligent tutoring system" OR "chatbot" OR "generative AI" OR "ChatGPT" OR "natural language processing" OR "adaptive learning") AND (education OR student OR teacher OR learning OR university OR "higher education" OR "K-12") AND (adoption OR acceptance OR intention OR attitude OR TAM OR UTAUT OR "technology acceptance")
```

### Limiters
- Publication Date: Since 2015
- Publication Type: Journal Articles, Reports - Research
- Peer Reviewed: Yes (check box)

### ERIC Descriptors (optional, for more targeted results)
Add to search: `descriptor:"Artificial Intelligence"` AND `descriptor:"Technology Uses in Education"` or `descriptor:"Technology Acceptance"`

### Export Instructions
1. Select results
2. Export: **ERIC citation** (.nbib) or **CSV**
3. Save as: `ERIC_export_YYYYMMDD.csv`

> Note: ERIC limits display to 2,000 results. If >2,000, narrow by date ranges (e.g., 2015-2020, 2021-2025).

---

## Database 7: Education Source (via EBSCO)

**URL:** Via institutional EBSCO portal

### Step-by-Step
1. Log in via institutional library portal -> EBSCO
2. Select "Education Source" database
3. Click "Advanced Search"
4. Enter each cluster in separate search boxes (same as PsycINFO EBSCO format)

### Query (EBSCO Advanced Search - 3 rows)
```
Row 1 (TX All Text):
"artificial intelligence" OR "AI" OR "machine learning" OR "intelligent tutoring system" OR "ITS" OR "chatbot" OR "generative AI" OR "ChatGPT" OR "GPT-4" OR "natural language processing" OR "automated grading" OR "adaptive learning"

Row 2 (AND, TX All Text):
education* OR student* OR instructor* OR teacher* OR learning OR pedagogy OR classroom OR university OR "higher education" OR "K-12" OR academic

Row 3 (AND, TX All Text):
adoption OR acceptance OR intention OR usage OR behavior OR attitude OR TAM OR UTAUT OR "technology acceptance" OR "user acceptance"
```

### Limiters
- Published Date: 20150101-20251231
- Language: English
- Source Types: Academic Journals
- Peer Reviewed: Yes

### Export Instructions
1. Select all -> "Share" -> "Export"
2. Format: **RIS** or **Direct Export**
3. Save as: `EduSource_export_YYYYMMDD.ris`

> Tip: PsycINFO and Education Source are both on EBSCO. You can search both simultaneously by selecting both databases before searching. But export separately for PRISMA documentation.

---

## Results Tracking Template

After each database search, record the following:

| Field | Value |
|-------|-------|
| Database | |
| Date searched | |
| Exact query used | (copy-paste) |
| Filters/Limiters applied | |
| Total hits | |
| Records exported | |
| Export filename | |
| Notes | |

### Expected Results Summary

| # | Database | Expected Hits | Actual Hits | Export File | Date |
|---|----------|:------------:|:-----------:|-------------|------|
| 1 | Web of Science | 800-2,000 | | | |
| 2 | Scopus | 1,000-3,000 | | | |
| 3 | PsycINFO | 300-800 | | | |
| 4 | IEEE Xplore | 200-600 | | | |
| 5 | ACM DL | 100-400 | | | |
| 6 | ERIC | 400-1,000 | | | |
| 7 | Education Source | 300-800 | | | |
| | **Total (before dedup)** | **3,100-8,600** | | | |

---

## Post-Search Steps

### 1. Deduplication
After collecting all exports, bring them back to this computer and run:
```bash
# Place all export files in:
/Users/hosung/jornal_AI-adoption_meta/data/raw/search_results/

# We will use Python/R deduplication scripts to:
# - Merge all exports
# - Remove duplicates by DOI and title similarity
# - Generate deduplicated master list
```

### 2. AI-Assisted Screening (Codex CLI + Gemini CLI)
```bash
# Title/Abstract screening with multi-model consensus:
# - Codex CLI (GPT model) screens each record
# - Gemini CLI (Gemini model) independently screens
# - Consensus = both agree -> auto-include/exclude
# - Disagreement -> manual review queue
```

### 3. PRISMA Flow Diagram Data
Record these numbers for the PRISMA 2020 flow diagram:
- Records identified from each database (7 numbers)
- Total records before dedup
- Duplicates removed
- Records screened (title/abstract)
- Records excluded at screening
- Full-text articles assessed
- Full-text excluded (with reasons)
- Studies included in final synthesis

---

## Troubleshooting

**Q: "AI" returns too many irrelevant results (e.g., "aid", abbreviations)**
- Solution: Use `"AI"` in quotes and combine with the education cluster to narrow results. In WoS/Scopus, this generally works well because TS/TITLE-ABS-KEY searches are field-specific.

**Q: Database limits the number of Boolean operators**
- Solution: Reduce Cluster 1 to core terms: `("artificial intelligence" OR "machine learning" OR "chatbot" OR "generative AI" OR "ChatGPT" OR "intelligent tutoring system" OR "adaptive learning")`

**Q: Too many results (>5,000 in one database)**
- Solution: Add a 4th filter: `AND (survey OR questionnaire OR "structural equation" OR SEM OR correlation OR "path analysis" OR "regression")` to target quantitative adoption studies specifically.

**Q: Institutional access not working**
- Solution: Use your university VPN or access through the library portal's proxy (e.g., ezproxy). URL pattern: `https://ezproxy.[university].edu/login?url=https://...`

**Q: EBSCO interface is different from described**
- Solution: EBSCO regularly updates its interface. Look for "Advanced Search" and use the multi-row search box interface. The query syntax remains the same.
