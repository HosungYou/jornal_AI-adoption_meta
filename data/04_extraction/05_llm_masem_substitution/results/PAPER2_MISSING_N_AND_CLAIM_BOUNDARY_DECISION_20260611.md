# Paper2 Missing-N and Claim-Boundary Decision

Date: 2026-06-11

## Decision

Paper 2 is framed as a task-contingent LLM augmentation and validation study,
not as an LLM replacement study. The primary claim is that a prespecified,
source-anchored, human-adjudicated workflow can evaluate LLM extraction behavior
by task family and can support bounded downstream substitution diagnostics.

## Approved Missing-N Rule

Rows that still lack source-supported numeric sample size after deterministic
sample-size reconciliation are excluded from N-weighted TSSEM/MASEM weighting.
They remain in the extraction, scoring, audit, and descriptive sensitivity
datasets, but they must be flagged as not eligible for N-weighted SEM.

## Sample-Size Source Hierarchy

Use the most specific source-supported sample size available for the statistic:

1. Pair-, table-, matrix-, or model-specific N.
2. Correlation matrix or structural model N for the exact row set.
3. Subsample, group, country, wave, or stratum N when the effect is explicitly
   tied to that group.
4. Study-total N only when the source shows that the effect uses the same
   analysis sample.

If the source does not clearly connect the N to the effect row, leave N missing.

## Multiple-Sample Handling

For studies with multiple samples, countries, waves, groups, or strata, use only
the sample-specific N attached to the reported effect. Do not borrow a study
total or a different subgroup N unless the source states that it is the same
analysis sample.

## Imputation Rule

No statistical imputation is allowed for N. Do not use average N, median N,
nearby-row N, or a generic same-study N as a substitute. A same-table or
same-model carry-forward is allowed only when it is source-supported and the
effect rows demonstrably share the same analysis sample.

## Current Application

The deterministic reconciliation fills numeric `sample_size_numeric` for
741/804 expert-reviewed substitution rows. The remaining 63 rows are excluded
from N-weighted TSSEM/MASEM weighting under the approved rule.

The current bounded core-6 TSSEM diagnostic therefore supports a claim about
the documented N-eligible complete-case subset only. It does not support an
all-construct or all-row SEM stability claim.

## Claim Boundary

Allowed wording:

- The workflow supports source-anchored, denominator-family-scored evaluation
  of LLM extraction behavior.
- The workflow supports targeted human-review triage and bounded downstream
  substitution diagnostics.
- The expert-reviewed LLM-assisted primary input produced no nonzero
  pooled-correlation delta relative to the human-reference baseline in the
  deterministic primary rerun.
- The bounded core-6 TSSEM diagnostic showed identical pooled correlations,
  paths, and fit in the documented N-eligible complete-case subset.

Disallowed wording unless additional conditions are met:

- Do not claim full-corpus `M1-R` accuracy from bounded 90-row source-rendered
  diagnostics.
- Do not claim unsupervised LLM replacement of the human reference standard.
- Do not claim all-construct/all-row SEM stability while 63 rows lack
  source-supported numeric N.

## Conditions for Broader Claims

Full-corpus `M1-R` accuracy requires a full target-denominator locked run,
manifest registration, exception-aware scoring, and denominator-family reporting
across the approved post-freeze target shell.

All-row SEM stability requires source-supported numeric N for all SEM input rows
and an approved full model specification. If the approved missing-N exclusion
rule is used instead, the claim must be worded as N-eligible subset stability,
not all-row stability.
