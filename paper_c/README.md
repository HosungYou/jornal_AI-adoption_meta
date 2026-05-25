# Paper C: Model-by-Procedure LLM Extraction Benchmark

Paper C is a computational evaluation of model-by-procedure behavior in
LLM-assisted structured extraction. It asks how model choice, extraction
procedure, and provenance-preserving harnesses affect source-verifiability,
schema validity, correction recoverability, reproducibility, and accuracy
against the frozen human reference.

## Fixed Direction

- Primary target journal: JMIR Metascience and Research Integrity.
- Corpus: the full 213-study Paper B validation corpus.
- Primary comparison: frozen human reference (`H`) versus versioned
  model-by-procedure conditions.
- Minimum procedure contrast: raw extraction versus the same model mediated by
  LongTable or an equivalent stateful research procedure.
- Minimum model contrast: at least one versioned cross-model contrast if the
  final design has resources to run it consistently.
- Primary claim: model differences may be directly interpretable for extraction
  capability, while the procedure/harness contribution should be framed around
  reproducibility, auditability, source verification, triage utility, correction
  traceability, and error visibility rather than presumed accuracy superiority.
- Product boundary: LongTable is evaluated as a stateful research harness, not
  promoted as a standalone product or general-purpose platform.
- Reproducibility boundary: local and provider execution context is part of the
  experimental condition and must be reported through a run-provenance table.

## Study Logic

Paper B validates whether a prespecified LLM-assisted workflow can support
MASEM-ready extraction and downstream inference stability. Paper C asks a
different computational question: which model/procedure conditions produce
reliable, inspectable, source-verifiable extraction outputs under locked and
reported execution conditions.

The central contrast is:

| Condition | Role |
|---|---|
| `H` | Frozen source-anchored adjudicated human reference standard |
| `M1-R` | Raw extraction by model 1 with full run provenance |
| `M1-P` | Model 1 mediated by a stateful research procedure with source spans, schema checks, uncertainty flags, checkpoints, correction history, and rerun bundles |
| `M2-R` | Raw extraction by model 2 under comparable prompt/schema/source conditions |
| Optional `M2-P` | Model 2 mediated by the same procedure when resources permit |

## Local Structure

| Path | Purpose |
|---|---|
| `RESEARCH_SPECIFICATION.md` | Study identity, research questions, hypotheses, corpus, and contribution |
| `PROTOCOL.md` | Operational workflow and guardrails |
| `ANALYSIS_PLAN.md` | Statistical and diagnostic analysis plan |
| `MEASUREMENT_PLAN.md` | Accuracy, error, auditability, and reproducibility metrics |
| `JOURNAL_STRATEGY.md` | Target-journal positioning and fallback path |
| `LITERATURE_REVIEW.md` | Core reference map |
| `prompts/` | Versioned extraction prompts for raw model and procedure-mediated conditions |
| `schemas/` | Structured extraction and audit-output schemas |
| `templates/` | Corpus manifest, model/procedure comparison, run-provenance, and repeatability templates |
| `scripts/` | Future analysis and validation scripts |

## Data Workspace

Paper C data artifacts live under:

`data/04_extraction/07_paper_c_harness_benchmark/`

Raw PDFs, private logs, model raw outputs, and rerun bundles must not be committed
unless a share-safe derivative has been explicitly prepared.
