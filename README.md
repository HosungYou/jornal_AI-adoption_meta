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
- **AI-assisted coding**: 7-Phase pipeline (Claude + GPT-4o + Groq consensus) with 20% human verification
- **Expected studies**: k = 40-80 studies, N > 10,000 participants

## Repository Structure

```
├── data/                   # Raw → extracted → verified → pooled → final
├── analysis/
│   ├── R/                  # 13 analysis scripts (00-13)
│   └── Python/             # Data cleaning, validation, reporting
├── docs/                   # Literature search → extraction → methodology
├── scripts/
│   ├── ai_coding_pipeline/ # 7-Phase AI extraction pipeline
│   ├── screening/          # Study screening tools
│   └── data_processing/    # Template creation, validation
├── supplementary/          # Codebook, PRISMA, protocol, construct mapping
├── configs/                # Model specs, Bayesian priors, network params
├── manuscript/             # Current draft, versions, figures, tables
└── figures/                # Source and output figures
```

## Key References

- Cheung, M. W.-L. (2015). *Meta-analytic structural equation modeling*. Wiley.
- Scherer, R., Siddiq, F., & Tondeur, J. (2019). The technology acceptance model (TAM): A meta-analytic structural equation modeling approach to explaining teachers' adoption of digital technology in education. *Computers & Education*, 128, 13-35.
- Sabherwal, R., Jeyaraj, A., & Chowa, C. (2006). Information system success: Individual and organizational determinants. *Management Science*, 52(12), 1849–1864.
- Peterson, R. A., & Brown, S. P. (2005). On the use of beta coefficients in meta-analysis. *Journal of Applied Psychology*, 90(1), 175–181.

## License

This work is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

## Author

Hosung You — Journal Article Research
