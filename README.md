# AI Adoption in Education: A Meta-Analytic Structural Equation Model

> Comparing four competing structural models (TAM/UTAUT Core, Integrated, AI-Only, Trust Dual-Mechanism) of AI adoption in educational contexts using MASEM.

**Target Journal:** *Computers & Education* (Impact Factor: 12.0, Elsevier)

## Research Questions

1. **RQ1**: To what extent do TAM/UTAUT path relationships hold in the educational AI adoption context?
2. **RQ2**: Do AI-specific constructs (Trust, Anxiety, Transparency, Autonomy) provide incremental explanatory power beyond traditional TAM/UTAUT variables?
3. **RQ3**: How do educational contextual factors moderate the structural relationships?

## Four Competing Models

| Model | Name | Paths | Key Question |
|-------|------|-------|-------------|
| M1 | TAM/UTAUT Core | 8 | Is AI "just another technology"? |
| M2 | Integrated | 14 | Do AI-specific constructs add value? |
| M3 | AI-Only | 7 | Can AI-specific constructs stand alone? |
| M4 | Trust Dual-Mechanism | 16 | Does Trust mediate through ATT and ANX? |

> Model 4 adds TRU→ATT (Reliance proxy) and TRU→ANX (Resistance proxy) to test Trust's dual mediation mechanism. See `docs/04_methodology/model_specification.md`.

## 12 Constructs

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

## Repository Structure (PRISMA-aligned)

```
data/                              # PRISMA 2020 data flow
├── 01_identification/             # Step 1: Database search + deduplication
│   ├── search_results/            #   Raw exports (WoS, Scopus, PsycINFO, IEEE)
│   ├── merged_all_databases.csv   #   22,166 merged records
│   ├── deduplicated_16189.csv     #   16,189 after dedup
│   └── dedup_report.txt           #   Deduplication log
├── 02_screening/                  # Step 2: Title/abstract screening
│   ├── screening_ai_dual.csv      #   16,189 AI screening decisions
│   ├── human_review_queue.csv     #   1,457 records for human review
│   └── screening_pilot_100.csv    #   Pilot screening sample
├── 03_eligibility/                # Step 3: Full-text eligibility (TBD)
├── 04_extraction/                 # Step 4: Data extraction (TBD)
├── 05_analysis/                   # Step 5: Pooled matrices + final data (TBD)
└── templates/                     # Coding templates + archived versions

docs/                              # Documentation (numbered by PRISMA stage)
├── 01_literature_search/          # Search strategy, database coverage
├── 02_screening/                  # Screening protocols, inclusion criteria
├── 03_data_extraction/            # Coding manual, construct harmonization
├── 04_methodology/                # MASEM methods, 4-model specification
├── 05_manuscript/                 # Writing timeline
├── 06_decisions/                  # Decision log, implementation plans
└── discussion/                    # Research discussion records (Korean)

paper_a/                           # Paper A: MASEM meta-analysis (C&E)
paper_b/                           # Paper B: LLM extraction methodology (RSM)

analysis/R/                        # 14 MASEM analysis scripts
analysis/Python/                   # Data cleaning, validation utilities
scripts/screening/                 # AI screening pipeline + retries
scripts/ai_coding_pipeline/        # 7-phase extraction pipeline
scripts/data_processing/           # PRISMA generation, template creation
scripts/figure_generation/         # Path diagrams, forest plots

configs/                           # Model specs (YAML), Bayesian priors, network params
supplementary/                     # PRISMA checklist, codebook, preregistration
tests/                             # Test suite for screening/processing scripts
```

## Current Pipeline Status

| PRISMA Stage | Status | Data Location | Count |
|-------------|--------|---------------|-------|
| 1. Identification | ✅ Complete | `data/01_identification/` | 16,189 records |
| 2. Screening | 🔄 Human review in progress | `data/02_screening/` | 575 include, 175 conflict, 714 uncertain |
| 3. Eligibility | ⏸ Next phase | — | ~575+ full-text |
| 4. Extraction | ⏸ Pending | — | AI pipeline ready |
| 5. Analysis | ⏸ Pending | — | 4 competing models specified |

## Methodology

- **Core method**: Two-Stage Meta-Analytic SEM (TSSEM; Cheung, 2015) via `metaSEM` R package
- **AI-assisted screening**: Gemini CLI + Claude Sonnet 4.6 (2-model consensus)
- **Competing models**: Approach B (pre-registered model comparison) with 4 models
- **Effect size**: Pearson r (with β→r conversion sensitivity analysis)
- **Advanced**: OSMASEM, Bayesian MASEM, Network Analysis (MAGNA)

## Key Documents

| Document | Location |
|----------|----------|
| Model specification (4 models) | `docs/04_methodology/model_specification.md` |
| Preregistration protocol | `supplementary/protocol/preregistration_protocol.md` |
| Decision log | `docs/06_decisions/decision_log.md` |
| Screening protocol | `docs/02_screening/TIERED_SCREENING_PROTOCOL.md` |
| Coding manual | `docs/03_data_extraction/coding_manual.md` |

## Key References

- Cheung, M. W.-L. (2015). *Meta-analytic structural equation modeling*. Wiley.
- Scherer, R., Siddiq, F., & Tondeur, J. (2019). *Computers & Education*, 128, 13-35.
- Sabherwal, R., Jeyaraj, A., & Chowa, C. (2006). *Management Science*, 52(12), 1849-1864.

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

## Author

Hosung You — Penn State College of Education
