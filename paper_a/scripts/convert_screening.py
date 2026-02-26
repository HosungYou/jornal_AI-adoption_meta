#!/usr/bin/env python3
"""
human_review_sheet_v5.xlsx (단일 시트) → CSV 변환 + IRR 산출

사용법:
    python3 convert_screening.py               # 전체 변환
    python3 convert_screening.py --dry-run      # 미리보기
    python3 convert_screening.py --irr-only     # IRR만 산출
"""

import argparse
import csv
import os
import sys
from collections import Counter
from openpyxl import load_workbook

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
EXCEL = os.path.join(REPO, "data", "templates", "human_review_sheet_v5.xlsx")
DUAL_CSV = os.path.join(REPO, "data", "03_screening", "screening_ai_dual.csv")
QUEUE_CSV = os.path.join(REPO, "data", "03_screening", "human_review_queue.csv")
OUT_DIR = os.path.join(REPO, "paper_a", "data", "02_screening", "human_verification")

D_MAP = {"O": "include", "X": "exclude", "?": "uncertain",
         "Include": "include", "Exclude": "exclude", "Uncertain": "uncertain", "": ""}


def read_sheet(excel_path):
    """zipfile로 직접 파싱 — openpyxl보다 10x 빠름"""
    import zipfile
    import xml.etree.ElementTree as ET

    ns = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
    records = []

    with zipfile.ZipFile(excel_path, "r") as z:
        tree = ET.parse(z.open("xl/worksheets/sheet1.xml"))
        rows = tree.findall(f".//{{{ns}}}row")

        for row_el in rows[1:]:  # skip header
            cells = {}
            for cell in row_el.findall(f"{{{ns}}}c"):
                ref = cell.get("r", "")
                col = "".join(c for c in ref if c.isalpha())
                is_el = cell.find(f"{{{ns}}}is")
                v_el = cell.find(f"{{{ns}}}v")
                val = ""
                if is_el is not None:
                    t = is_el.find(f"{{{ns}}}t")
                    if t is not None:
                        val = (t.text or "").strip()
                elif v_el is not None:
                    val = (v_el.text or "").strip()
                if val:
                    cells[col] = val

            rid = cells.get("A", "")
            if not rid.startswith("REC_"):
                continue
            records.append({
                "id": rid,
                "r1": cells.get("I", ""),       # R1(PI) 판단
                "r1_code": cells.get("J", ""),   # R1 코드
                "r1_memo": cells.get("K", ""),    # R1 메모
                "r2": cells.get("L", ""),         # R2 판단
                "r2_code": cells.get("M", ""),    # R2 코드
                "r2_memo": cells.get("N", ""),    # R2 메모
                "r3": cells.get("O", ""),         # R3(중재) 판단
                "final": cells.get("Q", ""),      # 최종판단
                "final_code": cells.get("R", ""), # 최종코드
            })
    return records


def cohens_kappa(pairs):
    if not pairs:
        return None, {}
    n = len(pairs)
    cats = sorted(set(d for p in pairs for d in p))
    mx = Counter(pairs)
    p_o = sum(mx[(c, c)] for c in cats) / n
    p_e = sum(
        (sum(1 for a, _ in pairs if a == c) / n) *
        (sum(1 for _, b in pairs if b == c) / n)
        for c in cats
    )
    k = (p_o - p_e) / (1 - p_e) if p_e < 1 else 1.0
    return round(k, 3), {"n": n, "agree_pct": round(p_o * 100, 1), "kappa": round(k, 3)}


def update_csv(path, by_id, dry_run):
    if not os.path.exists(path):
        return 0
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames
        rows = list(reader)
    updated = 0
    for row in rows:
        rec = by_id.get(row.get("record_id", ""))
        if not rec:
            continue
        d1 = D_MAP.get(rec["r1"], "")
        d2 = D_MAP.get(rec["r2"], "")
        fd = D_MAP.get(rec["final"], "")
        if d1 or d2 or fd:
            row["human1_decision"] = d1
            row["human2_decision"] = d2
            row["adjudicated_final_decision"] = fd
            row["exclude_code"] = rec["final_code"] or rec["r1_code"] or ""
            row["decision_rationale"] = rec["r1_memo"] or rec["r2_memo"] or ""
            row["adjudicator_id"] = "PI" if fd else ""
            updated += 1
    if not dry_run and updated:
        with open(path, "w", encoding="utf-8", newline="") as f:
            csv.DictWriter(f, fieldnames=fields).writeheader()
            csv.DictWriter(f, fieldnames=fields).writerows(rows)
    return updated


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--irr-only", action="store_true")
    args = parser.parse_args()

    print(f"Loading: {EXCEL}")
    records = read_sheet(EXCEL)
    print(f"  {len(records)} records loaded")

    # ── IRR ──
    pairs = [(D_MAP.get(r["r1"], ""), D_MAP.get(r["r2"], ""))
             for r in records if D_MAP.get(r["r1"]) and D_MAP.get(r["r2"])]
    kappa, stats = cohens_kappa(pairs)

    print(f"\n── IRR (R1 vs R2) ──")
    if stats:
        print(f"  Paired: {stats['n']}, Agreement: {stats['agree_pct']}%, κ = {stats['kappa']}")
        interp = ("Almost perfect" if kappa >= 0.81 else "Substantial" if kappa >= 0.61 else
                  "Moderate" if kappa >= 0.41 else "Fair" if kappa >= 0.21 else "Slight")
        print(f"  Interpretation: {interp}")
    else:
        print("  No paired data")

    # IRR 보고서 저장
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(os.path.join(OUT_DIR, "irr_report.md"), "w") as f:
        f.write("# Inter-Rater Reliability Report\n\n")
        if stats:
            f.write(f"- Paired records: {stats['n']}\n")
            f.write(f"- Agreement: {stats['agree_pct']}%\n")
            f.write(f"- Cohen's κ: {stats['kappa']} ({interp})\n")
        else:
            f.write("- No paired data yet\n")

    if args.irr_only:
        return

    # ── CSV 업데이트 ──
    by_id = {r["id"]: r for r in records}
    prefix = "[DRY RUN] " if args.dry_run else ""
    print(f"\n{prefix}Updating CSVs...")
    n1 = update_csv(DUAL_CSV, by_id, args.dry_run)
    n2 = update_csv(QUEUE_CSV, by_id, args.dry_run)
    print(f"  screening_ai_dual.csv: {n1} updated")
    print(f"  human_review_queue.csv: {n2} updated")

    # 요약 CSV
    if not args.dry_run:
        with open(os.path.join(OUT_DIR, "screening_human_decisions.csv"), "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=[
                "record_id", "r1_decision", "r1_code", "r2_decision", "r2_code",
                "r3_decision", "final_decision", "final_code"])
            w.writeheader()
            for r in records:
                if r["r1"] or r["r2"] or r["final"]:
                    w.writerow({
                        "record_id": r["id"],
                        "r1_decision": D_MAP.get(r["r1"], ""),
                        "r1_code": r["r1_code"],
                        "r2_decision": D_MAP.get(r["r2"], ""),
                        "r2_code": r["r2_code"],
                        "r3_decision": D_MAP.get(r["r3"], ""),
                        "final_decision": D_MAP.get(r["final"], ""),
                        "final_code": r["final_code"],
                    })

    # ── 진행률 ──
    r1_done = sum(1 for r in records if r["r1"])
    r2_done = sum(1 for r in records if r["r2"])
    final_done = sum(1 for r in records if r["final"])
    print(f"\n── Progress ──")
    print(f"  R1(PI): {r1_done}/{len(records)} ({r1_done/len(records)*100:.1f}%)")
    print(f"  R2:     {r2_done}/{len(records)} ({r2_done/len(records)*100:.1f}%)")
    print(f"  Final:  {final_done}/{len(records)} ({final_done/len(records)*100:.1f}%)")


if __name__ == "__main__":
    main()
