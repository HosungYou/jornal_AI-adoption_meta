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
| After keyword filter (Phase 1) | 3,274 |
| AI 3-model screening (Phase 2) | 1,457 human review queue |
| Final included (full-text) | TBD (~300 MASEM-eligible expected) |

## Current Screening Pipeline (v8 — 2026-02-26)

**AI Models**: Gemini + Claude Sonnet 4.6 (Codex dropped — 85% uncertain, no discriminating power)

| Category | Count | Description |
|----------|-------|-------------|
| Auto-INCLUDE | 358 | Gemini + Claude both include |
| Auto-EXCLUDE | 15 | Gemini + Claude both exclude |
| TIER1 Conflict | 95 | include ↔ exclude direct conflict |
| TIER2 High | 495 | one include + one uncertain |
| TIER3 Low | 494 | uncertain + uncertain, etc. |
| **Total** | **1,457** | |

**Human Review Design (Option C: 2-Rater IRR + R1 Adjudicator)**:
- R2 + R3: 200 papers independent coding (IRR) → Cohen's κ
- R1 (PI): spot-check Auto-INCLUDE 86건 + TIER2 additional 150건
- R1 serves as adjudicator for R2-R3 disagreements
- Excel: `data/templates/human_review_sheet_v8.xlsx`

## Directory Structure
```
paper_a/
├── README.md                    # This file
├── DISCUSSION_LOG_KR.md         # Research discussion log (Korean)
├── checklists/                  # PRISMA 2020 checklist
├── data/
│   ├── 00_search_records/       # Raw search results per database
│   ├── 01_deduplication/        # Deduplication logs and results
│   ├── 02_screening/            # Screening data
│   │   ├── tier1_keyword/       #   Phase 1: keyword auto-filter
│   │   ├── tier2_single_ai/     #   Phase 2: AI multi-model screening
│   │   ├── tier3_dual_ai/       #   (legacy: merged into Phase 2)
│   │   └── human_verification/  #   Phase 3: human review + IRR
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
