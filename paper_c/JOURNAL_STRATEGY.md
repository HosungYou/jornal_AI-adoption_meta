# Journal Strategy: Paper C

## Primary Target: JMIR Metascience and Research Integrity

Paper C is primarily a metascience and research-integrity paper. The central
claim is that LLM-assisted evidence coding should be evaluated as a
model-by-procedure condition with explicit run provenance, repeated-run
stability checks, and human-auditable source evidence.

### Fit

- Focuses on research process quality rather than only model performance.
- Addresses AI use in scientific workflows.
- Emphasizes transparency, reproducibility, reporting, and audit trails.
- Avoids presenting LongTable as a product-only contribution.

### Cover-Letter Claim

This manuscript evaluates how model choice and extraction procedure affect
LLM-assisted structured extraction from scholarly PDFs, with emphasis on
source-verifiability, auditability, reproducibility, and the conditions under
which model-performance comparisons are interpretable.

## Secondary Target: JMIR AI

JMIR AI is appropriate if the paper is framed as an applied AI-methods
evaluation. The risk is that the manuscript could be read as a single-product
platform study. To avoid that, the manuscript must present LongTable as one
procedure condition inside a broader model-by-procedure benchmark.

## Technical Fallback: Information Processing & Management

Information Processing & Management is suitable if the paper foregrounds
document extraction, information processing, source-grounded structured output,
and computational benchmark design.

## Evidence-Synthesis Fallback: Research Synthesis Methods

Research Synthesis Methods is suitable if the manuscript is reframed around
evidence synthesis automation. However, if Paper B also targets RSM, Paper C
should avoid duplicating the same methodological claim.

## Submission Positioning

Paper C should avoid:

- Vendor ranking as the main claim.
- LongTable promotion without an ablation design.
- Treating the human reference as perfect ground truth.
- Repeating Paper B's MASEM downstream substitution contribution.
- Treating a single observed model score as independent of prompt, preprocessing,
  runtime, and repeated-run variability.

Paper C should emphasize:

- Same-model procedure comparison.
- Versioned cross-model comparison where resources permit.
- Full 213-study corpus.
- Prespecified schema.
- Field-level `H` versus model/procedure condition comparison.
- Auditability and reproducibility metrics.
- Run-provenance and repeatability tables.
- Share-safe prompts, schemas, and analysis code.
