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

- **H1 (PI)**: Hosung You, Penn State College of Education
- **H2**: 박사과정생 1 (독립 코딩 담당)
- **H3**: 박사과정생 2 (QA spot-check 담당)

---

## 핵심 의사결정 기록

### 결정 1: Cohen's kappa vs. 다른 IRR 지표

**문제**: 3명의 human coder로 Cohen's kappa 사용 가능한가?
**결론**: Cohen's kappa는 2명 전용. 3명 이상은 Fleiss' kappa 또는 Krippendorff's alpha 사용.
**최종 설계**: 2명 human coder (H1, H2)가 독립 코딩 → Cohen's kappa + ICC(2,1) 사용. H3는 QA reviewer로 별도 역할.

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
- Human-first: H1+H2 독립 코딩 (blinded to AI) + AI 3개 모델 독립 추출
- Gold standard 확립 → AI 정확도 평가 (Paper B의 핵심 분석)
- Gold standard 데이터는 Paper A의 MASEM에도 활용

**Phase 2 (~200 studies) — 📗 Paper A 전용**:
- AI-first verification: AI consensus → 인간(H1, H2) 검증
- Phase 1에서 검증된 AI 성능을 기반으로, 효율적 코딩 방식 적용
- Paper B에서는 분석하지 않으며, Methods에서 간략 언급만

**Phase 3 (Phase 2의 10% spot-check) — 📗 Paper A 전용**:
- H3 (fresh eyes)가 독립적으로 spot-check
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

## 향후 논의 사항

- [ ] H2, H3 확정 후 역할 문서 업데이트
- [ ] Pilot calibration 결과에 따른 코딩 매뉴얼 수정
- [ ] AI extraction pipeline 테스트 결과 검토
- [ ] Paper A OSF Preprint 등록 일정 확정
- [ ] IRB exempt 신청 여부 확인
