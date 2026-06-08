# Full-Corpus Manual Blocker Gate Summary

Date: 2026-06-08

Status: researcher manual decisions applied for S015/S066/S099/S200. These rows are now a source-anchored row-draft/status layer, not terminal `manual_blocked` records. This is not a full-corpus freeze and does not start Step 5.

## Outputs

- `full_corpus_manual_blocker_audit_20260608.csv`
- `full_corpus_manual_blocker_reference_draft_20260608.csv`
- `full_corpus_manual_blocker_status_20260608.csv`
- `full_corpus_unresolved_blocker_register_20260608.csv`
- `full_corpus_manual_blocker_resolved_register_20260608.csv`

## Applied Researcher Decisions

| Study | Pair | Selected coder | Draft rows | Remaining caveat |
|---|---|---:|---:|---|
| `S015` | `Pair A` | `R2` | 30 | R2 slash-coded Poland/India values were split into Poland `n=528` and India `n=546` country-stratum rows. |
| `S066` | `Pair C` | `R1` | 12 | Beta/path conversion plus the R1 source-corrected ANX-BI typo caveat remain visible. |
| `S099` | `Pair D` | `R2` | 12 | Beta/path conversion caveat remains visible because no clean target correlation matrix was available in the audited source. |
| `S200` | `Pair C` | `R1` | 15 | Mixed Table 6 beta-converted rows and Table 5 direct/discriminant-validity rows remain visible as a caveat. |
| **Total** |  |  | **69** |  |

## Unresolved Register

`full_corpus_unresolved_blocker_register_20260608.csv` now has zero data rows. Resolved decisions are preserved in `full_corpus_manual_blocker_resolved_register_20260608.csv`.

## Next Action

Carry the 69 manual-blocker rows into the final full-corpus freeze audit when the remaining Phase 1 rule/source-value queue, residual batch 4/5 adjudication, and lightweight status audits are complete. Step 5 remains inactive.
