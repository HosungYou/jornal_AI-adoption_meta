# Paper A/C full10 pair 06_PE-TRU source evidence review log (2026-06-14)

## 검토 범위

- 대상 pair: `06_PE-TRU`
- 큐 row 수: 10
- 검토 파일: `paper_a_C_pair06_PE_TRU_source_evidence_draft_20260614.csv`
- 원칙: AI/source-trace candidate는 review evidence이며, human/source adjudication을 대체하지 않는다.

## 예비 결론

- supplemental input으로 승격할 값: `0`
- 조건부 후보: `0`
- 핵심 사유: 값이 없어서가 아니라 construct-mapping gate에서 탈락했다. PE/PU 대응 construct는 여러 row에서 확인되지만, 같은 source table 안에 full10 `TRU`로 볼 수 있는 measured trust construct가 없다.
- 제외 원칙: `insecurity`, `privacy concerns`, `psychological risk`, `perceived risk`, `habit`, `perceived competence`, `perceived enjoyment`는 full10 `TRU`로 자동 매핑하지 않는다.

## Study-level 판단 요약

| study_id | 후보값 | 판단 | 핵심 근거 |
| --- | ---: | --- | --- |
| S016 |  | do_not_promote_construct_mapping_failure_no_TRU | PU/PE counterpart is present, but the measured variables are FC, OQ, SE, AIA, TTF, HM, PU, PEOU, ATT, BI. The phrase “Trust level analysis” labels reliability testing, not a trust construct. source-anchored human confirmation 전에는 supplemental input에 반영하지 않음. |
| S025 |  | do_not_promote_construct_mapping_failure_no_TRU | PE is present, but measured constructs are AU, ADI, ACI, CGSE, EE, FC, HAB, HM, PE, PV, SI. No trust/TRU construct appears in the matrix. source-anchored human confirmation 전에는 supplemental input에 반영하지 않음. |
| S051 |  | do_not_promote_construct_mapping_failure_no_TRU | Performance expectancy is present, but the matrix variables are usage behavior, social influence, perceived risk, facilitating conditions, performance expectancy, effort expectancy, and usage intention. Perceived risk is not full10 TRU. source-anchored human confirmation 전에는 supplemental input에 반영하지 않음. |
| S055 |  | do_not_promote_construct_mapping_failure_no_TRU | PE is present, but measured constructs are BI, EE, FC, HT, HM, PE, SI, USE. No trust/TRU construct. source-anchored human confirmation 전에는 supplemental input에 반영하지 않음. |
| S057 |  | do_not_promote_construct_mapping_failure_no_TRU | The study measures perceived usefulness, perceived ease of use, subjective norm, experience, perceived enjoyment, anxiety, self-efficacy, and UTAUT2 variables. No measured trust/TRU construct is visible. source-anchored human confirmation 전에는 supplemental input에 반영하지 않음. |
| S072 |  | do_not_promote_construct_mapping_failure_privacy_not_TRU | PE is present, but the relevant non-UTAUT factor is Privacy Concerns (PC), not trust. Do not map privacy concerns to full10 TRU. source-anchored human confirmation 전에는 supplemental input에 반영하지 않음. |
| S157 |  | do_not_promote_construct_mapping_failure_competence_not_TRU | PE is present, but PC denotes perceived competence and the SDT variables PA/PR denote autonomy/relatedness. None is trust/TRU. source-anchored human confirmation 전에는 supplemental input에 반영하지 않음. |
| S164 |  | do_not_promote_construct_mapping_failure_habit_not_TRU | PE is present, but H denotes habit in this study. Table 4 has AT, BI, EE, FC, GPTU, H, HM, PBC, PE, SN; no trust/TRU construct. source-anchored human confirmation 전에는 supplemental input에 반영하지 않음. |
| S185 |  | do_not_promote_construct_mapping_failure_insecurity_not_TRU | PU can map to PE, but the possible counterpart is INS/insecurity, not trust. Insecurity is an inhibiting TRI construct and should not be substituted for full10 TRU. source-anchored human confirmation 전에는 supplemental input에 반영하지 않음. |
| S190 |  | do_not_promote_construct_mapping_failure_wrong_PE_no_TRU | The table includes PU, EOU, PE, TPR, TTF, SI, WIL, where PE is perceived enjoyment rather than performance expectancy; no trust/TRU construct is measured. source-anchored human confirmation 전에는 supplemental input에 반영하지 않음. |

## 처리 원칙

- `TRU`는 measured trust/trustworthiness/perceived trust construct가 source table에 명시될 때만 full10 `TRU`로 취급한다.
- 보안 위험, 불안정성, 프라이버시 우려, 심리적 위험은 trust와 이론적으로 관련될 수 있으나, Paper A/B의 source-anchored coding에서는 `TRU` 대체값으로 승격하지 않는다.
- 따라서 이번 pair에서는 researcher confirmation template에 새로 승인 요청할 numeric candidate가 없다.

## 다음 queue 위치

- 다음 full10 pair: `07_ANX-PE`
