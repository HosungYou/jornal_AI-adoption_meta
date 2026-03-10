# Coding Protocol: Paper B

## 개요

전체 ~300 MASEM-eligible studies에 대한 3-Phase 코딩 프로토콜.
Paper B와 Paper A의 범위가 다르므로, 각 Phase에서의 적용 범위를 명시함.

### Paper A / Paper B 범위 구분

```
Phase 1: Gold Standard 구축 (100 studies)
  ├── 📘 Paper B 범위: 인간 독립 코딩 vs. AI 추출 비교 (핵심 분석)
  └── 📗 Paper A 범위: Gold standard 데이터를 MASEM에도 활용

Phase 2: AI-First Verification (나머지 ~200 studies)
  ├── 📘 Paper B 범위: ❌ (Paper B에서는 분석하지 않음)
  └── 📗 Paper A 범위: ✅ (MASEM 데이터 생산)

Phase 3: Quality Assurance (Phase 2의 10% spot-check)
  ├── 📘 Paper B 범위: ❌ (Paper B에서는 분석하지 않음)
  └── 📗 Paper A 범위: ✅ (데이터 품질 검증)
```

**Paper B에 보고되는 것**: Phase 1의 100 studies만 (인간 IRR + AI accuracy + consensus + workflow)
**Paper A에 보고되는 것**: Phase 1 + Phase 2 + Phase 3 전체 (~300 studies의 MASEM 데이터)

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

## Phase 2: AI-First Verification (~200 studies) — 📗 Paper A 전용

> **📘 Paper B**: 이 Phase는 Paper B의 분석 대상이 아님.
> Paper B Methods에서는 "the remaining studies were coded using an AI-first
> verification workflow, described in the parent meta-analysis (You, 2026)" 정도로 간략 언급.

### 목적
나머지 ~200 studies에 대해 AI consensus 결과를 인간이 검증.
Phase 1의 gold standard로 검증된 AI 성능을 기반으로,
나머지 studies에 대해서는 AI-first → Human verification 방식으로 효율적으로 코딩.

### 절차

```
Step 1: AI Consensus 생성
  ├── 3개 AI 모델 추출 결과 → consensus 알고리즘 적용
  │   ├── Categorical: 다수결 (2/3 이상 일치)
  │   ├── Continuous: 중앙값 (3개 모델 중)
  │   └── Unanimous = high confidence, Split = flag for review
  └── 결과: data/04_consensus/ai_consensus_remaining.csv

Step 2: Human Verification (Single Coding)
  ├── R1: ~38 studies 할당
  ├── R2: ~38 studies 할당
  ├── R3: ~37 studies 할당
  ├── R4: ~37 studies 할당
  ├── 각 study에 대해:
  │   ├── AI consensus 값 확인
  │   ├── 원문(PDF) 대조
  │   ├── 일치 시: Accept
  │   ├── 불일치 시: Human override + 사유 기록
  │   └── AI consensus에서 flag된 항목은 특별 주의
  └── 결과: verified_data_phase2.csv

Step 3: Override Rate 계산
  ├── 전체 override 비율 (%)
  ├── Variable type별 override 비율
  ├── AI model별 단독 오류 빈도
  └── 📗 Paper A Methods에 보고
```

### Verification Coding Sheet

각 data element에 대해:
- `ai_consensus_value`: AI 합의 값
- `human_verified_value`: 인간 확인 값
- `match`: TRUE/FALSE
- `override_reason`: 불일치 시 사유 (코딩 오류 / 원문 누락 / 변환 오류 / 기타)

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

| 기록 항목 | Phase 1 (📘B + 📗A) | Phase 2 (📗A only) | Phase 3 (📗A only) |
|----------|---------------------|-------------------|-------------------|
| 코더 ID | R1/R2 (Pair A) + R3/R4 (Pair B) + AI pipeline | R1-R4 (equal split) | R1-R4 (cross) |
| 코딩 날짜 | ✅ | ✅ | ✅ |
| Study ID | ✅ | ✅ | ✅ |
| 소요 시간 | ✅ | ✅ | ✅ |
| 원문 참조 위치 | ✅ | ✅ | ✅ |
| 의사결정 메모 | ✅ (개별) | ✅ (override 시) | ✅ (오류 시) |
| AI 모델 output | ❌ (H1/H2 blinded) | ✅ | ✅ |

---

## Phase별 범위 요약

| | Phase 1 | Phase 2 | Phase 3 |
|---|---------|---------|---------|
| **대상** | 100 studies | ~200 studies | Phase 2의 10% |
| **방법** | 인간 독립 코딩 + AI 독립 추출 | AI consensus → 인간 검증 | 독립 spot-check |
| **코더** | Pair A (R1+R2) + Pair B (R3+R4) + cross-pair adj. | R1-R4 (equal split, single coding) | R1-R4 (cross spot-check) |
| **📘 Paper B** | ✅ 핵심 분석 | ❌ | ❌ |
| **📗 Paper A** | ✅ Gold standard 활용 | ✅ 데이터 생산 | ✅ 품질 보증 |
| **Timeline** | Week 1-3 | Week 4-5 | Week 5-6 |
| **산출물** | gold_standard_100.csv | verified_data_phase2.csv | qa_report.md |
