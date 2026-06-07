# Extraction Workflow Status Log

## Current Status Snapshot

**Date:** 2026-06-08

**Current stage:** Step 4 has produced a source-anchored tiered reference
freeze layer for the Paper1/Paper2 working package. Source-reviewed blocker
studies are recorded in the adjudication decision log, Paper1 primary direct-r
model input is separated from source-statistic/sensitivity/trace rows, and
Paper2 task units are frozen by scoring eligibility and denominator family.
Separately, 2026-06-08 Phase 2 source-review and source-value decisions were
recorded for S014/S021/S056/S092/S121/S195/S202/S206 and a scoped Phase 2
source-adjudicated freeze package was prepared. This scoped package does not
mean the full 213-study Paper B reference standard is complete.

**Do not claim Step 5 as complete.** The locked-output shell and scoring harness
exist, and Claude/Gemini smoke plus staged full-run locked outputs have been
scored. Full LLM comparison or MASEM substitution still requires model-explicit
locked outputs across the planned denominator families before any final
accuracy or substitution result is reported.

## Five-Step Workflow

| Step | Name | Entry criterion | Exit criterion | Status |
|---:|---|---|---|---|
| 1 | Raw human coder data freeze | Independent coder workbooks are submitted and preserved | Raw files are read-only; no consensus overwrites | Phase 1 complete; Phase 2 returned raw workbooks and freeze candidates preserved |
| 2 | Pre-adjudication human-human disagreement analysis | Raw coder data are frozen | Pairwise differences summarized by field, study, pair, and numeric tolerance | Phase 1 workbook exists; Phase 2 and combined Phase 1+2 derived queues generated from freeze candidates/raw packages |
| 3 | Source-document adjudication | Pairwise differences are available | Every discrepancy has a source-anchored decision and rationale | Paper1/Paper2 blocker studies resolved into tiered decisions for the 2026-06-05 freeze packet; full Phase 1+2 corpus adjudication still in progress |
| 4 | Reference standard freeze | Adjudication is complete | Frozen reference file and freeze log are committed | Tiered source-anchored reference layer created 2026-06-05; scoped Phase 2 package frozen 2026-06-08; full 213-study reference not complete |
| 5 | LLM comparison + MASEM substitution | Reference standard is frozen | LLM accuracy, triage, and substitution outputs are generated | Shell/scoring harness prepared; Codex GPT-5.5 clean full `0000-7858` scored; Claude default-unspecified shards through 3999 and Claude Sonnet clean shards through `4000-7858` scored; Gemini full paused due CLI error/capacity instability |

## Status Log

| Date | Stage | Event | Evidence | Next action |
|---|---|---|---|---|
| 2026-04-24 | Step 1 | Phase 1 raw R1 updates completed through S033 | `03_source_document_adjudication/phase1/decision_log_20260424.md` | Finish adjudication propagation into final extraction data |
| 2026-04-24 | Step 2 | Phase 1 pairwise comparison workbook created | `02_pre_adjudication_disagreement/phase1/AI_Adoption_Phase1_Pairwise_Comparison_R1R2_R3R4_20260424.xlsx` | Export final raw disagreement summary |
| 2026-04-25 | Step 0 | Active extraction workspace simplified into numbered folders | `data/04_extraction/README.md` | Keep future artifacts in numbered stage folders |
| 2026-04-25 | Step 3 | Current status clarified: adjudication in progress, reference not frozen | This file | Continue source-document adjudication before LLM comparison |
| 2026-04-25 | Step 3 | Early coding decisions checked against frozen raw workbooks | `03_source_document_adjudication/phase1/coding_decision_application_check_20260425.md` | Apply reviewed decisions in the adjudicated reference rather than editing raw workbooks |
| 2026-04-25 | Step 1 | Phase 2 combined coder workbooks generated for distribution | `01_raw_human_coder_data_freeze/phase2/coder_packages/` | Distribute files and freeze returned completed coder workbooks |
| 2026-05-01 | Step 2/3 | R1-R4 pairwise comparison and source-document adjudication workflow documented | `02_pre_adjudication_disagreement/RATER_COMPARISON_PLAYBOOK.md` | Use the playbook to triage meaningful differences before source-document adjudication |
| 2026-05-01 | Step 0 | Date-stamped coding transfer area added for operational file exchange | `06 coding by date/README.md` | Use date folders for share-safe coding packets, then move finalized artifacts into canonical workflow folders |
| 2026-05-06 | Step 1 | Phase 2 R1 Pair C 17-study working coding batch documented; `S136` HM exclusion correction recorded | `06 coding by date/2026-05-06/README.md`; `06 coding by date/2026-05-06/r1_pairc_17_study_coding_notes.md` | Preserve the local workbook outside Git unless approved for raw freeze; compare against R4 when Pair C returns are available |
| 2026-05-25 | Step 1 | Phase 2 R1-R4 returned workbooks preserved as raw returns and separate freeze candidates | `01_raw_human_coder_data_freeze/phase2/RETURN_MANIFEST_20260525.md` | Continue source-document adjudication from freeze candidates; do not edit raw returns |
| 2026-05-25 | Step 2 | Phase 2 pairwise disagreement queue generated from freeze-candidate workbooks | `02_pre_adjudication_disagreement/phase2/derived/phase2_pairwise_disagreement_summary_20260525.csv` | Triage one-coder-only rows, numeric/source differences, and status mismatches before reference freeze |
| 2026-05-25 | Step 2 | Combined Phase 1+2 pairwise disagreement queues generated for the full 213-study Paper B validation corpus | `02_pre_adjudication_disagreement/combined/derived/combined_pairwise_disagreement_summary_20260525.csv` | Use the combined correlation/status queue for meeting-first review and the all-study queue for full audit coverage |
| 2026-05-25 | Step 3 | Phase 2 PDF source checks recorded for confirmed exclusions and review-required candidates | `03_source_document_adjudication/phase2/phase2_exclusion_source_check_20260525.md` | Resolve review-source studies and duplicate-source issue before freezing the reference |
| 2026-06-05 | Step 3/4 | Source-audited tiered freeze packet created for Paper1/Paper2 blocker studies and Paper2 task-unit scoring preparation | `03_source_document_adjudication/phase2/source_adjudication_decisions_20260605.csv`; `04_reference_standard_freeze/paper2_reference_standard_freeze_note.md`; `04_reference_standard_freeze/CHECKSUMS_TIERED_FREEZE_20260605.csv` | Lock model/run/output files and apply task-family scoring rules before any final LLM accuracy or MASEM substitution claim |
| 2026-06-06 | Step 5 smoke | Locked-output template, multi-model run matrix, scoring rules, scoring harness, and one-row Claude/Gemini direct-r smoke scoring prepared | `05_llm_masem_substitution/locked_outputs/paper2_locked_output_template_20260606.csv`; `05_llm_masem_substitution/locked_outputs/model_runs/paper2_claude_smoke_direct_r_20260606.csv`; `05_llm_masem_substitution/locked_outputs/model_runs/paper2_gemini_smoke_direct_r_20260606.csv`; `05_llm_masem_substitution/results/SCORING_STATUS_20260606.md` | Decide the next locked run size by denominator family before scaling beyond smoke rows |
| 2026-06-06 | Step 5 staged run | Claude/Gemini 77-row denominator-family stratified outputs locked and scored; Claude full-run expansion started with first 3,750 eligible rows locked and scored | `05_llm_masem_substitution/locked_outputs/model_runs/paper2_claude_stratified10_allfamilies_20260606.csv`; `05_llm_masem_substitution/locked_outputs/model_runs/paper2_gemini_stratified10_allfamilies_20260606.csv`; `05_llm_masem_substitution/locked_outputs/model_runs/paper2_claude_full_allfamilies_0000_0499_20260606.csv`; `05_llm_masem_substitution/locked_outputs/model_runs/paper2_claude_full_allfamilies_0500_0999_20260606.csv`; `05_llm_masem_substitution/locked_outputs/model_runs/paper2_claude_full_allfamilies_1000_1499_20260606.csv`; `05_llm_masem_substitution/locked_outputs/model_runs/paper2_claude_full_allfamilies_1500_1999_20260606.csv`; `05_llm_masem_substitution/locked_outputs/model_runs/paper2_claude_full_allfamilies_2000_2499_20260606.csv`; `05_llm_masem_substitution/locked_outputs/model_runs/paper2_claude_full_allfamilies_2500_2999_20260606.csv`; `05_llm_masem_substitution/locked_outputs/model_runs/paper2_claude_full_allfamilies_3000_3499_20260606.csv`; `05_llm_masem_substitution/locked_outputs/model_runs/paper2_claude_full_allfamilies_3500_3749_20260606.csv`; `05_llm_masem_substitution/results/SCORING_STATUS_20260606.md` | Continue Claude full shards from 3750-3999; keep Gemini full paused until row-level CLI errors are eliminated |
| 2026-06-06 | Step 5 Codex/Gemini check | Codex hook-free batch path produced three clean 50-row full-run shards; Gemini retry 1-row probe still returned row-level CLI error | `05_llm_masem_substitution/locked_outputs/model_runs/paper2_codex_full_allfamilies_0000_0049_20260606.csv`; `05_llm_masem_substitution/locked_outputs/model_runs/paper2_codex_full_allfamilies_0050_0099_20260606.csv`; `05_llm_masem_substitution/locked_outputs/model_runs/paper2_codex_full_allfamilies_0100_0149_20260606.csv`; `05_llm_masem_substitution/locked_outputs/model_runs/paper2_gemini_probe1_retry_20260606.csv`; `05_llm_masem_substitution/results/SCORING_STATUS_20260606.md` | Continue Codex in 50-row shards from 0150-0199; keep Gemini full paused until a 1-row probe is clean |
| 2026-06-06 | Step 5 model-explicit continuation | Runner now records CLI model selectors; Claude Sonnet 4000-4499 and Codex GPT-5.5 0250-0349 locked cleanly and rescored; Gemini 2.5 Pro 1-row probe still produced `model_cli_error` and was not registered | `05_llm_masem_substitution/locked_outputs/model_runs/paper2_claude_sonnet_full_allfamilies_4000_4499_20260606.csv`; `05_llm_masem_substitution/locked_outputs/model_runs/paper2_codex_gpt55_full_allfamilies_0250_0349_20260606.csv`; `05_llm_masem_substitution/locked_outputs/model_runs/paper2_gemini25pro_probe1_20260606.csv`; `05_llm_masem_substitution/results/SCORING_STATUS_20260606.md` | Continue Claude Sonnet from 4500-4999 and Codex GPT-5.5 from 0350-0449; keep Gemini full paused until a model-explicit 1-row probe is clean |
| 2026-06-06 | Step 5 clean-only update | Claude Sonnet 4500-4999 and Codex GPT-5.5 0350-0949 locked cleanly and rescored; attempted Claude Sonnet 5000-6499 and 5000-5249 contained row-level `model_cli_error` from session limit and were removed from the clean manifest | `05_llm_masem_substitution/locked_outputs/model_runs/paper2_claude_sonnet_full_allfamilies_4500_4999_20260606.csv`; `05_llm_masem_substitution/locked_outputs/model_runs/paper2_codex_gpt55_full_allfamilies_0350_0449_20260606.csv`; `05_llm_masem_substitution/locked_outputs/model_runs/paper2_codex_gpt55_full_allfamilies_0450_0549_20260606.csv`; `05_llm_masem_substitution/locked_outputs/model_runs/paper2_codex_gpt55_full_allfamilies_0550_0649_20260606.csv`; `05_llm_masem_substitution/locked_outputs/model_runs/paper2_codex_gpt55_full_allfamilies_0650_0749_20260606.csv`; `05_llm_masem_substitution/locked_outputs/model_runs/paper2_codex_gpt55_full_allfamilies_0750_0849_20260606.csv`; `05_llm_masem_substitution/locked_outputs/model_runs/paper2_codex_gpt55_full_allfamilies_0850_0949_20260606.csv`; `05_llm_masem_substitution/results/SCORING_STATUS_20260606.md` | Rerun Claude Sonnet from 5000-5249 after the 21:50 KST reset; continue Codex GPT-5.5 from 0950-1049 |
| 2026-06-06 | Step 5 Codex full clean | Codex GPT-5.5 was backfilled and completed as clean model-explicit locked outputs for `0000-7858`; Claude Sonnet clean manifest advanced through `6499` and then paused at `6500-6999` due session-limit 429 reset reported for 2026-06-07 03:20 Asia/Seoul; Gemini stratified diagnostic with row-level CLI errors was removed from the clean manifest | `05_llm_masem_substitution/locked_outputs/model_runs/paper2_codex_gpt55_full_allfamilies_0000_0099_20260606.csv`; `05_llm_masem_substitution/locked_outputs/model_runs/paper2_codex_gpt55_full_allfamilies_7750_7858_20260606.csv`; `05_llm_masem_substitution/locked_outputs/LOCKED_OUTPUT_MANIFEST_20260606.csv`; `05_llm_masem_substitution/results/SCORING_STATUS_20260606.md`; `05_llm_masem_substitution/RUNBOOK_20260606.md` | Superseded by 2026-06-07 Claude Sonnet full-clean row; keep Gemini full paused until a model-explicit 1-row probe is clean |
| 2026-06-07 | Step 5 Claude Sonnet full clean | Claude Sonnet resumed after provider reset and completed clean model-explicit locked outputs for `6500-7858`, making the clean Sonnet continuation complete for `4000-7858`; scoring was regenerated with 109 clean locked-output files and 5,898 scorable rows | `05_llm_masem_substitution/locked_outputs/model_runs/paper2_claude_sonnet_full_allfamilies_6500_6749_retry3_20260607.csv`; `05_llm_masem_substitution/locked_outputs/model_runs/paper2_claude_sonnet_full_allfamilies_7750_7858_20260607.csv`; `05_llm_masem_substitution/locked_outputs/LOCKED_OUTPUT_MANIFEST_20260606.csv`; `05_llm_masem_substitution/results/SCORING_STATUS_20260606.md`; `05_llm_masem_substitution/NEXT_WORKER_HANDOFF_20260606.md` | Keep Gemini full paused until a model-explicit 1-row probe is clean; do not report final substitution claims without denominator-family interpretation |
| 2026-06-07 | Step 5 denominator-family interpretation | Codex GPT-5.5 and Claude Sonnet model-explicit results were summarized by denominator family and by their overlap subset; a Gemini 2.5 Pro one-row cleancheck probe failed with capacity exhaustion and was not registered as clean evidence | `05_llm_masem_substitution/results/PAPER2_MODEL_EXPLICIT_DENOMINATOR_FAMILY_SUMMARY_20260607.md`; `05_llm_masem_substitution/results/paper2_model_explicit_denominator_family_summary_20260607.csv`; `05_llm_masem_substitution/README.md`; `05_llm_masem_substitution/RUNBOOK_20260606.md` | Use denominator-family and overlap-subset language only; keep Gemini full paused until a clean model-explicit probe succeeds |
| 2026-06-07 | Step 5 extension gate | Claude Sonnet `0000-3999` backfill was attempted but blocked by Claude session-limit 429 before the 13:00 Asia/Seoul reset; no failed backfill rows were registered, and fail-fast support was added for future shard loops | `05_llm_masem_substitution/MODEL_FAMILY_EXTENSION_PLAN_20260607.md`; `scripts/llm_scoring_20260606/run_model_locked_output_batch.py`; `05_llm_masem_substitution/NEXT_WORKER_HANDOFF_20260606.md` | After provider reset, run a one-row Sonnet clean probe, then full `0000-3999` backfill with `--fail-on-model-cli-error`; use Gemini/Gemma only after a clean one-row probe |
| 2026-06-08 | Step 3 | Researcher-confirmed Phase 2 source-adjudication decisions recorded for S195/S206, S014, S021, S121, and S202; S014/S021/S056/S092 assignment status confirmed | `docs/06_decisions/2026-06-08_Paper_B_Source_Adjudication_Decisions.md`; `03_source_document_adjudication/phase2/phase2_source_adjudication_evidence_split_20260529.md` | Continue source-value adjudication for S014/S021/S056/S092/S121 and prepare decision-log entries before Step 4 freeze |
| 2026-06-08 | Step 3 | Researcher confirmed S014 academic researchers/faculty are eligible; S014/S021/S056/S092 PDFs were secured in the ignored adjudication source-PDF folder | `docs/06_decisions/2026-06-08_Paper_B_Source_Adjudication_Decisions.md`; `03_source_document_adjudication/phase2/phase2_source_adjudication_evidence_split_20260529.md`; `03_source_document_adjudication/source_pdfs/` (ignored local PDF folder) | Source-check S014 direct-path availability, verify S021 supplement/online-resource access if required, adjudicate S056/S092 path tables, transcribe S121 values by student/teacher sample, and prepare decision-log entries before Step 4 freeze |
| 2026-06-08 | Step 3 | Source-value/exclusion decision-log entries added for S195/S206/S202/S014/S021/S056/S092/S121 | `03_source_document_adjudication/phase2/decision_log_20260608.md`; `03_source_document_adjudication/phase2/phase2_source_adjudication_evidence_split_20260529.md` | Supplement/row-set follow-up remained for S021/S121 before Step 4 freeze |
| 2026-06-08 | Step 3 | S021 Springer online supplement recovered and checked; S121 Figure 2 student/teacher row set transcribed | `03_source_document_adjudication/source_pdfs/S021_supplementary_file1.pdf` (ignored); `03_source_document_adjudication/source_pdfs/S021_supplementary_file2.docx` (ignored); `03_source_document_adjudication/phase2/s121_figure2_row_set_20260608.md` | S021 model/row-set choice was subsequently resolved as limited primary Model 1 inclusion |
| 2026-06-08 | Step 3 | Researcher decided to include S021 via limited main-PDF primary Model 1 T1/T2 beta-converted rows | `03_source_document_adjudication/phase2/s021_primary_model_row_set_20260608.md`; `03_source_document_adjudication/phase2/decision_log_20260608.md` | Prepare Step 4 source-anchored adjudicated human reference draft from logged Step 3 decisions |
| 2026-06-08 | Step 4 | Source-adjudicated Phase 2 reference draft started from logged S014/S021/S056/S092/S121/S195/S202/S206 decisions | `04_reference_standard_freeze/paper_b_phase2_source_adjudicated_reference_draft_20260608.csv`; `04_reference_standard_freeze/paper_b_phase2_step4_decision_application_audit_20260608.csv`; `04_reference_standard_freeze/reference_standard_freeze_audit_draft_20260608.md` | Run freeze audit and only then commit a frozen reference file and final freeze log |
| 2026-06-08 | Step 4 | Freeze audit completed for the Phase 2 source-adjudicated draft; S092 source betas were reconstructed and draft r values corrected to Peterson-Brown conversions | `04_reference_standard_freeze/qa/freeze_audit_20260608.md`; `04_reference_standard_freeze/paper_b_phase2_source_adjudicated_reference_draft_20260608.csv`; `03_source_document_adjudication/phase2/decision_log_20260608.md` | Final reviewer/date/commit hash and final freeze log are still required before Step 5 |
| 2026-06-08 | Step 4 | Scoped frozen reference package prepared after researcher approval for the Phase 2 source-adjudicated high-priority package | `04_reference_standard_freeze/paper_b_phase2_source_adjudicated_reference_frozen_20260608.csv`; `04_reference_standard_freeze/reference_standard_freeze_log_20260608.md`; `04_reference_standard_freeze/post_freeze_corrections_20260608.md` | Record artifact commit hash in the freeze log; keep Step 5 inactive until the intended analysis scope is frozen |
| 2026-06-08 | Step 4 | Scoped frozen reference package artifact commit hash recorded | `04_reference_standard_freeze/reference_standard_freeze_log_20260608.md`; artifact commit `2c40c37a66229b6f0acac333048aa2b7e3a32679` | Decide whether Step 5 should run only on this scoped package or wait for full-corpus reference freeze |

## Coding Decisions Already Reflected

The following early coding discussions are reflected in the current Phase 1
decision log and protocol documents. Some raw coder workbook cells intentionally
still preserve pre-adjudication values; use Step 3 and Step 4 to apply final
source-anchored decisions.

- S164: Set `EE-SI = -0.024`, `FC-PE = 0.716`, and `PE-UB = 0.632`.
- S091: Use sample size `N = 382`; code the tool as ChatGPT-specific and keep
  the statistical coding decision.
- S187: Treat stress/anxious mapping as flagged and mapped to `ANX` pending
  adjudication record completion.
- S079: Treat the relevant effects as path coefficients.
- S223: Use the R1-coded value.
- S005: Exclude `JOY`; do not map `CON -> FC`; do not adopt `FC` for that case.
- S044: Use GAAIS Positive Attitudes toward AI as primary `ATT`; do not average
  Negative Attitudes into primary `ATT`.
- S054: Use teacher-only sample and exclude the high-school student sample; do
  not map Perceived Playfulness to `ATT`.
- S011: Exclude TTF paths from `FC` mapping.
- S180: Exclude from MASEM correlation contribution because no usable target
  construct-pair `r` or beta matrix is available.
- S220: Exclude because the focal use case is mental healthcare chatbot/content,
  not educational AI adoption.
- S151: Use source-reported `FC-UB = .558`; preserve source-reported
  three-decimal correlations during adjudication.
- S087: Exclude Satisfaction from `ATT`; do not treat
  `Satisfaction-Performance Expectancy` as `ATT-PE`.
- S051: Do not map Perceived Risk to `ANX`; include R1 direct values
  `EE-FC = .59`, `EE-PE = .48`, and `FC-PE = .47`.
- S120: Use R1 beta-converted path-coefficient values for `BI-EE`, `BI-FC`,
  `BI-PE`, `BI-SI`, and `BI-UB`; exclude R2-only `SI-TRU`, `SI-UB`, and
  `TRU-UB` rows.
- HTMT-only tables are not treated as usable MASEM correlation matrices.
- S081: Use R1 values for unresolved R1-R2 correlation differences.
- S035: Use R1 values for unresolved R1-R2 correlation differences.
- S191: Use R2 values for unresolved R1-R2 correlation differences.
- S217: Use R1 values for unresolved R1-R2 correlation differences.
- S033: Use R1 beta-converted path-coefficient values; retain `ATT-EE = .06`
  from beta `.013`.

## Required Update Rule

Whenever the project advances from one step to the next, add a new row to the
status log and cite the file that proves the transition.
