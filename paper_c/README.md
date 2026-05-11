# Paper C: Reproducible LLM Extraction Harness

Paper C is a computational evaluation of whether a stateful research harness
changes LLM-assisted structured extraction from a one-shot output into a
source-verifiable, schema-validatable, correction-recoverable research
procedure.

## Fixed Direction

- Primary target journal: JMIR Metascience and Research Integrity.
- Corpus: the full 213-study Paper B validation corpus.
- Primary comparison: frozen human reference (`H`) versus raw Codex (`C`) versus
  Codex with LongTable harness (`L`).
- Primary claim: LongTable does not need to substantially increase already-high
  Codex accuracy. It should preserve accuracy while improving reproducibility,
  auditability, source verification, triage utility, and correction traceability.
- Product boundary: LongTable is evaluated as a stateful research harness, not
  promoted as a standalone product or general-purpose platform.

## Study Logic

Paper B validates whether a prespecified LLM-assisted workflow can support
MASEM-ready extraction and downstream inference stability. Paper C asks a
different computational question: whether the same-model extraction process
becomes more inspectable and reproducible when mediated by a stateful harness.

The central contrast is:

| Condition | Role |
|---|---|
| `H` | Frozen source-anchored adjudicated human reference standard |
| `C` | Raw Codex extraction with minimal required run metadata |
| `L` | Codex extraction mediated by LongTable state, source spans, schema checks, uncertainty flags, checkpoints, correction history, and rerun bundles |

## Local Structure

| Path | Purpose |
|---|---|
| `RESEARCH_SPECIFICATION.md` | Study identity, research questions, hypotheses, corpus, and contribution |
| `PROTOCOL.md` | Operational workflow and guardrails |
| `ANALYSIS_PLAN.md` | Statistical and diagnostic analysis plan |
| `MEASUREMENT_PLAN.md` | Accuracy, error, auditability, and reproducibility metrics |
| `JOURNAL_STRATEGY.md` | Target-journal positioning and fallback path |
| `LITERATURE_REVIEW.md` | Core reference map |
| `prompts/` | Versioned extraction prompts for raw Codex and LongTable conditions |
| `schemas/` | Structured extraction and audit-output schemas |
| `templates/` | Corpus manifest and comparison table templates |
| `scripts/` | Future analysis and validation scripts |

## Data Workspace

Paper C data artifacts live under:

`data/04_extraction/07_paper_c_harness_benchmark/`

Raw PDFs, private logs, model raw outputs, and rerun bundles must not be committed
unless a share-safe derivative has been explicitly prepared.
