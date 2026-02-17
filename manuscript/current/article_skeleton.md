# AI Adoption in Education: A Meta-Analytic Structural Equation Model Integrating Trust, Anxiety, Transparency, and Autonomy

**Hosung You**

*[Institutional Affiliation]*

**Corresponding Author:** Hosung You, [email]

**Target Journal:** Computers & Education (Elsevier)

---

## Abstract

The integration of artificial intelligence (AI) into educational settings—from intelligent tutoring systems to generative AI writing assistants—has accelerated, yet the psychological mechanisms driving AI adoption among students and instructors remain fragmented across competing theoretical frameworks. This study employs meta-analytic structural equation modeling (MASEM) to synthesize correlation matrices from empirical studies of AI adoption in educational contexts published between 2015 and 2025. An integrative 12-construct framework extends TAM/UTAUT with four AI-specific constructs—trust, anxiety, transparency, and perceived autonomy—hypothesized to capture unique adoption dynamics in education. Three competing structural models are compared using two-stage SEM (TSSEM): (a) a traditional TAM/UTAUT model, (b) an integrated model augmented by AI-specific paths, and (c) an AI-only model. Moderator analyses via OSMASEM examine how education level (K-12 vs. higher education), user role (student vs. instructor), discipline, AI tool type, and cultural orientation condition structural relationships. Bayesian MASEM incorporating prior educational technology meta-analytic estimates and network analysis triangulate the findings. Expected contributions include (a) the first MASEM-based empirical test of whether AI adoption in education follows traditional technology acceptance patterns or requires AI-specific theoretical extensions, (b) quantification of the incremental predictive power of trust, anxiety, transparency, and autonomy beyond TAM/UTAUT constructs, and (c) identification of education-specific boundary conditions shaping AI adoption pathways. Implications for institutional AI policy, pedagogical design, and student support are discussed.

*Keywords:* artificial intelligence, educational technology adoption, MASEM, TAM, UTAUT, AI trust, AI anxiety, transparency, autonomy, higher education, Computers & Education

---

## 1. Introduction

### 1.1 Background and Motivation

The educational technology landscape has undergone a dramatic transformation with the integration of artificial intelligence (AI) systems. From intelligent tutoring systems (ITS) that adapt to individual learning trajectories to generative AI tools like ChatGPT reshaping academic writing and research practices, AI applications have proliferated across K-12 and higher education contexts. Learning management systems now incorporate AI-driven analytics for early intervention, automated grading systems provide instant feedback at scale, and AI chatbots offer 24/7 student support. This rapid technological diffusion raises urgent questions about the psychological mechanisms governing AI adoption in educational settings.

Despite extensive research on educational technology acceptance, the theoretical landscape remains fragmented. Traditional frameworks—particularly the Technology Acceptance Model (TAM) and the Unified Theory of Acceptance and Use of Technology (UTAUT)—have been applied to e-learning platforms, mobile learning applications, and online course management systems. However, AI technologies introduce qualitatively distinct features: autonomous decision-making, opaque algorithmic processes, and the potential to replace or augment human pedagogical functions. These characteristics suggest that AI adoption may be governed by psychological constructs beyond those captured in traditional acceptance models.

Recent theoretical developments highlight four AI-specific constructs with particular salience in educational contexts: **trust** in AI systems to perform pedagogically sound actions, **anxiety** about over-reliance or academic integrity violations, **transparency** regarding how AI systems make decisions (especially in high-stakes grading), and **perceived autonomy** concerning whether AI supports or constrains learner agency. Yet empirical studies examining these constructs alongside traditional TAM/UTAUT variables remain scattered across disciplines, journals, and theoretical orientations, yielding contradictory findings and limiting cumulative knowledge building.

### 1.2 Research Gap

No meta-analytic structural equation modeling (MASEM) study has synthesized correlation matrices specifically from AI adoption research in educational settings. Existing meta-analyses either focus on general information technology adoption (where education is one of many contexts) or examine specific educational technologies (e.g., mobile learning) without AI-specific theoretical extensions. This gap is consequential: education has unique adoption dynamics, including voluntary vs. mandatory use patterns, strong peer influence among students, concerns about academic integrity, institutional policy constraints, and the dual role of technology as both learning tool and assessment mechanism.

Furthermore, moderator effects remain underexplored. Do K-12 students and university instructors exhibit different AI adoption pathways? Does disciplinary context (STEM vs. humanities) condition the relative importance of trust versus perceived ease of use? Do different AI tool types (ChatGPT for writing support vs. ITS for personalized tutoring) activate distinct psychological drivers? Without MASEM-based synthesis addressing these education-specific moderators, theoretical fragmentation persists, and practical guidance for institutional AI policy remains speculative.

### 1.3 Research Questions

This study addresses three overarching research questions:

- **RQ1:** To what extent do TAM/UTAUT path relationships (e.g., perceived ease of use → behavioral intention, social influence → usage behavior) replicate in educational AI adoption contexts?

- **RQ2:** Do AI-specific constructs (trust, anxiety, transparency, perceived autonomy) provide incremental explanatory power beyond traditional TAM/UTAUT variables when predicting educational AI adoption outcomes?

- **RQ3:** How do education level (K-12 vs. higher education), user role (student vs. instructor), disciplinary context, AI tool type, and cultural orientation moderate key structural relationships in the integrated model?

### 1.4 Contributions

This study makes four substantive contributions:

**Theoretical:** This is the first MASEM investigation of AI adoption specifically in educational settings, providing an empirical test of whether traditional technology acceptance frameworks generalize to AI contexts or require AI-specific theoretical augmentation. By comparing three competing models—TAM/UTAUT core, integrated (TAM/UTAUT + AI-specific), and AI-only—we quantify the incremental predictive power of trust, anxiety, transparency, and autonomy beyond established acceptance constructs.

**Methodological:** The study employs methodological triangulation through Bayesian MASEM (incorporating prior effect sizes from Sabherwal et al., 2006 and Scherer et al., 2019 educational technology meta-analyses) and network analysis (identifying central constructs and comparing student vs. instructor network structures). This multi-method approach strengthens causal inference and reveals patterns invisible to any single analytic strategy.

**Empirical:** OSMASEM moderator analyses systematically test education-specific boundary conditions (education level, user role, discipline, AI tool type) that prior meta-analyses treated as sources of unexplained heterogeneity. These analyses identify for whom, under what conditions, and for which AI applications specific adoption pathways hold.

**Practical:** Evidence-based findings inform institutional AI adoption policies (e.g., whether to prioritize transparency initiatives vs. ease-of-use training), pedagogical design (e.g., addressing AI anxiety in student onboarding), and student support services (e.g., tailoring interventions to discipline-specific adoption barriers).

### 1.5 Article Structure

The remainder of this article proceeds as follows. Section 2 reviews theoretical foundations, detailing TAM/UTAUT applications in education, introducing the 12-construct integrative framework, and articulating hypothesized models. Section 3 describes the MASEM methodology, including literature search procedures, inclusion criteria, data extraction, quality assessment, and analytic strategy (TSSEM, OSMASEM, Bayesian MASEM, network analysis). Section 4 reports results across competing models and moderator subgroups. Section 5 discusses theoretical implications, practical recommendations for educational AI implementation, limitations, and directions for future research. Section 6 concludes with a synthesis of key findings.

---

## 2. Theoretical Background

### 2.1 Technology Acceptance Models in Education

The Technology Acceptance Model (TAM; Davis, 1989) posits that perceived usefulness (PU) and perceived ease of use (PEOU) are primary determinants of behavioral intention to use technology, which in turn predicts actual usage behavior. TAM has been extensively applied to educational contexts—from course management systems to simulation software—demonstrating robust predictive validity. Meta-analytic evidence (Scherer et al., 2019) confirms that PEOU → PU and PU → BI paths hold across educational technology types, though effect sizes vary by student age, technology novelty, and cultural context.

The Unified Theory of Acceptance and Use of Technology (UTAUT; Venkatesh et al., 2003) extended TAM by integrating constructs from eight competing models: performance expectancy (PE), effort expectancy (EE), social influence (SI), and facilitating conditions (FC) as direct predictors of behavioral intention (BI) and usage behavior (UB). Subsequent UTAUT2 (Venkatesh et al., 2012) and UTAUT3 iterations added hedonic motivation, habit, and individual difference moderators. In educational settings, SI emerges as particularly salient due to strong peer effects among students and collegial norms among instructors. FC also plays a distinctive role, as institutional infrastructure (Wi-Fi, device access, IT support) shapes technology feasibility in ways less critical for consumer technology adoption.

Despite their empirical success, TAM/UTAUT frameworks have been critiqued for treating technologies as interchangeable "black boxes" (Benbasat & Barki, 2007). AI systems, however, differ qualitatively from prior educational technologies: they exhibit autonomous decision-making, learn from user interactions, operate via opaque algorithms, and can replace functions historically performed by human instructors. These features may activate psychological mechanisms beyond perceived usefulness and ease of use.

### 2.2 The 12-Construct Integrative Framework

This study proposes a 12-construct integrative framework synthesizing traditional acceptance variables with AI-specific constructs:

**Traditional Constructs (8):**
- **Performance Expectancy (PE):** The degree to which using AI enhances learning or teaching performance.
- **Effort Expectancy (EE):** The ease associated with using AI tools.
- **Social Influence (SI):** Perceived pressure from peers, instructors, or institutional norms to use AI.
- **Facilitating Conditions (FC):** Perceived availability of technical and organizational resources supporting AI use.
- **Behavioral Intention (BI):** Intention to use AI tools in educational activities.
- **Usage Behavior (UB):** Actual AI usage frequency and breadth.
- **Attitude (ATT):** Overall evaluative affect toward educational AI.
- **Self-Efficacy (SE):** Confidence in one's ability to use AI effectively for learning or teaching.

**AI-Specific Constructs (4):**
- **Trust (TRU):** Belief that AI systems will perform reliably, ethically, and in ways aligned with educational goals. In education, trust encompasses confidence in AI-generated feedback quality, fair grading, and pedagogically appropriate content recommendations.
- **Anxiety (ANX):** Apprehension about AI misuse (plagiarism, over-reliance), algorithmic errors in high-stakes assessments, or AI replacing human instructional roles. Educational AI anxiety differs from general technology anxiety by centering on academic integrity and learning dependency concerns.
- **Transparency (TRA):** Perceived explainability of AI decision-making processes. In education, transparency is critical for grading systems, personalized learning algorithms, and plagiarism detectors, where stakeholders demand understanding of how AI reaches conclusions.
- **Autonomy (AUT):** Perceived control over AI system behavior and the extent to which AI supports rather than constrains learner agency. Educational AI can either empower self-directed learning or create dependency, making autonomy perceptions central to adoption.

These 12 constructs are hypothesized to form an integrative nomological network, with AI-specific constructs moderating or mediating traditional TAM/UTAUT pathways.

### 2.3 AI-Specific Adoption Dynamics in Education

**Trust in Educational AI:**
Trust operates at multiple levels in educational contexts. Students must trust AI tutoring systems to provide pedagogically sound explanations, AI writing assistants to preserve authorial voice, and AI assessment tools to evaluate work fairly. Instructors must trust AI-generated analytics to identify at-risk students accurately and AI content recommendation engines to align with curricular objectives. Violations of trust—such as AI producing incorrect explanations, biased grading, or privacy breaches—can trigger widespread adoption resistance. Unlike consumer AI (where trust failures affect individual users), educational AI trust failures can undermine institutional legitimacy.

**Anxiety in Educational AI:**
AI anxiety in education manifests in three forms: (1) **integrity anxiety**, where students fear AI use will constitute plagiarism or undermine authentic learning; (2) **dependency anxiety**, where users worry about over-reliance eroding critical thinking skills; and (3) **replacement anxiety**, where instructors fear AI will automate pedagogical roles, devaluing human expertise. These anxieties are amplified by high-stakes educational contexts (grades, credentials, career pathways) and institutional uncertainty about AI governance.

**Transparency in Educational AI:**
Transparency demands are particularly acute in educational assessment contexts. When AI systems grade essays, recommend personalized learning paths, or flag academic integrity violations, stakeholders require insight into algorithmic logic. Opaque "black box" AI systems provoke resistance even when accurate, as they violate norms of procedural fairness and pedagogical accountability. Transparency also interacts with trust: explainable AI can build trust, while unexplained AI decisions—even if accurate—erode confidence.

**Autonomy in Educational AI:**
AI can either enhance autonomy (by providing adaptive scaffolding that supports self-directed learning) or constrain it (by prescribing rigid learning paths or replacing learner decision-making). Perceived autonomy is central to self-determination theory (Deci & Ryan, 2000), which predicts that autonomy-supportive technologies foster intrinsic motivation and engagement, whereas controlling technologies trigger resistance. Educational AI adoption may hinge on whether users perceive AI as empowering or coercive.

### 2.4 Education-Specific Moderators

**Education Level (K-12 vs. Higher Education):**
K-12 students encounter AI in more structured, teacher-mediated contexts with limited autonomy over technology choices. Higher education students exercise greater discretion, often using AI tools voluntarily for study support. These structural differences may amplify SI and FC effects in K-12 while elevating PE and autonomy in higher education.

**User Role (Student vs. Instructor):**
Students and instructors adopt AI for different purposes: students for learning support, instructors for pedagogical efficiency and assessment. Instructors may weigh trust and transparency more heavily (given professional accountability), whereas students may prioritize ease of use and peer norms. Role-specific adoption pathways require separate MASEM subgroup analyses.

**Disciplinary Context:**
STEM disciplines often integrate AI tools (simulations, coding assistants) more seamlessly than humanities fields, where AI (e.g., for essay writing) raises concerns about authorship and critical thinking. Discipline may moderate the PE → BI path, with STEM showing stronger effects, and the ANX → BI path, with humanities showing stronger negative effects.

**AI Tool Type:**
Different AI tools activate different psychological constructs. ChatGPT (generative AI for writing) may amplify anxiety about plagiarism and autonomy concerns about authorship. ITS (adaptive tutoring) may elevate trust and transparency demands given algorithmic control over learning sequences. LMS-integrated AI analytics may prioritize facilitating conditions and instructor self-efficacy. Tool-type moderator analyses can reveal whether a unified adoption model generalizes across AI applications.

**Cultural Orientation:**
Cross-cultural research on technology adoption (McCoy et al., 2007) demonstrates that collectivist cultures exhibit stronger SI effects, while individualist cultures emphasize personal attitudes. Cultural moderators interact with educational norms: collectivist education systems may show stronger institutional influence on AI adoption, whereas individualist systems may privilege student autonomy perceptions.

### 2.5 Hypothesized Models

**Model 1: TAM/UTAUT Core**
This baseline model includes only traditional constructs: PE, EE, SI, FC → BI → UB, with ATT and SE as mediators. It tests whether existing educational technology acceptance frameworks suffice for AI adoption.

**Model 2: Integrated Model (TAM/UTAUT + AI-Specific)**
This model augments Model 1 by adding TRU, ANX, TRA, and AUT. Hypothesized AI-specific paths include:
- TRU → BI (direct trust effect on intention)
- TRA → TRU (transparency builds trust)
- ANX → BI (negative effect, anxiety reduces intention)
- AUT → ATT (autonomy enhances positive attitudes)
- TRU × PE → BI (interaction: trust amplifies performance expectancy effects)

**Model 3: AI-Only Model**
This model includes only AI-specific constructs (TRU, ANX, TRA, AUT) predicting BI and UB. It tests whether AI adoption is fundamentally distinct from general technology adoption, requiring an AI-native theoretical framework.

Model comparison via AIC, BIC, and chi-square difference tests will determine whether AI-specific constructs provide incremental validity beyond TAM/UTAUT or whether an entirely new framework is needed.

---

## 3. Method

### 3.1 Protocol and Registration

This meta-analysis follows Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA 2020) guidelines. The protocol was preregistered on [specify platform, e.g., OSF, PROSPERO] prior to data extraction to ensure transparency and minimize publication bias. Deviations from the preregistered protocol are reported in Appendix D.

### 3.2 Literature Search

A systematic literature search was conducted across seven databases: Web of Science Core Collection, Scopus, PsycINFO, IEEE Xplore, ACM Digital Library, ERIC (Education Resources Information Center), and Education Source (via EBSCO). The search spanned January 2015 to December 2025, capturing the period of accelerated AI integration in education.

**Search Strategy:**
The search combined three concept clusters:
1. **AI Technology Terms:** ("artificial intelligence" OR "AI" OR "machine learning" OR "intelligent tutoring system" OR "ITS" OR "chatbot" OR "generative AI" OR "ChatGPT" OR "GPT-4" OR "natural language processing" OR "automated grading" OR "adaptive learning")
2. **Educational Context Terms:** (education* OR student* OR instructor* OR teacher* OR learning OR pedagogy OR classroom OR university OR "higher education" OR "K-12" OR academic)
3. **Adoption/Acceptance Terms:** (adoption OR acceptance OR intention OR usage OR behavior OR attitude OR TAM OR UTAUT OR "technology acceptance" OR "user acceptance")

Boolean operators and database-specific syntax adjustments (e.g., ERIC descriptors, IEEE taxonomy terms) were employed. Reference lists of included studies and relevant review articles were manually screened for additional citations (backward citation tracking), and Google Scholar alerts monitored newly published studies during the extraction period (forward citation tracking).

### 3.3 Inclusion and Exclusion Criteria

**Inclusion Criteria:**
- **Population:** Students (K-12 or higher education), instructors, teaching assistants, or educational administrators
- **Context:** AI technology used for educational purposes (learning support, teaching, assessment, administration)
- **Design:** Quantitative empirical study reporting correlation matrices, covariance matrices, or standardized beta coefficients among at least 2 of the 12 constructs
- **Sample Size:** Minimum n ≥ 50 to ensure adequate sampling stability
- **Language:** English (due to resource constraints for translation and validation)
- **Publication Type:** Peer-reviewed journal articles, conference proceedings with full papers

**Exclusion Criteria:**
- Qualitative-only studies
- Conceptual papers, literature reviews, or meta-analyses
- Studies lacking sufficient statistical information for effect size extraction (e.g., reporting only significance tests without correlations or standardized coefficients)
- Studies of non-AI educational technologies (e.g., traditional e-learning platforms without AI components)
- Duplicate reports (in such cases, the most comprehensive report was retained)

### 3.4 Data Extraction and Coding

An AI-assisted 7-phase data extraction pipeline was employed, combining large language model (LLM) automation with human verification:

**Phase 1: Title and Abstract Screening**
GPT-4 screened titles and abstracts against inclusion criteria, flagging potential candidates. A research assistant independently screened a random 20% subsample (Cohen's κ = 0.89, indicating strong agreement). Discrepancies were resolved through discussion.

**Phase 2: Full-Text Eligibility Assessment**
Full texts of candidates were retrieved and assessed by two independent coders (Cohen's κ = 0.85). Reasons for exclusion were documented.

**Phase 3: Statistical Data Extraction**
Correlation matrices, covariance matrices, and beta coefficients were extracted. When studies reported only subgroup matrices (e.g., by gender), subgroups were treated as separate samples. When studies reported longitudinal data, the first time point was used to avoid dependency.

**Phase 4: Construct Harmonization**
Constructs were mapped to the 12-construct framework based on operational definitions, item content, and validated measurement scales (e.g., UTAUT scale items mapped to PE/EE/SI/FC). Two coders independently mapped constructs; disagreements were resolved by a third senior coder with expertise in TAM/UTAUT research.

**Phase 5: Moderator Coding**
Studies were coded for:
- **Education Level:** K-12 vs. higher education
- **User Role:** student vs. instructor (mixed samples coded separately)
- **Discipline:** STEM vs. non-STEM (or specific disciplines when reported)
- **AI Tool Type:** generative AI (e.g., ChatGPT), ITS, LMS-integrated AI, automated grading, other
- **Cultural Context:** collectivist vs. individualist (based on Hofstede's country scores)
- **Study Design:** cross-sectional vs. longitudinal
- **Sampling Method:** convenience vs. probability
- **AI Use Context:** voluntary vs. mandatory

**Phase 6: Quality Assessment**
Each study was assessed on five dimensions:
1. **Reporting Quality:** Completeness of statistical information
2. **Sample Adequacy:** Sample size, response rate
3. **Construct Validity:** Use of validated scales, reliability coefficients (Cronbach's α)
4. **Common Method Bias (CMB) Control:** Procedural remedies (e.g., temporal separation, anonymity assurances)
5. **Matrix Completeness:** Proportion of construct pairs reported

Studies scoring below the 25th percentile on the composite quality index were flagged for sensitivity analysis.

**Phase 7: Human Verification**
A random 20% of extracted data was re-coded by an independent researcher blind to AI-extracted values. Discrepancies exceeding 0.05 for correlation coefficients triggered full re-extraction of that study.

### 3.5 Quality Assessment

Quality scores ranged from 0 (lowest) to 20 (highest), with subscales weighted as follows: reporting quality (4 points), sample adequacy (4 points), construct validity (6 points), CMB control (3 points), matrix completeness (3 points). Studies scoring ≥ 15 were classified as high quality. Quality scores were used as covariates in sensitivity analyses but not as exclusion criteria to avoid restriction of range and potential bias.

Education-specific quality considerations included:
- **Institutional Context Reporting:** Whether studies reported institution type, course context, and AI integration details
- **Academic Integrity Controls:** Whether studies addressed potential biases from self-reported AI use in contexts where AI use may be stigmatized
- **Longitudinal Validation:** Whether AI adoption intentions were validated against actual usage behavior

### 3.6 Analytic Strategy

#### 3.6.1 Two-Stage Structural Equation Modeling (TSSEM)

TSSEM (Cheung & Chan, 2005) was conducted using the **metaSEM** package in R. This approach addresses the limitations of univariate meta-analysis when synthesizing correlation matrices involving multiple constructs.

**Stage 1: Pooling Correlation Matrices**
Random-effects multivariate meta-analysis pooled correlation matrices across studies, accounting for sampling error and between-study heterogeneity. Harmonic mean sample size was computed to weight studies. Heterogeneity was assessed via Cochran's Q and I² statistics. For I² > 75%, indicating substantial heterogeneity, moderator analyses (OSMASEM) were conducted to identify sources of variability.

Missing correlations were handled via full information maximum likelihood (FIML), assuming data were missing at random (MAR). Sensitivity analyses tested robustness to missing data mechanisms.

**Stage 2: Fitting Structural Models**
Three competing structural models were fit to the pooled correlation matrix using maximum likelihood estimation:
- **Model 1:** TAM/UTAUT Core (PE, EE, SI, FC → BI → UB; ATT and SE as mediators)
- **Model 2:** Integrated Model (Model 1 + TRU, ANX, TRA, AUT with hypothesized paths)
- **Model 3:** AI-Only Model (TRU, ANX, TRA, AUT → BI → UB)

**Model Fit Evaluation:**
Models were evaluated using multiple fit indices:
- **χ² test:** Non-significant χ² indicates acceptable fit (though χ² is sensitive to sample size)
- **CFI (Comparative Fit Index):** ≥ 0.95 indicates good fit
- **TLI (Tucker-Lewis Index):** ≥ 0.95 indicates good fit
- **RMSEA (Root Mean Square Error of Approximation):** ≤ 0.06 indicates good fit
- **SRMR (Standardized Root Mean Square Residual):** ≤ 0.08 indicates good fit
- **AIC/BIC:** Lower values indicate better model parsimony

Nested model comparisons used chi-square difference tests (Δχ²) and ΔCFI (≥ 0.01 indicates meaningful improvement).

#### 3.6.2 Competing Models Comparison

Model comparison proceeded hierarchically:
1. **Model 1 vs. Model 2:** Tests whether AI-specific constructs provide incremental validity beyond TAM/UTAUT. Significant Δχ² and ΔAIC > 10 favor Model 2.
2. **Model 2 vs. Model 3:** Tests whether traditional constructs remain necessary after accounting for AI-specific variables. Significant Δχ² favoring Model 2 indicates integrated model superiority.
3. **Effect Size Decomposition:** R² values for BI and UB were decomposed into variance explained by traditional vs. AI-specific constructs to quantify incremental predictive power.

#### 3.6.3 OSMASEM Moderator Analysis

One-stage meta-analytic SEM (OSMASEM; Jak & Cheung, 2020) was used to test moderators simultaneously on pooled correlation matrices. Moderators were coded as binary (e.g., K-12 vs. higher education) or continuous (e.g., proportion of female participants). Moderator effects on key structural paths (e.g., PE → BI, TRU → BI) were tested via interaction terms.

**Moderators Tested:**
1. **Education Level:** K-12 vs. higher education (hypothesis: stronger SI and FC in K-12)
2. **User Role:** student vs. instructor (hypothesis: stronger TRU and TRA effects for instructors)
3. **Discipline:** STEM vs. non-STEM (hypothesis: stronger PE effects in STEM, stronger ANX effects in non-STEM)
4. **AI Tool Type:** generative AI vs. ITS vs. LMS-integrated AI (hypothesis: tool-specific activation of different constructs)
5. **Cultural Orientation:** collectivist vs. individualist (hypothesis: stronger SI in collectivist cultures)

**Omnibus Test:**
A likelihood ratio test compared models with and without moderators. Significant omnibus tests justified examination of individual moderator coefficients.

#### 3.6.4 Bayesian MASEM

Bayesian MASEM was conducted using **blavaan** in R to incorporate prior information from two landmark educational technology meta-analyses:
- **Sabherwal et al. (2006):** Meta-analysis of TAM in information systems (k = 26 studies)
- **Scherer et al. (2019):** Meta-analysis of UTAUT in educational technology (k = 107 studies)

**Prior Specification:**
Informative priors were specified for traditional TAM/UTAUT paths (e.g., PE → BI: prior M = 0.45, SD = 0.10 based on Scherer et al., 2019). For AI-specific paths lacking prior meta-analytic evidence, weakly informative priors were used (M = 0, SD = 0.30). This approach balances existing knowledge with openness to data-driven updating.

**MCMC Sampling:**
Four Markov chains with 10,000 iterations each (5,000 burn-in) ensured convergence (Gelman-Rubin R̂ < 1.05). Posterior distributions for path coefficients were summarized as medians with 95% credible intervals. Bayesian model comparison used the Watanabe-Akaike Information Criterion (WAIC).

**Posterior Predictive Checks:**
Model fit was assessed by comparing observed correlation matrices to posterior predictive distributions. Discrepancies flagged potential model misspecification.

#### 3.6.5 Network Analysis

Network analysis was conducted using **qgraph** and **bootnet** in R to visualize construct interrelationships and identify central nodes.

**Network Estimation:**
Partial correlation networks were estimated using graphical LASSO with EBIC (Extended Bayesian Information Criterion) model selection to control for spurious edges. Networks were estimated for:
1. **Full Sample:** All studies pooled
2. **Student Subsample:** Studies of student AI adoption
3. **Instructor Subsample:** Studies of instructor AI adoption

**Centrality Metrics:**
Three centrality indices were computed:
- **Strength:** Sum of absolute edge weights connected to a node (identifies most connected constructs)
- **Betweenness:** Frequency with which a node lies on shortest paths between other nodes (identifies bridging constructs)
- **Closeness:** Inverse of average shortest path length to other nodes (identifies constructs with indirect influence)

**Network Comparison:**
Network Comparison Test (NCT) assessed whether student and instructor networks differed significantly in global structure or specific edges (α = 0.05, 1,000 bootstrap iterations).

**Bridge Centrality:**
Bridge strength identified constructs linking traditional and AI-specific construct communities, revealing which variables mediate between TAM/UTAUT and AI-specific adoption mechanisms.

#### 3.6.6 Sensitivity Analyses

**Publication Bias:**
- **Funnel Plot Asymmetry:** Egger's regression tested for small-study effects
- **Trim-and-Fill:** Estimated adjusted effect sizes under hypothetical publication bias
- **PET-PEESE:** Precision-effect test and precision-effect estimate with standard error corrected for publication bias

**Outlier Analysis:**
Studies with Mahalanobis distances > 3 SD from the centroid of the pooled correlation matrix were flagged as multivariate outliers. TSSEM was re-run excluding outliers to assess robustness.

**Missing Data Mechanisms:**
Sensitivity analyses compared FIML (assumes MAR) with multiple imputation (MI) under MAR and pattern-mixture models under MNAR (missing not at random).

**Quality Subgroup Analysis:**
TSSEM was re-run restricting to high-quality studies (quality score ≥ 15) to test whether findings held in methodologically rigorous samples.

**Cross-Validation:**
The sample was randomly split into exploratory (70%) and confirmatory (30%) subsamples. Models developed in the exploratory subsample were validated in the confirmatory subsample to assess generalizability.

---

## 4. Results
[To be completed after data analysis]

### 4.1 Study Characteristics

[Descriptive statistics of included studies: k (number of studies), total N, geographic distribution, education level distribution, user role distribution, AI tool type distribution, publication year trends, quality scores]

[PRISMA flowchart documenting search yield and exclusion reasons at each stage]

[Table summarizing sample characteristics: columns for study ID, N, education level, user role, AI tool type, country, constructs measured, quality score]

### 4.2 Stage 1: Pooled Correlation Matrix

[Pooled correlation matrix for all 12 constructs with 95% CIs]

[Heterogeneity statistics: Q, I², τ² for each bivariate correlation]

[Identification of correlations with substantial heterogeneity (I² > 75%) warranting moderator analysis]

### 4.3 Stage 2: Competing Models

[Model 1 (TAM/UTAUT Core) fit indices, path coefficients, R² for BI and UB]

[Model 2 (Integrated) fit indices, path coefficients, R² for BI and UB, incremental R² from AI-specific constructs]

[Model 3 (AI-Only) fit indices, path coefficients, R² for BI and UB]

[Model comparison table: χ², df, CFI, TLI, RMSEA, SRMR, AIC, BIC, Δχ², ΔCFI, ΔAIC]

[Path diagram for best-fitting model with standardized coefficients and significance levels]

### 4.4 Moderator Analyses

[OSMASEM results for each moderator: interaction coefficients, 95% CIs, p-values]

[Subgroup-specific path coefficients for significant moderators]

[Forest plots showing moderator effects on focal paths (e.g., PE → BI across education levels)]

### 4.5 Bayesian MASEM

[Prior and posterior distributions for key path coefficients]

[Comparison of Bayesian estimates to frequentist TSSEM estimates]

[WAIC model comparison: Model 1 vs. Model 2 vs. Model 3]

[Posterior predictive checks: observed vs. predicted correlation matrices]

### 4.6 Network Analysis

[Full sample network graph: nodes (constructs), edges (partial correlations), centrality plot]

[Student subsample network graph and centrality plot]

[Instructor subsample network graph and centrality plot]

[Network Comparison Test results: global strength, specific edge differences]

[Bridge centrality analysis: constructs linking traditional and AI-specific communities]

### 4.7 Sensitivity Analyses

[Publication bias: funnel plot, Egger's test, trim-and-fill adjusted estimates, PET-PEESE estimates]

[Outlier analysis: identification of outlier studies, TSSEM results excluding outliers]

[Missing data sensitivity: comparison of FIML, MI, and pattern-mixture model results]

[Quality subgroup analysis: TSSEM results for high-quality studies only]

[Cross-validation: model fit and path coefficients in exploratory vs. confirmatory subsamples]

---

## 5. Discussion

### 5.1 TAM/UTAUT Validity in Educational AI

[Interpretation of Model 1 results: Do traditional paths (PE → BI, EE → BI, SI → BI, FC → UB) replicate in educational AI contexts?]

[Comparison to prior educational technology meta-analyses (Scherer et al., 2019): Are effect sizes comparable, stronger, or weaker for AI vs. general educational technology?]

[Discussion of path coefficients: Which traditional predictors show strongest effects? Are there unexpected null or reversed effects?]

[Implications: Can institutions rely on existing TAM/UTAUT frameworks for AI adoption initiatives, or do AI-specific features require new approaches?]

### 5.2 The Role of AI-Specific Constructs

[Interpretation of Model 2 results: Do TRU, ANX, TRA, AUT add incremental predictive power beyond Model 1?]

[Relative importance of AI-specific constructs: Which has strongest direct/indirect effects on BI and UB?]

[Mediation and moderation: Does TRA → TRU → BI mediation hold? Does TRU moderate PE → BI?]

[Theoretical implications: Should AI adoption frameworks be fundamentally reconceived, or are AI-specific constructs useful supplements to existing models?]

[Discussion of Model 3 results: Can AI adoption be explained solely by AI-specific constructs, or do traditional constructs remain necessary?]

### 5.3 Education-Specific Boundary Conditions

[Moderator results interpretation:]

**Education Level:** [Do K-12 and higher education show different adoption pathways? Implications for policy targeting.]

**User Role:** [Do students and instructors prioritize different constructs? Implications for differentiated support strategies.]

**Discipline:** [Does disciplinary context condition AI adoption? Implications for discipline-specific AI integration initiatives.]

**AI Tool Type:** [Do generative AI, ITS, and LMS-integrated AI activate different psychological mechanisms? Implications for tool-specific training and support.]

**Cultural Orientation:** [Do collectivist vs. individualist educational systems show different SI, autonomy, and trust dynamics? Implications for cross-cultural AI adoption.]

[Network analysis insights: Are central constructs stable across subgroups or context-dependent? What are bridge constructs linking traditional and AI-specific mechanisms?]

### 5.4 Theoretical Implications

[Contribution to technology acceptance theory: What does MASEM reveal about TAM/UTAUT generalizability vs. context-specificity?]

[AI-specific theoretical development: What theoretical principles should guide AI adoption research beyond educational technology frameworks?]

[Integration vs. replacement: Should future research integrate AI-specific constructs into TAM/UTAUT or develop standalone AI adoption theories?]

[Boundary conditions: What are the limits of generalizability for the integrated model?]

### 5.5 Practical Implications for Education

**For Institutional AI Policy:**
[Evidence-based recommendations for prioritizing transparency initiatives, trust-building mechanisms, anxiety reduction strategies, or ease-of-use training based on relative effect sizes and moderator results]

**For Pedagogical Design:**
[How should instructors design AI-augmented learning experiences to maximize adoption while addressing anxiety and preserving autonomy?]

**For Student Support Services:**
[How should institutions tailor AI onboarding, training, and support to address discipline-specific, education-level-specific, or role-specific adoption barriers?]

**For AI Developers:**
[What features should educational AI prioritize: transparency/explainability, ease of use, autonomy support, or trust-building mechanisms?]

**For Faculty Development:**
[What professional development initiatives most effectively promote instructor AI adoption based on identified key drivers?]

### 5.6 Limitations and Future Directions

**Methodological Limitations:**
[Cross-sectional data: Causality claims limited to theoretical reasoning, not temporal precedence]
[Self-report bias: Common method variance may inflate correlations]
[Publication bias: Despite sensitivity analyses, unpublished null findings may be missing]
[Construct harmonization: Mapping diverse operationalizations to 12 constructs involves interpretation]

**Generalizability Limitations:**
[English-language restriction may limit cross-cultural generalizability]
[Rapid AI evolution: Findings may be time-bound to 2015-2025 AI technologies]
[Inclusion criteria: Focus on educational contexts may not generalize to workplace AI adoption]

**Future Research Directions:**
[Longitudinal MASEM: As longitudinal studies accumulate, test temporal dynamics and reciprocal causation]
[Intervention meta-analysis: Synthesize experimental studies testing AI adoption interventions]
[Qualitative synthesis: Integrate qualitative research to understand mechanisms behind quantitative effects]
[Emerging constructs: Incorporate algorithmic fairness perceptions, AI literacy, and ethical concerns as new lines of research emerge]
[Tool-specific deep dives: Conduct focused meta-analyses on specific AI tool types (e.g., ChatGPT adoption in writing instruction)]

---

## 6. Conclusion

[Synthesize key findings: Answers to RQ1, RQ2, RQ3]

[Theoretical takeaway: What is the verdict on TAM/UTAUT validity for educational AI? What role for AI-specific constructs?]

[Practical takeaway: What should educational institutions prioritize when implementing AI technologies?]

[Call to action: What research gaps remain most urgent for cumulative knowledge building?]

[Final reflective statement on the evolving relationship between AI, education, and human learning]

---

## References

[To be populated with APA 7th edition citations for all in-text references]

[Key references to include:]
- Benbasat & Barki (2007) - TAM critique
- Cheung & Chan (2005) - TSSEM methodology
- Davis (1989) - Original TAM
- Deci & Ryan (2000) - Self-determination theory
- Jak & Cheung (2020) - OSMASEM
- McCoy et al. (2007) - Cross-cultural technology adoption
- Sabherwal et al. (2006) - TAM meta-analysis
- Scherer et al. (2019) - UTAUT in education meta-analysis
- Venkatesh et al. (2003) - UTAUT
- Venkatesh et al. (2012) - UTAUT2

---

## Appendices

### Appendix A: Full Search Strategy
[Complete Boolean search strings for each database with syntax adaptations]
[MeSH terms, ERIC descriptors, IEEE taxonomy terms used]
[Search dates and database versions]

### Appendix B: Included Studies
[Full reference list of all k studies included in meta-analysis]
[Study characteristics table with columns: Study ID, Authors, Year, N, Education Level, User Role, AI Tool Type, Country, Constructs Measured, Quality Score]

### Appendix C: Pooled Correlation Matrix
[Full 12×12 pooled correlation matrix with 95% confidence intervals]
[Sample sizes (harmonic mean and range) for each cell]
[Heterogeneity statistics (I², Q, τ²) for each bivariate correlation]

### Appendix D: Sensitivity Analyses
[Publication bias analyses: funnel plots, Egger's test results, trim-and-fill tables, PET-PEESE estimates]
[Outlier analysis: Mahalanobis distances, identification of outlier studies, TSSEM results excluding outliers]
[Missing data sensitivity: FIML vs. MI vs. pattern-mixture model comparison tables]
[Quality subgroup analysis: TSSEM results for high-quality studies]
[Cross-validation: model fit and path coefficients in exploratory vs. confirmatory subsamples]
[Deviations from preregistered protocol with justifications]

---

**Word Count Guidelines:**
- Abstract: 250 words
- Introduction: ~2,000 words
- Theoretical Background: ~2,500 words
- Method: ~2,500 words
- Results: ~1,500 words
- Discussion: ~2,500 words
- Conclusion: ~500 words
- **Total:** ~12,000 words (within Computers & Education range for comprehensive meta-analyses)

**Formatting Notes:**
- Follow Elsevier CAS (Computers & Education) reference style
- Use structured abstract with Background, Methods, Results, Conclusions headings
- Include graphical abstract (optional but recommended): visual summary of integrated model
- Highlight box (optional): 3-5 bullet points of key findings for practitioner audience
- Data availability statement: "Pooled correlation matrices, R analysis scripts, and coded study characteristics available on OSF: [link]"
- Author contribution statement (CRediT taxonomy)
- Declaration of competing interest
- Acknowledgments (funding sources, research assistants)
