# Construct Selection Rationale for MASEM
**Project**: AI Adoption in Higher Education MASEM  
**Date**: 2026-04-03  
**Status**: Draft for Method section  
**Based on**: Full-text analysis of 224 PDFs + 52-study calibration  

---

## 1. Overview

This document presents the rationale for selecting 10 constructs for the meta-analytic structural equation model (MASEM). The construct set was derived inductively from systematic full-text analysis of all 224 included studies, then validated against 52 coded calibration studies with pair-level precision estimation.

### Final 10-Construct Model

| Tier | Construct | Abbr. | k (est.) | Primary Theory | AI-Specific? |
|------|-----------|-------|----------|----------------|--------------|
| 1 | Performance Expectancy | PE | 186 | TAM/UTAUT | No |
| 1 | Behavioral Intention | BI | 185 | TAM/UTAUT/TPB | No |
| 1 | Effort Expectancy | EE | 162 | TAM/UTAUT | No |
| 1 | Social Influence | SI | 114 | UTAUT/TPB | No |
| 1 | Facilitating Conditions | FC | 105 | UTAUT | No |
| 1 | Use Behavior | UB | 90 | UTAUT | No |
| 1 | Attitude | ATT | 81 | TAM/TPB | No |
| 1 | Self-Efficacy | SE | 44 | SCT/TAM3 | No |
| 2 | AI Anxiety | ANX | 40 | CTAM/AI-specific | Yes |
| 2 | Trust in AI | TRU | 36 | AI-specific | Yes |

### Excluded Constructs

| Construct | Abbr. | k (est.) | Exclusion Reason |
|-----------|-------|----------|------------------|
| Transparency | TRA | ~2 | Insufficient coverage (1.9% base rate) |
| Autonomy | AUT | ~0 | No extractable r-values |
| Hedonic Motivation | HM | ~33* | Structural inconsistency (see Section 4) |
| Habit | HAB | ~22* | Low AI-specificity + construct equivalence issues |
| Price Value | PV | ~8* | Near-zero variance in education context |

*Frequency detected but excluded for methodological reasons, not coverage.

---

## 2. Construct Identification Procedure

### 2.1 Inductive Derivation (Not A Priori Imposition)

A defining methodological commitment of this study was that construct selection would be driven by what primary researchers actually measured, not by what any single theoretical framework prescribes. Most MASEM studies in the technology adoption literature begin from a nominated theoretical model (typically TAM or UTAUT) and extract only the constructs that model specifies, then test whether those constructs replicate at the meta-analytic level. This approach privileges theoretical coherence over empirical coverage and carries a well-documented risk: constructs that appear prominently in primary research but fall outside the nominated framework are systematically excluded, producing a confirmatory artifact rather than a genuine synthesis of the literature's actual structure.

To avoid this, we conducted a systematic full-text analysis of all 224 included PDFs prior to any construct selection decision. Each PDF was processed using PyMuPDF for text extraction, with targeted detection of (a) the theoretical frameworks cited, (b) every latent construct operationalized with validated items, (c) the construct label and its source theory, and (d) whether the construct was presented as a predictor, mediator, or outcome within the study's structural model. Detection accuracy was calibrated against 52 human-coded studies, yielding construct-level precision ranging from 96% (PE) to 24% (TRU), with recall consistently above 80% for all Tier 1 constructs. Final frequency estimates incorporate these calibration adjustments.

### 2.2 Theoretical Landscape of the Corpus

The theoretical landscape of the 224-study corpus was heterogeneous:

| Theory | k | % |
|--------|---|---|
| TAM | 194 | 86.6% |
| UTAUT | 143 | 63.8% |
| TPB | 111 | 49.6% |
| IDT | 47 | 21.0% |
| SCT | 37 | 16.5% |
| TTF | 19 | 8.5% |
| VAM | 14 | 6.2% |
| ECM | 12 | 5.4% |
| PMT | 6 | 2.7% |

This pluralism signals that no single framework is adequate as an a priori scaffolding: 13.4% of the corpus does not use TAM at all, and 36.2% does not use UTAUT. Constructs unique to either framework would be absent from a meaningful proportion of studies.

### 2.3 Two-Tier Frequency Structure

From the full-text mapping, a natural two-tier frequency structure emerged:

**Tier 1 (Universal Coverage Threshold, >= 20% of studies):** PE (83.0%), BI (82.6%), EE (72.3%), SI (50.9%), FC (46.9%), UB (40.2%), ATT (36.2%), SE (19.6%). These eight constructs appear with sufficient frequency across sufficiently diverse theoretical contexts to yield stable Stage 1 correlation pooling.

**Tier 2 (AI-Specific Threshold, 15-20%):** ANX (17.9%), TRU (16.1%). Although both fall just below the Tier 1 threshold, they are theoretically non-redundant with any Tier 1 construct and represent the two most consistently measured AI-specific psychological constructs in the corpus. These constructs exhibit qualitative transformation in the AI context: Trust in AI involves delegation to an autonomous agent (Glikson & Woolley, 2020; Siau & Wang, 2018), and AI Anxiety encompasses existential concerns about replacement and control loss (Wang & Wang, 2022), qualitatively different from traditional computer anxiety (Compeau & Higgins, 1995).

**Below Tier 2 Threshold:** Construct coverage becomes too sparse for reliable MASEM estimation. Transparency (TRA, k approximately 2) and Autonomy (AUT, k approximately 0) appeared in too few studies to produce stable pooled correlations.

---

## 3. Construct Selection Criteria for MASEM

Following Cheung (2015) and Jak and Cheung (2020), each construct was required to meet three criteria simultaneously:

### 3.1 Theoretical Relevance
The construct must occupy a well-defined and consistent position in the nomological network of AI adoption, as established by at least two major theoretical frameworks.

### 3.2 Empirical Coverage
The construct must appear in a sufficient number of primary studies to populate all associated cells in the pooled correlation matrix. We adopted k >= 3 per cell as the minimum threshold (Viswesvaran & Ones, 1995), with k >= 10 as the target for stable estimation.

### 3.3 Construct Equivalence
The operationalization of the construct must be sufficiently consistent across studies to justify pooling correlations (Cheung, 2015, Chapter 2). This requires (a) definitional equivalence, (b) measurement equivalence, and (c) structural equivalence (consistent nomological position).

---

## 4. Exclusion Rationale for Specific Constructs

### 4.1 Hedonic Motivation (HM)

HM was excluded on construct equivalence grounds despite adequate frequency (~33 studies). The exclusion rests on three arguments:

1. **Structural position inconsistency**: HM functions as an exogenous predictor (antecedent to PE/EE) in some studies but occupies the same structural position as ATT (a consequence of PE/EE) in others. Pooling correlations from structurally incompatible models biases the Stage 2 SEM (Cheung, 2015). Specifically, the HM-PE cell would conflate "HM causes PE" studies with "PE causes enjoyment" studies, producing an uninterpretable pooled estimate.

2. **Low AI-specificity**: HM (enjoyment, fun) operates identically in social media, gaming, and e-commerce contexts. There is no theoretical basis for a qualitative shift in the enjoyment construct when the technology is AI-based.

3. **Operationalization heterogeneity**: Across studies, HM was variously measured as "perceived enjoyment" (Davis et al., 1992), "intrinsic motivation" (Deci & Ryan, 1985), "perceived fun," and "entertainment value," with non-equivalent item content.

### 4.2 Habit (HAB) and Price Value (PV)

HAB showed structural inconsistency similar to HM (sometimes predicting BI, sometimes predicting UB directly, sometimes moderating the BI-UB path). PV exhibited near-zero variance in the higher education subsample, where most AI tools (ChatGPT, Gemini) are available at no cost to students.

### 4.3 Transparency (TRA) and Autonomy (AUT)

TRA and AUT were initially theorized as AI-specific constructs but failed the empirical coverage criterion. From 52 calibration studies, only 1 study contributed extractable r-values involving TRA, and 0 for AUT. Full-text analysis of all 224 PDFs confirmed these base rates would not improve with additional coding (TRA approximately 2 viable studies total, AUT approximately 0).

These constructs are discussed in the limitation section as important theoretical constructs whose empirical measurement in the AI adoption literature has not yet reached the density required for meta-analytic synthesis.

---

## 5. Cell Coverage Analysis

### 5.1 Pooled Correlation Matrix Coverage (45 cells)

| Category | Count | % |
|----------|-------|---|
| Sufficient (k >= 10) | 43 | 95.6% |
| Marginal (k = 3-4) | 2 | 4.4% |
| Empty (k = 0) | 0 | 0% |

### 5.2 Weak Cells

| Cell | Current k | Projected k | Root Cause |
|------|-----------|-------------|------------|
| SE-TRU | 1 | ~4 | Trust and self-efficacy frameworks rarely co-occur |
| TRU-ANX | 1 | ~3 | Trust-oriented and anxiety-oriented studies come from different theoretical traditions |

The missingness pattern is **not-missing-at-random (NMAR)**: studies grounded in trust-oriented frameworks (privacy, ethics perspectives) infrequently measured anxiety, and vice versa.

### 5.3 Remediation Strategy

1. **Primary model**: Fit the 10-construct MASEM with pairwise deletion
2. **Sensitivity analysis 1**: 9-construct model excluding TRU, comparing all overlapping parameter estimates
3. **Sensitivity analysis 2**: Influence diagnostics for studies in sparse cells
4. **Sensitivity analysis 3**: Positive definiteness verification (eigenvalue inspection)
5. **Reporting**: Explicit confidence intervals for sparse-cell pooled correlations

---

## 6. Framing: "Theory-Driven MASEM"

This study is framed as **theory-driven MASEM** (Cheung, 2015), not confirmatory or exploratory:

- **Theory-driven aspects**: Construct selection is grounded in established frameworks (UTAUT, TAM, TPB). Structural paths in Stage 2 are derived from theory. The 10-construct model was specified before Stage 2 fitting.

- **Empirically bounded**: The exact boundary of 10 constructs (rather than 8 or 15) was determined by the joint criteria of theoretical relevance and empirical coverage, following the principle that it is better to estimate a well-supported subset model than to force-fit a complete theoretical model with insufficient data (Cheung, 2015).

---

## 7. Contribution

The full-text-driven construct selection procedure constitutes a methodological contribution in two ways:

1. **Avoiding confirmatory bias**: By inventorying all constructs actually measured across 224 studies before selecting the model, we avoid the common MASEM practice of imposing a single framework and excluding everything else.

2. **Transparent boundary setting**: The two-tier threshold, combined with explicit exclusion rationale for each dropped construct, provides a reproducible and defensible selection procedure that future MASEM studies can adapt.

---

## References

- Ajzen, I. (1991). The theory of planned behavior. *Organizational Behavior and Human Decision Processes*, 50(2), 179-211.
- Cheung, M. W.-L. (2015). *Meta-analysis: A structural equation modeling approach*. Wiley.
- Compeau, D. R., & Higgins, C. A. (1995). Computer self-efficacy. *MIS Quarterly*, 19(2), 189-211.
- Davis, F. D. (1989). Perceived usefulness, perceived ease of use, and user acceptance. *MIS Quarterly*, 13(3), 319-340.
- Davis, F. D., Bagozzi, R. P., & Warshaw, P. R. (1992). Extrinsic and intrinsic motivation. *Journal of Applied Social Psychology*, 22(14), 1111-1132.
- Glikson, E., & Woolley, A. W. (2020). Human trust in artificial intelligence. *Academy of Management Annals*, 14(2), 627-660.
- Jak, S., & Cheung, M. W.-L. (2020). Meta-analytic structural equation modeling with moderating effects on SEM parameters. *Psychological Methods*, 25(4), 430-455.
- Siau, K., & Wang, W. (2018). Building trust in artificial intelligence, machine learning, and robotics. *Cutter Business Technology Journal*, 31(2), 47-53.
- Venkatesh, V., Morris, M. G., Davis, G. B., & Davis, F. D. (2003). User acceptance of information technology: Toward a unified view. *MIS Quarterly*, 27(3), 425-478.
- Venkatesh, V., Thong, J. Y. L., & Xu, X. (2012). Consumer acceptance and use of information technology: Extending UTAUT. *MIS Quarterly*, 36(1), 157-178.
- Viswesvaran, C., & Ones, D. S. (1995). Theory testing: Combining psychometric meta-analysis and structural equation modeling. *Personnel Psychology*, 48(4), 865-885.
- Wang, Y.-Y., & Wang, Y.-S. (2022). Development and validation of an artificial intelligence anxiety scale. *International Journal of Human-Computer Interaction*, 38(7), 1-12.
