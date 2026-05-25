# Analysis Plan: Paper C

## Primary Analysis Unit

The primary unit is the extracted field nested within study and extraction
family. Study-level summaries are secondary. Some analyses will also use
matrix-level and construct-level units where field-level flattening would lose
important structure.

## Primary Comparisons

| Comparison | Purpose |
|---|---|
| `M1-R` vs `H` | Baseline accuracy and error profile for model 1 |
| `M2-R` vs `H` | Baseline accuracy and error profile for model 2 |
| `M1-R` vs `M1-P` | Same-model procedure or harness effect |
| `M2-R` vs `M2-P` | Optional same-model procedure effect for model 2 |
| Raw model contrast | Model-choice effect under comparable raw extraction conditions |
| Procedure contrast | Procedure-choice effect on values, source evidence, uncertainty flags, and reproducibility |
| Model-by-procedure pattern | Field-level diagnostic classification |

## Agreement Patterns

| Pattern | Interpretation |
|---|---|
| `H = M1-R = M2-R` | Stable/easy field across models |
| `H = M1-R != M2-R` | Candidate model-specific error |
| `H = M1-P != M1-R` | Candidate procedure-corrected error |
| `H = M1-R != M1-P` | Candidate procedure-induced error |
| Raw models agree but both differ from `H` | Systematic extraction task error not solved by model choice |
| Procedure output has source span and raw output does not | Verifiability gain independent of value agreement |
| Procedure uncertainty flag and procedure output differs from `H` | Useful triage signal |
| Procedure high confidence and procedure output differs from `H` | Dangerous-confidence error |

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

## Model and Procedure Framing

The model contrast should be interpreted as an empirical extraction-capability
comparison under versioned, reproducible conditions. This is likely the clearest
accuracy comparison for readers.

The procedure or harness contrast should not depend on a large accuracy gain. If
baseline model accuracy is high, the procedure claim should use
non-inferiority for accuracy plus superiority or descriptive improvement for
auditability, source verification, correction traceability, and reproducibility.
The non-inferiority margin must be prespecified before final analysis.

Candidate margin:

- Overall field-level agreement: LongTable is non-inferior if its agreement is
  no more than 2 percentage points lower than the corresponding raw model.
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
- Run-provenance completeness.
- Rerun bundle completeness.
- Repeated-run value stability.
- Repeated-run source-span stability.
- Repeated-run rank stability when comparing models.
- Difference between output reproducibility and procedural reproducibility.

## Execution Variability and Local Environment

Paper C should not treat a model score as a timeless property of the model. The
claim should be framed as model-by-procedure performance under a locked
extraction condition.

For API-served models, the local machine usually does not run inference, but it
can still affect PDF rendering, OCR/text extraction, chunking, prompt
serialization, wrapper behavior, schema parsing, and retry logic. The provider
backend, model snapshot, batching, hidden runtime changes, and exposed settings
can also affect outputs even when the local code is unchanged.

For local or self-hosted models, the local environment is a direct part of the
experimental condition. Hardware, runtime, quantization, GPU kernels, decoding
implementation, seeds, package versions, and model weights must be recorded and,
where possible, locked.

Recommended design:

1. Use a locked single full-corpus run per model-by-procedure condition for the
   main 213-study comparison if cost or time makes full replication infeasible.
2. Add repeated runs on a stratified stability subset, prioritizing high-risk
   fields and studies with human-human disagreement.
3. Report within-condition variability alongside accuracy. Model differences
   should not be interpreted as meaningful when they are smaller than run-to-run
   variability.
4. Include a run-provenance table and a repeatability table in the main paper or
   supplement.

## Statistical Approach

- Use paired comparisons because model/procedure conditions are applied to the
  same studies and fields.
- Use bootstrap confidence intervals clustered by study for field-level metrics.
- Use McNemar-type tests for paired binary outcomes where appropriate.
- Use mixed-effects models for error outcomes if fields are nested within study
  and extraction family.
- For repeated runs, estimate within-condition variability before interpreting
  between-model or between-procedure contrasts.
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
