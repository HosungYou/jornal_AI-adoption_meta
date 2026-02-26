# Journal Targeting Strategy: Paper B

## 1순위: Research Synthesis Methods (RSM)

### 저널 정보

| 항목 | 내용 |
|------|------|
| **출판사** | Wiley |
| **Impact Factor** | ~8.0 (2024) |
| **Scope** | Methods for systematic reviews and meta-analysis |
| **Review 기간** | 평균 3-4개월 |
| **Article types** | Original Article, Review, Tutorial |
| **Open Access** | Hybrid (OA option available) |
| **Word limit** | ~8,000 words (excluding references, tables, figures) |

### 적합성 분석

**강점**:
- AI-assisted data extraction 선행연구 다수 게재 (Gartlehner et al., 2024)
- Methods-focused 저널 → Paper B의 방법론 기여에 최적
- MASEM 관련 논문 게재 이력 있음
- Impact Factor 높음 → 높은 가시성

**고려사항**:
- 경쟁 심함 (rejection rate ~70%)
- 이미 AI extraction 논문 다수 → 차별화 필요
- MASEM-specific이라는 점이 핵심 차별화 포인트

### RSM 제출 전략

1. **Cover letter 핵심 메시지**: "First study to evaluate LLM-assisted coding specifically for MASEM correlation matrix extraction"
2. **차별화**: Multi-model consensus (기존 연구 대부분 단일 모델)
3. **PRISMA-trAIce 완벽 준수**: 이 저널이 이 가이드라인 발행에 참여했을 가능성
4. **Supplementary materials**: 프롬프트, 코드, 데이터 전체 OSF 링크

### 포맷 요구사항 (RSM)

| 항목 | 요구사항 |
|------|---------|
| Abstract | Structured (Background, Methods, Results, Conclusions) |
| Manuscript | Double-spaced, numbered lines |
| References | APA style 또는 Vancouver |
| Tables | Separate files preferred |
| Figures | High resolution (300 dpi) |
| Supplementary | Allowed, encouraged for methods papers |
| Data sharing | Required (OSF, Zenodo 등) |

---

## 2순위: JMIR AI

### 저널 정보

| 항목 | 내용 |
|------|------|
| **출판사** | JMIR Publications |
| **Impact Factor** | ~3.5-4.0 (newer journal) |
| **Scope** | AI applications in health and education |
| **Review 기간** | 평균 2-3개월 (faster than RSM) |
| **Article types** | Original Paper, Tutorial, Viewpoint |
| **Open Access** | Full OA (APC ~$2,500) |
| **Word limit** | ~6,000-8,000 words |

### 적합성 분석

**강점**:
- AI 방법론에 특화된 저널
- Open access → 높은 접근성
- Review 속도 빠름
- Education + AI 주제에 적합

**고려사항**:
- RSM 대비 낮은 IF
- Health 중심이지만 education도 수용
- 비교적 새로운 저널

### JMIR AI 제출 전략

1. **Cover letter**: AI + Education intersection 강조
2. **실무적 가이드라인 포함**: Practitioners를 위한 workflow recommendation
3. **TRIPOD-LLM 준수**: JMIR 계열이 TRIPOD에 우호적

---

## 제출 타임라인

```
Week 6 (Paper B v2.0 완성)
    │
    ▼
Week 7-8: 내부 검토 및 수정
    │
    ▼
Week 9: RSM 제출
    │
    ├── Accept → 완료
    ├── R&R → 수정 후 재제출 (4-6주)
    └── Reject → Week 13: JMIR AI 제출 (포맷 수정 후)
```

---

## Paper A와의 제출 전략

### 시차 관리

```
Paper B (방법론) → 먼저 제출 (Week 9)
    │
    ├── Paper A를 OSF Preprint으로 등록 (Week 8)
    │   └── Paper B에서 DOI로 cite
    │
    ▼
Paper A (MASEM) → 나중 제출 (Paper B accept 후 또는 동시)
    └── Computers & Education 타겟
```

### 인용 전략

Paper B에서 Paper A 인용 방식:

**Option 1 (OSF Preprint 등록 후)**:
```
You, H. (2026). AI adoption in education: A meta-analytic structural
equation model. OSF Preprints. https://doi.org/10.31219/osf.io/xxxxx
```

**Option 2 (Preprint 전)**:
```
You, H. (2026). AI adoption in education: A meta-analytic structural
equation model [Manuscript in preparation]. College of Education,
Pennsylvania State University.
```

---

## Reviewer 대응 예상

### 예상 질문 1: "왜 교육 분야 데이터로 방법론 평가?"
**대응**: MASEM은 correlation matrix 추출이 필수적이며, 교육 분야는 다양한 construct와 measurement instrument를 포함하여 방법론적 복잡성이 높음. 따라서 교육 분야 데이터는 AI 코딩 능력의 rigorous test를 제공.

### 예상 질문 2: "3개 모델 비교의 공정성"
**대응**: 동일 프롬프트, 동일 temperature(0), 동일 데이터 사용. 프롬프트를 모델별로 최적화하지 않은 것은 의도적 — 실제 연구자가 범용 프롬프트를 사용하는 시나리오 반영.

### 예상 질문 3: "100 studies가 충분한가?"
**대응**: 3,000 data elements (100 × 30 variables)는 기존 연구 대비 대규모. Gartlehner et al. (2024)은 22 SRs로 게재. Power analysis 제시.

### 예상 질문 4: "Gold standard의 신뢰도"
**대응**: 2-coder independent coding, blinded to AI, calibrated (pilot κ ≥ 0.80), IRR 보고 (κ ≥ 0.85 목표), discrepancy resolution protocol 문서화.
