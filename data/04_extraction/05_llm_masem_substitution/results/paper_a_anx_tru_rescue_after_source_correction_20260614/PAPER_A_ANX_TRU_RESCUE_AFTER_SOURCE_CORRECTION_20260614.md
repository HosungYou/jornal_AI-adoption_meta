# Paper A ANX-TRU Rescue After S004/S048 Source Correction

Date: 2026-06-14

## Bottom line

- `ANX-TRU` was not absent from the source corpus: source/frozen rows exist for `S036`, `S066`, and `S102`.
- For the active primary direct/latent-correlation route, only `S036` and `S102` are diagnostic-add candidates.
- `S066` remains sensitivity-only because the frozen value is beta/path converted.
- `S142` is excluded from this rescue because the source constructs do not support an approved `ANX-TRU` target mapping.
- Adding `S036` and `S102` restores full10 pair coverage from 44/45 to 45/45, but it does not create any full10 complete-case study.

## Candidate decisions

| study | value | decision | rationale |
| --- | ---: | --- | --- |
| S036 | -0.260 | source_confirmed_add_candidate_for_diagnostic_primary | Human/frozen row exists and PDF table confirms a same-matrix numeric ANX-TRU cell. No beta/path conversion. |
| S102 | 0.027 | source_confirmed_add_candidate_for_diagnostic_primary_with_mapping_caveat | Frozen reference accepted technostress->ANX with caveat; PDF confirms same-matrix numeric TS-T value. |
| S066 | 0.19 in frozen reference; PDF-visible Table 7 path PT->TANX = 0.140 | exclude_source_type_mismatch_for_primary | Frozen row is beta/path converted with retained caveat; active primary route should not use path conversion as direct correlation. |
| S142 |  | exclude_ai_false_positive_target_construct_mismatch | Prejudice toward AI and teaching concerns are not approved ANX-TRU target construct mapping for this rescue. |

## Coverage consequence

- Before rescue: observed full10 pairs `44/45`; missing `ANX-TRU`.
- After diagnostic rescue: observed full10 pairs `45/45`; missing `none`.
- Full10 complete-case studies after rescue: `0`.

## Highest-coverage studies after diagnostic rescue

| study | observed pairs | missing pairs | has ANX-TRU |
| --- | ---: | ---: | --- |
| S048 | 28 | 17 | False |
| S176 | 28 | 17 | False |
| S004 | 21 | 24 | False |
| S016 | 21 | 24 | False |
| S025 | 21 | 24 | False |
| S055 | 21 | 24 | False |
| S121 | 21 | 24 | False |
| S121-1 | 21 | 24 | False |
| S121-2 | 21 | 24 | False |
| S157 | 21 | 24 | False |

## Interpretation

The immediate `ANX-TRU` issue is a pipeline/input-boundary problem, not a PDF-access problem. The pair exists in the frozen full-corpus reference and is PDF-visible for `S036` and `S102`, but those rows were not present in the current Paper A source-corrected input.

This rescue alone is not enough for the primary full 10-construct MASEM route. It closes pair-level coverage, but full10 still has zero complete-case studies and the prior sparse partial-matrix TSSEM route failed with non-positive-definite implied covariance. The next defensible work is therefore to densify same-study matrices for high-coverage studies or to define a defensible missing-data TSSEM/MASEM strategy before manuscript-level full10 claims.

## Artifact status

- This is a diagnostic/review packet only.
- It does not mutate raw coder workbooks.
- It does not mutate the frozen reference standard.
- It does not constitute final Paper A row promotion until the researcher explicitly approves the promotion.
