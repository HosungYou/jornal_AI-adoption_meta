# Paper A/C full10 pair 04_ATT-PE source evidence review log (2026-06-14)

## 검토 범위

- 대상 pair: `04_ATT-PE`
- 큐 row 수: 13
- 검토 파일: `paper_a_C_pair04_ATT_PE_source_evidence_draft_20260614.csv`
- 원칙: AI/source-trace candidate는 review evidence이며, human/source adjudication을 대체하지 않는다.

## 예비 결론

- `04_ATT-PE`에서 supplemental input으로 바로 승격할 값: `0`
- 13개 row 모두 `ATT`가 측정 구성개념으로 확인되지 않았다.
- `PE` 또는 `PU`/performance-expectancy 대응 구성개념은 대체로 확인되지만, `ATT` 부재 때문에 ATT-PE 상관쌍은 만들 수 없다.
- AI 후보화의 주요 원인은 논문 본문/선행연구 설명의 일반 단어 `attitude` 또는 관련 연구 요약을 full10 `ATT` construct로 과탐지한 것으로 판단한다.

## Study-level 판단 요약

| study_id | 판단 | 핵심 근거 |
| --- | --- | --- |
| S004 | no promote | PE present as performance expectancy; ATT absent from correlation matrix constructs; 따라서 ATT-PE 상관값으로 보충 입력하지 않음. |
| S025 | no promote | PE present; measured constructs are UTAUT2/adoption-intention set; ATT absent; 따라서 ATT-PE 상관값으로 보충 입력하지 않음. |
| S035 | no promote | PE present; ChatGPT intention/adoption constructs present; ATT absent; 따라서 ATT-PE 상관값으로 보충 입력하지 않음. |
| S036 | no promote | PU/PE counterpart present; ATT absent from AI-ANX, AI-SE, BI, PEN, PEOU, PT, PU, SI matrix; 따라서 ATT-PE 상관값으로 보충 입력하지 않음. |
| S051 | no promote | PE present; usage intention/behavior and UTAUT factors present; ATT absent; 따라서 ATT-PE 상관값으로 보충 입력하지 않음. |
| S086 | no promote | PE present; PI, EE, IR, SI, FC, trust, BI, UB present; ATT absent; 따라서 ATT-PE 상관값으로 보충 입력하지 않음. |
| S088 | no promote | PE present; intention/use/trust/risk/tech-savviness model present; ATT appears only in narrative/literature context, not as measured construct; 따라서 ATT-PE 상관값으로 보충 입력하지 않음. |
| S121-1 | no promote | PE present for student SEM/PLS model; challenge/threat appraisal terms are not ATT; ATT absent; 따라서 ATT-PE 상관값으로 보충 입력하지 않음. |
| S121-2 | no promote | PE present for teacher SEM/PLS model; challenge/threat appraisal terms are not ATT; ATT absent; 따라서 ATT-PE 상관값으로 보충 입력하지 않음. |
| S157 | no promote | PE present; UTAUT2/SDT constructs include PC/PA/PR but not ATT; 따라서 ATT-PE 상관값으로 보충 입력하지 않음. |
| S173 | no promote | PE present; design/interactivity/ethics/trust and UTAUT constructs present; ATT absent; 따라서 ATT-PE 상관값으로 보충 입력하지 않음. |
| S191 | no promote | PE present; AU, BI, CSE, EE, FC, PE, PI, SI present; ATT absent; 따라서 ATT-PE 상관값으로 보충 입력하지 않음. |
| S223 | no promote | PU/PE counterpart present; PEU, BI, AU, SN, SE, trust/enjoyment/FC set present; ATT absent; 따라서 ATT-PE 상관값으로 보충 입력하지 않음. |

## 처리 원칙

- 위 row들은 Paper A supplemental input에 입력하지 않는다.
- 연구자가 원하면 개별 PDF를 다시 열어 ATT 측정문항 또는 상관표가 별도로 누락되었는지만 확인한다.
- 현재 source packet 수준에서는 `confirm_exclusion`이 타당하다.

## 다음 queue 위치

- 다음 full10 pair: `05_PE-SE`
