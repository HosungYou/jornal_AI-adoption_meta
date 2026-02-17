# Quick Reference Cheat Sheet (Print This)

**Project:** AI Adoption in Education MASEM | **Date Range:** 2015-2025

---

## DB1: Web of Science (Advanced Search)

```
TS=("artificial intelligence" OR "AI" OR "machine learning" OR "intelligent tutoring system" OR "ITS" OR "chatbot" OR "generative AI" OR "ChatGPT" OR "GPT-4" OR "natural language processing" OR "automated grading" OR "adaptive learning") AND TS=(education* OR student* OR instructor* OR teacher* OR learning OR pedagogy OR classroom OR university OR "higher education" OR "K-12" OR academic) AND TS=(adoption OR acceptance OR intention OR usage OR behavior OR attitude OR TAM OR UTAUT OR "technology acceptance" OR "user acceptance")
```
- Timespan: 2015-01-01 ~ 2025-12-31
- Export: Tab-delimited (UTF-8), Full Record + Cited References
- Filename: `WoS_export_YYYYMMDD.txt`

---

## DB2: Scopus (Advanced Search)

```
TITLE-ABS-KEY("artificial intelligence" OR "AI" OR "machine learning" OR "intelligent tutoring system" OR "ITS" OR "chatbot" OR "generative AI" OR "ChatGPT" OR "GPT-4" OR "natural language processing" OR "automated grading" OR "adaptive learning") AND TITLE-ABS-KEY(education* OR student* OR instructor* OR teacher* OR learning OR pedagogy OR classroom OR university OR "higher education" OR "K-12" OR academic) AND TITLE-ABS-KEY(adoption OR acceptance OR intention OR usage OR behavior OR attitude OR TAM OR UTAUT OR "technology acceptance" OR "user acceptance") AND PUBYEAR > 2014 AND PUBYEAR < 2026
```
- Export: CSV, Citation + Bibliographic + Abstract & keywords
- Filename: `Scopus_export_YYYYMMDD.csv`

---

## DB3: PsycINFO (EBSCO Advanced Search, 3 rows)

**Row 1 (TX All Text):**
```
"artificial intelligence" OR "AI" OR "machine learning" OR "intelligent tutoring system" OR "ITS" OR "chatbot" OR "generative AI" OR "ChatGPT" OR "GPT-4" OR "natural language processing" OR "automated grading" OR "adaptive learning"
```

**Row 2 (AND):**
```
education* OR student* OR instructor* OR teacher* OR learning OR pedagogy OR classroom OR university OR "higher education" OR "K-12" OR academic
```

**Row 3 (AND):**
```
adoption OR acceptance OR intention OR usage OR behavior OR attitude OR TAM OR UTAUT OR "technology acceptance" OR "user acceptance"
```
- Limiters: 2015-2025, English, Academic Journals + Conference
- Export: RIS format
- Filename: `PsycINFO_export_YYYYMMDD.ris`

---

## DB4: IEEE Xplore (Advanced Search GUI)

**Field 1 (All Metadata):**
```
artificial intelligence OR AI OR machine learning OR chatbot OR generative AI OR ChatGPT OR adaptive learning OR intelligent tutoring system
```

**AND Field 2 (All Metadata):**
```
education OR student OR teacher OR learning OR university OR higher education
```

**AND Field 3 (All Metadata):**
```
adoption OR acceptance OR intention OR TAM OR UTAUT OR technology acceptance
```
- Date Range: 2015-2025
- Export: CSV or BibTeX
- Filename: `IEEE_export_YYYYMMDD.csv`

---

## DB5: ACM Digital Library (Advanced Search)

**Field 1 (Anywhere):**
```
"artificial intelligence" OR "machine learning" OR "intelligent tutoring system" OR "chatbot" OR "generative AI" OR "ChatGPT" OR "adaptive learning"
```

**AND Field 2 (Anywhere):**
```
education OR student OR teacher OR learning OR university OR "higher education"
```

**AND Field 3 (Anywhere):**
```
adoption OR acceptance OR intention OR TAM OR UTAUT OR "technology acceptance"
```
- Published Between: January 2015 - December 2025
- Export: BibTeX
- Filename: `ACM_export_YYYYMMDD.bib`

---

## DB6: ERIC (eric.ed.gov, Advanced Search, Boolean/Phrase)

```
("artificial intelligence" OR "AI" OR "machine learning" OR "intelligent tutoring system" OR "chatbot" OR "generative AI" OR "ChatGPT" OR "natural language processing" OR "adaptive learning") AND (education OR student OR teacher OR learning OR university OR "higher education" OR "K-12") AND (adoption OR acceptance OR intention OR attitude OR TAM OR UTAUT OR "technology acceptance")
```
- Since 2015, Peer Reviewed, Journal Articles
- Export: CSV
- Filename: `ERIC_export_YYYYMMDD.csv`

---

## DB7: Education Source (EBSCO, same format as PsycINFO)

Same 3-row query as PsycINFO above. Select "Education Source" database in EBSCO.
- Limiters: 2015-2025, English, Academic Journals, Peer Reviewed
- Export: RIS
- Filename: `EduSource_export_YYYYMMDD.ris`

---

## Results Log (fill in by hand)

| DB | Hits | Exported | File | Date |
|----|:----:|:--------:|------|------|
| Web of Science | | | | |
| Scopus | | | | |
| PsycINFO | | | | |
| IEEE Xplore | | | | |
| ACM DL | | | | |
| ERIC | | | | |
| Education Source | | | | |
| **TOTAL** | | | | |

---

## If Too Many Results (>5,000 in any DB)

Add this 4th cluster to narrow to quantitative adoption studies:
```
AND (survey OR questionnaire OR "structural equation" OR SEM OR correlation OR "path analysis" OR regression)
```

## Export File Destination

Copy all files to USB or cloud, then place in:
```
/Users/hosung/jornal_AI-adoption_meta/data/raw/search_results/
```
