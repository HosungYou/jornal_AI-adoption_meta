# 연구자 역할 분담 (Paper B)

## 연구팀 구성

| 역할 | 연구자 | 소속 | 코더 ID | Pair |
|------|--------|------|---------|------|
| **PI / Phase 1 Pair A / Phase 2 Pair C** | Hosung You | Penn State, College of Education | R1 | A, C |
| **Phase 1 Pair A / Phase 2 Pair D** | PhD Student 1 | [소속 기입] | R2 | A, D |
| **Phase 1 Pair B / Phase 2 Pair D** | PhD Student 2 | [소속 기입] | R3 | B, D |
| **Phase 1 Pair B / Phase 2 Pair C** | PhD Student 3 | [소속 기입] | R4 | B, C |

> 2026-04-24 protocol amendment: Phase 1 pairwise coding is complete. Phase 2
> uses rotated pairs: R1+R4 and R2+R3. This prevents the Phase 1 pair structure
> from carrying unchanged into the remaining extraction work.

---

## 스크리닝 단계 역할 (Option C: 2-Rater IRR + R1 Adjudicator)

> 최종 확정: 2026-02-26. v8 Excel (`data/templates/human_review_sheet_v8.xlsx`) 기준.

### R2 + R3: IRR 독립 코딩 (200건)

| 작업 | R2 (PhD 1) | R3 (PhD 2) |
|------|-----------|-----------|
| 시트① IRR_200건 독립 코딩 | ✅ 200건 | ✅ 200건 (동일 셋) |
| 상대방 코딩 접근 | ❌ Blinded | ❌ Blinded |
| Claude 사유 참고 | ✅ 참고 가능 | ✅ 참고 가능 |

**IRR 200건 구성**:
- 🔴 85건 TIER1 (include ↔ exclude 충돌)
- 🔵 36건 SPOT_CHECK (Auto-INCLUDE 10% 검증)
- 🟡 79건 TIER2 (include + uncertain)

### R1(PI): Adjudicator + 추가 코딩 (~221건)

| 작업 | R1 (PI) | 시트 |
|------|---------|------|
| Auto-INCLUDE spot-check | 86건 (36 IRR검증 + 50 R1검증) | 시트② |
| TIER2 잔여 추가 코딩 | 135건 | 시트③ |
| R2-R3 불일치 중재 | 불일치건 (IRR 후) | 시트① R1 칼럼 |
| 최종판단 확정 | 전체 | 시트① 최종 칼럼 |

### IRR 지표

| 지표 | 산출 대상 | 목표 |
|------|----------|------|
| Cohen's κ | R2 vs. R3 (I/X/U 3범주) | κ ≥ 0.85 |
| ICC(2,1) | 연속형 변수 보조 지표 | ICC ≥ 0.90 |

### 불일치 해결 절차

```
R2 == R3 → 채택 (일치)
R2 ≠ R3 → R1이 독립 검토 → 최종판단 기록
합의 불가 → R1(PI) 최종 결정권
```

> **참고**: 스크리닝 단계 역할은 기존 R2+R3 기반 설계 유지. 데이터 추출 단계에서 4-coder 2-pair 설계 적용 (아래 참조).

---

## 데이터 추출 단계 역할

### Phase 0: Calibration (3 days)
전체 4명이 동일 10 studies 코딩 → pair 간 일관성 확인

| 작업 | R1 (PI) | R2 (PhD 1) | R3 (PhD 2) | R4 (PhD 3) |
|------|---------|-----------|-----------|-----------|
| 10 studies 독립 코딩 | ✅ | ✅ | ✅ | ✅ |
| Calibration 미팅 참여 | ✅ | ✅ | ✅ | ✅ |
| 목표: κ ≥ 0.80 | ✅ | ✅ | ✅ | ✅ |

### Phase 1: Initial Human Reference Standard 구축 (2-Pair Design; completed)
독립 코딩 — 100 studies (50 per pair), blinded to AI

| 작업 | R1 (PI) | R2 (PhD 1) | R3 (PhD 2) | R4 (PhD 3) |
|------|---------|-----------|-----------|-----------|
| Pair A: 50 studies 독립 코딩 | ✅ | ✅ | — | — |
| Pair B: 50 studies 독립 코딩 | — | — | ✅ | ✅ |
| AI output 접근 | ❌ Blinded | ❌ Blinded | ❌ Blinded | ❌ Blinded |
| Pair 내 상대방 코딩 접근 | ❌ Blinded | ❌ Blinded | ❌ Blinded | ❌ Blinded |
| 코딩 시트 제출 | `pair_a/coder_r1/` | `pair_a/coder_r2/` | `pair_b/coder_r3/` | `pair_b/coder_r4/` |
| Pair A 불일치 중재 | — | — | ✅ (cross-pair adj.) | — |
| Pair B 불일치 중재 | ✅ (cross-pair adj.) | — | — | — |

### Phase 2: Rotated-Pair Human Coding (remaining eligible studies)

| 작업 | R1 (PI) | R2 (PhD 1) | R3 (PhD 2) | R4 (PhD 3) |
|------|---------|-----------|-----------|-----------|
| Pair C: independent coding | ✅ | — | — | ✅ |
| Pair D: independent coding | — | ✅ | ✅ | — |
| AI output 접근 | ❌ until adjudication | ❌ until adjudication | ❌ until adjudication | ❌ until adjudication |
| Pair 내 상대방 코딩 접근 | ❌ blinded | ❌ blinded | ❌ blinded | ❌ blinded |
| Pair C 불일치 중재 | — | ✅ primary | ✅ secondary if needed | — |
| Pair D 불일치 중재 | ✅ primary | — | — | ✅ secondary if needed |
| Post-adjudication LLM comparison | ✅ lead | support | support | support |

### Phase 3: Quality Assurance — Paper A 전용

| 작업 | R1 (PI) | R2 (PhD 1) | R3 (PhD 2) | R4 (PhD 3) |
|------|---------|-----------|-----------|-----------|
| Phase 2 spot-check (10%) | Cross-check | Cross-check | Cross-check | Cross-check |
| IRR 계산 및 분석 | ✅ | — | — | — |
| Data finalization | ✅ | — | — | — |

---

## 상세 책임

### R1: PI / Phase 1 Pair A / Phase 2 Pair C (Hosung You)
- **전체 프로젝트 총괄 및 coordination**
- 스크리닝: spot-check 86건 + 추가코딩 135건 + R2-R3 불일치 중재
- Phase 0: Calibration 참여 (10 studies)
- Phase 1: Pair A coder (50 studies 독립 코딩) + Pair B discrepancies adjudicator
- Phase 2: Pair C coder with R4; Pair D discrepancies primary adjudicator
- Phase 2 이후: adjudicated human reference 대비 LLM comparison, triage, substitution analysis lead
- IRR 계산 및 통계 분석
- 논문 작성 (전체)
- OSF 등록 및 데이터 관리
- AI extraction pipeline 실행 및 관리
- 프롬프트 설계 및 최적화

### R2: PhD Student 1 (Phase 1 Pair A / Phase 2 Pair D)
- 스크리닝: IRR 200건 독립 코딩
- Phase 0: Calibration 참여 (10 studies)
- Phase 1: Pair A coder (50 studies 독립 코딩)
- Phase 2: Pair D coder with R3; Pair C discrepancies primary adjudicator
- 코딩 매뉴얼 숙지 및 calibration 참여
- Discrepancy 논의 참여
- 논문 검토 및 피드백

### R3: PhD Student 2 (Phase 1 Pair B / Phase 2 Pair D)
- 스크리닝: IRR 200건 독립 코딩 (R2와 동일 셋)
- Phase 0: Calibration 참여 (10 studies)
- Phase 1: Pair B coder (50 studies 독립 코딩) + Pair A discrepancies adjudicator
- Phase 2: Pair D coder with R2; Pair C discrepancies secondary check if needed
- Discrepancy 논의 참여

### R4: PhD Student 3 (Phase 1 Pair B / Phase 2 Pair C)
- Phase 0: Calibration 참여 (10 studies)
- Phase 1: Pair B coder (50 studies 독립 코딩)
- Phase 2: Pair C coder with R1; Pair D discrepancies secondary check if needed
- 코딩 매뉴얼 숙지 및 calibration 참여
- Discrepancy 논의 참여

---

## Training Protocol

### Phase 0: Calibration (3 days, all 4 coders)

| 세션 | 내용 | 시간 | 참여자 |
|------|------|------|--------|
| Orientation | 코딩 매뉴얼 리뷰, 12 construct 정의, 변수 설명 | 2시간 | R1, R2, R3, R4 |
| Pilot Practice | 10 pilot studies 코딩 (전체 4명 동일 셋, Paper B sample 외) | 3시간 | R1, R2, R3, R4 |
| Calibration | Pilot IRR 확인 (all pairs), disagreement 논의, 규칙 명확화 | 1시간 | R1, R2, R3, R4 |

**Calibration 기준**: Pilot에서 κ ≥ 0.80 (categorical), ICC ≥ 0.85 (continuous) 달성 후 본 코딩 시작. 모든 coder pair 조합에서 기준 충족 필요.

---

## Blinding Protocol

```
Phase 1 (completed independent coding, 2-Pair Design):

Pair A (50 studies)              Pair B (50 studies)
┌─────────┐  ┌─────────┐       ┌─────────┐  ┌─────────┐    ┌──────────────────┐
│   R1    │  │   R2    │       │   R3    │  │   R4    │    │   AI (3 models)  │
│ (blind) │  │ (blind) │       │ (blind) │  │ (blind) │    │   (independent)  │
└────┬────┘  └────┬────┘       └────┬────┘  └────┬────┘    └────────┬─────────┘
     │            │                  │            │                   │
     ▼            ▼                  ▼            ▼                   ▼
  coder_r1/   coder_r2/          coder_r3/   coder_r4/        02_ai_extraction/
     │            │                  │            │                   │
     └─────┬──────┘                  └─────┬──────┘                   │
           ▼                               ▼                          │
     IRR (R1 vs R2)                  IRR (R3 vs R4)                   │
     (unblinding)                    (unblinding)                     │
           │                               │                          │
           ▼                               ▼                          │
     R3 adjudicates              R1 adjudicates                       │
     Pair A discrepancies        Pair B discrepancies                 │
           │                               │                          │
           └──────────────┬────────────────┘                          │
                          ▼                                           ▼
                   05_gold_standard/ ──────────── comparison ──── AI outputs
```

**Blinding 해제 시점**: Phase 1 코딩이 100% 완료되고 모든 코딩 시트가 제출된 후에만 pair 내 상호 결과 및 AI 결과 공개

```
Phase 2 (rotated independent coding):

Pair C                             Pair D
┌─────────┐  ┌─────────┐       ┌─────────┐  ┌─────────┐    ┌──────────────────┐
│   R1    │  │   R4    │       │   R2    │  │   R3    │    │ Primary LLM flow │
│ (blind) │  │ (blind) │       │ (blind) │  │ (blind) │    │  hidden until    │
└────┬────┘  └────┬────┘       └────┬────┘  └────┬────┘    │  adjudication    │
     │            │                  │            │         └────────┬─────────┘
     ▼            ▼                  ▼            ▼                  │
  coder_r1/   coder_r4/          coder_r2/   coder_r3/               │
     │            │                  │            │                  │
     └─────┬──────┘                  └─────┬──────┘                  │
           ▼                               ▼                         │
     IRR (R1 vs R4)                  IRR (R2 vs R3)                  │
           │                               │                         │
           ▼                               ▼                         │
     R2 adjudicates              R1 adjudicates                      │
     Pair C discrepancies        Pair D discrepancies                │
           │                               │                         │
           └──────────────┬────────────────┘                         │
                          ▼                                          ▼
                  Phase 2 adjudicated human reference ────── LLM comparison
```

**Phase 2 blinding 해제 시점**: Pair C/D의 독립 코딩 제출 및 cross-pair
adjudication이 끝난 뒤에만 LLM output을 공개한다.

---

## Communication Protocol

- **주간 미팅**: 매주 1회 (30분), 진행 상황 확인
- **Coding 질문**: 코딩 중 의문사항은 개별 메모 → 주간 미팅에서 논의 (pair 내 상대방 답변 참고 불가)
- **긴급 질문**: PI에게 직접 문의 가능 (단, PI는 모든 코더에게 같은 답변 제공하여 형평성 유지)
- **Discrepancy Resolution**: Phase 1 완료 후 face-to-face 미팅으로 진행

---

## 윤리 및 이해충돌

- 모든 연구자는 이해충돌 없음을 선언
- IRB 승인: [해당 시 기입 — secondary data analysis로 exempt 가능성]
- AI 사용 투명성: 모든 AI involvement는 Methods에 보고
- 데이터: OSF에 공개 (개인정보 미포함)
