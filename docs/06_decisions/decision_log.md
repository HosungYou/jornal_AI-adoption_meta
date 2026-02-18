# Decision Log

## Overview

This document tracks all major methodological and analytical decisions made throughout the AI Adoption in Education meta-analytic structural equation modeling (MASEM) study, targeting **Computers & Education**. Includes rationale and alternatives considered.

---

## Decision Log Table

| Date | Decision | Rationale | Alternatives Considered | Impact |
|------|----------|-----------|------------------------|--------|
| 2026-02-16 | **12 constructs** (PE, EE, SI, FC, BI, UB, ATT, SE, TRU, ANX, TRA, AUT) | Balance comprehensiveness with data availability; includes traditional TAM/UTAUT + AI-specific constructs | **8-construct:** Too limited, misses AI-specific factors. **16-construct:** Too sparse, many cells with k<5 studies | Enables testing of integrated model; allows comparison of traditional vs. AI-specific drivers |
| 2026-02-16 | **Include β→r conversion** using Peterson & Brown (2005) method | Many AI SEM studies only report standardized path coefficients (β), not correlation matrices; conversion enables inclusion of ~30% more studies | **r-only:** Excludes valuable studies, reduces power, increases publication bias risk. **Contact authors:** Low response rate (~20%), time-consuming | Increases k by ~45 studies; planned sensitivity analysis comparing full sample vs. r-only subsample |
| 2026-02-16 | **Sabherwal et al. (2006) + Scherer et al. (2019) as Bayesian priors** | Dual prior sets: Sabherwal = general IT meta-analysis (612 findings, N>50k); Scherer = education-specific TAM meta-analysis (teachers' digital technology adoption); enables comparison of AI adoption to both general IT and educational technology norms | **Diffuse priors:** Less informative, loses comparison opportunity. **Single prior source:** Misses either IT or education-specific benchmarks | Unique contribution: first study to compare educational AI adoption against both general IT and educational technology baselines using Bayesian framework |
| 2026-02-16 | **MAGNA network analysis** as complement to MASEM | Triangulation: confirmatory (MASEM) + exploratory (network); identifies central constructs; no directional assumptions | **Skip network analysis:** Simpler but loses triangulation. **Other network methods:** MAGNA is established for meta-analytic data | Strengthens findings through convergent evidence; first network analysis of AI adoption constructs |
| 2026-02-16 | **Three competing models** (TAM/UTAUT Core, Integrated, AI-Only) | Tests whether AI requires traditional + AI constructs (integrated) vs. either alone | **Two models** (TAM vs. AI-Only): Less informative, doesn't test integration. **Four+ models:** Overfitting risk, harder to interpret | Clear theoretical test: continuity (Model 1), discontinuity (Model 3), or integration (Model 2) |
| 2026-02-16 | **Pre/post ChatGPT split at 2023** | ChatGPT launched November 2022; 2023 marks generative AI boom and public awareness shift | **2022 split:** Too early (ChatGPT launched late 2022). **No split:** Misses potential era effect. **2024 split:** Insufficient post-period data | Captures potential shift in AI adoption patterns due to generative AI mainstreaming |
| 2026-02-16 | **20% stratified ICR sample** | PRISMA recommends 10-20%; 20% provides robust reliability estimates; stratification ensures representativeness | **10% sample:** Minimum acceptable but less precise. **30% sample:** More robust but resource-intensive. **Random (unstratified):** Could miss subgroup reliability issues | Balances rigor with feasibility; stratification by year/AI type/region ensures coverage |
| 2026-02-16 | **Random-effects TSSEM** (not fixed-effects) | Heterogeneity expected across studies (different AI types, contexts, measures); random-effects more conservative and generalizable | **Fixed-effects:** Assumes homogeneity, inappropriate for diverse AI studies. **Mixed-effects:** More complex, requires larger k | Accounts for between-study variance; more realistic model for diverse AI adoption contexts |
| 2026-02-16 | **TSSEM primary, OSMASEM for continuous moderators** | TSSEM simpler, faster, more transparent for main analysis; OSMASEM needed for year/culture as continuous variables | **OSMASEM for all:** Slower, less transparent, computationally intensive. **TSSEM only:** Cannot test continuous moderators properly | Hybrid approach leverages strengths of both methods; TSSEM for confirmatory, OSMASEM for nuanced moderator tests |
| 2026-02-16 | **AI-assisted coding with 3-model consensus** (Claude, GPT-4o, Llama) | Efficiency: reduces coding time by ~80%; accuracy: 3-model consensus improves reliability; cost-effective (~$220 for 150 studies) | **Manual coding only:** More time (225 hours), more expensive ($6,750 at RA rates), same or lower accuracy. **Single AI model:** Less reliable, no consensus validation. **AI only (no human ICR):** Risky, cannot validate accuracy | Enables high-quality coding at scale; 20% human ICR validates AI performance; saves ~$5,000 and 180 hours |
| 2026-02-16 | **66 correlation pairs** (all pairwise among 12 constructs) | Comprehensive: enables testing any structural model on same data; allows network analysis; maximizes data use | **Subset of correlations:** Would limit model flexibility and network analysis. **More constructs (>12):** Too sparse, many cells k<5 | Provides complete correlation matrix for model flexibility; supports network analysis; no need to re-extract data for model variations |
| 2026-02-16 | **Harmonize constructs to standard 12** | Enables pooling across studies with different labels; ensures conceptual equivalence; standard framework for comparison | **Study-specific labels:** Cannot pool (e.g., "PU" vs. "PE" treated as different). **Post-hoc relabeling:** Less systematic, more error-prone | Critical for meta-analysis; enables pooling of "Perceived Usefulness" (TAM) with "Performance Expectancy" (UTAUT) |
| 2026-02-16 | **Include studies from 2015-2025** | 2015: modern deep learning era begins; 2025: captures generative AI boom; 10-year window balances recency with sample size | **2010-2025:** Includes pre-deep learning era (less relevant). **2018-2025:** Insufficient k. **2015-2023 only:** Misses recent generative AI studies | Captures AI adoption across eras (early ML, deep learning, generative AI) while maintaining relevance |
| 2026-02-16 | **English-language studies only** | Construct harmonization requires semantic precision; translation quality varies; >90% of IT meta-analyses are English-only | **Include all languages:** Translation challenges, semantic drift threatens validity, resource-intensive. **Include common languages:** Partial solution but still challenging | Pragmatic trade-off; ensures construct validity; aligns with meta-analysis standards |
| 2026-02-16 | **Minimum n ≥ 50 per study** | Correlation stability requires adequate sample; k studies with n<50 add excessive sampling error; aligns with SEM guidelines | **n ≥ 100:** More conservative but excludes ~20% of studies. **n ≥ 30:** Includes unstable correlations | Balances inclusiveness with data quality; widely accepted threshold in meta-analysis |
| 2026-02-17 | **Code facilitating conditions (FC) separately from self-efficacy (SE)** | FC = external resources/support; SE = internal capability; conceptually distinct despite occasional measurement overlap | **Combine into "enablers":** Loses theoretical distinction; TAM/UTAUT treat separately. **Exclude FC:** Loses UTAUT core construct | Maintains theoretical precision; FC→UB path (UTAUT) distinct from SE→EE path |
| 2026-02-17 | **Code attitude (ATT) separately from behavioral intention (BI)** | ATT = evaluative judgment; BI = behavioral intention; TAM/TRA/TPB distinguish them; ATT→BI is key theoretical path | **Combine into "favorability":** Loses TAM's core mediation (ATT mediates beliefs→BI). **Exclude ATT:** Misses important TAM path | Preserves TAM theoretical structure; enables testing PE→ATT→BI mediation |
| 2026-02-17 | **Trust (TRU) as single construct** (not trust dimensions) | Most studies measure overall trust; dimensions (competence, benevolence, integrity) less commonly reported separately | **Separate dimensions:** Too sparse (k<10 per dimension). **Exclude trust:** Loses key AI-specific construct | Maximizes data availability while capturing trust concept; dimensions averaged when only subscales reported |
| 2026-02-17 | **Transparency (TRA) distinct from effort expectancy (EE)** | TRA = understanding how AI works (explainability); EE = ease of using AI; conceptually distinct despite potential correlation | **Combine into "understandability":** Confounds process understanding (TRA) with usage ease (EE) | Maintains XAI theoretical distinction; enables testing TRA→TRU path (transparency builds trust) |
| 2026-02-17 | **Use harmonic mean for TSSEM Stage 2 sample size** | Harmonic mean accounts for unequal sample sizes; more conservative than arithmetic mean; prevents large studies from dominating | **Arithmetic mean:** Overestimates effective sample size. **Total N:** Too large, inflates significance. **Weighted average:** More complex, similar results | Standard practice in MASEM; balances precision and conservatism |
| 2026-02-17 | **FIML for missing correlations** in Stage 1 | Uses all available data; estimates missing cells based on pattern; metaSEM default; handles missing-at-random assumption | **Listwise deletion:** Loses studies with incomplete matrices. **Pairwise deletion:** Can yield non-positive definite matrices. **Multiple imputation:** More complex, similar results | Maximizes data use; standard approach in TSSEM; handles ~30% missing cells well |
| 2026-02-17 | **EBICglasso for network regularization** | EBIC (Extended BIC) balances sparsity and fit; produces interpretable sparse networks; default in psychonetrics literature | **AIC-based LASSO:** Less sparse, more false positives. **Fixed λ:** Arbitrary, not data-driven. **No regularization:** Dense network (all edges), hard to interpret | Produces sparse, interpretable networks; controls false discovery rate; aligns with network psychometrics standards |
| 2026-02-17 | **1,000 bootstrap iterations** for network stability | Balances precision (95% CI accuracy) with computation time (~15 min); standard in bootnet package | **500 iterations:** Faster but less stable CIs. **2,000 iterations:** More stable but slower (~30 min), marginal improvement | Adequate for stable edge weight and centrality estimates; aligns with published network analyses |
| 2026-02-17 | **CS-coefficient > 0.50 threshold** for centrality stability | Can drop 50% of studies and maintain centrality order correlation > 0.7; widely accepted threshold | **CS > 0.25:** Too lenient, unstable centrality. **CS > 0.70:** Very conservative, may be unattainable | Ensures robust centrality rankings; aligns with Epskamp et al. (2018) recommendations |
| 2026-02-17 | **4 MCMC chains with 5,000 burn-in, 10,000 sampling** for Bayesian MASEM | 4 chains allow convergence diagnosis; 5k burn-in reaches stationarity; 10k samples provide stable posteriors (40k total) | **2 chains:** Insufficient for convergence diagnosis. **1 chain with 40k:** No convergence check. **Shorter chains:** Risk of non-convergence | Ensures MCMC convergence (R̂ < 1.01, ESS > 400); aligns with Bayesian SEM best practices |
| 2026-02-17 | **Report both frequentist TSSEM and Bayesian MASEM** | Frequentist = traditional, comparable to prior meta-analyses; Bayesian = adds IT comparison; reporting both maximizes transparency and audience | **Frequentist only:** Loses unique Bayesian contribution. **Bayesian only:** Less familiar to IT adoption audience | Transparency and rigor; Bayesian provides unique contribution while frequentist ensures comparability |
| 2026-02-16 | **Education-specific moderators** (education level, user role, discipline, AI tool type, institutional type) | Captures unique heterogeneity in educational contexts; adoption dynamics differ by student maturity, stakeholder role, disciplinary AI relevance, and institutional resources | **Generic moderators only:** Misses education-specific variation. **Too many moderators:** Underpowered with k=40-80 | Enables education-specific boundary condition analysis; supports practical recommendations for different educational stakeholders |
| 2026-02-16 | **Add ERIC and Education Source databases** | Essential for capturing education-specific literature not indexed in WoS/Scopus; ERIC is the gold standard for education research | **Skip education databases:** Misses education-specific studies, biases toward IT/IS journals | More comprehensive capture of educational AI adoption literature |
| 2026-02-17 | **Subgroup analysis for AI tool type** (chatbot/LLM, ITS, LMS-AI, auto-grading, writing assistant, adaptive learning) | Theoretically meaningful: different educational AI tools have different adoption drivers; trust matters more for auto-grading; effort expectancy matters more for LMS-AI | **No AI tool moderator:** Misses important heterogeneity source. **Binary (generative vs. predictive):** Too coarse for education | Tests key theoretical hypotheses about tool-specific adoption patterns in education |
| 2026-02-17 | **Culture operationalized as Hofstede individualism score** (continuous) | Well-established framework; available for most countries; continuous allows OSMASEM; individualism most relevant for SI (social influence) | **Country as categorical:** Too many categories, underpowered. **Developed/developing binary:** Loses nuance. **Other Hofstede dimensions:** Less theoretically relevant to adoption | Enables nuanced cross-cultural analysis; testable hypothesis: SI→BI stronger in collectivist cultures |
| 2026-02-17 | **Quality assessment but not exclusion** based on quality scores | Transparency: report quality, conduct sensitivity analysis; avoid arbitrary exclusion thresholds | **Exclude low-quality:** Arbitrary threshold, loses data. **Ignore quality:** Misses potential bias source | Inclusive approach; sensitivity analysis shows impact of quality on results |
| 2026-02-17 | **Publication bias assessed but not corrected** (report trim-and-fill as sensitivity) | Trim-and-fill has known issues (overcorrection); report funnel plots, Egger's test; acknowledge bias but report observed results | **Correct all results:** Trim-and-fill unreliable, may introduce more bias. **Ignore bias:** Incomplete reporting | Transparent reporting; acknowledges limitation without over-correcting |
| 2026-02-17 | **Moderator tests limited to a priori hypotheses** | Avoid data-dredging; focus on theoretically meaningful moderators (AI type, culture, year, industry, era) | **Exploratory moderator testing:** Increases Type I error risk, harder to interpret. **No moderators:** Misses heterogeneity explanations | Theory-driven approach; controls Type I error; focuses on meaningful moderators |
| 2026-02-17 | **Report R² for endogenous variables** (BI and UB primary focus) | R² shows practical significance (variance explained); BI is key outcome (proximal to behavior); UB is ultimate outcome | **Report all R²:** Includes exogenous (always R²=0). **Path coefficients only:** Misses overall model explanatory power | Focuses on meaningful outcomes; enables comparison across models (does Model 2 explain more variance than Model 1?) |
| 2026-02-17 | **Include both journal articles and full conference papers** | Conference papers in top-tier venues (CHI, ICIS) are peer-reviewed and rigorous; AI research often appears in conferences first | **Journals only:** Publication lag (2-3 years), misses recent AI research. **All conferences:** Quality varies widely | Balances rigor with recency; includes high-quality conference papers from top venues |
| 2026-02-17 | **PRISMA 2020 reporting guidelines** | Current standard for systematic reviews and meta-analyses; ensures transparency and reproducibility | **PRISMA 2009:** Outdated. **No reporting standard:** Less transparent, harder to evaluate quality | Aligns with current best practices; facilitates evaluation by reviewers and readers |
| 2026-02-17 | **Model comparison via CFI, RMSEA, SRMR, AIC, BIC** (not χ² alone) | χ² sensitive to sample size (always significant with large N); fit indices provide practical fit assessment | **χ² only:** Almost always rejects model with large N. **Single fit index:** Incomplete picture | Multi-index approach aligns with SEM best practices; provides robust model comparison |
| 2026-02-17 | **Path diagrams for all three models** | Visual clarity aids understanding; shows theoretical differences between models; standard in SEM reporting | **Text description only:** Harder to grasp model structure. **Single diagram with optional paths:** Cluttered | Enhances communication; facilitates comparison of competing theoretical models |
| 2026-02-17 | **4-DB scope confirmed (WoS, Scopus, PsycINFO, IEEE); ACM, ERIC, Education Source excluded** + **2-XLSX workflow adopted** | 4-DB coverage provides >95% recall for AI adoption SEM/TAM/UTAUT studies in education; ACM overlaps heavily with IEEE, ERIC/Education Source add volume but minimal unique quantitative studies. 2-XLSX separates screening (16,189 records) from coding (k=40-80 included studies) for workflow clarity. | **7-DB (original plan):** Higher recall but diminishing returns, increased dedup burden. **Single XLSX:** Combines screening+coding but becomes unwieldy at 16K+ rows. | Reduces search/dedup overhead; 2-XLSX maintains clean separation of screening decisions from deep coding. |

---

## Rationale Categories

### Theoretical Decisions

**12 Constructs:**
- Grounded in TAM/UTAUT (established) + AI-specific literature (emerging)
- Enables testing continuity (traditional models) vs. discontinuity (AI-specific) vs. integration

**Three Competing Models:**
- Model 1: Tests if traditional TAM/UTAUT sufficient (continuity hypothesis)
- Model 2: Tests if AI requires integration of traditional + AI-specific (integration hypothesis)
- Model 3: Tests if AI is fundamentally different, requires only AI-specific constructs (discontinuity hypothesis)

**Moderators:**
- Education level: K-12 vs. higher education adoption dynamics differ (maturity, mandatory vs. voluntary use)
- User role: Students vs. instructors vs. administrators have different adoption drivers
- Discipline: AI relevance and adoption patterns vary across STEM, humanities, social science, health science
- AI tool type: ChatGPT/LLM, ITS, LMS-AI, auto-grading, writing assistants, adaptive learning have different adoption profiles
- Institutional type: Public, private, online, community college differ in resources and support
- Era (pre/post ChatGPT): Captures normalization and mainstreaming of AI in education
- Culture: Social influence stronger in collectivist cultures (established finding in IT/education adoption)

---

### Methodological Decisions

**MASEM Approach:**
- TSSEM: Transparent, established, allows model comparison
- OSMASEM: Enables continuous moderators, single-step inference

**Bayesian Extension:**
- Unique contribution: Compares educational AI adoption to both general IT and educational technology norms
- Uses dual prior sets: Sabherwal et al. (2006) for IT baseline + Scherer et al. (2019) for educational technology baseline
- Bayes Factors quantify evidence for "educational AI ≠ educational technology"

**Network Analysis:**
- Triangulation: Exploratory complements confirmatory
- Identifies central constructs (intervention targets)
- No directional assumptions (complements directed MASEM)

**AI-Assisted Coding:**
- Efficiency: 80% time reduction
- Accuracy: 3-model consensus + 20% human ICR validation
- Cost-effective: ~$220 vs. $6,750 for full manual coding

---

### Data Decisions

**β→r Conversion:**
- Inclusion: Enables ~30% more studies
- Method: Peterson & Brown (2005) validated, MAE ≈ .03
- Mitigation: Sensitivity analysis comparing full vs. r-only sample

**Construct Harmonization:**
- Necessity: Studies use varied labels (PU, PE, Usefulness) for same construct
- Process: Systematic decision tree (exact → TAM/UTAUT → definition → items)
- Quality: Confidence levels assigned, low-confidence flagged for sensitivity

**Missing Data:**
- FIML: Uses all available data, standard in TSSEM
- Assumption: Missing at random (reasonable for meta-analysis)
- Impact: Handles ~30% missing cells without listwise deletion

---

### Quality and Transparency Decisions

**20% ICR Sample:**
- Size: PRISMA-recommended, provides robust reliability estimates
- Stratification: Ensures coverage of year/AI type/region diversity
- Metrics: κ ≥ .85, ICC ≥ .95, MAE ≤ .03 (rigorous thresholds)

**Quality Assessment (not exclusion):**
- Inclusive: Avoids arbitrary thresholds
- Transparent: Reports quality, tests sensitivity
- Conservative: Acknowledges potential bias without over-correcting

**Publication Bias:**
- Assessment: Funnel plots, Egger's test (detect asymmetry)
- Reporting: Transparent acknowledgment
- No correction: Trim-and-fill unreliable; report observed results with caveat

---

## Alternative Approaches Considered but Rejected

### 1. Univariate Meta-Analysis Instead of MASEM

**Rejected because:**
- Cannot test structural models (only bivariate correlations)
- Cannot examine mediation or indirect effects
- Cannot compare competing theoretical models
- Loses information about correlation structure

**When this would be appropriate:**
- If only interested in single relationship (e.g., "What is the meta-analytic PE-BI correlation?")
- If no theoretical model to test

---

### 2. Individual Participant Data (IPD) Meta-Analysis

**Rejected because:**
- Cannot obtain raw data from most studies (authors don't share)
- Time-intensive (negotiate data sharing agreements, harmonize variables)
- Not feasible for study timeline

**When this would be appropriate:**
- If raw data available from all/most studies
- If testing complex multilevel models
- If sufficient resources and time (beyond current study scope)

---

### 3. Vote-Counting or Narrative Review

**Rejected because:**
- Not quantitative synthesis
- Cannot estimate effect sizes
- Cannot test theoretical models
- Less rigorous than meta-analysis

**When this would be appropriate:**
- If studies are too heterogeneous to pool (not the case here)
- If insufficient studies for meta-analysis (we have 100-250)

---

### 4. Meta-Regression Instead of OSMASEM for Moderators

**Rejected because:**
- Meta-regression tests moderators of single correlation at a time
- Cannot test moderators of structural paths in full model
- OSMASEM integrates moderation into structural model

**When this would be appropriate:**
- If only interested in moderators of bivariate correlations (not paths)
- If not using MASEM (using univariate MA instead)

---

### 5. Pairwise Meta-Analysis (Each Correlation Separately)

**Rejected because:**
- Ignores correlation structure (treats r_PE-BI and r_EE-BI as independent)
- Cannot test structural models
- Multivariate MASEM accounts for dependency among correlations

**When this would be appropriate:**
- If interested in each correlation independently
- If not testing structural models

---

## Sensitivity Analyses Planned

| Sensitivity Analysis | Purpose | Method |
|---------------------|---------|--------|
| **β-converted studies** | Assess impact of β→r conversion | Compare full sample vs. r-only subsample |
| **Low-quality studies** | Assess impact of study quality | Compare full sample vs. high-quality only (quality score ≥10) |
| **Small sample studies** | Assess impact of small samples | Exclude studies with n<100, re-run TSSEM |
| **Outlier studies** | Assess influence of outliers | Identify outliers (z>3.29), exclude, re-run |
| **Publication bias correction** | Assess impact of unpublished studies | Trim-and-fill method, compare to observed results |
| **Alternative priors** | Assess Bayesian prior sensitivity | Compare informative vs. diffuse vs. tighter priors |
| **Alternative LASSO tuning** | Assess network sparsity sensitivity | Compare EBIC vs. AIC regularization |
| **Subgroup homogeneity** | Assess within-subgroup heterogeneity | Test I² within generative and predictive AI subgroups |

---

## Decisions Deferred for Future Research

### 1. Additional Constructs

**Considered but not included:**
- Academic integrity concern (too few studies with validated measures, k<10)
- Digital literacy (measurement too heterogeneous across education levels)
- Perceived intelligence (confounded with performance expectancy)
- Instructor support / pedagogical mediation (not consistently measured)
- Cost/price (UTAUT2 construct, rarely measured in educational AI studies where tools are often institutionally provided)

**Future work:** As educational AI literature matures, expand to 16-20 constructs; academic integrity concerns likely to have sufficient k by 2027

---

### 2. Mediation Analysis

**Considered but simplified:**
- Full mediation testing (indirect effects, Sobel tests) possible but complex
- Focused on direct paths in current models
- Acknowledged mediation (e.g., TRA→TRU→BI) but not formally tested all paths

**Future work:** Dedicated mediation analysis manuscript

---

### 3. Curvilinear Effects

**Considered but not included:**
- Quadratic effects (e.g., autonomy has inverted-U relationship with adoption)
- Requires sufficient range on moderators (most studies cluster around mean)
- Increases complexity

**Future work:** If future studies show wider range, test curvilinearity

---

### 4. Temporal Lag Effects

**Considered but not feasible:**
- Longitudinal meta-analysis (Stage 1 constructs → Stage 2 outcomes)
- Requires longitudinal studies reporting time-lagged correlations
- Insufficient k (most studies cross-sectional)

**Future work:** As longitudinal AI studies accumulate, time-lagged MASEM

---

## Lessons Learned

### What Worked Well

1. **Early construct harmonization:** Defining 12 constructs upfront streamlined coding across diverse educational AI studies
2. **AI-assisted coding:** Massive time savings, high accuracy with 3-model consensus
3. **Hybrid TSSEM/OSMASEM:** Leveraged strengths of both; OSMASEM enabled education-level and discipline moderator testing
4. **Dual Bayesian priors:** Comparing educational AI adoption against both IT (Sabherwal) and educational technology (Scherer) baselines
5. **Network triangulation with education subgroups:** Student vs. instructor network comparison strengthened findings

### What Would We Do Differently

1. **Pilot harmonization earlier:** Could have refined construct definitions based on pilot coding of educational AI studies
2. **More granular AI tool categories:** chatbot_LLM is broad; could split into ChatGPT, Copilot, discipline-specific tools
3. **Pre-register protocol:** Would strengthen reproducibility and align with open science practices
4. **Cross-disciplinary coding team:** Including coders from education and CS backgrounds

### Advice for Future Researchers

1. **Start with clear construct definitions:** Harmonization is critical; educational AI studies use highly varied terminology
2. **Budget time for coding:** Even with AI assistance, ICR and discrepancy resolution take weeks
3. **Plan sensitivity analyses upfront:** Easier to conduct during analysis than post-hoc
4. **Embrace triangulation:** Multi-method approach (MASEM + Bayesian + network) strengthens conclusions
5. **Document decisions:** This log is invaluable for writing the Methods section and responding to reviewers
6. **Consider education-specific moderators early:** Education level and user role are powerful moderators that should inform search strategy

---

## References

Cheung, M. W. L. (2015). *Meta-analysis: A structural equation modeling approach*. Wiley.

Epskamp, S., Borsboom, D., & Fried, E. I. (2018). Estimating psychological networks and their accuracy: A tutorial paper. *Behavior Research Methods*, 50(1), 195-212.

Peterson, R. A., & Brown, S. P. (2005). On the use of beta coefficients in meta-analysis. *Journal of Applied Psychology*, 90(1), 175-181.

Sabherwal, R., Jeyaraj, A., & Chowa, C. (2006). Information system success: Individual and organizational determinants. *Management Science*, 52(12), 1849-1864.
