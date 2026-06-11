# Paper2 Expert-Reviewed MASEM Substitution Rerun

Date: 2026-06-11

## Boundary

This rerun is a deterministic model-ready-input and pooled-correlation
sensitivity rerun. The local R environment now provides `Rscript`, `OpenMx`,
and `metaSEM`, but the current expert-reviewed substitution input has
`sample_size_numeric` for only 49 of 804 rows. The output therefore supports
substitution-input readiness and pooled-correlation impact claims, not final
SEM path-coefficient or model-fit stability claims.

## Inputs

- Baseline: Paper1 primary model-ready tiered freeze input, 804 rows.
- P0/P1 expert-review layer: 1845 task units.
- Expert-reviewed LLM-assisted primary input: 804 rows.
- R/metaSEM readiness: `Rscript` 4.6.0, `OpenMx` 2.22.11, and `metaSEM` 1.5.0
  are available; `sample_size_numeric` is present for 49/804 rows.

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
- A final MASEM stability claim still requires sample-size completion or an
  explicit missing-N exclusion rule before TSSEM/metaSEM Stage 1/Stage 2 is run.
