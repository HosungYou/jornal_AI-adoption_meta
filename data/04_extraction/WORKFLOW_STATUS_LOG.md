# Extraction Workflow Status Log

## Current Status Snapshot

**Date:** 2026-05-06

**Current stage:** Step 3 is in progress for Phase 1. The project has completed
Phase 1 raw coding and has a Phase 1 pairwise comparison workbook. Source-document
adjudication decisions have started, but the source-anchored adjudicated human
reference standard has not been frozen. Phase 2 distribution packages have been
generated, and a 17-study R1 Pair C working coding batch has been documented,
but Phase 2 raw-coder returns have not been frozen.

**Do not start Step 5** LLM comparison or MASEM substitution as a current result
until Step 4 has a frozen reference file.

## Five-Step Workflow

| Step | Name | Entry criterion | Exit criterion | Status |
|---:|---|---|---|---|
| 1 | Raw human coder data freeze | Independent coder workbooks are submitted and preserved | Raw files are read-only; no consensus overwrites | Phase 1 complete; Phase 2 packages generated; partial R1 Pair C working batch documented |
| 2 | Pre-adjudication human-human disagreement analysis | Raw coder data are frozen | Pairwise differences summarized by field, study, pair, and numeric tolerance | Phase 1 workbook created; summary still needs final export |
| 3 | Source-document adjudication | Pairwise differences are available | Every discrepancy has a source-anchored decision and rationale | Phase 1 in progress |
| 4 | Reference standard freeze | Adjudication is complete | Frozen reference file and freeze log are committed | Not started |
| 5 | LLM comparison + MASEM substitution | Reference standard is frozen | LLM accuracy, triage, and substitution outputs are generated | Not started |

## Status Log

| Date | Stage | Event | Evidence | Next action |
|---|---|---|---|---|
| 2026-04-24 | Step 1 | Phase 1 raw R1 updates completed through S033 | `03_source_document_adjudication/phase1/decision_log_20260424.md` | Finish adjudication propagation into final extraction data |
| 2026-04-24 | Step 2 | Phase 1 pairwise comparison workbook created | `02_pre_adjudication_disagreement/phase1/AI_Adoption_Phase1_Pairwise_Comparison_R1R2_R3R4_20260424.xlsx` | Export final raw disagreement summary |
| 2026-04-25 | Step 0 | Active extraction workspace simplified into numbered folders | `data/04_extraction/README.md` | Keep future artifacts in numbered stage folders |
| 2026-04-25 | Step 3 | Current status clarified: adjudication in progress, reference not frozen | This file | Continue source-document adjudication before LLM comparison |
| 2026-04-25 | Step 3 | Early coding decisions checked against frozen raw workbooks | `03_source_document_adjudication/phase1/coding_decision_application_check_20260425.md` | Apply reviewed decisions in the adjudicated reference rather than editing raw workbooks |
| 2026-04-25 | Step 1 | Phase 2 combined coder workbooks generated for distribution | `01_raw_human_coder_data_freeze/phase2/coder_packages/` | Distribute files and freeze returned completed coder workbooks |
| 2026-05-01 | Step 2/3 | R1-R4 pairwise comparison and source-document adjudication workflow documented | `02_pre_adjudication_disagreement/RATER_COMPARISON_PLAYBOOK.md` | Use the playbook to triage meaningful differences before source-document adjudication |
| 2026-05-01 | Step 0 | Date-stamped coding transfer area added for operational file exchange | `06 coding by date/README.md` | Use date folders for share-safe coding packets, then move finalized artifacts into canonical workflow folders |
| 2026-05-06 | Step 1 | Phase 2 R1 Pair C 17-study working coding batch documented; `S136` HM exclusion correction recorded | `06 coding by date/2026-05-06/README.md`; `06 coding by date/2026-05-06/r1_pairc_17_study_coding_notes.md` | Preserve the local workbook outside Git unless approved for raw freeze; compare against R4 when Pair C returns are available |

## Coding Decisions Already Reflected

The following early coding discussions are reflected in the current Phase 1
decision log and protocol documents. Some raw coder workbook cells intentionally
still preserve pre-adjudication values; use Step 3 and Step 4 to apply final
source-anchored decisions.

- S164: Set `EE-SI = -0.024`, `FC-PE = 0.716`, and `PE-UB = 0.632`.
- S091: Use sample size `N = 382`; code the tool as ChatGPT-specific and keep
  the statistical coding decision.
- S187: Treat stress/anxious mapping as flagged and mapped to `ANX` pending
  adjudication record completion.
- S079: Treat the relevant effects as path coefficients.
- S223: Use the R1-coded value.
- S005: Exclude `JOY`; do not map `CON -> FC`; do not adopt `FC` for that case.
- S044: Use GAAIS Positive Attitudes toward AI as primary `ATT`; do not average
  Negative Attitudes into primary `ATT`.
- S054: Use teacher-only sample and exclude the high-school student sample; do
  not map Perceived Playfulness to `ATT`.
- S011: Exclude TTF paths from `FC` mapping.
- S180: Exclude from MASEM correlation contribution because no usable target
  construct-pair `r` or beta matrix is available.
- S220: Exclude because the focal use case is mental healthcare chatbot/content,
  not educational AI adoption.
- S151: Use source-reported `FC-UB = .558`; preserve source-reported
  three-decimal correlations during adjudication.
- S087: Exclude Satisfaction from `ATT`; do not treat
  `Satisfaction-Performance Expectancy` as `ATT-PE`.
- S051: Do not map Perceived Risk to `ANX`; include R1 direct values
  `EE-FC = .59`, `EE-PE = .48`, and `FC-PE = .47`.
- S120: Use R1 beta-converted path-coefficient values for `BI-EE`, `BI-FC`,
  `BI-PE`, `BI-SI`, and `BI-UB`; exclude R2-only `SI-TRU`, `SI-UB`, and
  `TRU-UB` rows.
- HTMT-only tables are not treated as usable MASEM correlation matrices.
- S081: Use R1 values for unresolved R1-R2 correlation differences.
- S035: Use R1 values for unresolved R1-R2 correlation differences.
- S191: Use R2 values for unresolved R1-R2 correlation differences.
- S217: Use R1 values for unresolved R1-R2 correlation differences.
- S033: Use R1 beta-converted path-coefficient values; retain `ATT-EE = .06`
  from beta `.013`.

## Required Update Rule

Whenever the project advances from one step to the next, add a new row to the
status log and cite the file that proves the transition.
