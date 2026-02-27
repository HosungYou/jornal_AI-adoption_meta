# Paper B 연구 논의 기록 (한국어)

> 이 문서는 Paper B 연구 설계 과정에서의 논의를 한국어 원문으로 보존합니다.
> 맥락 유지 및 의사결정 추적 목적.

---

## 2026-02-25: 초기 논의

### 1. 프로젝트 개요

**배경**: AI Adoption in Education에 대한 MASEM (Meta-Analytic Structural Equation Modeling) 연구 진행 중.
- 12개 construct (TAM/UTAUT + AI-specific): PE, EE, SI, FC, BI, UB, ATT, SE, TRU, ANX, TRA, AUT
- 16,189개 records에서 3단계 AI 스크리닝 → 575개 Include 판정
- 최종 MASEM-eligible: ~300개 예상

**목표**: 두 개의 독립 논문으로 분리 제출
- **Paper A** (메타분석): AI Adoption in Education MASEM → Computers & Education (IF 12.0)
- **Paper B** (방법론): LLM-Assisted Data Extraction 평가 → Research Synthesis Methods (1순위) / JMIR AI (2순위)

### 2. Paper A와 B의 관계

- Paper A와 B는 기존 구조를 참고용으로 사용하되, 필요 시 구조 변혁 가능
- Paper B는 Paper A의 100-study subsample을 gold standard로 사용
- Paper B는 Paper A 완성 전에 독립적으로 제출 가능 (OSF Preprint으로 cite)

### 3. AI 모델 선정

최종 결정된 AI 모델 3개:
- **Claude Sonnet 4.6** (Anthropic)
- **GPT Codex 5.3** (OpenAI)
- **Gemini CLI** (Google)

### 4. 연구팀 구성

- **R1 (PI / Adjudicator)**: Hosung You, Penn State College of Education
- **R2**: 박사과정생 1 (독립 코더)
- **R3**: 박사과정생 2 (독립 코더 + QA)

> ※ 2026-02-26 변경: H1/H2/H3 → R1/R2/R3. 결정 14 참조.

---

## 핵심 의사결정 기록

### 결정 1: Cohen's kappa vs. 다른 IRR 지표

**문제**: 3명의 human coder로 Cohen's kappa 사용 가능한가?
**결론**: Cohen's kappa는 2명 전용. 3명 이상은 Fleiss' kappa 또는 Krippendorff's alpha 사용.
**최종 설계**: 2명 human coder (R2, R3)가 독립 코딩 → Cohen's kappa + ICC(2,1) 사용. R1(PI)은 adjudicator로 불일치 중재.

### 결정 2: ICR 샘플링 비율

**문제**: 20% ICR sample만 할 것인가, 100% 할 것인가?
**조사 결과**:
- 일반 메타분석: 20% ICR이 관행
- AI validation 논문들: **모두 100% human verification** 사용 (Gartlehner 2024/2025, Jensen 2025, Khan 2025 등)
**최종 결정**: Paper B는 100 studies 전체를 gold standard로 코딩 (100% independent human coding)

### 결정 3: AI-first vs. Human-first 접근 + Paper A/B 범위 구분

**문제**: "AI extracts → Human verifies 100%" vs. "Human codes first → AI codes → Compare"
**분석**:
- AI-first: anchoring bias 위험 (인간이 AI 결과에 영향받음)
- Human-first: gold standard으로서의 가치 높음, 더 rigorous
**최종 설계**: 3-Phase Hybrid Design (Phase 1-3)

**Phase 1 (100 studies) — 📘 Paper B 핵심 + 📗 Paper A 활용**:
- Human-first: R2+R3 독립 코딩 (blinded to AI) + AI 3개 모델 독립 추출
- Gold standard 확립 → AI 정확도 평가 (Paper B의 핵심 분석)
- Gold standard 데이터는 Paper A의 MASEM에도 활용

**Phase 2 (~200 studies) — 📗 Paper A 전용**:
- AI-first verification: AI consensus → 인간(R1, R2) 검증
- Phase 1에서 검증된 AI 성능을 기반으로, 효율적 코딩 방식 적용
- Paper B에서는 분석하지 않으며, Methods에서 간략 언급만

**Phase 3 (Phase 2의 10% spot-check) — 📗 Paper A 전용**:
- R3 (fresh eyes)가 독립적으로 spot-check
- Paper B에서는 분석하지 않음

**Paper B에 보고하는 것**: Phase 1의 100 studies (IRR + AI accuracy + consensus + workflow)
**Paper A에 보고하는 것**: Phase 1-3 전체 (~300 studies의 MASEM 데이터)

### 결정 4: 샘플 크기

**문제**: Paper B에 300개 전체? 일부만?
**결론**: 100개면 충분. 근거:
- 3,000 data elements (100 studies × 30 variables)
- 기존 선행연구 대비 충분 (Gartlehner: 22개, Jensen: 178개 but subset verification)
- 6주 타임라인 내 실현 가능
- 층화무작위추출로 대표성 확보

### 결정 5: 575 → 300 → 100 프로세스

**문제**: 575개에서 100개를 어떻게 선택할 것인가?
**결론**: 2단계 프로세스
- Stage 1: Full-text eligibility review (575 → ~300) — MASEM-specific criteria 적용
- Stage 2: Stratified random sampling (~300 → 100) — 4개 층화 변수 (year, AI tool type, education level, region)
- 스크리닝(16,189 → 575)은 Paper A 범위이며 Paper B에서는 추적하지 않음

### 결정 6: Paper A 인용 전략

**문제**: 미완성 Paper A를 Paper B에서 어떻게 cite?
**결론**: OSF Preprint 전략
- Paper A를 OSF Preprint으로 등록 → DOI 획득
- Paper B에서 DOI로 cite
- APA 7th "manuscript in preparation" 형식도 backup으로 사용 가능

### 결정 7: MASEM 비판 대응

**우려**: Correlation 기반 MASEM에 대한 에디터 비판 가능성
**식별된 비판 요소 6가지**:
1. β → r 변환의 정확성 → Peterson & Brown (2005) + sensitivity analysis
2. Construct harmonization → 명확한 매핑 규칙 + 투명한 결정 로그
3. Positive definite matrix → near-PD correction + 보고
4. Common method bias → CMB 테스트 포함
5. Publication bias → funnel plot, trim-and-fill, PET-PEESE
6. Causal inference → "predictive model" 표현, 횡단 한계 명시

### 결정 8: 보고 가이드라인

Paper B에 적용할 보고 기준:
- **PRISMA-trAIce** (2025): 14-item checklist for AI in evidence synthesis
- **TRIPOD-LLM** (Collins et al., 2025, Nature Medicine): LLM 기반 연구 보고
- **RAISE framework** (Cochrane/Campbell/JBI/CEE, 2025): 책임 있는 AI 사용

---

## 선행연구 조사 결과 요약

### AI-Assisted Coding 선행 사례

| 저자 | 연도 | 샘플 | AI 모델 | 검증 방식 | 주요 발견 |
|------|------|------|---------|----------|----------|
| Gartlehner et al. | 2024 | 22 SRs | GPT-4 | 100% human verification | Data extraction에서 높은 정확도 |
| Gartlehner et al. | 2025 | 확장 | GPT-4 | 100% human verification | 반복 검증 |
| Jensen et al. | 2025 | 178 studies | Multiple LLMs | Subset verification | Multi-model 비교 |
| Khan et al. | 2025 | — | LLM-assisted | Full verification | MA data extraction |
| Campos et al. | 2024 | — | LLMs | — | SR data extraction 가이드라인 |
| Wang et al. | 2024 | — | GPT-4 | — | MA에서의 LLM 활용 |
| Alshami et al. | 2023 | — | ChatGPT | — | SR 자동화 |

### 학술지 및 기관 정책

- **Cochrane/Campbell/JBI/CEE**: RAISE Framework (2025) — AI는 도구로만, 인간 감독 필수
- **Nature Medicine**: TRIPOD-LLM 가이드라인 발표
- **Research Synthesis Methods**: AI-assisted SR 방법론 논문 활발히 게재 중
- **JMIR AI**: AI in health/education 방법론 중점

---

## 2026-02-26: 스크리닝 파이프라인 최종 확정 (v8)

### 결정 9: Codex 스크리닝 제외

**문제**: 3-모델 AI 스크리닝(Gemini + Claude + Codex) 결과에서 Codex의 판별력 부재.
**분석**:
- Codex의 85%가 uncertain 판정 → 스크리닝 기여 불가
- Gemini + Claude 2-모델 합의만으로 충분한 coverage 확보
**결론**: 스크리닝에서 Codex 제외, Gemini + Claude 2-model consensus로 진행.

> **참고**: Paper B의 Phase 1 데이터 추출에서는 여전히 3개 모델(Claude, Codex, Gemini) 사용.

### 결정 10: 스크리닝 파이프라인 확정 수치

| Category | Count | Description |
|----------|-------|-------------|
| Auto-INCLUDE | 358 → **367** | Gemini + Claude 둘 다 include |
| Auto-EXCLUDE | 15 | Gemini + Claude 둘 다 exclude |
| TIER1 Conflict | 95 | include ↔ exclude |
| TIER2 High | 495 → **480** | include + uncertain |
| TIER3 Low | 494 → **500** | uncertain 등 |
| **Total** | **1,457** | |

### 결정 11: 스크리닝 역할 설계 — Option C 채택 (2-Rater IRR + R1 Adjudicator)

**문제**: 3명이 동시에 스크리닝하는 것 vs. 2명 IRR + PI adjudicator 중 어느 것이 효율적인가?
**검토한 옵션**:
- **Option A**: 3명 동일 200건 코딩 (Fleiss' κ) — 자원 낭비
- **Option B**: R2+R3 200건 IRR + R1 별도 200건 — 중복 검증
- **Option C**: R2+R3 200건 IRR + R1 spot-check/추가코딩/adjudicator ✅

**채택 근거**:
- SR/MA 관행에서 2-rater IRR + adjudicator가 표준
- R1(PI)의 시간을 spot-check, 추가코딩, 중재에 분산 활용
- Cohen's κ(2명) 보고가 학술지에서 가장 흔한 형태

**R1(PI) 업무**:
| 작업 | 건수 | 시트 |
|------|------|------|
| Auto-INCLUDE spot-check | 86건 (36 IRR + 50 R1전용) | 시트② |
| TIER2 추가코딩 | 135건 (v8, 이전 150건) | 시트③ |
| R2-R3 불일치 중재 | IRR 후 불일치건 | 시트① |

### 결정 12: IRR 200건 구성

| Tier | Count | 근거 |
|------|-------|------|
| 🔴 TIER1 (include↔exclude) | 85 | 최우선 검증 대상 |
| 🔵 SPOT_CHECK (Auto-INCLUDE 10%) | 36 | Auto-INCLUDE 품질 검증 |
| 🟡 TIER2 (include+uncertain) | 79 | 나머지 배분 |
| **합계** | **200** | |

### 결정 13: Claude reason 데이터 무결성 수정

**문제**: v7 엑셀에서 Claude 판정(include)과 Claude 사유(E-FT exclude)가 모순되는 레코드 발견.
**원인**: v5 파이프라인의 Claude 판정과 v6(다른 세션)의 Claude 사유를 혼합하여 사용.
- IRR 200건 중 12건(6%)에서 모순 발생
- Auto-INCLUDE 358건 중 71건(19.8%)에서 모순 발생

**해결**:
1. v5 파이프라인 CSV만 권위적 소스로 확정
2. v6 사유 전면 폐기
3. 사유 없는 68건(exclude 52, include 13, uncertain 3)에 대해 수동으로 사유 생성
4. v8 엑셀에 모든 200건의 사유 반영 완료

### 결정 14: 코더 ID 체계 변경

**변경**: H1/H2/H3 → R1/R2/R3
| 이전 | 변경 후 | 역할 |
|------|---------|------|
| H1 | R1 (PI) | Adjudicator, spot-check, 추가코딩 |
| H2 | R2 (PhD 1) | 독립 코더 |
| H3 | R3 (PhD 2) | 독립 코더 + QA |

### 산출물

- `data/templates/human_review_sheet_v8.xlsx` — 최종 스크리닝 엑셀 (5개 시트)
- `paper_a/README.md` — 파이프라인 반영 완료
- `paper_a/DISCUSSION_LOG_KR.md` — 의사결정 기록 추가
- `paper_b/README.md` — 스크리닝 파이프라인 및 IRR 설계 반영
- `paper_b/RESEARCHER_ROLES.md` — R1/R2/R3 역할 및 Option C 반영

---

---

## 2026-02-27: v8 Excel 업데이트 — Claude 재스크리닝 및 Tier 재분류

### 결정 15: 42건 Claude 재스크리닝

**문제**: Sheet ③ (R1 추가코딩) 150건 중 42건에 Claude 사유가 없었음. 원인은 해당 건들이 Codex+Gemini 파이프라인에서만 처리되어 Claude 미평가 상태.
**해결**: Claude Opus 4.6으로 42건 직접 재스크리닝 (23 include, 19 uncertain)
**결과**: Claude 총 평가 건수 1,238 → 1,280건

### 결정 16: Tier 재분류

재스크리닝 후 15건의 Gemini+Claude 조합이 변경됨:
- 9건: TIER2 → Auto-INCLUDE (include+include) → Sheet ②로 물리적 이동
- 6건: TIER2 → TIER3 (uncertain+uncertain) → Sheet ③에서 삭제

**최종 수치 (v8)**:
| 항목 | 이전 | 이후 |
|------|------|------|
| Auto-INCLUDE (Sheet ②) | 358 | 367 |
| TIER2 (Sheet ③ R1 추가코딩) | 150 | 135 |
| TIER3 | 494 | 500 |
| R1 총 업무량 | ~236 | ~221 |

### 결정 17: 코딩 가이드 (Sheet ⑤) 업데이트

- TRA 정의 수정: "Training" → "AI Transparency (AI 투명성/설명가능성)"
- AUT 정의 명확화: "Perceived AI Autonomy (지각된 AI 자율성)"
- adoption_dv_type에 `adoption_composite` 추가
- UTAUT2 처리 근거, AI-specific construct 포함 rationale, TAM-UTAUT 교집합 명시

### 결정 18: 전체 문서 Codex 참조 정리

스크리닝 관련 문서에서 Codex → Gemini+Claude 반영, 수치 업데이트.
영향 파일: 10개 (README 3개, RESEARCHER_ROLES, DISCUSSION_LOG 2개, docs 4개)

### 산출물
- `data/templates/human_review_sheet_v8.xlsx` — 최종 업데이트 (5개 시트, 검증 완료)
- `paper_a/data/02_screening/claude_screening_results.csv` — 1,280건
- `data/templates/create_masem_template.py` — adoption_composite 추가

---

## 향후 논의 사항

- [ ] R2, R3 확정 후 역할 문서 업데이트
- [ ] Pilot calibration 결과에 따른 코딩 매뉴얼 수정
- [ ] AI extraction pipeline 테스트 결과 검토
- [ ] Paper A OSF Preprint 등록 일정 확정
- [ ] IRB exempt 신청 여부 확인
- [ ] TIER3 500건 처리 방안 결정 (AI 스크리닝 결과 기반 exclude 여부)
