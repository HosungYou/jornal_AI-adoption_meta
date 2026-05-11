# AI Adoption in Education: A Meta-Analytic Structural Equation Model

> Meta-Analytic Structural Equation Modeling (MASEM) of AI adoption in higher education, integrating traditional technology acceptance constructs with AI-specific psychological factors.

**Phase 1 Status:** Complete (N = 224 studies included)

## Research Questions

1. **RQ1**: To what extent do TAM/UTAUT path relationships hold in the higher education AI adoption context?
2. **RQ2**: Do AI-specific constructs (Trust in AI, AI Anxiety) provide incremental explanatory power beyond traditional TAM/UTAUT variables?
3. **RQ3**: How do educational contextual factors (education level, user role, AI tool type, culture) moderate the structural relationships?

## Structural Model (Model A)

Model A integrates TRA/TPB attitude-mediation architecture with UTAUT construct operationalizations and AI-specific extensions:

```
PE/EE → ATT → BI → UB
SI/SE/TRU → BI
ANX → ATT / BI (inhibitory)
FC → UB (direct)
```

See `docs/04_methodology/model_specification.md` for competing model specifications.

## 10 Constructs

| # | Construct | Abbr | k | Origin | Tier |
|---|-----------|------|---|--------|------|
| 1 | Performance Expectancy | PE | 186 | TAM/UTAUT | 1 |
| 2 | Behavioral Intention | BI | 185 | TAM/UTAUT/TPB | 1 |
| 3 | Effort Expectancy | EE | 162 | TAM/UTAUT | 1 |
| 4 | Social Influence | SI | 114 | UTAUT/TPB | 1 |
| 5 | Facilitating Conditions | FC | 105 | UTAUT | 1 |
| 6 | Use Behavior | UB | 90 | TAM/UTAUT | 1 |
| 7 | Attitude | ATT | 81 | TAM/TPB | 1 |
| 8 | Self-Efficacy | SE | 44 | SCT | 1 |
| 9 | AI Anxiety | ANX | 40 | AI-specific | 2 |
| 10 | Trust in AI | TRU | 36 | AI-specific | 2 |

> Constructs excluded on methodological grounds: HM (coverage failure), HAB (structural inconsistency), PV (near-zero variance), TRA/AUT (k < 3). See `docs/03_data_extraction/construct_selection_rationale.md`.

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
├── 04_extraction/                 # Step 4: Data extraction + Paper B/C validation workspaces
│   └── 07_paper_c_harness_benchmark/ # Paper C H-C-L harness benchmark scaffold
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

paper_a/                           # Paper A: MASEM meta-analysis (target TBD)
paper_b/                           # Paper B: LLM extraction methodology (target TBD)
paper_c/                           # Paper C: Codex vs Codex+LongTable harness benchmark

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
| 1. Identification | ✅ Complete | `data/01_identification/` | 16,189 unique records |
| 2. Screening | ✅ Complete | `data/02_screening/` | 224 studies included |
| 3. Full-text/Eligibility | ✅ Complete | `data/02_screening/pdfs/` | 224 PDFs obtained |
| 4. Data Extraction | 🔄 In progress | `data/04_extraction/` | Coding manual finalized, Phase 0 calibration done |
| 5. Analysis | ⏸ Pending | `analysis/` | TSSEM + OSMASEM pipeline ready |

## Methodology

- **Core method**: Two-Stage Meta-Analytic SEM (TSSEM; Cheung, 2015) via `metaSEM` R package
- **AI-assisted screening**: Gemini CLI + Claude Sonnet 4.6 (2-model consensus)
- **Construct model**: 10-construct (8 Tier 1 + 2 AI-specific Tier 2), derived inductively from 224-study full-text analysis
- **Theoretical architecture**: TRA/TPB mediation (PE/EE → ATT → BI) + AI-specific extensions (ANX, TRU)
- **Effect size**: Pearson r (with beta-to-r conversion sensitivity analysis)
- **Advanced**: OSMASEM for continuous moderators, Bayesian MASEM with Sabherwal et al. (2006) priors

## Key Documents

| Document | Location |
|----------|----------|
| Model specification (4 models) | `docs/04_methodology/model_specification.md` |
| Preregistration protocol | `supplementary/protocol/preregistration_protocol.md` |
| Decision log | `docs/06_decisions/decision_log.md` |
| Paper C harness benchmark specification | `paper_c/RESEARCH_SPECIFICATION.md` |
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
