# Sampling Protocol: 575 → MASEM Corpus → Phase 1/2 Human Reference Data

## 개요

Paper B의 validation sample과 Paper A의 final extraction corpus를 확보하기 위한
프로세스. 스크리닝(16,189 → 575)은 Paper A의 범위이며, Paper B에서는 필요한
범위만 추적한다.

**Protocol amendment, 2026-04-24**: Phase 1 is complete. Phase 2 will use
rotated human pairs (R1+R4, R2+R3) rather than AI-first single verification.

```
575 AI-screened Include
        │
        ▼
   [Stage 1] Full-Text Eligibility Review
   MASEM-specific criteria 적용
        │
        ▼
   ~300 MASEM-Eligible Studies
   (Paper A 전체 데이터셋)
        │
        ▼
   [Stage 2] Stratified Random Sampling
   층화무작위추출 (seed=42)
        │
        ▼
   Phase 1 Validation Set → primary Paper B reference sample
   (completed 4-coder/2-pair design: R1+R2, R3+R4)
        │
        ▼
   Phase 2 Remaining Eligible Studies → Paper A final dataset
   (rotated pairs: R1+R4, R2+R3)
```

---

## Stage 1: Full-Text Eligibility (575 → ~300)

### 목적
AI 스크리닝에서 "Include"로 판정된 575개 논문의 full-text를 검토하여
MASEM에 실제로 사용 가능한 연구만 선별

### 담당
- **PI (R1)**: 전체 575개 full-text review
- **R2**: 30% random sample (173개) 독립 review → IRR 확인
- **R3, R4**: Phase 1 코딩에 참여 (4 coders, 2 pairs)

### MASEM-Specific Eligibility Criteria

**포함 기준 (ALL 충족 필요)**:
1. 12개 target constructs 중 ≥ 2개의 construct-pair 통계 보고
2. Correlation matrix (r) 또는 standardized path coefficients (β) 보고
3. Quantitative effect size 추출 가능
4. 독립 표본 (duplicate sample 아님)
5. Full paper (conference abstract only 아님)

### Full-Text Exclusion Codes

| 코드 | 사유 | 예상 비율 |
|------|------|----------|
| **E-FT1** | < 2 construct-pair 통계 보고 | ~15% |
| **E-FT2** | Constructs가 12-construct model에 매핑 불가 | ~10% |
| **E-FT3** | Quantitative effect size 추출 불가 | ~10% |
| **E-FT4** | Duplicate sample (다른 포함 연구와 동일 표본) | ~5% |
| **E-FT5** | Conference abstract only (full paper 아님) | ~5% |
| **E-FT6** | Full-text 접근 불가 | ~5% |

### 프로세스

```
Step 1: PDF 수집
  ├── Open access → 직접 다운로드
  ├── Penn State Libraries → 기관 접근
  ├── 접근 불가 → Interlibrary Loan 요청
  └── 저자 직접 연락 (최후 수단)

Step 2: Full-text 스크리닝
  ├── PI가 575개 전체 review
  ├── 각 논문에 대해:
  │   ├── Correlation matrix 존재 여부 확인
  │   ├── Construct 매핑 가능성 확인
  │   ├── Sample size 확인 (n ≥ 50)
  │   └── Exclude code 부여 (해당 시)
  └── 결과: fulltext_eligibility_decisions.csv

Step 3: IRR 확인
  ├── R2가 30% random sample 독립 review
  ├── Cohen's κ 계산 (Include/Exclude 결정)
  ├── Target: κ ≥ 0.85
  └── Disagreement → 논의 후 합의

Step 4: 최종 MASEM-eligible 목록 확정
  └── ~300 studies (예상)
```

### Output Files

```
data/00_fulltext_eligibility/
├── fulltext_eligibility_decisions.csv
│   Columns: study_id, title, first_author, year, doi,
│            decision (include/exclude), exclude_code,
│            exclude_reason, num_constructs_identified,
│            has_correlation_matrix (yes/no/beta_only),
│            reviewer_id, review_date
│
├── fulltext_irr_sample.csv
│   (30% sample for IRR, PhD 1의 독립 판정 포함)
│
├── fulltext_irr_results.md
│   (κ 값, disagreement 분석)
│
└── excluded_studies_log.csv
    (제외된 연구 목록 + 사유)
```

---

## Stage 2: Phase 1 Validation Sampling (~300 → 100)

### 목적
Paper B의 primary validation sample을 위한 100개 연구를 ~300개에서 층화무작위추출.
이 단계는 Phase 1 pairwise workbook 기준으로 완료되었다.

### 층화 변수 (Stratification Variables)

| 변수 | 층 (Strata) | 근거 |
|------|------------|------|
| **Publication year** | 2022-2023 / 2024 / 2025-2026 | AI 연구의 시간적 변화 반영 |
| **AI tool type** | Chatbot-LLM / ITS / LMS-AI / Other | 도구별 보고 패턴 차이 |
| **Education level** | K-12 / Undergraduate / Graduate-Mixed | 교육 수준별 연구 특성 차이 |
| **Region** | East Asia / South-SE Asia / Middle East-Africa / Western | 지역별 보고 관행 차이 |

### 추출 방법

**Proportional stratified random sampling**:
- 각 stratum에서 원래 비율에 비례하여 추출
- 최소 stratum 크기: 3 studies (이하이면 해당 stratum 전체 포함)
- Random seed: 42 (reproducibility)

### 실행 스크립트

```python
# scripts/select_paper_b_sample.py

import pandas as pd
import numpy as np

# Config
SEED = 42
TARGET_N = 100

# Load MASEM-eligible studies
df = pd.read_csv('data/00_fulltext_eligibility/fulltext_eligibility_decisions.csv')
eligible = df[df['decision'] == 'include'].copy()

# Define strata
eligible['year_stratum'] = pd.cut(
    eligible['year'],
    bins=[2021, 2023, 2024, 2027],
    labels=['2022-2023', '2024', '2025-2026']
)

# Proportional allocation
strata_counts = eligible.groupby(
    ['year_stratum', 'ai_tool_type', 'education_level', 'region']
).size()

# Calculate proportional sample sizes
proportions = strata_counts / len(eligible)
sample_sizes = (proportions * TARGET_N).round().astype(int)
sample_sizes = sample_sizes.clip(lower=1)  # minimum 1 per stratum

# Adjust to exactly 100
while sample_sizes.sum() != TARGET_N:
    if sample_sizes.sum() > TARGET_N:
        # Remove from largest stratum
        idx = sample_sizes.idxmax()
        sample_sizes[idx] -= 1
    else:
        # Add to largest available stratum
        idx = (strata_counts - sample_sizes).idxmax()
        sample_sizes[idx] += 1

# Sample
np.random.seed(SEED)
sampled = []
for stratum, n in sample_sizes.items():
    stratum_df = eligible[
        (eligible['year_stratum'] == stratum[0]) &
        (eligible['ai_tool_type'] == stratum[1]) &
        (eligible['education_level'] == stratum[2]) &
        (eligible['region'] == stratum[3])
    ]
    if len(stratum_df) <= n:
        sampled.append(stratum_df)
    else:
        sampled.append(stratum_df.sample(n=n, random_state=SEED))

sample = pd.concat(sampled)
sample.to_csv('data/01_sample_selection/paper_b_sample_100.csv', index=False)
print(f"Selected {len(sample)} studies for Paper B gold standard")
```

### Output Files

```
data/01_sample_selection/
├── paper_b_sample_100.csv
│   Columns: study_id, title, first_author, year, doi,
│            journal, ai_tool_type, education_level,
│            region, year_stratum, sample_size_n
│
├── sampling_report.md
│   (층화 분포, 비례 할당 결과, 대표성 검증)
│
├── sample_vs_population_comparison.csv
│   (100개 sample vs ~300개 population의 특성 비교)
│
└── sampling_seed_log.txt
    (seed=42, timestamp, script version)
```

### 대표성 검증

100개 sample이 ~300개 population을 대표하는지 확인:
- Chi-square test (categorical variables)
- t-test / Mann-Whitney U (continuous variables)
- Effect size (Cramér's V, Cohen's d)
- 결과를 Paper B Methods에 보고

---

## Stage 3: Phase 2 Rotated-Pair Assignment

### 목적

Phase 1에서 제외된 remaining eligible studies를 Paper A의 final MASEM-ready
dataset으로 확정하기 위해 독립 인간 double coding을 실시한다. Phase 2에서는
Phase 1 pair를 반복하지 않고 R1+R4, R2+R3로 pair를 회전시켜 pair-specific
coding habits를 줄인다.

### 배정 규칙

| Pair | Coders | Assignment principle | Adjudication |
|---|---|---|---|
| Pair C | R1 + R4 | Remaining eligible studies의 절반 | R2 primary, R3 secondary if needed |
| Pair D | R2 + R3 | Remaining eligible studies의 절반 | R1 primary, R4 secondary if needed |

Assignment should be frozen before coding begins and logged with:

- `study_id`
- `phase`
- `pair_id`
- `coder_a`
- `coder_b`
- stratification variables used for balancing
- assignment timestamp
- random seed or manual-balancing rationale

### Paper B 사용 범위

Phase 2는 Paper B의 primary validation sample을 대체하지 않는다. 다만 Phase 2
assignment와 adjudication이 LLM comparison 이전에 고정되어 있으면, Phase 2는
external validation, triage sensitivity, 또는 human-workload simulation으로 사용할 수
있다.

## 스크리닝은 Paper B 범위 밖

| 단계 | Paper A 범위 | Paper B 범위 |
|------|-------------|-------------|
| Database search (22,166 → 16,189) | ✅ | ❌ |
| AI screening (16,189 → 575) | ✅ | ❌ |
| Human screening review | ✅ | ❌ |
| **Full-text eligibility (575 → ~300)** | ✅ | ✅ (Stage 1) |
| **Stratified sampling (~300 → 100)** | — | ✅ (Stage 2) |
| **Phase 1 human reference coding (100, 4 coders/2 pairs)** | ✅ (ICR) | ✅ (primary validation) |
| **Phase 2 rotated-pair human coding** | ✅ (핵심) | Optional external validation/triage sensitivity |
| **LLM extraction evaluation** | — | ✅ (핵심 for Phase 1; optional for Phase 2) |
| **Full dataset coding (~300)** | ✅ (핵심) | — |

Paper B의 Methods에서는 Stage 1 (full-text eligibility)부터 기술하되,
screening 과정은 "described in detail in the parent meta-analysis (You, 2026)"로 간략히 언급.
