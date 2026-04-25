# Phase 1+2 Reference Standard and Disagreement Analysis Protocol

## Decision

Phase 1 and Phase 2 are treated as two coding waves in one Paper B validation
corpus, not as primary versus optional validation tiers.

The Paper B analysis sequence is:

1. Freeze raw independent human coder data.
2. Analyze pre-adjudication human-human disagreement.
3. Resolve discrepancies against the source documents.
4. Freeze the source-anchored adjudicated human reference standard.
5. Compare LLM outputs and run MASEM substitution analyses against that frozen reference.

## Why Raw Disagreement Comes First

MASEM extraction is not a conventional rating task. Many cells are evidence
recovery values: sample size, correlation coefficient, beta coefficient, source
table, construct label, and exclusion rationale. Human coders should not be
forced into artificial psychological categories when the underlying task is to
recover source-document evidence.

Pre-adjudication human-human disagreement is still analytically important
because it shows which fields are difficult even before LLMs enter the workflow.
The raw disagreement analysis should report:

- Pair-level disagreement rates for Phase 1 and Phase 2.
- Field-family difficulty: bibliographic, sample, construct mapping,
  measurement, correlation, moderator, and exclusion decisions.
- Numeric disagreement magnitude for r, beta, N, reliability, and derived values.
- Construct-mapping disagreements and their rule-based resolutions.
- Phase block effects, because Phase 1 and Phase 2 occur at different times and
  use different reviewer pairings.

## Why Adjudication Is Still Required

LLM accuracy and downstream MASEM substitution cannot be evaluated against raw
unresolved coder disagreements. They require a source-anchored adjudicated human
reference standard: a reconciled value justified by the source document, coding
manual, and logged adjudication rationale.

Use this wording in current documents:

- Use: `source-anchored adjudicated human reference standard`
- Use: `adjudicated human reference`
- Avoid: `gold standard`, unless describing older superseded protocol language

The reference standard is not claimed to be infallible. It is the best available
expert interpretation of the source documents after independent coding and
documented discrepancy resolution.

## Dataset States

| State | Description | Use |
|---|---|---|
| `raw_human_coder_data` | Independent coder values before unblinding and adjudication | Human disagreement and field difficulty |
| `pairwise_diff_data` | Computed differences between paired coders | Discrepancy queue and disagreement analysis |
| `adjudicated_human_reference` | Source-anchored resolved values | LLM evaluation and Paper A MASEM input |
| `llm_outputs` | Prespecified workflow outputs, blinded until adjudication freeze | Post-adjudication comparison only |
| `llm_assisted_analysis_input` | Human-supervised LLM-derived or LLM-flagged extraction input | Downstream substitution analysis |

## Current Workload and Counts

The current package generator uses the local PDF-backed source of truth.

| Item | Count |
|---|---:|
| Studies with PDFs in current coding source | 223 |
| Phase 0 calibration studies | 10 |
| Phase 1 validation corpus | 100 |
| Phase 2 validation corpus | 113 |
| Combined Paper B validation corpus | 213 |

Phase 2 pair allocation:

| Pair | Coders | Phase 2 studies | Per-coder change relative to Phase 1 |
|---|---|---:|---:|
| Pair C | R1 + R4 | 57 | +7 studies each |
| Pair D | R2 + R3 | 56 | +6 studies each |

Calibration studies remain a training/calibration block. They are not counted
as part of the 213-study Paper B validation corpus unless explicitly reported as
a separate calibration dataset.

## GitHub and Local Structure

GitHub should track protocols, templates, scripts, codebooks, comparison
workbooks, and share-safe summaries. It should not track machine-specific PDFs,
raw local coder workbooks, API keys, temporary Excel lock files, or private raw
LLM outputs that cannot be shared.

Recommended local structure:

```
data/04_extraction/
├── phase1/                 # Phase 1 raw, diff, and adjudication guide
├── phase2/                 # Phase 2 assignment, raw, diff, and adjudication guide
├── reference/              # Frozen adjudicated reference documentation
├── qa/                     # QA gates and spot-check records
└── consensus/              # Share-safe comparison workbooks and notes
```

The final analysis should preserve both raw disagreement and adjudicated
reference states. Do not overwrite raw coder values during consensus work.
