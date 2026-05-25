# Decision: Phase 2 Returns, Source Checks, and Paper Readiness

Date: 2026-05-25

## Decision

Phase 2 R1-R4 returned coder workbooks are now preserved as raw returns and
separate freeze candidates. The project can begin Phase 2 pre-adjudication
disagreement analysis and source-document adjudication. Phase 1 and Phase 2 are
also now combined into full-corpus pre-adjudication outputs for the 213-study
Paper B validation corpus. Final Paper A, Paper B, and Paper C result claims
must wait until the source-anchored adjudicated human reference standard is
frozen.

## Files Accepted for Phase 2 Freeze Candidates

| Coder | Source used for freeze candidate | Notes |
|---|---|---|
| R1 | `AI_Adoption_MASEM_Coding_v3_R1_Phase0_1_2_completed_rows2_118_20260523.xlsx` | User approved using the completed rows 2-118 workbook while preserving the originally received R1 workbook separately. |
| R2 | `AI_Adoption_MASEM_Coding_v3_R2_Phase0_1_2_20260425_R2.xlsx` | Raw return preserved. |
| R3 | `AI_Adoption_MASEM_Coding_v3_R3_Phase0_1_2_20260425 (1).xlsx` | Latest `(합의) CORRELATIONS` sheet is treated as the current R3 work product. |
| R4 | `AI_Adoption_MASEM_Coding_v3_R4_Phase0_1_2_20260425_v2.xlsx` | Raw return preserved. |

## Structural Repairs

- Raw returned workbooks are preserved under
  `data/04_extraction/01_raw_human_coder_data_freeze/phase2/returned_raw/`.
- Freeze candidates are stored separately under
  `data/04_extraction/01_raw_human_coder_data_freeze/phase2/freeze_candidates/`.
- R3's `(합의) CORRELATIONS` sheet is promoted to `CORRELATIONS` in the freeze
  candidate.
- R3's original `CORRELATIONS` sheet is retained as
  `CORRELATIONS_original_return`.
- R3's duplicate column-G `original_beta` header is restored to `p_value`.

## Combined Phase 1+2 Outputs

The current pre-adjudication review basis is the full coding corpus:

| Component | Studies | Coder pairs |
|---|---:|---|
| Phase 1 | 100 | Pair A R1+R2; Pair B R3+R4 |
| Phase 2 | 113 | Pair C R1+R4; Pair D R2+R3 |
| Combined validation corpus | 213 | Four independent pair blocks |

The combined outputs are stored under
`data/04_extraction/02_pre_adjudication_disagreement/combined/`.
For meeting review, start with
`derived/combined_correlation_review_queue_20260525.csv` because it filters to
correlation, status, exclusion, and source-review issues. Use
`derived/combined_study_review_queue_20260525.csv` when metadata-only
differences also need to be audited. Use
`derived/combined_coder_values_long_20260525.csv` as the all-value long table
for reproducible analysis.

## Source-Check Decisions

The 2026-05-25 PDF checks support these confirmed exclusions:

| Study | Decision | Code | Reason |
|---|---|---|---|
| S039 | Exclude | E-FT3 | Dental diagnosis/clinical healthcare setting, not educational AI adoption. |
| S101 | Exclude | E-FT1 | ANN predictive-accuracy/factor-loading output, not usable target construct-pair statistics. |
| S108 | Exclude | E-FT1 | TAM/RIMMS group means and tests, not target construct-pair r or standardized path data. |
| S118 | Exclude | E-FT1 | Descriptive acceptance and use-frequency correlations, not an adoption-model inter-construct matrix or SEM path model. |
| S132 | Exclude | E-FT1 | Mentorship perception regressions/ratings, not usable AI-adoption construct-pair statistics. |
| S195 | Exclude | E-FT1 | Same DOI/PDF as S206; PLSR loadings and item-level correlation matrix, not construct-level MASEM statistics. |
| S206 | Exclude | E-FT1 | Same DOI/PDF as S195; PLSR loadings and item-level correlation matrix, not construct-level MASEM statistics. |
| S224 | Exclude | E-FT3 | Virtual learning/Google Classroom adoption, with AI only as possible enhancement. |

The following are not exclusions at this stage and require source adjudication:

| Study | Current action | Reason |
|---|---|---|
| S014 | Review source | R1 coded complete-sample indirect paths; R4 has no values. Need adjudication of indirect effects, construct mapping, and population eligibility. |
| S021 | Review source | Potentially usable genAI acceptance paths, but pre/post design requires handling rules. |
| S056 | Review source | R2 coded TAM PLS-SEM paths; R3 has no values. Need missing-side adjudication. |
| S092 | Review source | Appears to contain usable ChatGPT adoption SEM paths. |
| S121 | Review source | Appears to contain usable UTAUT/PLS-SEM paths. |
| S202 | Review source | Potentially usable SEM paths/correlations; mapping and focal technology need adjudication. |

## Paper Readiness Judgment

Paper A can be drafted at the level of introduction, methods, PRISMA flow,
coding workflow, and planned MASEM strategy. Final MASEM results should not be
written until the adjudicated reference data are frozen.

Paper B is now draftable as a methodology paper centered on task-contingent
field-level coding taxonomy across Phase 1 and Phase 2, not Phase 2 alone. The
strongest current contribution is the full-corpus structure of human-human
disagreement and source-adjudicated error taxonomy. LLM validity and downstream
substitution results remain pending.

Paper C is draftable as a protocol/scaffold and can be integrated with Paper B
only if its empirical claim is separated: Paper B evaluates the extraction task
and downstream MASEM validity; Paper C evaluates model/procedure behavior,
including model differences and procedure-driven auditability.

## Remaining Design Risks

- S195 and S206 have identical source PDFs and DOI values. This duplicate-source
  issue should be resolved before the final reference freeze.
- S014 requires a rule for whether indirect PLS-SEM effects through perceived
  risk can be treated as MASEM-ready construct-pair statistics.
- S021 requires a rule for pre/post model handling.
- S202 requires a final focal-technology and construct-mapping decision.
- Paper C needs a locked model set, prompt/schema versions, and a non-inferiority
  margin before final analysis.
