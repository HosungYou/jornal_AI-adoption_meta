# Full-Corpus Step 5 Pre-Run Authorization Packet

Date: 2026-06-09

Status: prepared for researcher review. This packet does not authorize any
model execution.

## Prepared Artifacts

- `full_corpus_locked_output_template_20260609.csv`: 2,043 unlocked target task
  rows.
- `FULL_CORPUS_MODEL_PROCEDURE_RUN_MATRIX_20260609.csv`: planned model/procedure
  conditions.
- `FULL_CORPUS_LOCKED_OUTPUT_MANIFEST_20260609.csv`: checksum manifest for
  current pre-run artifacts.
- `../schemas/FULL_CORPUS_LOCKED_OUTPUT_SCHEMA_20260609.md`: post-freeze locked
  output schema and leakage boundary.
- `../../07_paper_c_harness_benchmark/00_manifest/source_rendering_chunking_manifest_20260609.csv`:
  source rendering/chunking policy placeholder.
- `../../07_paper_c_harness_benchmark/06_rerun_bundles/repeatability_subset_manifest_20260609.csv`:
  120-row repeatability subset with 40 rows from each denominator family.

## Run Matrix Summary

| Condition | Role | Status |
|---|---|---|
| `M1-R-SMOKE` | Small stratified raw-model preflight | Pending approval |
| `M1-R` | Primary raw model baseline | Pending approval |
| `M1-P` | Same-model stateful research harness/procedure contrast | Pending approval |
| `M2-R` | Cross-model raw comparison | Pending approval |
| `M3-R` | Optional third-family raw robustness check | Pending approval |

All model selectors remain `to verify` before execution. The matrix preserves
prior candidate families from legacy scaffold work, but final model selectors
must be checked and recorded on the run date.

## Approval Items

Before any model condition is run, the researcher must approve:

1. The first executable condition, recommended as `M1-R-SMOKE`.
2. Exact model selector and provider surface for `M1`.
3. Whether `M2-R` and optional `M3-R` are in scope for the first full-corpus
   comparison.
4. Budget cap for smoke and full-corpus runs.
5. Source rendering/chunking policy, including whether model prompts may receive
   human-adjudicated source locators. Current default: no.
6. Private raw-output storage path and share-safe output policy.
7. Whether the 120-row repeatability subset is accepted as frozen for repeated
   run stability checks.

## Non-Claims

- No post-freeze model run has been executed.
- No scoring rerun has been executed.
- No LLM accuracy, model comparison, procedure comparison, or MASEM
  substitution result is current.
- Legacy pre-full-corpus outputs remain scaffold evidence unless explicitly
  re-keyed and revalidated against the 2026-06-09 frozen reference.

## Recommended Next Decision

Approve or revise the pre-run matrix. If approved, the first executable unit
should be `M1-R-SMOKE`, not a full-corpus run.
