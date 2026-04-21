# Paper A: Proposal Brief

## Title

**AI Adoption in Higher Education: A Meta-Analytic Structural Equation Modeling Approach Integrating Traditional Acceptance Factors and AI-Specific Psychological Constructs**

## Author

Hosung You, College of Education, Pennsylvania State University

## Status

Proposal Brief for Journal Venue Selection | April 2026

---

## Abstract

This study employs meta-analytic structural equation modeling (MASEM) to synthesize the structural relationships among 10 latent constructs driving artificial intelligence (AI) adoption in higher education. Drawing from a corpus of 224 empirical studies (2015-2025) identified through systematic search of four databases (Web of Science, Scopus, PsycINFO, IEEE Xplore; initial yield: 22,166 records), the study integrates traditional technology acceptance constructs (Performance Expectancy, Effort Expectancy, Social Influence, Facilitating Conditions, Attitude, Self-Efficacy, Behavioral Intention, Use Behavior) with AI-specific psychological factors (Trust in AI, AI Anxiety). The primary structural model follows a TRA/TPB-TAM mediation architecture in which Performance Expectancy and Effort Expectancy influence Behavioral Intention through Attitude, while Trust and Anxiety operate as AI-specific enablers and inhibitors, respectively. The analytical approach employs Cheung's (2015) two-stage MASEM (TSSEM) for the primary analysis, supplemented by one-stage MASEM (OSMASEM; Jak & Cheung, 2020) for continuous moderator testing (publication year, cultural individualism). Expected contributions include: (a) the first MASEM of AI adoption in higher education integrating both traditional acceptance factors and AI-specific constructs, (b) empirical adjudication between competing theoretical architectures, and (c) evidence-based recommendations for institutional AI adoption strategy.

**Keywords:** meta-analytic structural equation modeling, artificial intelligence adoption, higher education, technology acceptance, trust in AI, AI anxiety, UTAUT, Theory of Reasoned Action

---

## Introduction and Problem Statement

The rapid proliferation of artificial intelligence (AI) tools in higher education, including large language models (e.g., ChatGPT, Claude), intelligent tutoring systems, AI-powered writing assistants, and automated assessment platforms, has created urgent demand for theoretically grounded understanding of adoption determinants. Technology acceptance research has generated a substantial body of empirical findings, yet this literature remains fragmented across competing theoretical frameworks (TAM, UTAUT, TPB, UTAUT2) and isolated by study-level designs that cannot simultaneously test the full network of structural relationships.

Meta-analytic structural equation modeling (MASEM; Cheung, 2015; Viswesvaran & Ones, 1995) addresses this fragmentation by pooling inter-construct correlation matrices across studies and fitting structural models to the pooled matrix. While MASEM has been applied to general technology acceptance (Scherer et al., 2019; Blut et al., 2022), no published MASEM focuses specifically on AI adoption in higher education, integrating both traditional acceptance factors and the AI-specific psychological constructs (Trust in AI, AI Anxiety) that primary researchers have consistently judged important enough to measure.

### Research Gap

Three gaps motivate this study:

1. Existing meta-analyses of technology acceptance (e.g., Blut et al., 2022; Scherer et al., 2019) predate the generative AI era and do not include AI-specific constructs.
2. No MASEM has integrated Trust in AI and AI Anxiety alongside traditional UTAUT constructs in a single structural model, despite consistent empirical evidence that these constructs predict adoption intention above and beyond Performance Expectancy and Effort Expectancy.
3. The structural role of Attitude (ATT) in AI adoption remains contested: UTAUT (Venkatesh et al., 2003) dropped ATT on parsimony grounds, yet 36.2% of the AI adoption corpus (k = 81 studies) retains it, suggesting that evaluative judgment plays a more prominent role when technologies are perceived as autonomous agents.

---

## Theoretical Framework

### Theory Development Pathway

The structural model synthesizes five decades of behavioral intention theory:

```
TRA (1975) --> TAM (1989) --> TPB (1991) --> C-TAM-TPB (1995) --> UTAUT (2003) --> Model A (current)
```

- **Theory of Reasoned Action** (TRA; Fishbein & Ajzen, 1975): Behavioral beliefs form attitudes, which combine with subjective norms to predict behavioral intention.
- **Technology Acceptance Model** (TAM; Davis, 1989): Operationalizes TRA for IT adoption; PE and EE as core belief antecedents of Attitude.
- **Theory of Planned Behavior** (TPB; Ajzen, 1991): Extends TRA with Perceived Behavioral Control (later decomposed into SE and FC).
- **Combined TAM-TPB** (Taylor & Todd, 1995): Decomposes PBC into Self-Efficacy, Facilitating Conditions, and Computer Anxiety.
- **UTAUT** (Venkatesh et al., 2003): Synthesizes eight prior models; drops ATT on parsimony grounds.
- **Model A** (present study): Reinstates ATT as mediator based on AI-specific phenomenology (Scherer et al., 2019); adds Trust and Anxiety.

### AI-Specific Extensions

Two Tier 2 constructs extend the model beyond traditional technology acceptance:

- **Trust in AI (TRU)**: Relational disposition required when users delegate cognitive judgment to an autonomous agent (Glikson & Woolley, 2020; Siau & Wang, 2018). Not reducible to Performance Expectancy (relational vs. instrumental belief).
- **AI Anxiety (ANX)**: Existential threat appraisals unique to AI systems: job displacement, loss of agency, cognitive replacement (Wang & Wang, 2022). Not reducible to low Self-Efficacy (threat appraisal vs. capability belief).

### 10-Construct Structural Model

| Construct | Abbr. | k | Primary Theory | Structural Position |
|-----------|-------|---|----------------|---------------------|
| Performance Expectancy | PE | 186 | TAM/UTAUT | Exogenous -> ATT |
| Effort Expectancy | EE | 162 | TAM/UTAUT | Exogenous -> ATT, PE |
| Social Influence | SI | 114 | UTAUT/TPB | Exogenous -> BI |
| Facilitating Conditions | FC | 105 | UTAUT | Exogenous -> UB |
| Attitude | ATT | 81 | TAM/TPB | Endogenous (mediator) |
| Self-Efficacy | SE | 44 | SCT | Exogenous -> BI |
| AI Anxiety | ANX | 40 | AI-specific | Exogenous -> ATT, BI (inhibitory) |
| Trust in AI | TRU | 36 | AI-specific | Exogenous -> BI |
| Behavioral Intention | BI | 185 | TRA/TAM/UTAUT | Endogenous (primary DV) |
| Use Behavior | UB | 90 | TAM/UTAUT | Endogenous (ultimate outcome) |

*Note.* k = number of studies operationalizing the construct. Tier 1 (k >= 44) spans multiple theoretical traditions. Tier 2 (ANX, TRU) are AI-specific extensions.

### Primary Structural Paths

```
PE --> ATT --> BI --> UB
EE --> ATT
EE --> PE
SI --> BI
SE --> BI
TRU --> BI
ANX --> ATT (negative)
ANX --> BI (negative)
FC --> UB
```

---

## Research Questions

**RQ1:** To what extent do the TAM/UTAUT structural paths (PE -> ATT -> BI; EE -> ATT; SI -> BI; FC -> UB) hold in the meta-analytic pooled correlation matrix of AI adoption in higher education?

**RQ2:** Do AI-specific constructs (Trust in AI, AI Anxiety) provide statistically significant incremental explanatory power in Behavioral Intention (BI) beyond traditional acceptance factors (PE, EE, SI, ATT, SE)?

**RQ3:** Does Attitude (ATT) function as a significant mediator of the PE/EE -> BI relationship, or is the direct PE/EE -> BI path sufficient (as UTAUT claims)?

**RQ4:** How do publication year (pre/post-2023 generative AI era), cultural individualism (Hofstede IDV), education level (undergraduate vs. graduate), and AI tool type (LLM vs. non-LLM) moderate the structural relationships?

---

## Method

### Literature Search and Screening

- **Databases**: Web of Science, Scopus, PsycINFO (ProQuest), IEEE Xplore
- **Initial yield**: 22,166 records
- **After deduplication**: 16,189
- **After three-tier screening**: 224 studies included
- **Screening method**: AI-assisted (Gemini 2.5-Flash + Claude Sonnet 4.6) with human verification

### Inclusion Criteria

1. AI technology adoption/acceptance/use in higher education
2. Quantitative SEM/path analysis/regression with >= 2 constructs from the 10-construct model
3. Reports correlation matrix, Fornell-Larcker table, HTMT, or sufficient statistics
4. Samples: undergraduate, graduate students, or faculty/instructors
5. Published 2015-2025

### Data Extraction

- Hybrid AI-human pipeline: 3 LLMs (Claude, Gemini, Codex) + 4 human coders
- Multi-model consensus with human adjudication for divergent cases
- 20% stratified ICR verification (target kappa >= .85)

### Analytic Strategy

1. **Stage 1 (TSSEM)**: Pool study-level correlations into 10 x 10 positive-definite matrix (multivariate random-effects, FIML)
2. **Stage 2 (TSSEM)**: Fit structural model to pooled matrix via WLS
3. **Moderator analysis (OSMASEM)**: Study-level covariates as Level 2 predictors
4. **Model comparison**: Competing specifications via AIC and chi-square difference
5. **Sensitivity**: beta-to-r exclusion, ridge correction, leave-one-out

---

## Expected Contributions

1. **Theoretical**: First MASEM integrating TAM/UTAUT + AI-specific constructs (Trust, Anxiety) for higher education. Empirically adjudicates ATT's mediating role.
2. **Methodological**: Demonstrates inductive-deductive construct selection in MASEM; provides reproducible AI-assisted pipeline for large-scale meta-analysis.
3. **Practical**: Evidence-based recommendations for institutional AI strategy differentiated by user role, AI tool type, and cultural context.

---

## Target Audience and Venue Characteristics

Ideal venues should:
- Accept quantitative meta-analyses with structural equation modeling
- Have readership including educational technology researchers and practitioners
- Publish on AI/technology adoption in educational contexts
- Accept papers of 8,000-12,000 words (method-heavy, with supplementary materials)
- Impact Factor >= 4.0 preferred
- Turnaround: initial decision within 60-90 days

### Suggested Search Terms for Venue Identification

- "meta-analysis AND (technology acceptance OR technology adoption) AND education"
- "MASEM OR meta-analytic structural equation modeling"
- "artificial intelligence AND higher education AND acceptance"
- "UTAUT OR TAM AND meta-analysis"
- "trust AND AI AND adoption"

---

## Key Numbers at a Glance

| Parameter | Value |
|-----------|-------|
| Total corpus | N = 224 studies (2015-2025) |
| Initial search yield | 22,166 records from 4 databases |
| Constructs in model | 10 (8 Tier 1 + 2 AI-specific) |
| Off-diagonal cells | 45 (43 with k >= 10; 2 sparse) |
| Primary method | TSSEM (Cheung, 2015) |
| Secondary method | OSMASEM (Jak & Cheung, 2020) |
| Moderators tested | 4 (year, culture, education level, AI tool type) |
| Expected word count | 8,000-12,000 |
| Human coders | 4 (two independent pairs) |
| AI models used | 3 (Claude, Gemini, Codex) |

---

## References

Ajzen, I. (1991). The theory of planned behavior. *Organizational Behavior and Human Decision Processes, 50*(2), 179-211.

Blut, M., Chong, A., Tsiga, Z., & Venkatesh, V. (2022). Meta-analysis of the unified theory of acceptance and use of technology (UTAUT). *Journal of the Association for Information Systems, 23*(1), 13-95.

Cheung, M. W.-L. (2015). *Meta-analysis: A structural equation modeling approach*. Wiley.

Davis, F. D. (1989). Perceived usefulness, perceived ease of use, and user acceptance of information technology. *MIS Quarterly, 13*(3), 319-340.

Fishbein, M., & Ajzen, I. (1975). *Belief, attitude, intention and behavior: An introduction to theory and research*. Addison-Wesley.

Glikson, E., & Woolley, A. W. (2020). Human trust in artificial intelligence: Review of empirical research. *Academy of Management Annals, 14*(2), 627-660.

Jak, S., & Cheung, M. W.-L. (2020). Meta-analytic structural equation modeling with moderating effects on SEM parameters. *Psychological Methods, 25*(4), 430-449.

Scherer, R., Siddiq, F., & Tondeur, J. (2019). The technology acceptance model (TAM): A meta-analytic structural equation modeling approach. *Computers & Education, 128*, 13-35.

Venkatesh, V., Morris, M. G., Davis, G. B., & Davis, F. D. (2003). User acceptance of information technology: Toward a unified view. *MIS Quarterly, 27*(3), 425-478.

Viswesvaran, C., & Ones, D. S. (1995). Theory testing: Combining psychometric meta-analysis and structural equations modeling. *Personnel Psychology, 48*(4), 865-885.

Wang, X., & Wang, J. (2022). AI anxiety: Measuring fear of artificial intelligence. *Information Technology & People*. Advance online publication.
