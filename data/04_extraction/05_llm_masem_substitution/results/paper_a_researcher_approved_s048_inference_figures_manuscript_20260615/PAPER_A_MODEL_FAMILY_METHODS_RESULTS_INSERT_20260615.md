# Paper A Methods and Results insert: model-family MASEM

Date: 2026-06-15

## Methods insert

We treated the 10-construct AI adoption framework as the theoretical target and first evaluated whether the source-supported evidence base could sustain a single full-network MASEM. The target framework included performance expectancy, effort expectancy, social influence, facilitating conditions, attitude, self-efficacy, trust, AI anxiety, behavioral intention, and use behavior. Because no study supplied a complete 10-construct correlation matrix and sparse partial-matrix TSSEM produced non-positive-definite implied covariance structures, we did not force the full network into a single structural estimate. Instead, we used a model-family MASEM strategy in which the full 10-construct network was retained as the theoretical evidence map and empirically estimable submodels were fit as complete-case TSSEM/MASEM models.

The empirical model family included a seven-construct attitude-mediation model and a six-construct trust-mechanism model. Complete-case matrices were retained only when all required construct pairs were present and the study-level correlation matrix was positive definite. Stage 1 used random-effects TSSEM. Stage 2 fit the prespecified structural model to the pooled correlation matrix. Path-level support was evaluated using likelihood-based 95% confidence intervals from the Stage 2 model; paths were interpreted as supported when the interval excluded zero. Because finite standard errors and z-based p values were not returned for individual paths, paths with incomplete intervals were flagged as indeterminate rather than treated as significant.

## Results insert

The full 10-construct target reached complete pairwise coverage across the source-supported evidence base (45/45 construct pairs), but no study provided a complete same-study 10-construct matrix. Sparse partial-matrix TSSEM remained non-estimable because the implied covariance structure was not positive definite. The full10 model was therefore retained as a theoretical evidence map rather than reported as a single SEM result.

The core7 attitude-mediation model was estimable with four positive-definite complete-case matrices. The model fit the pooled matrix well, chi-square(5) = 6.15, p = .292, CFI = 0.999, TLI = 0.996, RMSEA = 0.009, and SRMR = 0.043. Supported paths included FC -> ATT, SI -> BI, ATT -> BI, FC -> UB, and BI -> UB. PE -> ATT and SI -> ATT had intervals that included zero, while EE -> ATT, PE -> BI, and EE -> BI had incomplete likelihood-based intervals and were not classified as supported.

The trust6 mechanism model was estimable with seven positive-definite complete-case matrices. Model fit was also strong, chi-square(4) = 8.96, p = .062, CFI = 0.996, TLI = 0.985, RMSEA = 0.011, and SRMR = 0.040. Supported paths included EE -> BI, TRU -> BI, and BI -> UB. EE -> TRU, SI -> TRU, and SI -> BI had intervals that included zero, while PE -> TRU and PE -> BI had incomplete likelihood-based intervals and were not classified as supported. These results support trust as an AI-specific mechanism linking adoption beliefs to behavioral intention, while anxiety and self-efficacy remain theory-relevant constructs for the full10 evidence map or future reduced extensions rather than confirmed mediators in the current empirical MASEM family.

## Table: path-level inference

| model_family | parameter | estimate | ci_text | inference_symbol | inference_class |
| --- | --- | --- | --- | --- | --- |
| Core7 ATT mediation | PE_to_ATT | 0.157 | [-0.170, 0.654] | ns | not_supported_95ci_includes_zero |
| Core7 ATT mediation | EE_to_ATT | 0.127 | [NA, NA] | CI? | ci_incomplete |
| Core7 ATT mediation | SI_to_ATT | 0.107 | [-0.012, 0.215] | ns | not_supported_95ci_includes_zero |
| Core7 ATT mediation | FC_to_ATT | 0.336 | [0.099, 0.400] | CI+ | supported_positive_95ci |
| Core7 ATT mediation | PE_to_BI | 0.187 | [NA, 0.582] | CI? | ci_incomplete |
| Core7 ATT mediation | EE_to_BI | 0.122 | [NA, 0.347] | CI? | ci_incomplete |
| Core7 ATT mediation | SI_to_BI | 0.190 | [0.190, 0.530] | CI+ | supported_positive_95ci |
| Core7 ATT mediation | ATT_to_BI | 0.512 | [0.300, 0.738] | CI+ | supported_positive_95ci |
| Core7 ATT mediation | FC_to_UB | 0.332 | [0.114, 0.544] | CI+ | supported_positive_95ci |
| Core7 ATT mediation | BI_to_UB | 0.575 | [0.397, 0.753] | CI+ | supported_positive_95ci |
| Trust6 trust mechanism | PE_to_TRU | 0.261 | [NA, 0.438] | CI? | ci_incomplete |
| Trust6 trust mechanism | EE_to_TRU | 0.140 | [-0.024, 0.285] | ns | not_supported_95ci_includes_zero |
| Trust6 trust mechanism | SI_to_TRU | 0.107 | [-0.049, 0.257] | ns | not_supported_95ci_includes_zero |
| Trust6 trust mechanism | PE_to_BI | 0.365 | [NA, 0.512] | CI? | ci_incomplete |
| Trust6 trust mechanism | EE_to_BI | 0.225 | [0.045, 0.375] | CI+ | supported_positive_95ci |
| Trust6 trust mechanism | SI_to_BI | 0.184 | [-0.017, 0.372] | ns | not_supported_95ci_includes_zero |
| Trust6 trust mechanism | TRU_to_BI | 0.243 | [0.126, 0.352] | CI+ | supported_positive_95ci |
| Trust6 trust mechanism | BI_to_UB | 0.714 | [0.650, 0.781] | CI+ | supported_positive_95ci |

## Table: model fit

| model_family | route | complete_case_k | effective_sample_size | chisq | df | p | CFI | TLI | RMSEA | RMSEA_low | RMSEA_high | SRMR | AIC | BIC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Core7 ATT mediation | paper_a_core7_att_mediation | 4 | 3172.000 | 6.146 | 5.000 | .292 | 0.999 | 0.996 | 0.009 | 0.000 | 0.027 | 0.043 | -3.854 | -34.165 |
| Trust6 trust mechanism | paper_a_trust6_mechanism | 7 | 10315.000 | 8.957 | 4.000 | .062 | 0.996 | 0.985 | 0.011 | 0.000 | 0.021 | 0.040 | 0.957 | -28.008 |
