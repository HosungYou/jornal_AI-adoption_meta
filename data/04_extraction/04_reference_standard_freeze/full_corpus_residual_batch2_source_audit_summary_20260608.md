# Full-Corpus Residual Batch 2 Source Audit Summary

Date: 2026-06-08

Status: residual `batch_2_numeric_source` source audit completed as a Step 4 draft/status layer. This is not a full 213-study freeze and does not start Step 5.

## Outputs

- `full_corpus_residual_batch2_source_audit_20260608.csv`
- `full_corpus_residual_batch2_reference_draft_20260608.csv`
- Updated `full_corpus_step4_application_progress_20260608.csv`
- Updated `full_corpus_freeze_gap_map_20260608.csv`
- Updated `full_corpus_residual_adjudication_triage_20260608.csv`

## Scope

Twenty residual `batch_2_numeric_source` studies were checked against local PDF text and the combined coder-value extract. Eighteen studies were converted into source-checked row-level reference drafts. Two studies were kept out of the row draft pending manual decisions: `S015` needs a multisample stratum/record-ID decision, and `S066` needs beta/path or exclusion adjudication.

## Row Draft Counts

| Study | Draft rows | Status |
|---|---:|---|
| `S076` | 15 | `reference_draft_created_from_R1_source_checked_table4` |
| `S015` | 0 | `manual_followup_multisample_stratum_decision_required` |
| `S053` | 10 | `reference_draft_created_from_R1_source_checked_target_rows` |
| `S067` | 15 | `reference_draft_created_from_R1_table4_rejecting_path_mix` |
| `S075` | 15 | `reference_draft_created_from_R1_table4_rejecting_path_substitution` |
| `S146` | 15 | `reference_draft_created_from_R4_complete_table4_rows` |
| `S153` | 15 | `reference_draft_created_with_aut_tru_mapping_caveats` |
| `S162` | 15 | `reference_draft_created_with_anx_mapping_caveat` |
| `S169` | 10 | `reference_draft_created_with_behavior_to_ub_source_correction` |
| `S066` | 0 | `manual_followup_beta_path_typo_required` |
| `S012` | 10 | `reference_draft_created_from_sqrt_transformed_squared_correlations` |
| `S018` | 10 | `reference_draft_created_from_matching_coder_rows` |
| `S045` | 10 | `reference_draft_created_from_R4_precision_values` |
| `S052` | 10 | `reference_draft_created_from_R4_precision_values` |
| `S063` | 10 | `reference_draft_created_with_ah_to_ub_caveat` |
| `S097` | 10 | `reference_draft_created_from_matching_high_correlation_rows` |
| `S102` | 10 | `reference_draft_created_with_technostress_to_anx_caveat` |
| `S103` | 10 | `reference_draft_created_with_hei_support_to_fc_caveat` |
| `S119` | 10 | `reference_draft_created_from_matching_table5_rows` |
| `S136` | 10 | `reference_draft_created_from_matching_table3_rows` |
| **Total** | **210** | 18 source-checked drafts; 2 manual follow-up studies |

## Study-Level Decisions

| Study | Pair | Rows | Source decision | Remaining caveat |
|---|---|---:|---|---|
| `S076` | `Pair A` | 15 | reference_draft_created_from_R1_source_checked_table4 | Carry R2 row-label shift as an audit note; retained values are source-checkable. |
| `S015` | `Pair A` | 0 | manual_followup_multisample_stratum_decision_required | Requires explicit decision whether to include Poland only, both country strata as separate records, or another prespecified handling rule. |
| `S053` | `Pair A` | 10 | reference_draft_created_from_R1_source_checked_target_rows | PDF text extraction is partially garbled; final freeze audit should visually confirm Table 5 row labels before freezing. |
| `S067` | `Pair C` | 15 | reference_draft_created_from_R1_table4_rejecting_path_mix | PC-to-TRU mapping remains a medium-confidence construct-family caveat for final freeze audit. |
| `S075` | `Pair C` | 15 | reference_draft_created_from_R1_table4_rejecting_path_substitution | Carry R4 path-substitution issue as an audit note; retained values are source-checkable in Table 4. |
| `S146` | `Pair B` | 15 | reference_draft_created_from_R4_complete_table4_rows | Carry R3 omission of UB rows as an audit note. |
| `S153` | `Pair C` | 15 | reference_draft_created_with_aut_tru_mapping_caveats | AUT/TRU construct mapping remains medium-confidence for final freeze audit. |
| `S162` | `Pair C` | 15 | reference_draft_created_with_anx_mapping_caveat | ANX rows remain a construct-family caveat because the source model also contains perceived stress. |
| `S169` | `Pair A` | 10 | reference_draft_created_with_behavior_to_ub_source_correction | Behavior-to-UB mapping and exclusion of AIHE/application outcome should remain visible for final freeze audit. |
| `S066` | `Pair C` | 0 | manual_followup_beta_path_typo_required | Requires expert beta-conversion/source correction and sample-definition adjudication before any reference rows are drafted. |
| `S012` | `Pair B` | 10 | reference_draft_created_from_sqrt_transformed_squared_correlations | Final freeze audit should preserve that these are transformed from source-reported squared correlations, not directly printed r values. |
| `S018` | `Pair A` | 10 | reference_draft_created_from_matching_coder_rows | No unresolved numeric caveat beyond excluded non-target constructs. |
| `S045` | `Pair B` | 10 | reference_draft_created_from_R4_precision_values | No remaining caveat beyond preserving source precision. |
| `S052` | `Pair B` | 10 | reference_draft_created_from_R4_precision_values | No remaining caveat beyond preserving source precision. |
| `S063` | `Pair C` | 10 | reference_draft_created_with_ah_to_ub_caveat | AH-to-UB mapping remains a medium-confidence construct-family caveat for final freeze audit. |
| `S097` | `Pair B` | 10 | reference_draft_created_from_matching_high_correlation_rows | Very high correlations should remain visible in final freeze audit but are source-reported. |
| `S102` | `Pair A` | 10 | reference_draft_created_with_technostress_to_anx_caveat | Technostress-to-ANX remains a medium-confidence construct-family caveat for final freeze audit. |
| `S103` | `Pair C` | 10 | reference_draft_created_with_hei_support_to_fc_caveat | HEI-support-to-FC mapping remains a medium-confidence construct-family caveat. |
| `S119` | `Pair C` | 10 | reference_draft_created_from_matching_table5_rows | PU-as-primary-PE decision should remain visible in final freeze audit. |
| `S136` | `Pair C` | 10 | reference_draft_created_from_matching_table3_rows | No unresolved caveat beyond excluded non-target UTAUT2 constructs. |

## Key Source Checks

- S012: PDF Table 3 explicitly labels off-diagonal entries as squared correlations; draft values are square-root transformed r values.
- S015: PDF confirms two independent country samples, Poland n=528 and India n=546; no row draft emitted until the stratum handling rule is explicit.
- S053: PDF Table 5 is a discriminant-validity/Fornell-Larcker table; only the target BI/EE/PE/SE/UB rows are drafted, while R2-only ATT rows remain excluded pending visual confirmation.
- S066: Source evidence is HTMT/path/VIF rather than a clean target correlation matrix; no row draft emitted because beta/path conversion and sample definition remain unresolved.
- S067 and S075: Table 4 correlation/discriminant-validity values are retained; path-coefficient substitutions are rejected.
- S169: Source labels the key endpoint as Behavior, so coder BI labels are source-corrected to UB; AI-in-higher-education/application rows are not drafted as target UB.

## Effect on Full-Corpus Progress

- `correlation_disagreement_pending_adjudication` is reduced from 117 to 97.
- A new progress category records 18 studies as `residual_batch2_source_checked_reference_draft`.
- A second category records 2 studies as `residual_batch2_manual_followup_required`.
- The new row-level draft adds 210 source-checked rows pending final full-corpus freeze application.

## Recommended Next Action

Process residual `batch_3_one_coder_only` studies from `full_corpus_residual_adjudication_triage_20260608.csv`, while keeping `S015` and `S066` visible as manual follow-up blockers. Keep Step 5 inactive until the intended full reference scope is frozen.
