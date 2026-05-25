# Protocol: Paper C Model-by-Procedure Benchmark

## Prerequisite

Final Paper C analyses require a frozen source-anchored adjudicated human
reference standard in `data/04_extraction/04_reference_standard_freeze/`.

Until that freeze exists, work in Paper C is limited to protocol development,
schema validation, prompt drafting, and clearly labeled pilot runs.

## Workflow Overview

1. Create the 213-study corpus manifest.
2. Link each study to the frozen human reference record.
3. Select versioned model conditions and lock comparable prompts/settings.
4. Run raw extraction conditions with the prespecified prompt and schema.
5. Run stateful procedure or harness conditions with the same extraction schema
   plus procedure artifacts.
6. Validate all outputs against the schema.
7. Build a model-by-procedure comparison table against `H`.
8. Classify agreement patterns and error types.
9. Score auditability, reproducibility, and correction recoverability.
10. Prepare a share-safe analysis package.

## Condition Requirements

### Raw Model Condition

Each raw model condition is a baseline. It must preserve enough metadata for a fair
comparison:

- PDF or source document identifier.
- Prompt version.
- Extraction schema version.
- Model identifier and access date.
- Interface or API route.
- Runtime settings if exposed.
- Output JSON or table.
- Parse/schema validation result.

### Stateful Procedure or Harness Condition

The stateful procedure condition must include all raw model requirements plus:

- Source spans for extracted values where applicable.
- Field-level uncertainty flags.
- Schema validation report.
- Checkpoint or decision trace for research-relevant ambiguities.
- Correction history.
- Rerun bundle or replay manifest.
- Link between each corrected value and the source/correction reason.

## Extraction Families

The benchmark covers the same MASEM-relevant extraction families used in Paper B:

- Bibliographic metadata.
- Sample characteristics.
- Construct harmonization.
- Measurement details.
- Correlation/statistic extraction.
- Matrix reconstruction.
- Moderator coding.

## Blinding and Leakage Guardrail

The human reference must be frozen before final Codex or LongTable comparison
analyses are interpreted. LLM outputs must not be used to modify the frozen
human reference except through an explicitly documented post-freeze correction
process.

## Paper B Non-Overlap Rule

Paper C may reuse the same 213-study corpus but must not duplicate Paper B's
main inferential claim about MASEM downstream substitution stability. Paper C's
main outcomes are computational and procedural: model differences, procedure
effects, error visibility, auditability, source verification, and
reproducibility.

## Share-Safe Artifacts

Commit only share-safe derivatives:

- Corpus manifest without private PDF links.
- Prompt and schema versions.
- Aggregated comparison outputs.
- Redacted audit reports.
- Analysis scripts.
- Journal-facing documentation.

Do not commit raw PDFs, private human workbooks, local model transcripts,
private LongTable state, or full rerun bundles unless a share-safe release
artifact has been explicitly approved.
