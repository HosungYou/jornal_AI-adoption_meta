# Project Agent Instructions

These instructions apply to the entire repository.

## LongTable Workspace Contract

This repository can also operate as a LongTable research workspace.

- Read `CURRENT.md` or `.longtable/current-session.json` before giving
  substantial project-specific research guidance when those files are present.
- Treat `.longtable/` as local runtime state, not as the primary
  researcher-facing publication artifact.
- Preserve open tensions and researcher decisions; do not collapse Paper B,
  Paper C, or Paper A into a single manuscript claim.
- For factual, current, or external claims, provide source links or file
  references when possible. Label unsupported claims as inference or estimate.

## Required Orientation For Paper B

Before changing Paper B extraction, coding, adjudication, LLM comparison, or
MASEM substitution materials, read:

1. `data/04_extraction/README.md`
2. `data/04_extraction/WORKFLOW_STATUS_LOG.md`
3. `docs/06_decisions/2026-04-25_Reference_Standard_and_Disagreement_Analysis.md`
4. `data/04_extraction/02_pre_adjudication_disagreement/RATER_COMPARISON_PLAYBOOK.md`

## Current Paper B Workflow Rule

Maintain this order:

1. Raw human coder data freeze
2. Pre-adjudication human-human disagreement analysis
3. Source-document adjudication
4. Source-anchored adjudicated human reference standard freeze
5. LLM comparison + MASEM substitution analysis

Do not run or document LLM accuracy analysis as current unless the relevant
human reference file has been frozen in `data/04_extraction/04_reference_standard_freeze/`.

## Paper C Harness Benchmark Rule

Paper C lives in `paper_c/` and
`data/04_extraction/07_paper_c_harness_benchmark/`.

The fixed Paper C design is:

- Primary target: JMIR Metascience and Research Integrity.
- Corpus: full 213-study Paper B validation corpus.
- Primary comparison: frozen human reference (`H`) versus raw Codex (`C`) versus
  Codex with LongTable harness (`L`).
- Primary claim: accuracy preservation plus improved reproducibility,
  auditability, source verification, triage utility, and correction
  traceability.
- Main boundary: Paper C evaluates the harness and procedure; Paper B evaluates
  MASEM-ready extraction validity and downstream substitution stability.

Do not start final Paper C accuracy analyses until the frozen human reference
standard exists. Pilot infrastructure and schema/prompt development are allowed
before the freeze when clearly labeled as pilot or scaffold work.

## Terminology

Use `source-anchored adjudicated human reference standard` for the current
protocol. Avoid `gold standard` except when quoting or preserving historical
decision logs.

For Paper C, describe LongTable as a stateful research harness or
provenance-preserving research procedure. Avoid product-promotion language.

## Data Safety

- Preserve raw coder workbooks; do not overwrite them during adjudication.
- Keep local PDFs, Excel lock files, private raw coder files, private LongTable
  state, raw model transcripts, and raw LLM outputs out of Git unless the team
  explicitly approves a share-safe release artifact.
- Do not add PDF hyperlinks to shareable comparison workbooks.
- If Paper B workflow status changes, update
  `data/04_extraction/WORKFLOW_STATUS_LOG.md` in the same commit.
- For Paper C, commit share-safe manifests, schemas, prompts, aggregate
  comparison tables, redacted audit summaries, and analysis scripts only.
