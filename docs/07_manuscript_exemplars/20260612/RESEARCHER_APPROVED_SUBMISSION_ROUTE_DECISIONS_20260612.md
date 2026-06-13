# Researcher-Approved Submission Route Decisions

Date recorded: 2026-06-12

Scope: Paper A and Paper B target-journal completion route

Status: Authoritative decision record for the current submission-completion sprint

## Decisions now fixed

| Item | Decision | Execution consequence |
| --- | --- | --- |
| Paper A primary model | Use the full 10-construct route as the primary route. | The manuscript, tables, figures, and analysis scripts should target the full 10-construct TSSEM/OSMASEM route first, not a reduced diagnostic route. |
| Paper A sample-size policy | Permit source-supported PDF/workbook N override. | Numeric N must be reconciled from source PDFs and extraction workbooks before final SEM claims. Rows without defensible N remain excluded or sensitivity-only. |
| Paper A evidence class | Use direct correlations as the primary evidence class; include expanded/converted effects as sensitivity. | Direct-r evidence is the main estimand. Beta/path/source-statistic conversions may support sensitivity analyses but must not be collapsed into the primary estimate. |
| Paper A moderators | Trust, anxiety, and self-efficacy are focal constructs/antecedents in the 10-construct model, not study-level moderators. | Moderator analysis should audit true study-level moderators: publication year or generative-AI era, cultural context/region or Hofstede IDV, education level/user role, and AI tool type such as LLM versus non-LLM. |
| Paper B RQ4 route | Attempt the broader TSSEM/MASEM rebuild. | Core-6 SEM remains the current bounded diagnostic result until the broader rebuild spec, source-type sufficiency audit, and successful run are complete. |
| Paper B RQ3 route | Treat cross-model disagreement as a main RQ3 triage signal. | Cross-model disagreement is part of the primary triage question, together with human-human disagreement, LLM uncertainty, and source-risk flags. It is not a vendor-ranking claim. |
| Submission order | Develop and submit Paper A and Paper B together. | Shared artifact tracking, status logs, and rendered outputs should be maintained together, while claims remain paper-specific. |
| Artifact policy | Include all share-safe rendered artifacts, including PDFs and PNGs. | Submission packets may include rendered PDFs/PNGs/tables/figures/scripts/manuscript drafts. Raw PDFs, private source packets, raw coder workbooks, and raw LLM outputs remain excluded from Git unless explicitly cleared. |

## Clarification on Paper A moderators

Trust, anxiety, and self-efficacy are already part of the structural model as constructs. The researcher clarification on 2026-06-12 is that these variables should be evaluated as **candidate mediator/mechanism constructs**, not as study-level moderators. They can moderate only if the study defines a separate study-level moderator variable such as construct presence, measurement framing, or construct role. That would be a different, weaker, and more defensibility-sensitive analysis than the current Paper A model.

The defensible primary route is:

1. Keep trust, anxiety, and self-efficacy inside the 10-construct SEM as theory-specified mediator/mechanism candidates where path coverage permits.
2. Audit indirect-effect feasibility using upstream `a` paths, downstream `b` paths, direct/comparison `c` paths, and same-study path overlap.
3. Audit true study-level moderators separately.
4. Run OSMASEM/meta-regression only for true study-level moderators with adequate coverage.
5. Report underpowered mediator paths or sparsely coded moderators as feasibility limits, not as failed hypotheses.

## Paper A mediator feasibility audit completed on 2026-06-12

Report: `data/04_extraction/05_llm_masem_substitution/results/paper_a_mediator_feasibility_20260612/PAPER_A_MEDIATOR_FEASIBILITY_AUDIT_20260612.md`

| Mediator/mechanism construct | First-pass finding | Reporting implication |
| --- | --- | --- |
| `ATT` | Standard TAM mediation is strongest: `PE -> ATT -> BI`, `EE -> ATT -> BI`, `SI -> ATT -> BI`, and `FC -> ATT -> BI` are all main indirect candidates. | Main Stage 2 indirect-effect family. |
| `TRU` | `PE -> TRU -> BI` and `EE -> TRU -> BI` are main indirect candidates; `SI -> TRU -> BI` is sensitivity-level; `FC/ATT/SE -> TRU -> BI` are underpowered or not identified. | AI-specific trust mechanism can be tested for PE/EE, with SI sensitivity. |
| `SE` | `FC/EE/PE/SI -> SE -> BI` and `EE/PE -> SE -> ATT` are sensitivity-level indirect candidates; no SE path reaches main-candidate threshold. | Self-efficacy should be reported as sensitivity/mechanism evidence, not a primary confirmed mediator. |
| `ANX` | Anxiety paths are underpowered or not identified in current input. | Anxiety remains a theory-specified construct/antecedent; do not claim confirmed mediation from current data. |

## Correction to previous status records

The user had already stated that Paper B cross-model disagreement should be the main RQ3. Some live documents already reflected that direction, but other gate documents still preserved older language treating Claude/Gemini or cross-model disagreement as supplementary-only or as an unresolved question. That was a documentation-state error, not a new substantive ambiguity.

This record resolves the inconsistency: cross-model disagreement is now part of main RQ3, and the broader TSSEM/MASEM rebuild is the selected Paper B route, subject to execution feasibility.

## Remaining execution gates

| Gate | Blocking condition | Required output |
| --- | --- | --- |
| Paper A structural estimability | The 2026-06-14 N-ready execution attempt failed at TSSEM1 for all tested routes because sparse partial matrices produced non-positive definite implied covariance. | Approved next route: source/matrix densification, reduced complete-case diagnostic, or explicitly labeled pooled-correlation sensitivity model. |
| Paper A moderator feasibility | Moderator candidates have been checked for first-pass field completeness and study count. | `ai_type` is the main substantive candidate; `common_method_bias` is QC/sensitivity; year/generative-era and other fields are not currently feasible. |
| Paper A full SEM run | Full 10-construct matrix availability must support estimation. Current full10 coverage is 44/45 pairs, 0 complete-case studies, and failed TSSEM1. | Converged TSSEM/OSMASEM result tables, path diagram, heterogeneity/sensitivity outputs before any final path claims. |
| Paper B broader rebuild spec | Broader TSSEM/MASEM scope must be defined without overstating current core-6 diagnostics. | Broader SEM specification, source-type sufficiency audit, and run log. |
| Paper B RQ3 figures/tables | Cross-model disagreement must be operationalized as a triage signal. | RQ3 table/figure showing cross-model disagreement together with human disagreement, uncertainty, and source-risk flags. |

## Paper A TSSEM/MASEM execution attempt completed on 2026-06-14

Report: `data/04_extraction/05_llm_masem_substitution/results/paper_a_masem_execution_20260614/PAPER_A_MASEM_EXECUTION_ATTEMPT_20260614.md`

| Route | Execution result | Decision implication |
| --- | --- | --- |
| `paper_a_core7_att_mediation` | 21/21 pair coverage, 71 partial studies, 3 complete-case studies; TSSEM1 failed because the implied covariance was not positive definite under sparse partial-matrix input; Stage 2 was not run. | Do not report ATT mediation path estimates yet. |
| `paper_a_trust6_mechanism` | 15/15 pair coverage, 72 partial studies, 6 complete-case studies; TSSEM1 failed for the same structural reason; Stage 2 was not run. | Trust remains a candidate mechanism, not a confirmed mediated effect. |
| `paper_a_full10_theory_target` | 44/45 pair coverage, one missing/unestimated pair, one single-study pair, 74 partial studies, 0 complete-case studies; TSSEM1 failed and Stage 2 was not run. | Full 10-construct model remains the primary theory target, but current data do not support final full-model path estimates. |

This resolves the immediate “have we actually run Paper A?” question: yes, an actual TSSEM/MASEM execution was attempted from the N-ready input, but it did not produce converged structural results. Manuscript text may describe the attempted route and feasibility boundary, but not final path coefficients, indirect effects, or model fit.

## Remaining technical questions

These are not route-decision questions. They are execution questions to answer from the data and analysis outputs.

1. Which true study-level Paper A moderator fields have enough coded coverage for OSMASEM/meta-regression after audit?
2. What operational threshold should define a useful Paper B cross-model disagreement triage signal once RQ3 tables/figures are generated?
3. Does the Paper B broader TSSEM/MASEM rebuild produce enough stable matrix/source-type coverage to replace or extend the core-6 diagnostic in the main text?

## Initial execution validation completed on 2026-06-12

Report: `data/04_extraction/05_llm_masem_substitution/results/initial_execution_validation_20260612/PAPER_A_B_INITIAL_EXECUTION_VALIDATION_20260612.md`

Summary:

1. Paper A moderator feasibility: `ai_type` and `common_method_bias` meet first-pass main-candidate thresholds. `user_role`, `education_level`, `country`/region, and `theoretical_framework` do not. Trust, anxiety, and self-efficacy remain constructs/antecedents, not moderators.
2. Paper B RQ3: cross-model disagreement remains usable as a main descriptive triage dimension, but not as a standalone high-yield detector. Its precision is high because the baseline review-needed rate is already very high; lift is approximately 1.0.
3. Paper B RQ4: broader rebuild is justified only as staged probing. Core-6 remains the completed diagnostic; `core7_add_att` and `core8_add_tru` may be attempted as sparse probes; `core9_add_anx` and the full 10-construct target are not ready from current coverage.

## Paper B sparse TSSEM/MASEM probe completed on 2026-06-12

Report: `data/04_extraction/05_llm_masem_substitution/results/paper_b_sparse_tssem_probe_20260612/PAPER_B_SPARSE_TSSEM_PROBE_20260612.md`

| Probe | Execution result | Decision implication |
| --- | --- | --- |
| `core7_add_att` | Conservative complete-case Stage 1 completed with 3 studies; Stage 2 failed because `aCov` was not positive definite. | Do not promote to main downstream SEM result. |
| `core8_add_tru` | Conservative complete-case rule found only 1 complete-case study. | Not runnable as current TSSEM path diagnostic. |

The broader rebuild was attempted and remains blocked for main-text extension. Paper B should retain the core-6 diagnostic as the completed downstream SEM evidence.

## Paper A year/generative-era moderator merge completed on 2026-06-12

Report: `data/04_extraction/05_llm_masem_substitution/results/paper_a_year_moderator_merge_20260612/PAPER_A_YEAR_GENERATIVE_ERA_MODERATOR_MERGE_20260612.md`

| Moderator | Execution result | Decision implication |
| --- | --- | --- |
| `ai_type` | 36 studies, generative=21 and general=15. | Main substantive moderator candidate. |
| `common_method_bias` | 36 studies, not addressed=22 and addressed=14. | Methodological/QC sensitivity moderator. |
| `year/generative-AI era` | 66 studies with year all post-2023; 8 missing. | Not feasible as a pre/post moderator from current data. |

Current open method choice:

1. For Paper A final path estimates, choose the next estimable route: source/matrix densification toward full10, a reduced complete-case diagnostic, or an explicitly labeled pooled-correlation sensitivity model. Until that choice is made and a structural model converges, Paper A is not submission-ready as a final MASEM results manuscript.


## 2026-06-14 latest-human-workbook correction

The earlier 20260612/initial 20260614 Paper A execution state is superseded in one important respect: it used a reduced analytic input, not the full latest human workbook universe. Rechecking the supplied Drive folder plus Drive-wide/local OneDrive-SSD candidates found later candidate final read-only R1-R4 copies under `Meta/AI Adoption/Coding_Latest_R1_R4_20260605`, including the R4 v2 workbook. Extraction from those latest workbooks produced 3,654 numeric target-construct rows, 181 studies, and 45/45 full10 pair coverage. Therefore, the earlier 44/45 pair-coverage statement should not be treated as the current full human-coding state.

The corrected boundary is narrower: full10 pair coverage exists, but full10 still has 0 complete-case studies, and partial-matrix TSSEM still fails under sparse per-study matrices. The reduced trust6 complete-case diagnostic did converge through Stage 2 with 8 positive-definite complete-case studies, and local PDF/source checks support the trust6 complete-case coded values. This supports reporting trust6 only as a reduced diagnostic/sensitivity result unless additional source-level matrix densification makes the full10 primary route estimable.

Correction evidence: `docs/07_manuscript_exemplars/20260614/PAPER_A_LATEST_HUMAN_WORKBOOK_RECHECK_20260614.md`; `data/04_extraction/05_llm_masem_substitution/results/paper_a_latest_human_workbook_audit_20260614/PAPER_A_LATEST_HUMAN_WORKBOOK_AUDIT_20260614.md`; `data/04_extraction/05_llm_masem_substitution/results/paper_a_masem_latest_human_execution_20260614/PAPER_A_MASEM_EXECUTION_ATTEMPT_20260614.md`; `data/04_extraction/05_llm_masem_substitution/results/paper_a_complete_case_latest_human_20260614/PAPER_A_LATEST_HUMAN_COMPLETE_CASE_TSSEM_PROBE_20260614.md`; `data/04_extraction/05_llm_masem_substitution/results/paper_a_latest_human_workbook_audit_20260614/TRUST6_COMPLETE_CASE_PDF_SOURCE_VALUE_AUDIT_20260614.md`.
