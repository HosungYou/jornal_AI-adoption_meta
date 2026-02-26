# Audit Trail Guide: Paper B

## 개요

Paper B의 모든 AI 활용 과정을 투명하게 문서화하기 위한 가이드.
PRISMA-trAIce (2025), TRIPOD-LLM (2025), RAISE (2025) 요구사항 충족.

---

## 1. AI Extraction Logging

### Per-Call Log (templates/extraction_log_template.csv)

매 API 호출마다 기록:

| Field | Description | Example |
|-------|-------------|---------|
| `call_id` | Unique call identifier | `CL-S001-A-001` |
| `study_id` | Study identifier | `S001` |
| `model` | AI model name | `claude_sonnet_4.6` |
| `model_version` | Specific version/date | `claude-sonnet-4-6-20260101` |
| `module` | Extraction module | `A` (bibliographic) |
| `prompt_version` | Prompt file hash | `v1.0_sha256_abc123` |
| `temperature` | Temperature setting | `0` |
| `max_tokens` | Max token setting | `4096` |
| `timestamp_start` | Call start time (UTC) | `2026-03-01T10:30:00Z` |
| `timestamp_end` | Call end time (UTC) | `2026-03-01T10:30:15Z` |
| `input_tokens` | Token count (input) | `3200` |
| `output_tokens` | Token count (output) | `450` |
| `cost_usd` | API cost | `0.012` |
| `status` | Call status | `success` / `error` / `retry` |
| `error_message` | Error details (if any) | `null` |
| `raw_output_file` | Path to raw JSON output | `data/02_ai_extraction/claude/S001_A_raw.json` |

### Per-Study Summary

각 study에 대해 3 models × 4 modules = 12 API calls 기록.

```
data/02_ai_extraction/
├── extraction_log.csv          ← 전체 API call 로그
├── claude/
│   ├── S001_A_raw.json        ← Module A raw output
│   ├── S001_B_raw.json        ← Module B raw output
│   ├── S001_C_raw.json        ← Module C raw output
│   ├── S001_D_raw.json        ← Module D raw output
│   ├── S001_combined.json     ← 4 modules merged
│   └── ...
├── codex/
│   └── (same structure)
└── gemini/
    └── (same structure)
```

---

## 2. Prompt Documentation

### 버전 관리

| File | Content | Version Control |
|------|---------|----------------|
| `prompts/module_a_bibliographic.md` | Module A prompt | Git-tracked, SHA hash |
| `prompts/module_b_correlation.md` | Module B prompt | Git-tracked, SHA hash |
| `prompts/module_c_construct.md` | Module C prompt | Git-tracked, SHA hash |
| `prompts/module_d_moderator.md` | Module D prompt | Git-tracked, SHA hash |

### 프롬프트 변경 규칙

- **Pilot 단계** (Week 1): 프롬프트 수정 허용 (10 test studies 기반)
- **본 추출 시작 후**: 프롬프트 수정 금지 (version frozen)
- 모든 변경은 Git commit으로 추적
- 최종 사용 프롬프트 버전을 Methods에 명시

---

## 3. Human Coding Audit

### Phase 1: Independent Coding Log

```
data/03_human_coding/
├── coder1_PI/
│   ├── coding_sheet_H1.csv       ← 100 studies × 30 variables
│   ├── coding_notes_H1.md        ← 판단 근거, 의문사항 메모
│   └── coding_time_log_H1.csv    ← 소요 시간 기록
│
└── coder2_phd1/
    ├── coding_sheet_H2.csv
    ├── coding_notes_H2.md
    └── coding_time_log_H2.csv
```

### Time Log 형식

| Field | Description |
|-------|-------------|
| `study_id` | S001-S100 |
| `coder_id` | H1 / H2 |
| `date` | 코딩 날짜 |
| `start_time` | 시작 시각 |
| `end_time` | 종료 시각 |
| `duration_min` | 소요 시간 (분) |
| `difficulty` | Easy / Medium / Hard |
| `notes` | 특이사항 |

---

## 4. IRR & Discrepancy Log

### IRR Calculation Record

```
data/06_analysis/
├── irr_results.csv               ← Variable별 κ, ICC 값
├── irr_summary.md                ← 전체 요약 + 해석
└── discrepancy_log.csv           ← 불일치 항목 + 해결 과정
```

### Discrepancy Log 형식

| Field | Description |
|-------|-------------|
| `disc_id` | 불일치 ID (D001-) |
| `study_id` | Study identifier |
| `variable` | 불일치 변수명 |
| `coder1_value` | H1의 값 |
| `coder2_value` | H2의 값 |
| `source_location` | 원문 참조 위치 (page, table, paragraph) |
| `resolution` | 합의 결과 |
| `resolved_value` | 최종 gold standard 값 |
| `resolution_method` | 원문 재확인 / 규칙 적용 / PI 결정 |
| `resolution_date` | 합의 날짜 |
| `notes` | 추가 설명 |

---

## 5. Consensus & Verification Log

### AI Consensus Record

```
data/04_consensus/
├── consensus_100.csv             ← 100 studies 합의 결과
├── consensus_remaining.csv       ← 나머지 ~200 studies
└── consensus_algorithm_log.md    ← 합의 규칙 + 매개변수
```

### Phase 2 Verification Log

```
data/03_human_coding/
├── phase2_verification_H1.csv    ← H1 검증 결과
└── phase2_verification_H2.csv    ← H2 검증 결과
```

| Field | Description |
|-------|-------------|
| `study_id` | Study identifier |
| `variable` | Variable name |
| `ai_consensus_value` | AI 합의 값 |
| `human_verified_value` | 인간 확인 값 |
| `match` | TRUE / FALSE |
| `override` | TRUE / FALSE |
| `override_reason` | 불일치 시 사유 |
| `verifier_id` | H1 / H2 |
| `verification_date` | 확인 날짜 |
| `time_spent_min` | 소요 시간 |

---

## 6. QA Spot-Check Log

```
data/06_analysis/
├── qa_spotcheck.csv              ← H3 spot-check 결과
└── qa_report.md                  ← QA 종합 보고서
```

### QA Report 항목

1. **Error rate**: 발견된 오류 수 / 전체 확인 data elements
2. **Error type breakdown**: 코딩 오류 / 입력 오류 / 변환 오류 / 매핑 오류
3. **Verifier-level analysis**: H1 담당분 vs. H2 담당분 오류율 비교
4. **Recommendation**: PASS / CONDITIONAL PASS / FAIL

---

## 7. OSF Repository Structure

최종 공개 데이터:

```
OSF Project: Paper B - LLM-Assisted MASEM Coding
│
├── 1_Prompts/
│   ├── module_a_bibliographic.md
│   ├── module_b_correlation.md
│   ├── module_c_construct.md
│   └── module_d_moderator.md
│
├── 2_Raw_AI_Outputs/
│   ├── claude/ (100 studies × 4 modules JSON)
│   ├── codex/ (100 studies × 4 modules JSON)
│   └── gemini/ (100 studies × 4 modules JSON)
│
├── 3_Gold_Standard/
│   ├── gold_standard_100.csv
│   └── irr_results.csv
│
├── 4_Analysis/
│   ├── analysis.R
│   ├── model_accuracy.csv
│   └── figures/
│
├── 5_Checklists/
│   ├── PRISMA_trAIce_completed.md
│   └── TRIPOD_LLM_completed.md
│
└── README.md (데이터 사전 + 재현 지침)
```

---

## 8. PRISMA-trAIce Compliance Map

Paper B Methods에 포함해야 할 14개 항목 매핑:

| # | PRISMA-trAIce Item | Paper B Section | Status |
|---|-------------------|-----------------|--------|
| 1 | AI tool name & version | Methods 3.2 | ✅ |
| 2 | AI access date range | Methods 3.2 | ✅ |
| 3 | Task description | Methods 3.2 | ✅ |
| 4 | Prompt text (full or summary) | Appendix A | ✅ |
| 5 | Prompt development process | Methods 3.2.1 | ✅ |
| 6 | Input data description | Methods 3.1 | ✅ |
| 7 | Output format specification | Methods 3.2.2 | ✅ |
| 8 | Human oversight protocol | Methods 3.3 | ✅ |
| 9 | Verification method | Methods 3.3 | ✅ |
| 10 | Error handling | Methods 3.3.3 | ✅ |
| 11 | Reproducibility measures | Methods 3.4 | ✅ |
| 12 | Limitations of AI use | Discussion | ✅ |
| 13 | Cost/resource reporting | Results | ✅ |
| 14 | Data availability | Data Availability Statement | ✅ |
