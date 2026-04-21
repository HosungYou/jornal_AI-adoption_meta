#!/usr/bin/env python3
"""
Claude API를 사용한 스크리닝 스크립트

기존 219건과 동일한 프롬프트·기준으로 미평가 1,238건 처리.
결과를 human_review_sheet_v5.xlsx의 Claude Sonnet 4.6 컬럼에 반영.

사용법:
    # 환경변수로 API 키 설정
    export ANTHROPIC_API_KEY="sk-ant-..."

    # 실행 (기본: 10건씩 배치)
    python3 claude_screening.py

    # 특정 범위만
    python3 claude_screening.py --start 0 --count 100

    # Dry run (API 호출 없이 대상 확인만)
    python3 claude_screening.py --dry-run

필요 패키지:
    pip install anthropic openpyxl
"""

import argparse
import csv
import json
import os
import sys
import time

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
QUEUE_CSV = os.path.join(REPO, "data", "03_screening", "human_review_queue.csv")
EXCEL_PATH = os.path.join(REPO, "data", "templates", "human_review_sheet_v5.xlsx")
PROGRESS_FILE = os.path.join(REPO, "paper_a", "data", "02_screening", "claude_screening_progress.json")
RESULTS_FILE = os.path.join(REPO, "paper_a", "data", "02_screening", "claude_screening_results.csv")

SCREENING_PROMPT = """You are screening studies for an educational AI adoption meta-analysis.

Apply these criteria:
1) Empirical quantitative study with primary data
2) AI technology is focal (not general ICT/IT)
3) Educational setting/population (students, instructors, administrators)
4) Adoption/acceptance/intention/use is measured
5) Correlation matrix or standardized beta/path data appears available or likely
6) English language
7) Publication window target: 2015-2025
8) Sample size n >= 50 (if stated or inferable from abstract)
9) Peer-reviewed journal article or full conference paper

Exclude codes:
E-FT1=Non-empirical (review, theoretical, meta-analysis, commentary),
E-FT2=No TAM/UTAUT constructs measured (no adoption/acceptance measurement),
E-FT3=AI is not the focal technology (general ICT, robotics, IoT, etc.),
E-FT4=Not education context (healthcare, business, government, etc.),
E-FT5=Cannot extract correlations/path coefficients (qualitative only, experiment-only),
E-FT6=Duplicate data,
E-FT7=Full text inaccessible,
E-FT8=Not in English

Return strict JSON:
{{
  "decision": "include|exclude|uncertain",
  "confidence": 0.0,
  "code": "E-FT1|E-FT2|E-FT3|E-FT4|E-FT5|E-FT6|E-FT7|E-FT8|",
  "criteria_flags": {{
    "quantitative": "yes|no|unclear",
    "ai_focal": "yes|no|unclear",
    "education_context": "yes|no|unclear",
    "adoption_outcome": "yes|no|unclear",
    "effect_size_reported": "yes|no|unclear",
    "english": "yes|no|unclear",
    "sample_size_adequate": "yes|no|unclear"
  }},
  "reason": "1-2 sentences"
}}

Title: {title}
Abstract: {abstract}
Keywords: {keywords}
Year: {year}
Source: {source}
"""


def load_progress():
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, "r") as f:
            return json.load(f)
    return {"completed": [], "last_index": 0}


def save_progress(progress):
    os.makedirs(os.path.dirname(PROGRESS_FILE), exist_ok=True)
    with open(PROGRESS_FILE, "w") as f:
        json.dump(progress, f)


def get_unscreened_records(completed_ids):
    """미평가 레코드 로드"""
    # 기존 Claude 평가 완료 ID (v4에서)
    v4_path = os.path.join(REPO, "data", "templates", "human_review_sheet_v4.xlsx")

    records = []
    with open(QUEUE_CSV, "r", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            rid = row["record_id"]
            if rid not in completed_ids:
                records.append(row)
    return records


def screen_one(client, record, model="claude-sonnet-4-6-20250514"):
    """단일 레코드 스크리닝"""
    prompt = SCREENING_PROMPT.format(
        title=record["title"],
        year=record["year"],
        abstract=record["abstract"][:3000],  # 토큰 제한
    )

    response = client.messages.create(
        model=model,
        max_tokens=300,
        temperature=0,
        messages=[{"role": "user", "content": prompt}],
    )

    text = response.content[0].text.strip()

    # JSON 파싱
    try:
        # JSON 블록 추출
        if "```" in text:
            text = text.split("```")[1]
            if text.startswith("json"):
                text = text[4:]
        result = json.loads(text)
        return result
    except json.JSONDecodeError:
        # 파싱 실패 시 텍스트에서 추출 시도
        decision = "uncertain"
        if '"include"' in text.lower():
            decision = "include"
        elif '"exclude"' in text.lower():
            decision = "exclude"
        return {"decision": decision, "code": "", "reason": f"JSON 파싱 실패: {text[:100]}"}


def main():
    parser = argparse.ArgumentParser(description="Claude API 스크리닝")
    parser.add_argument("--start", type=int, default=0, help="시작 인덱스")
    parser.add_argument("--count", type=int, default=0, help="처리 건수 (0=전체)")
    parser.add_argument("--dry-run", action="store_true", help="API 호출 없이 대상만 확인")
    parser.add_argument("--model", default="claude-sonnet-4-6-20250514", help="모델 ID")
    parser.add_argument("--delay", type=float, default=1.0, help="API 호출 간 대기(초)")
    args = parser.parse_args()

    # API 키 확인
    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key and not args.dry_run:
        print("Error: ANTHROPIC_API_KEY 환경변수를 설정하세요.")
        print("  export ANTHROPIC_API_KEY='sk-ant-...'")
        sys.exit(1)

    # 진행 상황 로드
    progress = load_progress()
    completed_ids = set(progress["completed"])
    print(f"이전 완료: {len(completed_ids)}건")

    # 미평가 레코드 로드
    records = get_unscreened_records(completed_ids)
    print(f"미평가: {len(records)}건")

    if args.start:
        records = records[args.start:]
    if args.count:
        records = records[:args.count]

    print(f"이번 처리 대상: {len(records)}건")

    if args.dry_run:
        from collections import Counter
        cats = Counter(r.get("review_type", "") for r in records)
        print(f"카테고리: {dict(cats)}")
        print("(Dry run - API 호출 안 함)")
        return

    # Anthropic 클라이언트
    try:
        from anthropic import Anthropic
    except ImportError:
        print("Error: pip install anthropic")
        sys.exit(1)

    client = Anthropic(api_key=api_key)

    # 결과 CSV 준비
    os.makedirs(os.path.dirname(RESULTS_FILE), exist_ok=True)
    csv_exists = os.path.exists(RESULTS_FILE)
    csv_file = open(RESULTS_FILE, "a", newline="", encoding="utf-8")
    writer = csv.DictWriter(csv_file, fieldnames=[
        "record_id", "decision", "code", "reason", "model", "timestamp"
    ])
    if not csv_exists:
        writer.writeheader()

    # 스크리닝 실행
    from collections import Counter
    results = Counter()
    errors = 0

    for i, rec in enumerate(records):
        rid = rec["record_id"]
        try:
            result = screen_one(client, rec, model=args.model)
            decision = result.get("decision", "uncertain")
            code = result.get("code", "")
            reason = result.get("reason", "")

            writer.writerow({
                "record_id": rid,
                "decision": decision,
                "code": code,
                "reason": reason,
                "model": args.model,
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            })
            csv_file.flush()

            completed_ids.add(rid)
            progress["completed"] = list(completed_ids)
            progress["last_index"] = args.start + i
            results[decision] += 1

            if (i + 1) % 10 == 0:
                save_progress(progress)
                print(f"  [{i+1}/{len(records)}] {dict(results)} (errors: {errors})")

        except Exception as e:
            errors += 1
            print(f"  Error {rid}: {e}")
            if errors > 10:
                print("Too many errors. Stopping.")
                break

        time.sleep(args.delay)

    csv_file.close()
    save_progress(progress)

    print(f"\n=== 완료 ===")
    print(f"  처리: {sum(results.values())}건")
    print(f"  결과: {dict(results)}")
    print(f"  오류: {errors}건")
    print(f"  결과 파일: {RESULTS_FILE}")
    print(f"\n다음 단계: python3 update_v5_with_claude.py")


if __name__ == "__main__":
    main()
