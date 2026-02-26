# Analysis Plan: Paper B

## 개요

Paper B의 4개 RQ에 대한 통계 분석 계획.
모든 분석은 R로 수행 (scripts/analysis.R).

---

## RQ1: AI 모델별 MASEM 코딩 정확도

**질문**: Claude Sonnet 4.6, GPT Codex 5.3, Gemini CLI 각각의 MASEM 코딩 정확도는 gold standard 대비 어떠한가?

### 1.1 Primary Metrics

| 변수 유형 | Metric | 기준값 | R Package |
|----------|--------|--------|-----------|
| Categorical (7개) | Cohen's κ (AI vs. Gold) | κ ≥ 0.80 excellent | `irr::kappa2()` |
| Categorical | Gwet's AC2 | AC2 ≥ 0.80 | `irrCAC::gwet.ac1.raw()` |
| Continuous (12개) | ICC(2,1) single measures | ICC ≥ 0.90 excellent | `irr::icc()` |
| Continuous | MAE (Mean Absolute Error) | < 0.05 for r values | Base R |
| Continuous | RMSE | < 0.10 for r values | Base R |
| Binary (match/no match) | Accuracy (%) | ≥ 95% | Base R |
| Binary | F1 score | ≥ 0.90 | `caret::confusionMatrix()` |

### 1.2 Analysis Steps

```r
# Step 1: Per-model accuracy
for each AI model (Claude, Codex, Gemini):
  for each variable (30개):
    calculate: κ or ICC (depending on variable type)
    calculate: accuracy, precision, recall, F1
    store: results_per_variable.csv

# Step 2: Overall accuracy per model
aggregate across variables:
  mean κ (categorical), mean ICC (continuous)
  overall accuracy (%)
  95% CI (bootstrap, B=1000)

# Step 3: Statistical comparison between models
  Cochran's Q test (categorical) → if significant → McNemar pairwise
  Repeated-measures ANOVA (continuous) → if significant → paired t-tests with Bonferroni
```

### 1.3 Output Tables

**Table 5**: Per-Model Accuracy Summary (3 models × overall metrics)
**Table 6**: Per-Variable Accuracy Breakdown (30 variables × 3 models × κ/ICC/accuracy)

---

## RQ2: Variable Type별 AI 정확도 차이

**질문**: Bibliographic, Statistical, Classificatory 변수 유형에 따라 AI 정확도가 다른가?

### 2.1 Variable Type Classification

| Type | Variables | N | 예상 난이도 |
|------|-----------|---|-----------|
| **Bibliographic** | A1-A8 | 8 | Low (정형 정보) |
| **Statistical** | B1-B12 | 12 | High (수치 추출) |
| **Classificatory** | C1-C6, D1-D4 | 10 | Medium (판단 필요) |

### 2.2 Analysis Steps

```r
# Step 1: Group-level accuracy
for each variable_type:
  pool accuracy metrics across variables within type
  calculate: mean accuracy, SD, 95% CI

# Step 2: Between-type comparison
  Kruskal-Wallis test (non-parametric, 3 groups)
  if significant → Dunn's post-hoc test with Bonferroni

# Step 3: Interaction (Model × Variable Type)
  Two-way repeated-measures ANOVA
  Model (3) × Variable_Type (3)
  Check interaction effect
```

### 2.3 Hypotheses

- H2a: Bibliographic > Classificatory > Statistical (accuracy order)
- H2b: Model × Variable_Type interaction이 유의 (특정 모델이 특정 유형에 강할 수 있음)

### 2.4 Output Tables & Figures

**Table 7**: Accuracy by Variable Type (3 types × 3 models)
**Figure 1**: Heatmap — Variable × Model accuracy matrix (30 × 3)

---

## RQ3: Multi-Model Consensus의 효과

**질문**: 3개 모델의 합의(consensus)가 개별 모델보다 정확한가?

### 3.1 Consensus Strategies

| Strategy | Rule | 적용 대상 |
|----------|------|----------|
| **Majority vote** | 2/3 이상 일치 | Categorical variables |
| **Unanimous** | 3/3 일치 | All variables (subset) |
| **Median** | 중앙값 | Continuous variables |
| **Best-of-three** | Oracle (upper bound) | Theoretical comparison |

### 3.2 Analysis Steps

```r
# Step 1: Calculate consensus values
for each study, each variable:
  majority_vote = mode of 3 AI values (if ≥ 2 agree)
  unanimous = value if all 3 agree, else NA
  median_value = median of 3 AI values

# Step 2: Consensus accuracy vs. Gold Standard
for each consensus strategy:
  calculate: κ, ICC, accuracy, F1
  compare with individual model accuracy

# Step 3: Statistical comparison
  McNemar test: consensus accuracy vs. best single model
  Paired comparison: consensus ICC vs. best single model ICC

# Step 4: Agreement analysis
  Calculate: % unanimous, % majority, % split (no consensus)
  Variable-type breakdown of agreement patterns
```

### 3.3 Output Tables

**Table 8**: Consensus vs. Individual Model Accuracy
- Rows: Claude, Codex, Gemini, Majority, Unanimous, Median
- Columns: κ (cat), ICC (cont), Accuracy (%), F1

**Table 9**: Agreement Pattern Distribution
- % Unanimous / Majority / Split by variable type

---

## RQ4: 최적 Human-AI Hybrid Workflow

**질문**: 어떤 human-AI collaboration 방식이 가장 효율적이면서 정확한가?

### 4.1 Workflow Scenarios (Simulated)

| Scenario | Human Effort | Description |
|----------|-------------|-------------|
| **W1** | 100% | All human coding (baseline) |
| **W2** | 0% verification | AI only (no human) |
| **W3** | 100% verification | AI extract → Human verify all |
| **W4** | Flag-only | AI extract → Human verify flagged items only |
| **W5** | Confidence-based | AI extract → Human verify low-confidence only |
| **W6** | Phase 1+2 hybrid | 100 gold + 200 AI-verified (actual design) |

### 4.2 Analysis Steps

```r
# Step 1: Simulate each workflow
for each scenario:
  estimate: accuracy (using Phase 1 data as benchmark)
  estimate: time cost (hours)
  estimate: error rate (%)

# Step 2: Efficiency metrics
for each scenario:
  accuracy_per_hour = accuracy / human_hours
  error_reduction = (baseline_error - scenario_error) / baseline_error

# Step 3: Cost-effectiveness frontier
  Plot: accuracy vs. human effort
  Identify: optimal efficiency point (knee of curve)

# Step 4: Decision framework
  Recommend: optimal workflow based on accuracy threshold
```

### 4.3 Bland-Altman Analysis

AI-Human 차이의 시각적 분석 (continuous variables):

```r
# Bland-Altman plot for each model
for each AI model:
  diff = AI_value - Gold_standard_value
  mean_val = (AI_value + Gold_standard_value) / 2
  mean_diff = mean(diff)
  sd_diff = sd(diff)
  LoA = c(mean_diff - 1.96 * sd_diff, mean_diff + 1.96 * sd_diff)

  plot(mean_val, diff)
  abline(h = c(mean_diff, LoA))
```

### 4.4 Output

**Table 10**: Workflow Comparison Summary
**Figure 2**: Bland-Altman plots (3 models)
**Figure 3**: Cost-effectiveness frontier

---

## Additional Analyses

### Error Analysis

```r
# Systematic error patterns
for each AI model:
  # Direction of errors
  overestimate_rate = mean(AI > Gold)  # for continuous
  underestimate_rate = mean(AI < Gold)

  # Study-level predictors of error
  glm(error ~ sample_size + journal_quality + matrix_type + year,
      family = binomial)
```

### Sensitivity Analyses

| 분석 | 목적 |
|------|------|
| Exclude β→r converted studies | 변환 오류 영향 확인 |
| Restrict to correlation-only studies | Pure r 데이터에서의 정확도 |
| By publication year | 최근 논문 vs. 과거 논문 차이 |
| By sample size (N) | 소규모 vs. 대규모 연구 차이 |
| By number of constructs | 복잡한 연구에서의 정확도 |

### Power Analysis (Post-hoc)

```r
# For McNemar test (consensus vs. best model)
# N = 100 studies, expected improvement = 5%
# 2-sided, alpha = .05
power.mcnemar.test(n = 100, paid = 0.05, psi = 2, sig.level = 0.05)

# For ICC comparison
# Using Zou (2007) confidence interval approach
# Report if 100 studies provide sufficient precision
```

---

## R Packages Required

```r
# IRR
library(irr)        # Cohen's kappa, ICC
library(irrCAC)     # Gwet's AC2, Krippendorff's alpha

# Classification
library(caret)      # Confusion matrix, F1, precision, recall

# Visualization
library(ggplot2)    # All figures
library(pheatmap)   # Heatmap (Figure 1)
library(blandr)     # Bland-Altman plots

# Statistical tests
library(coin)       # Exact McNemar
library(dunn.test)  # Dunn's post-hoc
library(lme4)       # Mixed-effects models (if needed)

# Utility
library(tidyverse)  # Data manipulation
library(readr)      # CSV reading
library(jsonlite)   # JSON parsing (AI outputs)
```

---

## 분석 산출물 요약

| 산출물 | 파일 | 위치 |
|--------|------|------|
| IRR results (R2 vs R3) | irr_results.csv | data/06_analysis/ |
| Per-model accuracy | model_accuracy.csv | data/06_analysis/ |
| Per-variable accuracy | variable_accuracy.csv | data/06_analysis/ |
| Consensus results | consensus_accuracy.csv | data/06_analysis/ |
| Error analysis | error_patterns.csv | data/06_analysis/ |
| Workflow comparison | workflow_simulation.csv | data/06_analysis/ |
| Heatmap (Fig 1) | fig1_heatmap.pdf | data/06_analysis/figures/ |
| Bland-Altman (Fig 2) | fig2_bland_altman.pdf | data/06_analysis/figures/ |
| Cost-effectiveness (Fig 3) | fig3_cost_effectiveness.pdf | data/06_analysis/figures/ |
| Full analysis script | analysis.R | scripts/ |
