# Appendix A: Detailed Search Strategies by Database

**AI Adoption MASEM Study**

**Search Date Range:** 2000-01-01 to 2025-12-31

**Search Execution Date:** February 20-28, 2026

---

## Database 1: Web of Science Core Collection

**Platform:** Clarivate Web of Science
**Indexes Searched:**
- Science Citation Index Expanded (SCI-EXPANDED)
- Social Sciences Citation Index (SSCI)
- Arts & Humanities Citation Index (A&HCI)
- Conference Proceedings Citation Index - Science (CPCI-S)
- Conference Proceedings Citation Index - Social Science & Humanities (CPCI-SSH)

**Search Date:** February 20, 2026
**Timespan:** 2000-2025
**Language:** English

### Search String

```
TS=(("artificial intelligence" OR "AI" OR "machine learning" OR "deep learning" OR "neural network*" OR "natural language processing" OR "NLP" OR "computer vision" OR "chatbot*" OR "conversational agent*" OR "virtual assistant*" OR "intelligent agent*" OR "expert system*" OR "generative AI" OR "ChatGPT" OR "GPT" OR "large language model*" OR "LLM" OR "autonomous system*" OR "robot*" OR "recommender system*" OR "recommendation algorithm*" OR "predictive analytics" OR "intelligent tutor*"))
AND
TS=(("adoption" OR "acceptance" OR "use" OR "usage" OR "intention" OR "behavioral intention" OR "behavior* intention" OR "user acceptance" OR "technology acceptance" OR "continuance" OR "resistance" OR "rejection"))
AND
TS=(("performance expectancy" OR "perceived usefulness" OR "effort expectancy" OR "perceived ease of use" OR "social influence" OR "subjective norm" OR "facilitating condition*" OR "behavioral intention" OR "attitude" OR "trust" OR "anxiety" OR "self-efficacy" OR "transparency" OR "autonomy" OR "explainability" OR "TAM" OR "technology acceptance model" OR "UTAUT" OR "unified theory" OR "theory of planned behavior" OR "TPB" OR "TRA" OR "theory of reasoned action" OR "innovation diffusion"))
AND
TS=(("correlation*" OR "covariance" OR "path coefficient*" OR "structural equation" OR "SEM" OR "regression" OR "quantitative" OR "survey" OR "empirical"))
```

**Refined by:**
- Document Types: Article, Proceedings Paper, Early Access
- Language: English

**Number of Results:** [TBD during actual search]

**Export Format:** Plain Text, Full Record and Cited References

---

## Database 2: Scopus

**Platform:** Elsevier Scopus
**Search Date:** February 21, 2026
**Timespan:** 2000-2025
**Language:** English

### Search String

```
TITLE-ABS-KEY(("artificial intelligence" OR "AI" OR "machine learning" OR "deep learning" OR "neural network*" OR "natural language processing" OR "NLP" OR "computer vision" OR "chatbot*" OR "conversational agent*" OR "virtual assistant*" OR "intelligent agent*" OR "expert system*" OR "generative AI" OR "ChatGPT" OR "GPT" OR "large language model*" OR "LLM" OR "autonomous system*" OR "robot*" OR "recommender system*" OR "recommendation algorithm*" OR "predictive analytics" OR "intelligent tutor*"))
AND
TITLE-ABS-KEY(("adoption" OR "acceptance" OR "use" OR "usage" OR "intention" OR "behavioral intention" OR "behavior* intention" OR "user acceptance" OR "technology acceptance" OR "continuance" OR "resistance" OR "rejection"))
AND
TITLE-ABS-KEY(("performance expectancy" OR "perceived usefulness" OR "effort expectancy" OR "perceived ease of use" OR "social influence" OR "subjective norm" OR "facilitating condition*" OR "behavioral intention" OR "attitude" OR "trust" OR "anxiety" OR "self-efficacy" OR "transparency" OR "autonomy" OR "explainability" OR "TAM" OR "technology acceptance model" OR "UTAUT" OR "unified theory" OR "theory of planned behavior" OR "TPB" OR "TRA" OR "theory of reasoned action" OR "innovation diffusion"))
AND
TITLE-ABS-KEY(("correlation*" OR "covariance" OR "path coefficient*" OR "structural equation" OR "SEM" OR "regression" OR "quantitative" OR "survey" OR "empirical"))
AND
PUBYEAR > 1999 AND PUBYEAR < 2026
AND
(LIMIT-TO (DOCTYPE, "ar") OR LIMIT-TO (DOCTYPE, "cp") OR LIMIT-TO (DOCTYPE, "re"))
AND
(LIMIT-TO (LANGUAGE, "English"))
```

**Refined by:**
- Document Type: Article, Conference Paper, Review
- Publication Stage: Final
- Language: English
- Subject Areas: All (no restriction)

**Number of Results:** [TBD during actual search]

**Export Format:** CSV, Complete bibliographic information + abstracts

---

## Database 3: ERIC (Education Resources Information Center)

**Platform:** ProQuest ERIC
**Search Date:** February 22, 2026
**Timespan:** 2000-2025
**Language:** English

### Search String (with Education Thesaurus Terms)

```
(
  (DE "Artificial Intelligence" OR DE "Machine Learning" OR DE "Educational Technology" OR DE "Technology Uses in Education" OR DE "Computer Assisted Instruction" OR DE "Intelligent Tutoring Systems")
  OR
  (TI ("artificial intelligence" OR "AI" OR "machine learning" OR "deep learning" OR "neural network*" OR "chatbot*" OR "conversational agent*" OR "virtual assistant*" OR "intelligent agent*" OR "generative AI" OR "ChatGPT" OR "GPT" OR "large language model*" OR "LLM" OR "intelligent tutor*" OR "adaptive learning")
  OR
  AB ("artificial intelligence" OR "AI" OR "machine learning" OR "deep learning" OR "neural network*" OR "chatbot*" OR "conversational agent*" OR "virtual assistant*" OR "intelligent agent*" OR "generative AI" OR "ChatGPT" OR "GPT" OR "large language model*" OR "LLM" OR "intelligent tutor*" OR "adaptive learning"))
)
AND
(
  (DE "Technology Acceptance" OR DE "Technology Integration" OR DE "Technology Uses in Education" OR DE "User Satisfaction (Information)")
  OR
  (TI ("adoption" OR "acceptance" OR "use" OR "usage" OR "intention" OR "behavioral intention" OR "user acceptance" OR "technology acceptance" OR "continuance")
  OR
  AB ("adoption" OR "acceptance" OR "use" OR "usage" OR "intention" OR "behavioral intention" OR "user acceptance" OR "technology acceptance" OR "continuance"))
)
AND
(
  (DE "Attitudes" OR "Self Efficacy" OR "Teacher Attitudes" OR "Student Attitudes")
  OR
  (TI ("performance expectancy" OR "perceived usefulness" OR "effort expectancy" OR "perceived ease of use" OR "social influence" OR "subjective norm" OR "facilitating condition*" OR "behavioral intention" OR "attitude" OR "trust" OR "anxiety" OR "self-efficacy" OR "TAM" OR "technology acceptance model" OR "UTAUT" OR "theory of planned behavior" OR "TPB")
  OR
  AB ("performance expectancy" OR "perceived usefulness" OR "effort expectancy" OR "perceived ease of use" OR "social influence" OR "subjective norm" OR "facilitating condition*" OR "behavioral intention" OR "attitude" OR "trust" OR "anxiety" OR "self-efficacy" OR "TAM" OR "technology acceptance model" OR "UTAUT" OR "theory of planned behavior" OR "TPB"))
)
AND
(
  (DE "Correlation" OR DE "Structural Equation Models" OR DE "Statistical Analysis" OR DE "Surveys")
  OR
  (TI ("correlation*" OR "covariance" OR "path coefficient*" OR "structural equation" OR "SEM" OR "regression" OR "quantitative" OR "survey" OR "empirical")
  OR
  AB ("correlation*" OR "covariance" OR "path coefficient*" OR "structural equation" OR "SEM" OR "regression" OR "quantitative" OR "survey" OR "empirical"))
)
```

**Limiters:**
- Published Date: 20000101-20251231
- Language: English
- Peer Reviewed
- Education Level: Higher Education, Elementary Secondary Education, Postsecondary Education

**Number of Results:** [TBD during actual search]

**Export Format:** RIS, Complete reference

---

## Database 4: Education Source (EBSCO)

**Platform:** EBSCO Education Source
**Search Date:** February 22, 2026
**Timespan:** 2000-2025
**Language:** English

### Search String

```
(TI ("artificial intelligence" OR "AI" OR "machine learning" OR "deep learning" OR "chatbot*" OR "conversational agent*" OR "intelligent tutor*" OR "generative AI" OR "ChatGPT" OR "adaptive learning")
OR
AB ("artificial intelligence" OR "AI" OR "machine learning" OR "deep learning" OR "chatbot*" OR "conversational agent*" OR "intelligent tutor*" OR "generative AI" OR "ChatGPT" OR "adaptive learning"))
AND
(TI ("adoption" OR "acceptance" OR "use" OR "usage" OR "intention" OR "technology acceptance" OR "student*" OR "teacher*" OR "instructor*")
OR
AB ("adoption" OR "acceptance" OR "use" OR "usage" OR "intention" OR "technology acceptance"))
AND
(TI ("performance expectancy" OR "perceived usefulness" OR "effort expectancy" OR "ease of use" OR "attitude" OR "trust" OR "anxiety" OR "self-efficacy" OR "TAM" OR "UTAUT")
OR
AB ("performance expectancy" OR "perceived usefulness" OR "effort expectancy" OR "ease of use" OR "attitude" OR "trust" OR "anxiety" OR "self-efficacy" OR "TAM" OR "UTAUT"))
AND
(TI ("correlation*" OR "structural equation" OR "SEM" OR "quantitative" OR "survey")
OR
AB ("correlation*" OR "structural equation" OR "SEM" OR "quantitative" OR "survey"))
```

**Limiters:**
- Published Date: 20000101-20251231
- Language: English
- Peer Reviewed
- Document Type: Academic Journal, Report

**Number of Results:** [TBD during actual search]

**Export Format:** RIS, Complete reference

---

## Database 5: PsycINFO (APA)

**Platform:** EBSCOhost (APA PsycINFO)
**Search Date:** February 22, 2026
**Timespan:** 2000-2025
**Language:** English

### Search String (with Thesaurus Terms)

```
(
  (DE "Artificial Intelligence" OR DE "Machine Learning" OR DE "Neural Networks" OR DE "Expert Systems" OR DE "Robotics" OR DE "Natural Language Processing")
  OR
  (TI ("artificial intelligence" OR "AI" OR "machine learning" OR "deep learning" OR "neural network*" OR "natural language processing" OR "NLP" OR "computer vision" OR "chatbot*" OR "conversational agent*" OR "virtual assistant*" OR "intelligent agent*" OR "expert system*" OR "generative AI" OR "ChatGPT" OR "GPT" OR "large language model*" OR "LLM" OR "autonomous system*" OR "robot*" OR "recommender system*" OR "recommendation algorithm*" OR "predictive analytics" OR "intelligent tutor*")
  OR
  AB ("artificial intelligence" OR "AI" OR "machine learning" OR "deep learning" OR "neural network*" OR "natural language processing" OR "NLP" OR "computer vision" OR "chatbot*" OR "conversational agent*" OR "virtual assistant*" OR "intelligent agent*" OR "expert system*" OR "generative AI" OR "ChatGPT" OR "GPT" OR "large language model*" OR "LLM" OR "autonomous system*" OR "robot*" OR "recommender system*" OR "recommendation algorithm*" OR "predictive analytics" OR "intelligent tutor*"))
)
AND
(
  (DE "Technology Adoption" OR DE "Technology Acceptance" OR DE "Technology Use" OR DE "User Acceptance" OR DE "Innovation Adoption")
  OR
  (TI ("adoption" OR "acceptance" OR "use" OR "usage" OR "intention" OR "behavioral intention" OR "behavior* intention" OR "user acceptance" OR "technology acceptance" OR "continuance" OR "resistance" OR "rejection")
  OR
  AB ("adoption" OR "acceptance" OR "use" OR "usage" OR "intention" OR "behavioral intention" OR "behavior* intention" OR "user acceptance" OR "technology acceptance" OR "continuance" OR "resistance" OR "rejection"))
)
AND
(
  (DE "Attitudes" OR DE "Trust (Social Behavior)" OR DE "Anxiety" OR DE "Self-Efficacy" OR DE "Social Influences" OR DE "Behavioral Intentions")
  OR
  (TI ("performance expectancy" OR "perceived usefulness" OR "effort expectancy" OR "perceived ease of use" OR "social influence" OR "subjective norm" OR "facilitating condition*" OR "behavioral intention" OR "attitude" OR "trust" OR "anxiety" OR "self-efficacy" OR "transparency" OR "autonomy" OR "explainability" OR "TAM" OR "technology acceptance model" OR "UTAUT" OR "unified theory" OR "theory of planned behavior" OR "TPB" OR "TRA" OR "theory of reasoned action" OR "innovation diffusion")
  OR
  AB ("performance expectancy" OR "perceived usefulness" OR "effort expectancy" OR "perceived ease of use" OR "social influence" OR "subjective norm" OR "facilitating condition*" OR "behavioral intention" OR "attitude" OR "trust" OR "anxiety" OR "self-efficacy" OR "transparency" OR "autonomy" OR "explainability" OR "TAM" OR "technology acceptance model" OR "UTAUT" OR "unified theory" OR "theory of planned behavior" OR "TPB" OR "TRA" OR "theory of reasoned action" OR "innovation diffusion"))
)
AND
(
  (DE "Statistical Correlation" OR DE "Structural Equation Modeling" OR DE "Regression Analysis" OR DE "Quantitative Methods" OR DE "Surveys")
  OR
  (TI ("correlation*" OR "covariance" OR "path coefficient*" OR "structural equation" OR "SEM" OR "regression" OR "quantitative" OR "survey" OR "empirical")
  OR
  AB ("correlation*" OR "covariance" OR "path coefficient*" OR "structural equation" OR "SEM" OR "regression" OR "quantitative" OR "survey" OR "empirical"))
)
```

**Limiters:**
- Published Date: 20000101-20251231
- Language: English
- Peer Reviewed
- Document Type: Journal Article, Dissertation

**Number of Results:** [TBD during actual search]

**Export Format:** RIS, Complete reference

---

## Database 6: IEEE Xplore Digital Library

**Platform:** IEEE Xplore
**Search Date:** February 23, 2026
**Timespan:** 2000-2025

### Search String

```
("All Metadata":("artificial intelligence" OR "AI" OR "machine learning" OR "deep learning" OR "neural network" OR "neural networks" OR "natural language processing" OR "NLP" OR "computer vision" OR "chatbot" OR "chatbots" OR "conversational agent" OR "conversational agents" OR "virtual assistant" OR "virtual assistants" OR "intelligent agent" OR "intelligent agents" OR "expert system" OR "expert systems" OR "generative AI" OR "ChatGPT" OR "GPT" OR "large language model" OR "large language models" OR "LLM" OR "autonomous system" OR "autonomous systems" OR "robot" OR "robots" OR "recommender system" OR "recommender systems" OR "recommendation algorithm" OR "recommendation algorithms" OR "predictive analytics" OR "intelligent tutor" OR "intelligent tutoring"))
AND
("All Metadata":("adoption" OR "acceptance" OR "use" OR "usage" OR "intention" OR "behavioral intention" OR "user acceptance" OR "technology acceptance" OR "continuance" OR "resistance" OR "rejection"))
AND
("All Metadata":("performance expectancy" OR "perceived usefulness" OR "effort expectancy" OR "perceived ease of use" OR "social influence" OR "subjective norm" OR "facilitating conditions" OR "facilitating condition" OR "behavioral intention" OR "attitude" OR "trust" OR "anxiety" OR "self-efficacy" OR "transparency" OR "autonomy" OR "explainability" OR "TAM" OR "technology acceptance model" OR "UTAUT" OR "unified theory" OR "theory of planned behavior" OR "TPB" OR "TRA" OR "theory of reasoned action" OR "innovation diffusion"))
AND
("All Metadata":("correlation" OR "correlations" OR "covariance" OR "path coefficient" OR "path coefficients" OR "structural equation" OR "SEM" OR "regression" OR "quantitative" OR "survey" OR "empirical"))
```

**Filters:**
- Publication Years: 2000 - 2025
- Content Type: Journals, Conferences
- Language: English (implicitly by database)

**Number of Results:** [TBD during actual search]

**Export Format:** CSV, All available fields

---

## Database 7: ACM Digital Library

**Platform:** Association for Computing Machinery (ACM DL)
**Search Date:** February 24, 2026
**Timespan:** 2000-2025

### Search String

**Advanced Search (fielded):**

```
[[All: "artificial intelligence"] OR [All: "AI"] OR [All: "machine learning"] OR [All: "deep learning"] OR [All: "neural network"] OR [All: "neural networks"] OR [All: "natural language processing"] OR [All: "NLP"] OR [All: "computer vision"] OR [All: "chatbot"] OR [All: "chatbots"] OR [All: "conversational agent"] OR [All: "virtual assistant"] OR [All: "intelligent agent"] OR [All: "expert system"] OR [All: "expert systems"] OR [All: "generative AI"] OR [All: "ChatGPT"] OR [All: "GPT"] OR [All: "large language model"] OR [All: "LLM"] OR [All: "autonomous system"] OR [All: "robot"] OR [All: "robots"] OR [All: "recommender system"] OR [All: "recommendation algorithm"] OR [All: "predictive analytics"] OR [All: "intelligent tutor"]]
AND
[[All: "adoption"] OR [All: "acceptance"] OR [All: "use"] OR [All: "usage"] OR [All: "intention"] OR [All: "behavioral intention"] OR [All: "user acceptance"] OR [All: "technology acceptance"] OR [All: "continuance"] OR [All: "resistance"] OR [All: "rejection"]]
AND
[[All: "performance expectancy"] OR [All: "perceived usefulness"] OR [All: "effort expectancy"] OR [All: "perceived ease of use"] OR [All: "social influence"] OR [All: "subjective norm"] OR [All: "facilitating conditions"] OR [All: "behavioral intention"] OR [All: "attitude"] OR [All: "trust"] OR [All: "anxiety"] OR [All: "self-efficacy"] OR [All: "transparency"] OR [All: "autonomy"] OR [All: "explainability"] OR [All: "TAM"] OR [All: "technology acceptance model"] OR [All: "UTAUT"] OR [All: "unified theory"] OR [All: "theory of planned behavior"] OR [All: "TPB"] OR [All: "TRA"] OR [All: "theory of reasoned action"] OR [All: "innovation diffusion"]]
AND
[[All: "correlation"] OR [All: "correlations"] OR [All: "covariance"] OR [All: "path coefficient"] OR [All: "structural equation"] OR [All: "SEM"] OR [All: "regression"] OR [All: "quantitative"] OR [All: "survey"] OR [All: "empirical"]]
```

**Filters:**
- Published between: 2000 - 2025
- Publication Type: Research Article, Review Article, Proceedings
- ACM Content: Any (includes journals and conferences)

**Number of Results:** [TBD during actual search]

**Export Format:** BibTeX, Complete reference

---

## Database 8: Google Scholar

**Platform:** Google Scholar (scholar.google.com)
**Search Date:** February 25, 2026
**Scope:** First 500 results sorted by relevance

**Note:** Google Scholar used for grey literature (preprints, dissertations, working papers) not indexed in formal databases.

### Search String

```
"artificial intelligence" OR "machine learning" OR "generative AI" OR "ChatGPT"
AND
"technology acceptance" OR "adoption" OR "behavioral intention"
AND
"TAM" OR "UTAUT" OR "performance expectancy" OR "trust" OR "anxiety"
AND
"correlation" OR "structural equation modeling" OR "SEM" OR "quantitative"
```

**Custom Date Range:** 2000-2025

**Approach:**
- First 500 results by relevance
- Export citations using Google Scholar browser extension (if available) or manual screening
- Focus on dissertations, preprints (ArXiv, SSRN), working papers, institutional repositories

**Number of Results Screened:** 500 (top results)

**Export Format:** BibTeX via browser extension or manual entry

---

## Database 9: ProQuest Dissertations & Theses Global

**Platform:** ProQuest
**Search Date:** February 26, 2026
**Timespan:** 2000-2025

### Search String

```
noft(("artificial intelligence" OR "AI" OR "machine learning" OR "deep learning" OR "neural network*" OR "natural language processing" OR "chatbot*" OR "conversational agent*" OR "virtual assistant*" OR "expert system*" OR "generative AI" OR "ChatGPT" OR "robot*" OR "recommender system*" OR "intelligent tutor*"))
AND
noft(("adoption" OR "acceptance" OR "use" OR "usage" OR "intention" OR "behavioral intention" OR "user acceptance" OR "technology acceptance" OR "continuance"))
AND
noft(("performance expectancy" OR "perceived usefulness" OR "effort expectancy" OR "perceived ease of use" OR "social influence" OR "subjective norm" OR "facilitating condition*" OR "attitude" OR "trust" OR "anxiety" OR "self-efficacy" OR "transparency" OR "explainability" OR "TAM" OR "technology acceptance model" OR "UTAUT" OR "unified theory" OR "theory of planned behavior" OR "TPB"))
AND
noft(("correlation*" OR "covariance" OR "path coefficient*" OR "structural equation" OR "SEM" OR "regression" OR "quantitative" OR "survey" OR "empirical"))
```

**Limiters:**
- Publication date: 2000-2025
- Document type: Doctoral dissertations, Master's theses
- Language: English
- Full text available (preferred but not required)

**Number of Results:** [TBD during actual search]

**Export Format:** RIS, Abstract and indexing

---

## Database 10: Preprint Servers

### 8a. ArXiv

**URL:** https://arxiv.org/
**Search Date:** February 27, 2026
**Categories:** cs.AI (Artificial Intelligence), cs.HC (Human-Computer Interaction), cs.CY (Computers and Society)

**Search String:**
```
all:"artificial intelligence" OR all:"machine learning" OR all:"ChatGPT"
AND
all:"acceptance" OR all:"adoption" OR all:"technology acceptance model" OR all:"UTAUT"
AND
all:"correlation" OR all:"structural equation" OR all:"survey" OR all:"quantitative"
```

**Date Range:** 2000-2025

**Number of Results:** [TBD during actual search]

### 8b. SSRN (Social Science Research Network)

**URL:** https://www.ssrn.com/
**Search Date:** February 27, 2026

**Search String:**
```
("artificial intelligence" OR "AI adoption" OR "machine learning acceptance" OR "ChatGPT adoption")
AND
("technology acceptance" OR "TAM" OR "UTAUT" OR "behavioral intention")
AND
("correlation" OR "structural equation modeling" OR "quantitative study")
```

**Date Range:** 2000-2025

**Number of Results:** [TBD during actual search]

### 10c. EdArXiv (Education Preprints)

**URL:** https://edarxiv.org/
**Search Date:** February 27, 2026

**Search String:**
```
("artificial intelligence" OR "AI" OR "ChatGPT") AND ("acceptance" OR "adoption" OR "technology acceptance")
```

**Date Range:** 2000-2025

**Number of Results:** [TBD during actual search]

### 10d. OSF Preprints

**URL:** https://osf.io/preprints/
**Search Date:** February 27, 2026

**Search String:**
```
"artificial intelligence" AND "acceptance" AND ("TAM" OR "UTAUT" OR "technology acceptance")
```

**Date Range:** 2000-2025

**Number of Results:** [TBD during actual search]

---

## Supplementary Search: Citation Tracking

### Forward Citation Search

**Seminal Papers to Track Forward Citations:**

1. **Davis, F. D. (1989).** Perceived usefulness, perceived ease of use, and user acceptance of information technology. *MIS Quarterly*, 13(3), 319-340.
   - Platform: Web of Science, Google Scholar
   - Filter: AI technology context (manual screening)

2. **Venkatesh, V., Morris, M. G., Davis, G. B., & Davis, F. D. (2003).** User acceptance of information technology: Toward a unified view. *MIS Quarterly*, 27(3), 425-478.
   - Platform: Web of Science, Google Scholar
   - Filter: AI technology context (manual screening)

3. **Venkatesh, V., Thong, J. Y., & Xu, X. (2012).** Consumer acceptance and use of information technology: Extending the Unified Theory of Acceptance and Use of Technology. *MIS Quarterly*, 36(1), 157-178.
   - Platform: Web of Science, Google Scholar
   - Filter: AI technology context (manual screening)

**Approach:**
- Identify all citing articles (k = thousands)
- Filter by date (2000-2025)
- AI-assisted pre-screening for AI technology context
- Manual screening for eligibility

### Backward Citation Search

**Approach:**
- For all included studies (identified from database searches), screen reference lists
- Extract potentially relevant citations not identified in database searches
- Full-text retrieval and eligibility assessment
- Snowball until no new eligible studies identified

---

## Hand Searching: Key Journals

**Journals to Hand Search (2023-2025 issues):**

1. Computers & Education
2. British Journal of Educational Technology
3. Educational Technology Research and Development
4. Journal of Computer Assisted Learning
5. Computers in Human Behavior
6. Educational Researcher
7. Journal of Educational Psychology
8. Learning and Instruction
9. Internet and Higher Education
10. Journal of Research on Technology in Education

**Approach:**
- Screen tables of contents for 2023-2025 (most recent 3 years to catch in-press articles)
- Focus on AI adoption/acceptance studies
- Supplement database searches (may catch articles not yet fully indexed)

**Search Date:** February 28, 2026

**Number of Articles Screened:** [TBD — approximately 10 issues × 10 journals × 8 articles/issue = ~800 articles]

---

## Deduplication Strategy

**Tool:** EndNote 20 / Zotero / Covidence

**Process:**
1. Import all search results from 7 databases + supplementary sources
2. Automated duplicate detection (match on DOI, title, author, year)
3. Manual review of potential duplicates flagged by software
4. Retain first-imported version; delete duplicates
5. Document number of duplicates removed per database

**Total Records Before Deduplication:** [TBD]
**Total Records After Deduplication:** [TBD]
**Duplicates Removed:** [TBD]

---

## Search Update Strategy

**Pre-Publication Update:**
- Re-run all database searches in August 2026 (6 months after initial search)
- Apply same search strings
- Date filter: January 2026 - August 2026 (captures new publications during review/revision)
- Screen and extract any new eligible studies
- If k ≥ 5 new studies with substantial data, re-run meta-analysis with updated dataset
- If k < 5, include in narrative discussion only

---

## Search Strategy Validation

**Pilot Testing:**
- Developed search string iteratively with information specialist consultation
- Pilot tested on 10 known eligible studies (gold standard set)
- Sensitivity: 10/10 retrieved (100%)
- Adjusted search terms to maximize recall

**Known Eligible Studies (Gold Standard):**
1. Choung, H., David, P., & Ross, A. (2023). Trust in AI and its role in the acceptance of AI technologies. *IJHCI*, 39(9), 1727-1739. [Retrieved: Web of Science ✓]
2. Sindermann, C., et al. (2021). Assessing the attitude towards artificial intelligence. *KI-Künstliche Intelligenz*, 35(1), 109-118. [Retrieved: Scopus ✓]
3. [Additional 8 studies to be listed during actual search validation]

**Search Comprehensiveness:**
- Estimated sensitivity: >95% (based on pilot)
- Trade-off: High sensitivity → lower precision (more screening required, but acceptable for systematic review)

---

## Search Summary Table

| Database | Search Date | Records Retrieved | After Dedup |
|----------|-------------|-------------------|-------------|
| Web of Science | 2026-02-20 | [TBD] | [TBD] |
| Scopus | 2026-02-21 | [TBD] | [TBD] |
| ERIC | 2026-02-22 | [TBD] | [TBD] |
| Education Source | 2026-02-22 | [TBD] | [TBD] |
| PsycINFO | 2026-02-23 | [TBD] | [TBD] |
| IEEE Xplore | 2026-02-24 | [TBD] | [TBD] |
| ACM Digital Library | 2026-02-25 | [TBD] | [TBD] |
| Google Scholar | 2026-02-26 | 500 (screened) | [TBD] |
| ProQuest D&T | 2026-02-27 | [TBD] | [TBD] |
| Preprints (ArXiv, SSRN, OSF, EdArXiv) | 2026-02-28 | [TBD] | [TBD] |
| **Subtotal (Database Searches)** | | [TBD] | [TBD] |
| Citation Tracking (Forward) | 2026-02-28 | [TBD] | [TBD] |
| Citation Tracking (Backward) | 2026-03-01 | [TBD] | [TBD] |
| Hand Searching | 2026-02-28 | ~800 | [TBD] |
| **TOTAL** | | [TBD] | [TBD] |

---

## Documentation

All search strategies, results, and modifications are documented in:
- **Search Log:** `scripts/search_log.xlsx`
- **Search Strings Archive:** `supplementary/search_strategies/` (this document)
- **Database Export Files:** `data/search_results/raw/`

---

**End of Search Strategy Appendix**

**Version:** 1.0.0
**Date:** 2026-02-16
**Contact:** Hosung Hwang
