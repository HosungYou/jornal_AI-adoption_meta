# Paper B Canonical Reference and Model Framing

Date: 2026-06-11

Status: Accepted for current Paper B Step 5 analysis.

## Decision

Use the OneDrive folder `Paper2_Human_Final_Consensus_20260605_v2` as the
canonical human consensus package for Paper B. The Git `04_reference_standard`
and `05_llm_masem_substitution` files are downstream source-audited freeze,
task-unit, locked-output, and scoring layers built from that consensus package.

Canonical OneDrive package identifier:

`AI Adoption Meta Analysis - Documents/Meta/AI Adoption/Paper2_Human_Final_Consensus_20260605_v2`

Observed package contents:

- `CHECKSUMS_20260605_v2.csv`
- `Paper2_Converted_Beta_Path_SourceStatistic_Sensitivity_Input_20260605_v2.csv`
- `Paper2_Direct_R_ConstructPair_Summary_20260605_v2.csv`
- `Paper2_Direct_R_Numeric_QC_20260605_v2.csv`
- `Paper2_Direct_R_Study_Summary_20260605_v2.csv`
- `Paper2_Human_Final_Consensus_Manifest_20260605_v2.md`
- `Paper2_Human_Final_Consensus_Reference_Document_20260605_v2.md`
- `Paper2_Metadata_Moderator_Wide_Candidate_20260605_v2.csv`
- `Paper2_Primary_SourceReported_Direct_R_Input_20260605_v2.csv`
- `Paper2_R1_R4_Structured_Comment_Decisions_20260605_v2.csv`
- `Paper2_Unified_Consensus_Codebook_20260605_v2.md`
- `Paper2_Unified_Consensus_Summary_20260605_v2.csv`
- `Paper2_Unified_Conversion_or_Review_Queue_20260605_v2.csv`
- `Paper2_Unified_Direct_R_Analysis_Input_20260605_v2.csv`
- `Paper2_Unified_Human_Final_Consensus_Decisions_20260605_v2.csv`
- `Paper2_Unified_Metadata_Consensus_20260605_v2.csv`

The v2 checksum manifest remains the package integrity anchor. The current local
inspection verified the folder path and produced SHA-256 values for all 16 files.

## Scoring Boundary

The scoring anchor is the source-anchored adjudicated human reference standard,
not raw coder returns and not an infallible reference. The 8,783 task units are
not one accuracy denominator. All analysis must use `denominator_family` and
`scoring_eligibility`.

Accepted scoring decisions:

- S072 ANX-EE `r = 1.0` is excluded from primary scoring and retained only as a
  trace/influence diagnostic.
- `source_blank_r` rows are included in the primary direct-r extraction family
  when the human consensus supplies a direct-r value. They should still be
  flagged for evidence-quality review.
- Converted beta/path/source-statistic rows are included in the primary numeric
  extraction evaluation table as an explicit converted/source-type stratum. They
  are not pooled with source-reported direct-r rows and do not silently enter the
  primary MASEM direct-r input.
- `not_derivable_trace`, pointer-only rows without source evidence text, and
  duplicate/unusable-source records are excluded from final evidence-content
  accuracy denominators.
- Abstentions on scorable rows count as incorrect, and abstention rates are
  reported separately.
- Metadata fields require both strict exact-match and relaxed normalized-match
  reporting.
- `absence_or_blank_consensus` is a triage/blank behavior family, not an
  accuracy claim.

## Model Framing

The primary workflow is the locked Codex GPT-5.5 workflow. Claude and Gemini are
supplementary cross-model sensitivity and triage evidence. They should not be
framed as a vendor ranking or model-winner result.

Clean model-explicit rows currently support:

- `codex:gpt-5.5` for `0000-7858`
- `gemini:gemini-3-flash-preview` for `0000-7858`
- `claude:sonnet` for `0000-7858`; the `0000-3999` Sonnet backfill was
  completed on 2026-06-11 with 16 clean shards and no `model_cli_error` rows

Diagnostic, failed, local-only, unregistered probe, or superseded model outputs
are excluded from clean scoring and must not be relabeled after locking. If a
legacy `probe` filename is explicitly registered in
`LOCKED_OUTPUT_MANIFEST_20260606.csv` as a clean locked model output, the
manifest and checksum record govern its provenance.

Legacy Claude Code/default-unspecified rows from the earlier `0000-3999` run
are retained only as audit provenance. They are not relabeled as Sonnet and are
not the Claude rows used for model-explicit Sonnet comparison after the
2026-06-11 backfill.

## PDF Source-Text Audit Boundary

The P0/P1 pointer-only source rows have a separate PDF text audit layer. All 746
rows had local PDFs located and extractable text. The audit found 245 rows with
both numeric value and construct-pair terms, 336 rows with numeric value found
but construct-pair terms not on the best page, 163 rows with source/context
terms but no numeric value hit, and 2 rows with no target hit.

This audit strengthens source-risk triage, but it does not overwrite the frozen
source-anchored adjudicated human reference standard. Rows without numeric value
hits, pair-term alignment, or reliable extracted table text remain manual
table-review/OCR or final alignment-check candidates before any final
substitution-stability claim.

## R/metaSEM Claim Boundary

The local R environment is now ready for Paper B meta-analytic scripting:
`Rscript` 4.6.0, `OpenMx` 2.22.11, and `metaSEM` 1.5.0 load successfully. The
current expert-reviewed substitution input has 804 rows and `r_numeric` for all
804 rows, but `sample_size_numeric` is present for only 49 rows.

Therefore, the current evidence supports deterministic substitution-input
readiness and pooled-correlation sensitivity checks. It does not yet support a
final full TSSEM Stage 1/Stage 2 SEM path-coefficient or model-fit stability
claim until sample sizes are completed or a documented missing-N exclusion rule
is applied.

## Manuscript Implication

Paper B should be written as a task-contingent LLM augmentation and
source-anchored evidence-synthesis methods paper. The core claims are RQ1-RQ3
task-family validity, error/source-condition analysis, human-review triage value,
and downstream MASEM substitution stability. Final substitution claims require
locked inputs and denominator-family reporting.
