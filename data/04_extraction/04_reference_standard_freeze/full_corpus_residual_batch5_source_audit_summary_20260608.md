# Residual Batch 5 Low-Burden Source Audit Summary

Date: 2026-06-08

Status: residual `batch_5_low_burden` source audit completed as a Step 4 draft layer and ready for shared progress/gap-map merge. This is not a full 213-study freeze and does not start Step 5.

## Outputs

- `full_corpus_residual_batch5_source_audit_20260608.csv`
- `full_corpus_residual_batch5_reference_draft_20260608.csv`

## Scope

31 residual `batch_5_low_burden` studies were processed using the combined coder-value extract, selected coder source-location trace, the batch 4/5 execution manifest, and exact local PDF availability/text extraction checks. Direct/Fornell-Larcker evidence was preferred over beta/path substitutions when available; beta/path and author-provided/model-coefficient rows are retained only as caveated draft evidence.

## Phase/Pair Counts

| Phase | Pair | Studies |
|---|---|---:|
| `phase1` | `Pair A` | 3 |
| `phase1` | `Pair B` | 6 |
| `phase2` | `Pair C` | 5 |
| `phase2` | `Pair D` | 17 |

## Row Draft Counts

| Study | Phase | Pair | Selected coder | Draft rows | Status |
|---|---|---|---:|---:|---|
| `S019` | `phase1` | `Pair A` | `R1` | 3 | `reference_draft_created_from_R1_fornell_larcker_table3_rows` |
| `S177` | `phase1` | `Pair A` | `R2` | 3 | `reference_draft_created_from_R2_table3_direct_rows` |
| `S211` | `phase1` | `Pair A` | `R2` | 2 | `reference_draft_created_from_R2_author_provided_model_coefficients` |
| `S050` | `phase1` | `Pair B` | `R4` | 15 | `reference_draft_created_from_R4_table5_direct_rows` |
| `S100` | `phase1` | `Pair B` | `R4` | 3 | `reference_draft_created_from_R4_table6_direct_rows` |
| `S142` | `phase1` | `Pair B` | `R4` | 3 | `reference_draft_created_from_R4_table3_direct_rows` |
| `S167` | `phase1` | `Pair B` | `R3` | 3 | `reference_draft_created_from_R3_complete_direct_rows_with_final_visual_caveat` |
| `S184` | `phase1` | `Pair B` | `R4` | 10 | `reference_draft_created_from_R4_table4_direct_rows` |
| `S213` | `phase1` | `Pair B` | `R4` | 3 | `reference_draft_created_from_R4_table5_direct_rows` |
| `S034` | `phase2` | `Pair C` | `R4` | 3 | `reference_draft_created_from_R4_complete_direct_heatmap_rows_with_final_visual_caveat` |
| `S061` | `phase2` | `Pair C` | `R1` | 7 | `reference_draft_created_from_R1_mixed_table5_direct_and_table6_beta_converted_rows` |
| `S080` | `phase2` | `Pair C` | `R1` | 4 | `reference_draft_created_from_R1_beta_converted_tableIII_rows` |
| `S115` | `phase2` | `Pair C` | `R4` | 6 | `reference_draft_created_from_R4_complete_direct_heatmap_rows_with_final_visual_caveat` |
| `S152` | `phase2` | `Pair C` | `R1` | 3 | `reference_draft_created_from_R1_beta_converted_table3_rows` |
| `S002` | `phase2` | `Pair D` | `R2` | 15 | `reference_draft_created_from_R2_table9_direct_rows` |
| `S024` | `phase2` | `Pair D` | `R2` | 9 | `reference_draft_created_from_R2_beta_converted_table6_rows` |
| `S025` | `phase2` | `Pair D` | `R2` | 21 | `reference_draft_created_from_R2_table3_direct_rows` |
| `S027` | `phase2` | `Pair D` | `R2` | 10 | `reference_draft_created_from_R2_table6_direct_rows` |
| `S032` | `phase2` | `Pair D` | `R2` | 15 | `reference_draft_created_from_R2_table4_direct_rows_with_mapping_caveat` |
| `S068` | `phase2` | `Pair D` | `R2` | 7 | `reference_draft_created_from_R2_beta_converted_figure1_rows` |
| `S077` | `phase2` | `Pair D` | `R3` | 10 | `reference_draft_created_from_R3_complete_direct_rows_with_final_visual_caveat` |
| `S078` | `phase2` | `Pair D` | `R2` | 6 | `reference_draft_created_from_R2_table3_direct_rows` |
| `S085` | `phase2` | `Pair D` | `R2` | 3 | `reference_draft_created_from_R2_table2_direct_rows` |
| `S094` | `phase2` | `Pair D` | `R3` | 1 | `reference_draft_created_from_R3_beta_converted_table3_row` |
| `S096` | `phase2` | `Pair D` | `R2` | 2 | `reference_draft_created_from_R2_direct_rows_with_source_label_caveat` |
| `S114` | `phase2` | `Pair D` | `R2` | 14 | `reference_draft_created_from_R2_table3_direct_rows` |
| `S135` | `phase2` | `Pair D` | `R2` | 10 | `reference_draft_created_from_R2_table13_direct_rows_with_mapping_caveat` |
| `S137` | `phase2` | `Pair D` | `R2` | 15 | `reference_draft_created_from_R2_table2_direct_rows_with_mapping_caveat` |
| `S150` | `phase2` | `Pair D` | `R2` | 4 | `reference_draft_created_from_R2_beta_converted_table5_rows` |
| `S210` | `phase2` | `Pair D` | `R2` | 6 | `reference_draft_created_from_R2_table4_direct_rows` |
| `S221` | `phase2` | `Pair D` | `R2` | 15 | `reference_draft_created_from_R2_table6_direct_rows_with_mapping_caveat` |
| **Total** |  |  |  | **231** | 31 source-checked drafts |

## Evidence Summary

| Evidence type | Rows |
|---|---:|
| `author_provided_or_model_coefficient_trace` | 2 |
| `fornell_larcker_off_diagonal_latent_correlation` | 3 |
| `source_reported_direct_correlation_or_latent_correlation` | 197 |
| `standardized_path_beta_converted` | 29 |

| r source | Rows |
|---|---:|
| `author_provided_model_coefficient` | 2 |
| `beta_converted_peterson_brown` | 29 |
| `source_reported_latent_correlation` | 3 |
| `source_reported_pearson_or_latent_correlation` | 197 |

| Mapping confidence | Rows |
|---|---:|
| `high` | 115 |
| `medium` | 116 |

## Remaining Caveats

- Routine final full-corpus freeze audit; retained rows are source-coder traceable.
- author-provided/model-coefficient values; retain source-type caveat and final visual audit before full freeze
- R3 ANX/prejudice mapping remains a final-freeze audit caveat
- selected direct rows need final visual table-label audit because source-location strings are blank
- selected direct heatmap rows need final visual table-label audit because source-location strings are blank
- mixed direct and beta-converted rows; retain source-type caveat in final freeze audit
- beta-converted path rows; retain beta-conversion caveat in final freeze audit
- beta-converted path rows; R3 extra ATT-TRU/BI-SI rows remain final-freeze audit caveats
- SE-UB/SI-UB mapping discrepancy remains a final-freeze audit caveat
- selected direct rows need final visual table-label audit; SI/social-support mapping retained as caveat
- single beta-converted row; retain beta-conversion caveat in final freeze audit
- direct row source-label caveat; retain final visual audit requirement
- R3 extra EE-UB row remains a final-freeze audit caveat
- PE-SE/PE-SI mapping discrepancy remains a final-freeze audit caveat
- PE-SE/FC-UB mapping discrepancy remains a final-freeze audit caveat
- beta-converted path rows; R3 extra FC-UB/SI-UB rows remain final-freeze audit caveats
- This batch does not freeze the full 213-study reference; drafted rows remain pending final full-corpus freeze application.

## Recommended Next Action

Merge batch 5 into the shared full-corpus progress/gap-map layer, then continue the remaining Phase 1 rule/progress and lightweight-status queues. Keep Step 5 inactive until the full reference scope is frozen.
