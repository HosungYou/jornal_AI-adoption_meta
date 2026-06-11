# Paper2 Expert-Reviewed MASEM Substitution Rerun

Date: 2026-06-11

## Boundary

This rerun is a deterministic model-ready-input and pooled-correlation
sensitivity rerun. The local R environment provides `Rscript`, `OpenMx`,
and `metaSEM`.
The baseline expert-reviewed substitution input has sparse
`sample_size_numeric` coverage before the deterministic sample-size
reconciliation layer. The N-reconciled derived input carries numeric N
for 741/804 rows; the remaining 63 rows
are excluded from N-weighted TSSEM/MASEM weighting under the approved
missing-N rule unless later source checks supply numeric N. The output
therefore supports substitution-input readiness, pooled-correlation
impact claims, and the bounded core-6 TSSEM diagnostic when
interpreted within its documented complete-case scope.

## Inputs

- Baseline: Paper1 primary model-ready tiered freeze input, 804 rows.
- P0/P1 expert-review layer: 1845 task units.
- Expert-reviewed LLM-assisted primary input: 804 rows.
- Baseline rows with `sample_size_numeric` before any later reconciliation layer: 49/804.
- N-reconciled rows with `sample_size_numeric`: 741/804.
- Rows excluded from N-weighted TSSEM/MASEM for missing N: 63.
- Sample-size reconciliation: `PAPER2_MASEM_SAMPLE_SIZE_RECONCILIATION_20260611.md`.
- Bounded core-6 TSSEM diagnostic: `r_tssem_substitution_20260611/PAPER2_TSSEM_SUBSTITUTION_DIAGNOSTIC_20260611.md`.
- Diagnostic scope: PE, EE, SI, FC, BI, UB; 15 complete-case studies; Stage 1/Stage 2 converged; max pooled-r delta 0.00000000.

## Substitution Actions

- llm_exact_numeric_replacement: 3
- retain_human_reference_after_p0_p1_review: 363
- retain_human_reference_after_source_risk_review: 358
- retain_human_reference_after_trace_review: 80
- Numeric rows with nonzero substituted value deltas: 0

## Pair-Level Rerun Comparisons

| Comparison | Max absolute delta in unweighted mean r | Structural edges with nonzero delta |
|---|---:|---:|
| baseline_primary_human_vs_converted_sensitivity_augmented | 0.116229 | 9 |
| baseline_primary_human_vs_expert_reviewed_llm_assisted_primary | 0.000000 | 0 |
| baseline_primary_human_vs_source_risk_excluded_sensitivity | 0.407000 | 9 |

## Interpretation

- The primary expert-reviewed LLM-assisted substitution input has no
  nonzero numeric change relative to the frozen human-reference primary
  input because the only exact Codex numeric candidates already match the
  reference values and P0/P1 high-risk rows are retained rather than
  replaced.
- Source-risk exclusion and converted-input augmentation are sensitivity
  diagnostics, not replacements for the primary source-anchored human
  reference baseline.
- The bounded core-6 complete-case TSSEM diagnostic supports a narrow
  path/fit stability check for PE, EE, SI, FC, BI, and UB only; it is
  not an all-construct or all-row MASEM stability claim.
- Under the approved missing-N rule, broader SEM wording must use
  N-eligible subset language unless later source-supported N
  completion makes every SEM input row eligible.
- A final all-row MASEM stability claim still requires source-supported
  N completion for rows excluded by the sample-size reconciliation
  layer and the approved full model specification.
