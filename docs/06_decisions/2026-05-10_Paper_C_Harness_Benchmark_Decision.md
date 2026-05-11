# Decision: Paper C Harness Benchmark Direction

Date: 2026-05-10

## Decision

Paper C will be developed as a computational evaluation of whether a stateful
research harness improves the reproducibility, auditability, source
verification, triage utility, and correction traceability of LLM-assisted
structured extraction from complex scholarly PDFs.

## Fixed Commitments

1. Primary target journal: JMIR Metascience and Research Integrity.
2. Corpus: the full 213-study Paper B validation corpus.
3. Comparison design: frozen human reference (`H`) versus raw Codex (`C`) versus
   Codex + LongTable harness (`L`).
4. LongTable condition minimum artifact set:
   - Source span.
   - Schema validation.
   - Uncertainty flag.
   - Correction log.
   - Rerun bundle.
   - Checkpoint/decision trace.
5. Git policy: do not commit raw `.longtable/` runtime state. Commit curated
   research specifications, protocols, schemas, prompts, templates, aggregate
   outputs, and redacted audit artifacts.

## Rationale

Baseline Codex extraction may already have high apparent accuracy. Therefore,
Paper C should not depend on a large accuracy gain. The stronger contribution is
to evaluate whether a stateful harness turns extraction into a verifiable,
auditable, and reproducible research procedure.

## Boundary From Paper B

Paper B remains the validation study for MASEM-ready extraction and downstream
substitution stability. Paper C uses the same corpus but asks a different
computational question: whether the extraction procedure itself becomes more
inspectable and reproducible under a stateful harness.

## Next Actions

1. Freeze the source-anchored adjudicated human reference standard.
2. Populate the 213-study Paper C corpus manifest.
3. Finalize raw Codex and LongTable prompt versions.
4. Validate the extraction schema.
5. Run a development pilot before final full-corpus extraction.
6. Run full `H-C-L` comparison only after the human reference freeze.
