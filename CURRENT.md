# CURRENT

Project: AI Adoption Meta-Analysis Methodology Strategy

This file is regenerated from `.longtable/current-session.json` and `.longtable/state.json`.

## Focus Now
- Current goal: Provide AI-candidate-only Paper A source-trace results for researcher review without violating Paper B reference-standard boundaries.
- Current blocker: AI traces are review evidence only; no row may enter Paper A supplemental input until the researcher confirms the source value, evidence type, and source location.
- Next action: Researcher confirms or rejects the seven S048 source-visible numeric-cell candidates before any supplemental input or model-family MASEM rerun.
- Perspectives: reviewer, methods_critic, measurement_auditor, ethics_reviewer, voice_keeper, venue_strategist
- Disagreement: show_on_conflict

## Open Questions
- Which AI-candidate source-trace rows should be human-confirmed and promoted to supplemental Paper A densification input?

## Recent LongTable Invocations
- researcher decision recorded: use the recommended candidate-only route; source-trace results should be provided to the researcher, who decides whether any row enters supplemental Paper A input.
- AI-candidate source-trace packet generated: existing human-coded source-review rows and full10 missing-pair densification candidates are traced without changing Paper A input or Paper B reference values. Korean researcher decision brief and shortlist were generated on 2026-06-14.
- A/C review execution artifacts generated: A study-level spot-check worksheet, C full10 pair-ordered queue, first batch workbook, and initial FC-PE construct-mapping evidence draft.
- boundary preserved: AI traces are not independent human coding and not source-anchored adjudication by themselves.

## Pending Decision Questions
- Researcher checkpoint pending: confirm or reject the seven S048 source-visible values in `paper_a_C_remaining_full10_batch_review_shortlist_20260615.csv`.

## Restart Prompt
- "Continue after the 2026-06-14 Paper A AI-candidate-only source-trace packet: AI traces are review evidence only and cannot enter Paper A supplemental input until the researcher confirms source value, evidence type, and source location. Use the generated confirmation template to decide which rows to promote."

## Quick Start
- Open `codex` in this directory.
- A good first message is usually `$longtable-start`.

## Evidence Rule
- External or current claims should carry a source link or be labeled as inference.

## 2026-06-14 update - Paper A/C full10 pair 04_ATT-PE source review

- Completed the ordered source-packet review for `04_ATT-PE` across 13 AI-candidate rows.
- Preliminary decision: do not promote any ATT-PE values. The reviewed sources show PE/PU or performance-expectancy counterparts, but no measured full10 ATT construct.
- Generated evidence artifacts under `data/04_extraction/05_llm_masem_substitution/results/paper_a_ai_candidate_source_trace_20260614/`:
  - `paper_a_C_pair04_ATT_PE_source_evidence_draft_20260614.csv`
  - `PAPER_A_C_PAIR04_ATT_PE_REVIEW_LOG_KO_20260614.md`
- Current next action: continue full10 ordered densification review at the next pair after `04_ATT-PE`; keep AI candidates as source-trace review evidence only until researcher confirmation.

## 2026-06-14 update - Paper A/C full10 pair 05_PE-SE source/PDF review

- Completed the ordered source/PDF review for `05_PE-SE` across 13 AI-candidate rows.
- Preliminary decision: no immediate promotion. `S121-1` and `S121-2` have conditional Figure 2 Spearman-r candidates (`.40`, `.30`) only if `genAI-related subjective competence` is approved as full10 `SE`.
- Exclusion rule recorded: do not map `PBC`, `Security`, generic efficacy language, or self-efficacy in references/background to full10 `SE`.
- Generated evidence artifacts under `data/04_extraction/05_llm_masem_substitution/results/paper_a_ai_candidate_source_trace_20260614/`:
  - `paper_a_C_pair05_PE_SE_source_evidence_draft_20260614.csv`
  - `PAPER_A_C_PAIR05_PE_SE_REVIEW_LOG_KO_20260614.md`
- Current next action: continue full10 ordered densification review at `07_ANX-PE`; S121 PE-SE mapping is already researcher-approved and staged.

## 2026-06-14 update - Researcher-approved S121 PE-SE supplement

- Researcher approved mapping `genAI-related subjective competence` to full10 `SE` for S121.
- Promoted two source-visible S121 Figure 2 Spearman-r values into researcher-approved supplemental input staging: `S121-1 PE-SE=.40` with `N=3094`; `S121-2 PE-SE=.30` with `N=1767`.
- Created `data/04_extraction/05_llm_masem_substitution/results/paper_a_researcher_approved_pe_se_s121_supplement_20260614/`.
- Boundary retained: PBC, Security, generic efficacy wording, and reference/background self-efficacy detections are still excluded from full10 `SE`.
- Current next action: continue full10 ordered densification review at `07_ANX-PE`; after the current ordered batch checkpoint, decide whether to rerun model-family MASEM with the researcher-approved PE-SE supplement.

## 2026-06-14 update - Paper A/C full10 pair 06_PE-TRU source/PDF review

- Completed the ordered source/PDF review for `06_PE-TRU` across 10 AI-candidate rows.
- Preliminary decision: promote no values. All rows failed the full10 `TRU` construct-mapping gate, not the numeric-value extraction step.
- Exclusion rule recorded: do not map `insecurity`, `privacy concerns`, `psychological risk`, `perceived risk`, `habit`, `perceived competence`, or `perceived enjoyment` to full10 `TRU`.
- Generated evidence artifacts under `data/04_extraction/05_llm_masem_substitution/results/paper_a_ai_candidate_source_trace_20260614/`:
  - `paper_a_C_pair06_PE_TRU_source_evidence_draft_20260614.csv`
  - `PAPER_A_C_PAIR06_PE_TRU_REVIEW_LOG_KO_20260614.md`
- Current next action: continue full10 ordered densification review at `07_ANX-PE`.

## 2026-06-14 update - Paper A/C full10 pair 07_ANX-PE source/PDF review

- Completed the ordered source/PDF review for `07_ANX-PE` across 14 AI-candidate rows.
- Preliminary decision: no immediate promotion. `S121-1` and `S121-2` have conditional Figure 2 Spearman-r candidates (`-0.23`, `-0.08`) only if `threat appraisal` is approved as full10 `ANX`.
- Exclusion rule recorded: do not map `perceived risk`, `innovative resistance`, `trust`, `privacy/security`, `reference-only anxiety`, or `challenge appraisal` to full10 `ANX`.
- Generated evidence artifacts under `data/04_extraction/05_llm_masem_substitution/results/paper_a_ai_candidate_source_trace_20260614/`:
  - `paper_a_C_pair07_ANX_PE_source_evidence_draft_20260614.csv`
  - `PAPER_A_C_PAIR07_ANX_PE_REVIEW_LOG_KO_20260614.md`
- Current next action: continue full10 ordered densification review at `08_BI-PE`; do not rerun model-family MASEM until approved supplemental rows are staged.

## 2026-06-15 update - S121 ANX rejection and remaining C-tier batch triage

- Researcher rejected mapping `threat appraisal` to full10 `ANX`; `S121-1 ANX-PE=-0.23` and `S121-2 ANX-PE=-0.08` are not promoted.
- Completed a remaining-queue batch triage instead of continuing pair-by-pair: 413 rows across 36 full10 pair labels.
- Batch-safe source-visible numeric-cell candidates: 7 rows, all from `S048` Table 2 Pearson correlation matrix.
- Held/excluded groups: S004 SE rows depend on rejected `PKC -> SE`; S072 rows require construct-mapping audit before any value entry; one/no-human-supported-construct rows remain excluded unless source adjudication reopens mapping.
- Generated evidence artifacts under `data/04_extraction/05_llm_masem_substitution/results/paper_a_ai_candidate_source_trace_20260614/`:
  - `paper_a_C_remaining_full10_batch_triage_20260615.csv`
  - `paper_a_C_remaining_full10_batch_review_shortlist_20260615.csv`
  - `PAPER_A_C_REMAINING_FULL10_BATCH_TRIAGE_KO_20260615.md`
- Current next action: researcher confirms or rejects the seven S048 values before supplemental input or model-family MASEM rerun.
