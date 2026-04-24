# Analysis Plan: Paper B

## Current Positioning

Updated 2026-04-24. This plan supersedes the earlier three-model comparative framework. Paper B is now framed as a validation study of one prespecified LLM-assisted workflow for MASEM-ready data extraction. Additional LLMs may be used only as supplementary robustness or triage analyses.

The central methodological question is not which model wins. The central question is whether a transparent, documented, human-supervised LLM workflow can assist with extraction tasks that matter for MASEM: construct harmonization, correlation matrix recovery, moderator coding, and downstream inference stability.

## Phase Status and Protocol Amendment

Updated later on 2026-04-24. Phase 1 human pairwise coding is complete. Phase 2
will use rotated human pairs rather than AI-first single verification:

- Phase 1 primary validation sample: Pair A = R1+R2; Pair B = R3+R4
- Phase 2 operational/external validation sample: Pair C = R1+R4; Pair D = R2+R3
- LLM outputs remain unavailable to human coders until each phase's independent coding and adjudication are complete
- Phase 2 can be reported in Paper B only as external validation, triage sensitivity, or workload simulation if the analysis is frozen before LLM comparison

## Research Questions

**RQ1. Extraction validity.** How accurately does the prespecified LLM workflow extract bibliographic, sample, construct, measurement, correlation, and moderator information relative to an adjudicated human reference standard?

**RQ2. Systematic error.** Which extraction families, study characteristics, reporting formats, or construct ambiguities are associated with LLM extraction errors?

**RQ3. Downstream stability.** Do LLM-assisted inputs preserve the pooled correlations, structural path coefficients, indirect effects, and substantive conclusions obtained from human-coded inputs?

**Supplementary RQ. Model sensitivity.** If additional models are evaluated, does cross-model disagreement help identify extraction fields requiring human review?

## Data Structure

| Level | Unit | Examples | Primary use |
|---|---|---|---|
| Study | One primary article | Year, country, sample, design | Sampling and moderator diagnostics |
| Construct | Construct instance within study | PE, EE, ATT, BI, TRU, ANX | Construct harmonization validity |
| Statistic | Extracted numeric value | r, alpha, N, reliability | Numeric extraction accuracy |
| Matrix | Study-level correlation matrix | Construct order, cells, missingness | MASEM readiness |
| Model | Pooled MASEM output | Path estimates, indirect effects | Downstream substitution analysis |

## Human Reference Standard

Human coders independently extract the validation sample using a shared codebook. Discrepancies are resolved through cross-pair adjudication and logged. The final adjudicated dataset is the reference standard for evaluation. The manuscript should avoid implying that this standard is flawless; it is the best available expert interpretation of the source documents.

The reference standard has two tiers:

| Tier | Human coding design | Primary role in Paper B |
|---|---|---|
| Phase 1 | R1+R2 and R3+R4 independent pair coding; cross-pair adjudication | Primary validation sample |
| Phase 2 | R1+R4 and R2+R3 rotated pair coding; cross-pair adjudication | Optional external validation, triage sensitivity, and workload simulation |

The Phase 2 tier is valuable because it changes pair composition. This helps evaluate whether the workflow is robust beyond the original R1-R2 and R3-R4 pair structure.

## Primary LLM Workflow

The primary workflow uses the prespecified Codex 5.5 configuration. The final manuscript must report the exact model identifier, interface, access dates, prompt version, preprocessing steps, output schema, model settings, and human oversight procedure.

The workflow returns structured outputs for:

| Extraction family | Expected fields | Evaluation approach |
|---|---|---|
| Bibliographic metadata | Title, year, journal, DOI | Exact agreement |
| Sample characteristics | N, population, country, education level | Exact or tolerance-based agreement |
| Construct harmonization | Original construct, mapped construct family | Agreement plus adjudicated disagreement review |
| Measurement details | Instrument, scale source, reliability | Exact/tolerance agreement and missingness |
| Correlation extraction | r values, sample sizes, matrix source | Absolute error and tolerance-band agreement |
| Matrix reconstruction | Completeness, symmetry, construct order | Matrix diagnostics |
| Moderator coding | Tool type, role, setting, design | Agreement and discrepancy typology |

## RQ1: Extraction Validity

Categorical and nominal fields will be evaluated with exact agreement, Cohen's kappa where applicable, and Gwet's AC1/AC2 when prevalence imbalance makes kappa unstable. Numeric fields will be evaluated with mean absolute error, root mean squared error, and the proportion of values inside prespecified tolerance bands. Correlation coefficients should be evaluated with tighter tolerance than descriptive sample fields.

Primary outputs:

| Output | Description |
|---|---|
| Table 1 | Validation design summary |
| Table 2 | Planned analysis and reporting matrix |
| Table 3 | Primary results shell by extraction family |
| Appendix table | Field-level agreement and discrepancy rates |

## RQ2: Systematic Error

Errors will be classified by extraction family and by source of difficulty. Expected sources include ambiguous construct labels, partial correlation matrices, multiple samples within one article, PLS-SEM tables with Fornell-Larcker diagonals, appendices split across files, and studies with incomplete reporting.

Potential predictors of extraction error:

| Predictor | Rationale |
|---|---|
| Reporting format | Tables, appendices, narrative-only reporting may differ in parseability |
| Matrix type | Pearson, latent correlation, Fornell-Larcker, HTMT, or mixed tables |
| Construct ambiguity | Similar labels may map to different theoretical families |
| Study design | PLS-SEM, CB-SEM, survey-only, intervention, or mixed design |
| Publication year | Newer studies may reduce training-data contamination risk |
| PDF quality | OCR quality and table structure affect extraction |

For binary error outcomes, use logistic regression or mixed-effects logistic regression if multiple fields are nested within studies. For numeric error, use absolute error as the dependent variable and examine robust or mixed-effects models as needed.

## RQ3: Downstream Substitution Analysis

The substitution analysis is the core methodological contribution. It asks whether LLM-assisted extraction would change the substantive conclusions of the MASEM after human-supervised review.

Planned comparisons:

| Component | Human-coded input | LLM-assisted input | Stability criterion |
|---|---|---|---|
| Pooled correlations | Reference matrix | LLM-assisted matrix | No material shift beyond prespecified tolerance |
| Structural paths | Reference estimates | LLM-assisted estimates | No reversal of focal path signs |
| Indirect effects | Reference indirect effects | LLM-assisted indirect effects | Interpretation remains substantively similar |
| Moderator effects | Reference moderator model | LLM-assisted moderator model | Same substantive moderator conclusion |
| Model fit | Reference MASEM fit | LLM-assisted MASEM fit | No decision-changing deterioration |

The manuscript should report both numerical differences and interpretive consequences. A workflow may be suitable for first-pass extraction even if it is not suitable for unsupervised synthesis.

## Human-Human vs. LLM-Human Disagreement

Because MASEM extraction is not primarily a human rating task, the validation should
not force all outputs into artificial categories. Numeric extraction cells should be
evaluated as evidence-recovery values, while construct mapping and inclusion decisions
should be evaluated as categorical or ordinal judgments.

Planned comparison:

| Comparison | Purpose |
|---|---|
| R1-R2 and R3-R4 disagreement | Establish Phase 1 human coding difficulty |
| R1-R4 and R2-R3 disagreement | Establish Phase 2 difficulty under rotated pairs |
| Primary LLM vs adjudicated human reference | Evaluate extraction validity |
| Cross-model disagreement vs human disagreement | Test whether model disagreement can triage hard fields |

Visualizations should emphasize error and consequence rather than artificial category
formation: scatterplots with tolerance bands, Bland-Altman plots, study-by-construct
delta heatmaps, error-taxonomy bar charts, and human-vs-LLM MASEM path overlays.

## Supplementary Model Sensitivity

If Claude or Gemini outputs are retained, they should be analyzed only as secondary sensitivity checks. The analysis should ask whether model disagreement flags uncertain fields, not which vendor is best.

Possible outputs:

| Analysis | Purpose |
|---|---|
| Cross-model disagreement rate | Identify fields requiring human review |
| Disagreement by extraction family | Locate difficult extraction tasks |
| Primary workflow vs. alternative workflow | Assess robustness of conclusions |
| Triage simulation | Estimate human review savings when disagreement triggers review |

## Figure Plan

**Figure 1. Downstream substitution stability simulation.** This figure illustrates how the final manuscript will compare LLM-assisted path estimates with human-reference path estimates. Current figure values are simulated placeholders and must be replaced after analysis.

## Reproducibility Requirements

The final manuscript should archive:

| Artifact | Required content |
|---|---|
| Codebook | Field definitions, coding rules, construct mapping rules |
| Prompts | Full prompt text, version, and development notes |
| Logs | Extraction dates, model identifiers, errors, adjudication records |
| Validation data | Human reference data and LLM outputs where permissible |
| Analysis scripts | Agreement metrics, matrix diagnostics, substitution analysis |
| Environment | Software versions, API/interface details, random seeds if applicable |
