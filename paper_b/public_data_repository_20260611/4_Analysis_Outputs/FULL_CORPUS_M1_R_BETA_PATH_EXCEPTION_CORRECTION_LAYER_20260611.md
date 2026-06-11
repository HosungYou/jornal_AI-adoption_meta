# Full-Corpus M1-R Beta/Path Exception-Correction Layer

Date: 2026-06-11

## Scope

This artifact records the post-freeze beta/path exception-correction layer
created after the bounded S009/S010 source-reference QA. It is a scorer/gate
policy layer, not a frozen-reference edit.

The layer must be consumed before any larger `M1-R` shard is interpreted as a
full-corpus accuracy result.

Layer artifact:

- `data/04_extraction/05_llm_masem_substitution/results/full_corpus_m1_r_beta_path_exception_correction_layer_20260611.csv`

Input QA artifact:

- `data/04_extraction/05_llm_masem_substitution/results/full_corpus_m1_r_beta_path_source_reference_qa_20260611.csv`

## Boundary

- Frozen reference files are unchanged.
- No human reference values are added to model prompts.
- Private source-packet text is not reproduced or committed.
- This layer does not authorize a larger model run by itself.

## Layer Counts

| Policy | Rows | Step 5 handling |
|---|---:|---|
| `reference_contract_caveat_no_in_place_freeze_change` | 8 | Exclude from the generic full-accuracy denominator. These S009 rows may only be reported separately as raw-beta retrieval/reference-contract caveats unless a researcher-authorized correction layer later changes the scoring contract. |
| `manual_source_reference_adjudication_required_no_in_place_freeze_change` | 1 | Exclude from all accuracy gates until S009 `FC-UB` is manually adjudicated or explicitly excluded. |
| `contract_aware_converted_effect_scoring_allowed_after_layer_consumed` | 2 | Exclude from the raw `model_answer_normalized` generic scorer; include only under a contract-aware beta/path scorer that scores `converted_effect_value` against the frozen value. |
| `exclude_until_explicit_structural_path_evidence_or_reference_correction` | 4 | Exclude until explicit structural path evidence is available or a post-freeze reference correction/exception decision is authorized. IPMA/importance-like candidates remain invalid path evidence. |

## Scorer Instructions

The generic full-accuracy scorer must not treat these 15 rows as ordinary
numeric rows.

For S009 raw-beta-confirmed rows, the model can be credited only in a separate
diagnostic/reference-contract caveat analysis. These rows should not enter the
converted-effect accuracy denominator while the frozen row label and value
contract remain inconsistent.

For S009 `FC-UB`, no score should be assigned until manual source/reference
adjudication resolves whether the row should be corrected, excluded, or retained
with an explicit caveat.

For S010 `PE->BI` and `BI->UB`, a contract-aware beta/path scorer may score
`converted_effect_value` against the frozen value after this exception layer is
loaded. The raw beta field is evidence that the source path was recovered; it is
not the final converted-effect score.

For the four S010 no-explicit-path rows, the scorer must not substitute IPMA,
importance, total-effect, indirect-effect, HTMT, or discriminant-validity values
for structural path coefficients.

## Gate Decision

Full-corpus `M1-R` remains blocked until the Step 5 scoring gate explicitly
loads or enforces this exception-correction layer. The next implementation task
is to wire this layer into the Step 5 scoring workflow or scorer wrapper before
any larger shard is run or interpreted.
