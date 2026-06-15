# Paper A: AI Adoption in Education — Model-Family MASEM

## Current status

Paper A is currently framed as a model-family MASEM manuscript.

- `full10` is the theoretical 10-construct target and evidence map.
- `core7` and `trust6` are the empirical model-family MASEM routes.
- `ANX` and `SE` remain theory-relevant but are currently underidentified for primary complete-case MASEM.
- The current Word manuscript contains real model-family results, but tables, figures, and PRISMA reporting still need a submission-readiness pass.

## Relationship to Paper B
Paper B (targeting *Research Synthesis Methods*) focuses exclusively on **LLM-assisted data extraction methodology** using a 100-study subsample. Paper A is the **parent meta-analysis** that Paper B references for screening and eligibility procedures.

## Researcher handoff

Read this first:

- `paper_a/RESEARCHER_README.md`
- `paper_a/PRISMA_COUNTS_REVIEW_NEEDED_20260615.md`

Current draft:

- `paper_a/manuscript/target_journal/apa7_model_family_full_manuscript_scaffold_20260615/PAPER_A_APA7_SUBMISSION_STRENGTHENED_INLINE_MANUSCRIPT_20260615.docx`

## PRISMA count status

Current source files support these provisional counts:

| Stage | Count | Source |
| --- | ---: | --- |
| Records identified | 22,166 | `data/01_identification/dedup_report.txt` |
| Duplicates removed | 5,977 | `data/01_identification/dedup_report.txt` |
| Unique records after deduplication | 16,189 | `data/01_identification/dedup_report.txt` |
| Human-reviewed records | 657 | `data/02_screening/screening_summary.json` |
| Human-reviewed included records | 225 | `data/02_screening/screening_summary.json` |
| Human-reviewed excluded records | 432 | `data/02_screening/screening_summary.json` |

The prior repository status also reports `224` included, so a final PRISMA 2020 flow diagram is not locked yet. Resolve `224` versus `225` before submission.

## Submission-readiness gap

- Tables must be regenerated in APA 7th style without internal grid lines.
- A true PRISMA 2020 flow diagram must be generated after count lock.
- Path figures should be redesigned as publication-grade MASEM diagrams.
- Add a path estimate coefficient/forest plot and model-feasibility plot.
- External tables/figures are not reused directly; only reporting conventions should be borrowed.

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
