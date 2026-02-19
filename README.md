# AI Adoption in Education: A Meta-Analytic Structural Equation Model Integrating Trust, Anxiety, Transparency, and Autonomy

> A comprehensive meta-analytic structural equation modeling study synthesizing AI adoption research in educational contexts to test the validity of TAM/UTAUT frameworks for educational AI technologies.

**Target Journal:** *Computers & Education* (Impact Factor: 12.0, Elsevier)

## Research Questions

1. **RQ1**: To what extent do TAM/UTAUT path relationships hold in the educational AI adoption context? (TSSEM on 12-construct model)
2. **RQ2**: Do AI-specific constructs (Trust, Anxiety, Transparency, Autonomy) provide incremental explanatory power beyond traditional TAM/UTAUT variables in educational settings? (Competing models comparison)
3. **RQ3**: How do educational contextual factors (education level, user role, discipline, AI tool type, institutional type, cultural context, temporal period) moderate the structural relationships? (OSMASEM + subgroup analysis)

## Theoretical Framework

Extended 12-construct model integrating TAM, UTAUT, and AI-specific variables:

| # | Construct | Abbr | Origin |
|---|-----------|------|--------|
| 1 | Performance Expectancy | PE | TAM/UTAUT |
| 2 | Effort Expectancy | EE | TAM/UTAUT |
| 3 | Social Influence | SI | UTAUT |
| 4 | Facilitating Conditions | FC | UTAUT |
| 5 | Behavioral Intention | BI | TAM/UTAUT |
| 6 | Use Behavior | UB | TAM/UTAUT |
| 7 | Attitude | ATT | TAM |
| 8 | Self-Efficacy | SE | SCT |
| 9 | AI Trust | TRU | AI-specific |
| 10 | AI Anxiety | ANX | AI-specific |
| 11 | AI Transparency | TRA | AI-specific |
| 12 | Perceived AI Autonomy | AUT | AI-specific |

→ **66 pairwise correlations** pooled across studies

## Analysis Suite (10 Modules)

| # | Analysis | Script | Contribution |
|---|----------|--------|-------------|
| 1 | TSSEM (Two-Stage SEM) | `02-03` | Pooled correlation → structural model |
| 2 | Competing Models | `04` | TAM vs Integrated vs AI-Only |
| 3 | OSMASEM + Continuous Moderators | `05` | Publication year, Hofstede scores |
| 4 | Pre/Post ChatGPT Temporal | `06` | Path changes around 2023 |
| 5 | Meta-Analytic Mediation | `07` | Indirect effects (TRA→TRU→BI) |
| 6 | Heterogeneity Decomposition | `08` | I², τ², prediction intervals |
| 7 | Publication Bias | `09` | Trim-fill, PET-PEESE, selection models |
| 8 | Sensitivity (r-only vs r+β) | `10` | β→r conversion robustness |
| 9 | Bayesian MASEM | `11` | Sabherwal et al. informative priors |
| 10 | Network Analysis (MAGNA) | `12` | Construct centrality, bridge analysis |

## Methodology

- **Population**: Students (K-12, undergraduate, graduate), instructors, educational administrators
- **Context**: AI in teaching, learning, and educational administration (ChatGPT, intelligent tutoring systems, LMS-AI, automated grading, AI writing assistants)
- **Effect size**: Pearson correlations (r), with β→r conversion (Peterson & Brown, 2005) and sensitivity analysis
- **Core method**: Two-Stage Meta-Analytic SEM (TSSEM; Cheung, 2015) via `metaSEM` R package
- **Advanced**: One-Stage MASEM (OSMASEM), Bayesian MASEM (`blavaan`), Network Analysis (`psychonetrics`)
- **AI-assisted screening**: Codex CLI + Gemini CLI (dual-provider OAuth); AI-assisted coding: 3-model consensus pipeline
- **Expected studies**: k = 40-80 studies, N > 10,000 participants (initial); actual pipeline yielded k ≈ 150-220 candidates
- **Actual screening**: 16,189 records screened (3-tier AI pipeline); 256 include, 175 conflict, 1,776 uncertain (Gemini retry pending)

## Repository Structure

```
data/
├── 01_raw/                  # Original database exports (WoS, Scopus, PsycINFO, IEEE)
├── 02_processed/            # Merged & deduplicated master (16,189 records)
├── 03_screening/            # AI screening results + human review queue
│   ├── screening_ai_dual.csv       # Full 16,189-record screening log
│   ├── human_review_queue.csv      # 571 records for human review
│   └── logs/                       # Extraction & processing logs
├── 04_included/             # Final included studies (after human review)
├── 05_coding/               # AI-extracted correlations (7-phase pipeline)
├── 06_pooled/               # Pooled correlation & asymptotic covariance matrices
├── 07_final/                # MASEM-ready dataset + data provenance
└── templates/               # Coding & screening workbook templates

scripts/
├── screening/               # 3-tier AI screening (Codex + Gemini) + retry logic
└── ai_coding_pipeline/      # 7-phase correlation extraction pipeline

analysis/
├── R/                       # 13 MASEM analysis scripts (TSSEM, OSMASEM, Bayesian)
└── Python/                  # Data cleaning, matrix validation, reporting

docs/
├── 01_protocol/             # Pre-registration & search strategy
├── 02_screening/            # Tiered screening protocol
├── 03_extraction/           # Coding manual & construct crosswalk
└── 04_analysis/             # Statistical analysis documentation

supplementary/               # PRISMA checklist, codebook, risk of bias
configs/                     # Model specs, Bayesian priors, network parameters
```

## Screening and Coding Authority

- Tiered screening protocol: `docs/02_screening/TIERED_SCREENING_PROTOCOL.md`
- Screening data (16,189 records): `data/03_screening/screening_ai_dual.csv`
- Human review queue (571 records): `data/03_screening/human_review_queue.csv`
- Operational coding template: `data/templates/AI_Adoption_MASEM_Coding_v1.xlsx`
- Title/abstract AI assistance: Codex CLI (gpt-5.1-codex-mini → gpt-5.3-codex-spark) + Gemini CLI (gemini-2.5-flash)
- Final screening decisions: Two independent human coders + PI adjudication

## Current Pipeline Status

| Stage | Status | Count |
|-------|--------|-------|
| Database search | ✅ Complete | 16,189 records |
| AI screening (T1-T3) | ✅ Complete | 16,189 records |
| Gemini retry 1 | ✅ Complete | 2,669 recovered |
| Codex retry 2 | ✅ Complete | 245/250 recovered |
| Gemini retry 2 | ✅ Complete | 1,215/1,633 recovered |
| Human review | 🔄 In progress | 1,093 records |
| Full-text retrieval | ⏸ Next phase | ~299+ studies |
| Data extraction | ⏸ Next phase | AI pipeline ready |

**AI Screening Final Consensus (post all retries)**

| Consensus | Count |
|-----------|-------|
| Exclude | 14,408 |
| Include | 299 |
| Conflict (→ human adjudication) | 175 |
| Uncertain — Gemini failed (residual) | 685 |
| Uncertain — Genuine (→ human review) | 619 |

## Key References

- Cheung, M. W.-L. (2015). *Meta-analytic structural equation modeling*. Wiley.
- Scherer, R., Siddiq, F., & Tondeur, J. (2019). The technology acceptance model (TAM): A meta-analytic structural equation modeling approach to explaining teachers' adoption of digital technology in education. *Computers & Education*, 128, 13-35.
- Sabherwal, R., Jeyaraj, A., & Chowa, C. (2006). Information system success: Individual and organizational determinants. *Management Science*, 52(12), 1849–1864.
- Peterson, R. A., & Brown, S. P. (2005). On the use of beta coefficients in meta-analysis. *Journal of Applied Psychology*, 90(1), 175–181.

## License

This work is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

## Author

Hosung You — Journal Article Research
