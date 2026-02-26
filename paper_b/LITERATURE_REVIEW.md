# Literature Review: AI-Assisted Data Extraction in Systematic Reviews

## 개요

Paper B의 Introduction 및 Discussion 작성을 위한 선행연구 정리.
2023-2026년 발표된 AI-assisted systematic review/meta-analysis 방법론 연구.

---

## 1. AI-Assisted Data Extraction 실증 연구

### 1.1 Gartlehner et al. (2024)

- **제목**: Data extraction for evidence synthesis using a large language model
- **게재**: Research Synthesis Methods
- **내용**: GPT-4를 사용한 22개 systematic review의 데이터 추출
- **방법**: AI 추출 → 100% human verification
- **결과**: 높은 정확도, 특히 bibliographic data에서 우수
- **시사점**: AI-assisted extraction이 실현 가능함을 최초로 대규모 입증

### 1.2 Gartlehner et al. (2025)

- **제목**: (확장 연구)
- **게재**: Research Synthesis Methods (expected)
- **내용**: 2024년 연구의 확장 및 반복 검증
- **방법**: 동일한 100% human verification 프로토콜
- **시사점**: 재현성 확인

### 1.3 Jensen et al. (2025)

- **제목**: Multi-LLM comparison for systematic review data extraction
- **내용**: 178 studies에 대해 다중 LLM 비교
- **방법**: Multiple LLM 모델 비교 평가
- **결과**: 모델 간 성능 차이 존재
- **시사점**: Multi-model approach의 근거 제공

### 1.4 Khan et al. (2025)

- **제목**: LLM-assisted data extraction for meta-analysis
- **내용**: 메타분석 데이터 추출에 LLM 활용
- **방법**: Full human verification
- **시사점**: 메타분석 특화 추출의 가능성

### 1.5 Campos et al. (2024)

- **제목**: Guidelines for using LLMs in systematic review data extraction
- **내용**: SR 데이터 추출에서의 LLM 활용 가이드라인 제시
- **시사점**: 방법론적 프레임워크 제공

### 1.6 Wang et al. (2024)

- **제목**: LLMs in meta-analysis
- **내용**: 메타분석에서의 LLM 활용 현황
- **시사점**: 현 시점 AI 활용의 장점과 한계 정리

### 1.7 Alshami et al. (2023)

- **제목**: ChatGPT for systematic review automation
- **내용**: ChatGPT를 사용한 SR 자동화 탐색
- **시사점**: 초기 탐색적 연구로서의 가치

---

## 2. 보고 가이드라인 및 프레임워크

### 2.1 PRISMA-trAIce (2025)

- **제목**: PRISMA-trAIce: A 14-item checklist for reporting AI in evidence synthesis
- **내용**: AI를 활용한 evidence synthesis의 투명한 보고를 위한 14개 항목
- **핵심 항목**:
  1. AI tool identification (name, version, access date)
  2. Prompt documentation
  3. Human oversight description
  4. Error handling procedures
  5. Reproducibility measures
- **Paper B 적용**: checklists/PRISMA_trAIce_checklist.md에서 항목별 compliance 추적

### 2.2 TRIPOD-LLM (Collins et al., 2025)

- **제목**: TRIPOD-LLM: Reporting guideline for studies using LLMs
- **게재**: Nature Medicine
- **내용**: LLM 기반 연구의 보고 가이드라인
- **핵심**: 모델 세부사항, 프롬프트, 평가 방법 투명 보고
- **Paper B 적용**: checklists/TRIPOD_LLM_checklist.md에서 compliance 추적

### 2.3 RAISE Framework (2025)

- **발행기관**: Cochrane, Campbell Collaboration, JBI, CEE (공동)
- **제목**: Responsible AI in Systematic Evidence synthesis
- **핵심 원칙**:
  1. AI는 도구로서만 사용 (의사결정 주체는 인간)
  2. 완전한 투명성 (프롬프트, 설정, 결과 공개)
  3. 인간 감독 필수 (AI 결과의 독립적 검증)
  4. 재현 가능성 보장
  5. 편향 인식 및 대응
- **Paper B 적용**: Methods에서 RAISE 준수 명시

---

## 3. 관련 방법론 문헌

### 3.1 MASEM 방법론

| 문헌 | 핵심 기여 |
|------|----------|
| Cheung (2015) | metaSEM R package, two-stage MASEM |
| Jak & Cheung (2020) | MASEM 실무 가이드 |
| Viswesvaran & Ones (1995) | Meta-analytic path analysis 초기 방법 |

### 3.2 IRR 방법론

| 문헌 | 핵심 기여 |
|------|----------|
| Cohen (1960) | Cohen's kappa 원저 |
| Gwet (2008, 2014) | AC1/AC2 (kappa paradox 해결) |
| Shrout & Fleiss (1979) | ICC 분류 체계 |
| Krippendorff (2011) | Krippendorff's alpha |
| Hallgren (2012) | IRR 계산 실무 튜토리얼 |

### 3.3 β → r 변환

| 문헌 | 핵심 기여 |
|------|----------|
| Peterson & Brown (2005) | β → r 변환 공식: r ≈ β + .05λ |
| Roth et al. (2018) | 변환의 한계 및 주의사항 |
| Aloe (2015) | 변환 방법 비교 |

---

## 4. Gap Analysis: 본 연구의 기여

### 기존 연구의 한계

| 한계 | 기존 연구 | Paper B의 대응 |
|------|----------|---------------|
| **Single model** | 대부분 GPT-4 단일 모델 | 3개 모델 비교 |
| **Non-MASEM** | General SR extraction | MASEM-specific coding (correlation matrix) |
| **Small sample** | 22 SRs (Gartlehner) | 100 studies, 3,000 data elements |
| **No consensus** | 개별 모델 평가만 | Multi-model consensus 전략 평가 |
| **Limited variable types** | Bibliographic 중심 | 30개 변수 (4개 모듈) 포괄 |
| **No workflow optimization** | 정확도 보고만 | Cost-effectiveness 분석 포함 |
| **Older models** | GPT-3.5, GPT-4 | 최신 모델 (2025-2026) |

### Paper B의 독자적 기여 (Unique Contributions)

1. **MASEM-specific AI coding evaluation**: Correlation matrix 추출의 AI 정확도를 최초로 평가
2. **Three-model comparative framework**: 3개 LLM의 체계적 비교 + consensus 전략
3. **Gold standard rigor**: 2-coder independent coding + blinding + full IRR
4. **Workflow optimization**: 다양한 human-AI collaboration 시나리오의 efficiency 비교
5. **Comprehensive reporting**: PRISMA-trAIce + TRIPOD-LLM + RAISE 동시 준수
6. **Full transparency**: 프롬프트, 코드, 데이터 전체 OSF 공개

---

## 5. Key References (Paper B 인용 예정)

```
Alshami, A., et al. (2023). ChatGPT for systematic review automation.
Campos, L., et al. (2024). Guidelines for LLMs in SR data extraction.
Cheung, M. W.-L. (2015). Meta-analytic structural equation modeling. Wiley.
Cohen, J. (1960). A coefficient of agreement for nominal scales.
Collins, G. S., et al. (2025). TRIPOD-LLM. Nature Medicine.
Gartlehner, G., et al. (2024). Data extraction using LLM. Research Synthesis Methods.
Gartlehner, G., et al. (2025). Extended LLM extraction validation.
Gwet, K. L. (2014). Handbook of inter-rater reliability (4th ed.).
Hallgren, K. A. (2012). Computing inter-rater reliability. Tutorials in Quantitative Methods.
Jensen, A., et al. (2025). Multi-LLM comparison for SR data extraction.
Khan, S., et al. (2025). LLM-assisted data extraction for meta-analysis.
Krippendorff, K. (2011). Computing Krippendorff's alpha-reliability.
Peterson, R. A., & Brown, S. P. (2005). On the use of beta coefficients.
PRISMA-trAIce Consortium. (2025). Reporting AI in evidence synthesis.
RAISE Consortium. (2025). Responsible AI in systematic evidence synthesis.
Shrout, P. E., & Fleiss, J. L. (1979). Intraclass correlations.
Wang, J., et al. (2024). LLMs in meta-analysis.
You, H. (2026). AI adoption in education: A meta-analytic structural equation model. OSF Preprint.
```
