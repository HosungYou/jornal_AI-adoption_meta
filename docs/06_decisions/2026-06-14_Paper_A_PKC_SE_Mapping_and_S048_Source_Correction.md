# Paper A PKC-SE mapping and S048 source-correction decision

Date: 2026-06-14

## Decision

For Paper A source densification, `PKC` in S004 is not approved as
`SE`/self-efficacy.

The S004 source table may contain numeric cells involving `PKC`, but those cells
must not enter the Paper A `SE` matrix unless a later source-adjudication
decision explicitly reopens and approves that construct mapping.

S048 Table 2 is accepted as a Pearson correlation matrix for the target
constructs. `INT` is treated as `BI`, and `USE` is treated as `UB`.

## Consequences

- Exclude S004 priority candidates that require `PKC -> SE`.
- Reopen or remove existing S004 `SE` rows that depend on `PKC`.
- Correct source-visible approved S004 rows where the source table and existing
  frozen value disagree.
- Treat S048 as a source-correction item rather than a simple AI-candidate
  append.
- Keep S072 excluded unless its construct mapping is explicitly reopened.

## Evidence boundary

This decision documents a source-adjudication rule. It does not itself modify
the frozen reference standard or analytic workbook. Corrected analytic inputs
must be generated as separate proposal artifacts until the researcher approves
promotion into a canonical input.

## Next execution step

Generate a Paper A corrected source-input proposal for S004/S048, then rerun
coverage and MASEM feasibility using that proposal as a diagnostic input.
