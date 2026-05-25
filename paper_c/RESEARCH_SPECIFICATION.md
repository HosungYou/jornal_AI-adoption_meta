# Research Specification: Paper C

## Working Title

From Model Output to Auditable Evidence Coding: A Model-by-Procedure Evaluation
of LLM-Assisted Structured Data Extraction From Scholarly PDFs

## Target Journal

Primary target: JMIR Metascience and Research Integrity.

Secondary targets, if needed: JMIR AI, Information Processing & Management, and
Research Synthesis Methods.

## Research Object

The study evaluates LLM-assisted extraction from complex scholarly PDFs in an
AI-adoption-in-education MASEM project. The object of evaluation is not a simple
model leaderboard and not a harness-only demonstration. The design separates two
questions:

1. Whether model choice materially changes extraction accuracy and error type.
2. Whether a stateful research procedure improves source grounding,
   auditability, error visibility, correction recoverability, and procedural
   reproducibility.

## Corpus

The final corpus is the full 213-study Paper B validation corpus:

- Phase 1 validation Wave 1: 100 studies.
- Phase 2 validation Wave 2: 113 studies.
- Reference condition: the frozen source-anchored adjudicated human reference
  standard.

The Paper C benchmark must not begin final accuracy analyses until the human
reference standard is frozen. Pilot infrastructure can be built earlier using
clearly marked development subsets.

## Conditions

| Code | Condition | Description |
|---|---|---|
| `H` | Human reference | Frozen source-anchored adjudicated human reference standard |
| `M1-R` | Raw model 1 | First prespecified model using the shared extraction schema and prompt, with basic run metadata |
| `M1-P` | Model 1 + stateful procedure | Same model mediated by LongTable or equivalent stateful procedure with source-span requirements, schema validation, uncertainty flags, checkpoint/decision trace, correction history, and rerun bundle |
| `M2-R` | Raw model 2 | Second prespecified model using the same schema and comparable prompt |
| `M2-P` | Model 2 + stateful procedure | Optional if resources permit; used to separate model effects from procedure effects |

The minimum publishable design should include one same-model procedure contrast
and one cross-model raw contrast. A fuller factorial design is preferable if it
can be run consistently.

## Research Questions

**RQ1. Model differences.** How much do versioned LLMs differ in field-level
accuracy and error taxonomy when evaluated against the frozen human reference?

**RQ2. Procedure differences.** Does a stateful research procedure change
accuracy, error visibility, source grounding, correction recoverability, and
schema validity relative to raw model extraction?

**RQ3. Interaction.** Are procedure gains larger for particular models, field
families, or high-risk extraction tasks?

**RQ4. Reproducibility.** Which model/procedure combinations are most
reproducible and auditable without overstating access to hidden model reasoning?

## Core Hypotheses

**H1. Model effects are plausible and reportable.** Model choice will produce
meaningful differences in at least some high-risk field families.

**H2. Procedure effects are strongest for auditability.** The stateful procedure
will most clearly improve source-span coverage, schema validity, correction
traceability, and uncertainty triage. It should not be assumed to produce large
accuracy gains.

**H3. High-risk task interaction.** Procedure effects will be largest for
correlation values, statistic-type classification, construct mapping,
multi-sample separation, and table-type interpretation.

**H4. Better procedural reproducibility.** Stateful procedure conditions will
improve the ability to replay, inspect, and compare extraction runs even when
overall accuracy differences are small.

## Main Contribution

The paper tests whether extraction outcomes are better explained by model choice,
procedure choice, or their interaction. The harness contribution should be framed
as external procedural transparency and verification infrastructure, not as a
standalone accuracy claim or access to hidden model reasoning.

## Boundary From Paper B

Paper B evaluates the MASEM-ready extraction task itself: human disagreement,
field-level error taxonomy, LLM-human validity, and downstream substitution
stability. Paper C evaluates computational model/procedure behavior: model
differences, procedure effects, source-grounding, auditability, reproducibility,
and human adjudication support.
