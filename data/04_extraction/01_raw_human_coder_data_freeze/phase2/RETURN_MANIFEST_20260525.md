# Phase 2 Return Manifest

Date: 2026-05-25

Raw returned workbooks are preserved separately from freeze candidates. Freeze candidates contain only structural repairs and source-check status updates needed for adjudication workflow; raw coder values are not overwritten.

## Freeze Candidate Summary

| Coder | Phase 2 assigned | Status counts | Nonempty Phase 2 studies | Nonempty rows | Zero-value Phase 2 studies |
|---|---:|---|---:|---:|---|
| R1 | 57 | {'done': 53, 'excluded': 4} | 54 | 517 | S108, S132, S224 |
| R2 | 56 | {'done': 49, 'excluded': 4, 'review_source': 3} | 49 | 466 | S021, S039, S092, S101, S118, S202, S206 |
| R3 | 56 | {'done': 48, 'excluded': 4, 'review_source': 4} | 48 | 428 | S021, S039, S056, S101, S118, S121, S202, S206 |
| R4 | 57 | {'done': 52, 'excluded': 4, 'review_source': 1} | 54 | 517 | S014, S132, S195 |

## Repairs Applied

- R1 `AI_Adoption_MASEM_Coding_v3_R1_Phase0_1_2_freeze_candidate_20260525.xlsx`: filled source-checked EXCLUSION_LOG rows; normalized Phase 2 ASSIGNMENT statuses for freeze candidate
- R2 `AI_Adoption_MASEM_Coding_v3_R2_Phase0_1_2_freeze_candidate_20260525.xlsx`: filled source-checked EXCLUSION_LOG rows; normalized Phase 2 ASSIGNMENT statuses for freeze candidate
- R3 `AI_Adoption_MASEM_Coding_v3_R3_Phase0_1_2_latest_consensus_freeze_candidate_20260525.xlsx`: renamed original CORRELATIONS to CORRELATIONS_original_return; promoted latest consensus sheet to CORRELATIONS; restored duplicate original_beta header in column G to p_value; filled source-checked EXCLUSION_LOG rows; normalized Phase 2 ASSIGNMENT statuses for freeze candidate
- R4 `AI_Adoption_MASEM_Coding_v3_R4_Phase0_1_2_freeze_candidate_20260525.xlsx`: filled source-checked EXCLUSION_LOG rows; normalized Phase 2 ASSIGNMENT statuses for freeze candidate

## Source-Check Boundary

Confirmed exclusions and review-required candidates are documented in `data/04_extraction/03_source_document_adjudication/phase2/phase2_exclusion_source_check_20260525.md`.