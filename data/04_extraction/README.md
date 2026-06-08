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
| 5 | `05_llm_masem_substitution/` | Post-freeze LLM comparison and MASEM substitution analyses | Requires separate post-freeze run/analysis gate for new full-corpus claims |
| 6 | `06 coding by date/` | Date-stamped operational staging area for share-safe coding packets and transfer artifacts | Active |
| 99 | `99_archive/` | Historical files not used in the active workflow | Reference only |

## Current Stage

The project is currently between Step 3 adjudication and full-corpus Step 4
freeze. Phase 2 returned workbooks are now preserved, and a scoped Step 4 freeze
package has been prepared for the source-adjudicated Phase 2 high-priority
decisions. This scoped package does not mean the full 213-study
source-anchored adjudicated human reference standard is complete.

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
- Step 5 must use the frozen full-corpus reference only after a separate
  post-freeze run/analysis gate confirms the intended model/procedure scope.

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
