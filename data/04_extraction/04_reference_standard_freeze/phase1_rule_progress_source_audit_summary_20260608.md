# Phase 1 Rule/Progress Source Audit Summary

Date: 2026-06-08

Status: 10 remaining Phase 1 rule/progress queue studies were source-checked into a Step 4 row-level reference draft. This is not a full 213-study freeze and does not start Step 5.

## Outputs

- `phase1_rule_progress_source_audit_20260608.csv`
- `phase1_rule_progress_reference_draft_20260608.csv`
- `phase1_rule_progress_audit_queue_20260608.csv`
- `full_corpus_step4_application_progress_20260608.csv`
- `full_corpus_freeze_gap_map_20260608.csv`

## Row Counts

| Study | Draft rows | Primary decision |
|---|---:|---|
| `S005` | 6 | Logged rule applied: JOY rows and CON-to-FC rows are excluded; retained target rows are AIA/AISE/BITL/PU only. |
| `S011` | 3 | Logged rule applied: retain TAM structural paths only; TTF-to-ATT and TTF-to-BI are not mapped to FC and are excluded. |
| `S044` | 10 | Logged rule applied: GAAIS Positive Attitudes toward AI is ATT; Negative Attitudes is not averaged into ATT. |
| `S079` | 5 | Logged rule applied: relevant effects are standardized path coefficients, not zero-order correlations; retain path/beta conversion caveat. |
| `S086` | 21 | Progress-only case source-value audited: direct Table 2 correlation matrix retained with R2 three-decimal precision. |
| `S087` | 10 | Logged rule applied: Satisfaction is not ATT; all Satisfaction-as-ATT rows are excluded from the target row draft. |
| `S166` | 5 | Logged rule applied: HTMT-only evidence is excluded; structural paths are retained as beta-converted/path-coefficient rows. |
| `S168` | 6 | Progress-only/source-type audit: HTMT table is not used; structural paths from Table 4 are retained as beta-converted/path-coefficient rows. |
| `S187` | 15 | Logged rule applied: Stress is mapped to ANX with traceability caveat; source table also supports non-ANX latent-correlation rows. |
| `S223` | 21 | Logged rule applied: R1-coded row set accepted; R2-only ATT/ENJ/security rows and source-alignment anomalies are excluded. |
| **Total** | **102** | |

## Evidence Types

| Evidence type | Rows |
|---|---:|
| `fornell_larcker_off_diagonal_latent_correlation` | 42 |
| `source_reported_direct_correlation_or_latent_correlation` | 41 |
| `standardized_path_beta_converted` | 19 |

## Mapping Confidence

| Confidence | Rows |
|---|---:|
| `high` | 78 |
| `medium` | 24 |

## Caveats Retained

- S011, S079, S166, and S168 are retained as path/beta-conversion evidence, not zero-order correlations.
- S166 and S168 retain HTMT exclusion notes; HTMT values are not used as target correlations.
- S187 retains a Stress-to-ANX construct-mapping caveat for final full-corpus freeze audit.
- S074 remains separately drafted with an ANX/AXT orientation caveat from the high-priority rule audit layer.

## Recommended Next Action

1. Run the remaining lightweight metadata/status audit queue: 48 metadata/lightweight studies plus 1 correlation-queue lightweight study.
2. Keep all row drafts in audit form until the final full-corpus freeze package is assembled and QA-checked.
3. Keep Step 5 inactive until the full reference scope is frozen.
