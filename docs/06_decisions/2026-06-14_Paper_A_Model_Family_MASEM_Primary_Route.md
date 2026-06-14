# Paper A Decision: Primary Empirical Route as Model-Family MASEM

Date: 2026-06-14
Project: AI Adoption Meta-Analysis, Paper A
Decision status: researcher-approved methodological direction for next analysis phase

## Decision

Paper A will use **model-family MASEM** as the primary empirical route.

The full 10-construct framework remains the **theoretical target model** and the organizing evidence map, but it will not be forced into a single full10 structural MASEM result unless the data later satisfy defensible estimation conditions. Empirical SEM results will be reported through a pre-specified family of source-defensible models that map onto the theory and have adequate matrix support.

## Rationale in one paragraph

The current corpus supports the 10-construct theory at the pairwise evidence-map level, but it does not yet support a single full10 SEM as the primary empirical result. After S004/S048 source correction and S036/S102 ANX-TRU rescue, full10 pair coverage reaches 45/45, but full10 still has zero complete-case studies and sparse partial-matrix TSSEM continues to fail with non-positive-definite implied covariance. The defensible response is not arbitrary matrix repair or unsupported construct remapping. The defensible response is to retain full10 as the theory target and estimate a theoretically pre-specified family of lower-dimensional MASEM models where constructs are co-measured and source-supported.

## Current project evidence behind the decision

Evidence from the 2026-06-14 Paper A diagnostic runs:

| Route | Current status | Implication |
| --- | --- | --- |
| full10 theory target | 45/45 pair coverage after ANX-TRU rescue, 0 complete-case studies, partial-matrix TSSEM fails | Use as theoretical target and coverage/evidence map, not as current primary SEM estimate |
| core7 ATT mediation | 21/21 pairs, 4 complete-case studies, complete-case TSSEM converged | Primary empirical mechanism model candidate |
| trust6 mechanism | 15/15 pairs, 7 complete-case studies, complete-case TSSEM converged | Primary empirical mechanism model candidate |
| ANX/SE mechanism extensions | source-supported in selected pairs but not enough for full10 complete-case estimation | Supplementary pairwise/mechanism evidence unless a separately defensible model is estimable |

Local evidence files:

- `data/04_extraction/05_llm_masem_substitution/results/paper_a_source_corrected_s004_s048_20260614/PAPER_A_SOURCE_CORRECTION_AND_MASEM_STATUS_20260614.md`
- `data/04_extraction/05_llm_masem_substitution/results/paper_a_anx_tru_rescue_after_source_correction_20260614/PAPER_A_ANX_TRU_RESCUE_AND_MASEM_STATUS_20260614.md`
- `data/04_extraction/05_llm_masem_substitution/results/paper_a_full10_densification_queue_after_anx_tru_20260614/PAPER_A_FULL10_DENSIFICATION_QUEUE_AFTER_ANX_TRU_20260614.md`

## Model-family definition

### Family 0: full10 theoretical target and evidence map

Constructs: PE, EE, SI, FC, ATT, BI, UB, TRU, ANX, SE.

Purpose:

- Preserve the full theory-driven conceptual network.
- Report pairwise availability, same-study co-measurement, construct coverage, and source feasibility.
- Provide a transparent explanation for why the full10 SEM is not currently estimable as the primary result.
- Identify whether any future source-confirmed densification could make a full10 SEM feasible.

Primary output type:

- Evidence-map figure.
- Pairwise coverage heatmap.
- Construct-pair random-effects summary table where appropriate.
- Same-study co-measurement table and missingness map.
- Non-estimability statement for full10 SEM.

### Family 1: core7 ATT mediation model

Constructs: PE, EE, SI, FC, ATT, BI, UB.

Theory role:

- Represents the core adoption path from performance, effort, social, and facilitating-condition beliefs through attitude and behavioral intention to use behavior.
- Keeps the classic TAM attitude/intention logic while preserving UTAUT-style exogenous predictors.

Empirical role:

- Primary source-defensible empirical MASEM candidate.
- Already has full required pair coverage and complete-case converged TSSEM evidence in the current diagnostic run.

Candidate structural paths:

- PE -> ATT
- EE -> ATT
- SI -> ATT
- FC -> UB
- PE -> BI
- EE -> BI
- SI -> BI
- ATT -> BI
- BI -> UB

### Family 2: trust6 mechanism model

Constructs: PE, EE, SI, TRU, BI, UB.

Theory role:

- Represents trust as a mechanism linking AI/technology belief formation to adoption intention and use behavior.
- Especially relevant for AI adoption because trust, reliability, and appropriate reliance are central adoption constraints.

Empirical role:

- Primary source-defensible empirical MASEM candidate.
- Already has full required pair coverage and complete-case converged TSSEM evidence in the current diagnostic run.

Candidate structural paths:

- PE -> TRU
- EE -> TRU
- SI -> TRU
- PE -> BI
- EE -> BI
- SI -> BI
- TRU -> BI
- BI -> UB

### Family 3: anxiety and self-efficacy mechanism extensions

Constructs: ANX and SE added only when the source matrix supports a defensible estimable model.

Theory role:

- ANX and SE are not moderators in the current Paper A logic.
- They are mediator/theoretical mechanism constructs: self-efficacy can shape perceived ease/effort and intention, while anxiety can inhibit ease, trust, attitude, or intention depending on the source model.

Empirical role:

- Supplementary mechanism models or pairwise/meta-regression evidence unless coverage supports a pre-specified SEM.
- Do not promote beta/path coefficients, HTMT, loadings, or theory-only claims into zero-order/latent correlation inputs.

Candidate extension paths to evaluate only if data permit:

- SE -> EE
- SE -> ATT or BI
- ANX -> EE
- ANX -> TRU
- ANX -> ATT or BI
- TRU -> BI
- BI -> UB

## Academic-method justification

### Why model-family MASEM is methodologically defensible

MASEM is designed to synthesize correlation matrices and test structural models, including direct and indirect effects, over a body of studies. However, MASEM depends on defensible correlation input, matrix compatibility, and interpretable missing-data assumptions. A single forced full10 matrix is not required when the literature measures theoretically adjacent but not identical construct sets. A pre-specified model family is defensible when each member is theory-linked, source-supported, and reported with transparent coverage boundaries.

### Why not force the full10 SEM now

Current project evidence shows three constraints:

1. No source-supported study currently provides a complete 10-construct matrix.
2. Sparse partial-matrix TSSEM fails even after ANX-TRU rescue.
3. The densest studies are structurally blocked because they do not measure target ANX and SE, so completing full10 would require unsupported construct remapping rather than simple source extraction.

Forcing full10 would invite reviewer objections:

- Non-positive-definite pooled or implied covariance structures can arise from sparse and incompatible pairwise evidence.
- Arbitrary nearPD repair changes the estimand and can obscure the empirical missingness problem.
- Beta/path coefficients and correlations are not interchangeable without a separately justified sensitivity design.
- Construct remapping after seeing feasibility problems looks post hoc unless explicitly approved and source-defensible.

### Why reduced routes are not a retreat from theory

The reduced routes are not selected because they give convenient results. They are selected because they represent theoretically meaningful submodels of the full10 framework and satisfy better empirical support:

- `core7` captures the core UTAUT/TAM adoption process.
- `trust6` captures AI-appropriate reliance and trust-based adoption.
- ANX and SE remain in the theory framework but are not forced into SEMs when source matrices do not support them.
- full10 remains visible as the theory target, coverage map, and future densification frontier.

## Reference-backed claims to use in the manuscript

### Methodological claims

1. MASEM is appropriate for theory testing over pooled correlation structures, including indirect effects and competing path models.
2. Two-stage and one-stage MASEM are standard choices, but they require defensible handling of missing correlations and study-level dependence.
3. Pairwise pooled matrices can become non-positive definite when correlations are synthesized from different subsets of studies or when missingness is structurally uneven.
4. Missing coefficients are not automatically fatal in MASEM, but they require transparent assumptions and sensitivity checks.
5. When the full theoretical network is not empirically estimable, pre-specified source-defensible submodels are preferable to arbitrary matrix repair.

### Theory claims

1. TAM and UTAUT justify PE/PU, EE/PEOU, SI, FC, ATT, BI, and UB as the core adoption pathway.
2. Trust is central to AI/automation adoption because users must decide whether and how to rely on the system.
3. Self-efficacy is a social-cognitive mechanism that shapes perceived capability and technology use.
4. Anxiety is a technology-readiness and acceptance barrier that can impair ease, trust, attitude, and intention.
5. In this Paper A design, trust, anxiety, and self-efficacy are mechanism/mediator constructs, not moderators, unless the researcher explicitly changes the model.

## Proposed manuscript language

### Methods: analysis strategy

We treated the 10-construct AI adoption framework as the theoretical target model and first evaluated its empirical support as a source-anchored coverage network. Because no primary study supplied a complete 10-construct correlation matrix and sparse partial-matrix TSSEM attempts produced non-positive-definite implied covariance structures, we did not force the full network into a single primary SEM. Instead, we pre-specified a family of theory-consistent MASEM models corresponding to empirically supported substructures of the target framework. The primary empirical MASEM models were restricted to construct families with source-supported same-study co-measurement and acceptable correlation evidence. The full 10-construct model was retained as the conceptual target and reported through coverage, feasibility, and pairwise evidence-map results.

### Results: full10 feasibility

The source-corrected and researcher-approved diagnostic input achieved complete pairwise coverage of the 10-construct network after ANX-TRU rescue, but it did not produce a complete same-study 10-construct matrix. The highest-density studies measured core adoption and trust constructs but did not measure the target anxiety and self-efficacy constructs. Therefore, the full10 network was considered theoretically specified but empirically non-estimable as a single primary MASEM in the current corpus.

### Results: empirical model family

The empirically estimable MASEM results were therefore organized as a model family. The core7 model tested the UTAUT/TAM adoption pathway through attitude and behavioral intention, while the trust6 model tested trust as an AI adoption mechanism linking belief constructs to intention and use. Anxiety and self-efficacy were retained as theoretical mechanism constructs and evaluated in supplementary evidence maps or reduced mechanism models only where source-supported matrices were sufficient.

## Reporting plan

### Main text tables and figures

1. Table A1: Paper A construct definitions and approved remaps.
2. Table A2: full10 pairwise coverage and same-study co-measurement summary.
3. Table A3: empirical model-family eligibility table: full10, core7, trust6, ANX/SE extensions.
4. Table A4: MASEM fit and path estimates for core7 and trust6.
5. Figure A1: full10 theoretical model with estimable and non-estimable regions.
6. Figure A2: construct-pair coverage heatmap.
7. Figure A3: model-family SEM diagrams with standardized estimates.

### Supplementary materials

1. Full reference bank and theory mapping table.
2. ANX-TRU rescue source-trace packet.
3. Densification queue and source-blocked full10 matrix explanation.
4. Sensitivity analysis: complete-case TSSEM versus any defensible one-stage/partial route if later implemented.
5. Exclusion log for beta/path, HTMT, loadings, and unsupported remaps.

## Guardrails

- Do not call the reduced models the full AI adoption model.
- Do not treat AI/source-trace candidates as human-coded values unless researcher-confirmed.
- Do not overwrite raw coder workbooks or frozen reference files.
- Do not use `PKC -> SE` for S004; the researcher has rejected that remap.
- Do not promote beta/path coefficients into primary correlations.
- Do not use nearPD matrix repair as a primary route without labeling it as an exploratory sensitivity analysis.
- Do not describe trust, anxiety, or self-efficacy as moderators in this route.

## Next work sequence

1. Build a source-clean model-family analysis input using only researcher-approved source corrections and promotions.
2. Produce a full10 coverage/evidence-map packet: pairwise k, total N, same-study co-measurement, matrix density, and source-blocked missing constructs.
3. Re-run model-family MASEM using the pre-specified families: core7 and trust6 first; ANX/SE models only if eligibility thresholds are met.
4. Produce manuscript-ready tables for eligibility, fit, paths, indirect effects, and limitations.
5. Draft the Paper A Methods and Results sections around the model-family MASEM strategy.
6. Keep Paper B separate: cross-model disagreement remains Paper B RQ3 and is not evidence for promoting Paper A source rows.

## Reference collection file

A structured reference bank for this decision is stored at:

- `paper_a/analysis_strategy/PAPER_A_MODEL_FAMILY_MASEM_REFERENCE_BANK_20260614.csv`

A human-facing copy is stored in the OneDrive analysis strategy folder.
