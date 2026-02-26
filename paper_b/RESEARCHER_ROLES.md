# 연구자 역할 분담 (Paper B)

## 연구팀 구성

| 역할 | 연구자 | 소속 | 코더 ID |
|------|--------|------|---------|
| **PI / Human Coder 1** | Hosung You | Penn State, College of Education | H1 |
| **Human Coder 2** | PhD Student 1 | [소속 기입] | H2 |
| **QA Reviewer** | PhD Student 2 | [소속 기입] | H3 |

---

## Phase별 역할

### Phase 1: Gold Standard 구축 (Week 2-3)
독립 코딩 — 100 studies, blinded to AI

| 작업 | H1 (PI) | H2 (PhD 1) | H3 (PhD 2) |
|------|---------|-----------|-----------|
| 100 studies 독립 코딩 | ✅ 전체 | ✅ 전체 | — |
| AI output 접근 | ❌ Blinded | ❌ Blinded | — |
| 상대방 코딩 접근 | ❌ Blinded | ❌ Blinded | — |
| 코딩 시트 제출 | `coder1_PI/` | `coder2_phd1/` | — |

**핵심 규칙**:
- H1과 H2는 코딩 기간 동안 서로의 결과를 볼 수 없음
- AI extraction 결과에 대한 접근 차단
- 각자 별도의 컴퓨터/계정에서 작업
- 코딩 완료 후 동시에 제출

### Phase 2: AI-First Verification (Week 3-5)
나머지 ~200 studies, AI consensus 검증

| 작업 | H1 (PI) | H2 (PhD 1) | H3 (PhD 2) |
|------|---------|-----------|-----------|
| AI consensus 검증 | ✅ ~100 studies | ✅ ~100 studies | — |
| 원문 대조 확인 | ✅ | ✅ | — |
| Discrepancy 기록 | ✅ | ✅ | — |
| 최종 값 결정 | ✅ (본인 담당분) | ✅ (본인 담당분) | — |

### Phase 3: Quality Assurance (Week 5-6)

| 작업 | H1 (PI) | H2 (PhD 1) | H3 (PhD 2) |
|------|---------|-----------|-----------|
| Phase 2 spot-check (10%) | — | — | ✅ ~20 studies |
| Discrepancy resolution | ✅ (최종 결정) | — | — |
| IRR 계산 | ✅ | — | — |
| Data finalization | ✅ | — | — |

---

## 상세 책임

### H1: PI (Hosung You)
- **전체 프로젝트 총괄**
- Phase 1: 100 studies 독립 코딩 (Human Coder 1)
- Phase 2: ~100 studies AI consensus 검증
- Phase 3: Discrepancy resolution 최종 결정권
- IRR 계산 및 통계 분석
- 논문 작성 (전체)
- OSF 등록 및 데이터 관리
- AI extraction pipeline 실행 및 관리
- 프롬프트 설계 및 최적화

### H2: PhD Student 1
- Phase 1: 100 studies 독립 코딩 (Human Coder 2)
- Phase 2: ~100 studies AI consensus 검증
- 코딩 매뉴얼 숙지 및 calibration 참여
- Discrepancy 논의 참여
- 논문 검토 및 피드백

### H3: PhD Student 2
- Phase 3: 10% random spot-check (~20 studies)
- Fresh eyes — Phase 1-2에 참여하지 않아 편향 없음
- QA 결과 보고서 작성
- Error rate 계산 및 보고

---

## Training Protocol

### Phase 1 시작 전 (Week 1)

| 세션 | 내용 | 시간 | 참여자 |
|------|------|------|--------|
| Orientation | 코딩 매뉴얼 리뷰, 12 construct 정의, 변수 설명 | 2시간 | H1, H2, H3 |
| Pilot Practice | 10 pilot studies 코딩 (Paper B sample 외) | 3시간 | H1, H2 |
| Calibration | Pilot IRR 확인, disagreement 논의, 규칙 명확화 | 1시간 | H1, H2 |

**Calibration 기준**: Pilot에서 κ ≥ 0.80 (categorical), ICC ≥ 0.85 (continuous) 달성 후 본 코딩 시작

### H3 Training (Week 4)

| 세션 | 내용 | 시간 |
|------|------|------|
| QA Orientation | Spot-check 절차, 코딩 매뉴얼 핵심 요약 | 1시간 |
| Practice | 5 studies QA 연습 | 1시간 |

---

## Blinding Protocol

```
Phase 1 (독립 코딩):
┌─────────┐    ┌─────────┐    ┌──────────────────┐
│   H1    │    │   H2    │    │   AI (3 models)  │
│ (blind) │    │ (blind) │    │   (independent)  │
└────┬────┘    └────┬────┘    └────────┬─────────┘
     │              │                   │
     ▼              ▼                   ▼
  coder1_PI/    coder2_phd1/     02_ai_extraction/
     │              │                   │
     └──────┬───────┘                   │
            ▼                           │
     IRR Calculation                    │
     (unblinding)                       │
            │                           │
            ▼                           ▼
     05_gold_standard/ ←── comparison ── AI outputs
```

**Blinding 해제 시점**: Phase 1 코딩이 100% 완료되고 모든 코딩 시트가 제출된 후에만 H1-H2 상호 결과 및 AI 결과 공개

---

## Communication Protocol

- **주간 미팅**: 매주 1회 (30분), 진행 상황 확인
- **Coding 질문**: 코딩 중 의문사항은 개별 메모 → 주간 미팅에서 논의 (상대방 답변 참고 불가)
- **긴급 질문**: PI에게 직접 문의 가능 (단, PI는 H2에게 같은 답변 제공하여 형평성 유지)
- **Discrepancy Resolution**: Phase 1 완료 후 face-to-face 미팅으로 진행

---

## 윤리 및 이해충돌

- 모든 연구자는 이해충돌 없음을 선언
- IRB 승인: [해당 시 기입 — secondary data analysis로 exempt 가능성]
- AI 사용 투명성: 모든 AI involvement는 Methods에 보고
- 데이터: OSF에 공개 (개인정보 미포함)
