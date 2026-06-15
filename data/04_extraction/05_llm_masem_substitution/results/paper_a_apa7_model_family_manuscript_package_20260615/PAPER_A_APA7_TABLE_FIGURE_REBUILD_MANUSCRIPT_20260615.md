# From Theoretical Coverage to Estimable Model Families: A Meta-Analytic Structural Equation Modeling Study of AI Adoption

## Status note

This rebuild focuses on submission-ready reporting structure: APA-style tables, a PRISMA 2020-style flow diagram, model-family feasibility graphics, and MASEM path/coefficient figures. The manuscript remains pending final target-journal formatting and team verification of full-text eligibility boxes.

## Abstract

AI adoption research in education draws on technology acceptance, unified acceptance, trust, self-efficacy, and anxiety traditions, but individual studies rarely report complete correlation matrices needed to test the whole theoretical system. This study reconstructs AI adoption as a 10-construct theoretical target and evaluates which parts of that target are empirically estimable using model-family meta-analytic structural equation modeling (MASEM). The current PRISMA count lock identifies 224 unique included reports/studies after resolving a 225-row screening include set by merging one duplicate DOI. The full10 target achieved 45/45 pairwise coverage but zero complete 10-construct matrices, so empirical MASEM was conducted through core7 attitude-mediation and trust6 AI-reliance model-family descendants.

## Method

### PRISMA count lock

| Item | Count |
| --- | --- |
| Records identified from databases | 22166 |
| Duplicate records removed | 5977 |
| Records after deduplication/screened | 16189 |
| Records excluded before human review | 15532 |
| Human-reviewed records | 657 |
| Human-reviewed excluded rows | 432 |
| Human-reviewed included rows | 225 |
| Duplicate included DOI rows merged | 1 |
| Unique included reports/studies current lock | 224 |

![Figure 1. PRISMA 2020 flow diagram for Paper A.](paper_a/manuscript/target_journal/apa7_model_family_full_manuscript_scaffold_20260615/figures/figure_1_prisma_2020_flow_diagram_paper_a_20260615.png)

### Theoretical model-family specification

| Construct | Label | Origin | AI-adoption function | Role |
| --- | --- | --- | --- | --- |
| PE | Performance expectancy / perceived usefulness | TAM, TAM2, UTAUT | Instrumental usefulness: AI improves learning, teaching, productivity, or task performance. | full10; core7; trust6 |
| EE | Effort expectancy / perceived ease of use | TAM, computer self-efficacy, UTAUT | Operational ease: AI is manageable, learnable, and low burden. | full10; core7; trust6 |
| SI | Social influence | UTAUT | Normative and institutional endorsement mechanism. | full10; core7; trust6 |
| FC | Facilitating conditions | UTAUT | Resource and infrastructure mechanism enabling adoption and use. | full10; core7 |
| ATT | Attitude | TRA/TPB, TAM | Evaluative mediator translating beliefs into intention. | full10; core7 |
| TRU | Trust | Trust in automation, trust in IS, AI reliance | Reliance mechanism under AI opacity, uncertainty, and vulnerability. | full10; trust6 |
| ANX | Anxiety | Technology readiness, affective threat | Threat/unease mechanism retained in theory but underidentified for primary MASEM. | full10; future mechanism |
| SE | Self-efficacy | Social cognitive theory, computer self-efficacy | Capability mechanism; currently feasible mainly in smaller supplemental sets. | full10; future mechanism |
| BI | Behavioral intention | TRA/TPB, TAM, UTAUT | Proximal motivational adoption outcome. | full10; core7; trust6 |
| UB | Use behavior | TAM, UTAUT | Behavioral adoption/use outcome. | full10; core7; trust6 |

![Figure 2. Theoretical genealogy of Paper A model families.](paper_a/manuscript/target_journal/apa7_model_family_full_manuscript_scaffold_20260615/figures/figure_2_theoretical_genealogy_full10_model_family_20260615.png)

![Figure 3. Paper A analytic workflow.](paper_a/manuscript/target_journal/apa7_model_family_full_manuscript_scaffold_20260615/figures/figure_3_paper_a_analytic_workflow_20260615.png)

### Matrix-feasibility diagnosis

| Model family | Constructs | Required pairs | Observed pairs | Partial studies | Positive-definite complete cases | Manuscript role |
| --- | --- | --- | --- | --- | --- | --- |
| core7 ATT mediation | PE,EE,SI,FC,ATT,BI,UB | 21 | 21 | 72 | 4 | primary empirical model-family member |
| trust6 trust mechanism | PE,EE,SI,TRU,BI,UB | 15 | 15 | 73 | 7 | primary empirical model-family member |
| full10 theoretical target | PE,EE,SI,FC,ATT,SE,TRU,ANX,BI,UB | 45 | 45 | 77 | 0 | theoretical target and evidence map; not current primary SEM estimate |

![Figure 8. Model-family feasibility diagnosis.](paper_a/manuscript/target_journal/apa7_model_family_full_manuscript_scaffold_20260615/figures/figure_8_model_feasibility_plot_20260615.png)

## Results

### Full10 evidence map

![Figure 4. Full10 evidence map.](paper_a/manuscript/target_journal/apa7_model_family_full_manuscript_scaffold_20260615/figures/figure_4_full10_evidence_map_publication_20260615.png)

### Primary model-family fit

| Model | k | N_eff | chi-square | df | p | CFI | TLI | RMSEA | SRMR |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Core7 ATT mediation | 4 | 3172 | 6.146 | 5 | .292 | 0.999 | 0.996 | 0.009 | 0.043 |
| Trust6 trust mechanism | 7 | 10315 | 8.957 | 4 | .062 | 0.996 | 0.985 | 0.011 | 0.040 |

### Primary path estimates

| Model | From | To | Estimate | 95% CI | Inference |
| --- | --- | --- | --- | --- | --- |
| Core7 ATT mediation | PE | ATT | 0.157 | [-0.170, 0.654] | not supported 95ci includes zero |
| Core7 ATT mediation | EE | ATT | 0.127 | [NA, NA] | ci incomplete |
| Core7 ATT mediation | SI | ATT | 0.107 | [-0.012, 0.215] | not supported 95ci includes zero |
| Core7 ATT mediation | FC | ATT | 0.336 | [0.099, 0.400] | supported positive 95ci |
| Core7 ATT mediation | PE | BI | 0.187 | [NA, 0.582] | ci incomplete |
| Core7 ATT mediation | EE | BI | 0.122 | [NA, 0.347] | ci incomplete |
| Core7 ATT mediation | SI | BI | 0.190 | [0.190, 0.530] | supported positive 95ci |
| Core7 ATT mediation | ATT | BI | 0.512 | [0.300, 0.738] | supported positive 95ci |
| Core7 ATT mediation | FC | UB | 0.332 | [0.114, 0.544] | supported positive 95ci |
| Core7 ATT mediation | BI | UB | 0.575 | [0.397, 0.753] | supported positive 95ci |
| Trust6 trust mechanism | PE | TRU | 0.261 | [NA, 0.438] | ci incomplete |
| Trust6 trust mechanism | EE | TRU | 0.140 | [-0.024, 0.285] | not supported 95ci includes zero |
| Trust6 trust mechanism | SI | TRU | 0.107 | [-0.049, 0.257] | not supported 95ci includes zero |
| Trust6 trust mechanism | PE | BI | 0.365 | [NA, 0.512] | ci incomplete |
| Trust6 trust mechanism | EE | BI | 0.225 | [0.045, 0.375] | supported positive 95ci |
| Trust6 trust mechanism | SI | BI | 0.184 | [-0.017, 0.372] | not supported 95ci includes zero |
| Trust6 trust mechanism | TRU | BI | 0.243 | [0.126, 0.352] | supported positive 95ci |
| Trust6 trust mechanism | BI | UB | 0.714 | [0.650, 0.781] | supported positive 95ci |

![Figure 5. Core7 MASEM path model.](paper_a/manuscript/target_journal/apa7_model_family_full_manuscript_scaffold_20260615/figures/figure_5_core7_publication_masem_path_20260615.png)

![Figure 6. Trust6 MASEM path model.](paper_a/manuscript/target_journal/apa7_model_family_full_manuscript_scaffold_20260615/figures/figure_6_trust6_publication_masem_path_20260615.png)

![Figure 7. Path estimate coefficient plot.](paper_a/manuscript/target_journal/apa7_model_family_full_manuscript_scaffold_20260615/figures/figure_7_path_estimate_coefficient_plot_20260615.png)

### Supplemental diagnostics

| Model | k | Status | chi-square | df | p | CFI | RMSEA | AIC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| core7_full | 4 | converged | 6.146 | 5 | .292 | 0.999 | 0.009 | -3.854 |
| core6_no_ATT_direct_beliefs | 17 | converged | 1.780 | 3 | .619 | 1.000 | 0.000 | -4.220 |
| core7_pure_ATT_mediation_no_direct_belief_BI | 4 | status_6 | 18.318 | 8 | .019 | 0.991 | 0.020 | 2.318 |
| trust6_full | 7 | converged | 8.957 | 4 | .062 | 0.996 | 0.011 | 0.957 |
| trust5_no_TRU_direct_acceptance | 20 | converged | 6.496 | 3 | .090 | 0.997 | 0.008 | 0.496 |
| trust6_trust_mediator_no_direct_belief_BI | 7 | converged | 150.683 | 7 | < .001 | 0.888 | 0.045 | 136.683 |
| se4_capability_effort_intention | 2 | status_6 | 2.916 | 2 | .233 | 0.999 | 0.022 | -1.084 |

### PE versus EE role comparison

| Model | Predictor | Target | Estimate | 95% CI | Inference |
| --- | --- | --- | --- | --- | --- |
| Core7 ATT mediation | PE | ATT | 0.157 | [-0.170, 0.654] | not supported 95ci includes zero |
| Core7 ATT mediation | EE | ATT | 0.127 | [NA, NA] | ci incomplete |
| Core7 ATT mediation | PE | BI | 0.187 | [NA, 0.582] | ci incomplete |
| Core7 ATT mediation | EE | BI | 0.122 | [NA, 0.347] | ci incomplete |
| Trust6 trust mechanism | PE | TRU | 0.261 | [NA, 0.438] | ci incomplete |
| Trust6 trust mechanism | EE | TRU | 0.140 | [-0.024, 0.285] | not supported 95ci includes zero |
| Trust6 trust mechanism | PE | BI | 0.365 | [NA, 0.512] | ci incomplete |
| Trust6 trust mechanism | EE | BI | 0.225 | [0.045, 0.375] | supported positive 95ci |

### Anxiety and self-efficacy feasibility

| Model | Constructs | k | Status | CFI | RMSEA |
| --- | --- | --- | --- | --- | --- |
| se4_capability_effort_intention | SE,EE,BI,UB | 2 | status_6 | 0.999 | 0.022 |
| se4_capability_attitude_intention | SE,ATT,BI,UB | 0 | not_run | NA | NA |
| anx4_threat_attitude_intention | ANX,ATT,BI,UB | 0 | not_run | NA | NA |
| anx4_trust_threat_reliance | ANX,TRU,BI,UB | 0 | not_run | NA | NA |
| se_anx_bi_capability_threat | SE,ANX,BI,UB | 0 | not_run | NA | NA |
| se_anx_tru_bi | SE,ANX,TRU,BI | 0 | not_run | NA | NA |

## Reporting boundary

External references are used as methodological and reporting exemplars only. The tables and figures above are recreated from Paper A data and should replace the scaffold-level table/figure presentation in the previous Word draft.
