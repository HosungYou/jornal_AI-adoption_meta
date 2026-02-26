#!/usr/bin/env python3
"""
human_review_sheet_v5.xlsx 생성 — 단일 시트 구조

구조:
  - 1개 데이터 시트: 전체 1,457건 (AI 3모델 합의 + 인간 3리뷰어)
  - 1개 가이드 시트: 코딩 규칙 + 리뷰어 역할 + 제외코드

AI 컬럼: Codex | Gemini | Claude Sonnet 4.6 | AI 합의
인간 컬럼: R1(PI) 판단/코드/메모 | R2 판단/코드/메모 | R3(중재) 판단/메모
최종: 최종판단 | 최종코드
"""

import csv
import json
import os
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
QUEUE_CSV = os.path.join(REPO_ROOT, "data", "03_screening", "human_review_queue.csv")
V4_PARSED = "/tmp/v4_parsed.json"
OUTPUT = os.path.join(REPO_ROOT, "data", "templates", "human_review_sheet_v5.xlsx")

# ── 스타일 ──
THIN = Border(*(Side(style="thin", color="D9D9D9"),) * 4)
S_BASE = {"fill": PatternFill("solid", fgColor="2F5496"),
           "font": Font("맑은 고딕", bold=True, color="FFFFFF", size=10)}
S_AI   = {"fill": PatternFill("solid", fgColor="8DB4E2"),
           "font": Font("맑은 고딕", bold=True, color="1F3864", size=10)}
S_R1   = {"fill": PatternFill("solid", fgColor="FFF2CC"),
           "font": Font("맑은 고딕", bold=True, color="BF8F00", size=10)}
S_R2   = {"fill": PatternFill("solid", fgColor="FCE4D6"),
           "font": Font("맑은 고딕", bold=True, color="C55A11", size=10)}
S_R3   = {"fill": PatternFill("solid", fgColor="E2EFDA"),
           "font": Font("맑은 고딕", bold=True, color="375623", size=10)}
S_FINAL = {"fill": PatternFill("solid", fgColor="D5A6BD"),
            "font": Font("맑은 고딕", bold=True, color="5B2C6F", size=10)}
DATA_FONT = Font("맑은 고딕", size=9)
AI_FONT = Font("맑은 고딕", size=9, color="666666")

EXCLUSION_CODES = [
    "E-FT1", "E-FT2", "E-FT3", "E-FT4",
    "E-FT5", "E-FT6", "E-FT7", "E-FT8",
]

# v4 판단값 표준화
def std(val):
    v = (val or "").strip()
    if v in ("x", "X"): return "X"
    if v in ("o", "O"): return "O"
    if v == "?": return "?"
    if len(v) > 3: return ""
    return v


def hdr(ws, row, col, text, style):
    c = ws.cell(row=row, column=col, value=text)
    c.fill = style["fill"]
    c.font = style["font"]
    c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    c.border = THIN


def dat(ws, row, col, val, font=DATA_FONT):
    c = ws.cell(row=row, column=col, value=val)
    c.font = font
    c.border = THIN
    c.alignment = Alignment(vertical="top", wrap_text=True)
    return c


def main():
    # ── 데이터 로드 ──
    # CSV: Codex + Gemini 데이터
    csv_by_id = {}
    with open(QUEUE_CSV, "r") as f:
        for row in csv.DictReader(f):
            csv_by_id[row["record_id"]] = row

    # v4 Excel: Claude + 기존 리뷰어 데이터
    v4_by_id = {}
    with open(V4_PARSED, "r") as f:
        data = json.load(f)
    for cat in ("include", "conflict", "uncertain"):
        for rec in data[cat]:
            rid = rec.get("A", "")
            if rid:
                v4_by_id[rid] = rec

    # ── 레코드 병합 (정렬: include → conflict → uncertain) ──
    ordered_ids = []
    for cat in ("include", "conflict", "uncertain"):
        for rec in data[cat]:
            rid = rec.get("A", "")
            if rid and rid not in ordered_ids:
                ordered_ids.append(rid)

    print(f"Records: {len(ordered_ids)}")

    # ── 워크북 생성 ──
    wb = Workbook()
    wb.remove(wb.active)

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # Sheet 1: 스크리닝 (단일 시트)
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    ws = wb.create_sheet("스크리닝")

    headers = [
        # 기본 (파란)
        ("ID",     S_BASE, 12),
        ("제목",    S_BASE, 55),
        ("연도",    S_BASE, 6),
        ("초록",    S_BASE, 15),
        # AI (하늘)
        ("Codex",           S_AI, 10),
        ("Gemini",          S_AI, 10),
        ("Claude\nSonnet 4.6", S_AI, 12),
        ("AI 합의",          S_AI, 10),
        # R1-PI (노랑)
        ("R1(PI)\n판단", S_R1, 10),
        ("R1\n코드",     S_R1, 10),
        ("R1\n메모",     S_R1, 18),
        # R2 (주황)
        ("R2\n판단", S_R2, 10),
        ("R2\n코드", S_R2, 10),
        ("R2\n메모", S_R2, 18),
        # R3-중재 (초록)
        ("R3(중재)\n판단", S_R3, 10),
        ("R3\n메모",       S_R3, 18),
        # 최종 (보라)
        ("최종판단", S_FINAL, 10),
        ("최종코드", S_FINAL, 10),
    ]

    for i, (text, style, width) in enumerate(headers, 1):
        hdr(ws, 1, i, text, style)
        ws.column_dimensions[get_column_letter(i)].width = width

    # ── 데이터 쓰기 ──
    for row_idx, rid in enumerate(ordered_ids, 2):
        csv_rec = csv_by_id.get(rid, {})
        v4_rec = v4_by_id.get(rid, {})

        col = 1
        # 기본
        dat(ws, row_idx, col, rid); col += 1
        dat(ws, row_idx, col, v4_rec.get("D", csv_rec.get("title", ""))); col += 1
        year_val = v4_rec.get("G", csv_rec.get("year", ""))
        try:
            year_val = int(float(year_val))
        except (ValueError, TypeError):
            pass
        dat(ws, row_idx, col, year_val); col += 1
        dat(ws, row_idx, col, csv_rec.get("abstract", v4_rec.get("F", ""))); col += 1

        # AI 3모델
        dat(ws, row_idx, col, csv_rec.get("screen_decision_codex", ""), AI_FONT); col += 1
        dat(ws, row_idx, col, csv_rec.get("screen_decision_gemini", ""), AI_FONT); col += 1
        claude_val = v4_rec.get("Q", "")
        # Claude 값 표준화: EXCLUDE→exclude, KEEP→include, REVIEW→uncertain
        cl_map = {"EXCLUDE": "exclude", "KEEP - TAM/UTAUT 구인 있음": "include",
                   "REVIEW - 판단 불가 (full-text 필요)": "uncertain"}
        claude_std = cl_map.get(claude_val, claude_val.lower() if claude_val else "")
        dat(ws, row_idx, col, claude_std, AI_FONT); col += 1

        # AI 합의 (3모델 majority)
        votes = []
        for v in [csv_rec.get("screen_decision_codex", ""),
                   csv_rec.get("screen_decision_gemini", ""),
                   claude_std]:
            if v in ("include", "exclude", "uncertain"):
                votes.append(v)
        if len(votes) >= 2:
            from collections import Counter as Ctr
            vc = Ctr(votes)
            majority = vc.most_common(1)[0]
            if majority[1] >= 2:
                consensus = majority[0]
            else:
                consensus = "conflict"
        elif len(votes) == 1:
            consensus = votes[0] + " (1-model)"
        else:
            consensus = ""
        dat(ws, row_idx, col, consensus, AI_FONT); col += 1

        # R1(PI) — 기존 리뷰어1 데이터 보존
        dat(ws, row_idx, col, std(v4_rec.get("S", ""))); col += 1
        dat(ws, row_idx, col, v4_rec.get("T", "")); col += 1
        dat(ws, row_idx, col, v4_rec.get("U", "")); col += 1

        # R2 — 기존 리뷰어2 데이터 보존
        dat(ws, row_idx, col, std(v4_rec.get("V", ""))); col += 1
        dat(ws, row_idx, col, v4_rec.get("W", "")); col += 1
        dat(ws, row_idx, col, v4_rec.get("X", "")); col += 1

        # R3(중재), 최종 — 비워둠
        for _ in range(4):
            dat(ws, row_idx, col, ""); col += 1

    n_rows = len(ordered_ids) + 1

    # ── 데이터 검증 ──
    dv_decision = DataValidation(type="list", formula1='"O,X,?"', allow_blank=True,
                                  errorTitle="입력 오류", error="O/X/? 중 선택")
    dv_decision.prompt = "O=포함, X=제외, ?=불확실"
    ws.add_data_validation(dv_decision)

    dv_code = DataValidation(type="list",
                              formula1=f'"{",".join(EXCLUSION_CODES)}"',
                              allow_blank=True)
    ws.add_data_validation(dv_code)

    dv_final = DataValidation(type="list", formula1='"Include,Exclude,Uncertain"',
                               allow_blank=True)
    ws.add_data_validation(dv_final)

    # 판단 드롭다운 적용: R1(9), R2(12), R3(15)
    for decision_col in [9, 12, 15]:
        letter = get_column_letter(decision_col)
        dv_decision.add(f"{letter}2:{letter}{n_rows}")
    # 코드 드롭다운: R1(10), R2(13)
    for code_col in [10, 13]:
        letter = get_column_letter(code_col)
        dv_code.add(f"{letter}2:{letter}{n_rows}")
    # 최종판단 드롭다운: col 17
    f_letter = get_column_letter(17)
    dv_final.add(f"{f_letter}2:{f_letter}{n_rows}")
    # 최종코드
    fc_letter = get_column_letter(18)
    dv_code.add(f"{fc_letter}2:{fc_letter}{n_rows}")

    # 고정 틀, 필터
    ws.freeze_panes = "C2"
    ws.auto_filter.ref = f"A1:{get_column_letter(18)}{n_rows}"
    ws.row_dimensions[1].height = 35

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # Sheet 2: 코딩가이드
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    gs = wb.create_sheet("코딩가이드")
    bf = Font("맑은 고딕", bold=True, size=11)
    nf = Font("맑은 고딕", size=10)
    tf = Font("맑은 고딕", bold=True, size=13, color="FFFFFF")

    # 제목
    c = gs.cell(row=1, column=1, value="스크리닝 코딩 가이드 & 리뷰어 역할")
    c.font = tf
    c.fill = PatternFill("solid", fgColor="2F5496")
    gs.merge_cells("A1:E1")

    # ── 리뷰어 역할 ──
    r = 3
    gs.cell(row=r, column=1, value="1. 리뷰어 역할 및 순서").font = bf
    r += 1

    roles = [
        ("순서", "담당", "범위", "할 일", "목적"),
        ("Step 1", "Claude Sonnet 4.6",
         "1,457건 전체",
         "미평가 1,238건 AI 스크리닝 완료",
         "3-AI 합의 완성"),
        ("Step 2", "R1 — PI (유호성)",
         "1,457건 전체",
         "AI 합의 확인 + 독립 판단 (O/X/?)",
         "전수 인간 검토"),
        ("Step 3", "R2 — PhD학생",
         "계층 무작위 20% (~290건)",
         "R1과 독립적으로 판단 (블라인드)",
         "IRR (Cohen's κ) 산출"),
        ("Step 4", "IRR 확인",
         "R1∩R2 겹치는 ~290건",
         "κ ≥ 0.80이면 통과, 미달 시 논의 후 재검토",
         "신뢰도 확보"),
        ("Step 5", "R3 — 중재자 (지도교수/공저자)",
         "R1-R2 불일치 건만",
         "불일치 건 최종 판단",
         "불일치 해결"),
        ("Step 6", "PI",
         "전체",
         "최종판단·최종코드 컬럼 확정 → convert_screening.py 실행",
         "데이터 확정"),
    ]
    for i, row_data in enumerate(roles):
        for j, val in enumerate(row_data):
            c = gs.cell(row=r + i, column=j + 1, value=val)
            c.font = bf if i == 0 else nf
            c.border = THIN

    r += len(roles) + 2

    # ── 판단 입력 ──
    gs.cell(row=r, column=1, value="2. 판단 입력값").font = bf
    r += 1
    for code, label, desc in [
        ("O", "포함(Include)", "AI 채택/수용 TAM/UTAUT 구인 측정한 실증 양적 연구"),
        ("X", "제외(Exclude)", "아래 제외코드 중 하나에 해당"),
        ("?", "불확실(Uncertain)", "초록만으로 판단 불가, full-text 확인 필요"),
    ]:
        gs.cell(row=r, column=1, value=code).font = bf
        gs.cell(row=r, column=2, value=label).font = nf
        gs.cell(row=r, column=3, value=desc).font = nf
        r += 1

    r += 1
    gs.cell(row=r, column=1, value="3. 제외코드").font = bf
    r += 1
    code_desc = {
        "E-FT1": "비실증 연구 (리뷰, 이론, 메타분석, 논평)",
        "E-FT2": "TAM/UTAUT 구인 없음 (채택/수용 측정 안 함)",
        "E-FT3": "AI가 초점 기술이 아님 (일반 ICT, 로봇, IoT 등)",
        "E-FT4": "교육 맥락 아님 (기업, 의료, 공공 등)",
        "E-FT5": "상관/경로계수 추출 불가 (순수 질적, 실험 비교만)",
        "E-FT6": "중복 데이터 (동일 표본의 다른 논문)",
        "E-FT7": "전문(full-text) 접근 불가",
        "E-FT8": "영어 아님",
    }
    for code, desc in code_desc.items():
        gs.cell(row=r, column=1, value=code).font = bf
        gs.cell(row=r, column=2, value=desc).font = nf
        r += 1

    r += 1
    gs.cell(row=r, column=1, value="4. AI 합의 규칙").font = bf
    r += 1
    for rule in [
        "3모델 중 2개 이상 동일 판단 → 다수결 (majority)",
        "3모델 모두 다른 판단 → conflict",
        "Claude 미평가 시 → Codex+Gemini 2모델 합의 적용",
        "AI 합의는 참조용 — 최종 판단은 인간 리뷰어가 결정",
    ]:
        gs.cell(row=r, column=1, value=rule).font = nf
        r += 1

    r += 1
    gs.cell(row=r, column=1, value="5. 포함 기준 (Inclusion Criteria)").font = bf
    r += 1
    for crit in [
        "① AI(인공지능)가 초점 기술 (ChatGPT, ITS, 생성형 AI 등)",
        "② 교육 맥락 (K-12, 대학, 성인교육 — 학생/교수자/행정가)",
        "③ TAM/UTAUT 구인 측정 (PE, EE, SI, FC, BI, Trust, Anxiety 등)",
        "④ 실증적 양적 연구 (상관계수 또는 표준화 경로계수 추출 가능)",
        "⑤ 2015-2025년 출판",
        "⑥ 영어 논문",
    ]:
        gs.cell(row=r, column=1, value=crit).font = nf
        r += 1

    # 열 너비
    for col, w in [(1, 18), (2, 22), (3, 30), (4, 45), (5, 20)]:
        gs.column_dimensions[get_column_letter(col)].width = w

    # ── 저장 ──
    wb.save(OUTPUT)
    print(f"Saved: {OUTPUT}")
    print(f"Sheets: {wb.sheetnames}")

    # 통계
    r1_filled = sum(1 for rid in ordered_ids if std(v4_by_id.get(rid, {}).get("S", "")))
    r2_filled = sum(1 for rid in ordered_ids if std(v4_by_id.get(rid, {}).get("V", "")))
    claude_filled = sum(1 for rid in ordered_ids if v4_by_id.get(rid, {}).get("Q", "").strip())
    print(f"\nData preserved: Claude={claude_filled}, R1={r1_filled}, R2={r2_filled}")
    print(f"Claude 미평가: {len(ordered_ids) - claude_filled}건 → Step 1에서 완료 필요")


if __name__ == "__main__":
    main()
