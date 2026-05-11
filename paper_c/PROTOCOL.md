# Protocol: Paper C Harness Benchmark

## Prerequisite

Final Paper C analyses require a frozen source-anchored adjudicated human
reference standard in `data/04_extraction/04_reference_standard_freeze/`.

Until that freeze exists, work in Paper C is limited to protocol development,
schema validation, prompt drafting, and clearly labeled pilot runs.

## Workflow Overview

1. Create the 213-study corpus manifest.
2. Link each study to the frozen human reference record.
3. Run raw Codex extraction (`C`) with the prespecified prompt and schema.
4. Run Codex + LongTable extraction (`L`) with the same extraction schema plus
   harness artifacts.
5. Validate both outputs against the schema.
6. Build a three-way `H-C-L` comparison table.
7. Classify agreement patterns and error types.
8. Score auditability, reproducibility, and correction recoverability.
9. Prepare a share-safe analysis package.

## Condition Requirements

### Raw Codex (`C`)

Raw Codex is the baseline. It must preserve enough metadata for a fair
comparison:

- PDF or source document identifier.
- Prompt version.
- Extraction schema version.
- Model identifier and access date.
- Runtime settings if exposed.
- Output JSON or table.
- Parse/schema validation result.

### Codex + LongTable (`L`)

The LongTable condition must include all raw Codex requirements plus:

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
main outcomes are computational and procedural: accuracy preservation, error
visibility, auditability, source verification, and reproducibility.

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
