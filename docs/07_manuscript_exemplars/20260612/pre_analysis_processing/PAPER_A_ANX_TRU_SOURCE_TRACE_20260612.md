# Paper A ANX-TRU Source Trace

Date: 2026-06-12

## Why ANX-TRU Was Flagged

The pre-analysis N/matrix gate showed `ANX-TRU` as 0 rows in the 2026-06-05
Paper A primary direct-r model-ready freeze. The researcher noted that this
seemed inconsistent with prior memory of available rows, so the pair was traced
across the legacy Paper A package, the post-freeze full-corpus Step 5 shell, the
public metadata package, and the mounted External SSD repo copies.

## Current Finding

The 0-row result is not evidence that the literature has no `ANX-TRU` data. It
means the 2026-06-05 Paper A primary direct-r freeze contains no eligible
`ANX-TRU` row. After deduplicating shell/template/public-metadata traces, the
broader 2026-06-09 full-corpus reference and legacy expanded/sensitivity files
contain unique `ANX-TRU` candidate evidence in separate source-type strata:

| interpretation | rows |
| --- | --- |
| legacy_expanded_or_sensitivity_only_source_statistic_review_candidate | 1 |
| post_freeze_full_corpus_converted_effect_candidate_compare_alongside_primary_not_pooled | 1 |
| post_freeze_full_corpus_direct_r_candidate_not_in_20260605_paper_a_primary | 1 |
| post_freeze_full_corpus_latent_correlation_candidate_main_text_separate_panel | 1 |

## Studies Found

| study_id | rows |
| --- | --- |
| S036 | 1 |
| S066 | 1 |
| S102 | 1 |
| S142 | 1 |

## Method Decision

For Paper A primary direct-r TSSEM/OSMASEM, `ANX-TRU` remains not estimable from
the 2026-06-05 primary direct-r freeze. For the revised manuscript spine, this
pair should not simply be labeled absent. It should be handled as a source-type
and corpus-version boundary:

- `S036` is a post-freeze full-corpus direct-r candidate.
- `S102` is a post-freeze latent/Fornell-Larcker off-diagonal candidate.
- `S066` is a post-freeze beta/path-converted candidate.
- `S142` appears only in the legacy expanded/sensitivity source-statistic path.

The next analysis step is therefore to decide whether Paper A should be rebuilt
from the 2026-06-09 full-corpus reference for final claims, rather than relying
on the 2026-06-05 legacy primary freeze alone.

## SSD Check

The mounted External SSD contains repo copies, but the checked
`journal_AI-adoption_meta` copy is shallower than the current workspace and did
not add ANX-TRU rows. The `dissertation_AI-adoption_meta` CSVs also did not
contain additional ANX-TRU rows. Current best evidence is therefore the
post-freeze full-corpus reference in this workspace.

## Output

- `paper_a_anx_tru_source_trace_20260612.csv`
- `paper_a_anx_tru_unique_candidate_trace_20260612.csv`
