# Paper B Document Generation Plan

Date: 2026-05-28

Status: planning map for documents that can be generated from the confirmed
Research Specification, accepted tolerance rules, task-contingent augmentation
memo, and current extraction workflow state.

## Immediate Documents

These can be generated now because they rely on design decisions and
pre-adjudication artifacts rather than post-freeze LLM results.

| Document | Purpose | Source inputs | Output target |
|---|---|---|---|
| Methods scaffold | Convert the current design into manuscript-ready Methods language | Research Specification, `ANALYSIS_PLAN.md`, tolerance rules, workflow status | `paper_b/manuscript/` |
| Table shell packet | Create publication-ready tables for dataset states, taxonomy, RQ0 disagreement, LLM validity shell, and substitution shell | Direction memo, analysis plan, combined disagreement summaries | `paper_b/tables/` or manuscript appendix |
| Figure brief packet | Specify Figure 1-5 as reproducible figure briefs before drawing or scripting | Analysis plan and tolerance rules | `paper_b/figures/` |
| RQ0 disagreement report | Report human-human disagreement counts and tolerance-band distribution without LLM claims | Combined Phase 1+2 disagreement CSVs | `paper_b/reports/` |
| Adjudication meeting packet | Turn P0-P3 priority rules into a meeting agenda for source-document adjudication | Review queue, playbook, tolerance rules | `data/04_extraction/03_source_document_adjudication/` |
| Supplementary protocol appendix | Document dataset states, task families, tolerance bands, triage categories, and stop rules | Decision logs and tolerance rules | manuscript supplement |

## Post-Freeze Documents

These require the frozen source-anchored adjudicated human reference standard.

| Document | Entry condition | Purpose |
|---|---|---|
| Reference freeze log | Step 4 complete | Record source-anchored reference file, freeze date, exclusions, and known caveats. |
| LLM comparison analysis report | Frozen reference and locked LLM outputs | Report RQ1 validity and RQ2 error taxonomy by task family. |
| Triage-yield report | Frozen reference, LLM outputs, source-type flags | Estimate how well human disagreement and LLM signals prioritize expert review. |
| MASEM substitution report | Locked human-reference and LLM-assisted MASEM inputs | Report RQ4 pooled correlations, paths, fit decisions, and inference stability. |
| Reproducibility archive manifest | Final prompts, schemas, scripts, and outputs locked | Prepare share-safe archive contents for submission or OSF. |

## Recommended Next Work

The next work should be the immediate manuscript-and-analysis scaffold, not
post-freeze LLM evaluation.

1. Generate the Methods scaffold around the accepted workflow sequence:
   raw human coding -> pre-adjudication disagreement -> source adjudication ->
   reference freeze -> LLM comparison -> MASEM substitution.
2. Generate Table 1 and Table 2 as manuscript-ready tables because they are
   design/taxonomy tables and do not require reference freeze.
3. Generate the RQ0 disagreement report from combined Phase 1+2 artifacts,
   including numeric tolerance-band distribution and high-priority review
   examples.
4. Convert the P0/P1/P2/P3 rules into an adjudication meeting packet so Step 3
   can move toward reference freeze.
5. Only after Step 4 freeze, generate RQ1-RQ4 empirical reports.

## Stop Rule

Do not generate manuscript text that presents LLM accuracy, triage yield, or
MASEM substitution stability as a completed result until the required post-freeze
artifacts exist.
