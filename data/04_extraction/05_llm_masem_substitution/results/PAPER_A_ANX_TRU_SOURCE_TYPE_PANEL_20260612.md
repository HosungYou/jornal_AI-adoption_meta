# Paper A ANX-TRU Source-Type Panel

Date: 2026-06-12

## Boundary

`ANX-TRU` is absent from the 2026-06-05 Paper A primary direct-r freeze,
but it is not absent from the broader evidence trail. The post-freeze
full-corpus reference contains source-type-specific candidates. They should
be reported as a corpus/source-type boundary, not silently pooled into the
legacy primary matrix.

## Source-Type Counts

| source_type_class | rows |
| --- | --- |
| post_freeze_converted_effect_candidate | 2 |
| post_freeze_direct_r_candidate | 1 |
| post_freeze_latent_correlation_candidate | 1 |

## Candidate Panel

| study_id | r_numeric_or_reference | source_type_class | manuscript_role | modeling_action |
| --- | --- | --- | --- | --- |
| S036 | -0.26 | post_freeze_direct_r_candidate | main_text_source_type_panel_primary_like_not_legacy_freeze | compare_against_legacy_primary_absence |
| S066 | 0.19 | post_freeze_converted_effect_candidate | main_text_converted_effect_comparison_panel | compare_not_pool_with_direct_r |
| S102 | 0.027 | post_freeze_latent_correlation_candidate | main_text_separate_latent_panel | compare_not_pool_with_observed_direct_r |
| S142 | 0.027 | post_freeze_converted_effect_candidate | main_text_converted_effect_comparison_panel | compare_not_pool_with_direct_r |

## Recommended Claim Boundary

- Legacy 2026-06-05 primary direct-r model: `ANX-TRU` remains not estimable.
- Revised manuscript: describe `ANX-TRU` as recoverable only through the
  post-freeze full-corpus source-type panel.
- Do not pool direct-r, latent, and converted-effect candidates in one primary
  estimate. The comparison itself is a methodological result.

## Output

- `data/04_extraction/05_llm_masem_substitution/results/paper_a_anx_tru_source_type_panel_20260612.csv`
