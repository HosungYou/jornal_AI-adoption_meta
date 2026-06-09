# Full-Corpus Step 5 Pre-Run Authorization Packet

Date: 2026-06-09

Status: `M1-R-SMOKE` was researcher-authorized and executed. This packet does
not authorize any full-corpus model execution.

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
| `M1-R-SMOKE` | Small stratified raw-model preflight | Authorized, executed, and manifest-registered |
| `M1-R` | Primary raw model baseline | Pending approval |
| `M1-P` | Same-model stateful research harness/procedure contrast | Pending approval |
| `M2-R` | Cross-model raw comparison | Pending approval |
| `M3-R` | Optional third-family raw robustness check | Pending approval |
| `M1-R-SOURCE-SMOKE` | Private source-packet prompt/export preflight | Authorized, executed, and manifest-registered |

All model selectors remain `to verify` before execution. The matrix preserves
prior candidate families from legacy scaffold work, but final model selectors
must be checked and recorded on the run date.

Update after researcher approval: `M1-R-SMOKE` was locked to
`codex:gpt-5.5` through `codex-cli 0.137.0` and executed on 30 stratified
post-freeze rows. The remaining full-corpus/procedure/model-comparison rows are
still not authorized.

Second update: `M1-R-SOURCE-SMOKE` was executed for the current PDF-available
subset (`S021`, `S056`, `S092`) using private source packets with source quotes
suppressed in committed output. This validates the source-packet prompt/export
path only; it does not authorize full-corpus execution.

Third update: a full target-shell source coverage audit found archive filename
coverage for all 194 target studies, but local text rendering still produced
private packets for only 3 studies / 18 target rows. The remaining 191 studies /
2,025 target rows failed local PDF read/materialization with `Operation timed
out`. This blocks full-corpus `M1-R` until the archive PDFs are locally
materialized or equivalent share-safe source renderings are available.

## Authorization Decision Recorded

The researcher approved Codex's recommended next step on 2026-06-09:

1. First executable condition: `M1-R-SMOKE` only.
2. Exact provider/model surface for the smoke: `openai`; `codex:gpt-5.5`.
3. Local CLI/version lock: `codex-cli 0.137.0; model_selector=gpt-5.5`.
4. Budget/scope: smoke-only 30-row preflight; no full-corpus run authorized.
5. Source rendering/chunking policy: no human reference value and no
   human-adjudicated source locator in prompts.
6. Private raw-output policy: raw transcripts not committed; locked structured
   CSV may be registered.
7. Repeatability subset: the 120-row 40/40/40 subset remains frozen for later
   repeated-run stability checks.

## Smoke Execution Evidence

- Run ID: `paper_b_full_corpus_m1_raw_smoke_20260609`
- Locked output:
  `data/04_extraction/05_llm_masem_substitution/locked_outputs/model_runs/paper_b_full_corpus_m1_raw_smoke_20260609.csv`
- Status summary:
  `data/04_extraction/05_llm_masem_substitution/results/FULL_CORPUS_M1_R_SMOKE_STATUS_20260609.md`
- Rows: 30, balanced 10/10/10 across denominator families.
- `model_cli_error` rows: 0.
- Manifest registration: true.
- Interpretation: all 30 rows abstained with `insufficient_evidence` because
  this smoke used the current task stubs without source-document chunks.

## Source-Rendered Smoke Evidence

- Run ID: `paper_b_full_corpus_m1_raw_source_rendered_smoke_20260609`
- Locked output:
  `data/04_extraction/05_llm_masem_substitution/locked_outputs/model_runs/paper_b_full_corpus_m1_raw_source_rendered_smoke_20260609.csv`
- Status summary:
  `data/04_extraction/05_llm_masem_substitution/results/FULL_CORPUS_M1_R_SOURCE_RENDERED_SMOKE_STATUS_20260609.md`
- Source rendering manifest:
  `data/04_extraction/07_paper_c_harness_benchmark/00_manifest/source_rendering_available_pdf_manifest_20260609.csv`
- Rows: 6, across `S021`, `S056`, and `S092`.
- Denominator family: `secondary_beta_or_path_converted_effect_size` only.
- `model_cli_error` rows: 0.
- Source quote policy violations: 0.
- Nonblank model answers: 6.
- Nonblank committed source quotes: 0.
- Manifest registration: true.

## Full Coverage Materialization Audit

- Coverage manifest:
  `data/04_extraction/07_paper_c_harness_benchmark/00_manifest/source_rendering_full_coverage_manifest_20260609.csv`
- Coverage status:
  `data/04_extraction/07_paper_c_harness_benchmark/00_manifest/SOURCE_RENDERING_FULL_COVERAGE_STATUS_20260609.md`
- Target studies audited: 194.
- Archive filename coverage: 194 studies.
- Private packets successfully rendered: 3 studies / 18 target rows.
- Local rendering/materialization failures: 191 studies / 2,025 target rows.
- Dominant failure mode: `Operation timed out` while reading OneDrive PDF files.
- Interpretation: source files appear indexed in the archive, but they are not
  currently usable as local prompt inputs for full-corpus model execution.

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

- No post-freeze full-corpus model run has been executed.
- No scoring rerun has been executed.
- No LLM accuracy, model comparison, procedure comparison, or MASEM
  substitution result is current.
- Legacy pre-full-corpus outputs remain scaffold evidence unless explicitly
  re-keyed and revalidated against the 2026-06-09 frozen reference.

## Recommended Next Decision

Resolve the local OneDrive PDF materialization/readability blocker before any
full-corpus `M1-R` run. A share-safe materialization action package now exists
for the 191 blocked studies / 2,025 blocked target rows:

- `data/04_extraction/07_paper_c_harness_benchmark/00_manifest/source_pdf_materialization_gap_manifest_20260609.csv`
- `data/04_extraction/07_paper_c_harness_benchmark/06_rerun_bundles/source_pdf_materialization_batches_20260609.csv`
- `data/04_extraction/07_paper_c_harness_benchmark/00_manifest/SOURCE_PDF_MATERIALIZATION_PLAN_20260609.md`
- `scripts/llm_scoring_20260606/check_source_pdf_materialization.py`

After the relevant PDFs are locally materialized, rerun the checker and then
rerun source rendering coverage. A balanced source-rendered smoke becomes
eligible only after rendered private packets cover the intended target scope.

Follow-up checker status: the full 191-study materialization gap was checked
again after attempting to identify a CLI hydration route. All 191 studies still
returned `not_materialized_or_read_timeout`, and the available local CLI surface
did not execute the OneDrive `MarkPinned` context action. The next gate remains
OneDrive/Finder local materialization followed by checker and source-rendering
coverage reruns.
