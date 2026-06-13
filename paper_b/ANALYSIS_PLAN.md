# Analysis Plan: Paper B

## Current Positioning

Updated 2026-04-24. This plan supersedes the earlier three-model comparative framework. Paper B is now framed as a validation study of one prespecified LLM-assisted workflow for MASEM-ready data extraction. Additional LLMs are not used for vendor ranking; their current role is to support cross-model disagreement as a main RQ3 triage signal.

The central methodological question is not which model wins. The central question is whether a transparent, documented, human-supervised LLM workflow can assist with extraction tasks that matter for MASEM: construct harmonization, correlation matrix recovery, moderator coding, and downstream inference stability.

Updated 2026-05-28. The current Paper B direction is **task-contingent LLM augmentation, not replacement**. The manuscript should not be organized around a single overall LLM accuracy score. It should evaluate extraction by task family, human-human disagreement, source-anchored adjudication, matrix readiness, error consequence, human-review triage value, and downstream MASEM substitution stability.

## Phase Status and Protocol Amendment

Updated 2026-04-25. Phase 1 human pairwise coding is complete. Phase 2 uses
rotated human pairs rather than AI-first single verification. Phase 1 and Phase
2 now form one combined Paper B validation corpus:

- Phase 0 calibration: 10 studies, separate calibration/training block
- Phase 1 validation Wave 1: 100 studies; Pair A = R1+R2; Pair B = R3+R4
- Phase 2 validation Wave 2: 113 studies; Pair C = R1+R4; Pair D = R2+R3
- Combined Paper B validation corpus: 213 studies
- LLM outputs remain unavailable to human coders until each phase's independent coding and adjudication are complete
- Phase is modeled as a time block / coding wave / reviewer-pair block, not as a primary-versus-optional tier

## Research Questions

**RQ0. Human coding difficulty before adjudication.** Where do independent human coders disagree before consensus, and which fields, source formats, construct mappings, or phase blocks explain that disagreement?

**RQ1. Extraction validity.** How accurately does the prespecified LLM workflow extract bibliographic, sample, construct, measurement, correlation, and moderator information relative to an adjudicated human reference standard?

**RQ2. Error taxonomy and source conditions.** Which extraction families, study characteristics, reporting formats, source types, or construct ambiguities explain human and LLM extraction errors?

**RQ3. Human-review triage value.** Can human-human disagreement, LLM uncertainty, source-type flags, or cross-model disagreement identify the rows, fields, or studies that most need expert review?

**RQ4. Downstream substitution stability.** If human-supervised LLM-assisted values are substituted into the MASEM input, do the pooled correlations, structural path coefficients, indirect effects, model-fit decisions, and substantive conclusions remain stable?

**Model-sensitivity boundary.** If additional models are evaluated, they support RQ3 triage through cross-model disagreement and do not create a vendor-ranking or autonomous-replacement claim.

## Data Structure

| Level | Unit | Examples | Primary use |
|---|---|---|---|
| Study | One primary article | Year, country, sample, design | Sampling and moderator diagnostics |
| Construct | Construct instance within study | PE, EE, ATT, BI, TRU, ANX | Construct harmonization validity |
| Statistic | Extracted numeric value | r, alpha, N, reliability | Numeric extraction accuracy |
| Matrix | Study-level correlation matrix | Construct order, cells, missingness | MASEM readiness |
| Model | Pooled MASEM output | Path estimates, indirect effects | Downstream substitution analysis |

## Source-Anchored Adjudicated Human Reference Standard

Human coders independently extract the validation sample using a shared codebook. Discrepancies are resolved through cross-pair adjudication and logged. The final adjudicated dataset is the reference standard for evaluation. The manuscript should avoid implying that this standard is flawless; it is the best available expert interpretation of the source documents.

The reference standard has two waves:

| Wave | Human coding design | Primary role in Paper B |
|---|---|---|
| Phase 1 | R1+R2 and R3+R4 independent pair coding; cross-pair adjudication | Validation Wave 1 |
| Phase 2 | R1+R4 and R2+R3 rotated pair coding; cross-pair adjudication | Validation Wave 2 |

Phase 2 is valuable because it changes pair composition. This helps evaluate whether the workflow is robust beyond the original R1-R2 and R3-R4 pair structure.

Current workload:

| Coder | Phase 1 studies | Phase 2 studies | Additional Phase 2 load |
|---|---:|---:|---:|
| R1 | 50 | 57 | +7 |
| R2 | 50 | 56 | +6 |
| R3 | 50 | 56 | +6 |
| R4 | 50 | 57 | +7 |

The analysis preserves five dataset states: raw human coder data, pairwise diff
data, adjudicated human reference, LLM outputs, and LLM-assisted analysis input.
Raw disagreement should be analyzed before adjudication, while LLM accuracy and
MASEM substitution analyses use only the frozen adjudicated reference.

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

## MASEM-Ready Extraction Task Taxonomy

Paper B should report task-family results rather than collapse validity into a single metric.

| Task family | Example fields | Main difficulty | Error consequence | Primary metric |
|---|---|---|---|---|
| Bibliographic metadata | title, year, DOI, journal | source identification | low | exact agreement |
| Sample definition | N, subgroup, country, participant role | analytic sample selection | medium/high | exact or tolerance agreement |
| Construct mapping | original label to MASEM construct family | conceptual equivalence | high | agreement plus adjudication type |
| Measurement evidence | scale, reliability, source table | fragmented reporting | medium | agreement and missingness |
| Numeric evidence recovery | r, beta, alpha, p, SE | table parsing and source type | high | absolute error and tolerance band |
| Matrix reconstruction | order, symmetry, completeness | matrix assembly | high | matrix diagnostics |
| Moderator coding | AI type, education level, region, design | boundary coding | medium/high | agreement and discrepancy type |
| MASEM import readiness | usable row or cell status | cross-field consistency | high | import/pass-fail plus error class |

Decision categories should be bounded and task-specific:

- `routine automation candidate`
- `LLM-assisted with human verification`
- `expert adjudication required`
- `not safe for automated substitution`

Operational pre-analysis rules for these categories are accepted as working
rules in `PAPER_B_TOLERANCE_AND_DECISION_RULES.md`. That document defines
coefficient, sample-size, reliability, categorical-field, triage, and downstream
substitution rules before any final LLM comparison is run.

## RQ1: Extraction Validity

Categorical and nominal fields will be evaluated with exact agreement, Cohen's kappa where applicable, and Gwet's AC1/AC2 when prevalence imbalance makes kappa unstable. Numeric fields will be evaluated with mean absolute error, root mean squared error, and the proportion of values inside prespecified tolerance bands. Correlation coefficients should be evaluated with tighter tolerance than descriptive sample fields.

The tolerance bands are pre-analysis decision rules rather than post hoc
justifications. For correlation/path values, the current draft distinguishes
exact agreement, rounding-only differences, small numeric differences, material
review differences, high-priority differences, and invalid or inference-risk
cases. Source-type mismatches, sign reversals, HTMT-only values used as
correlations, Fornell-Larcker diagonals used as correlations, wrong samples, and
wrong construct mappings override numeric tolerance and require expert
adjudication.

Primary outputs:

| Output | Description |
|---|---|
| Table 1 | Validation design summary |
| Table 2 | Planned analysis and reporting matrix |
| Table 3 | Primary results shell by extraction family |
| Appendix table | Field-level agreement and discrepancy rates |

## RQ0: Raw Human-Human Disagreement Before Adjudication

The first empirical step is not LLM evaluation. It is a human disagreement
analysis using raw independent coder values before any consensus meeting.

Planned outputs:

| Output | Description |
|---|---|
| Human disagreement table | Field-family disagreement rates by phase and pair |
| Numeric disagreement plot | Absolute coder differences for r, beta, N, and reliability values |
| Construct mapping review | Construct labels that produced human disagreement before adjudication |
| Phase block check | Phase 1 versus Phase 2 disagreement comparison |

This analysis establishes the difficulty of the extraction task. It also helps
interpret later LLM errors: a mismatch on a field where humans also disagreed is
different from a mismatch on a routine field that humans coded consistently.

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

## RQ3: Human-Review Triage Value

The manuscript should test whether review signals help prioritize expert adjudication rather than imply unsupervised replacement.

Candidate triage signals:

| Signal | Rationale |
|---|---|
| Human-human disagreement in the same field family | Human disagreement marks task difficulty before LLM evaluation |
| Missing or weak source span in LLM output | Low source anchoring should trigger review |
| Source-type flags | HTMT, Fornell-Larcker, beta-only, path-only, or no-matrix cases are high risk |
| Construct-family overlap | ATT, TRU, ANX, FC, and SE labels often overlap with adjacent constructs |
| Cross-model disagreement, if retained | Supplementary signal for review load, not a vendor-ranking result |

Primary outputs:

| Output | Description |
|---|---|
| Triage flag table | Field-family rows with human disagreement, LLM missingness, source-type flags, and review priority |
| Review-yield estimate | How many high-consequence errors are captured by each signal |
| False reassurance audit | Cases where routine-looking rows still required source adjudication |

The triage draft prioritizes P0/P1 cases before the reference freeze:
inclusion/exclusion splits, analytic-sample disagreements, invalid coefficients,
sign reversals, HTMT/Fornell-Larcker misuse, source-type mismatches,
one-coder-only focal matrix values, construct-family ambiguity, and matrix
reconstruction failures.

## RQ4: Downstream Substitution Analysis

The substitution analysis is the core methodological contribution. It asks whether LLM-assisted extraction would change the substantive conclusions of the MASEM after human-supervised review.

Researcher-approved route recorded on 2026-06-12: attempt a broader TSSEM/MASEM rebuild. The existing core-6 diagnostic remains the completed bounded evidence until the broader rebuild specification, source-type sufficiency audit, and successful run are complete.

Planned comparisons:

| Component | Human-coded input | LLM-assisted input | Stability criterion |
|---|---|---|---|
| Pooled correlations | Reference matrix | LLM-assisted matrix | No material shift beyond prespecified tolerance |
| Structural paths | Reference estimates | LLM-assisted estimates | No reversal of focal path signs |
| Indirect effects | Reference indirect effects | LLM-assisted indirect effects | Interpretation remains substantively similar |
| Moderator effects | Reference moderator model | LLM-assisted moderator model | Same substantive moderator conclusion |
| Model fit | Reference MASEM fit | LLM-assisted MASEM fit | No decision-changing deterioration |

The manuscript should report both numerical differences and interpretive consequences. A workflow may be suitable for first-pass extraction even if it is not suitable for unsupervised synthesis.

The planned substitution rules classify deltas as stable/negligible, reviewable,
material sensitivity, or inference-changing. Pooled correlations should report
absolute `r` differences plus a Fisher-z sensitivity audit. Structural paths,
indirect effects, moderator conclusions, and model-fit decisions should be
treated as unstable whenever signs, retained/non-retained decisions, fit
threshold decisions, or substantive conclusions change.

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

## Table Plan

| Table | Purpose | Current status |
|---|---|---|
| Table 1. Validation design and dataset states | Show raw human coding, pairwise disagreement, adjudicated reference, LLM outputs, and substitution inputs as separate states | Can be drafted now |
| Table 2. MASEM-ready extraction task taxonomy | Define task families, difficulty, consequence, and metrics | Can be drafted now |
| Table 3. RQ0 human disagreement results | Report Phase 1+2 pairwise disagreement by phase, pair, field family, and mismatch type | Can be populated from combined disagreement artifacts |
| Table 4. LLM validity by task family | Report post-freeze LLM agreement/error and decision category | Planned; requires frozen reference and locked LLM outputs |
| Table 5. Downstream substitution stability | Compare human-reference and LLM-assisted MASEM outputs using predeclared stability classes | Planned; requires locked substitution inputs |

## Figure Plan

**Figure 1. Study design flow.** Raw human coding -> pre-adjudication human disagreement -> source-document adjudication -> frozen human reference -> LLM comparison -> MASEM substitution. The figure must visually enforce that LLM comparison begins only after reference freeze.

**Figure 2. MASEM-ready extraction task taxonomy.** Layer routine identification, sample/source definition, construct harmonization, numeric evidence recovery, matrix reconstruction, and MASEM inference with an error-consequence gradient.

**Figure 3. Human-human disagreement heatmap.** Rows should be task families or construct pairs; columns should be Phase 1 Pair A, Phase 1 Pair B, Phase 2 Pair C, and Phase 2 Pair D.

**Figure 4. LLM error by task family.** Rows should be task families; columns should include exact agreement, missingness, numeric error, source-type error, and construct-map error.

**Figure 5. Downstream substitution stability.** Overlay human-reference and LLM-assisted estimates for focal paths with equivalence or tolerance bands. Current simulated values must be replaced after analysis.

## Analysis Sequence

1. Report corpus and validation design.
2. Report RQ0 human-human pre-adjudication disagreement.
3. Freeze and describe the source-anchored adjudicated human reference.
4. Evaluate LLM validity by task family.
5. Classify errors by taxonomy and source condition.
6. Evaluate human-review triage signals.
7. Run downstream substitution only after the reference and LLM-assisted inputs are locked.
8. Interpret whether LLM assistance is safe for routine extraction, review support, or not safe for automated substitution.

## Claims To Avoid

- Do not claim that LLMs can replace human coders.
- Do not make a model or vendor ranking the main contribution.
- Do not treat overall accuracy as proof of suitability for MASEM.
- Do not call the adjudicated human reference a perfect gold standard.
- Do not present LLM substitution as acceptable before source-anchored adjudication.

## Claims To Make

- MASEM-ready extraction is a multi-layer evidence recovery task.
- Human-human disagreement is a necessary baseline for interpreting LLM errors.
- LLM performance should be evaluated by task family and error consequence.
- Source-anchored adjudication is required before LLM comparison.
- The practical contribution is bounded augmentation and expert review triage.
- The downstream test is whether human-supervised LLM assistance preserves MASEM conclusions.

## Minimum Evidence Needed Before Submission

Paper B should not be submitted until these exist:

1. Frozen source-anchored adjudicated human reference standard.
2. Versioned primary LLM workflow outputs.
3. Field-family validity table.
4. Error taxonomy table with source-backed examples.
5. Matrix-readiness diagnostics.
6. Human-review triage analysis.
7. Downstream substitution analysis using locked human-reference and LLM-assisted inputs.
8. Prompt, schema, model, preprocessing, and analysis-script archive.

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
