# Paper A 연구 논의 기록 (Discussion Log)

> 이 문서는 Paper A(교육 분야 AI 채택 MASEM 메타분석) 진행 과정에서의 주요 논의와 결정 사항을 기록합니다.

---

## 2026-02-26: 스크리닝 프로세스 보고 방안 논의

### 배경
- Paper B의 `SAMPLING_PROTOCOL.md`에서 "16,189 → 575 스크리닝은 Paper A의 범위"라고 명시
- Paper A에서 해당 스크리닝 과정을 어떻게 보고할지, 인간 검토 절차가 충분한지 논의 필요

### 논의 1: Paper A에서 스크리닝 과정 보고 의무

**결론: 반드시 보고해야 함.**

PRISMA 2020 가이드라인(Item 7)에 따라, 스크리닝을 수행한 논문에서 전체 과정을 투명하게 보고해야 한다. Paper A Methods 섹션에 다음을 기술해야 함:
- 3-Tier AI-Assisted Screening 프로토콜 (Tier 1: 키워드 필터, Tier 2: 단일 AI, Tier 3: 이중 AI)
- AI 모델 선택 근거 (Codex, Gemini 사용 이유)
- 인간 검토 절차 (AI Include/Conflict 판정에 대한 human adjudication)
- 각 단계별 수치 (22,166 → 16,189 → 575)

### 논의 2: `human_review_sheet_v4.xlsx` 데이터 현황 점검

Excel 파일의 실제 데이터 분석 결과:

| 시트 | 총 건수 | Claude 판단 | 리뷰어1 | 리뷰어2 | 최종판단 |
|------|---------|-------------|---------|---------|----------|
| include확인 | 575 | 219/575 | 73/575 | 72/575 | **0/575** |
| 제외권고 | 72 | 72/72 | 72/72 | 10/72 | **0/72** |
| HIGH+MEDIUM | 356 | 0/356 | 1/356 | 31/356 | **0/356** |
| conflict | 175 | 0/175 | 0/175 | 0/175 | **0/175** |
| genuine_uncertain | 707 | 0/707 | 0/707 | 0/707 | **0/707** |

**발견 사항:**
- CSV 파일(`screening_ai_dual.csv`, `human_review_queue.csv`)의 `human1_decision`, `human2_decision`, `adjudicated_final_decision` 컬럼은 **전부 비어 있음**
- 인간 리뷰 데이터는 Excel 파일에만 일부 기록되어 있으며, CSV와 연동되지 않은 상태
- 리뷰어1은 주로 제외권고 72건 + include확인 일부를 담당
- 리뷰어2는 include확인 일부 + HIGH+MEDIUM 일부를 담당
- 각자 다른 시트를 맡아 **1명씩** 진행한 상태
- conflict(175건)과 uncertain(707건)은 아직 아무도 검토하지 않음
- 최종판단(⚖ 최종판단)은 전체 시트에서 **0건** 기록

### 논의 3: 스크리닝 인원 — 3명 전수 vs 1명 검토

**질문:** 3명이 모두 스크리닝 해야 하는가, 각자 맡은 범위에서 1명만 해도 되는가?

**결론: 1명 검토도 수용 가능하나, 조건이 있음.**

PRISMA 2020은 "몇 명의 리뷰어가 참여했고, 독립적이었는지, 불일치를 어떻게 해결했는지"를 보고하라고 요구하며, 반드시 2명 이상 전수 스크리닝을 강제하지는 않는다.

**수용 가능한 3가지 접근법:**

| 접근법 | 리소스 | 수용도 | 비고 |
|--------|--------|--------|------|
| A. 전수 이중 스크리닝 | 매우 높음 | Gold standard | 16,189건에는 비현실적 |
| B. AI 스크리닝 + 인간 검증 샘플 | 중간 | 점점 수용 확대 | 현 프로젝트에 적합 |
| C. 1인 스크리닝 + 부분 IRR | 낮음 | 수용 가능 (20~30% 샘플) | 현 프로젝트에 적합 |

**채택 권장안: B+C 혼합 접근**

### 논의 4: 16,189 → 575 과정 검증 결과

레포에 이미 문서화된 자료:
- `docs/02_screening/TIERED_SCREENING_PROTOCOL.md` — 3-Tier 방법론 전체 기술
- `docs/screening/TIER_VALIDATION_REPORT.md` — 검증 결과
- `data/03_screening/screening_ai_dual.csv` (36MB) — AI 이중 스크리닝 원시 데이터 (16,189건)
- `data/03_screening/human_review_queue.csv` (3.5MB) — 인간 리뷰 대기열 (1,457건)
- `data/templates/human_review_sheet_v4.xlsx` — AI + 인간 응답 기록 (부분 완료)
- `supplementary/prisma/PRISMA_2020.txt` — PRISMA 플로우 숫자

**3-Tier AI 스크리닝 검증:**
- Tier 1 (키워드 필터): 12,915건 자동 제외 — 파일럿 104건 교차 검증 FN=0%, 추가 20건 랜덤 감사 100% 정확
- Tier 2 (단일 AI - Gemini): 613건 평가 — Include 8건 모두 적합 (confidence 0.80–1.00)
- Tier 3 (이중 AI - Codex+Gemini): 2,557건 독립 평가
- 최종: exclude 14,725 / include 575 / conflict 175 / uncertain 714

### 결정 사항: Paper A 스크리닝 인간 검증 최소 요건

**반드시 완료해야 할 작업:**

1. **Include확인 575건** — PI 전수 검토 + 두 번째 리뷰어 최소 20%(115건) 독립 검토 → Cohen's κ 산출 (목표 ≥ 0.80)
2. **Conflict 175건** — 최소 1인 전수 판단 (AI 불일치 건), 가능하면 2인 독립 후 불일치 PI 중재
3. **Uncertain 707건** — 최소 1인 제목/초록 기반 전수 검토
4. **Tier 1 제외 12,915건** — 추가 검증 불필요 (이미 파일럿+감사로 검증 완료)

**IRR 산출 전략 (stratified random sample):**
- Tier 1에서 100건 (기존 20건 감사 + 80건 추가)
- Include 575건에서 115건 (~20%)
- Conflict 175건 전수
- Uncertain 707건에서 140건 (~20%)
- 합계 ~510건에 대해 2인 독립 스크리닝 → κ 보고

### 논의 5: 논문 Methods 기술 방향

**권장 기술 방식:**

> "Title and abstract screening was conducted using a three-tier AI-assisted protocol... All AI include decisions (n = 575) and conflict cases (n = 175) were subsequently verified by the principal investigator. To assess inter-rater reliability, a second reviewer independently screened a stratified random sample of 20% of records across all screening categories. Agreement was substantial (κ = X.XX)."

이렇게 하면 "3명 전수"가 아니어도 리뷰어와 편집자가 수용 가능하다. 핵심은:
1. AI가 1차 스크리너 역할을 했다는 점을 투명히 밝히고
2. 인간이 검증했다는 증거(IRR)를 제시하는 것

### 미해결 과제

- [ ] Include확인 575건 인간 검토 완료
- [ ] Conflict 175건 인간 판단 완료
- [ ] Uncertain 707건 인간 검토 완료
- [ ] IRR 산출용 stratified random sample 선정 및 2인 독립 스크리닝
- [ ] Cohen's κ 산출
- [ ] CSV 파일과 Excel 파일 간 인간 리뷰 데이터 동기화
- [ ] PRISMA_2020.txt의 Final Inclusion 수치 업데이트
- [ ] Search_Strategy_Appendix.md의 "[TBD]" 실제 수치로 교체
- [ ] 최종판단(⚖ 최종판단) 컬럼 전체 기록

---

## 2026-02-26: Paper A 폴더 구조 생성

### 배경
- Paper B는 이미 체계적인 폴더 구조(`paper_b/`)가 존재
- Paper A는 레포 루트의 여러 폴더에 자료가 분산되어 있었음
- Paper A 전용 폴더를 Paper B 구조에 맞춰 생성하기로 결정

### 결정 사항

**생성된 `paper_a/` 디렉토리 구조:**

```
paper_a/
├── README.md
├── DISCUSSION_LOG_KR.md         ← 이 파일
├── checklists/                  # PRISMA 2020 체크리스트
├── data/
│   ├── 00_search_records/       # 데이터베이스별 원시 검색 결과
│   ├── 01_deduplication/        # 중복 제거 로그
│   ├── 02_screening/            # 스크리닝 데이터
│   │   ├── tier1_keyword/       #   Tier 1: 키워드 자동 필터
│   │   ├── tier2_single_ai/     #   Tier 2: 단일 AI (Gemini)
│   │   ├── tier3_dual_ai/       #   Tier 3: 이중 AI (Codex+Gemini)
│   │   └── human_verification/  #   인간 검증 시트 및 IRR 데이터
│   ├── 03_eligibility/          # 전문 적격성 평가
│   ├── 04_extraction/           # 데이터 추출
│   │   ├── ai_extraction/       #   AI 자동 추출
│   │   ├── human_coding/        #   인간 코딩
│   │   └── consensus/           #   합의 도출
│   └── 05_analysis/             # 최종 분석 데이터셋
├── manuscript/                  # 원고 초안
├── scripts/                     # 분석 스크립트 (R, Python)
├── templates/                   # 코딩 시트, IRR 템플릿 등
└── prompts/                     # AI 추출용 프롬프트 모듈
```

**Paper B와의 차이점:**
- `data/02_screening/`을 Tier별로 세분화 (Paper A의 3-Tier 구조 반영)
- `data/00_search_records/`, `data/01_deduplication/` 추가 (Paper A만의 범위)
- `data/03_eligibility/` 추가 (전문 적격성 평가 단계)
- 체크리스트는 PRISMA 2020 (Paper B는 PRISMA-trAIce, TRIPOD-LLM)

**기존 레포 자료와의 관계:**
- `docs/02_screening/` → `paper_a/data/02_screening/`으로 이관 또는 참조
- `data/03_screening/` → `paper_a/data/02_screening/`과 매핑
- `supplementary/prisma/` → `paper_a/checklists/`로 이관 또는 참조
- `supplementary/Search_Strategy_Appendix.md` → Paper A Methods 섹션 기반 자료

---

## 2026-02-26: 스크리닝 파이프라인 재정의 & v5 Excel 구조 개편

### 문제 1: Tier 2는 "단일 AI"가 아님

프로토콜에는 "Tier 2 = Single AI (Gemini)"로 기술되어 있으나, 실제 데이터 분석 결과:

| Tier 2 (613건) | 건수 | 비율 |
|----------------|------|------|
| Codex + Gemini **둘 다** 평가 | 411 | 67% |
| Gemini만 | 202 | 33% |

Gemini가 uncertain 판정한 건에 Codex를 보완 투입한 것으로 확인됨. `codex_retry2_model = gpt-5.1-codex-mini` 250건 기록.

**결정:** "단일 AI" 표현을 삭제하고, 전체를 "AI 이중 스크리닝 (Codex + Gemini)"으로 통합 기술.

### 문제 2: Claude = 3번째 AI 스크리너

Claude Sonnet 4.6이 575건 중 219건을 평가하여 72건을 exclude로 뒤집은 것은 **인간 검증이 아니라 AI 스크리닝의 추가 레이어**.

**결정:** Claude를 AI 스크리닝 Phase에 포함시키고, 인간 검증과 분리.

### 수정된 스크리닝 파이프라인

```
Phase 1: 키워드 자동 필터
  16,189 → 3,274건 통과 (12,915건 제외)

Phase 2: AI 3모델 스크리닝
  Codex + Gemini: 3,274건 평가
  Claude Sonnet 4.6: Include 후보 재평가
  → AI 합의: 다수결 (3모델 중 2개 이상 동일 → 채택)

Phase 3: 인간 검증 (3명)
  Step 1: Claude 미평가 1,238건 완료 (AI 합의 완성)
  Step 2: R1(PI) — 1,457건 전수 검토
  Step 3: R2(PhD) — 계층 무작위 20% (~290건) 독립 검토
  Step 4: IRR 확인 (κ ≥ 0.80)
  Step 5: R3(중재자) — R1-R2 불일치 건 최종 판단
  Step 6: PI — 최종판단 확정
```

### v5 Excel 구조 개편

**v4 문제점:**
- 5개 데이터 시트 (중복 포함)
- AI 분석 컬럼과 스크리닝 컬럼 혼재
- Claude가 인간 리뷰어와 같은 위치에 배치

**v5 구조 (단일 시트):**
```
스크리닝 시트 (1,457건 × 18컬럼):
  기본: ID | 제목 | 연도 | 초록
  AI 3모델: Codex | Gemini | Claude Sonnet 4.6 | AI 합의
  R1(PI): 판단 | 코드 | 메모
  R2: 판단 | 코드 | 메모
  R3(중재): 판단 | 메모
  최종: 최종판단 | 최종코드

코딩가이드 시트:
  리뷰어 역할 및 순서 (Step 1~6)
  판단 입력값 (O/X/?)
  제외코드 (E-FT1~E-FT8)
  AI 합의 규칙 (3모델 다수결)
  포함 기준
```

**리뷰어 3명 역할:**

| Step | 담당 | 범위 | 목적 |
|------|------|------|------|
| Step 1 | Claude Sonnet 4.6 | 미평가 1,238건 | AI 합의 완성 |
| Step 2 | R1 — PI | 1,457건 전수 | 전수 인간 검토 |
| Step 3 | R2 — PhD학생 | ~290건 (20% 표본) | IRR 산출 |
| Step 4 | IRR 확인 | R1∩R2 ~290건 | κ ≥ 0.80 확인 |
| Step 5 | R3 — 중재자 | 불일치 건만 | 불일치 해결 |
| Step 6 | PI | 전체 | 최종 확정 |

### 현재 진행률

| 항목 | 완료 | 전체 | 비율 |
|------|------|------|------|
| Claude 평가 | 219 | 1,457 | 15% |
| R1(PI) | 72 | 1,457 | 4.9% |
| R2 | 71 | 1,457 | 4.9% |
| 최종판단 | 0 | 1,457 | 0% |
