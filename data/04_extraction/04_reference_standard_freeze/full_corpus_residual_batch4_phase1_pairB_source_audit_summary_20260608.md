# Residual Batch 4 Phase 1 Pair B Source Audit Summary

Date: 2026-06-08

Status: residual `batch_4_moderate::phase1::Pair B` source audit completed as a Step 4 sub-batch draft layer. Shared progress/gap-map files are intentionally unchanged until batch 4 sub-batches are merged. This is not a full 213-study freeze and does not start Step 5.

## Outputs

- `full_corpus_residual_batch4_phase1_pairB_source_audit_20260608.csv`
- `full_corpus_residual_batch4_phase1_pairB_reference_draft_20260608.csv`

## Scope

Eighteen residual `batch_4_moderate` studies in Phase 1 Pair B were processed using the combined coder-value extract, selected coder source-location trace, and exact local PDF availability/text extraction checks. Direct/Fornell-Larcker evidence was preferred over beta/path substitutions when both were available. S117 original beta rows were Peterson-Brown converted and keep original beta values in `original_beta`.

## Row Draft Counts

| Study | Selected coder | Draft rows | Status |
|---|---:|---:|---|
| `S163` | `R4` | 15 | `reference_draft_created_from_R4_table6_direct_rows` |
| `S186` | `R4` | 15 | `reference_draft_created_from_R4_table2_direct_precision_rows` |
| `S007` | `R3` | 10 | `reference_draft_created_from_R3_direct_rows_rejecting_R4_beta_paths` |
| `S125` | `R4` | 15 | `reference_draft_created_from_R4_complete_table6_rows` |
| `S055` | `R3` | 21 | `reference_draft_created_from_R3_complete_direct_rows_with_final_visual_caveat` |
| `S212` | `R4` | 8 | `reference_draft_created_from_R4_table3_precision_rows` |
| `S017` | `R3` | 6 | `reference_draft_created_from_R3_numeric_direct_rows_excluding_invalid_anx_string` |
| `S073` | `R3` | 7 | `reference_draft_created_from_R3_beta_converted_rows` |
| `S117` | `R3` | 7 | `reference_draft_created_from_R3_original_beta_rows_converted_peterson_brown` |
| `S176` | `R3` | 28 | `reference_draft_created_from_R3_complete_direct_rows_with_final_visual_caveat` |
| `S010` | `R4` | 6 | `reference_draft_created_from_R4_beta_converted_nordic_rows` |
| `S043` | `R4` | 6 | `reference_draft_created_from_R4_direct_text_section_rows` |
| `S111` | `R4` | 6 | `reference_draft_created_from_R4_table2_direct_rows` |
| `S160` | `R4` | 6 | `reference_draft_created_from_R4_table6_direct_rows` |
| `S225` | `R4` | 6 | `reference_draft_created_from_R4_beta_converted_table4_rows` |
| `S020` | `R4` | 10 | `reference_draft_created_from_R4_table3_direct_rows_excluding_R3_invalid_anx_string` |
| `S026` | `R3` | 15 | `reference_draft_created_from_R3_complete_direct_rows_with_final_visual_caveat` |
| `S170` | `R4` | 5 | `reference_draft_created_from_R4_beta_converted_table5_rows` |
| **Total** |  | **192** | 18 source-checked sub-batch drafts |

## Evidence Summary

| Evidence type | Rows |
|---|---:|
| `source_reported_direct_correlation_or_latent_correlation` | 161 |
| `standardized_path_beta_converted` | 24 |
| `standardized_path_beta_converted_from_original_beta` | 7 |

| r source | Rows |
|---|---:|
| `beta_converted_peterson_brown` | 31 |
| `source_reported_pearson_or_latent_correlation` | 161 |

## Remaining Caveats

- S055, S176, and S026 use complete direct selected-coder row sets whose row source-location strings were blank; retain final visual table-label audit before full freeze.
- S073, S010, S225, S170, and S117 retain beta/path conversion caveats; S117 was converted from original beta values in this sub-batch draft.
- S017 and S020 exclude nonnumeric coder-string rows from the row draft.
- This sub-batch does not update shared full-corpus progress/gap-map files; merge only after the remaining batch 4 sub-batches are complete.

## Recommended Next Action

Process the remaining residual `batch_4_moderate` sub-batches: phase1/Pair A, phase2/Pair C, and phase2/Pair D. Keep Step 5 inactive until the full reference scope is frozen.
