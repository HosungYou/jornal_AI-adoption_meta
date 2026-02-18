# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [0.2.1] - 2026-02-18

### Overview
Full-scale AI-assisted screening of 16,189 records using a three-tier acceleration strategy. Tier 1 keyword pre-filter eliminates 12,915 obviously irrelevant records in <1 second; Tier 2 sends 613 partial-match records to Gemini CLI only; Tier 3 sends 2,557 strong-match records through dual Codex+Gemini screening with asyncio parallelism (8 workers). Expected total runtime: ~3 hours vs ~147 hours for naive sequential processing (~50x speedup).

### Added — Scripts

| File | Purpose |
|------|---------|
| `scripts/screening/ai_screening_tiered.py` | Three-tier accelerated screening: T1 keyword auto-exclude, T2 single-AI (Gemini), T3 dual-AI (Codex+Gemini) with asyncio concurrency |
| `scripts/screening/ai_screening_parallel.py` | Asyncio-based parallel dual-AI screening (predecessor to tiered approach) |
| `scripts/screening/postprocess_t1_codes.py` | Post-processor to upgrade T1 exclude codes from generic E2 to specific reasons (E2:no_ai_terms, E2+E3:ai_no_edu_no_adopt) |

### Added — Documentation

| File | Description |
|------|-------------|
| `docs/screening/TIERED_SCREENING_PROTOCOL.md` | Complete protocol documenting 3-tier classification logic, keyword patterns, pilot validation (0 false negatives), and PRISMA 2020 reporting guidance |

### Changed — Source Code

| File | Change |
|------|--------|
| `scripts/screening/ai_screening.py` | Fix: config path now uses `Path(__file__).resolve()` instead of relative path (cwd-independent) |

### Changed — Data Artifacts

| File | Change |
|------|--------|
| `data/01_extracted/screening_pilot_100.csv` | Reprocessed 3 Codex timeout records → all exclude; conflicts reduced 8→5, agreement 92.3%→95.2% |

### Three-Tier Screening Strategy

```
16,189 deduplicated records
  ├── T1 Keyword Pre-filter (12,915 = 79.8%)  →  auto-exclude  [<1 sec]
  │     No AI-related terms in title/abstract/keywords
  ├── T2 Single AI — Gemini (613 = 3.8%)      →  Gemini only   [~25 min]
  │     AI terms + partial match (education OR adoption, not both)
  └── T3 Dual AI — Codex+Gemini (2,557 = 15.8%) → both engines [~3 hrs]
        AI terms + education + adoption (strongest candidates)
```

**Pilot validation:** 104-record pilot confirmed 0 false negatives from T1 keyword filter. All 8 pilot includes correctly routed to T3.

## [0.2.0] - 2026-02-17

### Overview
Implements the complete 2-XLSX screening and coding pipeline for the AI Adoption in Education MASEM study. This release establishes the operational infrastructure for processing 16,189 candidate records through dual-AI (Codex CLI + Gemini CLI) title/abstract screening, human adjudication, and extraction of included studies (k = 40–80) into a structured coding workbook. A 100-record stratified pilot validates the end-to-end workflow.

### Added — Scripts

| File | Purpose |
|------|---------|
| `scripts/screening/create_screening_workbook.py` | Generates the 1st XLSX (Screening Workbook) from the deduplicated CSV; 4 sheets (SCREENING, CODEBOOK, EXCLUSION_LOG, SEARCH_LOG) with dropdown validations and pre-filled search log |
| `scripts/screening/merge_ai_to_xlsx.py` | Merges AI screening CSV outputs into the 1st XLSX by `record_id`; resume-safe (does not overwrite existing values), non-destructive (human-coder columns untouched) |
| `scripts/screening/export_included_to_coding.py` | Extracts `adjudicated_final_decision == "include"` records from the 1st XLSX and generates the 2nd XLSX (Coding Workbook) with pre-filled STUDY_METADATA; reuses `create_masem_template.py` infrastructure (9 sheets) |
| `scripts/screening/extract_pilot_sample.py` | Stratified random sampling from the screening master CSV, preserving `source_database` proportions |
| `scripts/generate_synthetic_master.py` | Generates synthetic bibliographic data (16,189 records) for pipeline development and testing |

### Added — Test Suite

| File | Tests | Coverage |
|------|:-----:|----------|
| `tests/conftest.py` | — | Common fixtures (`sample_screening_csv`, `sample_ai_results_csv`) |
| `tests/test_ai_screening.py` | 22 | JSON parsing (clean, codeblock, mixed, empty, no-json), `normalize_decision`, `consensus`, `prepare_record_id`, `build_prompt` |
| `tests/test_create_screening_workbook.py` | 6 | Sheet presence, row count, column order, dropdown validations, SEARCH_LOG prefill, CODEBOOK population |
| `tests/test_dedup_merge.py` | 8 | DOI exact dedup, fuzzy title dedup (≥0.90 threshold), schema validation, database merge with lineage tracking |
| `tests/test_generate_prisma.py` | 10 | PRISMA counts, Codex/Gemini exclude tallies, 3-format output generation, exclusion code enumeration |
| `tests/test_merge_ai_to_xlsx.py` | 5 | AI column population, human column preservation, no-overwrite semantics, missing ID handling |

**Result: 51 tests, all passing (0.29 s)**

### Added — Data Artifacts

| File | Description |
|------|-------------|
| `data/processed/screening_master_16189_20260217.csv` | Deduplicated screening master (16,189 records, 15 columns) |
| `data/processed/dedup_report_20260217.txt` | Deduplication report: 22,166 → 16,189 (27.0% removal rate) |
| `data/processed/pilot_100_sample.csv` | 100-record stratified pilot sample |
| `data/templates/AI_Adoption_Screening_v1.xlsx` | Full 1st XLSX Screening Workbook (16,189 records, 28 columns, 11 dropdown validations) |
| `data/templates/AI_Adoption_Screening_pilot_100.xlsx` | Pilot 1st XLSX with AI screening decisions merged |
| `data/templates/AI_Adoption_MASEM_Coding_pilot_test.xlsx` | Pilot 2nd XLSX with 15 included studies pre-filled in STUDY_METADATA |
| `data/01_extracted/screening_pilot_100.csv` | Simulated dual-AI screening results for pilot |
| `data/01_extracted/prisma_pilot.json` | PRISMA 2020 flow counts (JSON) |
| `data/01_extracted/prisma_pilot.txt` | PRISMA 2020 flow summary (plain text) |
| `data/01_extracted/prisma_pilot.csv` | PRISMA 2020 flow data (tabular) |

### Added — Documentation

| File | Change |
|------|--------|
| `docs/06_decisions/implementation_plan_codex_gemini_screening.md` | New: Codex + Gemini OAuth screening implementation plan with Section 10 (Two-XLSX Workflow Architecture) |

### Changed — Documentation

| File | Change |
|------|--------|
| `docs/search_strategy/SEARCH_EXECUTION_GUIDE.md` | Scope narrowed from 7 databases to 4 (WoS, Scopus, PsycINFO, IEEE); ACM, ERIC, Education Source sections removed |
| `docs/06_decisions/decision_log.md` | Decision #50 added: 4-DB scope confirmation + 2-XLSX workflow adoption rationale |
| `README.md` | Added `data/processed/` to repository structure; screening workbook reference; updated AI-assisted methodology description |
| `docs/README.md` | Updated `01_literature_search/` description to 4-DB set; added `search_strategy/` row |

### Changed — Source Code

| File | Change |
|------|--------|
| `scripts/screening/ai_screening.py` | Bugfix: escaped `{}`/`}}` in `SCREENING_PROMPT` JSON template to prevent `KeyError` on `.format()` call |
| `scripts/ai_coding_pipeline/config.yaml` | Gemini CLI block added under `screening_cli` (OAuth auth, version/auth/screen commands) |

### Architecture Decision: Two-XLSX Workflow (Decision #50)

```
DOCX (canonical protocol — AI_Adoption_MASEM_Coding_Manual_v1.docx)
  ├── 1st XLSX: Screening Workbook (16,189 records)
  │     ├── AI pre-screening (Codex CLI + Gemini CLI, OAuth)
  │     ├── Human Coder 1 + Coder 2 (100% of records)
  │     └── PI adjudication → final include/exclude
  └── 2nd XLSX: Coding Workbook (k = 40–80 included studies)
        ├── STUDY_METADATA (pre-filled from screening)
        ├── CORRELATION_MATRIX (66 pairwise correlations)
        ├── CONSTRUCT_MAPPING (12 constructs)
        └── MODERATOR_VARIABLES + AI_EXTRACTION_PROVENANCE
```

### Database Scope Decision (Decision #50)

- **Confirmed:** WoS, Scopus, PsycINFO, IEEE (4 databases)
- **Excluded:** ACM (heavy overlap with IEEE), ERIC and Education Source (add volume but minimal unique quantitative SEM/TAM/UTAUT studies)
- **Rationale:** 4-DB set provides >95% recall for the target population; reduces dedup burden without sacrificing coverage

## [0.1.0] - 2026-02-16

### Added
- Initial repository setup: migrated from dissertation (organizational) to journal article (educational) focus
- Target journal: Computers & Education (IF 12.0, Elsevier)
- Complete directory structure for education-focused AI adoption MASEM
- Education-specific moderators: education level, user role, discipline, AI tool type, institutional type
- ERIC and Education Source added to database search strategy
- Scherer et al. (2019) education-specific Bayesian priors alongside Sabherwal et al. (2006)
- Education-focused construct operationalizations (PE as learning outcomes, ANX as academic integrity concerns, etc.)
- Journal article manuscript skeleton (Abstract, Introduction, Method, Results, Discussion)
- 13 R analysis script skeletons adapted for education moderators
- 7-Phase AI coding pipeline adapted for educational AI studies
- Comprehensive coding manual with education-specific moderator coding
- Construct harmonization guide with education-specific variant labels
- Methodology documentation (MASEM, Bayesian with education priors, Network Analysis with student/instructor subgroups)
- Configuration files for competing models, education-adapted Bayesian priors, network parameters
- Supplementary materials (preregistration, PRISMA, codebook, construct crosswalk) for education scope
- Education-specific quality flags (student convenience sampling, single-institution bias)

### Changed (from dissertation base)
- Population: employees/workers → students, instructors, educational administrators
- Context: organizational/workplace → educational settings (K-12, higher education)
- Moderators: industry sector → education level, user role, discipline, AI tool type, institutional type
- Databases: Added ERIC, Education Source
- Expected k: 80-150 → 40-80 studies (education-specific scope)
- Bayesian priors: Added Scherer et al. (2019) teacher TAM meta-analysis
- Network subgroups: cross-industry → student vs. instructor, K-12 vs. higher ed
- Manuscript format: dissertation chapters → journal article (C&E format)
