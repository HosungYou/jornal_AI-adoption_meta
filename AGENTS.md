# Project Agent Instructions

These instructions apply to the entire repository.

## Required Orientation

Before changing Paper B extraction, coding, adjudication, LLM comparison, or
MASEM substitution materials, read:

1. `data/04_extraction/README.md`
2. `data/04_extraction/WORKFLOW_STATUS_LOG.md`
3. `docs/06_decisions/2026-04-25_Reference_Standard_and_Disagreement_Analysis.md`

## Current Workflow Rule

Maintain this order:

1. Raw human coder data freeze
2. Pre-adjudication human-human disagreement analysis
3. Source-document adjudication
4. Source-anchored adjudicated human reference standard freeze
5. LLM comparison + MASEM substitution analysis

Do not run or document LLM accuracy analysis as current unless the relevant
human reference file has been frozen in `data/04_extraction/04_reference_standard_freeze/`.

## Terminology

Use `source-anchored adjudicated human reference standard` for the current
protocol. Avoid `gold standard` except when quoting or preserving historical
decision logs.

## Data Safety

- Preserve raw coder workbooks; do not overwrite them during adjudication.
- Keep local PDFs, Excel lock files, private raw coder files, and raw LLM outputs
  out of Git unless the team explicitly approves a share-safe release artifact.
- Do not add PDF hyperlinks to shareable comparison workbooks.
- If workflow status changes, update `data/04_extraction/WORKFLOW_STATUS_LOG.md`
  in the same commit.
