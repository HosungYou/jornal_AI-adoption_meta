# Full-Corpus Freeze Inventory

Date: 2026-06-08

Status: scope-lock inventory for the Paper B full-corpus Step 4 freeze path. Manual blockers S015/S066/S099/S200 have been resolved into a source-anchored row-draft/status layer, but this is not a full 213-study freeze and does not start Step 5.

## Inputs

- `data/04_extraction/04_reference_standard_freeze/full_corpus_step4_application_progress_20260608.csv`
- `data/04_extraction/04_reference_standard_freeze/full_corpus_freeze_gap_map_20260608.csv`
- `data/04_extraction/04_reference_standard_freeze/full_corpus_residual_adjudication_triage_20260608.csv`
- `.omx/plans/paper_b_full_reference_freeze_ralplan_20260608.md`
- `.omx/plans/paper_b_freeze_baseline_raw_status_20260608.txt`
- `.omx/plans/paper_b_freeze_baseline_raw_diff_paths_20260608.txt`
- `.omx/plans/paper_b_freeze_baseline_pdf_status_20260608.txt`
- `.omx/plans/paper_b_freeze_baseline_step5_status_20260608.txt`

## Corpus Count Check

- Progress rows: 213
- Gap-map rows: 213
- Residual triage rows: 124
- Unique progress study IDs: 213
- Unique gap-map study IDs: 213

## Current Progress Status Counts

| Progress status | Studies |
|---|---:|
| `correlation_disagreement_pending_adjudication` | 83 |
| `correlation_queue_lightweight_audit_pending` | 1 |
| `manual_blocker_resolved_reference_draft` | 4 |
| `metadata_only_or_no_correlation_gap_pending_lightweight_audit` | 48 |
| `phase1_high_confidence_reference_draft_or_exclusion_status` | 12 |
| `phase1_progress_only_source_value_audit_queue` | 2 |
| `phase1_rule_decision_row_filter_or_source_audit_queue` | 8 |
| `phase1_rule_reference_draft_completed` | 3 |
| `phase1_rule_reference_draft_orientation_caveat` | 1 |
| `phase2_confirmed_exclusion_full_corpus_status_draft` | 6 |
| `residual_batch1_source_checked_reference_draft` | 7 |
| `residual_batch2_source_checked_reference_draft` | 18 |
| `residual_batch3_source_checked_reference_draft` | 12 |
| `scoped_phase2_frozen` | 8 |

## Current Gap Status Counts

| Step 4 status | Studies |
|---|---:|
| `decision_logged_not_frozen_full_corpus` | 26 |
| `frozen_scoped_package` | 8 |
| `not_frozen_lightweight_audit_pending` | 48 |
| `pre_adjudication_correlation_queue_not_frozen` | 1 |
| `pre_adjudication_disagreement_not_frozen` | 83 |
| `source_checked_not_frozen_full_corpus` | 6 |
| `source_checked_reference_draft_not_frozen_full_corpus` | 41 |

## Residual Triage Counts

| Recommended batch | Studies | Phase/pair split |
|---|---:|---|
| `batch_1_high_burden` | 7 | phase1/Pair A: 4, phase1/Pair B: 2, phase2/Pair C: 1 |
| `batch_2_numeric_source` | 20 | phase1/Pair A: 6, phase1/Pair B: 5, phase2/Pair C: 9 |
| `batch_3_one_coder_only` | 14 | phase1/Pair B: 9, phase2/Pair C: 1, phase2/Pair D: 4 |
| `batch_4_moderate` | 52 | phase1/Pair A: 9, phase1/Pair B: 18, phase2/Pair C: 13, phase2/Pair D: 12 |
| `batch_5_low_burden` | 31 | phase1/Pair A: 3, phase1/Pair B: 6, phase2/Pair C: 5, phase2/Pair D: 17 |

## Open Queues

- Manual blockers: none currently unresolved. S015, S066, S099, and S200 are resolved into `full_corpus_manual_blocker_reference_draft_20260608.csv` with caveats carried to final freeze audit.
- Phase 1 rule/source-value queue: S005, S011, S044, S079, S086, S087, S166, S168, S187, S223
- Residual `batch_4_moderate` (52): S004, S007, S009, S010, S017, S020, S026, S031, S038, S042, S043, S055, S058, S064, S069, S070, S071, S073, S089, S093, S095, S098, S104, S111, S112, S113, S117, S125, S129, S131, S134, S143, S148, S156, S160, S161, S163, S170, S171, S173, S176, S179, S181, S183, S186, S192, S201, S204, S207, S212, S216, S225
- Residual `batch_5_low_burden` (31): S002, S019, S024, S025, S027, S032, S034, S050, S061, S068, S077, S078, S080, S085, S094, S096, S100, S114, S115, S135, S137, S142, S150, S152, S167, S177, S184, S210, S211, S213, S221
- Metadata/lightweight audit (48): S003, S006, S008, S013, S016, S022, S023, S029, S036, S037, S040, S047, S049, S062, S082, S083, S088, S090, S105, S106, S107, S109, S116, S122, S123, S124, S126, S128, S133, S138, S139, S140, S144, S149, S155, S158, S159, S165, S172, S175, S182, S198, S199, S203, S205, S209, S215, S219
- Correlation-queue lightweight audit (1): S196

## Existing Step 4 Draft/Status Feeders

- Source-checked or scoped/frozen/status-draft study count: 71
- Existing feeder files include Phase 1 high-confidence drafts, Phase 1 high-priority rule drafts, residual batch 1/2/3 source audits and reference drafts, manual-blocker resolved row drafts, scoped Phase 2 frozen package files, and Phase 2 confirmed exclusion status drafts.

## Freeze Gates

- Every study must receive exactly one `study_terminal_status`: `included`, `excluded`, or `manual_blocked`.
- `caveat_status` is an overlay, not a terminal status.
- S015/S066/S099/S200 are resolved into row drafts but must retain their country-stratum, beta/path, and mixed-evidence caveats in the final freeze audit.
- S074 must retain or resolve its ANX/AXT caveat explicitly.
- Manual-blocked records must carry nonblank, nongeneric source/evidence/decision/evidence-basis fields; `unknown`, `not_available`, `n/a`, and `na` are not acceptable placeholders.
- Step 5 remains inactive unless a separate post-freeze gate is approved.

## Next Action

Proceed to the remaining Phase 1 rule/source-value queue or residual `batch_4_moderate` source adjudication. Stop before final freeze authorization, commit, or push unless the user explicitly approves those gates.
