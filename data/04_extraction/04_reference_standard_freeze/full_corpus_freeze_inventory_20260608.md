# Full-Corpus Freeze Inventory

Date: 2026-06-09

Status: scope-lock inventory for the Paper B full-corpus Step 4 freeze path after residual batches 1-5, Phase 1 rule/progress audits, manual-blocker resolution, and lightweight status audit have been merged into the shared progress/gap-map. This is not a full 213-study freeze and does not start Step 5.

## Inputs

- `data/04_extraction/04_reference_standard_freeze/full_corpus_step4_application_progress_20260608.csv`
- `data/04_extraction/04_reference_standard_freeze/full_corpus_freeze_gap_map_20260608.csv`
- `data/04_extraction/04_reference_standard_freeze/full_corpus_residual_adjudication_triage_20260608.csv`
- `data/04_extraction/04_reference_standard_freeze/full_corpus_lightweight_status_audit_20260609.csv`
- `.omx/plans/paper_b_full_reference_freeze_ralplan_20260608.md`

## Corpus Count Check

- Progress rows: 213
- Gap-map rows: 213
- Residual triage rows: 124
- Lightweight status audit rows: 49
- Unique progress study IDs: 213
- Unique gap-map study IDs: 213

## Current Progress Status Counts

| Progress status | Studies |
|---|---:|
| `residual_batch4_source_checked_reference_draft` | 52 |
| `lightweight_status_audit_completed` | 49 |
| `residual_batch5_source_checked_reference_draft` | 31 |
| `residual_batch2_source_checked_reference_draft` | 18 |
| `phase1_high_confidence_reference_draft_or_exclusion_status` | 12 |
| `residual_batch3_source_checked_reference_draft` | 12 |
| `phase1_rule_progress_source_checked_reference_draft` | 10 |
| `scoped_phase2_frozen` | 8 |
| `residual_batch1_source_checked_reference_draft` | 7 |
| `phase2_confirmed_exclusion_full_corpus_status_draft` | 6 |
| `manual_blocker_resolved_reference_draft` | 4 |
| `phase1_rule_reference_draft_completed` | 3 |
| `phase1_rule_reference_draft_orientation_caveat` | 1 |

## Current Gap Status Counts

| Step 4 status | Studies |
|---|---:|
| `residual_batch4_source_checked_reference_draft` | 52 |
| `lightweight_status_audit_completed` | 49 |
| `source_checked_reference_draft_not_frozen_full_corpus` | 41 |
| `residual_batch5_source_checked_reference_draft` | 31 |
| `decision_logged_not_frozen_full_corpus` | 16 |
| `phase1_rule_progress_source_checked_reference_draft` | 10 |
| `frozen_scoped_package` | 8 |
| `source_checked_not_frozen_full_corpus` | 6 |

## Residual Triage Counts

| Recommended batch | Studies | Phase/pair split |
|---|---:|---|
| `batch_4_moderate` | 52 | phase1/Pair A: 9, phase1/Pair B: 18, phase2/Pair C: 13, phase2/Pair D: 12 |
| `batch_5_low_burden` | 31 | phase1/Pair A: 3, phase1/Pair B: 6, phase2/Pair C: 5, phase2/Pair D: 17 |
| `batch_2_numeric_source` | 20 | phase1/Pair A: 6, phase1/Pair B: 5, phase2/Pair C: 9 |
| `batch_3_one_coder_only` | 14 | phase1/Pair B: 9, phase2/Pair C: 1, phase2/Pair D: 4 |
| `batch_1_high_burden` | 7 | phase1/Pair A: 4, phase1/Pair B: 2, phase2/Pair C: 1 |

## Lightweight Audit Terminal Counts

| Status draft | Studies |
|---|---:|
| `included_coder_agreed_correlation_rows_status_draft` | 43 |
| `excluded_from_masem_correlation_contribution_status_draft` | 6 |

## Open Queues

- Manual blockers: none currently unresolved. S015, S066, S099, and S200 are resolved into `full_corpus_manual_blocker_reference_draft_20260608.csv` with caveats carried to final freeze audit.
- Phase 1 rule/source-value queue: none active in the shared progress layer; the remaining queue was source-audited into `phase1_rule_progress_reference_draft_20260608.csv`.
- Residual correlation-disagreement batches: none active in the shared progress layer; batches 1-5 have source-checked row drafts.
- Metadata/lightweight audit: none active in the shared progress layer; 49 studies are completed in `full_corpus_lightweight_status_audit_20260609.csv`.
- Active blocker: Step 4 full-corpus freeze is authorized; the next blocker is the separate post-freeze Step 5 gate for model/procedure scope and denominator-family reporting.

## Existing Step 4 Draft/Status Feeders

- Phase 1 high-confidence row/status drafts.
- Phase 1 high-priority rule row drafts and Phase 1 rule/progress source-checked row drafts.
- Residual batch 1-5 source-audit and reference-draft files.
- Manual-blocker resolved row drafts for S015/S066/S099/S200.
- Scoped Phase 2 frozen package files and Phase 2 confirmed exclusion status drafts.
- Lightweight status audit with 43 coder-agreed correlation-row carry-forward studies and 6 E-FT1/no-target status-only studies.

## Freeze Gates

- Every study must receive exactly one final `study_terminal_status`: `included`, `excluded`, or `manual_blocked` in the frozen package.
- `caveat_status` is an overlay, not a terminal status.
- S015/S066/S099/S200 are resolved into row drafts but must retain their country-stratum, beta/path, and mixed-evidence caveats in the final freeze audit.
- S074 must retain or resolve its ANX/AXT caveat explicitly.
- S187 must retain its stress-to-ANX mapping caveat explicitly.
- Path/beta-converted rows and HTMT exclusions must remain visible in the final freeze QA layer.
- Manual-blocked records, if any appear during final QA, must carry nonblank, nongeneric source/evidence/decision/evidence-basis fields; `unknown`, `not_available`, `n/a`, and `na` are not acceptable placeholders.
- Step 5 remains inactive unless a separate post-freeze gate is approved.

## 2026-06-09 Application QA Inventory Update

- Application rows: 2043
- Study status rows: 213
- Included application-draft studies: 194
- Excluded/no-target status-only studies: 17
- Duplicate-source status-only studies: 2
- Shared progress/gap-map status: `full_corpus_reference_application_qa_completed_pending_freeze_authorization` for all 213 studies.
- Step 5 remains inactive.

## 2026-06-09 Freeze Authorization Inventory Update

- Frozen target rows: 2043
- Frozen study-status rows: 213
- Included frozen-reference studies: 194
- Excluded/no-target frozen status studies: 17
- Duplicate-source frozen status studies: 2
- Shared progress/gap-map status: `full_corpus_reference_standard_frozen_authorized_20260609` for all 213 studies.
- Freeze authorization: `full_corpus_reference_standard_freeze_authorization_20260609.md`
- Caveat register: `full_corpus_reference_standard_freeze_caveat_register_20260609.csv`
- Step 5 remains inactive until a separate post-freeze gate is approved.

## Next Action

Open a separate post-freeze Step 5 gate before generating new full-corpus LLM comparison or MASEM substitution claims.
