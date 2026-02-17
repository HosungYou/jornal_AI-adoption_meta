# Systematic Literature Search Strategy

## Overview

This document outlines the systematic search strategy for identifying empirical studies on AI technology adoption and acceptance suitable for meta-analytic structural equation modeling (MASEM).

## Search Databases

### Primary Databases

1. **Web of Science (Core Collection)**
   - Coverage: Multidisciplinary, high-quality journals
   - Justification: Comprehensive coverage of technology adoption research

2. **Scopus**
   - Coverage: Broader than WoS, includes more regional journals
   - Justification: Captures AI adoption studies in emerging markets

3. **PsycINFO**
   - Coverage: Psychology, educational psychology, and behavioral sciences
   - Justification: Strong coverage of individual acceptance, attitudes, and educational technology research

4. **IEEE Xplore**
   - Coverage: Engineering and computer science
   - Justification: Early AI adoption studies, technical implementations, educational technology

5. **ACM Digital Library**
   - Coverage: Computing and information technology
   - Justification: Human-computer interaction, AI user experience research

6. **ERIC (Education Resources Information Center)**
   - Coverage: Education research, K-12 through higher education
   - Justification: 1.6M+ records, strongest education-specific database for AI in teaching and learning

7. **Education Source**
   - Coverage: Education journals and professional reports
   - Justification: Practitioner-focused AI in education research, pedagogical technology adoption

### Supplementary Sources

6. **Google Scholar**
   - Purpose: Backward/forward citation searching, grey literature scanning
   - Justification: Identify recent preprints, working papers, and highly cited non-indexed work
   - Limitation: Not used for primary systematic search due to lack of reproducibility

## Search String

### Core Search String

```
("artificial intelligence" OR "AI" OR "machine learning" OR "deep learning" OR
"generative AI" OR "ChatGPT" OR "large language model" OR "LLM" OR "neural network" OR
"intelligent system" OR "cognitive computing" OR "automated decision" OR "algorithmic system" OR
"intelligent tutoring system" OR "ITS" OR "AI tutor" OR "AI writing assistant" OR
"automated grading" OR "AI-powered learning")

AND

("adoption" OR "acceptance" OR "intention" OR "use" OR "usage" OR "TAM" OR "UTAUT" OR
"technology acceptance model" OR "unified theory" OR "behavioral intention" OR
"user acceptance" OR "continuance" OR "post-adoption")

AND

("correlation" OR "structural equation" OR "SEM" OR "path analysis" OR "path model" OR
"regression" OR "covariance" OR "empirical" OR "quantitative" OR "survey")

AND

("education" OR "educational" OR "learning" OR "teaching" OR "student" OR "instructor" OR
"classroom" OR "higher education" OR "K-12" OR "university" OR "pedagogical" OR "academic")
```

### Database-Specific Adaptations

**Web of Science & Scopus**: Use full search string in Title/Abstract/Keywords fields

**PsycINFO**: Add thesaurus terms:
- "Artificial Intelligence" (Thesaurus term)
- "Technology Adoption" (Thesaurus term)
- "User Attitudes" (Thesaurus term)
- "Educational Technology" (Thesaurus term)
- "Computer Assisted Instruction" (Thesaurus term)

**IEEE Xplore**: Adjust to metadata fields:
- ("Abstract": artificial intelligence) AND ("Abstract": adoption OR acceptance)

**ACM Digital Library**: Use ACM Computing Classification System filters:
- Human-centered computing → Human computer interaction (HCI)

**ERIC**: Use ERIC thesaurus terms:
- "Artificial Intelligence" (Thesaurus term)
- "Educational Technology" (Thesaurus term)
- "Technology Uses in Education" (Thesaurus term)
- "Technology Acceptance" (Thesaurus term)

**Education Source**: Field search in Title/Abstract/Keywords with full search string

## Inclusion Parameters

### Date Range
**January 1, 2015 – December 31, 2025**

Rationale:
- 2015: Modern deep learning era begins (AlexNet aftermath, widespread commercial AI)
- 2025: Generative AI boom and maturation
- 10-year window balances recency with sufficient study accumulation

### Language
**English only**

Rationale:
- Construct harmonization requires consistent language
- Translation quality varies; semantic drift threatens construct validity
- >90% of meta-analytic SEM studies are English-only

### Publication Types
**Peer-reviewed journal articles and conference proceedings with full papers**

Included:
- Empirical research articles
- Full conference papers with complete methodology

Excluded:
- Editorials, commentaries, opinion pieces
- Book chapters (unless reporting original empirical data)
- Dissertations (to avoid overlap with published versions)
- Posters and extended abstracts

## Search Fields

### Primary Fields
1. **Title**: High-precision capture of AI adoption focus
2. **Abstract**: Broader capture, includes methodology keywords
3. **Keywords**: Author-assigned and database-indexed terms

### Field Combination Logic
(Title OR Abstract OR Keywords) for all search terms

## Search Execution Protocol

### Step 1: Database Searches (Week 1-2)
- Execute search string in each database
- Export results to reference management software (Zotero)
- Record:
  - Database name
  - Search date
  - Number of results
  - Search string used

### Step 2: Deduplication (Week 2)
- Automated deduplication in Zotero
- Manual review of near-duplicates (same authors, similar titles)
- Priority rule: Keep version with most complete data (journal > conference)

### Step 3: Backward Citation Searching (Week 3-4)
- Review reference lists of included studies
- Identify highly cited foundational papers (TAM, UTAUT, AI trust)
- Add eligible studies not captured in database search

### Step 4: Forward Citation Searching (Week 3-4)
- Use Google Scholar "Cited by" for included studies
- Identify recent studies citing seminal AI adoption papers
- Add eligible studies published after database search dates

## PRISMA 2020 Flow Diagram Structure

```
┌─────────────────────────────────────────────────────┐
│  IDENTIFICATION                                      │
├─────────────────────────────────────────────────────┤
│  Database searching:                                 │
│    - Web of Science: n = ____                        │
│    - Scopus: n = ____                                │
│    - PsycINFO: n = ____                              │
│    - IEEE Xplore: n = ____                           │
│    - ACM Digital Library: n = ____                   │
│    - ERIC: n = ____                                  │
│    - Education Source: n = ____                      │
│                                                      │
│  Other sources:                                      │
│    - Citation searching: n = ____                    │
│    - Hand searching: n = ____                        │
│                                                      │
│  Total identified: n = ____                          │
│  Duplicates removed: n = ____                        │
│  Records screened: n = ____                          │
└─────────────────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────────────────┐
│  SCREENING                                           │
├─────────────────────────────────────────────────────┤
│  Records excluded (title/abstract): n = ____        │
│    - Not AI technology: n = ____                     │
│    - Not adoption/acceptance: n = ____               │
│    - Qualitative only: n = ____                      │
│    - Conceptual/review: n = ____                     │
│    - Other reasons: n = ____                         │
│                                                      │
│  Full-text articles assessed: n = ____               │
└─────────────────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────────────────┐
│  ELIGIBILITY                                         │
├─────────────────────────────────────────────────────┤
│  Full-text articles excluded: n = ____               │
│    - No correlation matrix/β: n = ____               │
│    - No target constructs: n = ____                  │
│    - Sample size < 50: n = ____                      │
│    - Duplicate sample: n = ____                      │
│    - Other reasons: n = ____                         │
└─────────────────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────────────────┐
│  INCLUDED                                            │
├─────────────────────────────────────────────────────┤
│  Studies included in meta-analysis: k = ____         │
│  Total sample size: N = ____                         │
└─────────────────────────────────────────────────────┘
```

## Citation Chasing Strategy

### Backward Searching
1. **Seminal Papers** (always review their references):
   - Venkatesh et al. (2003) UTAUT
   - Davis (1989) TAM
   - Recent AI adoption reviews (2020-2025)

2. **Inclusion Rule**: Reference must meet all inclusion criteria

3. **Stopping Rule**: Continue until no new eligible studies found in 2 consecutive highly cited papers

### Forward Searching
1. **Seed Papers**: Top 20 most-cited AI adoption papers from database search
2. **Tool**: Google Scholar "Cited by" function
3. **Recency Focus**: Prioritize citations from 2023-2025 (generative AI era)
4. **Stopping Rule**: Sample 50 most recent citations per seed paper

## Search Documentation

### Required Documentation Per Search
- Search query (exact syntax)
- Database name and platform
- Search date and time
- Filters applied (date, language, document type)
- Number of results
- Export format and file name

### Reproducibility File
Create `search_log.csv` with columns:
- database
- search_date
- search_string
- filters_applied
- n_results
- file_exported

## Quality Control

### Pre-Search Validation
- Test search string on known relevant studies (benchmark set of 10 known AI adoption papers)
- Sensitivity: ≥80% of benchmark papers should be retrieved
- If <80%, refine search terms

### Post-Search Validation
- Random sample of 100 excluded records reviewed by second screener
- False negative rate should be <5%

## Timeline

| Week | Activity | Deliverable |
|------|----------|-------------|
| 1 | Execute database searches | Raw citation export files |
| 2 | Deduplication, initial screening setup | Deduplicated library |
| 3-4 | Citation chasing | Expanded candidate pool |
| 5-6 | Title/abstract screening | Eligible full-text list |
| 7-8 | Full-text review | Final included studies list |

## Ethical Considerations

- All databases accessed through institutional subscriptions
- No copyright violations in PDF acquisition
- PRISMA reporting ensures transparency
- Registration with PROSPERO or OSF for transparency

## References

Page, M. J., McKenzie, J. E., Bossuyt, P. M., Boutron, I., Hoffmann, T. C., Mulrow, C. D., ... & Moher, D. (2021). The PRISMA 2020 statement: An updated guideline for reporting systematic reviews. *BMJ*, 372, n71.

Xiao, Y., & Watson, M. (2019). Guidance on conducting a systematic literature review. *Journal of Planning Education and Research*, 39(1), 93-112.
