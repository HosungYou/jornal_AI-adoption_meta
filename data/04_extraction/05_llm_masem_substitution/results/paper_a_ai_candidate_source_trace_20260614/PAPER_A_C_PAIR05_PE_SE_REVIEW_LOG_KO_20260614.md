# Paper A/C full10 pair 05_PE-SE source evidence review log (2026-06-14)

## 검토 범위

- 대상 pair: `05_PE-SE`
- 큐 row 수: 13
- 검토 파일: `paper_a_C_pair05_PE_SE_source_evidence_draft_20260614.csv`
- 원칙: AI/source-trace candidate는 review evidence이며, human/source adjudication을 대체하지 않는다.

## 예비 결론

- 즉시 supplemental input으로 승격할 값: `0`
- 조건부 후보: `2` (`S121-1`, `S121-2`)
- 조건: `genAI-related subjective competence`를 full10 `SE`로 인정할지 연구자가 확인해야 한다. 인정될 경우 Figure 2에서 학생 표본 `r = .40`, 교사 표본 `r = .30`이 후보값이다.
- 나머지 11개 row는 measured self-efficacy construct가 없거나, `SE`가 Security/PBC/일반 효능감 표현으로 감지된 오탐이다.

## Study-level 판단 요약

| study_id | 후보값 | 판단 | 핵심 근거 |
| --- | ---: | --- | --- |
| S004 |  | do_not_promote_construct_mapping_failure_no_SE | PE present; no measured self-efficacy construct in matrix. PKC is perceived knowledge, not SE.; source-anchored human confirmation 전에는 supplemental input에 반영하지 않음. |
| S030 |  | do_not_promote_construct_mapping_failure_no_SE | PU present; PBC/perceived behavioral control is present but not coded as full10 self-efficacy under current rule. Self-efficacy appears in narrative/TPB background only.; source-anchored human confirmation 전에는 supplemental input에 반영하지 않음. |
| S055 |  | do_not_promote_construct_mapping_failure_no_SE | PE present; measured constructs are BI, EE, FC, HT, HM, PE, SI, USE. No self-efficacy construct.; source-anchored human confirmation 전에는 supplemental input에 반영하지 않음. |
| S072 |  | do_not_promote_construct_mapping_failure_no_SE | PE present; measured constructs include PE, EE, SI, FC, HM, privacy concerns, learning value, habit, robotics adoption, BI, VTA use. No self-efficacy construct.; source-anchored human confirmation 전에는 supplemental input에 반영하지 않음. |
| S088 |  | do_not_promote_construct_mapping_failure_no_SE | PE present; model includes intention/use/trust/risk/tech-savviness, not measured self-efficacy.; source-anchored human confirmation 전에는 supplemental input에 반영하지 않음. |
| S121-1 | 0.40 | candidate_value_found_requires_human_mapping_confirmation | Conditional candidate: performance expectancy and genAI-related subjective competence correlate at Spearman r=.40 for students. Requires researcher confirmation that subjective competence maps to full10 SE.; source-anchored human confirmation 전에는 supplemental input에 반영하지 않음. |
| S121-2 | 0.30 | candidate_value_found_requires_human_mapping_confirmation | Conditional candidate: performance expectancy and genAI-related subjective competence correlate at Spearman r=.30 for teachers. Requires researcher confirmation that subjective competence maps to full10 SE.; source-anchored human confirmation 전에는 supplemental input에 반영하지 않음. |
| S173 |  | do_not_promote_construct_mapping_failure_no_SE | PE present; no measured self-efficacy construct in discriminant-validity matrix.; source-anchored human confirmation 전에는 supplemental input에 반영하지 않음. |
| S176 |  | do_not_promote_construct_mapping_failure_no_SE | PE present; no measured self-efficacy construct. Self-efficacy appears only in cited/background references, not as a study variable.; source-anchored human confirmation 전에는 supplemental input에 반영하지 않음. |
| S185 |  | do_not_promote_construct_mapping_failure_no_SE | PU present; PBC contains ability/control wording but is not full10 self-efficacy under current rule. Self-efficacy appears only as background/future external factor/reference.; source-anchored human confirmation 전에는 supplemental input에 반영하지 않음. |
| S190 |  | do_not_promote_construct_mapping_failure_no_SE | PU/perceived usefulness present; no self-efficacy construct. PE abbreviation in this paper can refer to perceived enjoyment, not full10 PE-SE.; source-anchored human confirmation 전에는 supplemental input에 반영하지 않음. |
| S214 |  | do_not_promote_construct_mapping_failure_no_SE | PE present; measured constructs are BI, EE, FC, GPTU, H, HM, PE, SI. No self-efficacy construct.; source-anchored human confirmation 전에는 supplemental input에 반영하지 않음. |
| S223 |  | do_not_promote_construct_mapping_failure_wrong_SE | PU present and a table value with SE exists, but SE denotes Security, not self-efficacy. Do not map to full10 SE.; source-anchored human confirmation 전에는 supplemental input에 반영하지 않음. |

## 처리 원칙

- `S121-1/S121-2`는 값 후보를 보존하되, 연구자 확인 전에는 `promote_to_supplemental_input=pending`으로 유지한다.
- `PBC`, `Security`, 일반 `efficacy` 표현, 참고문헌의 self-efficacy는 full10 `SE`로 자동 매핑하지 않는다.
- 현재 기준에서는 `S121`만 researcher checkpoint 대상이다.

## 다음 queue 위치

- 다음 full10 pair: `06_PE-TRU`
