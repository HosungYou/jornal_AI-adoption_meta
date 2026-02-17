# Master Integration Document — AI Adoption in Education MASEM

> Central coordination document for the AI Adoption in Education Meta-Analytic SEM journal article.
> All decisions, cross-references, and integration points are tracked here.
> Target Journal: **Computers & Education** (IF 12.0, Elsevier)

## Document Version History

| Version | Date | Changes |
|---------|------|---------|
| 0.1.0 | 2026-02-16 | Initial scaffolding (migrated from dissertation, education-focused) |

---

## 1. Project Overview

**Title**: AI Adoption in Education: A Meta-Analytic Structural Equation Model Integrating Trust, Anxiety, Transparency, and Autonomy

**Target Journal**: Computers & Education (Elsevier, IF 12.0)

**Scope**: Quantitative synthesis of empirical AI adoption studies in educational contexts (2015-2025) using MASEM to simultaneously test structural path models across pooled correlation matrices from ~40-80 primary studies involving students, instructors, and educational administrators.

**Companion Study**: Dissertation (organizational AI adoption) at `dissertation_AI-adoption_meta/`

---

## 2. Construct Registry (12 Standard Constructs)

| ID | Construct | Abbr | Role in Model | Education Interpretation |
|----|-----------|------|---------------|------------------------|
| 1 | Performance Expectancy | PE | Core predictor (TAM/UTAUT) | AI improves learning outcomes / teaching effectiveness |
| 2 | Effort Expectancy | EE | Core predictor (TAM/UTAUT) | Educational AI is easy to use and integrate |
| 3 | Social Influence | SI | Core predictor (UTAUT) | Peers/instructors encourage AI use in learning |
| 4 | Facilitating Conditions | FC | Core predictor (UTAUT) | Institution provides AI tools and training |
| 5 | Behavioral Intention | BI | Core mediator | Intention to adopt AI for academic purposes |
| 6 | Use Behavior | UB | Core outcome | Actual use of AI in learning/teaching |
| 7 | Attitude | ATT | Mediator (TAM) | Overall evaluation of educational AI |
| 8 | Self-Efficacy | SE | Antecedent | Confidence in using AI for academic tasks |
| 9 | AI Trust | TRU | AI-specific predictor | Trust in AI accuracy for educational content |
| 10 | AI Anxiety | ANX | AI-specific predictor | Academic integrity anxiety, AI over-reliance fear |
| 11 | AI Transparency | TRA | AI-specific antecedent | AI grading fairness, explainability |
| 12 | Perceived AI Autonomy | AUT | AI-specific antecedent | AI decision independence in educational contexts |

---

## 3. Education-Specific Moderators

| Moderator | Type | Categories | Rationale |
|-----------|------|------------|-----------|
| Education Level | Categorical | K-12, undergraduate, graduate, mixed | Adoption patterns differ by maturity |
| User Role | Categorical | student, instructor, administrator, mixed | Different adoption drivers |
| Discipline | Categorical | STEM, humanities, social_science, health_science, mixed | AI relevance varies by field |
| AI Tool Type | Categorical | chatbot_LLM, ITS, LMS_AI, auto_grading, writing_assistant, adaptive_learning, general | Tool-specific adoption |
| Institutional Type | Categorical | public, private, online, community_college, mixed | Resource availability differs |
| Culture (Hofstede) | Continuous | 0-100 individualism score | Cross-cultural comparison |
| Temporal Period | Binary | pre_chatgpt (2015-2022), post_chatgpt (2023-2025) | Generative AI era effect |

---

## 4. Analysis Module Cross-Reference

| Module | R Script | Input Data | Output | Dependencies |
|--------|----------|-----------|--------|-------------|
| Data Prep | `01_data_preparation.R` | `data/02_verified/` | Cleaned matrices | None |
| Stage 1 Pooling | `02_stage1_pooling.R` | Cleaned matrices | `data/03_pooled/` | Module 1 |
| Stage 2 SEM | `03_stage2_sem.R` | Pooled matrix | Path coefficients | Module 2 |
| Competing Models | `04_competing_models.R` | Pooled matrix | Model comparison | Module 2 |
| OSMASEM | `05_osmasem_moderators.R` | Raw matrices + moderators | Moderation effects | Module 1 |
| Temporal | `06_temporal_analysis.R` | Raw matrices + years | Pre/post comparison | Module 1 |
| Mediation | `07_mediation.R` | Pooled matrix | Indirect effects | Module 2 |
| Heterogeneity | `08_heterogeneity.R` | Raw correlations | I², tau², PI | Module 1 |
| Pub Bias | `09_publication_bias.R` | Raw correlations | Bias diagnostics | Module 1 |
| Sensitivity | `10_sensitivity.R` | r-only + r+beta datasets | Robustness check | Module 1 |
| Bayesian MASEM | `11_bayesian_masem.R` | Pooled matrix + priors | Posteriors, BF | Module 2 |
| Network | `12_network_analysis.R` | Pooled matrix | Network metrics | Module 2 |
| Visualization | `13_visualization.R` | All outputs | Figures | All modules |

---

## 5. Key Decision Log

| Date | Decision | Rationale | Reference |
|------|----------|-----------|-----------|
| 2026-02-16 | Education-only scope (separate from dissertation) | Different adoption dynamics in education vs. organizations; different target journals | Migration Plan v1 |
| 2026-02-16 | 12 constructs (not 8 or 16) | Balance between comprehensiveness and data availability | Plan v1 |
| 2026-02-16 | Include beta-to-r conversion | Many AI studies report only beta; Peterson & Brown (2005) conversion is standard | Plan v1 |
| 2026-02-16 | 3-model comparison approach | Tests TAM/UTAUT validity, integrated model, and AI-only model | Plan v1 |
| 2026-02-16 | Sabherwal + Scherer priors for Bayesian | Compare general IT priors with education-specific priors | Plan v1 |
| 2026-02-16 | MAGNA network analysis with education subgroups | Triangulation with student vs. instructor subgroup networks | Plan v1 |
| 2026-02-16 | Add ERIC and Education Source databases | Essential for education-specific systematic search | Plan v1 |
| 2026-02-16 | Target Computers & Education (IF 12.0) | Top education technology journal, ideal for MASEM methodology | Plan v1 |

---

## 6. Data Flow

```
PDFs → Phase 0 (RAG Index)
     → Phase 1 (AI Extraction) → Phase 2 (Construct Mapping)
     → Phase 3 (3-Model Consensus) → Phase 4 (ICR Sampling)
     → Phase 5 (Human Resolution) → Phase 6 (QA Final)
     → data/04_final/ → R Analysis Pipeline
```

---

## 7. Quality Gates

| Gate | Criterion | Script |
|------|-----------|--------|
| G1 | All correlation matrices are positive definite | `01_data_preparation.R` |
| G2 | kappa >= .85 for categorical, ICC >= .95 for numerical | `phase4_sampling_icr.py` |
| G3 | TSSEM Stage 1 converges | `02_stage1_pooling.R` |
| G4 | All competing models converge | `04_competing_models.R` |
| G5 | MCMC chains converge (R-hat < 1.01) | `11_bayesian_masem.R` |
| G6 | Network stability CS > 0.50 | `12_network_analysis.R` |

---

## 8. Manuscript Mapping (Computers & Education Format)

| Manuscript Section | Data Source | Script |
|-------------------|------------|--------|
| Table 1: Study characteristics | `data/04_final/` | -- |
| Table 2: Pooled correlation matrix | `data/03_pooled/` | `02_stage1_pooling.R` |
| Table 3: Path coefficients (3 models) | `analysis/output/path_coefficients/` | `03_stage2_sem.R` |
| Table 4: Model comparison (fit indices) | `analysis/output/model_comparison/` | `04_competing_models.R` |
| Table 5: Education moderator results | `analysis/output/` | `05_osmasem_moderators.R` |
| Table 6: Bayesian posterior summaries | `analysis/output/bayesian_posteriors/` | `11_bayesian_masem.R` |
| Figure 1: PRISMA flow diagram | `supplementary/prisma/` | `generate_prisma.py` |
| Figure 2: Path diagram (best-fit model) | `figures/output/` | `13_visualization.R` |
| Figure 3: Forest plots (key paths) | `figures/output/` | `13_visualization.R` |
| Figure 4: Bayesian posteriors | `analysis/output/bayesian_posteriors/` | `11_bayesian_masem.R` |
| Figure 5: Network graph (full + subgroups) | `analysis/output/network_graphs/` | `12_network_analysis.R` |

---

## 9. Differentiation from Dissertation

| Aspect | Dissertation (Org) | Journal Article (Edu) |
|--------|-------------------|----------------------|
| Repo | `dissertation_AI-adoption_meta` | `jornal_AI-adoption_meta` |
| Population | Employees, managers, consumers | Students, instructors, administrators |
| Context | Workplace, multi-industry | K-12, higher education |
| Moderators | Industry, AI type, culture, temporal | Education level, user role, discipline, AI tool, institutional type |
| Expected k | 80-150 | 40-80 |
| Databases | WoS, Scopus, PsycINFO, IEEE, ACM | WoS, Scopus, PsycINFO, IEEE, ACM, **ERIC**, **Education Source** |
| Bayesian Priors | Sabherwal et al. (2006) | Sabherwal + **Scherer et al. (2019)** |
| Network Subgroups | Cross-industry | Student vs. instructor, K-12 vs. HE |
| Target Venue | Dissertation defense | Computers & Education |
| Format | Dissertation chapters | Journal article (~8,000-10,000 words) |

---

## 10. Key References

- Cheung, M. W.-L. (2015). *Meta-analytic structural equation modeling*. Wiley.
- Sabherwal, R., Jeyaraj, A., & Chowa, C. (2006). Information system success. *Management Science*, 52(12), 1849-1864.
- Scherer, R., Siddiq, F., & Tondeur, J. (2019). The technology acceptance model (TAM): A meta-analytic structural equation modeling approach to explaining teachers' adoption of digital technology in education. *Computers & Education*, 128, 13-35.
- Peterson, R. A., & Brown, S. P. (2005). On the use of beta coefficients in meta-analysis. *Journal of Applied Psychology*, 90(1), 175-181.
- Venkatesh, V., Morris, M. G., Davis, G. B., & Davis, F. D. (2003). User acceptance of information technology. *MIS Quarterly*, 27(3), 425-478.
