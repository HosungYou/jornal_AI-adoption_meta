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
| 5 | `05_llm_masem_substitution/` | Post-freeze LLM comparison and MASEM substitution analyses | Source-rendered smoke/preflight runs completed; full source-rendering coverage clean; legacy pre-full-corpus RQ1-RQ3/OSF package preserved; full-corpus model runs and result claims remain authorization-gated |
| 6 | `06 coding by date/` | Date-stamped operational staging area for share-safe coding packets and transfer artifacts | Active |
| 99 | `99_archive/` | Historical files not used in the active workflow | Reference only |

## Current Stage

The project is currently past the post-freeze Step 5 source-materialization gate
after the full-corpus Step 4 freeze. The full 213-study source-anchored
adjudicated human reference standard is frozen with caveats preserved, and full
source-rendering coverage is now clean for the 194-study / 2,043-row target
shell. Model runs and result claims remain blocked until a specific
source-rendered model condition, exact model selector, and budget are explicitly
authorized.

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
  one S009 directed-value mismatch. Full-corpus model execution and result claims
  remain unauthorized pending beta/path retrieval disambiguation and specific
  run-condition approval.
- Step 5 shell/scoring harness is prepared. Clean model-explicit locked outputs
  are available for `codex:gpt-5.5`, `gemini:gemini-3-flash-preview`, and
  `claude:sonnet` across `0000-7858`. The earlier Claude Code/default-
  unspecified `0000-3999` rows are retained only as audit provenance after the
  2026-06-11 Sonnet backfill. RQ1-RQ3 task-family outputs and a MASEM
  substitution bridge were generated on 2026-06-11. A P0/P1 expert-review layer
  and deterministic substitution-input/pooled-correlation rerun were also
  generated on 2026-06-11. The local R/OpenMx/metaSEM environment is available,
  and all 746 P0/P1 pointer-only source rows have a PDF source-text audit layer.
  A deterministic sample-size reconciliation layer now fills numeric N for
  741/804 legacy rerun rows from the 2026-06-09 frozen full-corpus reference,
  with 63 rows excluded from N-weighted TSSEM/MASEM weighting unless later
  source checking supplies numeric N. Final SEM substitution-stability claims
  still require the full R/metaSEM TSSEM Stage 1/Stage 2 rerun, and they must
  not use one 8,783-row denominator. This legacy package remains superseded by
  the 2026-06-09 full-corpus freeze for final Paper B claim construction.

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
- Step 5 PDF source-text audit:
  `05_llm_masem_substitution/results/pdf_source_text_audit_20260611/PAPER2_POINTER_ONLY_PDF_SOURCE_TEXT_AUDIT_20260611.md`
- Step 5 R/metaSEM readiness check:
  `05_llm_masem_substitution/results/r_masem_readiness_20260611/PAPER2_R_MASEM_READINESS_20260611.md`
- Step 5 N-reconciled R/metaSEM readiness check:
  `05_llm_masem_substitution/results/r_masem_readiness_n_reconciled_20260611/PAPER2_R_MASEM_READINESS_20260611.md`
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
