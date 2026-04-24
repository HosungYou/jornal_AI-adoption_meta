# Coding Protocol: Paper B

## 개요

전체 MASEM-eligible studies에 대한 human-first extraction protocol.
Paper B와 Paper A의 범위가 다르므로, 각 Phase에서의 적용 범위를 명시함.

**Protocol amendment, 2026-04-24**: Phase 1 pairwise coding is complete.
Phase 2 is reset from the earlier AI-first single-verification plan to a
rotated-pair human coding design: Pair C = R1+R4 and Pair D = R2+R3. AI outputs
remain blinded during independent human coding and are used after adjudication
for LLM augmentation, triage, and substitution analyses.

### Paper A / Paper B 범위 구분

```
Phase 1: Initial Human Reference Standard 구축 (100 studies; completed)
  ├── Pair A: R1+R2
  ├── Pair B: R3+R4
  ├── 📘 Paper B 범위: 인간 독립 코딩 vs. LLM workflow 비교의 primary validation sample
  └── 📗 Paper A 범위: adjudicated extraction data를 MASEM에도 활용

Phase 2: Rotated-Pair Human Coding (remaining eligible studies)
  ├── Pair C: R1+R4
  ├── Pair D: R2+R3
  ├── 📘 Paper B 범위: optional external/operational validation 또는 triage sensitivity
  └── 📗 Paper A 범위: final MASEM extraction dataset 생산

Phase 3: Quality Assurance (Phase 2의 10% spot-check)
  ├── 📘 Paper B 범위: ❌ (Paper B에서는 분석하지 않음)
  └── 📗 Paper A 범위: ✅ (데이터 품질 검증)
```

**Paper B에 보고되는 것**: Phase 1을 primary validation sample로 보고한다. Phase 2는
분석 전에 protocol amendment로 고정된 경우에만 external validation, triage
sensitivity, 또는 workload simulation으로 보고한다.
**Paper A에 보고되는 것**: Phase 1 + Phase 2 + Phase 3 전체의 adjudicated
MASEM-ready extraction data.

---

## 코딩 변수 (30개)

### Module A: Bibliographic (8 variables)

| # | Variable | Type | 코딩 규칙 |
|---|----------|------|----------|
| A1 | `study_id` | ID | 자동 부여 (S001-S100) |
| A2 | `first_author` | Text | 성(last name) 기준, et al. 불필요 |
| A3 | `year` | Numeric | 출판 연도 (online first 기준) |
| A4 | `journal` | Text | 저널 전체 이름 (약어 아님) |
| A5 | `doi` | Text | DOI 전체 URL |
| A6 | `country` | Categorical | 데이터 수집 국가 (다국가: primary 기준) |
| A7 | `sample_size_n` | Numeric | 최종 분석에 사용된 N |
| A8 | `study_design` | Categorical | Cross-sectional / Longitudinal / Experimental / Mixed |

### Module B: Statistical (12 variables)

| # | Variable | Type | 코딩 규칙 |
|---|----------|------|----------|
| B1 | `matrix_type` | Categorical | Correlation (r) / Path coefficient (β) / Both |
| B2 | `num_constructs_reported` | Numeric | 보고된 construct 수 |
| B3-B12 | `r_[construct_pair]` | Numeric | Correlation/path coefficient (-1.00 ~ 1.00) |

**Correlation coding rules**:
- r 값 직접 보고 → 그대로 코딩
- β만 보고 → Peterson & Brown (2005) 변환: r ≈ β + .05λ (λ = 1 if β ≥ 0, λ = 0 if β < 0)
- 변환 시 `conversion_flag = TRUE` 표시
- 유의하지 않은 결과도 반드시 코딩 (p > .05도 포함)
- 보고 안 된 construct-pair → `NA` (빈칸 아님)

### Module C: Construct Classification (6 variables)

| # | Variable | Type | 코딩 규칙 |
|---|----------|------|----------|
| C1 | `constructs_measured` | List | 12개 target constructs 중 측정된 것들 |
| C2 | `construct_mapping_notes` | Text | 논문의 원래 construct명 → 12-construct 매핑 근거 |
| C3 | `measurement_instrument` | Text | 사용된 척도명 (예: TAM3, UTAUT2) |
| C4 | `ai_tool_studied` | Categorical | Chatbot-LLM / ITS / LMS-AI / Other |
| C5 | `ai_tool_name` | Text | 구체적 도구명 (예: ChatGPT, Copilot) |
| C6 | `education_level` | Categorical | K-12 / Undergraduate / Graduate / Mixed |

### Module D: Moderator (4 variables)

| # | Variable | Type | 코딩 규칙 |
|---|----------|------|----------|
| D1 | `region` | Categorical | East Asia / South-SE Asia / Middle East-Africa / Western |
| D2 | `subject_area` | Text | 학문 분야 (STEM, Social Science, Language, Mixed 등) |
| D3 | `mandatory_voluntary` | Categorical | Mandatory / Voluntary / Not specified |
| D4 | `duration_weeks` | Numeric | AI 사용 기간 (주 단위, 보고 시) |

---

## Phase 1: Gold Standard 구축 (100 studies) — 📘 Paper B 핵심 / 📗 Paper A 활용

### 목적
100개 gold standard studies에 대해 4명의 인간 코더(R1-R4)가 2개 독립 pair로 코딩하고,
3개 AI 모델이 동일 studies를 독립 추출. Gold standard 대비 AI 정확도 평가.
- Phase 0 (Calibration): 전체 4명이 동일 10 studies 코딩 → κ ≥ 0.80 확인
- Phase 1: Pair A (R1+R2) = 50 studies, Pair B (R3+R4) = 50 studies
- Cross-pair adjudication: R1이 Pair B 불일치 중재, R3가 Pair A 불일치 중재

### Step 1: AI Extraction (Week 1)

```
3개 모델 × 100 studies × 4 modules = 1,200 API calls

1. Claude CLI (Anthropic) [claude-sonnet-4-6]
   ├── Interface: Claude CLI
   ├── Temperature: 0
   ├── Max tokens: 4096
   └── Prompt: prompts/module_a-d (순차 실행)

2. Codex CLI (OpenAI) [latest]
   ├── Interface: Codex CLI
   ├── Temperature: 0
   ├── Max tokens: 4096
   └── Prompt: 동일 prompt 사용

3. Gemini CLI (Google) [gemini-2.5-flash]
   ├── Interface: Gemini CLI
   ├── Temperature: 0
   ├── Max tokens: 4096
   └── Prompt: 동일 prompt 사용
```

### Step 2: Independent Human Coding (Week 2-3)

```
Step 2a: 코딩 시트 배포
  ├── Pair A (R1+R2): 50 studies 할당, 각자 template 사본 받음
  ├── Pair B (R3+R4): 50 studies 할당, 각자 template 사본 받음
  └── 각자 별도 폴더에서 작업 (pair_a/coder_r1/, pair_a/coder_r2/, pair_b/coder_r3/, pair_b/coder_r4/)

Step 2b: 독립 코딩
  ├── Pair A: 50 studies × 30 variables = 1,500 data elements (R1, R2 각각)
  ├── Pair B: 50 studies × 30 variables = 1,500 data elements (R3, R4 각각)
  ├── 일일 목표: 10 studies/day × 5 days (per coder)
  ├── 예상 소요: 30-45 min/study
  ├── PDF에서 직접 추출 (AI 결과 참조 불가)
  └── 불명확한 경우: 개별 메모 작성 → 주간 미팅에서 논의

Step 2c: 코딩 시트 제출
  ├── Week 3 Day 2까지 동시 제출
  ├── 제출 전 pair 내 상대방 결과 열람 불가
  └── 제출 형식: CSV (UTF-8)
```

### Step 3: IRR + Gold Standard (Week 3)

```
Step 3a: Unblinding + IRR 계산
  ├── Pair A: R1 vs. R2 코딩 시트 비교 (50 studies)
  ├── Pair B: R3 vs. R4 코딩 시트 비교 (50 studies)
  ├── IRR 계산 (templates/irr_calculation_template.R)
  │   ├── Categorical: Cohen's κ (pair 내), Gwet's AC2
  │   ├── Continuous: ICC(2,1), ICC(2,k)
  │   └── Per-variable breakdown (pair별 + 전체)
  └── 결과: data/06_analysis/irr_results.csv

Step 3b: Discrepancy Resolution (Cross-Pair Adjudication)
  ├── 불일치 항목 목록 생성 (discrepancy_log.csv)
  ├── Pair A 불일치 → R3 (cross-pair adjudicator)가 독립 검토
  ├── Pair B 불일치 → R1 (cross-pair adjudicator)가 독립 검토
  ├── 각 불일치에 대해:
  │   ├── Adjudicator가 독립적으로 원문 검토
  │   ├── 코딩 규칙 적용
  │   └── Pair 내 합의 시도 → 불가 시 adjudicator 최종 결정
  └── 합의 불가 시: cross-pair adjudicator 최종 결정권

Step 3c: Gold Standard 확정
  ├── Pair 내 일치 → 채택
  ├── Pair 내 불일치 → cross-pair adjudicator 중재 후 확정
  ├── 저장: data/05_gold_standard/gold_standard_100.csv
  ├── 📘 Paper B: AI 평가의 ground truth
  └── 📗 Paper A: MASEM 데이터로도 활용
```

### Step 4: AI vs. Gold Standard 비교 (Week 3-4) — 📘 Paper B 전용

```
비교 구조:

                   100 Studies
                       │
         ┌─────────────┼─────────────┐
         ▼             │             ▼
   50 Studies (Pair A) │     50 Studies (Pair B)
    R1 + R2 독립코딩   │      R3 + R4 독립코딩
         │             │             │
         ▼             │             ▼
    IRR (R1 vs R2)     │      IRR (R3 vs R4)
         │             │             │
         ▼             │             ▼
  R3 cross-pair adj.   │   R1 cross-pair adj.
         │             │             │
         └──────┬──────┘──────┬──────┘
                ▼             ▼
          Gold Standard    AI Models (독립추출)
          (100 studies)    Claude / Codex / Gemini
                │             │
                │        ┌────┴────┐────┐
                │        ▼         ▼    ▼
                │     Claude   Codex  Gemini
                │        │         │    │
                │        └────┬────┘────┘
                │             ▼
                │       AI Consensus
                │             │
                └──────┬──────┘
                       ▼
                비교 분석 (RQ1-4)
```

**📘 Paper B에 보고하는 분석**:
- RQ1: Individual AI vs. Gold Standard (κ, ICC, accuracy, F1, MAE)
- RQ2: Variable type별 정확도 차이 (Bibliographic > Statistical > Classificatory?)
- RQ3: Multi-model consensus vs. individual model
- RQ4: Workflow simulation (cost-effectiveness)

### 코딩 규칙 (Decision Rules)

1. **Correlation matrix 내 값 우선**: Table에 보고된 r 값 > text에 언급된 값
2. **Multiple samples**: 독립 표본이면 각각 코딩, 동일 표본이면 가장 큰 N 사용
3. **Multiple time points**: 가장 최근 시점 사용 (종단 연구)
4. **β 변환**: Peterson & Brown (2005) 공식 적용 + `conversion_flag` 표시
5. **유의하지 않은 결과**: 반드시 코딩 (누락 시 publication bias 증가)
6. **Construct 매핑 모호**: `construct_mapping_notes`에 근거 기록
7. **Missing data**: `NA`로 코딩 (빈칸 금지, 0과 구분)

---

## Phase 2: Rotated-Pair Human Coding — 📗 Paper A 핵심 / 📘 Paper B optional validation

> **Protocol amendment, 2026-04-24**: Phase 2 is no longer AI-first single
> verification. It uses independent human double coding with rotated pairs:
> Pair C = R1+R4 and Pair D = R2+R3.

### 목적
Phase 1에서 같은 pair로 형성된 합의 습관이나 pair-specific bias를 Phase 2에
그대로 가져오지 않기 위해 reviewer pairs를 교차 재구성한다. Phase 2의 주된
목적은 Paper A의 final MASEM-ready extraction dataset을 만들고, 동시에 Paper B의
LLM augmentation 논리를 더 큰 operational dataset에서 점검할 수 있는 audit trail을
남기는 것이다.

### 절차

```
Step 1: Phase 2 assignment freeze
  ├── Remaining eligible studies를 Pair C와 Pair D로 배정
  ├── Pair C: R1+R4
  ├── Pair D: R2+R3
  ├── Study assignment, pair_id, coder IDs, assignment timestamp 기록
  └── AI output은 independent coding 완료 전까지 비공개

Step 2: Independent human double coding
  ├── Pair C: R1과 R4가 동일 studies를 독립 코딩
  ├── Pair D: R2와 R3가 동일 studies를 독립 코딩
  ├── PDF 원문에서 직접 추출
  ├── 상대 코더 결과와 AI 결과 접근 금지
  ├── 모호한 construct mapping, beta/r 변환, sample mismatch는 notes에 기록
  └── 결과: data/04_extraction/phase2/{pair_c,pair_d}/coder_R*.xlsx 또는 csv

Step 3: Pairwise comparison and IRR
  ├── Pair C: R1 vs R4
  ├── Pair D: R2 vs R3
  ├── Categorical: percent agreement, Cohen's kappa, Gwet's AC1/AC2
  ├── Numeric: absolute error, tolerance-band agreement, ICC where appropriate
  └── 결과: data/04_extraction/phase2/phase2_irr_results.csv

Step 4: Cross-pair adjudication
  ├── Pair C 불일치: R2가 primary adjudicator, R3가 필요 시 secondary check
  ├── Pair D 불일치: R1이 primary adjudicator, R4가 필요 시 secondary check
  ├── Adjudicator는 원문 PDF와 코딩 매뉴얼만 기준으로 판단
  ├── 해결값, 근거 위치, rule applied, confidence 기록
  └── 결과: data/04_extraction/phase2/phase2_adjudicated.csv

Step 5: Post-adjudication LLM comparison
  ├── 인간 adjudicated value를 reference로 고정한 뒤 LLM output 공개
  ├── LLM vs human reference: field-level agreement, numeric error, error taxonomy
  ├── Human-human disagreement vs LLM-human disagreement 비교
  ├── Cross-model disagreement은 triage signal로만 사용
  └── 결과: data/04_extraction/phase2/llm_triage_analysis.csv
```

### Phase 2 Coding Sheet

각 data element에 대해:
- `phase`: `phase2`
- `pair_id`: `pair_c` 또는 `pair_d`
- `coder_id`: R1, R2, R3, R4
- `human_value`: 독립 코더의 원 코딩값
- `source_location`: page/table/appendix/paragraph
- `extraction_basis`: correlation matrix / path coefficient / text / appendix
- `conversion_flag`: beta-to-r 변환 여부
- `construct_mapping_confidence`: high / medium / low
- `coding_notes`: 모호성, 제외 근거, sample mismatch, scale orientation 이슈

### Phase 2 LLM Comparison Sheet

인간 adjudication 이후에만 생성한다.

- `human_reference_value`: adjudicated Phase 2 값
- `llm_primary_value`: prespecified primary LLM workflow output
- `llm_alt_values`: optional supplementary model outputs
- `match`: exact / within_tolerance / mismatch / not_reported
- `error_type`: wrong source / beta-r confusion / wrong sample / construct mismatch / exclusion error / other
- `triage_flag`: whether this field should have been routed to human review

---

## Phase 3: Quality Assurance — 📗 Paper A 전용

> **📘 Paper B**: 이 Phase는 Paper B의 분석 대상이 아님.

### 목적
Phase 2 결과의 독립적 품질 검증. Cross-check 방식으로 spot-check.

### 절차

```
Step 1: Random Sample 추출
  ├── Phase 2 verified data에서 10% random sample (~15 studies)
  ├── Random seed: 99 (reproducibility)
  └── 층화: R1-R4 담당분에서 균등 추출

Step 2: Independent Spot-Check
  ├── Cross-check: 다른 코더가 담당한 studies를 spot-check (~15 studies × 30 variables)
  ├── PDF 원문 대조
  ├── Error 발견 시 기록
  └── Error rate 계산: errors / total elements

Step 3: QA Gates
  ├── Gate 1: Error rate < 5% → PASS
  ├── Gate 2: Range check (r: -1 ~ 1, N: > 0 등)
  ├── Gate 3: Completeness (missing data < 10%)
  ├── Gate 4: Symmetry check (correlation matrix)
  └── 결과: qa_report.md

Step 4: 미달 시 대응
  ├── Error rate 5-10%: 해당 verifier의 전체 분 재검토
  ├── Error rate > 10%: Phase 2 전체 재검토
  └── Range/completeness 오류: 개별 수정
```

---

## AI Extraction Protocol (Phase 1 & 2 공통)

### Prompt Strategy

**모듈식 설계**: 4개 모듈로 분리하여 정확도 향상
- Module A: Bibliographic extraction
- Module B: Correlation/path coefficient extraction
- Module C: Construct classification
- Module D: Moderator coding

**각 모듈 구성**:
1. System instruction (역할 정의)
2. Variable definitions (코딩 매뉴얼 요약)
3. Decision rules (판단 기준)
4. Output format (JSON schema)
5. Few-shot examples (2-3개)

### AI Output 형식

```json
{
  "study_id": "S001",
  "model": "claude_cli_sonnet_4_6",
  "module": "A",
  "extraction_timestamp": "2026-03-01T10:30:00Z",
  "data": {
    "first_author": "Kim",
    "year": 2023,
    "journal": "Computers & Education",
    "country": "South Korea",
    "sample_size_n": 342,
    "study_design": "cross-sectional"
  },
  "confidence": {
    "first_author": "high",
    "year": "high",
    "sample_size_n": "medium"
  },
  "notes": "Sample size reported differently in abstract (N=350) vs methods (N=342). Used methods section value."
}
```

### Multi-Model Consensus Algorithm

```python
def calculate_consensus(claude_val, codex_val, gemini_val, var_type):
    values = [claude_val, codex_val, gemini_val]
    non_null = [v for v in values if v is not None]

    if var_type == 'categorical':
        # Majority vote
        from collections import Counter
        counts = Counter(non_null)
        most_common = counts.most_common(1)
        if most_common[0][1] >= 2:
            return {
                'value': most_common[0][0],
                'agreement': 'majority' if most_common[0][1] == 2 else 'unanimous',
                'confidence': 'high' if most_common[0][1] == 3 else 'medium'
            }
        else:
            return {'value': None, 'agreement': 'split', 'confidence': 'low'}

    elif var_type == 'continuous':
        # Median + range check
        import numpy as np
        median_val = np.median(non_null)
        range_val = max(non_null) - min(non_null)
        return {
            'value': round(median_val, 3),
            'agreement': 'unanimous' if range_val < 0.01 else 'majority' if range_val < 0.05 else 'divergent',
            'confidence': 'high' if range_val < 0.01 else 'medium' if range_val < 0.05 else 'low'
        }
```

---

## Audit Trail 요구사항

| 기록 항목 | Phase 1 (📘B + 📗A) | Phase 2 (📗A + optional 📘B) | Phase 3 (📗A only) |
|----------|---------------------|-------------------|-------------------|
| 코더 ID | R1/R2 (Pair A) + R3/R4 (Pair B) + LLM pipeline | R1/R4 (Pair C) + R2/R3 (Pair D) + LLM pipeline after adjudication | R1-R4 (cross) |
| 코딩 날짜 | ✅ | ✅ | ✅ |
| Study ID | ✅ | ✅ | ✅ |
| 소요 시간 | ✅ | ✅ | ✅ |
| 원문 참조 위치 | ✅ | ✅ | ✅ |
| 의사결정 메모 | ✅ (개별) | ✅ (override 시) | ✅ (오류 시) |
| AI 모델 output | ❌ (human coding 완료 전까지 blinded) | ❌ independent coding/adjudication 전까지 blinded; 이후 comparison용 공개 | ✅ |

---

## Phase별 범위 요약

| | Phase 1 | Phase 2 | Phase 3 |
|---|---------|---------|---------|
| **대상** | 100 studies | Remaining eligible studies | Phase 2의 10% |
| **방법** | 인간 독립 코딩 + LLM 독립 추출 | Rotated-pair human double coding → adjudication → LLM comparison | 독립 spot-check |
| **코더** | Pair A (R1+R2) + Pair B (R3+R4) + cross-pair adj. | Pair C (R1+R4) + Pair D (R2+R3) + cross-pair adj. | R1-R4 (cross spot-check) |
| **📘 Paper B** | ✅ primary validation | Optional external validation/triage sensitivity | ❌ |
| **📗 Paper A** | ✅ Gold standard 활용 | ✅ 데이터 생산 | ✅ 품질 보증 |
| **Timeline** | Completed | Next phase | After Phase 2 |
| **산출물** | phase1_adjudicated_reference.csv | phase2_adjudicated.csv + phase2_llm_comparison.csv | qa_report.md |
