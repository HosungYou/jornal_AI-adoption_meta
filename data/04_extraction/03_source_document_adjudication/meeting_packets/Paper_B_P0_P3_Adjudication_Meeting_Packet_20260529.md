# Paper B P0-P3 Source Adjudication Meeting Packet

Date: 2026-05-29

Purpose: convert the accepted Paper B tolerance and priority rules into a
meeting-ready packet so Step 3 source-document adjudication can move toward the
Step 4 reference freeze.

## Entry Condition

Use this packet only with the combined Phase 1+2 pre-adjudication artifacts:

- `data/04_extraction/02_pre_adjudication_disagreement/combined/derived/combined_correlation_review_queue_20260525.csv`
- `data/04_extraction/02_pre_adjudication_disagreement/combined/derived/combined_pairwise_disagreement_long_20260525.csv`
- `data/04_extraction/02_pre_adjudication_disagreement/combined/derived/combined_study_review_queue_20260525.csv`

Do not edit raw coder workbooks during the meeting. Record final values only in
the adjudication log and then in the adjudicated reference dataset.

## Meeting Goal

Produce source-anchored decisions for the highest-consequence disagreements
before the reference freeze.

Minimum decision fields for each item:

- Study ID.
- Phase block and pair.
- Field or construct pair.
- Raw coder values.
- Source table/page/section.
- Evidence type.
- Final adjudicated value or exclusion decision.
- Rule applied.
- Rationale.
- Adjudicator and date.
- Follow-up needed before freeze.

## Priority Rules

| Priority | Trigger | Meeting action |
|---|---|---|
| P0 immediate | Inclusion/exclusion split, different analytic sample, coefficient outside valid bounds, sign reversal, HTMT-only as r, Fornell-Larcker diagonal as r, duplicate/review-source issue | Resolve before dependent rows are finalized. |
| P1 high | A4 difference, one-coder-only focal matrix value, source-type mismatch, construct ambiguity involving ATT/TRU/ANX/FC/SE, matrix reconstruction failure | Source-check and record the rule applied. |
| P2 standard | A3 difference, repeated A2 differences, reliability/material measurement discrepancy, moderator boundary disagreement | Source-check before freeze after P0/P1 rows. |
| P3 low | A0/A1 rounding-only, metadata spelling/capitalization, DOI/title normalization, non-focal formatting | Standardize after high-consequence rows; preserve raw disagreement. |

## First Agenda

1. Confirm duplicate/review-source blockers from the LongTable status:
   S195/S206 duplicate-source issue and S014/S021/S056/S092/S121/S202
   review-source decisions.
2. Review A5 rows from the RQ0 report:
   S207, S072, S046, S007, S164, S070, and S183.
3. Review A4 rows with focal construct pairs:
   ANX-BI, ANX-PE, BI-PE, ATT-BI, PE-UB, EE-SE, and FC-UB.
4. Review one-coder-only focal matrix rows from
   `combined_correlation_review_queue_20260525.csv`.
5. Mark P3 metadata/rounding cleanup rows for batch standardization outside the
   main adjudication meeting.

## Researcher Decisions Already Resolved

Recorded 2026-06-08:

| Study or issue | Decision | Meeting implication |
|---|---|---|
| S195/S206 | Use S195 as the canonical duplicate audit row; mark S206 as duplicate of S195. | Record exclusion/duplicate decision and remove duplicated source from the target matrix count. |
| S014 indirect effects | Exclude indirect effects through perceived risk as direct target-pair values. | Do not freeze R1's indirect PE/SI -> perceived-risk -> adoption rows as MASEM-ready values. |
| S014 population | Treat academic researchers/faculty as eligible under the Paper B educational-population rule. | Do not exclude S014 on population grounds; retain or exclude only after source-checking usable direct target-pair evidence. |
| S021 time points | Use separate T1/T2 strata. | Do not pool pre- and post-training coefficients. |
| S014/S021/S056/S092 source access | PDFs were found in the local OneDrive PDF archive and copied into the ignored adjudication source-PDF folder. S021 online supplement files were also recovered from Springer. | Do not remove these studies from the freeze queue for missing PDFs; S021 is now included through the limited main-PDF primary Model 1 row set because Supplementary Table S4 is `f Squared` only. |
| S121 samples | Treat students and teachers as separate samples if teacher values are extracted. | Do not pool student and teacher estimates. |
| S202 focal technology | Exclude AI-driven LMS administrative automation from the Paper B AI-adoption target universe. | Record as target-matrix exclusion despite local numeric SEM evidence. |

## Source-Value Decisions Already Logged

Recorded in `data/04_extraction/03_source_document_adjudication/phase2/decision_log_20260608.md`:

| Study | Logged status | Meeting implication |
|---|---|---|
| S195/S206 | Duplicate/exclusion decision logged. | Use S195 as canonical and do not count S206 as a second source. |
| S202 | Target-matrix exclusion decision logged. | Exclude AI-driven LMS administrative automation despite local numeric evidence. |
| S014 | No direct standardized mapped target-pair coefficient found after excluding indirect perceived-risk paths and HTMT. | Remove R1's two indirect-effect candidate rows from the target matrix in the Step 4 draft. |
| S056 | Table 2 source-reported construct correlations supersede R2's Table 3 beta-converted path rows if retained. | Use `ATT-EE = 0.816`, `ATT-PE = 0.803`, `EE-PE = 0.854`, unless the researcher overrides the evidence-type rule. |
| S092 | Table 3 standardized SEM paths confirm R3's three target rows under the beta-to-r rule. | Carry source betas `BI-EE beta = 0.174`, `BI-PE beta = 0.234`, and `EE-PE beta = 0.354`; Step 4 converted `r` values are `0.224`, `0.284`, and `0.404`. |
| S021 | Main PDF and Springer online supplement checked; Supplementary Table S4 is `f Squared` only; researcher decision is to include the limited main-PDF primary Model 1 row set. | Apply T1/T2 beta-converted rows from `s021_primary_model_row_set_20260608.md`; do not treat Table S4 as a coefficient source. |
| S121 | Figure 2 student/teacher heatmaps checked and row set transcribed in `s121_figure2_row_set_20260608.md`. | Apply separate student/teacher rows in Step 4; correct student `FC-UB` to `0.29` and student `PE-SE` to `0.40`; carry `SE` as medium-confidence subjective-competence/self-efficacy mapping. |

Assignment check for the source-review studies:

| Study | Phase/pair | Assigned coders |
|---|---|---|
| S014 | Phase 2 Pair C | R1 + R4 |
| S021 | Phase 2 Pair D | R2 + R3 |
| S056 | Phase 2 Pair D | R2 + R3 |
| S092 | Phase 2 Pair D | R2 + R3 |

## Remaining Meeting Work

1. Apply the logged S195/S206, S202, S014, S021, S056, S092, and S121 decisions only in the
   Step 4 reference draft, not in raw coder workbooks.

## Decision Log Template

```markdown
### S### - short label

- Phase/pair:
- Field or construct pair:
- Raw values:
  - R#:
  - R#:
- Source location:
- Evidence type:
- Priority: P0/P1/P2/P3
- Decision:
- Rule applied:
- Rationale:
- Adjudicator:
- Date:
- Follow-up:
```

## Ready-To-Freeze Exit Check

Before Step 4 reference freeze:

- Every included study has one final status.
- Every exclusion has an exclusion code and source-backed rationale.
- Every retained correlation/path row has one evidence type.
- HTMT-only values are excluded from target correlations.
- Fornell-Larcker diagonal values are not used as correlations.
- Construct mappings are consistent with the current coding manual.
- Sample/subgroup decisions are documented before dependent numeric rows are
  finalized.
- Rounding-only rows are marked as such rather than escalated.
- Meaningful discrepancies have decision-log entries.
- Raw coder files remain preserved as pre-adjudication evidence.
