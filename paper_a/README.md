# Paper A: AI Adoption in Education — Meta-Analytic Structural Equation Modeling (MASEM)

## Target Journal
**Computers & Education** (Impact Factor 12.0)

## Research Overview
This study conducts a comprehensive meta-analytic structural equation modeling (MASEM) analysis of AI adoption in educational settings (2015-2025). It integrates 12 theoretical constructs from TAM/UTAUT frameworks—including performance expectancy, effort expectancy, trust, anxiety, and AI transparency—to model the structural relationships driving AI adoption among students, instructors, and administrators.

## Scope
Paper A covers the **full pipeline** from literature identification to MASEM analysis:
- Systematic search across 10 databases (22,166 records)
- Deduplication (22,166 → 16,189)
- Three-tier AI-assisted screening (16,189 → 575 AI-include)
- Human verification of screening decisions
- Full-text eligibility assessment
- Data extraction (AI-assisted + human verification)
- MASEM analysis with moderator testing

## Relationship to Paper B
Paper B (targeting *Research Synthesis Methods*) focuses exclusively on **LLM-assisted data extraction methodology** using a 100-study subsample. Paper A is the **parent meta-analysis** that Paper B references for screening and eligibility procedures.

## Key Numbers
| Stage | Records |
|-------|---------|
| Identified | 22,166 |
| After deduplication | 16,189 |
| AI-screened include | 575 |
| AI conflict | 175 |
| Uncertain | 714 |
| Human review queue | 1,457 |
| Final included | TBD |

## Directory Structure
```
paper_a/
├── README.md                    # This file
├── SCREENING_PROTOCOL.md        # 3-Tier AI screening methodology
├── SEARCH_STRATEGY.md           # Database search strategy and execution
├── DATA_EXTRACTION_PLAN.md      # Extraction protocol for MASEM variables
├── ANALYSIS_PLAN.md             # MASEM analysis methodology
├── RESEARCHER_ROLES.md          # Team roles and responsibilities
├── JOURNAL_STRATEGY.md          # Submission strategy for C&E
├── TIMELINE.md                  # Project timeline and milestones
├── DISCUSSION_LOG_KR.md         # Research discussion log (Korean)
├── checklists/
│   └── PRISMA_2020_checklist.md
├── data/
│   ├── 00_search_records/       # Raw search results per database
│   ├── 01_deduplication/        # Deduplication logs and results
│   ├── 02_screening/            # Screening data by tier
│   │   ├── tier1_keyword/
│   │   ├── tier2_single_ai/
│   │   ├── tier3_dual_ai/
│   │   └── human_verification/  # Human review sheets and IRR data
│   ├── 03_eligibility/          # Full-text eligibility assessment
│   ├── 04_extraction/           # Data extraction pipeline
│   │   ├── ai_extraction/
│   │   ├── human_coding/
│   │   └── consensus/
│   └── 05_analysis/             # Final analysis datasets
├── manuscript/
├── scripts/
├── templates/
└── prompts/
```

## Reporting Standards
- PRISMA 2020 Statement
- MARS (Meta-Analysis Reporting Standards, APA)
