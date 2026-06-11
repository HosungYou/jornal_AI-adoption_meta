# Paper B Direction Memo: Task-Contingent LLM Augmentation for MASEM-Ready Extraction

Date: 2026-05-27

Status: design memo, not empirical results. The source-anchored adjudicated human reference standard is not frozen yet, so LLM accuracy and MASEM substitution analyses must remain planned analyses.

## Working Position

Paper B should be framed as a methods paper about **task-contingent augmentation, not replacement**.

The central claim is:

> LLM-assisted extraction for MASEM should not be judged by a single overall accuracy score. It should be evaluated by task family, human disagreement, source-anchored adjudication, matrix readiness, and downstream inferential stability.

This moves the paper away from a vendor/model benchmark and toward a durable validation template for complex quantitative synthesis.

## Why This Framing Is Stronger

Existing LLM evidence-synthesis studies already show that LLMs can assist with systematic review data extraction, but they also show that performance varies by task type, outcome type, source format, and validation design. Paper B should therefore avoid the weak claim that an LLM "can extract data." That claim is no longer distinctive.

Paper B's distinctive contribution is narrower and stronger:

1. MASEM-ready extraction is harder than ordinary study-characteristic extraction.
2. Human coders disagree before adjudication, and that disagreement is evidence about task difficulty.
3. A source-anchored adjudicated human reference standard is needed before LLM comparison.
4. The practical question is whether LLM-assisted inputs preserve MASEM conclusions after human supervision.

## Current Local Evidence Anchor

The current combined Phase 1+2 pre-adjudication artifacts already support the first empirical layer of the paper.

Source files:

- `data/04_extraction/02_pre_adjudication_disagreement/combined/derived/combined_pairwise_disagreement_summary_20260525.csv`
- `data/04_extraction/02_pre_adjudication_disagreement/combined/derived/combined_pairwise_disagreement_long_20260525.csv`
- `data/04_extraction/WORKFLOW_STATUS_LOG.md`

Current pre-adjudication disagreement counts from the combined 213-study validation corpus:

| Family or type | Count |
|---|---:|
| Total pre-adjudication disagreement rows | 2,949 |
| Metadata disagreement rows | 1,585 |
| Correlation disagreement rows | 1,364 |
| Correlation numeric/source differences | 734 |
| Correlation one-coder-only rows | 630 |

These counts are not results for LLM performance. They are the empirical basis for RQ0: MASEM-ready extraction contains field families where trained human coders disagree before source adjudication.

## Revised Research Questions

### RQ0. Human Task Difficulty

Where do independent human coders disagree before adjudication, and what does this reveal about the task structure of MASEM-ready extraction?

Planned outputs:

- Disagreement rates by phase, pair, field family, and mismatch type.
- Correlation/path coefficient differences by tolerance band.
- One-coder-only evidence recovery cases.
- Construct-mapping disagreements and source-type disagreements.

Interpretation:

RQ0 establishes the baseline difficulty of the extraction task before LLMs are evaluated. This prevents the paper from treating human-coded data as a black-box truth source.

### RQ1. Task-Contingent LLM Validity

How accurately does the prespecified LLM workflow recover MASEM-ready extraction fields relative to the source-anchored adjudicated human reference standard?

Evaluate by task family rather than a single score:

- Bibliographic metadata.
- Sample and analytic N.
- Construct names and target construct mappings.
- Measurement and reliability evidence.
- Correlation/path coefficient recovery.
- Matrix reconstruction.
- Moderator coding.

Interpretation:

The paper should identify where LLM assistance is routine, where it is reviewable, and where it is unsafe without expert source adjudication.

### RQ2. Error Taxonomy and Source Conditions

Which field families, source formats, reporting structures, and construct ambiguities explain human and LLM extraction errors?

Candidate error classes:

| Error class | Description | Likely consequence |
|---|---|---|
| Routine metadata error | Wrong or missing DOI, year, journal, or title variant | Usually low consequence |
| Sample-definition error | Wrong analytic N, subgroup, country, or participant role | Affects weights and moderator coding |
| Construct-mapping error | Original construct mapped to wrong MASEM family | Can alter correlation matrix structure |
| Source-type error | HTMT, Fornell-Larcker, beta/path, or zero-order r confused | Can invalidate matrix cells |
| Numeric recovery error | Wrong r, beta, reliability, or p-value | Can shift pooled correlations |
| Matrix-readiness error | Missing symmetry, wrong construct order, duplicated diagonal, or untraceable source | Blocks direct MASEM import |
| Inference-changing error | Error changes sign, model fit, path interpretation, or moderator conclusion | Highest consequence |

Interpretation:

This is the paper's taxonomy contribution. The taxonomy should be empirical enough to be supported by RQ0/RQ1, but general enough for other synthesis teams to reuse.

### RQ3. Human-Review Triage Value

Can disagreement signals help prioritize human review?

Candidate signals:

- Human-human disagreement in the same field family.
- LLM uncertainty or missing source span.
- Cross-model disagreement if supplementary models are retained.
- Source-type flags: HTMT, Fornell-Larcker, beta-only, path-only, no matrix.
- High-risk construct families: ATT, TRU, ANX, FC, SE where labels overlap with adjacent constructs.

Interpretation:

The practical value is not unsupervised replacement. It is directing expert time toward rows where errors are likely or consequential.

### RQ4. Downstream Substitution Stability

If LLM-assisted values are substituted into the MASEM input after human supervision, do the substantive conclusions remain stable?

Compare:

- Pooled correlation matrices.
- Focal structural path estimates.
- Indirect effects.
- Model fit decisions.
- Moderator conclusions.
- Sensitivity analyses for beta-converted and source-type-flagged values.

Interpretation:

Element-level accuracy is not enough. A workflow is useful only if its errors do not change the substantive interpretation, or if its review flags successfully catch the errors that would change interpretation.

### Supplementary RQ. Model Sensitivity

If additional models are used, do not rank vendors in the main text. Use cross-model disagreement only as a supplementary triage signal.

## Table Shells

### Table 1. Validation Design and Dataset States

| Component | Description | Paper B role | Current status |
|---|---|---|---|
| Parent corpus | Educational AI adoption MASEM corpus | Source population | Active in Paper A |
| Validation corpus | Phase 1+2 213-study corpus | Paper B empirical corpus | Pre-adjudication artifacts exist |
| Raw human coder data | Independent human coding before adjudication | RQ0 baseline | Frozen/preserved by phase |
| Pairwise diff data | Human-human disagreement tables | Task difficulty evidence | Combined outputs generated |
| Source-anchored adjudicated human reference | Source-resolved expert reference | RQ1-RQ4 comparison baseline | Not frozen |
| LLM outputs | Prespecified workflow output | Post-freeze evaluation only | Planned |
| LLM-assisted MASEM input | Human-supervised substitution input | RQ4 | Planned |

### Table 2. MASEM-Ready Extraction Task Taxonomy

| Task family | Example fields | Main difficulty | Error consequence | Primary metric |
|---|---|---|---|---|
| Bibliographic metadata | title, year, DOI, journal | source identification | low | exact agreement |
| Sample definition | N, subgroup, country, role | analytic sample selection | medium/high | exact/tolerance agreement |
| Construct mapping | original label -> MASEM construct | conceptual equivalence | high | agreement + adjudication type |
| Measurement evidence | scale, reliability, source table | fragmented reporting | medium | agreement/missingness |
| Numeric evidence recovery | r, beta, alpha, p, SE | table parsing and source type | high | absolute error + tolerance band |
| Matrix reconstruction | order, symmetry, completeness | matrix assembly | high | matrix diagnostics |
| Moderator coding | AI type, education level, region, design | boundary coding | medium/high | agreement + discrepancy type |
| MASEM import readiness | usable row/cell status | cross-field consistency | high | import/pass-fail + error class |

### Table 3. RQ0 Human Disagreement Results Shell

| Phase | Pair | Field family | Mismatch type | Count | Priority interpretation |
|---|---|---|---|---:|---|
| Phase 1 | Pair A | correlation | numeric/source difference | 373 | high source-check load |
| Phase 1 | Pair A | correlation | one coder only | 170 | evidence recovery asymmetry |
| Phase 1 | Pair A | metadata | metadata difference | 429 | routine standardization burden |
| Phase 1 | Pair B | correlation | numeric/source difference | 97 | source-type review |
| Phase 1 | Pair B | correlation | one coder only | 276 | evidence recovery asymmetry |
| Phase 1 | Pair B | metadata | metadata difference | 334 | routine standardization burden |
| Phase 2 | Pair C | correlation | numeric/source difference | 193 | source-check load |
| Phase 2 | Pair C | correlation | one coder only | 64 | evidence recovery asymmetry |
| Phase 2 | Pair C | metadata | metadata difference | 463 | routine standardization burden |
| Phase 2 | Pair D | correlation | numeric/source difference | 71 | source-check load |
| Phase 2 | Pair D | correlation | one coder only | 120 | evidence recovery asymmetry |
| Phase 2 | Pair D | metadata | metadata difference | 359 | routine standardization burden |

### Table 4. LLM Validity Results Shell

| Task family | N fields/cells | Human disagreement baseline | LLM agreement/error | Adjudication need | Decision category |
|---|---:|---:|---:|---:|---|
| Bibliographic metadata | TBD | TBD | TBD | TBD | automate/review |
| Sample definition | TBD | TBD | TBD | TBD | review |
| Construct mapping | TBD | TBD | TBD | TBD | expert review |
| Measurement evidence | TBD | TBD | TBD | TBD | review |
| Correlation/path recovery | TBD | TBD | TBD | TBD | expert review |
| Matrix reconstruction | TBD | TBD | TBD | TBD | expert review |
| Moderator coding | TBD | TBD | TBD | TBD | review |

Decision category should use bounded labels:

- `routine automation candidate`
- `LLM-assisted with human verification`
- `expert adjudication required`
- `not safe for automated substitution`

### Table 5. Downstream Substitution Results Shell

| MASEM output | Human-reference input | LLM-assisted input | Difference | Stability rule | Interpretation |
|---|---:|---:|---:|---|---|
| pooled PE-BI correlation | TBD | TBD | TBD | tolerance band | TBD |
| pooled EE-BI correlation | TBD | TBD | TBD | tolerance band | TBD |
| PE -> BI path | TBD | TBD | TBD | no sign/substantive reversal | TBD |
| ATT -> BI path | TBD | TBD | TBD | no sign/substantive reversal | TBD |
| TRU -> BI path | TBD | TBD | TBD | no sign/substantive reversal | TBD |
| ANX -> BI path | TBD | TBD | TBD | no sign/substantive reversal | TBD |
| Model 1 vs Model 2 decision | TBD | TBD | TBD | same model-comparison conclusion | TBD |
| Key moderator conclusion | TBD | TBD | TBD | same substantive conclusion | TBD |

## Figure Shells

### Figure 1. Study Design Flow

Show the sequence:

Raw human coding -> pre-adjudication human disagreement -> source-document adjudication -> frozen human reference -> LLM comparison -> MASEM substitution.

The figure should visually enforce the rule that LLM comparison begins only after the reference standard is frozen.

### Figure 2. MASEM-Ready Extraction Task Taxonomy

Layered diagram:

1. Routine identification.
2. Sample and source definition.
3. Construct harmonization.
4. Numeric evidence recovery.
5. Matrix reconstruction.
6. MASEM inference.

Add an error-consequence gradient from low to high.

### Figure 3. Human-Human Disagreement Heatmap

Rows: task families or construct pairs.

Columns: Phase 1 Pair A, Phase 1 Pair B, Phase 2 Pair C, Phase 2 Pair D.

Cells: disagreement count, rate, or standardized residual.

Purpose: show that task difficulty is uneven across extraction families and coding waves.

### Figure 4. LLM Error by Task Family

Rows: task families.

Columns: exact agreement, missingness, numeric error, source-type error, construct-map error.

Purpose: prevent a single overall accuracy number from dominating the paper.

### Figure 5. Downstream Substitution Stability

Overlay human-reference and LLM-assisted estimates for focal paths with equivalence/tolerance bands.

Recommended display:

- coefficient plot for structural paths;
- delta heatmap for pooled correlations;
- small panel for model-fit or model-comparison decisions.

## Analysis Sequence

1. Report corpus and validation design.
2. Report RQ0 human-human pre-adjudication disagreement.
3. Freeze and describe the source-anchored adjudicated human reference.
4. Evaluate LLM validity by task family.
5. Classify errors by taxonomy and source condition.
6. Evaluate triage signals.
7. Run downstream substitution only after the reference and LLM-assisted inputs are locked.
8. Interpret whether LLM assistance is safe for routine extraction, review support, or not safe for automated substitution.

## Claims To Avoid

- Avoid: LLMs can replace human coders.
- Avoid: One model is best for systematic review extraction.
- Avoid: Overall accuracy proves suitability for MASEM.
- Avoid: The adjudicated human reference is a perfect gold standard.
- Avoid: LLM substitution is acceptable before source-anchored adjudication.

## Claims To Make

- MASEM-ready extraction is a multi-layer evidence recovery task.
- Human-human disagreement is a necessary baseline for interpreting LLM errors.
- LLM performance should be evaluated by task family and error consequence.
- Source-anchored adjudication is required before LLM comparison.
- The ultimate test is whether human-supervised LLM assistance preserves downstream MASEM conclusions.

## Minimum Evidence Needed Before Submission

Paper B should not be submitted until these exist:

1. Frozen source-anchored adjudicated human reference standard.
2. Versioned primary LLM workflow outputs.
3. Field-family validity table.
4. Error taxonomy table with source-backed examples.
5. Matrix-readiness diagnostics.
6. Downstream substitution analysis using locked human-reference and LLM-assisted inputs.
7. Prompt, schema, model, preprocessing, and analysis-script archive.

## Reference Anchors

- Gartlehner et al. (2024), "Data extraction for evidence synthesis using a large language model: A proof-of-concept study." Research Synthesis Methods. https://doi.org/10.1002/jrsm.1710
- Konet et al. (2024), "Performance of two large language models for data extraction in evidence synthesis." Research Synthesis Methods. https://pubmed.ncbi.nlm.nih.gov/38895747/
- "What level of automation is good enough? A benchmark of large language models for meta-analysis data extraction." Research Synthesis Methods. https://www.cambridge.org/core/journals/research-synthesis-methods/article/what-level-of-automation-is-good-enough-a-benchmark-of-large-language-models-for-metaanalysis-data-extraction/2EA4DAFAAC11E76216DC0A512CA29D59
- PRISMA-trAIce checklist. https://pmc.ncbi.nlm.nih.gov/articles/PMC12694947/
- TRIPOD-LLM statement. https://www.nature.com/articles/s41591-024-03425-5
