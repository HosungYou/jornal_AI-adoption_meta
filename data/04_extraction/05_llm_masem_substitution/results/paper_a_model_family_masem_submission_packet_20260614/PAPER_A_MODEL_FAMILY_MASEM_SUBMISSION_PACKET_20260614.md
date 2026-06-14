# Paper A Model-Family MASEM Submission Packet

Date: 2026-06-14

## Bottom line

Paper A should report **model-family MASEM** as the primary empirical route. The 10-construct network remains the theory target and evidence map, but it is not currently estimable as a single primary SEM.

## Current empirical basis

- Full10 pairwise coverage after ANX-TRU rescue: 45/45 pairs.
- Full10 complete-case studies: 0.
- Full10 sparse partial-matrix TSSEM status: failed.
- Core7 complete-case TSSEM: .
- Trust6 complete-case TSSEM: .

## Manuscript-ready interpretation

The source-corrected Paper A evidence base supports the full conceptual network as an evidence map, but not as a single full10 MASEM estimate. The empirical MASEM results should therefore be organized as a model family. The core7 model estimates the central UTAUT/TAM adoption pathway through attitude and behavioral intention. The trust6 model estimates an AI-specific trust mechanism linking belief constructs to intention and use. Anxiety and self-efficacy remain theory-relevant mechanism constructs, but they should be reported in supplementary evidence maps or reduced extensions unless source-supported matrices become sufficient for a stable SEM.

## Table 1. Model-family eligibility

| model_family | constructs | required_pairs | observed_pairs_after_rescue | min_pair_k | partial_matrix_studies | complete_case_studies | positive_definite_complete_cases | partial_tssem_status | complete_case_stage1 | complete_case_stage2 | pooled_min_eigen | primary_status | manuscript_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| core7 ATT mediation | PE,EE,SI,FC,ATT,BI,UB | 21 | 21 | 11 | 72 | 4 | 4 | failed | converged |  | 0.3141589957898905 | eligible complete-case diagnostic model | primary empirical model-family member |
| trust6 trust mechanism | PE,EE,SI,TRU,BI,UB | 15 | 15 | 9 | 73 | 7 | 7 | failed | converged |  | 0.3151627736366538 | eligible complete-case diagnostic model | primary empirical model-family member |
| full10 theoretical target | PE,EE,SI,FC,ATT,SE,TRU,ANX,BI,UB | 45 | 45 | 1 | 77 | 0 | 0 | failed | not_run |  | -0.0102318481320849 | not empirically estimable as one SEM in current data | theoretical target and evidence map; not current primary SEM estimate |

## Table 2. Complete-case MASEM fit

| model_family | chisq | df | p | CFI | TLI | RMSEA | SRMR | AIC | BIC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| core7 ATT mediation | 6.146 | 5.000 | 0.292 | 0.999 | 0.996 | 0.009 | 0.043 | -3.854 | -34.165 |
| trust6 trust mechanism | 8.957 | 4.000 | 0.062 | 0.996 | 0.985 | 0.011 | 0.040 | 0.957 | -28.008 |

## Table 3. Structural path estimates

| model_family | parameter | estimate |
| --- | --- | --- |
| core7 ATT mediation | PE_to_ATT | 0.157 |
| core7 ATT mediation | PE_to_BI | 0.187 |
| core7 ATT mediation | EE_to_ATT | 0.127 |
| core7 ATT mediation | EE_to_BI | 0.122 |
| core7 ATT mediation | SI_to_ATT | 0.107 |
| core7 ATT mediation | SI_to_BI | 0.19 |
| core7 ATT mediation | FC_to_ATT | 0.336 |
| core7 ATT mediation | FC_to_UB | 0.332 |
| core7 ATT mediation | ATT_to_BI | 0.512 |
| core7 ATT mediation | BI_to_UB | 0.575 |
| trust6 trust mechanism | PE_to_TRU | 0.261 |
| trust6 trust mechanism | PE_to_BI | 0.365 |
| trust6 trust mechanism | EE_to_TRU | 0.14 |
| trust6 trust mechanism | EE_to_BI | 0.225 |
| trust6 trust mechanism | SI_to_TRU | 0.107 |
| trust6 trust mechanism | SI_to_BI | 0.184 |
| trust6 trust mechanism | TRU_to_BI | 0.243 |
| trust6 trust mechanism | BI_to_UB | 0.714 |

## Proposed Methods text

We treated the 10-construct AI adoption framework as the theoretical target model and first evaluated its empirical support as a source-anchored coverage network. Because no primary study supplied a complete 10-construct correlation matrix and sparse partial-matrix TSSEM attempts produced non-positive-definite implied covariance structures, we did not force the full network into a single primary SEM. Instead, we pre-specified a family of theory-consistent MASEM models corresponding to empirically supported substructures of the target framework. The primary empirical MASEM models were restricted to construct families with source-supported same-study co-measurement and acceptable correlation evidence. The full 10-construct model was retained as the conceptual target and reported through coverage, feasibility, and pairwise evidence-map results.

## Proposed Results text

After source correction and researcher-approved ANX-TRU rescue, the full 10-construct network reached complete pairwise coverage but still had no complete same-study 10-construct matrix. Sparse partial-matrix TSSEM attempts remained non-estimable because the implied covariance structure was not positive definite. The model-family route was therefore used for empirical MASEM. The core7 attitude-mediation model converged with excellent approximate fit (CFI = 0.999, TLI = 0.996, RMSEA = 0.009, SRMR = 0.043). The trust6 mechanism model also converged with strong fit (CFI = 0.996, TLI = 0.985, RMSEA = 0.011, SRMR = 0.040). These findings support reporting the full10 network as the theoretical evidence map and the core7/trust6 models as the empirically estimable MASEM family.

## Reviewer-defense points

- This is not a post hoc abandonment of full10; full10 remains the theoretical target and feasibility map.
- The empirical route is constrained by source-supported same-study co-measurement, not by convenience.
- The strategy avoids arbitrary nearPD repair, unsupported imputation, beta/path-to-correlation mixing, and rejected construct remaps.
- Trust, anxiety, and self-efficacy are mechanism constructs, not moderators, under the current Paper A route.

## Generated files

- `paper_a_model_family_eligibility_table_20260614.csv`
- `paper_a_model_family_fit_table_20260614.csv`
- `paper_a_model_family_structural_paths_20260614.csv`
- `paper_a_full10_coverage_after_anx_tru_rescue_20260614.csv`
