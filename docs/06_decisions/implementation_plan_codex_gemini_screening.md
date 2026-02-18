# Implementation Plan: Codex + Gemini OAuth Screening

## 1. Purpose
- Execute large-scale study screening for educational AI adoption MASEM with procedural legitimacy and methodological validity.
- Enforce canonical governance: screening/coding rules are anchored in
  `docs/03_data_extraction/AI_Adoption_MASEM_Coding_Manual_v1.docx`.

## 2. Canonical Authority
- Source of truth (SOT): `docs/03_data_extraction/AI_Adoption_MASEM_Coding_Manual_v1.docx`
- Operational mirrors:
  - `docs/02_study_selection/inclusion_exclusion_criteria.md`
  - `docs/02_study_selection/screening_protocol.md`
  - `docs/03_data_extraction/coding_manual.md`
- Operational template:
  - `data/templates/AI_Adoption_MASEM_Coding_v1.xlsx`

## 3. Decision Lock (Final)
- AI pre-screening: Codex CLI + Gemini CLI using OAuth-authenticated sessions.
- Human coding: two independent human coders for 100% of records.
- Human mode: AI suggestions visible during human coding (non-blinded).
- Final decision: PI adjudicates unresolved human conflicts.
- IRR thresholds:
  - Title/Abstract: Cohen's kappa >= 0.80
  - Full-text: Cohen's kappa >= 0.85
- Exclusion coding: canonical E1-E12 system with required rationale text.

## 4. Data Contract
- Core screening fields required in template/dataset:
  - `screen_decision_codex`
  - `screen_decision_gemini`
  - `screen_consensus`
  - `human1_decision`
  - `human2_decision`
  - `adjudicated_final_decision`
  - `exclude_code`
  - `decision_rationale`
  - `adjudicator_id`
  - `screen_run_id`
  - `oauth_auth_method_codex`
  - `oauth_auth_method_gemini`

## 5. Execution Workflow
1. Ingest and deduplicate merged database results.
2. Run Codex and Gemini title/abstract screening independently.
3. Assign AI consensus bucket:
   - `include`
   - `exclude` (candidate only)
   - `conflict`
4. Human coder 1 and coder 2 independently code all records.
5. Resolve disagreements by PI adjudication.
6. Lock final exclusion codes + rationale.
7. Generate PRISMA counts from adjudicated final decisions.

## 6. CLI/OAuth Preflight
```bash
codex --login
codex exec "Say OK."

gemini auth login
gemini -p "Say OK."
```

## 7. Core Commands

### 7.1 Deduplication
```bash
python3 scripts/screening/dedup_merge.py \
  --inputs data/00_raw/search_results/wos.csv data/00_raw/search_results/scopus.csv \
  --names WoS Scopus \
  --output data/00_raw/search_results/deduplicated_records.csv \
  --report data/00_raw/search_results/dedup_report.txt
```

### 7.2 Dual AI Screening
```bash
python3 scripts/screening/ai_screening.py \
  data/00_raw/search_results/deduplicated_records.csv \
  data/01_extracted/screening_ai_dual.csv \
  --engine both \
  --auto-login \
  --save-every 50 \
  --resume
```

### 7.3 PRISMA Snapshot
```bash
python3 scripts/data_processing/generate_prisma.py \
  --screening-csv data/01_extracted/screening_ai_dual.csv \
  --identified-total 16189 \
  --duplicates-removed 0 \
  --output-prefix supplementary/prisma/prisma_flow_input
```

## 8. Required Outputs
- Screening dataset with AI + human + adjudication fields.
- Exclusion log with E-code + rationale for all final exclusions.
- IRR report (Title/Abstract and Full-text).
- PRISMA files:
  - `supplementary/prisma/prisma_flow_input.json`
  - `supplementary/prisma/prisma_flow_input.csv`
  - `supplementary/prisma/prisma_flow_input.txt`

## 9. QA Gates
- No final exclusion without `exclude_code` and `decision_rationale`.
- No unresolved records before PRISMA finalization.
- IRR thresholds met; otherwise recalibration and recoding required.
- All screening decisions traceable to run metadata and adjudicator.

## 10. Two-XLSX Workflow Architecture

### 10.1 Document Hierarchy
| Document | Role | Path |
|----------|------|------|
| **DOCX** (canonical) | Screening/coding protocol source of truth | `docs/03_data_extraction/AI_Adoption_MASEM_Coding_Manual_v1.docx` |
| **1st XLSX** (Screening Workbook) | All 16,189 records: AI + human screening decisions | `data/templates/AI_Adoption_Screening_v1.xlsx` |
| **2nd XLSX** (Coding Workbook) | Included studies (k=40-80): correlation matrices, constructs, moderators | `data/templates/AI_Adoption_MASEM_Coding_v1.xlsx` |

### 10.2 Flow
```
DOCX (canonical protocol)
  ├── 1st XLSX: Screening Workbook (16,189 records, AI+human screening)
  │     ├── AI pre-screening (Codex + Gemini)
  │     ├── Human coder 1 + 2
  │     └── PI adjudication → final include/exclude
  └── 2nd XLSX: Coding Workbook (k=40-80 included studies)
        ├── STUDY_METADATA (pre-filled from screening)
        ├── CORRELATION_MATRIX
        ├── CONSTRUCT_MAPPING
        └── MODERATOR_VARIABLES + provenance
```

### 10.3 Scripts
| Script | Purpose |
|--------|---------|
| `scripts/screening/create_screening_workbook.py` | Generate 1st XLSX from screening master CSV |
| `scripts/screening/merge_ai_to_xlsx.py` | Merge AI screening results into 1st XLSX |
| `scripts/screening/export_included_to_coding.py` | Extract included studies → generate 2nd XLSX |
