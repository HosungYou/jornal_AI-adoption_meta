# Full-Corpus Residual Batch 1 Source Audit Summary

Date: 2026-06-08

Status: residual `batch_1_high_burden` source audit completed as a Step 4 draft/status layer. This is not a full 213-study freeze and does not start Step 5.

## Outputs

- `full_corpus_residual_batch1_source_audit_20260608.csv`
- `full_corpus_residual_batch1_reference_draft_20260608.csv`
- Updated `full_corpus_step4_application_progress_20260608.csv`
- Updated `full_corpus_freeze_gap_map_20260608.csv`
- Updated `full_corpus_residual_adjudication_triage_20260608.csv`

## Scope

Seven high-burden residual studies were source-checked from local PDFs and the combined coder-value extract. The PDFs were used as local evidence only and were not copied into this Step 4 folder or committed.

## Row Draft Counts

| Study | Draft rows |
|---|---:|
| `S030` | 21 |
| `S046` | 15 |
| `S048` | 21 |
| `S057` | 28 |
| `S178` | 10 |
| `S188` | 6 |
| `S190` | 21 |
| **Total** | **122** |

## Study-Level Decisions

| Study | Pair | Rows | Source decision | Remaining caveat |
|---|---|---:|---|---|
| `S030` | `Pair A` | 21 | reference_draft_created_with_pbc_to_fc_caveat | PBC-to-FC mapping remains a construct-family caveat for final expert freeze audit. |
| `S046` | `Pair A` | 15 | reference_draft_created_with_ai_stb_to_anx_caveat | AI-STB-to-ANX remains a moderate-confidence mapping for final expert freeze audit. |
| `S048` | `Pair B` | 21 | reference_draft_created_from_one_coder_source_checked_rows | One-coder-only row set should be carried to final freeze audit, but values are source-checkable in the PDF table. |
| `S057` | `Pair B` | 28 | reference_draft_created_from_one_coder_source_checked_rows_with_table_typo_excluded | One-coder-only row set and source table typo should be visible in final freeze audit, but retained target rows are source-checkable. |
| `S178` | `Pair A` | 10 | reference_draft_created_with_idt_exclusion_caveat | R2 construct remapping of IDT constructs is rejected for this draft and should remain visible in final audit notes. |
| `S188` | `Pair C` | 6 | reference_draft_created_with_diagonal_value_correction | PTA-to-TRU mapping remains moderate-confidence; the .679 versus .889 correction should be retained in audit notes. |
| `S190` | `Pair A` | 21 | reference_draft_created_with_moderate_mapping_caveats | ATT/ANX/FC mappings are moderate-confidence construct-family decisions for final expert freeze audit. |

## Key Source Checks

- S030: PDF Table 4 confirms the PEOU/PU/PT/ATT/SN/PBC/INT Fornell-Larcker off-diagonal values; PBC is retained as FC rather than R2's SE mapping.
- S046: PDF Table 5 confirms the Fornell-Larcker off-diagonal values and that AI-STB to PU is negative; AI-STB is retained as ANX with a mapping caveat.
- S048: PDF Table 2 raw text confirms Pearson correlations among retained target constructs; PA/NOV/POL are excluded.
- S057: PDF Table 2 confirms the lower-triangle construct matrix and the source FC-PV `2.30` typo; PV and other non-target constructs are excluded, so the typo is not used.
- S178: PDF Table 4 supports the retained TAM/trust target rows; IDT constructs are excluded rather than remapped to FC/SE/TRA.
- S188: PDF Table 3 confirms `EE-PE = .679`; R4's `.889` is the PEAI diagonal square-root AVE and is excluded.
- S190: PDF Table 2 confirms source-reported Pearson correlations; ATT/ANX/FC rows retain moderate-confidence mapping notes.

## Effect on Full-Corpus Progress

- `correlation_disagreement_pending_adjudication` is reduced from 124 to 117.
- A new progress category records 7 studies as `residual_batch1_source_checked_reference_draft`.
- The new row-level draft adds 122 source-checked rows pending final full-corpus freeze application.

## Recommended Next Action

Process residual `batch_2_numeric_source` studies from `full_corpus_residual_adjudication_triage_20260608.csv`, then continue the one-coder-only and moderate residual batches. Keep Step 5 inactive until the intended full reference scope is frozen.
