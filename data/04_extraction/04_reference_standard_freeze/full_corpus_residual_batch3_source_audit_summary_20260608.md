# Full-Corpus Residual Batch 3 Source Audit Summary

Date: 2026-06-08

Status: residual `batch_3_one_coder_only` source audit completed as a Step 4 draft/status layer. This is not a full 213-study freeze and does not start Step 5.

## Outputs

- `full_corpus_residual_batch3_source_audit_20260608.csv`
- `full_corpus_residual_batch3_reference_draft_20260608.csv`
- Updated `full_corpus_step4_application_progress_20260608.csv`
- Updated `full_corpus_freeze_gap_map_20260608.csv`
- Updated `full_corpus_residual_adjudication_triage_20260608.csv`

## Scope

Fourteen residual `batch_3_one_coder_only` studies were checked against local PDF text and the combined coder-value extract. Twelve studies were converted into source-checked row-level reference drafts. Two studies were kept out of the row draft pending manual beta/path decisions: `S200` and `S099`.

## Row Draft Counts

| Study | Draft rows | Status |
|---|---:|---|
| `S072` | 15 | `reference_draft_created_from_source_corrected_core_utaut_rows` |
| `S060` | 15 | `reference_draft_created_from_one_coder_source_checked_rows` |
| `S127` | 15 | `reference_draft_created_from_one_coder_source_checked_rows_with_naming_caveat` |
| `S193` | 15 | `reference_draft_created_from_one_coder_source_checked_rows` |
| `S200` | 0 | `manual_followup_path_only_or_cross_loading_required` |
| `S157` | 28 | `reference_draft_created_from_R2_complete_table3_rows` |
| `S065` | 10 | `reference_draft_created_from_R3_source_corrected_core_tam_rows` |
| `S214` | 15 | `reference_draft_created_from_source_corrected_gptu_to_ub_rows` |
| `S099` | 0 | `manual_followup_beta_path_only_required` |
| `S130` | 10 | `reference_draft_created_with_table_sign_typo_caveat` |
| `S141` | 10 | `reference_draft_created_with_beh_reflective_caveat` |
| `S154` | 10 | `reference_draft_created_from_one_coder_source_checked_rows` |
| `S174` | 10 | `reference_draft_created_from_one_coder_source_checked_rows` |
| `S197` | 6 | `reference_draft_created_from_R3_source_corrected_acceptance_rows` |
| **Total** | **159** | 12 source-checked drafts; 2 manual follow-up studies |

## Study-Level Decisions

| Study | Pair | Rows | Source decision | Remaining caveat |
|---|---|---:|---|---|
| `S072` | `Pair B` | 15 | reference_draft_created_from_source_corrected_core_utaut_rows | R3/R4 mapping disagreements remain visible; retained rows are source-checkable off-diagonal Table 2 values. |
| `S060` | `Pair B` | 15 | reference_draft_created_from_one_coder_source_checked_rows | One-coder-only row set should remain visible in final freeze audit. |
| `S127` | `Pair B` | 15 | reference_draft_created_from_one_coder_source_checked_rows_with_naming_caveat | Naming collision caveat: paper PE is not target PE; target PE comes from PU. |
| `S193` | `Pair B` | 15 | reference_draft_created_from_one_coder_source_checked_rows | One-coder-only row set should remain visible in final freeze audit. |
| `S200` | `Pair C` | 0 | manual_followup_path_only_or_cross_loading_required | Requires expert decision on whether beta/path conversion is permitted or whether the study should be excluded from direct-r reference rows. |
| `S157` | `Pair D` | 28 | reference_draft_created_from_R2_complete_table3_rows | PC-to-SE and PA-to-AUT mappings remain medium-confidence caveats for final freeze audit. |
| `S065` | `Pair D` | 10 | reference_draft_created_from_R3_source_corrected_core_tam_rows | Carry R2 construct-mapping mismatch as an audit note. |
| `S214` | `Pair B` | 15 | reference_draft_created_from_source_corrected_gptu_to_ub_rows | GPTU-to-UB mapping should remain visible in final freeze audit. |
| `S099` | `Pair D` | 0 | manual_followup_beta_path_only_required | Requires expert beta-conversion/source-type decision before any reference rows are drafted. |
| `S130` | `Pair B` | 10 | reference_draft_created_with_table_sign_typo_caveat | ANX-PE is printed as positive .47 although source text says technology anxiety is negatively correlated with other variables; retain as printed pending final visual/expert audit. |
| `S141` | `Pair B` | 10 | reference_draft_created_with_beh_reflective_caveat | Source notes BEH was not purely reflective; carry this measurement caveat into final freeze audit. |
| `S154` | `Pair B` | 10 | reference_draft_created_from_one_coder_source_checked_rows | Paper uses AI as adoption intentions, not artificial intelligence; mapping note should remain visible. |
| `S174` | `Pair B` | 10 | reference_draft_created_from_one_coder_source_checked_rows | One-coder-only row set should remain visible in final freeze audit. |
| `S197` | `Pair D` | 6 | reference_draft_created_from_R3_source_corrected_acceptance_rows | Carry R2 label mismatch as an audit note. |

## Key Source Checks

- S072: Table 2 confirms latent correlations; privacy concerns are not mapped to ANX and hedonic motivation is not mapped to ATT.
- S157: Table 3 confirms a complete Pearson correlation matrix; R2's complete target row set is used, with PC-to-SE and PA-to-AUT caveats.
- S200 and S099: source evidence is path/beta-style or cross-loading/discriminant-validity evidence without a clean target correlation matrix, so no batch 3 row draft is emitted.
- S214: Table 5 confirms GPTU as a source-reported usage construct; GPTU is mapped to UB while hedonic motivation/habit rows are excluded.
- S130: Table 2 is retained as printed, but the ANX-PE sign contradiction remains a final-audit caveat.
- S197: Table 3 supports GenAI acceptance as BI and rejects the inconsistent R2 label mapping.

## Effect on Full-Corpus Progress

- `correlation_disagreement_pending_adjudication` is reduced from 97 to 83.
- A new progress category records 12 studies as `residual_batch3_source_checked_reference_draft`.
- A second category records 2 studies as `residual_batch3_manual_followup_required`.
- The new row-level draft adds 159 source-checked rows pending final full-corpus freeze application.

## Recommended Next Action

Resolve the accumulated manual follow-up blockers (`S015`, `S066`, `S099`, and `S200`) or proceed to residual `batch_4_moderate` if those manual decisions are deliberately deferred. Keep Step 5 inactive until the intended full reference scope is frozen.
