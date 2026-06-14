# Paper A S048 연구자 승인 및 model-family MASEM 재실행 기록

Date: 2026-06-15

## 1. 이번 실행의 결정

연구자는 `S048` Table 2에서 확인된 7개 source-visible Pearson correlation 값을 Paper A 보충 분석 입력으로 승인했다. 이 승인은 Paper A 분석 입력에만 적용되며 Paper B의 source-anchored adjudicated human reference standard를 변경하지 않는다.

승인된 값은 다음과 같다.

| Study | Pair | r | Source locator |
| --- | --- | ---: | --- |
| S048 | BI-FC | 0.424 | S048_doc1 page 13 chunk 1; Table 2 descriptive statistics and correlations; INT x FC |
| S048 | BI-PE | 0.659 | S048_doc1 page 13 chunk 1; Table 2 descriptive statistics and correlations; INT x PE |
| S048 | BI-SI | 0.626 | S048_doc1 page 13 chunk 1; Table 2 descriptive statistics and correlations; INT x SN |
| S048 | EE-UB | 0.398 | S048_doc1 page 13 chunk 1; Table 2 descriptive statistics and correlations; USE x EE |
| S048 | FC-UB | 0.340 | S048_doc1 page 13 chunk 1; Table 2 descriptive statistics and correlations; USE x FC |
| S048 | SI-UB | 0.589 | S048_doc1 page 13 chunk 1; Table 2 descriptive statistics and correlations; USE x SN |
| S048 | TRU-UB | 0.442 | S048_doc1 page 13 chunk 1; Table 2 descriptive statistics and correlations; USE x Trust |

## 2. 입력 데이터 처리 결과

최신 입력 파일에는 위 7개 값이 이미 `source-correction` 계층으로 들어와 있었다. 따라서 이번 작업은 중복 행 추가가 아니라, 기존 7행을 `researcher-approved supplemental Paper A S048 Table 2 source row`로 승격하는 방식으로 처리했다.

| Item | Result |
| --- | ---: |
| Upstream input rows | 836 |
| Output input rows | 836 |
| Existing S048 rows promoted | 7 |
| New duplicated rows inserted | 0 |
| Paper B reference standard mutated | no |

분석 입력 파일: `data/04_extraction/05_llm_masem_substitution/results/paper_a_researcher_approved_s048_supplement_20260615/paper_a_source_corrected_plus_researcher_approved_anx_tru_pe_se_s048_input_20260615.csv`

## 3. Partial/sparse matrix MASEM 실행 결과

Sparse partial-matrix TSSEM은 세 route 모두에서 Stage 1이 실패했다. 이유는 이전과 동일하게 sparse partial input에서 metaSEM/OpenMx의 implied covariance가 positive definite가 아니었기 때문이다. 따라서 sparse partial-matrix 결과는 구조경로 추정치로 보고하지 않는다.

| Route | Required pairs | Observed pairs | Missing pooled pairs | Min pair k | Partial studies | Complete-case studies | TSSEM1 | Stage 2 | Pairwise pooled min eigen |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | ---: |
| core7 ATT mediation | 21 | 21 | 0 | 11 | 72 | 4 | failed | not_run | 0.3142 |
| trust6 trust mechanism | 15 | 15 | 0 | 9 | 73 | 7 | failed | not_run | 0.3152 |
| full10 theoretical target | 45 | 45 | 0 | 1 | 77 | 0 | failed | not_run | -0.0109 |

Full10은 pairwise evidence map 기준으로는 45/45 pair coverage를 갖지만, 같은 연구 내 complete 10-construct matrix가 0개이므로 단일 full10 SEM으로 주장할 수 없다. Pairwise pooled full10 matrix도 positive definite가 아니며 nearPD 보정은 진단용으로만 생성했고 본문 추론에는 사용하지 않는다.

## 4. Complete-case TSSEM/MASEM 결과

Complete-case route에서는 reduced empirical model family가 수렴했다.

| Route | Candidate complete cases | Positive-definite complete cases | Study IDs | Stage 1 | Stage 2 |
| --- | ---: | ---: | --- | --- | --- |
| core7 ATT mediation | 4 | 4 | S048; S055; S176; S214 | converged | converged |
| trust6 trust mechanism | 7 | 7 | S004; S048; S121; S121-1; S121-2; S173; S176 | converged | converged |
| full10 theoretical target | 0 | 0 |  | not_run | not_run |

## 5. Model fit

| Model | chisq | df | p | CFI | TLI | RMSEA | SRMR | AIC | BIC |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| core7 ATT mediation | 6.146 | 5 | 0.292 | 0.999 | 0.996 | 0.009 | 0.043 | -3.854 | -34.165 |
| trust6 trust mechanism | 8.957 | 4 | 0.062 | 0.996 | 0.985 | 0.011 | 0.040 | 0.957 | -28.008 |

## 6. Structural path estimates

### core7 ATT mediation

| Path | Estimate |
| --- | ---: |
| PE_to_ATT | 0.157 |
| EE_to_ATT | 0.127 |
| SI_to_ATT | 0.107 |
| FC_to_ATT | 0.336 |
| ATT_to_BI | 0.512 |
| PE_to_BI | 0.187 |
| EE_to_BI | 0.122 |
| SI_to_BI | 0.190 |
| FC_to_UB | 0.332 |
| BI_to_UB | 0.575 |

### trust6 trust mechanism

| Path | Estimate |
| --- | ---: |
| PE_to_TRU | 0.261 |
| EE_to_TRU | 0.140 |
| SI_to_TRU | 0.107 |
| TRU_to_BI | 0.243 |
| PE_to_BI | 0.365 |
| EE_to_BI | 0.225 |
| SI_to_BI | 0.184 |
| BI_to_UB | 0.714 |

## 7. 해석 및 다음 manuscript 방향

가장 방어 가능한 route는 `full10 theoretical target + reduced empirical model-family MASEM`이다. 즉 full10은 이론적 대상 및 coverage/evidence map으로 유지하고, 실제 구조경로 추정은 source-supported complete-case가 가능한 `core7`과 `trust6` route로 보고하는 것이 타당하다.

중요한 경계는 다음과 같다.

- Full10 전체 route는 pairwise coverage는 충분하지만 complete-case matrix가 0개이므로 단일 primary SEM으로 보고하면 안 된다.
- Sparse partial-matrix TSSEM은 non-positive definite implied covariance 오류로 실패했으므로, 이 route의 구조경로를 manuscript 결과로 쓰면 안 된다.
- Trust, anxiety, self-efficacy는 moderator가 아니라 mechanism/mediator 후보 construct로 유지한다. 다만 현재 수렴한 empirical MASEM에서는 trust6만 trust mediator/mechanism route로 구조적으로 추정되며, anxiety와 self-efficacy는 full10 evidence map 또는 추가 source densification 후 reduced extension에서 다루는 것이 맞다.
- S004 `PKC -> SE`, S121 `threat appraisal -> ANX`, S072 construct-mapping audit rows는 이번 입력에 추가하지 않았다.

## 8. 다음 작업

1. Paper A Methods에 `model-family MASEM` route를 명시하고 full10을 theoretical target/evidence map으로 둔 근거를 정리한다.
2. Paper A Results에 위 complete-case core7/trust6 fit table과 structural path table을 삽입한다.
3. Figure/Table 산출물은 `full10 evidence coverage map`, `core7 path diagram`, `trust6 path diagram`, `model-family eligibility table` 순서로 만든다.
4. Anxiety/self-efficacy mediation은 현재 primary MASEM claim이 아니라 feasibility/supplementary mechanism discussion으로 처리한다.
