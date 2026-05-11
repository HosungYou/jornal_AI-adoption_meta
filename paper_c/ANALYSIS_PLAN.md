# Analysis Plan: Paper C

## Primary Analysis Unit

The primary unit is the extracted field nested within study and extraction
family. Study-level summaries are secondary. Some analyses will also use
matrix-level and construct-level units where field-level flattening would lose
important structure.

## Primary Comparisons

| Comparison | Purpose |
|---|---|
| `C` vs `H` | Baseline raw Codex accuracy and error profile |
| `L` vs `H` | LongTable-mediated Codex accuracy and error profile |
| `C` vs `L` | Harness effect on values, source evidence, uncertainty flags, and reproducibility |
| `H-C-L` pattern | Field-level diagnostic classification |

## Agreement Patterns

| Pattern | Interpretation |
|---|---|
| `H = C = L` | Stable/easy field |
| `H = L != C` | Candidate harness-corrected Codex error |
| `H = C != L` | Candidate harness-induced error |
| `C = L != H` | Systematic model error not resolved by harness |
| `H != C != L` | High-ambiguity field requiring source re-review |
| `L` has source span and `C` does not | Verifiability gain independent of value agreement |
| `L` uncertainty flag and `L != H` | Useful triage signal |
| `L` high confidence and `L != H` | Dangerous-confidence error |

## Accuracy Metrics

Categorical fields:

- Exact agreement with the human reference.
- Cohen's kappa or Gwet's AC1/AC2 where appropriate.
- Field-family disagreement rate.

Numeric fields:

- Mean absolute error.
- Root mean squared error.
- Tolerance-band agreement.
- Bland-Altman diagnostics for selected numeric families.

Correlation and matrix fields:

- Absolute error in `r`.
- Tolerance-band agreement for correlations.
- Matrix completeness.
- Matrix symmetry and construct-order diagnostics.
- Wrong-statistic-type rate, such as beta, loading, reliability, or sqrt(AVE)
  mistaken for a correlation.

## Non-Inferiority Framing

Because baseline Codex may already be highly accurate, the primary accuracy
claim should use non-inferiority rather than require large superiority. The
non-inferiority margin must be prespecified before final analysis.

Candidate margin:

- Overall field-level agreement: LongTable is non-inferior if its agreement is
  no more than 2 percentage points lower than raw Codex.
- High-risk field families: use family-specific margins because expected error
  rates differ by field.

## Error Taxonomy

Errors will be coded into the following initial families:

- Unsupported value or missing source evidence.
- Wrong statistic type.
- Table-type misclassification.
- Correlation matrix reconstruction error.
- Multiple-sample contamination.
- Construct mapping drift.
- Moderator coding mismatch.
- Omission error.
- Over-extraction or invented value.
- Schema/format failure.
- Ambiguous source requiring human adjudication.

## Auditability Metrics

| Metric | Definition |
|---|---|
| Source-span coverage | Share of extracted fields with source location/evidence |
| Source-span correctness | Share of source spans judged to support the extracted value |
| Schema validity | Share of outputs passing the extraction schema |
| Correction recoverability | Share of errors whose origin and correction can be traced from artifacts |
| Uncertainty usefulness | Precision/recall of uncertainty flags for fields later found discrepant |
| Adjudication time | Time required for human verification or correction |
| Audit completion rate | Share of fields that a reviewer can fully audit from artifacts |

## Reproducibility Metrics

- Prompt/schema/model-version completeness.
- Rerun bundle completeness.
- Repeated-run value stability.
- Repeated-run source-span stability.
- Difference between output reproducibility and procedural reproducibility.

## Statistical Approach

- Use paired comparisons because `C` and `L` are applied to the same studies and
  fields.
- Use bootstrap confidence intervals clustered by study for field-level metrics.
- Use McNemar-type tests for paired binary outcomes where appropriate.
- Use mixed-effects models for error outcomes if fields are nested within study
  and extraction family.
- Report effect sizes and confidence intervals rather than relying only on
  significance tests.

## Reporting Priorities

The main paper should emphasize:

1. Accuracy preservation or deterioration.
2. High-risk field improvements and failures.
3. Auditability and reproducibility gains.
4. Concrete examples of corrected, exposed, and unresolved errors.
5. Limits of the claim: LongTable improves external procedural transparency, not
   access to hidden model reasoning.
