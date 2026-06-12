# Data Extraction Workspace

This folder follows the Paper B validation sequence. Keep active work in the
numbered folders below.

## Active Structure

| Step | Folder | Purpose | Current status |
|---:|---|---|---|
| 0 | `00_protocol/` | Coding manual, PDF tracker, calibration files, generation scripts | Active |
| 1 | `01_raw_human_coder_data_freeze/` | Raw independent human coder workbooks and freeze candidates | Phase 1 complete; Phase 2 returned raw workbooks and freeze candidates preserved |
| 2 | `02_pre_adjudication_disagreement/` | Pairwise comparison workbooks and raw human-human disagreement summaries | Phase 1 comparison workbook exists; Phase 2 queue and combined Phase 1+2 queues generated |
| 3 | `03_source_document_adjudication/` | Source-check decisions and adjudication logs | Phase 1 and Phase 2 adjudication in progress |
| 4 | `04_reference_standard_freeze/` | Frozen source-anchored adjudicated human reference standard | Full 213-study corpus frozen with retained caveats on 2026-06-09 |
| 5 | `05_llm_masem_substitution/` | Post-freeze LLM comparison and MASEM substitution analyses | Source-rendered smoke/preflight runs, a scored 90-row bounded M1-R shard, a completed source-packet-required 2,043-row full-corpus M1-R run, a bounded core-6 TSSEM diagnostic, and a derived 804-row N-complete MASEM input exist; all-construct/all-row SEM claims remain gated by the final TSSEM/MASEM specification and source-type boundaries |
| 6 | `06 coding by date/` | Date-stamped operational staging area for share-safe coding packets and transfer artifacts | Active |
| 99 | `99_archive/` | Historical files not used in the active workflow | Reference only |

## Current Stage

The project is currently past the post-freeze Step 5 full-corpus `M1-R`
execution gate after the full-corpus Step 4 freeze. The full 213-study
source-anchored adjudicated human reference standard is frozen with caveats
preserved, and full source-rendering coverage is clean for the 194-study /
2,043-row target shell. A 90-row bounded source-rendered `M1-R` shard was
executed and scored as staged diagnostic evidence, then the dedicated
source-packet-required 2,043-row full-corpus `M1-R` expansion completed across
nine shards with 0 duplicate task IDs and 0 model CLI failures. The full-corpus
outputs are scored through the exception-aware wrapper and may be interpreted
only by denominator family and contract-aware exception status. A bounded core-6
complete-case R/metaSEM TSSEM diagnostic has also been run for the Paper1
human-reference baseline versus the expert-reviewed LLM-assisted primary input.
The derived 804-row MASEM rerun input now has numeric N for every row after
approved PDF source-supported N overrides. All-construct/all-row SEM result
claims remain gated by the final TSSEM/MASEM specification, matrix sparsity, and
source-type boundaries.

The 2026-06-05 tiered Paper1/Paper2 package remains preserved as a legacy
pre-full-corpus evidence package. Its clean model-explicit `0000-7858` locked
outputs, RQ1-RQ3 summaries, deterministic substitution-input rerun, PDF
source-text audit, R/metaSEM readiness check, manuscript draft, and OSF public
archive are retained for reproducibility, but they are not the final
full-corpus Step 5 accuracy/substitution claim.

- Step 1 is complete for Phase 1 raw coder packages.
- Step 2 exists as the Phase 1 pairwise comparison workbook.
- Step 1 is complete for Phase 2 returned raw workbooks and separate freeze
  candidates.
- Step 2 has a Phase 2 derived pre-adjudication disagreement queue.
- Step 2 also has combined Phase 1+2 derived pre-adjudication queues for the
  full 213-study Paper B validation corpus.
- Step 3 has source-check and source-value decisions documented for selected
  Phase 2 high-priority items.
- Step 4 has a scoped frozen Phase 2 source-adjudicated package and a full
  213-study frozen reference package authorized on 2026-06-09.
- Step 4 is complete for the full-corpus source-anchored adjudicated human
  reference standard, with caveats retained in the frozen package.
- Step 5 has a post-freeze gate, full-corpus task shell, locked-output
  template, run matrix, repeatability subset, smoke/preflight outputs, and a
  source PDF materialization action package. The full materialization/readability
  sweep and full source-rendering coverage audit are now clean: 191/191
  materialization-gap studies, 2,025/2,025 gap rows, 194/194 source-rendered
  target studies, and 2,043/2,043 target rows. A balanced 30-row full-coverage
  source-rendered smoke has also been locked, diagnostically scored, and
  prompt/path reviewed. A 40-row revised source-rendered smoke has now been
  locked and diagnostically scored with route violations=0. A follow-up 25-row
  table-retrieval smoke unblocked S003 direct-r/FLC retrieval at 10/10 correct,
  but S009/S010 true beta/path controls remain partial with 7/25 abstentions and
  one S009 directed-value mismatch. The 2026-06-11 beta/path exception layer is
  now consumed by the full-corpus scoring wrapper. The required private source
  packets for the 10-study bounded shard were regenerated in ignored private
  storage, and a 90-row `M1-R` shard was locked and scored with
  `model_cli_error=0`, source quote policy violations=0, and denominator-family
  generic numeric scoring of direct/source-r 15/30, latent/construct
  correlation 27/30, and secondary beta/path 13/30. This is staged diagnostic
  evidence only. The dedicated 2,043-row full-corpus `M1-R` expansion was then
  locked and scored through the exception-aware gate on 2026-06-12, with 0
  duplicate task IDs, 0 model CLI failures, and denominator-family scoring
  separated for latent/source-flagged, direct/source-r, and secondary
  beta/path-converted rows. A bounded core-6 complete-case TSSEM diagnostic was
  also run on PE, EE, SI, FC, BI, and UB with 15 complete-case studies; Stage 1
  REM and Stage 2 converged for both the Paper1 human-reference baseline and the
  expert-reviewed LLM-assisted primary input, with maximum pooled-r delta
  0.00000000. All-construct/all-row SEM result claims remain gated.
- Step 5 shell/scoring harness is prepared. Clean model-explicit locked outputs
  are available for `codex:gpt-5.5`, `gemini:gemini-3-flash-preview`, and
  `claude:sonnet` across `0000-7858`. The earlier Claude Code/default-
  unspecified `0000-3999` rows are retained only as audit provenance after the
  2026-06-11 Sonnet backfill. RQ1-RQ3 task-family outputs and a MASEM
  substitution bridge were generated on 2026-06-11. A P0/P1 expert-review layer
  and deterministic substitution-input/pooled-correlation rerun were also
  generated on 2026-06-11. The local R/OpenMx/metaSEM environment is available,
  and all 746 P0/P1 pointer-only source rows have a PDF source-text audit layer.
  A deterministic sample-size reconciliation layer fills numeric N for 741/804
  legacy rerun rows from the 2026-06-09 frozen full-corpus reference, and the
  approved PDF source check supplies derived source-supported N for the
  remaining 63 rows. The current derived input is therefore N-complete, but the
  bounded core-6 TSSEM diagnostic still supports only subset stability. Final
  all-construct/all-row SEM substitution claims require the final approved
  TSSEM/MASEM specification and an explicit ANX-TRU/source-type boundary; they
  must not use one 8,783-row denominator. This legacy package remains
  superseded by the 2026-06-09 full-corpus freeze for final Paper B claim
  construction.

For the combined Phase 1+2 Paper B validation corpus, Phase 2 uses R1+R4 for
57 studies and R2+R3 for 56 studies. Raw returned workbooks are preserved
separately from freeze candidates so that structural repairs, status
normalization, and source-check notes do not overwrite original coder returns.
Phase 0 calibration rows and historical `Phase 2: Single` rows in the Phase 1
workbooks are excluded from the combined analysis.

## Active Files

- Canonical manual: `00_protocol/AI_Adoption_MASEM_Coding_Manual_v2.md`
- Shareable manual DOCX: `00_protocol/AI_Adoption_MASEM_Coding_Manual_v2.docx`
- Package generator: `00_protocol/scripts/generate_coder_packages.py`
- Phase 1 raw workbooks: `01_raw_human_coder_data_freeze/phase1/coder_packages/`
- Phase 2 distribution workbooks:
  `01_raw_human_coder_data_freeze/phase2/coder_packages/`
- Phase 2 returned raw workbooks:
  `01_raw_human_coder_data_freeze/phase2/returned_raw/`
- Phase 2 freeze candidates:
  `01_raw_human_coder_data_freeze/phase2/freeze_candidates/`
- Phase 2 return manifest:
  `01_raw_human_coder_data_freeze/phase2/RETURN_MANIFEST_20260525.md`
- Phase 2 pre-adjudication disagreement queue:
  `02_pre_adjudication_disagreement/phase2/derived/phase2_pairwise_disagreement_long_20260525.csv`
- Combined Phase 1+2 pre-adjudication meeting queue:
  `02_pre_adjudication_disagreement/combined/derived/combined_correlation_review_queue_20260525.csv`
- Combined Phase 1+2 all-coding long table:
  `02_pre_adjudication_disagreement/combined/derived/combined_coder_values_long_20260525.csv`
- Combined Phase 1+2 disagreement summary:
  `02_pre_adjudication_disagreement/combined/derived/combined_pairwise_disagreement_summary_20260525.csv`
- Phase 2 PDF source-check report:
  `03_source_document_adjudication/phase2/phase2_exclusion_source_check_20260525.md`
- 2026-06-05 source adjudication decisions:
  `03_source_document_adjudication/phase2/source_adjudication_decisions_20260605.csv`
- 2026-06-05 reference freeze note:
  `04_reference_standard_freeze/paper2_reference_standard_freeze_note.md`
- 2026-06-05 workbook mutation manifest:
  `04_reference_standard_freeze/workbook_mutation_manifest_20260605.csv`
- 2026-06-05 checksum manifest:
  `04_reference_standard_freeze/CHECKSUMS_TIERED_FREEZE_20260605.csv`
- 2026-06-11 Paper B canonical reference/model-framing decision:
  `../../docs/06_decisions/2026-06-11_Paper_B_Canonical_Reference_and_Model_Framing.md`
- Step 5 RQ1 extraction-validity output:
  `05_llm_masem_substitution/results/PAPER2_RQ1_EXTRACTION_VALIDITY_20260611.md`
- Step 5 RQ2 error-taxonomy/source-condition output:
  `05_llm_masem_substitution/results/PAPER2_RQ2_ERROR_TAXONOMY_SOURCE_CONDITIONS_20260611.md`
- Step 5 RQ3 triage/cross-model sensitivity output:
  `05_llm_masem_substitution/results/PAPER2_RQ3_TRIAGE_CROSS_MODEL_SENSITIVITY_20260611.md`
- Step 5 MASEM substitution bridge:
  `05_llm_masem_substitution/results/PAPER2_MASEM_SUBSTITUTION_BRIDGE_20260611.md`
- Step 5 P0/P1 expert-review layer:
  `05_llm_masem_substitution/results/PAPER2_P0_P1_EXPERT_REVIEW_20260611.md`
- Step 5 deterministic MASEM substitution-input rerun:
  `05_llm_masem_substitution/results/PAPER2_MASEM_SUBSTITUTION_RERUN_20260611.md`
- Step 5 MASEM sample-size reconciliation:
  `05_llm_masem_substitution/results/PAPER2_MASEM_SAMPLE_SIZE_RECONCILIATION_20260611.md`
- Step 5 PDF-supported N override:
  `05_llm_masem_substitution/results/PAPER2_MASEM_SAMPLE_SIZE_PDF_OVERRIDE_20260612.md`
- Step 5 N-complete R/metaSEM readiness check:
  `05_llm_masem_substitution/results/r_masem_readiness_n_pdf_override_20260612/PAPER2_R_MASEM_READINESS_20260612.md`
- Step 5 matrix/source-type boundary audit:
  `05_llm_masem_substitution/results/PAPER2_MASEM_MATRIX_IDENTIFICATION_AUDIT_20260612.md`
- Step 5 ANX-TRU source-type panel:
  `05_llm_masem_substitution/results/PAPER_A_ANX_TRU_SOURCE_TYPE_PANEL_20260612.md`
- Step 5 full-corpus M1-R expansion gate:
  `05_llm_masem_substitution/results/FULL_CORPUS_M1_R_EXPANSION_GATE_20260612.md`
- Step 5 full-corpus M1-R dedicated manifest:
  `05_llm_masem_substitution/locked_outputs/FULL_CORPUS_M1_R_FULL_RUN_MANIFEST_20260612.csv`
- Step 5 full-corpus M1-R shard commands:
  `07_paper_c_harness_benchmark/06_rerun_bundles/run_full_corpus_m1r_expansion_20260612.sh`
- Step 5 full-corpus M1-R locked outputs:
  `05_llm_masem_substitution/locked_outputs/model_runs/paper_b_full_corpus_m1_raw_full_0000_0249_20260612.csv`
  through
  `05_llm_masem_substitution/locked_outputs/model_runs/paper_b_full_corpus_m1_raw_full_2000_2042_20260612.csv`
- Step 5 full-corpus M1-R scoring outputs:
  `05_llm_masem_substitution/results/paper_b_full_corpus_m1_raw_full_scored_20260612.csv`
  and
  `05_llm_masem_substitution/results/paper_b_full_corpus_m1_raw_full_exception_layer_scored_20260612.csv`
- Step 5 full-corpus M1-R status and next-work memo:
  `05_llm_masem_substitution/results/PAPER_B_STEP5_FULL_CORPUS_M1R_STATUS_AND_NEXT_WORK_20260612.md`
- Step 5 bounded M1-R shard preflight:
  `05_llm_masem_substitution/results/FULL_CORPUS_M1_R_BOUNDED_SHARD_PREFLIGHT_20260611.md`
- Step 5 bounded M1-R shard task bundle:
  `07_paper_c_harness_benchmark/06_rerun_bundles/source_rendered_bounded_m1r_shard_task_ids_20260611.csv`
- Step 5 bounded M1-R locked output:
  `05_llm_masem_substitution/locked_outputs/model_runs/paper_b_full_corpus_m1_raw_bounded_shard_0090_20260611.csv`
- Step 5 bounded M1-R shard status:
  `05_llm_masem_substitution/results/FULL_CORPUS_M1_R_BOUNDED_SHARD_STATUS_20260611.md`
- Step 5 PDF source-text audit:
  `05_llm_masem_substitution/results/pdf_source_text_audit_20260611/PAPER2_POINTER_ONLY_PDF_SOURCE_TEXT_AUDIT_20260611.md`
- Step 5 R/metaSEM readiness check:
  `05_llm_masem_substitution/results/r_masem_readiness_20260611/PAPER2_R_MASEM_READINESS_20260611.md`
- Step 5 N-reconciled R/metaSEM readiness check:
  `05_llm_masem_substitution/results/r_masem_readiness_n_reconciled_20260611/PAPER2_R_MASEM_READINESS_20260611.md`
- Step 5 bounded TSSEM substitution diagnostic:
  `05_llm_masem_substitution/results/r_tssem_substitution_20260611/PAPER2_TSSEM_SUBSTITUTION_DIAGNOSTIC_20260611.md`
- Paper B public repository archive folder:
  `../../paper_b/public_data_repository_20260611/`
- Paper B OSF public repository:
  `https://osf.io/mkrgd/overview`
- Paper B manuscript methods/results draft:
  `../../paper_b/manuscript/PAPER_B_METHODS_RESULTS_DRAFT_20260611.md`
- Active R4 raw workbook:
  `01_raw_human_coder_data_freeze/phase1/coder_packages/R4/AI_Adoption_MASEM_Coding_v3_R4.xlsx`
  promoted from the 2026-04-23 R4 file
- Phase 1 comparison workbook:
  `02_pre_adjudication_disagreement/phase1/AI_Adoption_Phase1_Pairwise_Comparison_R1R2_R3R4_20260424.xlsx`
- R1-R4 comparison playbook:
  `02_pre_adjudication_disagreement/RATER_COMPARISON_PLAYBOOK.md`
- Phase 1 adjudication decisions:
  `03_source_document_adjudication/phase1/decision_log_20260424.md`
- Local source PDFs, if available:
  `03_source_document_adjudication/source_pdfs/` (ignored by Git)
- Workflow status log: `WORKFLOW_STATUS_LOG.md`
- Date-stamped coding transfer area:
  `06 coding by date/`
- Phase 2 R1 Pair C 17-study working coding notes:
  `06 coding by date/2026-05-06/r1_pairc_17_study_coding_notes.md`

## Removed From Active Structure

Duplicated coder-package manual DOCX files were removed from Git. Use the
canonical manual in `00_protocol/` instead. Historical screening/progress files,
older R4 workbook snapshots, source PDF variants, and duplicated annotated guides
were moved to `99_archive/`.
