# Research Specification: Paper C

## Working Title

From LLM Extraction to Auditable Evidence Coding: A Comparative Evaluation of
Raw Codex and a Stateful Research Harness for Structured Data Extraction From
Scholarly PDFs

## Target Journal

Primary target: JMIR Metascience and Research Integrity.

Secondary targets, if needed: JMIR AI, Information Processing & Management, and
Research Synthesis Methods.

## Research Object

The study evaluates a reproducible LLM-assisted extraction procedure for complex
scholarly PDFs in an AI-adoption-in-education MASEM project. The object of
evaluation is not a model leaderboard. It is the effect of a stateful research
harness on extraction accuracy, error visibility, source grounding,
auditability, and correction recoverability.

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
| `C` | Raw Codex | Codex extraction using the prespecified schema and prompt, with basic run metadata |
| `L` | Codex + LongTable | Same Codex model mediated by LongTable state, source-span requirements, schema validation, uncertainty flags, checkpoint/decision trace, correction history, and rerun bundle |

The intended comparison is same-model, different-harness. Any cross-model
comparison is supplementary only.

## Research Questions

**RQ1. Accuracy preservation.** Does Codex with LongTable preserve extraction
accuracy relative to raw Codex when both are evaluated against the frozen human
reference?

**RQ2. Error reduction and error visibility.** Which field families and error
types are reduced, exposed, or left unchanged by the LongTable harness?

**RQ3. Verifiability and auditability.** Does the LongTable harness improve
source-span coverage, source-span correctness, schema validity, correction
recoverability, uncertainty-flag usefulness, and human adjudication efficiency?

**RQ4. Reproducibility.** Does the LongTable harness improve procedural
reproducibility and repeated-run stability without overstating access to the
model's internal reasoning?

## Core Hypotheses

**H1. Non-inferior accuracy.** Codex + LongTable will be non-inferior to raw
Codex in field-level agreement with the human reference.

**H2. High-risk field gains.** LongTable will improve or better triage high-risk
fields, including correlation values, statistic-type classification, construct
mapping, multi-sample separation, and table-type interpretation.

**H3. Stronger auditability.** LongTable will substantially improve the share of
extractions with verifiable source spans, valid schemas, traceable corrections,
and reusable rerun metadata.

**H4. Better procedural reproducibility.** LongTable will improve the ability to
replay, inspect, and compare extraction runs even if overall accuracy changes are
small because baseline Codex accuracy is already high.

## Main Contribution

The paper tests whether a stateful, provenance-preserving research harness turns
LLM-assisted extraction from a black-box output into an auditable evidence-coding
procedure. The claim is external procedural transparency, not access to hidden
model reasoning.

## Boundary From Paper B

Paper B evaluates a prespecified LLM-assisted workflow for MASEM-ready
extraction and downstream substitution stability. Paper C evaluates the
computational harness itself: accuracy preservation, error typology,
source-grounding, auditability, reproducibility, and human adjudication support.
