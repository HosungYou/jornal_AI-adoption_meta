# Measurement Plan: Paper C

## Outcome Families

Paper C separates four outcome families:

1. Extraction accuracy.
2. Model-difference profile.
3. Error type and error visibility.
4. Verifiability, auditability, and reproducibility.

## Accuracy Outcomes

| Field family | Primary metric | Notes |
|---|---|---|
| Bibliographic metadata | Exact agreement | DOI/title/year/journal |
| Sample characteristics | Exact or tolerance agreement | `N`, country, education level, user group |
| Construct harmonization | Agreement and discrepancy typology | Include confidence and ambiguity flags |
| Measurement details | Exact/tolerance agreement | Reliability, scale source, instrument |
| Correlation/statistic values | Absolute error and tolerance agreement | Correlation tolerance should be prespecified |
| Matrix reconstruction | Completeness and structural diagnostics | Symmetry, construct order, missing cells |
| Moderator coding | Exact agreement and error typology | Tool type, role, setting, design |

## Model-Difference Outcomes

| Outcome | Operationalization |
|---|---|
| Cross-model agreement | Share of fields where raw model conditions return the same value |
| Model-specific error | Field is correct for one model and incorrect for another |
| Model-specific omission | Source value exists but is omitted by one model condition |
| Model-specific over-extraction | Unsupported value appears in one model condition only |
| High-risk family sensitivity | Model differences within construct mapping, statistic-type classification, and correlation recovery |

## Procedure-Specific Outcomes

| Outcome | Operationalization |
|---|---|
| Source-span coverage | Count of fields with page/table/section/span evidence divided by eligible fields |
| Source-span correctness | Independent reviewer judgment that the span supports the value |
| Unsupported-value rate | Extracted values without adequate source evidence |
| Schema validity | JSON/schema pass rate and required-field completeness |
| Correction recoverability | Whether the error source and correction rationale can be reconstructed |
| Uncertainty usefulness | Whether uncertainty flags predict procedure-output disagreement with `H` or source ambiguity |
| Rerun completeness | Whether prompt, schema, model, date, source, and settings are sufficient to rerun |
| Run-to-run stability | Agreement between repeated runs under the same condition |
| Source-span stability | Whether repeated runs cite the same supporting page/table/span for the same value |
| Rank stability | Whether model rankings remain the same across repeat runs or bootstrap samples |
| Invalid-output stability | Whether schema or formatting failure rates change across repeat runs |
| Adjudication efficiency | Time or steps required for a human reviewer to verify or correct an extraction |

## Error Types To Code

- Unsupported value.
- Missing value despite source availability.
- Wrong statistic type.
- Wrong table type.
- Wrong construct mapping.
- Mixed sample or wrong sample.
- Wrong moderator category.
- Matrix reconstruction failure.
- Schema failure.
- Overconfident incorrect value.
- Flagged uncertainty that correctly predicted a problem.

## Minimum Stateful Procedure Artifact Set

Each stateful procedure or harness condition must produce:

- Source span or source-location field.
- Prompt version.
- Schema version.
- Model identifier and access date.
- Field-level extraction decision.
- Field-level uncertainty flag.
- Schema validation result.
- Correction history.
- Checkpoint or decision trace for ambiguous research choices.
- Rerun manifest.

## Minimum Run-Provenance Artifact Set

Each raw model and procedure condition must preserve:

- Source PDF identifier and hash.
- Preprocessing/OCR/text-extraction version.
- Chunking and input-window policy.
- Exact prompt payload or prompt serialization hash.
- Prompt, schema, and parser versions.
- Model provider, model identifier, endpoint, and snapshot/version when exposed.
- Run timestamp and timezone.
- Decoding/runtime settings, including temperature, top-p, max tokens,
  reasoning/thinking effort, seed if exposed, and retry policy.
- Client package/runtime version.
- Local hardware, operating system, model weights/release hash, quantization,
  and inference runtime for locally hosted models.

## Interpretation Rule

Accuracy and verifiability are interpreted separately. A condition can preserve
accuracy while improving auditability, or it can be accurate but insufficiently
auditable. The paper should not treat opaque correct answers as equivalent to
source-verifiable correct answers.

When repeated-run variability is measured, model or procedure superiority should
not be claimed from a difference that is smaller than within-condition
run-to-run variation.
