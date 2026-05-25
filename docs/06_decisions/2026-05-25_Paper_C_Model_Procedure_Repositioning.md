# Decision: Paper C Model-by-Procedure Repositioning

Date: 2026-05-25

## Decision

Paper C should be repositioned from a harness-only benchmark to a
model-by-procedure benchmark.

The rationale is that model differences may be more directly meaningful for
field-level extraction capability, while the LongTable or stateful harness
contribution is strongest as auditability and reproducibility infrastructure.
The harness should not be assumed to produce a large accuracy gain. It should be
tested for accuracy preservation or improvement, but its primary value is
source-grounding, error visibility, correction traceability, rerun completeness,
and human adjudication support.

## Updated Empirical Object

The empirical object is not:

- A model leaderboard alone.
- A product demonstration of LongTable.
- A claim that a harness exposes hidden model reasoning.

The empirical object is:

- Model choice under a fixed extraction schema.
- Procedure choice under the same or comparable model.
- Model-by-procedure interaction for high-risk extraction families.

## Minimum Design

| Dimension | Minimum requirement |
|---|---|
| Human reference | Frozen source-anchored adjudicated human reference standard |
| Model contrast | At least two versioned raw model conditions using comparable prompts/settings |
| Procedure contrast | At least one same-model raw-vs-stateful procedure comparison |
| Outcome families | Accuracy, error taxonomy, source verification, auditability, correction recoverability, reproducibility |
| Boundary | No final analysis before the human reference freeze |

## Revised Paper C Claim

Paper C asks whether extraction quality and inspectability are better explained
by model choice, procedure choice, or their interaction. It can report model
accuracy differences when present, but it should preserve the harness
contribution as a verifiable research-process claim.

This makes Paper C more defensible because a small or null harness accuracy
effect would not collapse the manuscript. A null or small accuracy effect can
still coexist with meaningful gains in source-span coverage, schema validity,
correction traceability, and rerun completeness.

## Boundary From Paper B

Paper B remains the task-and-methods paper: human disagreement, task-contingent
field taxonomy, LLM-human validity, and downstream MASEM substitution stability.

Paper C becomes the computational evaluation paper: model differences,
procedure effects, model-by-procedure interaction, and auditability outcomes.
