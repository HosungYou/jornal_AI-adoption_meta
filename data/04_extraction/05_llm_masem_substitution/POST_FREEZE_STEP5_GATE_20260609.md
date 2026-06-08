# Post-Freeze Step 5 Gate

Date: 2026-06-09

Status: gate opened after full-corpus Step 4 freeze. No new model run, scoring rerun, LLM accuracy claim, or MASEM substitution claim is authorized by this gate document.

## Reference Now In Scope

- Frozen reference rows: `../04_reference_standard_freeze/full_corpus_reference_standard_frozen_20260609.csv`
- Frozen study status: `../04_reference_standard_freeze/full_corpus_reference_standard_study_status_frozen_20260609.csv`
- Caveat register: `../04_reference_standard_freeze/full_corpus_reference_standard_freeze_caveat_register_20260609.csv`
- Freeze authorization: `../04_reference_standard_freeze/full_corpus_reference_standard_freeze_authorization_20260609.md`

## Gate Decision

1. The full-corpus frozen reference is now the required reference for any new Paper B full-corpus Step 5 claim.
2. Pre-freeze `Paper2` locked-output/scoring artifacts remain legacy/scaffold evidence unless explicitly re-keyed and revalidated against the 2026-06-09 frozen reference.
3. The next executable unit is not a model run; it is a locked-output template rebuild from `full_corpus_step5_task_unit_shell_20260609.csv` plus a model/procedure run matrix.
4. Step 5 reporting must use denominator-family and caveat overlays, not one overall accuracy denominator.
5. Paper C model-by-procedure claims require a separate run-condition gate that fixes model selectors, raw/procedure conditions, source rendering, prompt/schema versions, and repeatability subset.

## Prepared Gate Artifacts

- `FULL_CORPUS_POST_FREEZE_INPUT_MANIFEST_20260609.csv`
- `full_corpus_step5_task_unit_shell_20260609.csv`
- `full_corpus_step5_status_only_shell_20260609.csv`

## Task Shell Counts

- Target-row task units: 2043
- Status-only corpus-accounting records: 19
- Included frozen-reference studies: 194
- Excluded/no-target frozen status studies: 17
- Duplicate-source frozen status studies: 2
- HTMT caveat overlay rows: 23 (not a target denominator family; HTMT-only values remain excluded)

## Denominator Families

| Denominator family | Rows |
|---|---:|
| `primary_direct_r_or_source_reported_correlation` | 697 |
| `primary_latent_or_construct_correlation_with_source_type_flag` | 931 |
| `secondary_beta_or_path_converted_effect_size` | 415 |

## Scoring Eligibility

| Scoring eligibility | Rows |
|---|---:|
| `eligible_after_locked_llm_output` | 697 |
| `eligible_after_locked_llm_output_with_source_type_denominator` | 1346 |

## Evidence Families

| Evidence family | Rows |
|---|---:|
| `beta_or_path_converted_effect_size` | 415 |
| `direct_r_effect_size_extraction` | 697 |
| `latent_or_construct_correlation` | 931 |

## Locked Model/Procedure Scope To Decide Before Execution

Recommended minimum gate for Paper B Step 5:

- Rebuild the locked-output template from the 2,043-row full-corpus task shell.
- Use one model-explicit raw extraction condition as the first post-freeze smoke run.
- Add cross-model comparison only after one condition passes schema, manifest, and scoring checks.
- Keep beta/path-converted and latent/Fornell-Larcker rows in separate denominator families.
- Treat status-only studies as corpus-accounting records, not target task rows.

Recommended minimum gate for Paper C:

- `H`: full-corpus frozen reference.
- `M1-R`: raw model extraction with versioned model selector and full run provenance.
- `M1-P`: same model mediated by a stateful research harness/procedure.
- `M2-R`: at least one clearly versioned cross-model raw condition if resources permit a complete comparable run.
- Repeatability subset: stratified rows from direct r, beta/path, latent/Fornell-Larcker, caveat-bearing rows, and high-disagreement studies; exact row IDs to be frozen before reruns.

## Non-Claims

- Do not report old `8783` task-unit results as final full-corpus accuracy.
- Do not merge denominator families into one overall accuracy number.
- Do not start Paper C final analysis from raw model outputs that lack frozen model/procedure provenance.
- Do not commit raw model transcripts, private PDFs, private source text, or local-only rerun bundles.

## Next Action

Create the post-freeze locked-output template and model/procedure run matrix from the task shell, then request explicit authorization before running any model condition.
