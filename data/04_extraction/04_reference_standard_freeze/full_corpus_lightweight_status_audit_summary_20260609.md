# Full-Corpus Lightweight Status Audit Summary

Date: 2026-06-09

Status: lightweight metadata/status audit completed for 49 studies: 48 metadata/lightweight cases plus S196, the single correlation-queue lightweight case. This is not a full 213-study freeze and does not start Step 5.

## Outputs

- `full_corpus_lightweight_status_audit_20260609.csv`
- `full_corpus_step4_application_progress_20260608.csv`
- `full_corpus_freeze_gap_map_20260608.csv`

## Audit Type Counts

| Audit type | Studies |
|---|---:|
| `metadata_status_lightweight_audit` | 43 |
| `no_target_correlation_status_audit` | 6 |

## Terminal Status Counts

| Status draft | Studies |
|---|---:|
| `included_coder_agreed_correlation_rows_status_draft` | 43 |
| `excluded_from_masem_correlation_contribution_status_draft` | 6 |

## Phase/Pair Counts

| Phase | Pair | Studies |
|---|---|---:|
| `phase1` | `Pair A` | 2 |
| `phase1` | `Pair B` | 10 |
| `phase2` | `Pair C` | 23 |
| `phase2` | `Pair D` | 14 |

## Reference Row Carry-Forward

- Coder-agreed target correlation row drafts to carry forward at final freeze application: 449.
- New row-level source-value adjudication records created in this audit: 0.
- No-target status drafts: S023, S105, S109, S144, S196, and S215 are carried as E-FT1/status-only drafts pending final freeze QA.

## S196 Resolution

- S196 was the only `correlation_queue_lightweight_audit_pending` case. It has no coded target correlation rows, R2 carried a no-correlation/excluded status, and a lightweight PDF text check did not identify a usable target construct-pair matrix or direct standardized target-path set. It is closed as `excluded_from_masem_correlation_contribution_status_draft` with E-FT1 pending final full-corpus QA.

## Recommended Next Action

1. Assemble the final full-corpus Step 4 freeze application/QA layer across source-checked row drafts, coder-agreed lightweight rows, status-only exclusions, and scoped frozen records.
2. Preserve caveats for S074, S187, path/beta-converted rows, HTMT exclusions, and manual decision records during final freeze QA.
3. Keep Step 5 inactive until the full reference scope is frozen and the post-freeze gate is explicitly passed.
