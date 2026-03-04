# Repository Restructuring Proposal

> **Date**: 2026-03-04
> **Author**: Claude Opus 4.6 (AI Research Assistant)
> **Status**: PI 검토 대기
> **원칙**: 불필요한 파일 삭제, 중복 제거, 의사결정 추적 명확화

---

## 1. 현재 문제점 진단

### 문제 1: data/ 디렉토리 중복 (3개의 "raw" 폴더)

| 경로 | 내용 | 문제 |
|------|------|------|
| `data/00_raw/` | study_metadata.csv + empty subdirs | 빈 스캐폴딩 (실 데이터 없음) |
| `data/01_raw/` | **실제 검색 결과** (WoS, Scopus 등 CSV/XLS) | 이것이 진짜 raw data |
| `data/raw/` | empty search_results/ | 완전히 빈 폴더 |

**해결**: `data/01_raw/`만 유지, 나머지 2개 삭제

### 문제 2: data/ 번호 체계 혼란 (두 개의 번호 체계 공존)

현재 두 가지 번호 체계가 혼재:

체계 A (README 기준): 00_raw → 01_extracted → 02_processed → 03_screening → 04_included → 05_coding → 06_pooled → 07_final
체계 B (실제 존재): 00_raw → 01_raw → 01_extracted → 02_processed → 02_verified → 03_pooled → 03_screening → 04_final → 06_pooled → 07_final

**결과**: 같은 번호에 다른 단계 (02_processed vs 02_verified), 빈 단계 (04_included, 05_coding 없음)

### 문제 3: docs/ 디렉토리 중복 (같은 주제 3곳에 분산)

| 주제 | 위치 1 | 위치 2 | 위치 3 |
|------|--------|--------|--------|
| 검색 전략 | `docs/01_literature_search/` (2 files) | `docs/search_strategy/` (2 files) | — |
| 스크리닝 | `docs/02_screening/` (1 file) | `docs/02_study_selection/` (2 files) | `docs/screening/` (1 file) |

### 문제 4: 오래된 템플릿 버전 7개 공존

`data/templates/`에 human_review_sheet 7개 버전:
- `human_review_sheet.xlsx` (2MB, 원본)
- `human_review_sheet_v2.xlsx`
- `human_review_sheet_v3.xlsx`
- `human_review_sheet_v4.xlsx`
- `human_review_sheet_v5.xlsx`
- `human_review_sheet_v7_IRR.xlsx`
- `human_review_sheet_v8.xlsx` ← **현재 사용 중**

→ v8만 유지, 나머지는 `_archive/`로 이동 (git history에 보존됨)

### 문제 5: paper_a/ vs root data/ 중복

paper_a/ 내부에도 `data/02_screening/`, `data/04_extraction/` 등이 있고, root `data/03_screening/`에도 스크리닝 데이터가 있음. 어느 것이 권위 있는 데이터인지 불명확.

### 문제 6: 빈 스캐폴딩 (.gitkeep만 있는 디렉토리)

총 40개+ 디렉토리에 .gitkeep만 존재. 데이터가 채워지기 전까지는 불필요한 노이즈.

### 문제 7: MASTER_INTEGRATION_DOCUMENT.md vs README.md 중복

README.md와 MASTER_INTEGRATION_DOCUMENT.md가 거의 동일한 정보를 담고 있음.

---

## 2. 제안: 삭제 대상 파일/디렉토리

### 즉시 삭제 가능 (데이터 없는 빈 스캐폴딩)

```
삭제:
  data/00_raw/                          # 빈 스캐폴딩 (data/01_raw/가 실제 데이터)
  data/raw/                             # 완전히 빈 폴더
  data/01_extracted/                    # 빈 CSV만 있음, 아직 추출 전
  data/02_verified/                     # 빈 verified_correlations.csv
  data/03_pooled/                       # 빈 (.gitkeep만), data/06_pooled/에 실제 파일 있음
  data/04_final/                        # 빈 (.gitkeep만), data/07_final/에 실제 파일 있음
  figures/                              # 빈 output/ + source/ (.gitkeep만)
  manuscript/                           # 빈 (paper_a/manuscript/와 paper_b/manuscript/가 실제)
```

### 통합 후 삭제 (중복 docs)

```
통합:
  docs/search_strategy/* → docs/01_literature_search/로 이동
  docs/02_study_selection/* → docs/02_screening/으로 이동
  docs/screening/* → docs/02_screening/으로 이동

삭제 (이동 후):
  docs/search_strategy/
  docs/02_study_selection/
  docs/screening/
```

### 아카이브 (오래된 템플릿)

```
data/templates/_archive/로 이동:
  human_review_sheet.xlsx
  human_review_sheet_v2.xlsx
  human_review_sheet_v3.xlsx
  human_review_sheet_v4.xlsx
  human_review_sheet_v5.xlsx
  human_review_sheet_v7_IRR.xlsx

유지:
  human_review_sheet_v8.xlsx ← 현재 사용 중
  AI_Adoption_MASEM_Coding_v1.xlsx ← 코딩 템플릿
  create_masem_template.py ← 스크립트
```

### 통합 후 삭제 (중복 문서)

```
삭제:
  MASTER_INTEGRATION_DOCUMENT.md        # README.md로 통합
```

---

## 3. 제안: 새로운 data/ 번호 체계

현재 → 제안:

```
data/
├── 01_raw/                    # (유지) 원본 검색 결과
│   └── search_results/        # WoS, Scopus, PsycINFO, IEEE
├── 02_processed/              # (유지) 병합 + 중복제거
├── 03_screening/              # (유지) AI 스크리닝 + 인간 리뷰
├── 06_pooled/                 # (유지) 합동 상관행렬 — 번호 유지 (git history 보존)
├── 07_final/                  # (유지) 최종 MASEM 데이터셋 — 번호 유지
└── templates/                 # (유지, 정리) 현재 사용 중인 것만
```

번호 갭(04, 05)은 향후 단계 추가 시 사용 예정:
- `04_included/` — full-text eligibility 완료 후 생성
- `05_coding/` — AI 코딩 파이프라인 실행 후 생성

---

## 4. 제안: 새로운 docs/ 구조

```
docs/
├── 01_literature_search/      # 검색 전략 (통합: 기존 search_strategy/ 포함)
│   ├── database_coverage.md
│   ├── search_strategy.md
│   ├── QUICK_REFERENCE_CHEATSHEET.md    # ← search_strategy/에서 이동
│   └── SEARCH_EXECUTION_GUIDE.md        # ← search_strategy/에서 이동
├── 02_screening/              # 스크리닝 (통합: 기존 02_study_selection/, screening/ 포함)
│   ├── TIERED_SCREENING_PROTOCOL.md
│   ├── inclusion_exclusion_criteria.md  # ← 02_study_selection/에서 이동
│   ├── screening_protocol.md            # ← 02_study_selection/에서 이동
│   └── TIER_VALIDATION_REPORT.md        # ← screening/에서 이동
├── 03_data_extraction/        # (유지)
├── 04_methodology/            # (유지) — model_specification.md 업데이트 완료
├── 05_manuscript/             # (유지)
├── 06_decisions/              # (유지) — decision_log.md 업데이트 완료
├── discussion/                # (유지) — 토론 기록
└── README.md                  # docs 색인
```

---

## 5. 영향 없는 디렉토리 (변경 없음)

이 디렉토리들은 실제 데이터/코드가 있으므로 변경하지 않음:

- `analysis/` — 13개 R 스크립트 + Python 유틸리티
- `scripts/` — 스크리닝, AI 코딩 파이프라인
- `configs/` — 모델 명세 YAML, Bayesian priors
- `supplementary/` — PRISMA, codebook, protocol
- `paper_a/` — Paper A 전용 데이터/스크립트
- `paper_b/` — Paper B 전용 데이터/스크립트
- `tests/` — 테스트 코드
- `pdfs/` — PDF 저장소 (.gitkeep)

---

## 6. README.md 업데이트 필요

현재 README.md의 "Repository Structure" 섹션이 실제 구조와 불일치. 재구조화 후 업데이트 필요:
- data/ 구조 반영
- docs/ 구조 반영
- Model 4 추가 반영
- 파이프라인 상태 업데이트

---

## 7. 실행 순서

PI 승인 후:

1. docs/ 파일 이동 (통합)
2. data/ 빈 디렉토리 삭제
3. 템플릿 아카이브 이동
4. MASTER_INTEGRATION_DOCUMENT.md 삭제
5. figures/, manuscript/ 빈 스캐폴딩 삭제
6. README.md 업데이트
7. 커밋 + 푸시

모든 삭제 대상은 git history에 보존되므로 필요 시 복구 가능.

---

## 8. 요약 (삭제/이동 수량)

| 작업 | 수량 |
|------|------|
| 디렉토리 삭제 | 8개 |
| 파일 이동 (통합) | 5개 |
| 파일 아카이브 | 6개 (오래된 템플릿) |
| 파일 삭제 | 1개 (MASTER_INTEGRATION_DOCUMENT.md) |
| README 업데이트 | 1개 |
| 총 영향 파일 | ~21개 |
