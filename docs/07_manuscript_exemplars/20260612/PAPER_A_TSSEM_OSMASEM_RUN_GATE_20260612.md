# Paper A TSSEM/OSMASEM Run Gate

Date: 2026-06-12

Decision: The lead approved actual TSSEM/OSMASEM/sensitivity estimation for Paper A. The initial 2026-06-12 gate identified numeric sample-size reconciliation as the first blocker. A subsequent 2026-06-14 execution attempt used the N-ready 804-row input and moved the active blocker to structural estimability under sparse partial-matrix input.

## Researcher-Approved Execution Route Recorded on 2026-06-12

| Item | Decision | Gate implication |
| --- | --- | --- |
| Primary model | Full 10-construct route. | Build the analytic matrix toward the complete PE, EE, SI, FC, ATT, SE, TRU, ANX, BI, UB model. |
| Sample-size policy | Source-supported PDF/workbook N override allowed. | Reconcile missing numeric N from source PDFs or original coder workbooks before final SEM claims. |
| Evidence class | Direct-r primary; expanded/converted sensitivity. | Keep the primary estimand clean and report converted evidence only as sensitivity. |
| Mediator/mechanism constructs | Trust/anxiety/self-efficacy are candidate mediator/mechanism constructs, not moderators. | Test indirect paths inside Stage 2 MASEM where path coverage permits. |
| Moderators | Study-level moderators remain separate from mediator constructs. | Audit true study-level moderators before OSMASEM/meta-regression: year/generative-AI era, cultural context/region or Hofstede IDV, education level/user role, and AI tool type. |

## Mediator Gate Recorded on 2026-06-12

| Construct | Gate result |
| --- | --- |
| `ATT` | Main indirect candidate for standard TAM mediation. |
| `TRU` | Main indirect candidate for `PE/EE -> TRU -> BI`; sensitivity for `SI -> TRU -> BI`. |
| `SE` | Sensitivity-level mediator/mechanism only. |
| `ANX` | Underpowered or not identified for confirmed mediation in current input. |

## Moderator Gate Recorded on 2026-06-12

| Moderator | Gate result |
| --- | --- |
| `ai_type` | Main substantive moderator candidate. |
| `common_method_bias` | Eligible as methodological/QC sensitivity. |
| `year/generative-AI era` | Not feasible as current pre/post moderator: 66 merged studies are all post-2023 and 8 are missing year. |
| `user_role`, `education_level`, `country/region`, `theoretical_framework` | Not feasible from current coverage/balance. |

## Readiness Snapshot

| Metric | Value |
| --- | --- |
| Primary rows | 804 |
| Usable rows after 10-construct and r checks | 796 |
| Rows missing numeric N | 754 |
| Studies represented | 74 |
| Construct-pair coverage | 44/45 |
| Complete 10-construct studies | 0 |
| Studies with 15 or more pairs | 26 |

## Execution Update Recorded on 2026-06-14

Report: `data/04_extraction/05_llm_masem_substitution/results/paper_a_masem_execution_20260614/PAPER_A_MASEM_EXECUTION_ATTEMPT_20260614.md`

| Route | Construct target | Pair coverage | Complete-case studies | TSSEM1 result | Stage 2 result | Gate implication |
| --- | --- | ---: | ---: | --- | --- | --- |
| `paper_a_core7_att_mediation` | PE, EE, SI, FC, ATT, BI, UB | 21/21 | 3 | Failed: implied covariance not positive definite under sparse partial-matrix input | Not run | Do not report ATT mediation path estimates yet. |
| `paper_a_trust6_mechanism` | PE, EE, SI, TRU, BI, UB | 15/15 | 6 | Failed: implied covariance not positive definite under sparse partial-matrix input | Not run | Do not report TRU mechanism path estimates yet. |
| `paper_a_full10_theory_target` | PE, EE, SI, FC, ATT, SE, TRU, ANX, BI, UB | 44/45 | 0 | Failed: implied covariance not positive definite under sparse partial-matrix input | Not run | Full 10-construct path claims remain blocked. |

The immediate blocker is no longer only numeric N. The current N-ready input can generate pairwise random-effects pooled correlations for diagnostic coverage, but it does not yet support a converged `metaSEM` structural model. The full 10-construct route has no complete-case studies and is missing one pair (`ANX-TRU`), so it remains a theory target rather than an estimable final model from the current file.

## Stop Condition

Do not report a primary N-weighted TSSEM/OSMASEM estimate from this file until one of the following is true:

1. Source-supported numeric N is filled for the rows entering the SEM input and the structural TSSEM/MASEM route converges; or
2. A Paper A-specific N-eligible and matrix-completeness subset rule is approved, documented, and produces a converged structural model; or
3. A methodological decision is made to run an explicitly labeled non-primary diagnostic, such as a reduced complete-case route or pooled-correlation sensitivity model, with no final substantive path claims.

## Recommended Next Action

Choose and document the next estimable Paper A route before reporting path results: source/matrix densification for the full 10-construct target, a reduced complete-case diagnostic model, or a clearly labeled pooled-correlation sensitivity model. The recommended default is to keep the full 10-construct model as the theoretical target, report the 2026-06-14 run as an execution boundary, and run any reduced model only as a diagnostic/sensitivity analysis.


## 2026-06-14 latest-human-workbook correction

The earlier 20260612/initial 20260614 Paper A execution state is superseded in one important respect: it used a reduced analytic input, not the full latest human workbook universe. Rechecking the supplied Drive folder plus Drive-wide/local OneDrive-SSD candidates found later candidate final read-only R1-R4 copies under `Meta/AI Adoption/Coding_Latest_R1_R4_20260605`, including the R4 v2 workbook. Extraction from those latest workbooks produced 3,654 numeric target-construct rows, 181 studies, and 45/45 full10 pair coverage. Therefore, the earlier 44/45 pair-coverage statement should not be treated as the current full human-coding state.

The corrected boundary is narrower: full10 pair coverage exists, but full10 still has 0 complete-case studies, and partial-matrix TSSEM still fails under sparse per-study matrices. The reduced trust6 complete-case diagnostic did converge through Stage 2 with 8 positive-definite complete-case studies, and local PDF/source checks support the trust6 complete-case coded values. This supports reporting trust6 only as a reduced diagnostic/sensitivity result unless additional source-level matrix densification makes the full10 primary route estimable.

Correction evidence: `docs/07_manuscript_exemplars/20260614/PAPER_A_LATEST_HUMAN_WORKBOOK_RECHECK_20260614.md`; `data/04_extraction/05_llm_masem_substitution/results/paper_a_latest_human_workbook_audit_20260614/PAPER_A_LATEST_HUMAN_WORKBOOK_AUDIT_20260614.md`; `data/04_extraction/05_llm_masem_substitution/results/paper_a_masem_latest_human_execution_20260614/PAPER_A_MASEM_EXECUTION_ATTEMPT_20260614.md`; `data/04_extraction/05_llm_masem_substitution/results/paper_a_complete_case_latest_human_20260614/PAPER_A_LATEST_HUMAN_COMPLETE_CASE_TSSEM_PROBE_20260614.md`; `data/04_extraction/05_llm_masem_substitution/results/paper_a_latest_human_workbook_audit_20260614/TRUST6_COMPLETE_CASE_PDF_SOURCE_VALUE_AUDIT_20260614.md`.
