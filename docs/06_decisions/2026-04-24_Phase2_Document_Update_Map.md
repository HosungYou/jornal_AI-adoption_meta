# Phase 2 Protocol Update Map

## Scope

This map records which documents were updated after the Phase 2 rotated-pair
protocol amendment.

## Updated Documents

| Document | Update |
|---|---|
| `paper_b/CODING_PROTOCOL.md` | Replaced Phase 2 AI-first single verification with R1+R4 / R2+R3 rotated-pair human coding. |
| `paper_b/RESEARCHER_ROLES.md` | Updated coder roles, Phase 2 pairing, adjudication responsibilities, and blinding diagram. |
| `paper_b/TIMELINE.md` | Replaced single-verification timeline with rotated-pair coding, adjudication, and post-adjudication LLM comparison steps. |
| `paper_b/SAMPLING_PROTOCOL.md` | Added Phase 2 assignment rules and clarified Phase 2 as Paper A core plus optional Paper B validation. |
| `paper_b/ANALYSIS_PLAN.md` | Added Phase 1/Phase 2 reference-standard tiers and visualization plan for numeric extraction errors. |
| `paper_b/AUDIT_TRAIL_GUIDE.md` | Updated human coding folders, discrepancy fields, Phase 2 logs, and blinding requirements. |
| `paper_b/README.md` | Added Phase 2 protocol reset summary and updated IRR design. |
| `paper_b/DISCUSSION_LOG_KR.md` | Added decision record for Phase 2 rotated-pair human coding. |
| `paper_b/manuscript/Paper_B_RSM_Summarized_Manuscript_v0.2.md` | Updated the Method section to reflect Phase 1 completion and Phase 2 rotated pairs. |
| `paper_b/manuscript/Paper_B_RSM_Summarized_Manuscript_v0.2.docx` | Regenerated from the updated manuscript Markdown with table-safe layout and rendered for QA. |
| `paper_b/templates/discrepancy_log_template.csv` | Added phase, pair, coder IDs, adjudicator, LLM comparison, and error taxonomy fields. |
| `paper_b/checklists/PRISMA_trAIce_checklist.md` | Updated human oversight protocol wording. |
| `paper_b/checklists/TRIPOD_LLM_checklist.md` | Updated LLM specification from 3-model comparison to primary workflow plus optional sensitivity. |
| `data/04_extraction/AI_Adoption_MASEM_Coding_Manual_v2.md` | Updated workflow diagram, workflow rules, and timeline for Phase 2 rotated pairs. |
| `data/04_extraction/generate_coding_manual_docx.py` | Updated DOCX generator source to reflect manual v2.4 protocol language and tolerate missing equation-rendering dependency. |
| `data/04_extraction/generate_coder_packages.py` | Updated future package assignment logic so Phase 2 studies are duplicated to rotated pairs R1+R4 and R2+R3 rather than split as single-coder assignments. |
| `data/04_extraction/AI_Adoption_MASEM_Coding_Manual_v2.docx` | Regenerated from the updated manual with a table-safe layout and rendered for QA. |
| `data/04_extraction/coding_progress_20260424.md` | Added Phase 2 protocol amendment note. |
| `data/04_extraction/consensus/README.md` | Added Phase 2 next-step pairing and blinding notes. |
| `docs/06_decisions/decision_log.md` | Added the Phase 2 rotated-pair decision. |
| `docs/06_decisions/2026-03-06_IRR_and_AutoInclude_Decision.md` | Marked the earlier Phase 2 single-coding plan as superseded. |
| `docs/06_decisions/2026-04-24_Phase2_Rotated_Pair_Protocol.md` | Added the canonical amendment decision. |

## Documents Not Rewritten

`paper_b/DISCUSSION_LOG_KR.md` retains earlier historical notes about AI-first
verification so the decision history remains traceable. The later 2026-04-24
entry supersedes those notes.

The coding manual Word file has been regenerated for sharing. If the team later
changes Phase 2 pair assignments or adjudication roles, regenerate the Word file
again from the updated Markdown source.
