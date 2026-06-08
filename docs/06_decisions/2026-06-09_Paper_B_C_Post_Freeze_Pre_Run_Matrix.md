# Paper B/C Post-Freeze Pre-Run Matrix

Date: 2026-06-09

## Decision

The post-freeze Step 5 locked-output template and Paper C model/procedure run
matrix are prepared, but no model condition is authorized yet.

## Rationale

The full-corpus source-anchored adjudicated human reference standard is frozen,
but the old `Paper2` model-output artifacts predate the full-corpus freeze. A
new post-freeze execution needs a template, run matrix, source rendering policy,
and repeatability subset before any model output can be treated as current.

## Prepared Files

- `data/04_extraction/05_llm_masem_substitution/locked_outputs/full_corpus_locked_output_template_20260609.csv`
- `data/04_extraction/05_llm_masem_substitution/locked_outputs/FULL_CORPUS_MODEL_PROCEDURE_RUN_MATRIX_20260609.csv`
- `data/04_extraction/05_llm_masem_substitution/locked_outputs/FULL_CORPUS_LOCKED_OUTPUT_MANIFEST_20260609.csv`
- `data/04_extraction/05_llm_masem_substitution/locked_outputs/FULL_CORPUS_PRE_RUN_AUTHORIZATION_PACKET_20260609.md`
- `data/04_extraction/05_llm_masem_substitution/schemas/FULL_CORPUS_LOCKED_OUTPUT_SCHEMA_20260609.md`
- `data/04_extraction/07_paper_c_harness_benchmark/00_manifest/source_rendering_chunking_manifest_20260609.csv`
- `data/04_extraction/07_paper_c_harness_benchmark/06_rerun_bundles/repeatability_subset_manifest_20260609.csv`
- `scripts/llm_scoring_20260606/prepare_post_freeze_step5_artifacts.py`

## Verification Counts

- Locked-output template rows: 2,043
- Locked template status: 2,043 `template_unlocked`
- Model answer cells populated: 0
- Repeatability subset rows: 120
- Repeatability denominator split: 40 direct/source-reported, 40 latent/source
  type, 40 beta/path-converted
- Run matrix conditions: `M1-R-SMOKE`, `M1-R`, `M1-P`, `M2-R`, optional `M3-R`

## Boundary

This decision authorizes planning artifacts only. The next step requires a
researcher decision on the first executable condition, exact model selector,
budget cap, source rendering/chunking details, and private-output storage.
