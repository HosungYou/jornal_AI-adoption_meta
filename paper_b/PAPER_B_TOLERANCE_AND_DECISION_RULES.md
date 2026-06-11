# Paper B Pre-Analysis Tolerance Bands and Decision Rules

Date: 2026-05-28

Status: accepted working pre-analysis rules, not empirical LLM results. These
rules define how Paper B will classify disagreement, review priority, and
downstream substitution stability before final LLM comparison or MASEM
substitution is run.

## Boundary

These rules do not authorize Step 5 analyses. The project is still in
source-document adjudication, and the source-anchored adjudicated human
reference standard is not frozen. RQ1-RQ4 remain planned analyses until the
reference file, LLM outputs, and substitution inputs are locked.

Primary local anchors:

- `data/04_extraction/README.md`
- `data/04_extraction/WORKFLOW_STATUS_LOG.md`
- `docs/06_decisions/2026-04-25_Reference_Standard_and_Disagreement_Analysis.md`
- `data/04_extraction/02_pre_adjudication_disagreement/RATER_COMPARISON_PLAYBOOK.md`
- `data/04_extraction/02_pre_adjudication_disagreement/combined/derived/combined_pairwise_disagreement_long_20260525.csv`
- `data/04_extraction/02_pre_adjudication_disagreement/combined/derived/combined_correlation_review_queue_20260525.csv`

## 1. Element-Level Numeric Tolerance Bands

These bands are triage rules, not automatic acceptance rules. A value inside a
small numeric band can still require adjudication if the source type, construct
mapping, sample, sign, or source span is wrong.

### Correlations, standardized paths, and beta-converted values

Apply these bands only after confirming that the two values refer to the same
construct pair, sample, and evidence type. Do not compare zero-order `r`, HTMT,
Fornell-Larcker diagonal values, and standardized paths as if they were the same
statistic.

| Band | Absolute difference | Interpretation | Handling |
|---|---:|---|---|
| A0 exact | 0.000 | Same reported value | Keep source-reported precision. |
| A1 rounding-only | >0.000 and <=0.005 | Likely rounding or precision difference when sign and source type match | Mark as rounding-only unless source table shows otherwise. |
| A2 small numeric difference | >0.005 and <=0.010 | Usually low magnitude but no longer pure rounding | Review when field is high consequence, repeated, or used in a focal matrix. |
| A3 material review | >0.010 and <0.050 | Meaningful coefficient difference | Source-check and log before reference freeze. |
| A4 high-priority review | >=0.050 | Difference likely capable of changing matrix or path interpretation | Review row/column alignment, construct mapping, sample choice, and source type first. |
| A5 invalid or inference-risk | sign reversal, coefficient outside valid bounds, source-type mismatch, wrong construct/sample, HTMT-only as r, Fornell-Larcker diagonal as r | Numeric tolerance is not meaningful | Expert adjudication required; do not use for automated substitution. |

### Sample size and analytic sample

| Case | Interpretation | Handling |
|---|---|---|
| Same analytic `N` | Exact agreement | Accept after source location is recorded. |
| Difference of 1 participant | Possible article-text/table-note discrepancy | Log if it affects weighting or indicates a different sample. |
| Difference greater than 1 participant | Potential analytic-sample mismatch | Source adjudication required. |
| Different subgroup, population, or sample selected | Different estimand | Resolve sample definition before any numeric rows from the study are finalized. |

No `N` tolerance should be used to silently accept a value into the MASEM input.
The tolerance only determines review priority.

### Reliability and scale statistics

| Band | Absolute difference | Handling |
|---|---:|---|
| Exact or rounding-only | <=0.005 | Mark as rounding if same scale and source table are confirmed. |
| Review | >0.005 and <=0.030 | Source-check if reliability is reported as evidence quality or sensitivity input. |
| Material | >0.030 | Log as a substantive reliability discrepancy. |

### Categorical and construct fields

There is no numeric tolerance for categorical fields. Inclusion status, target
sample, construct-family mapping, source type, matrix usability, moderator
coding, and evidence-type labels require exact rule-consistent agreement or
source-anchored adjudication.

## 2. Downstream Substitution Stability Rules

RQ4 should report both numerical deltas and interpretive consequences. A
substitution can be numerically small but still decision-changing if it alters a
sign, source eligibility decision, model-fit judgment, or focal conclusion.

### Pooled correlations

Report absolute `r` differences and a Fisher-z sensitivity audit:
`delta_z = atanh(r_llm_assisted) - atanh(r_reference)`.

| Stability class | Rule |
|---|---|
| Stable/negligible | Same sign, same included construct pair, `abs(delta_r) <= 0.010`, no interpretation change. |
| Reviewable small shift | `0.010 < abs(delta_r) <= 0.030`, no sign or conclusion change. |
| Material sensitivity | `0.030 < abs(delta_r) <= 0.050`, or focal construct-pair ranking changes. |
| Inference-changing | `abs(delta_r) > 0.050`, sign reversal, interval/decision crosses zero, construct pair appears/disappears, or model interpretation changes. |

### Structural paths

| Stability class | Rule |
|---|---|
| Stable/negligible | Same sign, same retained focal path, `abs(delta_beta) <= 0.030`, and same substantive conclusion. |
| Reviewable shift | `0.030 < abs(delta_beta) <= 0.100`, or the path is near an interpretive threshold. |
| Inference-changing | `abs(delta_beta) > 0.100`, sign reversal, retained/non-retained decision changes, focal path order changes, or conclusion changes. |

### Indirect, moderator, and model-fit conclusions

| Component | Stable if | Inference-changing if |
|---|---|---|
| Indirect effects | Same direction and same substantive conclusion | Sign, retained/non-retained decision, or interpretation changes. |
| Moderator effects | Same moderator conclusion and same direction for focal effects | Moderator support, direction, or focal subgroup interpretation changes. |
| Model fit/model comparison | Same predeclared fit or model-comparison decision | Any decision crosses the predeclared fit/model-comparison boundary. |

## 3. Task-Family Decision Categories

These categories are assigned at the task-family or field-family level after
combining human disagreement evidence, source adjudication status, LLM comparison
results, and downstream substitution risk.

| Decision category | Minimum condition | Examples | Manuscript language |
|---|---|---|---|
| `routine automation candidate` | Low consequence, high human agreement, traceable source span, exact or rounding-only LLM agreement, no cross-field dependency | DOI/year/title cleanup, journal metadata, obvious article identifiers | Candidate for automated first-pass extraction with audit sampling. |
| `LLM-assisted with human verification` | Medium consequence or moderate human disagreement, source span present, numeric difference within A1/A2, no unresolved construct/source-type issue | country, education level, participant role, reliability values, simple moderator fields | Useful for prefill and prioritization, but requires human verification. |
| `expert adjudication required` | High consequence, conceptual ambiguity, source-type ambiguity, one-coder-only evidence, A3/A4 difference, weak source span, or matrix dependency | construct mapping, analytic sample, zero-order r vs beta/path, Fornell-Larcker off-diagonal, matrix reconstruction | Requires source-document adjudication before inclusion in the reference or MASEM input. |
| `not safe for automated substitution` | Untraceable source, invalid coefficient, HTMT-only as r, Fornell-Larcker diagonal as r, wrong sample/construct, sign reversal, or inference-changing substitution | source-unavailable cells, incoherent matrix, duplicated diagonal, source-type confusion, values that alter focal paths | Must not be substituted automatically; use only after expert correction or exclude from the automated path. |

## 4. Human Disagreement Triage Priority

Use the combined Phase 1+2 pre-adjudication queue to prioritize adjudication
before the reference freeze.

| Priority | Trigger | Action |
|---|---|---|
| P0 immediate | Inclusion/exclusion split, different analytic sample, coefficient outside valid bounds, sign reversal, HTMT-only as r, Fornell-Larcker diagonal as r, duplicate/review-source issue | Source-check before any dependent rows are finalized. |
| P1 high | A4 difference, one-coder-only value in a focal matrix, source-type mismatch, construct family ambiguity involving ATT/TRU/ANX/FC/SE, matrix reconstruction failure | Review in source-document adjudication meeting and record rule applied. |
| P2 standard | A3 difference, repeated A2 differences, reliability/material measurement discrepancy, moderator boundary disagreement | Source-check before freeze; can follow P0/P1 rows. |
| P3 low | A0/A1 rounding-only, metadata spelling/capitalization, DOI/title normalization, non-focal formatting | Standardize after high-consequence rows; preserve raw disagreement as analyzable evidence. |

## 5. Reporting Implications

Paper B should make three separations visible in tables and figures:

1. Raw human-human disagreement before adjudication.
2. Source-anchored adjudicated human reference after adjudication.
3. Post-freeze LLM-assisted extraction and downstream substitution.

Recommended table additions:

- Add a tolerance-band column to the RQ0 human disagreement table.
- Add a decision-category column to the LLM validity-by-task-family table.
- Add a stability-class column to the downstream substitution table.

Recommended figure additions:

- Show coefficient deltas with A1/A3/A4 boundaries for human and LLM comparison.
- Show RQ4 coefficient/path overlays with stable, reviewable, material, and
  inference-changing zones.

## 6. Stop Rules

Stop and require expert adjudication when any of the following occurs:

- The value cannot be traced to a source table/page/section.
- The source type is unclear or mixed.
- The task involves construct-family mapping with plausible alternatives.
- A row affects analytic sample, inclusion/exclusion, or matrix membership.
- A substitution changes sign, retained/non-retained status, model-fit decision,
  or substantive conclusion.
- The proposed automated path would overwrite or hide raw coder disagreement.
