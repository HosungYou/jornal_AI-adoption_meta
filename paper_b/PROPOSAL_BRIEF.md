# Paper B: Proposal Brief

## Title

**LLM-Assisted Data Extraction for Meta-Analytic Structural Equation Modeling: A Multi-Model Comparative Framework with Human Gold-Standard Validation**

## Author

Hosung You, College of Education, Pennsylvania State University

## Status

Proposal Brief for Journal Venue Selection | April 2026

---

## Abstract

Data extraction remains the most time-intensive and error-prone phase of systematic reviews and meta-analyses. This study evaluates the accuracy, reliability, and cost-effectiveness of large language model (LLM)-assisted data extraction for meta-analytic structural equation modeling (MASEM), a methodologically demanding synthesis technique requiring extraction of full inter-construct correlation matrices from primary studies. Using a 100-study gold-standard subsample from a parent meta-analysis of AI adoption in higher education (N = 224 studies), three LLM models (Claude Sonnet 4.6, Gemini 2.5-Flash, Codex) independently extract four categories of data: bibliographic metadata, correlation matrices, construct operationalizations, and moderator variables (approximately 30 data elements per study; 3,000 total). Extraction accuracy is evaluated against a human gold standard produced by four independent coders (two pairs with cross-pair adjudication; target kappa >= .85). The study tests whether multi-model consensus (majority voting across three LLMs) outperforms single-model extraction and identifies the optimal human-AI hybrid workflow that maximizes accuracy while minimizing researcher time investment. Reporting follows PRISMA-trAIce (2025) and TRIPOD-LLM guidelines.

**Keywords:** large language models, data extraction, meta-analysis, systematic review methodology, inter-rater reliability, automation, MASEM, correlation matrix extraction, multi-model consensus

---

## Introduction and Problem Statement

Systematic reviews and meta-analyses are foundational to evidence-based practice, yet their production is bottlenecked by manual data extraction, which accounts for approximately 30-60% of total researcher time (Borah et al., 2017). In meta-analytic structural equation modeling (MASEM), the extraction burden is amplified: rather than extracting a single effect size per study, MASEM requires the full inter-construct correlation matrix (often 10-20 pairwise correlations per study), along with construct operationalization details, sample sizes, and reliability coefficients. For a 200-study MASEM with 10 constructs, this implies approximately 6,000 individual data elements to be located, verified, and coded.

The emergence of large language models (LLMs) with extended context windows (100K-1M tokens) and multimodal capabilities (PDF/table parsing) offers a potential solution. Several recent studies have explored LLM-assisted extraction for standard meta-analyses (e.g., Wang et al., 2024; Khraisha et al., 2024), but none has evaluated LLM performance on the methodologically demanding task of correlation matrix extraction for MASEM, which requires:

1. Identifying the correct correlation table format (Pearson, Fornell-Larcker, HTMT)
2. Mapping study-specific construct labels to standardized constructs
3. Distinguishing latent correlations from observed correlations
4. Handling PLS-SEM studies that report only square-root AVE on the diagonal

### Research Gap

No published study has:
- Compared multiple LLMs head-to-head on MASEM-specific extraction tasks
- Evaluated multi-model consensus as an error-reduction strategy for correlation matrix extraction
- Established benchmarks for LLM accuracy by data type (bibliographic vs. statistical vs. classificatory)

---

## Research Questions

**RQ1:** What is the extraction accuracy of each LLM model (Claude, Gemini, Codex) for MASEM-specific data elements, compared to the human gold standard? (Element-level precision, recall, F1)

**RQ2:** Does extraction accuracy vary by data type: bibliographic metadata (title, year, sample size) vs. statistical data (correlations, reliability) vs. classificatory data (construct mapping, moderator coding)?

**RQ3:** Does multi-model consensus (3-model majority voting) produce higher accuracy than any single model alone? What is the optimal consensus threshold?

**RQ4:** What is the optimal human-AI hybrid workflow that achieves >= 95% accuracy while minimizing researcher time? (Full AI, AI + spot-check, AI + full verify)

---

## Method

### Study Design

Comparative accuracy study evaluating three LLM models against a human gold standard on a 100-study stratified subsample from the parent meta-analysis corpus (N = 224). Fully crossed design: all three LLMs and all four human coders process the same 100 studies.

### Sampling

100 studies selected via stratified random sampling from the 224-study corpus:
- Stratification variables: publication year (pre-2023 vs. post-2023), AI tool type (LLM vs. non-LLM), methodology (PLS-SEM vs. CB-SEM), journal type (education vs. IS)
- Ensures representation of methodological diversity relevant to extraction difficulty

### Gold Standard Construction

| Component | Detail |
|-----------|--------|
| Human coders | 4 (R1, R2, R3, R4) |
| Pairing | Pair A: R1 + R2 (50 studies); Pair B: R3 + R4 (50 studies) |
| Independence | Blinded within pairs |
| ICR metric | Cohen's kappa (categorical); ICC(2,1) (continuous) |
| ICR target | kappa >= .85 |
| Adjudication | Cross-pair: R1 adjudicates Pair B; R3 adjudicates Pair A |
| Final standard | Consensus values for all 3,000 data elements |

### LLM Extraction Pipeline

Three models process each PDF independently:
- **Claude Sonnet 4.6** (Anthropic): 200K context window
- **Gemini 2.5-Flash** (Google): 1M context window
- **Codex** (OpenAI): Extended context

Extraction modules:
| Module | Content | Elements/Study |
|--------|---------|----------------|
| A | Bibliographic metadata (title, year, N, country, etc.) | ~8 |
| B | Correlation matrix extraction (Pearson, F-L, HTMT) | ~10-15 |
| C | Construct operationalization (scale source, items, reliability) | ~5 |
| D | Moderator variables (education level, AI tool type, setting) | ~5 |

### Multi-Model Consensus Algorithm

```
For each data element:
  if 3/3 models agree     --> adopt (high confidence)
  if 2/3 models agree     --> adopt (majority confidence)
  if 3-way disagreement   --> flag for human adjudication
```

### Analysis Plan

| Metric | Application |
|--------|-------------|
| Precision, Recall, F1 | Element-level accuracy (categorical) |
| Mean Absolute Error | Correlation accuracy (continuous) |
| Proportion within +/- .02 | Correlation tolerance band |
| McNemar's test | Paired comparison between models |
| Cohen's d, Odds Ratios | Effect sizes for all comparisons |
| Cost per element | Dollar cost and time cost |

---

## Expected Contributions

1. **Methodological**: First empirical benchmark for LLM accuracy on MASEM-specific extraction tasks. Reproducible framework for evaluating AI extraction tools in any quantitative synthesis context.

2. **Practical**: Identifies the optimal human-AI hybrid workflow for MASEM data extraction. Expected time reduction: 60-80% compared to fully manual extraction at >= 95% accuracy.

3. **Reporting Standards**: Demonstrates PRISMA-trAIce (2025) and TRIPOD-LLM compliance for transparent reporting of AI-assisted evidence synthesis.

---

## Relationship to Paper A

| Dimension | Paper A | Paper B |
|-----------|---------|---------|
| Focus | MASEM substantive findings | LLM methodology validation |
| Corpus | Full 224 studies | 100-study subsample |
| Primary outcome | Structural path coefficients | Extraction accuracy metrics |
| Theoretical base | TAM/UTAUT/TRA | Information extraction, NLP |
| Target audience | EdTech / IS researchers | Research methods / meta-analysis community |

Paper B can be submitted independently (cites Paper A as OSF preprint).

---

## Target Audience and Venue Characteristics

Ideal venues should:
- Publish methodological innovations in systematic review / meta-analysis
- Have readership conducting quantitative evidence synthesis
- Be open to AI/LLM applications in research methodology
- Accept papers of 6,000-10,000 words with technical detail
- Impact Factor >= 3.0 preferred
- Value reproducibility and open-science reporting
- Have published on automation, NLP, or ML in systematic reviews

### Suggested Search Terms for Venue Identification

- "systematic review AND (automation OR machine learning OR NLP) AND data extraction"
- "meta-analysis AND (large language model OR LLM OR GPT OR AI)"
- "research synthesis methods AND technology"
- "inter-rater reliability AND automated coding"
- "PRISMA AND artificial intelligence"

---

## Key Numbers at a Glance

| Parameter | Value |
|-----------|-------|
| Gold standard sample | 100 studies (stratified from N = 224) |
| Human coders | 4 (two independent pairs) |
| LLM models tested | 3 (Claude Sonnet 4.6, Gemini 2.5-Flash, Codex) |
| Data elements per study | ~30 |
| Total data elements | ~3,000 |
| ICR target | Cohen's kappa >= .85 |
| Accuracy target | >= 95% element-level |
| Extraction modules | 4 (bibliographic, correlation, construct, moderator) |
| Reporting standards | PRISMA-trAIce (2025), TRIPOD-LLM |
| Expected word count | 6,000-10,000 |

---

## References

Borah, R., Brown, A. W., Capers, P. L., & Allison, D. B. (2017). Analysis of the time and workers needed to conduct systematic reviews. *BMJ Open, 7*(2), e012545.

Cheung, M. W.-L. (2015). *Meta-analysis: A structural equation modeling approach*. Wiley.

Collins, G. S., et al. (2025). TRIPOD-LLM: Transparent reporting of LLM-assisted prediction model development. *BMJ*.

Jak, S., & Cheung, M. W.-L. (2020). Meta-analytic structural equation modeling with moderating effects on SEM parameters. *Psychological Methods, 25*(4), 430-449.

Khraisha, Q., et al. (2024). Can large language models replace humans in systematic reviews? *arXiv preprint*.

Marshall, I. J., & Wallace, B. C. (2019). Toward systematic review automation. *Systematic Reviews, 8*, 163.

Page, M. J., et al. (2021). The PRISMA 2020 statement. *BMJ, 372*, n71.

Tsafnat, G., et al. (2014). Systematic review automation technologies. *Systematic Reviews, 3*, 74.

Viswesvaran, C., & Ones, D. S. (1995). Theory testing: Combining psychometric meta-analysis and structural equations modeling. *Personnel Psychology, 48*(4), 865-885.

Wang, S., et al. (2024). GPT-4 for systematic review screening. *Journal of Medical Internet Research, 26*, e52758.
