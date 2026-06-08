# Paper C Post-Freeze Model/Procedure Gate

Date: 2026-06-09

Status: Paper C may now move from scaffold to run-condition planning because the full 213-study human reference is frozen. This document does not authorize final model runs by itself.

## Human Reference Anchor

- `H`: `data/04_extraction/04_reference_standard_freeze/full_corpus_reference_standard_frozen_20260609.csv`
- Study status/corpus accounting: `data/04_extraction/04_reference_standard_freeze/full_corpus_reference_standard_study_status_frozen_20260609.csv`
- Caveat register: `data/04_extraction/04_reference_standard_freeze/full_corpus_reference_standard_freeze_caveat_register_20260609.csv`
- Paper C pointer artifact: `data/04_extraction/07_paper_c_harness_benchmark/01_human_reference_snapshot/full_corpus_reference_pointer_20260609.csv`

## Gate Decision

Paper C should use the full-corpus frozen reference as `H`, but it should not treat model scores as timeless model properties. Model, local wrapper, prompt/schema, source rendering, batching, retry behavior, and stateful-harness procedure are part of the condition.

## Minimum Design To Lock Before Running

| Condition | Minimum requirement |
|---|---|
| `M1-R` | One model-explicit raw extraction condition over the frozen task shell |
| `M1-P` | Same model selector with stateful research harness/provenance-preserving procedure |
| `M2-R` | One complete comparable raw cross-model condition if resources permit |
| Optional `M2-P` | Same procedure applied to M2 only after M1-P is stable |
| Stability subset | Stratified subset frozen before repeated runs |

## Primary Reporting Families

| Family | Role |
|---|---|
| Direct/source-reported correlations | Primary numeric extraction evidence |
| Latent/Fornell-Larcker construct correlations | Separate source-type denominator |
| Beta/path-converted rows | Secondary/sensitivity denominator |
| Caveat-bearing rows | Diagnostic and sensitivity overlay |
| Status-only studies | Corpus accounting, not target-row accuracy |
| HTMT exclusions | Caveat/accounting overlay; no HTMT-only target rows are scored |

## Required Pre-Run Artifacts

- Full-corpus locked-output template generated from `full_corpus_step5_task_unit_shell_20260609.csv`.
- Model/procedure run matrix with versioned selectors and provider/API/CLI surface.
- Prompt/schema version IDs.
- Source rendering/chunking manifest.
- Repeatability subset manifest.
- Private-output policy and share-safe summary plan.

## Next Action

Prepare the locked-output template and run matrix. Do not run final Paper C conditions until the researcher approves the model selectors, procedure contrast, and repeatability subset.
