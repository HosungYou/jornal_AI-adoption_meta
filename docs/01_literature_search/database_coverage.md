# Database Coverage and Characteristics

## Overview

This document details the characteristics, coverage, and expected contribution of each database to the systematic literature search for AI adoption meta-analysis.

## Database Comparison Table

| Database | Subject Coverage | Unique Strengths | Expected Hits | Overlap with Others |
|----------|------------------|------------------|---------------|---------------------|
| Web of Science | Multidisciplinary, high-impact journals | Citation tracking, quality filtering | 300-500 | High with Scopus (60-70%) |
| Scopus | Broader multidisciplinary | More regional journals, conference proceedings | 400-600 | High with WoS (60-70%) |
| PsycINFO | Psychology, educational psychology | Individual acceptance, attitudes, educational contexts | 200-350 | Moderate (30-40%) |
| IEEE Xplore | Engineering, computer science | Technical AI systems, HCI, educational technology | 150-250 | Moderate with ACM (50%) |
| ACM Digital Library | Computing, information systems | User experience, interaction design, learning technologies | 100-200 | Moderate with IEEE (50%) |
| ERIC | Education research, K-12 through higher ed | Education-specific AI adoption, pedagogical technology | 200-400 | Moderate with PsycINFO (40%), low with others (20%) |
| Education Source | Education journals, practitioner reports | Practitioner-focused AI in education | 100-200 | High with ERIC (60%) |
| Google Scholar | Universal | Grey literature, preprints, recent work | 1,500+ (supplementary only) | Very high (80-90%) |

## Database-Specific Details

### Web of Science (Core Collection)

**Coverage:**
- 21,000+ peer-reviewed journals
- Conference proceedings (selective)
- Strong in business, management, psychology, computer science

**Indexed Fields Searched:**
- Title (TI)
- Abstract (AB)
- Author Keywords (AK)
- Keywords Plus (WoS-assigned terms)

**Date Coverage:**
- 2015-2025 for this search
- Historical coverage varies by journal

**Export Format:**
- Plain text, BibTeX, RIS
- **Preferred:** RIS (most complete metadata)

**Expected Contribution:**
- High-quality AI adoption studies in top-tier journals
- Strong coverage of UTAUT/TAM applications
- Educational AI adoption in multidisciplinary journals

**Search Fields Used:**
```
TS=(search string)
```
Where TS = Topic (Title + Abstract + Keywords + Keywords Plus)

**Filters Applied:**
- Document Type: Article, Proceedings Paper
- Language: English
- Timespan: 2015-2025

---

### Scopus

**Coverage:**
- 27,000+ peer-reviewed journals
- More international and regional journals than WoS
- Strong conference proceeding coverage

**Indexed Fields Searched:**
- Title
- Abstract
- Author Keywords
- Indexed Keywords

**Date Coverage:**
- 2015-2025 for this search
- Comprehensive from 1996 onwards

**Export Format:**
- CSV, RIS, BibTeX
- **Preferred:** RIS

**Expected Contribution:**
- Broader geographic coverage (Asian, European regional journals)
- AI adoption in emerging markets and diverse educational systems
- Conference proceedings with full papers (educational technology conferences)

**Search Fields Used:**
```
TITLE-ABS-KEY(search string)
```

**Filters Applied:**
- Document Type: Article, Conference Paper
- Language: English
- Publication Stage: Final
- Date: 2015-2025

**Unique Value:**
- More comprehensive than WoS (27k vs 21k journals)
- Better coverage of non-US journals
- Strong in engineering and computer science

---

### PsycINFO

**Coverage:**
- 2,500+ journals in psychology, educational psychology, and behavioral sciences
- Strong in individual behavior, attitudes, acceptance, educational contexts
- Unique thesaurus of psychological and educational constructs

**Indexed Fields Searched:**
- Title
- Abstract
- Keywords (author and APA thesaurus terms)

**Date Coverage:**
- 2015-2025 for this search
- Historical coverage to 1800s (comprehensive from 1967)

**Export Format:**
- RIS, APA PsycNET format
- **Preferred:** RIS

**Expected Contribution:**
- Individual-level AI acceptance and attitudes in educational settings
- AI anxiety, trust, self-efficacy constructs among students and instructors
- Educational psychology applications of AI technologies

**Thesaurus Terms Used:**
```
Artificial Intelligence (Thesaurus)
Technology Adoption (Thesaurus)
User Attitudes (Thesaurus)
Behavioral Intention (Thesaurus)
Computer Anxiety (Thesaurus)
Self-Efficacy (Thesaurus)
Educational Technology (Thesaurus)
Computer Assisted Instruction (Thesaurus)
```

**Filters Applied:**
- Methodology: Quantitative, Empirical Study
- Language: English
- Age Group: (no filter - all populations)
- Publication Type: Journal Article, Conference Paper

**Unique Value:**
- Best coverage of psychological constructs (anxiety, trust, self-efficacy)
- Strong in educational psychology and educational AI adoption
- Rigorous behavioral science methodology applied to educational contexts

---

### IEEE Xplore

**Coverage:**
- 5+ million documents in electrical engineering, computer science, electronics
- Conference proceedings (IEEE-sponsored)
- Standards, technical reports (excluded in this search)

**Indexed Fields Searched:**
- Document Title
- Abstract
- Index Terms (IEEE controlled vocabulary)

**Date Coverage:**
- 2015-2025 for this search
- Comprehensive from 1988 onwards

**Export Format:**
- CSV, BibTeX, RIS
- **Preferred:** BibTeX (best IEEE metadata)

**Expected Contribution:**
- Technical AI systems adoption in educational settings
- Human-AI interaction in learning environments
- Early educational AI adoption studies (intelligent tutoring systems, adaptive learning)

**Search Fields Used:**
```
("Abstract": artificial intelligence) AND ("Abstract": adoption OR acceptance)
```

**Filters Applied:**
- Content Type: Journals, Conferences
- Year: 2015-2025

**Unique Value:**
- Earliest educational AI adoption studies (intelligent tutoring systems)
- Explainability, transparency constructs in educational AI
- Educational robotics and AI-based learning systems

---

### ACM Digital Library

**Coverage:**
- 1+ million articles and proceedings in computing
- ACM-published journals and conferences
- Strong in human-computer interaction

**Indexed Fields Searched:**
- Title
- Abstract
- Keywords
- ACM Computing Classification System (CCS) categories

**Date Coverage:**
- 2015-2025 for this search
- Comprehensive from 1950s

**Export Format:**
- BibTeX, EndNote, ACM Ref
- **Preferred:** BibTeX

**Expected Contribution:**
- HCI perspective on AI adoption in education
- User experience with educational AI systems
- Interaction design and usability in learning technologies

**CCS Categories Filtered:**
```
Human-centered computing → Human computer interaction (HCI)
Human-centered computing → Empirical studies in HCI
Computing methodologies → Artificial intelligence
```

**Filters Applied:**
- Publication Type: Research Article, Proceedings
- Year: 2015-2025

**Unique Value:**
- HCI community's AI adoption research in educational contexts
- User experience and interface studies for learning technologies
- Explainability and transparency focus in educational AI

---

### Google Scholar (Supplementary)

**Coverage:**
- Universal (journals, books, theses, preprints, reports)
- No quality filtering
- Includes grey literature

**Search Approach:**
- **NOT used for primary systematic search** (lack of reproducibility)
- Used for backward/forward citation searching only
- Used to identify recent preprints and working papers

**Citation Searching Protocol:**
1. Identify top 20 most-cited studies from database search
2. Use "Cited by" function to find forward citations
3. Review 50 most recent citations per seed paper
4. Apply same inclusion/exclusion criteria

**Expected Contribution:**
- Recent preprints (2024-2025)
- Working papers from top institutions
- Grey literature from think tanks, industry research

**Limitations:**
- No controlled vocabulary
- Duplicate detection difficult
- Quality varies widely
- Not reproducible (results change daily)

**Justification for Supplementary Use Only:**
- PRISMA guidelines recommend transparent, reproducible searches
- Google Scholar lacks advanced search operators and stable results
- Used only for citation chasing, not primary search

---

### ERIC (Education Resources Information Center)

**Coverage:**
- 1.6+ million records in education research
- K-12 through higher education
- Journal articles, research reports, conference papers
- Education-specific database (U.S. Department of Education)

**Indexed Fields Searched:**
- Title
- Abstract
- Descriptors (ERIC thesaurus terms)
- Author-supplied keywords

**Date Coverage:**
- 2015-2025 for this search
- Comprehensive coverage from 1966 onwards

**Export Format:**
- RIS, CSV, Plain text
- **Preferred:** RIS

**Expected Contribution:**
- AI adoption in K-12 and higher education settings
- Student and instructor perspectives on educational AI
- Intelligent tutoring systems, AI-powered learning platforms
- AI writing assistants in academic contexts

**ERIC Thesaurus Terms Used:**
```
Artificial Intelligence (Descriptor)
Educational Technology (Descriptor)
Technology Uses in Education (Descriptor)
Technology Acceptance (Descriptor)
Student Attitudes (Descriptor)
Teacher Attitudes (Descriptor)
Computer Assisted Instruction (Descriptor)
Machine Learning (Descriptor)
```

**Filters Applied:**
- Publication Type: Journal Articles, Reports - Research
- Education Level: (no filter - all levels K-12 through Higher Ed)
- Peer Reviewed: Yes
- Publication Date: 2015-2025

**Unique Value:**
- Only education-specific database in the search
- Strong coverage of pedagogical AI applications
- Practitioner and researcher perspectives
- Cross-level education research (K-12, undergraduate, graduate)

---

### Education Source

**Coverage:**
- 2,800+ education journals and periodicals
- Research reports and education-related documents
- Practitioner-focused publications
- Published by EBSCO

**Indexed Fields Searched:**
- Title
- Abstract
- Subject terms
- Author keywords

**Date Coverage:**
- 2015-2025 for this search
- Comprehensive from 1980s onwards

**Export Format:**
- RIS, BibTeX, CSV
- **Preferred:** RIS

**Expected Contribution:**
- Practitioner-focused AI adoption in education
- Teaching and learning with AI technologies
- AI integration in curriculum and instruction
- Educational administrator perspectives

**Filters Applied:**
- Document Type: Academic Journals, Reports
- Language: English
- Publication Date: 2015-2025

**Unique Value:**
- Practitioner and policy perspectives on AI in education
- Implementation studies in real classroom settings
- AI adoption barriers and facilitators in schools
- Professional development for AI integration

---

## Field Mapping Across Databases

| Concept | WoS Field | Scopus Field | PsycINFO Field | IEEE Field | ACM Field | ERIC Field | Education Source Field |
|---------|-----------|--------------|----------------|------------|-----------|------------|------------------------|
| AI Technology | Topic (TS) | TITLE-ABS-KEY | Title/Abstract | Abstract | Title/Abstract | Descriptors + Text | Subject + Text |
| Adoption | Topic (TS) | TITLE-ABS-KEY | Thesaurus + Text | Abstract | Title/Abstract | Descriptors + Text | Subject + Text |
| Education Context | Topic (TS) | TITLE-ABS-KEY | Thesaurus + Text | Full text | Full text | Descriptors (primary) | Subject (primary) |
| Methodology | Topic (TS) | TITLE-ABS-KEY | Methodology Filter | Full text | Full text | Abstract | Abstract |

## Duplicate Handling Strategy

### Expected Overlap Rates
- WoS ↔ Scopus: 60-70% (both multidisciplinary, high-quality journals)
- IEEE ↔ ACM: 40-50% (computing overlap)
- PsycINFO ↔ WoS/Scopus: 30-40% (psychology journals indexed in multidisciplinary DBs)
- ERIC ↔ Education Source: 50-60% (both education-focused)
- ERIC ↔ PsycINFO: 30-40% (educational psychology overlap)
- ERIC ↔ WoS/Scopus: 20-30% (major education journals in multidisciplinary DBs)
- Education Source ↔ WoS/Scopus: 15-25% (practitioner journals less indexed)
- Any DB ↔ Google Scholar: 80-90% (GS indexes almost everything)

### Deduplication Protocol

**Step 1: Automated Deduplication (Zotero)**
- Match on DOI (highest priority)
- Match on Title + First Author + Year
- Match on PMID, ISBN (if applicable)

**Step 2: Manual Review of Near-Duplicates**
- Same authors, similar titles, same year → likely duplicate
- **Priority rule:** Keep version with most complete data
  1. Journal article > conference paper (if both available)
  2. Final published version > preprint
  3. Version with correlation matrix > version without

**Step 3: Duplicate Sample Identification**
- Same author team + overlapping data collection period → flag as potential duplicate sample
- Review methodology sections during full-text screening
- If duplicate samples confirmed: keep most complete analysis

### Duplicate Tracking
Create `duplicates_log.csv`:
- original_id
- duplicate_id
- match_reason (DOI, title, etc.)
- resolution (kept, removed)
- kept_version_source

---

## Export Formats and Metadata Completeness

| Database | Format | DOI Coverage | Abstract Coverage | Keywords Coverage | Full-Text Link |
|----------|--------|--------------|-------------------|-------------------|----------------|
| Web of Science | RIS | 95%+ | 100% | 100% | Via library resolver |
| Scopus | RIS | 98%+ | 100% | 100% | Via library resolver |
| PsycINFO | RIS | 90%+ | 100% | 100% (Thesaurus) | Via library resolver |
| IEEE | BibTeX | 100% | 100% | 95% | Direct IEEE links |
| ACM | BibTeX | 100% | 100% | 90% (CCS codes) | Direct ACM links |
| ERIC | RIS | 85%+ | 100% | 100% (Descriptors) | Via ERIC or library |
| Education Source | RIS | 80%+ | 100% | 95% (Subject terms) | Via EBSCOhost |

**Quality Check:**
- Verify DOI presence in ≥90% of exported records
- Verify abstract presence in 100% of exported records
- If missing, manually retrieve from publisher website

---

## Search Execution Tracking

### Log Template

```csv
database,search_date,search_time,n_results,filters_applied,exported_file
Web of Science,2026-02-16,10:30,450,"Article|Proceedings; EN; 2015-2025; Education context",wos_export_20260216.ris
Scopus,2026-02-16,11:15,580,"Article|ConferencePaper; EN; Final; 2015-2025; Education context",scopus_export_20260216.ris
PsycINFO,2026-02-16,14:00,320,"Quantitative; EN; 2015-2025; Educational context",psycinfo_export_20260216.ris
IEEE Xplore,2026-02-16,15:30,210,"Journals|Conferences; 2015-2025; Education context",ieee_export_20260216.bib
ACM Digital Library,2026-02-16,16:45,180,"Research Article|Proceedings; 2015-2025",acm_export_20260216.bib
ERIC,2026-02-16,09:00,350,"Peer Reviewed; Journal Articles; 2015-2025",eric_export_20260216.ris
Education Source,2026-02-16,13:30,220,"Academic Journals; EN; 2015-2025",edusource_export_20260216.ris
```

---

## Database Access and Institutional Subscriptions

**Institutional Access Required:**
- Web of Science: Yes (institutional subscription)
- Scopus: Yes (institutional subscription)
- PsycINFO: Yes (via EBSCOhost or Ovid)
- IEEE Xplore: Partial (many open access; subscription for full access)
- ACM Digital Library: Partial (ACM membership or institutional subscription)
- ERIC: No (free, public access via eric.ed.gov)
- Education Source: Yes (via EBSCOhost subscription)
- Google Scholar: No (free, public access)

**Access Verification:**
- Confirm institutional access to all databases before search execution
- Verify VPN access for off-campus searching
- Document subscription coverage dates

---

## Expected Study Yield

### Optimistic Scenario (Education-Focused)
- Total raw hits: 2,500-3,000
- After deduplication: 1,500-2,000
- After title/abstract screening: 200-350
- After full-text review: 60-80 included studies

### Conservative Scenario (Education-Focused)
- Total raw hits: 1,500-2,000
- After deduplication: 1,000-1,200
- After title/abstract screening: 100-200
- After full-text review: 40-60 included studies

### Target
- **k ≥ 40 studies** for stable MASEM estimates in education-specific context
- **N > 10,000 total participants** for adequate power
- **≥8 studies per correlation cell** for Stage 1 TSSEM

---

## Quality Indicators by Database

| Database | Peer Review | Impact Factor Filter | Methodology Filter | Citation Data |
|----------|-------------|----------------------|--------------------|---------------|
| Web of Science | Yes | Yes (JCR quartiles) | No | Yes (cited reference search) |
| Scopus | Yes | Yes (CiteScore) | No | Yes (Scopus API) |
| PsycINFO | Yes | No | Yes (Empirical/Quantitative) | Limited |
| IEEE Xplore | Yes (IEEE-sponsored) | No | No | Yes (IEEE Xplore API) |
| ACM Digital Library | Yes | No | No | Yes (ACM DL API) |
| ERIC | Mixed (filter available) | No | No | Limited |
| Education Source | Yes (filter available) | No | No | Limited |

---

## References

Bramer, W. M., Rethlefsen, M. L., Kleijnen, J., & Franco, O. H. (2017). Optimal database combinations for literature searches in systematic reviews: A prospective exploratory study. *Systematic Reviews*, 6(1), 245.

Gusenbauer, M., & Haddaway, N. R. (2020). Which academic search systems are suitable for systematic reviews or meta-analyses? Evaluating retrieval qualities of Google Scholar, PubMed, and 26 other resources. *Research Synthesis Methods*, 11(2), 181-217.
