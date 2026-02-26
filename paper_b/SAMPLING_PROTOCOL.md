# Sampling Protocol: 575 → ~300 → 100

## 개요

Paper B의 gold standard sample을 확보하기 위한 3단계 프로세스.
스크리닝(16,189 → 575)은 Paper A의 범위이며, Paper B에서는 추적하지 않음.

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
   100 Studies → Paper B Gold Standard
```

---

## Stage 1: Full-Text Eligibility (575 → ~300)

### 목적
AI 스크리닝에서 "Include"로 판정된 575개 논문의 full-text를 검토하여
MASEM에 실제로 사용 가능한 연구만 선별

### 담당
- **PI (H1)**: 전체 575개 full-text review
- **PhD 1 (H2)**: 30% random sample (173개) 독립 review → IRR 확인

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
  ├── PhD 1이 30% random sample 독립 review
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

## Stage 2: Stratified Random Sampling (~300 → 100)

### 목적
Paper B의 gold standard를 위한 100개 연구를 ~300개에서 층화무작위추출

### 층화 변수 (Stratification Variables)

| 변수 | 층 (Strata) | 근거 |
|------|------------|------|
| **Publication year** | 2015-2019 / 2020-2022 / 2023-2025 | AI 연구의 시간적 변화 반영 |
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
    bins=[2014, 2019, 2022, 2026],
    labels=['2015-2019', '2020-2022', '2023-2025']
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

## 스크리닝은 Paper B 범위 밖

| 단계 | Paper A 범위 | Paper B 범위 |
|------|-------------|-------------|
| Database search (22,166 → 16,189) | ✅ | ❌ |
| AI screening (16,189 → 575) | ✅ | ❌ |
| Human screening review | ✅ | ❌ |
| **Full-text eligibility (575 → ~300)** | ✅ | ✅ (Stage 1) |
| **Stratified sampling (~300 → 100)** | — | ✅ (Stage 2) |
| **Gold standard coding (100)** | ✅ (일부) | ✅ (핵심) |
| **AI extraction evaluation** | — | ✅ (핵심) |
| **Full dataset coding (~300)** | ✅ (핵심) | — |

Paper B의 Methods에서는 Stage 1 (full-text eligibility)부터 기술하되,
screening 과정은 "described in detail in the parent meta-analysis (You, 2026)"로 간략히 언급.
