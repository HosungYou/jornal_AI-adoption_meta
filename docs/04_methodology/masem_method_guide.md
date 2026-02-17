# MASEM Methodology Guide

## Overview

This guide explains Meta-Analytic Structural Equation Modeling (MASEM) and its application to educational AI adoption research. MASEM synthesizes correlation matrices across studies to test structural models, combining the strengths of meta-analysis and SEM.

---

## 1. What is MASEM?

### 1.1 Definition

**Meta-Analytic Structural Equation Modeling (MASEM):** A method that combines meta-analysis and structural equation modeling to:
1. Pool correlation matrices across studies
2. Fit structural models on the pooled correlation matrix
3. Test theoretical relationships at the meta-analytic level

### 1.2 Why Use MASEM?

**Advantages over Traditional Meta-Analysis:**
- Tests full theoretical models (not just bivariate relationships)
- Examines mediation, indirect effects, model fit
- Controls for common method bias through measurement models
- Provides standardized path coefficients across studies

**Advantages over Single-Study SEM:**
- Larger effective sample size (cumulative N across studies)
- More generalizable findings
- Tests whether theoretical models hold across contexts
- Reduces sampling error and publication bias

**Advantages over Univariate Meta-Analysis:**
- Preserves correlation structure among variables
- Tests competing structural models
- Examines indirect effects and mediation
- Evaluates overall model fit (CFI, RMSEA, SRMR)

---

## 2. MASEM vs. Traditional SEM

### 2.1 Comparison

| Aspect | Traditional SEM | MASEM |
|--------|----------------|-------|
| **Data Source** | Single study | Multiple studies (meta-analysis) |
| **Sample Size** | One study's n | Cumulative N across studies |
| **Input** | Raw data or covariance matrix | Pooled correlation matrix |
| **Generalizability** | Limited to study sample | Generalizes across contexts |
| **Statistical Power** | Depends on single study n | High (cumulative n often >10,000) |
| **Model Fit** | Study-specific | Meta-analytic fit |
| **Moderators** | Within-study subgroups | Across-study moderators |

---

## 3. MASEM Approaches

### 3.1 Two-Stage SEM (TSSEM)

**Developer:** Cheung (2015), Cheung & Chan (2005)

**Philosophy:** Separate meta-analysis (Stage 1) from structural modeling (Stage 2)

#### Stage 1: Pool Correlation Matrices

**Objective:** Combine correlation matrices across studies to create a pooled matrix

**Methods:**
- **Fixed-Effects Model:** Assumes homogeneous correlations across studies
- **Random-Effects Model:** Allows correlations to vary across studies (recommended)

**Output:**
- Pooled correlation matrix (12×12 for our 12 constructs)
- Heterogeneity statistics (I², Q-test)
- Sampling variance-covariance matrix

**Software:** `metaSEM` package in R (Cheung, 2015)

---

#### Stage 2: Fit Structural Model

**Objective:** Fit SEM on pooled correlation matrix from Stage 1

**Input:**
- Pooled correlation matrix
- Harmonic mean sample size (or weighted average)
- Structural model specification

**Output:**
- Path coefficients (β)
- Model fit indices (CFI, RMSEA, SRMR, χ²)
- R² for endogenous variables
- Indirect effects (if mediation paths)

**Estimation:** Weighted Least Squares (WLS) or Maximum Likelihood (ML)

---

### 3.2 One-Stage MASEM (OSMASEM)

**Developer:** Jak & Cheung (2020)

**Philosophy:** Simultaneous estimation of pooled correlations and structural model

**Advantages:**
- Can include continuous moderators directly
- Single-step inference (no two-stage uncertainty)
- More efficient for moderator testing

**Disadvantages:**
- Computationally intensive
- More complex to implement
- Longer run time for complex models

**When to Use:**
- Testing continuous moderators (e.g., Hofstede individualism score)
- Complex moderator interactions
- When Stage 1 heterogeneity is very high

---

### 3.3 Our Approach: Hybrid

**Primary Analysis:** TSSEM (simpler, more transparent)
- Stage 1: Pool correlations with random-effects model
- Stage 2: Fit three competing models
- Compare models using fit indices

**Moderator Analysis:** OSMASEM
- Test continuous moderators (year, education level as ordinal)
- Subgroup TSSEM for categorical moderators (AI tool type, user role: student vs instructor, education level: K-12 vs HE)

---

## 4. TSSEM Stage 1: Pooling Correlation Matrices

### 4.1 Fixed-Effects vs. Random-Effects

**Fixed-Effects Model:**

**Assumption:** True correlation is identical across all studies

**Formula:**
```
r_pooled = Σ(w_i × r_i) / Σ(w_i)

where w_i = n_i - 3  (inverse variance weight)
```

**Use when:** Homogeneity test non-significant (Q-test p > .05)

**Interpretation:** Pooled correlation is the single true correlation

---

**Random-Effects Model (Recommended):**

**Assumption:** True correlations vary across studies (heterogeneity)

**Formula:**
```
r_pooled = Σ(w_i* × r_i) / Σ(w_i*)

where w_i* = 1 / (v_i + τ²)
  v_i = sampling variance of r_i
  τ² = between-study variance (estimated)
```

**Use when:** Heterogeneity present (Q-test p < .05) OR default choice

**Interpretation:** Pooled correlation is the mean of a distribution of true correlations

---

### 4.2 Heterogeneity Assessment

**Q-Statistic:**

**Formula:**
```
Q = Σ[w_i × (r_i - r_pooled)²]

df = k - 1
```

**Interpretation:**
- Q-test p < .05 → Significant heterogeneity (use random effects)
- Q-test p > .05 → Homogeneity (can use fixed effects, but random effects still safer)

---

**I² Statistic:**

**Formula:**
```
I² = [(Q - df) / Q] × 100%
```

**Interpretation:**
- I² = 0-25%: Low heterogeneity
- I² = 25-50%: Moderate heterogeneity
- I² = 50-75%: Substantial heterogeneity
- I² = 75-100%: High heterogeneity

**Action:** If I² > 50%, explore moderators to explain heterogeneity

---

### 4.3 Handling Missing Correlations

**Problem:** Not all studies report all 66 pairwise correlations

**Solutions:**

**1. Full Information Maximum Likelihood (FIML):**
- Use all available data
- Estimate missing correlations based on pattern of available correlations
- Default in `tssem1()` function

**2. Multiple Imputation:**
- Impute missing correlations multiple times
- Pool results across imputations
- More conservative than FIML

**3. Pairwise Deletion:**
- Each correlation pooled based on studies reporting that pair
- k varies per correlation cell
- Can lead to non-positive definite matrix

**Our Approach:** FIML (metaSEM default)

---

### 4.4 Stage 1 Implementation (R Code)

```r
library(metaSEM)

# Prepare data: List of correlation matrices
cor_matrices <- list(
  Smith2023 = matrix(c(1.00, .45, .52,
                       .45, 1.00, .48,
                       .52, .48, 1.00), nrow=3, byrow=TRUE,
                    dimnames=list(c("PE","EE","BI"), c("PE","EE","BI"))),
  Jones2024 = matrix(c(1.00, .50, .55,
                       .50, 1.00, .46,
                       .55, .46, 1.00), nrow=3, byrow=TRUE,
                    dimnames=list(c("PE","EE","BI"), c("PE","EE","BI")))
)

# Sample sizes
sample_sizes <- c(285, 400)

# Run TSSEM Stage 1 (random-effects)
stage1 <- tssem1(Cov = cor_matrices,
                 n = sample_sizes,
                 method = "REM",  # Random-effects model
                 RE.type = "Diag")  # Diagonal τ² matrix

# View results
summary(stage1)
```

**Output Interpretation:**
- Pooled correlations for each pair
- Heterogeneity statistics (Q, I²)
- τ² estimates (between-study variance)

---

## 5. TSSEM Stage 2: Structural Modeling

### 5.1 Model Specification

**RAM Notation (Reticular Action Model):**

Three matrices define the model:
- **A matrix:** Asymmetric paths (regressions)
- **S matrix:** Symmetric paths (variances, covariances)
- **F matrix:** Filter (observed vs. latent variables)

**Example: Simple TAM Model**

```
Model: PE→BI, EE→BI, PE↔EE

PE and EE are exogenous (correlated)
BI is endogenous
```

**RAM Specification:**

```r
# A matrix: Regression paths
A <- matrix(c(0, 0, 0,   # PE row (no paths TO PE)
              0, 0, 0,   # EE row (no paths TO EE)
              "0.3*beta_PE", "0.3*beta_EE", 0),  # BI row (PE→BI, EE→BI)
            nrow=3, byrow=TRUE,
            dimnames=list(c("PE","EE","BI"), c("PE","EE","BI")))

# S matrix: Variances and covariances
S <- matrix(c("0.5*var_PE", NA, NA,
              "0.3*cov_PE_EE", "0.5*var_EE", NA,
              0, 0, "0.5*resid_BI"),
            nrow=3, byrow=TRUE,
            dimnames=list(c("PE","EE","BI"), c("PE","EE","BI")))

# F matrix: All observed (identity matrix)
F <- diag(3)
dimnames(F) <- list(c("PE","EE","BI"), c("PE","EE","BI"))
```

---

### 5.2 Stage 2 Implementation (R Code)

```r
# Extract pooled correlation matrix from Stage 1
pooled_cor <- vec2symMat(coef(stage1), diag = FALSE)

# Harmonic mean sample size
n_harmonic <- 1 / mean(1 / sample_sizes)

# Fit Model 1 (TAM core)
model1 <- tssem2(stage1,
                 Amatrix = A,
                 Smatrix = S,
                 Fmatrix = F,
                 intervals.type = "LB",  # Likelihood-based CI
                 mx.algebras = list(
                   indirect_PE = mxAlgebra(beta_PE * beta_BI_UB, name="ind_PE")
                 ))

# View results
summary(model1)
```

**Output:**
- Path coefficients with 95% CI
- Model fit: χ², df, p, CFI, RMSEA, SRMR
- R² for endogenous variables
- Indirect effects (if specified)

---

### 5.3 Model Fit Indices

**Absolute Fit:**

**Chi-Square (χ²):**
- Tests exact fit: H₀: model fits perfectly
- Non-significant p (p > .05) → good fit
- **Limitation:** Sensitive to sample size (almost always significant with large N)

**SRMR (Standardized Root Mean Square Residual):**
- Average absolute difference between observed and predicted correlations
- **Cutoff:** SRMR < .08 (good fit), < .05 (excellent fit)

---

**Incremental Fit:**

**CFI (Comparative Fit Index):**
- Compares model fit to null model (no relationships)
- **Cutoff:** CFI > .95 (good fit), > .97 (excellent fit)

**TLI (Tucker-Lewis Index):**
- Similar to CFI, penalizes complexity
- **Cutoff:** TLI > .95 (good fit)

---

**Parsimony-Adjusted Fit:**

**RMSEA (Root Mean Square Error of Approximation):**
- Badness-of-fit per degree of freedom
- **Cutoff:** RMSEA < .08 (acceptable), < .06 (good), < .05 (excellent)
- **90% CI:** Narrow CI indicates precision

---

**Information Criteria:**

**AIC (Akaike Information Criterion):**
```
AIC = -2LL + 2k
```
- Lower AIC = better fit
- Compare models: ΔAIC > 10 → substantial difference

**BIC (Bayesian Information Criterion):**
```
BIC = -2LL + k×ln(n)
```
- Penalizes complexity more than AIC
- Lower BIC = better model

---

### 5.4 Interpreting Fit Indices

**Good Model Fit (all criteria met):**
- χ² p > .05 (if n < 500) OR non-significant
- CFI > .95
- TLI > .95
- RMSEA < .06 with 90% CI upper bound < .08
- SRMR < .08

**Acceptable Fit (most criteria met):**
- CFI > .90
- RMSEA < .08
- SRMR < .10

**Poor Fit:**
- CFI < .90
- RMSEA > .10
- SRMR > .10

---

## 6. Model Comparison

### 6.1 Nested Models

**Definition:** Model A is nested in Model B if Model A is a constrained version of Model B

**Example:**
- Model 1 (TAM core): PE→BI, EE→BI
- Model 2 (TAM + AI constructs): PE→BI, EE→BI, TRU→BI, ANX→BI
- Model 2 nests Model 1 (adds paths)

---

### 6.2 Chi-Square Difference Test

**Formula:**
```
Δχ² = χ²_Model1 - χ²_Model2
Δdf = df_Model1 - df_Model2

p-value from χ² distribution with Δdf
```

**Interpretation:**
- p < .05 → Model 2 fits significantly better
- p > .05 → Model 1 is preferred (more parsimonious)

**Example:**

| Model | χ² | df | CFI | RMSEA |
|-------|----|----|-----|-------|
| Model 1 | 85.3 | 42 | .93 | .065 |
| Model 2 | 52.1 | 38 | .97 | .042 |

```
Δχ² = 85.3 - 52.1 = 33.2
Δdf = 42 - 38 = 4
p < .001 → Model 2 significantly better
```

---

### 6.3 Fit Index Differences

**For non-nested models, use:**

**ΔCFI:**
- ΔCFI > .01 → Meaningful difference
- Prefer model with higher CFI

**ΔRMSEA:**
- ΔRMSEA > .015 → Meaningful difference
- Prefer model with lower RMSEA

**ΔSRMR:**
- ΔSRMR > .01 → Meaningful difference
- Prefer model with lower SRMR

**AIC/BIC:**
- ΔAIC > 10 or ΔBIC > 10 → Strong preference for lower value
- ΔAIC 4-10 or ΔBIC 4-10 → Moderate preference

---

## 7. Moderator Analysis

### 7.1 Categorical Moderators (Subgroup TSSEM)

**Approach:** Run separate TSSEM for each subgroup, compare pooled correlations and path coefficients

**Example: Student vs. Instructor Subgroups**

```r
# Split data by user role
student_studies <- studies[studies$user_role == "Student", ]
instructor_studies <- studies[studies$user_role == "Instructor", ]

# Run Stage 1 separately
stage1_student <- tssem1(Cov = cor_matrices_student, n = n_student, method = "REM")
stage1_instructor <- tssem1(Cov = cor_matrices_instructor, n = n_instructor, method = "REM")

# Fit same model on both
model_student <- tssem2(stage1_student, Amatrix=A, Smatrix=S, Fmatrix=F)
model_instructor <- tssem2(stage1_instructor, Amatrix=A, Smatrix=S, Fmatrix=F)

# Compare path coefficients
coef_student <- coef(model_student)
coef_instructor <- coef(model_instructor)

# Test difference (Wald test or permutation test)
```

---

### 7.2 Continuous Moderators (OSMASEM)

**Approach:** Include moderator as predictor of correlation heterogeneity

**Example: Publication Year (Education Context)**

```r
library(metaSEM)

# Prepare moderator data
moderator_data <- data.frame(
  study_id = names(cor_matrices),
  year = c(2020, 2021, 2023, ...)  # Publication years
)

# Run OSMASEM with year as moderator
osmasem_model <- osmasem(
  model.name = "Year Moderator Model",
  Mmatrix = M,  # Model matrix (like TSSEM A and S)
  data = cor_matrices,
  n = sample_sizes,
  moderators = moderator_data$year,
  intervals.type = "LB"
)

summary(osmasem_model)
```

**Output:**
- Main effects: Average path coefficients
- Moderator effects: How year changes path coefficients
- Example: β(PE→BI) = .35 + .02×(year-2020)
  - Interpretation: PE→BI path in educational AI adoption increases by .02 per year

---

## 8. Assumptions and Diagnostics

### 8.1 MASEM Assumptions

**1. Independence:**
- Studies must be independent (no duplicate samples)
- Check: Review for same author, overlapping data collection

**2. Homogeneity of Constructs:**
- Constructs must be comparable across studies
- Check: Construct harmonization protocol (see construct_harmonization.md)

**3. Adequate Sample Size per Cell:**
- Each correlation should be reported in ≥10 studies
- Check: k per correlation pair

**4. Positive Definiteness:**
- Correlation matrices must be positive definite
- Check: Eigenvalues > 0, metaSEM will flag violations

**5. No Publication Bias (or accounted for):**
- Missing studies may bias results
- Check: Funnel plots, Egger's test, trim-and-fill

---

### 8.2 Diagnostic Checks

**Outlier Detection:**

```r
# Identify outlier correlations (z > 3.29, p < .001)
outliers <- studies %>%
  mutate(z = (r - r_pooled) / se) %>%
  filter(abs(z) > 3.29)
```

**Influence Analysis:**

```r
# Leave-one-out analysis
influence_results <- lapply(1:k, function(i) {
  stage1_loo <- tssem1(Cov = cor_matrices[-i], n = sample_sizes[-i])
  coef(stage1_loo)
})

# Compare to full model: if one study changes results substantially, it's influential
```

**Publication Bias:**

```r
# Funnel plot for PE→BI correlation
library(meta)
meta_pe_bi <- metacor(cor = r_PE_BI, n = n, studlab = study_id)
funnel(meta_pe_bi)
egger.test(meta_pe_bi)  # Asymmetry test
```

---

## 9. Reporting MASEM Results

### 9.1 Stage 1 Results

**Report:**
- Number of studies (k) and total N
- Pooled correlations for all construct pairs (table)
- Heterogeneity statistics (I², Q) for each correlation
- Between-study variance (τ²)

**Example Table (Educational AI Context):**

| Correlation | k | N | r | 95% CI | Q | I² | τ² |
|-------------|---|---|---|--------|---|----|----|
| PE-BI | 45 | 12,840 | .48 | [.44, .52] | 165.3*** | 72% | .015 |
| EE-BI | 42 | 11,950 | .42 | [.38, .46] | 148.2*** | 68% | .012 |
| TRU-BI | 28 | 7,650 | .55 | [.50, .60] | 98.5*** | 75% | .020 |

---

### 9.2 Stage 2 Results

**Report:**
- Path coefficients with 95% CI (table)
- Model fit indices (CFI, RMSEA, SRMR, χ²)
- R² for endogenous variables
- Indirect effects (if applicable)

**Example Table:**

| Path | β | SE | 95% CI | p |
|------|---|----|----|---|
| PE → BI | .35 | .03 | [.29, .41] | <.001 |
| EE → BI | .28 | .03 | [.22, .34] | <.001 |
| TRU → BI | .32 | .04 | [.24, .40] | <.001 |
| ANX → BI | -.18 | .03 | [-.24, -.12] | <.001 |

**Model Fit:** χ²(38) = 52.1, p = .065, CFI = .97, RMSEA = .042 [.028, .056], SRMR = .045

---

### 9.3 Model Comparison Results

| Model | χ² | df | CFI | RMSEA | SRMR | AIC | BIC |
|-------|----|----|-----|-------|------|-----|-----|
| Model 1 (TAM/UTAUT) | 85.3 | 42 | .93 | .065 | .068 | 12843 | 12968 |
| Model 2 (Integrated) | 52.1 | 38 | .97 | .042 | .045 | 12758 | 12905 |
| Model 3 (AI-Only) | 78.2 | 40 | .94 | .058 | .062 | 12822 | 12955 |

**Best Fitting Model:** Model 2 (lowest AIC/BIC, highest CFI, lowest RMSEA/SRMR)

---

## 10. Software and Resources

### 10.1 R Packages

**metaSEM (Cheung, 2015):**
- Primary package for TSSEM and OSMASEM
- Install: `install.packages("metaSEM")`
- Documentation: https://cran.r-project.org/package=metaSEM

**OpenMx:**
- Backend for SEM estimation (required by metaSEM)
- Install: `install.packages("OpenMx")`

**lavaan:**
- Alternative SEM package (can convert models)
- Install: `install.packages("lavaan")`

---

### 10.2 Learning Resources

**Books:**
- Cheung (2015). *Meta-Analysis: A Structural Equation Modeling Approach*. Wiley.
- Jak (2015). *Meta-Analytic Structural Equation Modelling*. Springer.

**Tutorials:**
- metaSEM vignettes: `vignette("metaSEM")`
- Cheung's website: http://mikewlcheung.github.io/metasem/

**Online Courses:**
- MASEM Workshop materials (Cheung)

---

## References

Cheung, M. W. L. (2015). *Meta-analysis: A structural equation modeling approach*. Wiley.

Cheung, M. W. L., & Chan, W. (2005). Meta-analytic structural equation modeling: A two-stage approach. *Psychological Methods*, 10(1), 40-64.

Jak, S., & Cheung, M. W. L. (2020). Meta-analytic structural equation modeling with moderating effects on SEM parameters. *Psychological Methods*, 25(4), 430-455.

Viswesvaran, C., & Ones, D. S. (1995). Theory testing: Combining psychometric meta-analysis and structural equations modeling. *Personnel Psychology*, 48(4), 865-885.
