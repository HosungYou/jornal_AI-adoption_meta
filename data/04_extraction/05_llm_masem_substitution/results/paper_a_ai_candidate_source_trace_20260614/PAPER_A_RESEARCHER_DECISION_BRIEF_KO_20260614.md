# Paper A researcher decision brief: AI-candidate source trace

Date: 2026-06-14

## 핵심 판단

AI trace는 분석값이 아니라 검토 증거입니다. Paper A supplemental input으로 승격하려면 연구자가 source table/PDF를 보고 값, evidence type, source location을 직접 확정해야 합니다. 이 원칙은 Paper B의 source-anchored adjudicated human reference standard를 침해하지 않기 위한 경계입니다.

## 전체 규모

- Existing human-coded value review rows: 727
- Full10 missing-pair densification trace rows: 574
- Human confirmation template rows: 1192

## AI trace 상태 요약

### Existing human-coded values

- ai_trace_auto_value_visible_exact: 609
- ai_trace_possible_value_visible_broad_match: 118

### Existing review priority

- p1_review_value_not_found_in_any_text: 451
- p2_source_or_pdf_presence_gap: 276

### Full10 missing-pair densification

- likely_not_densifiable_construct_pair_not_visible: 2
- likely_not_densifiable_one_construct_not_visible: 107
- possible_densification_source_review_candidate: 465

## 추천 의사결정 순서

1. `A_fast_confirm_existing_human_value`부터 처리: 이미 human-coded 값이 PDF/source text에서 정확히 보이는 행입니다. 빠르게 source location과 evidence type만 확인하면 됩니다.
2. `B_check_possible_false_positive_existing_value` 처리: 숫자 broad match만 있으므로 false positive 가능성이 있습니다. table을 열어 값과 construct label이 같은 셀인지 확인해야 합니다.
3. `C_open_table_for_possible_full10_densification` 처리: construct/table cue는 보이지만 값은 아직 추가되지 않았습니다. PDF/source table에서 실제 상관값을 직접 찾아야 합니다.

## Shortlist 규모

- A_fast_confirm_existing_human_value: 609
- B_check_possible_false_positive_existing_value: 118
- C_open_table_for_possible_full10_densification: 465

## 먼저 볼 study 후보

| study_id | A_fast_confirm_existing_human_value | B_check_possible_false_positive_existing_value | C_open_table_for_possible_full10_densification | total_shortlist_rows |
| --- | --- | --- | --- | --- |
| S185 | 69 | 0 | 24 | 93 |
| S194 | 75 | 0 | 0 | 75 |
| S121-1 | 42 | 0 | 24 | 66 |
| S121-2 | 42 | 0 | 24 | 66 |
| S208 | 50 | 0 | 0 | 50 |
| S036 | 12 | 0 | 24 | 36 |
| S028 | 31 | 19 | 0 | 50 |
| S072 | 8 | 0 | 19 | 27 |
| S004 | 0 | 0 | 24 | 24 |
| S030 | 0 | 0 | 24 | 24 |
| S055 | 0 | 0 | 24 | 24 |
| S088 | 0 | 0 | 24 | 24 |

## 사용자가 내려야 하는 결정

- 각 행에 대해 `human_decision`을 `confirm`, `correct`, `exclude`, `defer` 중 하나로 지정합니다.
- 승격하려면 `final_value_if_confirmed`, `evidence_type`, `source_location_confirmed`, `decision_rationale`, `promote_to_supplemental_input=yes`가 필요합니다.
- `C_open_table...` 행은 AI가 값을 넣지 않았으므로, 사람이 source table에서 값을 직접 입력하기 전에는 승격할 수 없습니다.

## 생성 파일

- Shortlist CSV: `data/04_extraction/05_llm_masem_substitution/results/paper_a_ai_candidate_source_trace_20260614/paper_a_researcher_decision_shortlist_20260614.csv`
- Study summary CSV: `data/04_extraction/05_llm_masem_substitution/results/paper_a_ai_candidate_source_trace_20260614/paper_a_researcher_decision_study_summary_20260614.csv`
- Original confirmation template: `data/04_extraction/05_llm_masem_substitution/results/paper_a_ai_candidate_source_trace_20260614/paper_a_human_confirmation_template_from_ai_trace_20260614.csv`

## 다음 실행 조건

연구자가 승격할 행을 확인하면, 그때 supplemental Paper A input을 생성하고 model-family MASEM을 rerun할 수 있습니다. 확인 전에는 current source-clean model-family MASEM 결과를 primary empirical route로 유지해야 합니다.
