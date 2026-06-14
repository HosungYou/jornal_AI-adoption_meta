# Paper A source correction and MASEM status

Date: 2026-06-14

## Decision encoded

- `PKC -> SE` is rejected for S004.
- S004 PKC-derived `SE` candidates are excluded.
- S048 Table 2 is accepted as Pearson correlation evidence.
- S048 `INT -> BI` and `USE -> UB` are accepted.
- S072 remains excluded because the required construct remaps were already
  rejected in the frozen reference notes.

## Corrected diagnostic input

- Corrected diagnostic input rows: 832.
- S004/S048 change-log rows: 56.
- This is a diagnostic proposal input, not a frozen-reference edit and not a
  workbook overwrite.

## Coverage effect

| Route | Required pairs | Observed pairs | Missing pairs | Numeric studies | Complete-case studies | Complete-case IDs |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| full10 theory target | 45 | 44 | 1: `ANX-TRU` | 75 | 0 | none |
| trust6 mechanism | 15 | 15 | 0 | 73 | 7 | S004; S048; S121; S121-1; S121-2; S173; S176 |
| core7 ATT mediation | 21 | 21 | 0 | 72 | 4 | S048; S055; S176; S214 |

## TSSEM/MASEM execution

### Sparse partial-matrix route

The partial-matrix TSSEM attempt failed for all three routes with the same
non-positive definite implied covariance problem seen before. This remains a
methodological blocker for claiming a sparse full10 TSSEM result from the
current partial-matrix input.

### Complete-case route

| Route | Stage 1 | Stage 2 | Fit summary | Claim boundary |
| --- | --- | --- | --- | --- |
| trust6 mechanism | converged, REM | converged | CFI = 0.996; TLI = 0.985; RMSEA = 0.011; SRMR = 0.040 | Reduced diagnostic/sensitivity route only |
| core7 ATT mediation | converged, REM | converged | CFI = 0.999; TLI = 0.996; RMSEA = 0.009; SRMR = 0.043 | Reduced diagnostic/sensitivity route only |
| full10 theory target | not run | not run | zero complete-case studies | Primary route not estimable yet |

## Main interpretation

S048 source correction materially improves reduced-route feasibility by adding
S048 as a complete-case study for trust6 and core7. It does not solve the full10
primary route. The full10 pair universe remains short by `ANX-TRU`, and no study
currently has a complete 10-construct matrix.

The defensible manuscript posture is:

- Keep full10 as the theory target and source-densification goal.
- Do not report full10 structural paths as final results.
- Report trust6/core7 complete-case TSSEM as diagnostic or sensitivity evidence
  only if the manuscript explicitly labels them as reduced-route probes.
- Continue source search/adjudication for `ANX-TRU` and for complete-case
  densification before making a full10 MASEM claim.

## Next task

Search the corrected input, frozen reference, latest-human workbooks, and
AI/source-trace artifacts for source-plausible `ANX-TRU` evidence. If no
source-plausible pair exists, document full10 as pairwise nearly complete but
not fully estimable and proceed with reduced-route sensitivity reporting.
