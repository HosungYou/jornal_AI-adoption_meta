# Paper A model-family MASEM submission run packet

Date: 2026-06-14

## Execution status

The Paper A source-clean submission input was used for the model-family MASEM run. This is the modified direction: full10 is retained as the theoretical target and evidence map, while `core7` and `trust6` are the empirical primary model-family members.

## Eligibility

| model_family | constructs | required_pairs | observed_pairs | complete_case_studies | complete_case_ids | stage1 | stage2 | role | submission_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| core7 ATT mediation | PE,EE,SI,FC,ATT,BI,UB | 21 | 21 | 4 | S048;S055;S176;S214 | converged | converged | primary empirical model-family member | eligible and converged |
| trust6 trust mechanism | PE,EE,SI,TRU,BI,UB | 15 | 15 | 7 | S004;S048;S121;S121-1;S121-2;S173;S176 | converged | converged | primary empirical model-family member | eligible and converged |
| full10 theoretical target | PE,EE,SI,FC,ATT,SE,TRU,ANX,BI,UB | 45 | 45 | 0 | none | not_run | not_run | theoretical target and evidence map | not empirically estimable as one SEM |

## Fit table

| model_family | chisq | df | p | CFI | TLI | RMSEA | SRMR | AIC | BIC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| core7 ATT mediation | 6.146 | 5 | 0.292 | 0.999 | 0.996 | 0.009 | 0.043 | -3.854 | -34.165 |
| trust6 trust mechanism | 8.957 | 4 | 0.062 | 0.996 | 0.985 | 0.011 | 0.040 | 0.957 | -28.008 |

## Structural paths

| model_family | path | estimate |
| --- | --- | --- |
| core7 ATT mediation | PE -> ATT | 0.157 |
| core7 ATT mediation | PE -> BI | 0.187 |
| core7 ATT mediation | EE -> ATT | 0.127 |
| core7 ATT mediation | EE -> BI | 0.122 |
| core7 ATT mediation | SI -> ATT | 0.107 |
| core7 ATT mediation | SI -> BI | 0.190 |
| core7 ATT mediation | FC -> ATT | 0.336 |
| core7 ATT mediation | FC -> UB | 0.332 |
| core7 ATT mediation | ATT -> BI | 0.512 |
| core7 ATT mediation | BI -> UB | 0.575 |
| trust6 trust mechanism | PE -> TRU | 0.261 |
| trust6 trust mechanism | PE -> BI | 0.365 |
| trust6 trust mechanism | EE -> TRU | 0.140 |
| trust6 trust mechanism | EE -> BI | 0.225 |
| trust6 trust mechanism | SI -> TRU | 0.107 |
| trust6 trust mechanism | SI -> BI | 0.184 |
| trust6 trust mechanism | TRU -> BI | 0.243 |
| trust6 trust mechanism | BI -> UB | 0.714 |

## Interpretation

The full10 network has complete pairwise coverage in the source-clean input but zero complete-case studies, so it remains a theoretical target and evidence-map result rather than a single primary SEM. The core7 and trust6 models both converged from positive-definite complete-case matrices and therefore form the current primary empirical model-family MASEM route.
