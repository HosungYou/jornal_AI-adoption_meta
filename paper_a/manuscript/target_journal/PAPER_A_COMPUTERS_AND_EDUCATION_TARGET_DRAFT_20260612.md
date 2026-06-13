# AI Adoption in Higher Education: A Meta-Analytic Structural Equation Modeling Study

Target journal: Computers & Education

Draft date: 2026-06-12

## Submission Package State

This target-journal draft updates the existing APA-style shell for Computers & Education. It includes the introduction, methods, input/QC results, table/figure spine, and team insertion points. It deliberately does not invent Stage 1/Stage 2 estimates. A diagnostic Paper A TSSEM/MASEM run was attempted on 2026-06-14 using the N-ready 804-row input; all tested structural routes failed at `metaSEM::tssem1` under sparse partial-matrix input, so final Stage 1/Stage 2 path claims remain unavailable.

Researcher-approved route recorded on 2026-06-12:

- Primary model: full 10-construct TSSEM/OSMASEM route.
- N policy: source-supported PDF/workbook N override is allowed with provenance.
- Evidence class: direct correlations are primary; expanded direct-r-form and converted beta/path/source-statistic evidence are sensitivity.
- Mediator/moderator boundary: trust, anxiety, and self-efficacy are focal mediator/mechanism candidates inside the path model, not study-level moderators.

## Highlights

- Synthesizes AI adoption evidence in higher education with MASEM.
- Integrates TAM/UTAUT predictors with trust and AI anxiety.
- Separates direct-r inputs from converted sensitivity evidence.
- Tests structural and moderator paths across ten constructs.
- Provides reproducible extraction and QC artifacts.

## Abstract

Artificial intelligence tools are increasingly embedded in higher education, but the empirical adoption literature remains fragmented across constructs, samples, tools, and reporting formats. This study synthesizes higher-education AI adoption evidence using meta-analytic structural equation modeling. The planned model integrates performance expectancy, effort expectancy, social influence, facilitating conditions, attitude, self-efficacy, trust in AI, AI anxiety, behavioral intention, and use behavior. The current analysis-ready package preserves source-reported direct correlations separately from expanded direct-r-form and converted sensitivity evidence. At the 2026-06-05 checkpoint, the model-ready primary input contains 804 rows after tiered source decisions. The current target-journal package documents the final structure, tables, figures, and analysis gate for a Computers & Education submission. A 2026-06-14 structural execution attempt did not yield converged TSSEM/MASEM path estimates; final path estimates, indirect effects, model fit, and moderator results should be inserted only after an estimable structural route is approved and successfully run.

Keywords: artificial intelligence; technology acceptance; higher education; MASEM; UTAUT; trust; anxiety

## Introduction

Artificial intelligence tools are now embedded in higher education through large language models, intelligent tutoring systems, automated assessment systems, writing assistants, recommendation tools, and analytics platforms. Their spread has produced a rapidly expanding empirical literature on adoption, acceptance, and use. Yet this literature remains difficult to interpret cumulatively because studies draw from overlapping but nonidentical acceptance frameworks, measure different subsets of constructs, and report evidence in formats that do not directly support a single structural synthesis.

Meta-analytic structural equation modeling is well suited to this problem because it can synthesize study-level correlation matrices and test a theory-guided network of relationships. In AI adoption research, this is especially important. Performance expectancy, effort expectancy, social influence, facilitating conditions, attitude, self-efficacy, behavioral intention, and use behavior provide continuity with TAM, TPB, and UTAUT. Trust in AI and AI anxiety capture psychological features of AI systems that are not fully reducible to general usefulness or ease-of-use beliefs.

The present study develops a MASEM of AI adoption in higher education that integrates traditional technology acceptance constructs with AI-specific psychological constructs. The working model treats attitude as a theoretically meaningful mediator rather than assuming that the parsimonious UTAUT exclusion of attitude applies unchanged to AI adoption contexts. It also tests whether trust, anxiety, and self-efficacy operate as AI-specific mechanism constructs where the correlation network supports indirect-effect estimation.

## Literature Review

[Reserved for team contribution. Use the Team Writing Brief in `docs/07_manuscript_exemplars/20260612/TEAM_WRITING_BRIEF_LIT_REVIEW_DISCUSSION_20260612.md`.]

## Method

### Design and Reporting

Paper A is the parent meta-analysis for the AI adoption evidence-synthesis project. It uses systematic-review procedures to identify eligible studies and applies TSSEM/OSMASEM to synthesize construct-level relationships. Reporting should align with PRISMA 2020 and Computers & Education submission requirements.

### Search, Screening, and Eligibility

The documented search workflow yielded 22,166 records. After deduplication, 16,189 records remained for screening. The final manuscript must harmonize the proposal-stage included-study count with the final locked full-text MASEM-eligible count before submission.

### Constructs and Model Architecture

The primary model uses 10 constructs: performance expectancy, effort expectancy, social influence, facilitating conditions, attitude, self-efficacy, trust in AI, AI anxiety, behavioral intention, and use behavior. The planned architecture places performance expectancy and effort expectancy upstream of attitude, attitude upstream of behavioral intention, behavioral intention upstream of use behavior, and trust/anxiety as AI-specific antecedents of behavioral intention.

### Analysis Plan

The primary analysis will use the full 10-construct two-stage MASEM route after numeric sample-size reconciliation. Stage 1 will pool study-level correlation matrices with random-effects TSSEM when feasible. Stage 2 will fit the prespecified structural model to the pooled matrix and estimate indirect effects where the path network supports them. OSMASEM or equivalent meta-regression will test true study-level moderators when moderator data are sufficiently complete. Sensitivity analyses will separate primary direct-r evidence from expanded direct-r-form and converted beta/path/source-statistic evidence.

Source-supported numeric sample sizes will be required for final analytic inclusion. Rows lacking sample-size support may be reconciled from source PDFs or original coder workbooks when provenance is recorded; otherwise, they will be excluded from primary TSSEM estimation or retained only in sensitivity diagnostics.

Trust, anxiety, and self-efficacy are treated as focal mediator/mechanism candidates in the structural model, not as study-level moderators. The first-pass mediator audit indicates that attitude is the strongest standard mediator; trust can be tested as an AI-specific mediator for `PE/EE -> TRU -> BI`, with `SI -> TRU -> BI` as sensitivity; self-efficacy is sensitivity-level only; and anxiety mediation is underpowered or not identified in the current input. Moderator feasibility is separate: `ai_type` is the current substantive moderator candidate, `common_method_bias` is a methodological/QC sensitivity moderator, and year/generative-AI era is not feasible as a current pre/post moderator because the merged available years are all post-2023.

The 2026-06-14 execution attempt tested three structural routes: a seven-construct attitude-mediation route, a six-construct trust-mechanism route, and the full 10-construct theory target. The pairwise random-effects pooled matrices are available for route diagnostics, but `metaSEM::tssem1` failed for all three routes because the implied covariance was not positive definite under sparse partial-matrix input. Therefore, these outputs may support coverage and feasibility reporting, but they must not be written as final structural path estimates.

## Results

### Analysis-Ready Input

| Input or gate | Current value | Submission interpretation |
| --- | --- | --- |
| Primary model-ready rows | 804 | Main candidate input after tiered freeze |
| Usable rows after r checks | 796 | Rows available for matrix construction once N is resolved |
| Rows missing numeric N | 754 | Primary N-weighted SEM blocker |
| Studies represented | 74 | Current study-level matrix universe |
| Construct-pair coverage | 44/45 | Broad but incomplete coverage |

### Primary MASEM Results

The 2026-06-14 diagnostic structural run attempted the approved Paper A direction but did not produce final Stage 2 estimates. The appropriate manuscript treatment is a result-boundary statement plus a table of route feasibility, not path-coefficient interpretation.

| Route | Constructs | Pair coverage | Complete-case studies | TSSEM1 result | Stage 2 result | Current claim boundary |
| --- | --- | ---: | ---: | --- | --- | --- |
| Attitude mediation diagnostic | PE, EE, SI, FC, ATT, BI, UB | 21/21 | 3 | Failed: non-positive definite implied covariance under sparse partial matrices | Not run | Feasible as a theory route only after an estimable Stage 1 solution is available. |
| Trust mechanism diagnostic | PE, EE, SI, TRU, BI, UB | 15/15 | 6 | Failed: non-positive definite implied covariance under sparse partial matrices | Not run | Trust remains a candidate mechanism; no path claim can be made yet. |
| Full 10-construct theory target | PE, EE, SI, FC, ATT, SE, TRU, ANX, BI, UB | 44/45 | 0 | Failed: non-positive definite implied covariance under sparse partial matrices | Not run | Retain as the primary theoretical target, but do not claim final full-model estimates from the current input. |

The pairwise pooled route matrices are available as input-readiness artifacts. They should be cited as diagnostic support only unless a subsequent approved analysis route produces a converged structural model.

### Mediator/Mechanism Feasibility

The 2026-06-12 mediator feasibility audit separates mediator/mechanism testing from moderator analysis. Attitude has the strongest coverage for standard TAM mediation. Trust has sufficient first-pass coverage for `PE -> TRU -> BI` and `EE -> TRU -> BI`, with `SI -> TRU -> BI` treated as sensitivity. Self-efficacy can be evaluated only as sensitivity-level mechanism evidence. Anxiety should remain theory-specified but should not be reported as a confirmed mediator unless later model estimation resolves the current underpowered path coverage.

| Mediator/mechanism | Main candidate paths | Sensitivity paths | Current claim boundary |
| --- | --- | --- | --- |
| Attitude | `PE -> ATT -> BI`; `EE -> ATT -> BI`; `SI -> ATT -> BI`; `FC -> ATT -> BI` | None needed at feasibility stage | Standard TAM mediation family is feasible for Stage 2 indirect-effect testing. |
| Trust | `PE -> TRU -> BI`; `EE -> TRU -> BI` | `SI -> TRU -> BI` | AI-specific trust mechanism can be tested for PE/EE and treated as sensitivity for SI. |
| Self-efficacy | None at main threshold | `FC/EE/PE/SI -> SE -> BI`; selected `SE -> ATT` paths | Sensitivity-level mechanism evidence only. |
| Anxiety | None | None sufficiently supported | Theory-specified construct; do not claim confirmed mediation from current data. |

### Moderator Feasibility

The 2026-06-12 moderator audit supports `ai_type` as the only substantive main moderator candidate from the current input. `common_method_bias` has sufficient coverage but should be treated as methodological/QC sensitivity. The year/generative-era merge linked 66 studies to publication year, but all available years fall in the post-2023 category and eight studies remain missing; therefore a pre/post generative-era moderator is not currently identifiable. User role, education level, country/region, and theoretical framework are too sparse or unbalanced for main moderator claims.

| Moderator | Coverage result | Reporting role |
| --- | --- | --- |
| `ai_type` | 36 studies; generative=21, general=15 | Main substantive moderator candidate. |
| `common_method_bias` | 36 studies; not addressed=22, addressed=14 | Methodological/QC sensitivity. |
| `year/generative-AI era` | 66 studies with year, all post-2023; 8 missing | Not identifiable as pre/post moderator. |
| `user_role` | 36 studies but smallest level has 2 studies | Not feasible for main moderator claim. |
| `education_level`, `country/region`, `theoretical_framework` | Sparse or unbalanced | Not feasible from current input. |

## Discussion

[Reserved for team contribution after lead inserts final results.]


## 2026-06-14 latest-human-workbook correction

The earlier 20260612/initial 20260614 Paper A execution state is superseded in one important respect: it used a reduced analytic input, not the full latest human workbook universe. Rechecking the supplied Drive folder plus Drive-wide/local OneDrive-SSD candidates found later candidate final read-only R1-R4 copies under `Meta/AI Adoption/Coding_Latest_R1_R4_20260605`, including the R4 v2 workbook. Extraction from those latest workbooks produced 3,654 numeric target-construct rows, 181 studies, and 45/45 full10 pair coverage. Therefore, the earlier 44/45 pair-coverage statement should not be treated as the current full human-coding state.

The corrected boundary is narrower: full10 pair coverage exists, but full10 still has 0 complete-case studies, and partial-matrix TSSEM still fails under sparse per-study matrices. The reduced trust6 complete-case diagnostic did converge through Stage 2 with 8 positive-definite complete-case studies, and local PDF/source checks support the trust6 complete-case coded values. This supports reporting trust6 only as a reduced diagnostic/sensitivity result unless additional source-level matrix densification makes the full10 primary route estimable.

Correction evidence: `docs/07_manuscript_exemplars/20260614/PAPER_A_LATEST_HUMAN_WORKBOOK_RECHECK_20260614.md`; `data/04_extraction/05_llm_masem_substitution/results/paper_a_latest_human_workbook_audit_20260614/PAPER_A_LATEST_HUMAN_WORKBOOK_AUDIT_20260614.md`; `data/04_extraction/05_llm_masem_substitution/results/paper_a_masem_latest_human_execution_20260614/PAPER_A_MASEM_EXECUTION_ATTEMPT_20260614.md`; `data/04_extraction/05_llm_masem_substitution/results/paper_a_complete_case_latest_human_20260614/PAPER_A_LATEST_HUMAN_COMPLETE_CASE_TSSEM_PROBE_20260614.md`; `data/04_extraction/05_llm_masem_substitution/results/paper_a_latest_human_workbook_audit_20260614/TRUST6_COMPLETE_CASE_PDF_SOURCE_VALUE_AUDIT_20260614.md`.
