# Full-Corpus M1-R Beta/Path Contract Review

Date: 2026-06-11

## Scope

This review follows the 2026-06-11 `M1-R-SOURCE-SMOKE-TABLE-RETRIEVAL` rerun.
It is a gate review for S009/S010 beta/path rows only. It does not authorize a
larger `M1-R`, `M1-P`, `M2-R`, or `M3-R` execution, and it does not report
full-corpus accuracy, model-comparison, or MASEM substitution results.

## Evidence Reviewed

- `data/04_extraction/05_llm_masem_substitution/results/full_corpus_m1_r_source_rendered_table_retrieval_smoke_scored_20260609.csv`
- `data/04_extraction/05_llm_masem_substitution/results/full_corpus_m1_r_source_rendered_table_retrieval_smoke_scored_20260610.csv`
- `data/04_extraction/05_llm_masem_substitution/results/full_corpus_m1_r_source_rendered_table_retrieval_smoke_scored_20260611.csv`
- `data/04_extraction/05_llm_masem_substitution/locked_outputs/model_runs/paper_b_full_corpus_m1_raw_source_rendered_table_retrieval_smoke_20260609.csv`
- `data/04_extraction/05_llm_masem_substitution/locked_outputs/model_runs/paper_b_full_corpus_m1_raw_source_rendered_table_retrieval_smoke_20260610.csv`
- `data/04_extraction/05_llm_masem_substitution/locked_outputs/model_runs/paper_b_full_corpus_m1_raw_source_rendered_table_retrieval_smoke_20260611.csv`
- `data/04_extraction/04_reference_standard_freeze/full_corpus_reference_standard_frozen_20260609.csv`
- `data/04_extraction/07_paper_c_harness_benchmark/06_rerun_bundles/source_rendered_table_retrieval_smoke_task_ids_20260609.csv`
- Private source packets were consulted locally only to classify source-direction and source-type issues; source text is not reproduced here.

## Findings

The 2026-06-11 rerun should not be treated as evidence that the source-rendered
pipeline is ready for larger full-corpus M1-R execution. It exposes a contract
problem between three layers:

1. The frozen reference stores S009/S010 rows under
   `beta_converted_peterson_brown`, but the `original_beta` field is blank.
2. The prompt asks the model to recover the raw standardized beta/path
   coefficient and place that raw coefficient in `model_answer_normalized`.
3. The scorer compares `model_answer_normalized` directly with frozen `r_value`.

That contract is not stable enough for full-corpus accuracy scoring.

Row-level audit file:

- `data/04_extraction/05_llm_masem_substitution/results/full_corpus_m1_r_beta_path_contract_review_20260611.csv`

## S009

S009 has two distinct problems.

First, several 2026-06-11 abstentions were induced by the v4 path-direction
overlay. The overlay used the construct-pair order as if it were the active
directed path. For beta/path rows this is not valid. For example, a MASEM
construct pair such as `BI-EE` can correspond to a source-directed path
`EE->BI`. The 2026-06-09 run recovered several of these source-directed values,
while the later direction overlay made the same rows abstain.

Second, several S009 frozen rows behave like raw beta values even though their
reference source label says `beta_converted_peterson_brown`. Applying the
Peterson-Brown back-calculation from the frozen value does not recover the raw
source beta for those rows. The `FC-UB` row is worse: the retrieved source beta
does not match either the frozen value or the Peterson-Brown implied beta.

Conclusion for S009: do not fix this by adding stronger alias text. S009 needs
source-directed path metadata and a reference/scoring contract QA note before it
can be used as a full-corpus scoring gate.

## S010

S010 demonstrates the opposite pattern. For the rows where a raw source beta was
recovered, the raw beta generally matches the Peterson-Brown implied raw beta
from the frozen reference. The current scorer marks these rows wrong because the
model outputs raw beta while the frozen `r_value` is a converted effect-size
value.

The 2026-06-10 run also shows that IPMA/importance values can be mistakenly
used as path coefficients if the route instruction is too permissive. The
2026-06-11 v4 instruction correctly rejects IPMA/importance tables, but it still
does not solve the raw-beta versus converted-effect output contract.

Conclusion for S010: the next runnable version needs either explicit raw beta
and converted effect fields, or scorer-side conversion from raw beta when
`r_source=beta_converted_peterson_brown`. Without that, valid raw beta recovery
will continue to be scored as incorrect.

## Gate Decision

Full-corpus M1-R remains blocked.

The next defensible step is not a larger shard. It is a beta/path contract patch
that separates:

- source-directed path metadata from construct-pair order;
- raw source beta/path coefficient from Peterson-Brown converted effect value;
- path coefficient tables from IPMA, total-effect, indirect-effect, HTMT, and
  discriminant-validity tables;
- reference QA caveats from model retrieval errors.

## Recommended Next Action

Prepare a small `M1-R-BETA-PATH-CONTRACT-PROBE` before any larger M1-R run.
The probe should use source-directed path metadata and an output schema that
captures both raw beta and the converted effect-size value without exposing
human reference values or human-adjudicated source locators in the prompt.

The current 2026-06-11 table-retrieval smoke remains diagnostic only.
