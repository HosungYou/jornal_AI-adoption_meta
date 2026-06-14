# Paper A A/C review execution plan

Date: 2026-06-14

## 확정된 사용자 선택

- A tier: `A_fast_confirm_existing_human_value`는 study-level spot check 방식으로 검토한다.
- C tier: `C_open_table_for_possible_full10_densification`는 full10 전체 pair 순서대로 검토한다.

## A tier 실행 방식

- 대상 행: 609
- 대상 study: 67
- 각 study에서 1-3개 representative row를 먼저 확인한다.
- spot check가 통과하면 같은 source table 구조의 나머지 row를 batch-confirm 후보로 처리할 수 있다.
- 단, batch-confirm도 연구자 결정이며 `promote_to_supplemental_input=yes`는 confirmation template에 사람이 기록해야 한다.

## C tier 실행 방식

- 대상 행: 465
- pair order는 `PE, EE, SI, FC, ATT, SE, TRU, ANX, BI, UB`의 full10 이론 순서를 사용한다.
- 각 row는 source packet/PDF table을 열어 실제 상관값을 사람이 입력해야 한다.
- AI trace가 construct/table cue를 찾았다는 사실만으로 값이 추가되지 않는다.

## 첫 review pair들

| order | pair | candidate_rows |
| --- | --- | --- |
| 3 | FC-PE | 2 |
| 4 | ATT-PE | 13 |
| 5 | PE-SE | 13 |
| 6 | PE-TRU | 10 |
| 7 | ANX-PE | 14 |
| 8 | BI-PE | 1 |
| 9 | PE-UB | 6 |
| 11 | EE-FC | 2 |
| 12 | ATT-EE | 13 |
| 13 | EE-SE | 13 |

## 생성 파일

- A spot-check worksheet: `data/04_extraction/05_llm_masem_substitution/results/paper_a_ai_candidate_source_trace_20260614/paper_a_A_fast_confirm_study_level_spotcheck_worksheet_20260614.csv`
- C full10 ordered queue: `data/04_extraction/05_llm_masem_substitution/results/paper_a_ai_candidate_source_trace_20260614/paper_a_C_full10_pair_ordered_densification_review_queue_20260614.csv`
- C batch 01: `data/04_extraction/05_llm_masem_substitution/results/paper_a_ai_candidate_source_trace_20260614/paper_a_C_full10_pair_ordered_batch01_20260614.csv`
- C pair summary: `data/04_extraction/05_llm_masem_substitution/results/paper_a_ai_candidate_source_trace_20260614/paper_a_C_full10_pair_ordered_queue_summary_20260614.csv`

## 다음 실행

1. `paper_a_A_fast_confirm_study_level_spotcheck_worksheet_20260614.csv`에서 spotcheck_required 행만 먼저 확인한다.
2. `paper_a_C_full10_pair_ordered_batch01_20260614.csv`부터 source/PDF table을 열어 human_source_value를 채운다.
3. 확인된 row만 confirmation template 또는 supplemental input builder로 넘긴다.
