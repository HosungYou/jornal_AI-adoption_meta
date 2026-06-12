# Paper B Step 5 Full-Corpus M1-R Status and Next Work

Date: 2026-06-12

## Current Documented State

The post-freeze Step 5 full-corpus `M1-R` execution blocker is resolved. The
full 213-study source-anchored Paper B reference was frozen on 2026-06-09, full
private source rendering reached 194/194 target studies and 2,043/2,043 target
rows, the 15-row S009/S010 beta/path exception-correction layer is consumed by
the scorer/gate, and the dedicated source-packet-required full-corpus `M1-R`
expansion completed on 2026-06-12.

The completed `M1-R` full-corpus run covers exactly 2,043 eligible task units
across nine shards, with 0 duplicate task IDs, 0 model CLI failures after the
repair-aware wrapper path, and 0 committed source-quote rows. The dedicated
manifest is:

- `locked_outputs/FULL_CORPUS_M1_R_FULL_RUN_MANIFEST_20260612.csv`

The primary row-level scoring outputs are:

- `results/paper_b_full_corpus_m1_raw_full_scored_20260612.csv`
- `results/paper_b_full_corpus_m1_raw_full_score_summary_20260612.csv`
- `results/paper_b_full_corpus_m1_raw_full_exception_layer_scored_20260612.csv`
- `results/paper_b_full_corpus_m1_raw_full_exception_layer_scored_summary_20260612.csv`

## Denominator-Family Outcomes

| Denominator family | Rows total | Scored rows | Correct rows | Abstention rows |
|---|---:|---:|---:|---:|
| `primary_latent_or_construct_correlation_with_source_type_flag` | 931 | 715 | 672 | 216 |
| `primary_direct_r_or_source_reported_correlation` | 697 | 572 | 517 | 125 |
| `secondary_beta_or_path_converted_effect_size` | 415 | 338 | 153 | 77 |

These outcomes must not be collapsed into a single corpus-wide accuracy score.
Converted beta/path rows remain a sensitivity stratum unless an approved
source-type or converted-effect claim explicitly consumes that layer.

## Exception-Aware Gate

The full exception-aware layer records 15 rows with gate-status effects:

| Gate status | Rows | Interpretation |
|---|---:|---|
| `not_scored_reference_contract_caveat` | 8 | Exclude from the generic full-accuracy numerator until the source-reference contract layer is explicitly consumed. |
| `not_scored_no_explicit_structural_path_evidence` | 4 | Exclude pending structural-path evidence or reference correction. |
| `not_scored_manual_source_reference_adjudication_required` | 1 | Hold out of automated accuracy interpretation. |
| `contract_aware_converted_effect_scoring_allowed_after_layer_consumed` | 2 | Policy-allowed rows; do not count as scored/correct in the generic full-corpus exception summary unless the contract-aware layer is explicitly consumed with locked answers. |

## Manuscript Work Completed in This Pass

The manuscript draft now includes the full-corpus `M1-R` denominator-family
paragraph, an updated claim boundary, and manuscript-ready Table 2/Table 5
drafts for claim-carrying reporting:

- `../../../paper_b/manuscript/PAPER_B_METHODS_RESULTS_DRAFT_20260611.md`

The workflow state documents now identify full-corpus `M1-R` as completed
rather than blocked:

- `../README.md`
- `../../README.md`
- `../../WORKFLOW_STATUS_LOG.md`
- `../../../CURRENT.md`
- `../../../.longtable/current-session.json`
- `../../../.longtable/state.json`

## Claim Boundaries

Supported now:

- Post-freeze source-packet-required `M1-R` evidence exists for the 2,043-row
  full-corpus Step 5 shell.
- Extraction validity can be reported by denominator family and exception-aware
  gate status.
- The workflow can be framed as task-contingent LLM augmentation and review
  triage support.

Not supported now:

- A single full-corpus accuracy denominator.
- A model-vendor ranking claim.
- An autonomous LLM replacement claim for the source-anchored human reference.
- A final all-construct or all-row SEM substitution-stability claim.
- Silent pooling of direct-r, source-flagged latent correlations, and converted
  beta/path rows.

## Remaining Work Order

1. Decide the SEM reporting lane: core-6 diagnostic only, core-plus-extension,
   or a later source-type-approved 10-construct rebuild.
2. If a broader SEM lane is selected, write the final TSSEM/MASEM specification
   before running or interpreting any all-construct model.
3. Convert Table 2/Table 5 into the final target-journal table format after the
   journal-specific manuscript template is fixed.
4. Update public repository or OSF materials only after the manuscript wording
   and share-safe artifact set are fixed; do not expose raw PDFs, raw workbooks,
   private source packets, raw transcripts, or unapproved raw model outputs.
