# GRADE Evidence Assessment Framework for MASEM

**Grading of Recommendations, Assessment, Development, and Evaluations (GRADE)**

**Adapted for Meta-Analytic Structural Equation Modeling of Observational/Correlational Studies**

---

## Overview

The GRADE framework assesses the **certainty (quality) of evidence** for each key finding in the meta-analysis. GRADE moves beyond statistical significance to evaluate confidence in effect estimates.

**Key Principle:** Start at a baseline certainty level, then systematically consider factors that increase or decrease certainty.

**GRADE Certainty Levels:**
- **High (⊕⊕⊕⊕):** Very confident the true effect is close to the estimate
- **Moderate (⊕⊕⊕◯):** Moderately confident; true effect likely close but possibly substantially different
- **Low (⊕⊕◯◯):** Limited confidence; true effect may be substantially different
- **Very Low (⊕◯◯◯):** Very little confidence; true effect likely substantially different

---

## GRADE for MASEM: Starting Point

**Standard GRADE:**
- Randomized Controlled Trials (RCTs) start at **High**
- Observational studies start at **Low**

**Modified for MASEM:**
- Well-designed **correlational studies** can provide **High certainty** for associations (not causal effects)
- Starting point for MASEM: **High ⊕⊕⊕⊕**
- Rationale: Large sample sizes, multiple independent studies, quantitative synthesis increases precision and reduces bias compared to single observational studies

**Critical Distinction:**
- GRADE assesses certainty of **association** (correlation, path coefficient), NOT causality
- Even High certainty evidence only supports "X and Y are associated," not "X causes Y"

---

## Five GRADE Domains

### 1. Risk of Bias

**Question:** Do study limitations (selection bias, measurement bias, reporting bias, CMB) reduce confidence in the estimate?

**Assessment:**

| Consideration | Downgrade? | Magnitude |
|---------------|------------|-----------|
| <25% of weight from high risk-of-bias studies | No | — |
| 25-50% of weight from high risk-of-bias studies | Yes | −1 level (serious RoB) |
| >50% of weight from high risk-of-bias studies | Yes | −2 levels (very serious RoB) |
| Sensitivity analysis changes conclusion (sign flip, significance change) | Yes | −1 level (impact of RoB) |

**Weight Calculation:**
```
Weight_HighRisk = Σ(n_HighRisk_studies) / Σ(n_all_studies)
```

**Example:**
- Total N = 10,000
- High-risk studies: N = 3,000 (30% weight)
- **Downgrade:** Yes, −1 level (serious risk of bias)

**Documentation (Summary of Findings Table):**
- "30% of weight from high risk-of-bias studies; sensitivity analysis excluding these studies showed similar effect size (β changed from 0.45 to 0.42)" → Downgrade −1

---

### 2. Inconsistency (Heterogeneity)

**Question:** Is there unexplained variability in effect sizes across studies?

**Assessment:**

| Consideration | Downgrade? | Magnitude |
|---------------|------------|-----------|
| I² < 40% (low heterogeneity) | No | — |
| I² 40-75% AND heterogeneity explained by moderators | No | — |
| I² 40-75% AND heterogeneity NOT explained | Yes | −1 level (serious inconsistency) |
| I² > 75% (considerable) AND heterogeneity NOT explained | Yes | −1 or −2 levels (serious/very serious) |
| 95% prediction interval crosses null (includes zero) for non-null pooled estimate | Yes | −1 level (conflicting evidence) |
| Point estimates vary widely AND confidence intervals show minimal overlap | Yes | −1 level (inconsistent results) |

**Mitigation:**
- **If meta-regression identifies significant moderators** (e.g., AI type, culture) that explain heterogeneity (R² ≥ 50%), do NOT downgrade for inconsistency
- **Subgroup analysis:** Report separate estimates per subgroup with lower heterogeneity

**Example 1 (Education Context):**
- PE→BI: I² = 65%, 95% PI [0.25, 0.60], pooled r = 0.42
- Meta-regression: User role explains R² = 55% (students: r=0.50, instructors: r=0.35)
- **Decision:** No downgrade (heterogeneity explained)

**Example 2 (Education Context):**
- ANX→BI: I² = 80%, 95% PI [-0.40, 0.10], pooled r = -0.15
- Meta-regression: Education level, discipline, AI tool type did not explain variance
- **Decision:** Downgrade −2 (very serious inconsistency; PI crosses zero)

**Documentation:**
- "I² = 65% (moderate heterogeneity); meta-regression showed user role (student vs. instructor) explained 55% of variance" → No downgrade
- "I² = 80% (considerable heterogeneity); 95% prediction interval crosses zero; education-specific moderators (level, discipline, AI tool type) did not explain variance" → Downgrade −2

---

### 3. Indirectness

**Question:** Do the studies directly address the research question, or are there important differences in population, constructs, or outcomes?

**Assessment:**

| Consideration | Downgrade? | Magnitude |
|---------------|------------|-----------|
| Constructs measured directly with exact labels (e.g., "Performance Expectancy") | No | — |
| Constructs harmonized with **high confidence** (exact/synonymous definitions) | No | — |
| >25% of constructs mapped with **moderate confidence** (adapted scales, partial match) | Yes | −1 level (serious indirectness) |
| >50% of constructs mapped with **low confidence** (ambiguous, ad-hoc scales) | Yes | −2 levels (very serious indirectness) |
| Outcome is **proxy** (e.g., Behavioral Intention as proxy for Actual Use Behavior) | Yes | −1 level (indirect outcome) |
| Population differs from research question (e.g., students when generalizing to workforce) | Yes | −1 level (indirect population) |

**MASEM-Specific Considerations:**

**Construct Harmonization:**
- If construct crosswalk shows "exact" or "high" confidence for >75% of studies → No downgrade
- If "moderate" confidence for 25-50% → Downgrade −1
- If "low" confidence for >25% → Downgrade −2

**Outcome Indirectness:**
- **BI→UB path:** If most studies measure BI only (no actual UB), and we're interested in behavior → Downgrade −1 for UB predictions
- **TRU→BI path:** Direct measurement of both → No downgrade

**Example:**
- TRU→BI path: 15/20 studies used "Trust in AI" (exact), 5/20 used "Algorithm Trust" (high confidence synonym)
- **Decision:** No downgrade (construct harmonization high quality)

**Documentation:**
- "85% of studies used exact or high-confidence synonyms for Trust construct; 15% moderate confidence" → No downgrade
- "Behavioral Intention measured in all studies; only 40% measured Actual Use Behavior" → Downgrade −1 for predictions to behavior

---

### 4. Imprecision

**Question:** Is the confidence interval wide enough to include both meaningful and trivial effects, or conflicting interpretations?

**Assessment:**

| Consideration | Downgrade? | Magnitude |
|---------------|------------|-----------|
| 95% CI excludes trivial effects (e.g., for correlation, excludes │r│ < 0.10) | No | — |
| Total sample size ≥1,000 AND narrow CI | No | — |
| 95% CI includes both meaningful benefit and meaningful harm (crosses ±0.10) | Yes | −1 level (serious imprecision) |
| 95% CI very wide (crosses multiple interpretation thresholds: small/medium/large) | Yes | −2 levels (very serious imprecision) |
| Total sample size <500 | Yes | −1 level (small sample imprecision) |
| Number of studies k < 10 | Yes | −1 level (few studies) |

**Thresholds for "Meaningful" Effects (Correlations):**
- Trivial: │r│ < 0.10
- Small: │r│ = 0.10
- Medium: │r│ = 0.30
- Large: │r│ = 0.50

**For Path Coefficients (β):**
- Similar thresholds: │β│ < 0.10 trivial, 0.10 small, 0.30 medium, 0.50 large

**Example 1:**
- PE→BI: β = 0.45, 95% CI [0.40, 0.50], N = 8,500, k = 35
- **Decision:** No downgrade (CI narrow, excludes trivial, large sample)

**Example 2:**
- TRA→TRU: β = 0.18, 95% CI [0.05, 0.31], N = 1,200, k = 8
- **Decision:** Downgrade −1 (CI includes trivial effect r=0.05; k < 10)

**Example 3:**
- AUT→ANX: β = 0.22, 95% CI [-0.05, 0.49], N = 450, k = 5
- **Decision:** Downgrade −2 (CI crosses zero from negative to positive; very wide; N < 500, k < 10)

**Documentation:**
- "95% CI [0.40, 0.50] excludes trivial effects; N = 8,500" → No downgrade
- "95% CI [0.05, 0.31] includes trivial effects (r < 0.10); k = 8 studies" → Downgrade −1

---

### 5. Publication Bias

**Question:** Is there evidence that published studies systematically differ from unpublished studies (small-study effects, p-hacking)?

**Assessment:**

| Consideration | Downgrade? | Magnitude |
|---------------|------------|-----------|
| Funnel plot symmetric AND Egger's test p > 0.10 | No | — |
| Comprehensive search (grey literature, dissertations) AND k ≥ 30 | No | — |
| Funnel plot asymmetric BUT explained by moderators (not publication bias) | No | — |
| Egger's test p < 0.05 AND funnel plot asymmetric | Yes | −1 level (suspected publication bias) |
| PET-PEESE correction changes conclusion (effect becomes non-significant) | Yes | −2 levels (serious publication bias) |
| Small-study effects evident (smaller studies show larger effects) | Yes | −1 level (publication bias likely) |
| k < 10 (too few studies to assess publication bias) | Unclear | Note limitation, no downgrade |

**MASEM-Specific Considerations:**

**Multiple Correlations:**
- Assess publication bias separately for each key path (not just overall)
- PE→BI, EE→BI, TRU→BI, ANX→BI, BI→UB (5 focal paths minimum)

**Grey Literature:**
- If ≥20% of studies are dissertations/preprints → Less concern for publication bias
- If <5% grey literature → Greater concern

**Example 1:**
- PE→BI: k = 35, funnel plot symmetric, Egger's p = 0.42, 25% dissertations
- **Decision:** No downgrade (no evidence of bias)

**Example 2:**
- ANX→BI: k = 12, funnel plot asymmetric (small studies more negative), Egger's p = 0.03
- PET-PEESE: unadjusted r = -0.25, adjusted r = -0.18 (still significant)
- **Decision:** Downgrade −1 (suspected publication bias, but effect remains after correction)

**Example 3:**
- TRA→TRU: k = 8, cannot reliably assess publication bias
- **Decision:** Note as limitation in Summary of Findings; no downgrade (insufficient data)

**Documentation:**
- "Funnel plot symmetric; Egger's test p = 0.42; 25% grey literature" → No downgrade
- "Funnel plot asymmetric; Egger's p = 0.03; PET-PEESE correction: r changed from -0.25 to -0.18 (remains significant)" → Downgrade −1

---

## GRADE Summary of Findings Table Template

**Table: Summary of Findings — Model 2 (Integrated Model)**

| Path | Pooled β (95% CI) | k | N | I² | Certainty | Factors Affecting Certainty |
|------|-------------------|---|---|----|-----------|-----------------------------|
| PE → BI | 0.45 (0.40, 0.50) | 35 | 8,500 | 62% | ⊕⊕⊕⊕ HIGH | No serious limitations |
| EE → BI | 0.32 (0.26, 0.38) | 32 | 7,800 | 55% | ⊕⊕⊕◯ MODERATE | Downgrade −1: 30% weight from high risk-of-bias studies |
| SI → BI | 0.28 (0.20, 0.36) | 28 | 6,200 | 70% | ⊕⊕◯◯ LOW | Downgrade −1: inconsistency (I²=70%, PI crosses 0.10)<br>Downgrade −1: imprecision (wide CI) |
| TRU → BI | 0.38 (0.32, 0.44) | 22 | 5,100 | 48% | ⊕⊕⊕◯ MODERATE | Downgrade −1: indirectness (25% moderate-confidence construct mapping) |
| ANX → BI | -0.22 (-0.30, -0.14) | 18 | 4,200 | 65% | ⊕⊕◯◯ LOW | Downgrade −1: risk of bias (35% high risk)<br>Downgrade −1: inconsistency (I²=65%, unexplained) |
| TRA → TRU | 0.42 (0.35, 0.49) | 15 | 3,400 | 52% | ⊕⊕⊕◯ MODERATE | Downgrade −1: publication bias suspected (Egger's p=0.04) |
| BI → UB | 0.50 (0.44, 0.56) | 30 | 6,800 | 58% | ⊕⊕⊕◯ MODERATE | Downgrade −1: indirectness (60% of studies used BI only, no UB measure) |

**Legend:**
- **⊕⊕⊕⊕ HIGH:** Very confident in the effect estimate
- **⊕⊕⊕◯ MODERATE:** Moderately confident; true effect likely close but may differ
- **⊕⊕◯◯ LOW:** Limited confidence; true effect may be substantially different
- **⊕◯◯◯ VERY LOW:** Very little confidence; true effect likely substantially different

**k:** Number of studies
**N:** Total sample size
**I²:** Heterogeneity percentage

---

## Interpretation Guide

### High Certainty (⊕⊕⊕⊕)

**Meaning:** Very confident the true association is close to the estimate.

**Implications:**
- Strong evidence for the association
- Future research very unlikely to change the conclusion
- Can inform practice/theory with high confidence

**Example:** PE→BI (β = 0.45, ⊕⊕⊕⊕)
- "High certainty that performance expectancy is positively associated with behavioral intention in AI adoption contexts"

### Moderate Certainty (⊕⊕⊕◯)

**Meaning:** Moderately confident; true effect likely close but possibly substantially different.

**Implications:**
- Moderate evidence for the association
- Future research may change the estimate but unlikely to reverse direction
- Can inform practice/theory with some caution

**Example:** TRU→BI (β = 0.38, ⊕⊕⊕◯, downgraded for indirectness)
- "Moderate certainty that AI trust is positively associated with behavioral intention; construct measurement varied across studies"

### Low Certainty (⊕⊕◯◯)

**Meaning:** Limited confidence; true effect may be substantially different.

**Implications:**
- Limited evidence; association plausible but uncertain
- Future research likely to change the estimate
- Use with caution for practice/theory; more research needed

**Example:** ANX→BI (β = -0.22, ⊕⊕◯◯, downgraded for RoB + inconsistency)
- "Low certainty that AI anxiety is negatively associated with behavioral intention; high risk of bias and unexplained heterogeneity reduce confidence"

### Very Low Certainty (⊕◯◯◯)

**Meaning:** Very little confidence; true effect likely substantially different from estimate.

**Implications:**
- Very limited evidence; association highly uncertain
- Any estimate very uncertain
- Should not inform practice; more high-quality research essential

**Example:** AUT→ANX (β = 0.18, ⊕◯◯◯, downgraded for RoB + inconsistency + imprecision)
- "Very low certainty about the association between perceived AI autonomy and AI anxiety; wide confidence interval, high risk of bias, and substantial heterogeneity"

---

## Reporting GRADE in Manuscript

### Methods Section

**Certainty Assessment:**
> "We assessed the certainty of evidence for each key path coefficient using the GRADE framework (Guyatt et al., 2008), adapted for meta-analytic structural equation modeling. We started at High certainty (large samples, multiple studies, quantitative synthesis) and systematically considered five domains: (1) risk of bias, (2) inconsistency (heterogeneity), (3) indirectness (construct harmonization, outcome relevance), (4) imprecision (confidence interval width, sample size), and (5) publication bias. Each domain could result in downgrading certainty by 1-2 levels. Two reviewers independently assessed certainty for each path; discrepancies were resolved by consensus."

### Results Section

**Present Summary of Findings Table** (see template above)

**Narrative Summary:**
> "Certainty of evidence varied across paths. High certainty (⊕⊕⊕⊕) was achieved for PE→BI (β = 0.45, 95% CI [0.40, 0.50]), indicating strong, consistent evidence for the performance expectancy-intention relationship in AI contexts. Moderate certainty (⊕⊕⊕◯) was assigned to TRU→BI, EE→BI, TRA→TRU, and BI→UB due to concerns about construct harmonization indirectness (TRU→BI), risk of bias (EE→BI), publication bias (TRA→TRU), or outcome indirectness (BI→UB). Low certainty (⊕⊕◯◯) was assigned to SI→BI and ANX→BI due to unexplained heterogeneity and imprecision."

### Discussion Section

**Limitations — Link to GRADE:**
> "GRADE assessments identified key limitations. First, 30% of studies were rated high risk for common method bias, reducing certainty for some paths (e.g., EE→BI downgraded to Moderate). Second, substantial heterogeneity (I² > 60%) for several paths remained unexplained after meta-regression, indicating important moderators not captured in our analysis. Third, construct harmonization required moderate-confidence mapping for 25% of studies, introducing indirectness. Future research should employ multi-source data (reduce CMB), longitudinal designs (test temporal ordering), and standardized AI acceptance scales (improve construct validity)."

---

## GRADE Resources

### Assessment Tools

**Online GRADE Calculator:**
- GRADEpro GDT (Guideline Development Tool): https://www.gradepro.org/

**R Package:**
- `gradepro` (under development; manual calculation currently required)

### Key References

- Guyatt, G. H., et al. (2008). GRADE: An emerging consensus on rating quality of evidence and strength of recommendations. *BMJ*, 336(7650), 924-926.
- Guyatt, G. H., et al. (2011). GRADE guidelines: 1. Introduction—GRADE evidence profiles and summary of findings tables. *Journal of Clinical Epidemiology*, 64(4), 383-394.
- Guyatt, G. H., et al. (2011). GRADE guidelines: 5. Rating the quality of evidence—publication bias. *Journal of Clinical Epidemiology*, 64(12), 1277-1282.
- Murad, M. H., et al. (2014). The effect of publication bias magnitude and direction on the certainty in evidence. *BMJ Evidence-Based Medicine*, 23(3), 84-86.
- Schünemann, H. J., et al. (2013). Grading quality of evidence and strength of recommendations for diagnostic tests and strategies. *BMJ*, 346, f2015.

### GRADE Working Group
- Official website: https://www.gradeworkinggroup.org/
- Handbook: https://gdt.gradepro.org/app/handbook/handbook.html

---

**End of GRADE Evidence Assessment Framework**

**Version:** 1.0.0
**Date:** 2026-02-16
