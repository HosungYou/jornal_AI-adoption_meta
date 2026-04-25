# Phase 2 Rotated-Pair Protocol Amendment

## Decision

Phase 1 pairwise coding is complete. Phase 2 will use a rotated-pair human
coding design rather than the earlier AI-first single-verification plan.

## Pairing

| Phase | Pair | Coders | Role |
|---|---|---|---|
| Phase 1 | Pair A | R1 + R2 | Completed validation Wave 1 pair |
| Phase 1 | Pair B | R3 + R4 | Completed validation Wave 1 pair |
| Phase 2 | Pair C | R1 + R4 | Remaining eligible studies |
| Phase 2 | Pair D | R2 + R3 | Remaining eligible studies |

## Rationale

The rotated-pair design reduces pair-specific bias. Phase 1 established coding
patterns within R1-R2 and R3-R4. Reusing the same pairs in Phase 2 would make it
harder to distinguish true coding-rule stability from pair-specific habits.

This design also better supports the LLM augmentation framing. The human data are
not artificial categories produced by raters; they are reference extraction cells
anchored to source documents. Therefore Phase 2 should first create adjudicated
human reference values and only then compare LLM outputs against them.

## Blinding Rule

Human coders must not access LLM outputs during independent coding or
adjudication. LLM outputs can be opened only after the adjudicated Phase 2 human
reference is frozen.

## Adjudication

| Discrepancy source | Primary adjudicator | Secondary check |
|---|---|---|
| Pair C: R1 vs R4 | R2 | R3 if needed |
| Pair D: R2 vs R3 | R1 | R4 if needed |

## Paper A / Paper B Use

For Paper A, Phase 2 contributes to the final MASEM-ready extraction dataset.

For Paper B, Phase 1 and Phase 2 are used together as the validation corpus.
Phase is handled as a coding wave/time block and reviewer-pair block. LLM
comparison begins only after raw independent human coding, pairwise disagreement
analysis, and source-anchored adjudication are frozen.

Current allocation from the package generator:

| Pair | Coders | Studies | Per-coder change vs Phase 1 |
|---|---|---:|---:|
| Pair C | R1 + R4 | 57 | +7 |
| Pair D | R2 + R3 | 56 | +6 |

## Required Artifacts

- Phase 2 assignment log
- Pair C and Pair D independent coding sheets
- Phase 2 pairwise discrepancy log
- Phase 2 adjudicated human reference file
- Phase 2 LLM comparison file generated only after adjudication
- Updated audit trail showing prompt/model versions, human blinding, and
  adjudication decisions
