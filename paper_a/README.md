# Paper A: AI Adoption in Education — Model-Family MASEM

## Current status

Paper A is currently framed as a model-family MASEM manuscript.

- `full10` is the theoretical 10-construct target and evidence map.
- `core7` and `trust6` are the empirical model-family MASEM routes.
- `ANX` and `SE` remain theory-relevant but are currently underidentified for primary complete-case MASEM.
- The current Word manuscript contains real model-family results and rebuilt APA 7th-style body tables/figures.
- Final full-text eligibility exclusion boxes remain source-lock pending before journal submission.

## Relationship to Paper B
Paper B (targeting *Research Synthesis Methods*) focuses exclusively on **LLM-assisted data extraction methodology** using a 100-study subsample. Paper A is the **parent meta-analysis** that Paper B references for screening and eligibility procedures.

## Researcher handoff

Read this first:

- `paper_a/RESEARCHER_README.md`
- `paper_a/PRISMA_COUNTS_REVIEW_NEEDED_20260615.md`

Current draft:

- `paper_a/manuscript/target_journal/apa7_model_family_full_manuscript_scaffold_20260615/PAPER_A_APA7_TABLE_FIGURE_REBUILD_MANUSCRIPT_20260615.docx`

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
| Duplicate included DOI row | 1 | `paper_a/PRISMA_COUNTS_LOCK_20260615.md` |
| Unique included reports/studies | 224 | `paper_a/PRISMA_COUNTS_LOCK_20260615.md` |
| Local automated PDFs retrieved | 89 | `data/02_screening/pdf_download_log.json` |
| Local automated PDFs not downloaded/access needed | 136 | `data/02_screening/pdf_download_log.json` |

The current lock resolves the screening discrepancy as `225 - 1 duplicate included DOI row = 224` unique included reports/studies. Final full-text eligibility exclusion boxes are still not source-locked.

## Submission-readiness gap

- Tables have been regenerated in APA 7th style without internal grid lines.
- Figure 1 has been rebuilt as a portrait, stage-labeled, multi-box PRISMA 2020-style draft.
- Path figures have been redesigned as black-font publication-oriented MASEM diagrams.
- Path estimate coefficient and model-feasibility plots have been added.
- External tables/figures are not reused directly; only reporting conventions should be borrowed.
- Remaining blocker: final full-text eligibility exclusion boxes need source-locked team confirmation.

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

## 2026-06-15 Paper A APA table/figure rebuild

- Locked the current PRISMA include discrepancy as `225 included screening rows - 1 duplicate included DOI row = 224 unique included reports/studies`, pending final full-text box confirmation.
- Generated APA 7th table/figure rebuild manuscript: `paper_a/manuscript/target_journal/apa7_model_family_full_manuscript_scaffold_20260615/PAPER_A_APA7_TABLE_FIGURE_REBUILD_MANUSCRIPT_20260615.docx`.
- Generated PRISMA-style flow, theoretical genealogy, analytic workflow, revised full10 evidence map, core7/trust6 path diagrams, path coefficient plot, and model-feasibility plot.
- Updated OSF-ready package with the rebuilt manuscript, figures, and PRISMA count-lock files.
- Refined Figure 1 to a portrait, stage-labeled, multi-box PRISMA 2020-style draft; local automated PDF retrieval is reported separately from final full-text eligibility.
- OSF-ready zip: `paper_a/public_data_repository_20260615_osf_ready.zip`.
- OSF upload status: uploaded to the Paper A OSF component at https://osf.io/bwzgc/overview on 2026-06-16; uploaded file is `public_data_repository_20260615_osf_ready.zip`.

## 2026-06-16 LongTable panel submission draft

- Created a new submission-oriented Paper A draft after LongTable panel review: `paper_a/manuscript/target_journal/apa7_model_family_full_manuscript_scaffold_20260615/PAPER_A_LONGTABLE_PANEL_SUBMISSION_DRAFT_20260616.docx`.
- Created Korean writing guide for theory and Discussion: `paper_a/manuscript/target_journal/apa7_model_family_full_manuscript_scaffold_20260615/PAPER_A_THEORY_DISCUSSION_WRITING_GUIDE_KR_20260616.docx`.
- Main claim now uses the safer framing: theory-preserving estimability diagnosis of AI adoption mechanisms using model-family MASEM.
- The draft keeps `full10` as theoretical target/evidence map, `core7` and `trust6` as small-k complete-case model-family estimates, and `ANX`/`SE` as theory-retained but empirically underidentified future mechanisms.
- OSF component: https://osf.io/bwzgc/overview.
