# Residual Batch 4 Phase 2 Pair D Source Audit Summary

Date: 2026-06-08

Status: residual `batch_4_moderate::phase2::Pair D` source audit completed as a Step 4 sub-batch draft layer. Shared progress/gap-map files are intentionally unchanged until batch 4 sub-batches are merged. This is not a full 213-study freeze and does not start Step 5.

## Outputs

- `full_corpus_residual_batch4_phase2_pairD_source_audit_20260608.csv`
- `full_corpus_residual_batch4_phase2_pairD_reference_draft_20260608.csv`

## Scope

12 residual `batch_4_moderate` studies in Phase 2 Pair D were processed using the combined coder-value extract, selected coder source-location trace, the batch 4/5 execution manifest, and exact local PDF availability/text extraction checks. Direct/Fornell-Larcker evidence was preferred over beta/path substitutions when available; beta/path rows are retained only as caveated draft evidence.

## Row Draft Counts

| Study | Selected coder | Draft rows | Status |
|---|---:|---:|---|
| `S004` | `R2` | 21 | `reference_draft_created_from_R2_table3_direct_rows` |
| `S031` | `R2` | 6 | `reference_draft_created_from_R2_table2_direct_rows` |
| `S098` | `R2` | 6 | `reference_draft_created_from_R2_table3_direct_rows` |
| `S131` | `R2` | 4 | `reference_draft_created_from_R2_beta_converted_table8_rows` |
| `S143` | `R2` | 10 | `reference_draft_created_from_R2_table3_direct_rows` |
| `S161` | `R2` | 10 | `reference_draft_created_from_R2_table5_direct_rows` |
| `S171` | `R2` | 15 | `reference_draft_created_from_R2_table3_direct_rows` |
| `S173` | `R2` | 21 | `reference_draft_created_from_R2_table2_direct_rows` |
| `S181` | `R2` | 6 | `reference_draft_created_from_R2_table3_direct_rows` |
| `S183` | `R2` | 15 | `reference_draft_created_from_R2_table4_direct_rows` |
| `S204` | `R2` | 7 | `reference_draft_created_from_R2_beta_converted_table5_rows` |
| `S207` | `R3` | 6 | `reference_draft_created_from_R3_direct_table3_rows_with_numeric_typo_caveat` |
| **Total** |  | **127** | 12 source-checked sub-batch drafts |

## Evidence Summary

| Evidence type | Rows |
|---|---:|
| `source_reported_direct_correlation_or_latent_correlation` | 116 |
| `standardized_path_beta_converted` | 11 |

| r source | Rows |
|---|---:|
| `beta_converted_peterson_brown` | 11 |
| `source_reported_pearson_or_latent_correlation` | 116 |

| Mapping confidence | Rows |
|---|---:|
| `high` | 110 |
| `medium` | 17 |

## Remaining Caveats

- Routine final full-corpus freeze audit; retained rows are source-coder traceable.
- beta-converted rows with BI/UB outcome-orientation caveat; retain in final freeze audit
- R3 nonnumeric/misaligned row remains excluded from this draft
- beta-converted Table 5 structural-path rows; row mapping and N discrepancy retained as final-freeze caveat
- R2 BI-PE numeric-format error excluded; selected direct rows need final visual table-label audit where source-location is blank
- This sub-batch does not update shared full-corpus progress/gap-map files; merge only after all batch 4 sub-batches are complete.

## Recommended Next Action

Merge the completed batch 4 Phase 1 and Phase 2 sub-batch draft layers into the shared full-corpus progress/gap-map audit layer, then continue the remaining Phase 1 rule/progress and lightweight-status queues. Keep Step 5 inactive until the full reference scope is frozen.
