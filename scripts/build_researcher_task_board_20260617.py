#!/usr/bin/env python3
"""Build researcher-facing Paper A/B task board artifacts in OneDrive."""

from __future__ import annotations

import shutil
from datetime import date
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor
from openpyxl import Workbook
from openpyxl.comments import Comment
from openpyxl.formatting.rule import FormulaRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.worksheet.datavalidation import DataValidation


ROOT = Path(
    "/Users/newhosung/Library/CloudStorage/OneDrive-SharedLibraries-"
    "ThePennsylvaniaStateUniversity/AI Adoption Meta Analysis - Documents"
)
WORK_DIR = ROOT / "00_INDEX" / "2026-06-17_Paper_A_B_work_allocation"
SHARED = WORK_DIR / "00_shared"
ARCHIVE = WORK_DIR / "99_archive" / "previous_technical_plan_20260617"

BOARD_XLSX = SHARED / "연구자_작업보드_20260617.xlsx"
GUIDE_DOCX = SHARED / "연구자_작업안내_20260617.docx"
GUIDE_MD = SHARED / "연구자_작업안내_20260617.md"
README_MD = SHARED / "README_먼저_읽어주세요.md"
PAPER_A_PROCESS_DOCX = SHARED / "Paper_A_포함판단_과정_설명서_20260617.docx"
PAPER_A_PROCESS_MD = SHARED / "Paper_A_포함판단_과정_설명서_20260617.md"
PAPER_A_REFERENCES_DIR = WORK_DIR / "References" / "Paper_A"
LOCAL_REPO_ROOT = Path(__file__).resolve().parents[1]
LOCAL_PAPER_A_REFERENCE_PDFS = LOCAL_REPO_ROOT / "references" / "paper_a_apa7_evidence_review_20260615" / "pdfs"

STATUS_VALUES = ["시작 전", "진행 중", "검토 요청", "완료", "막힘"]
ROLE_VALUES = ["R1", "R2", "R3", "R4", "PI", "공동"]
PRIORITY_VALUES = ["높음", "보통", "낮음"]


def rel_link(target: Path, base: Path = SHARED) -> str:
    return target.relative_to(ROOT).as_posix()


REFERENCE_FILES = [
    {
        "id": "REF-A-COUNT",
        "paper": "Paper A",
        "label": "Paper A 포함 수/PRISMA 기준 파일 묶음",
        "when": "Methods와 Results의 포함 연구 수, PRISMA 흐름도, 224/225 표현을 확정할 때 봅니다.",
        "path": ROOT / "90_repository_mirror/journal_AI-adoption_meta",
        "must_read": "\n".join(
            [
                "루트: 90_repository_mirror/journal_AI-adoption_meta",
                "paper_a/PRISMA_COUNTS_LOCK_20260615.md",
                "paper_a/PRISMA_COUNTS_REVIEW_NEEDED_20260615.md",
                "data/02_screening/screening_summary.json",
                "data/02_screening/human_screening_results_consolidated.csv",
                "paper_a/public_data_repository_20260615/6_PRISMA_Count_Lock/PRISMA_COUNTS_LOCK_20260615.md",
            ]
        ),
        "note": "확인 이유는 숫자 차이를 다시 분석하려는 것이 아니라, Methods/Results/PRISMA에서 같은 기준을 쓰기 위한 최종 원고 표현을 잠그기 위해서입니다.",
    },
    {
        "id": "REF-A-PROCESS",
        "paper": "Paper A",
        "label": "Paper A 포함 판단 과정 설명서",
        "when": "A2에서 인간 판단, AI 보조 선별, 최종 포함 절차를 Methods 문장으로 검수할 때 봅니다.",
        "path": PAPER_A_PROCESS_DOCX,
        "must_read": "\n".join(
            [
                "00_shared/Paper_A_포함판단_과정_설명서_20260617.docx",
                "00_shared/Paper_A_포함판단_과정_설명서_20260617.md",
                "03_source_adjudication/Paper_A/2026-06-14_human_process_candidate_audit/REVIEW_THIS_PAPER_A_HUMAN_PROCESS_AUDIT_20260614.docx",
                "03_source_adjudication/Paper_A/2026-06-14_human_style_source_adjudication/PAPER_A_HUMAN_STYLE_SOURCE_ADJUDICATION_GUIDE_20260614.docx",
            ]
        ),
        "note": "AI가 새 판단을 하라는 문서가 아니라, 이미 진행된 인간 검토와 AI 보조 선별 과정을 연구자가 원고 Methods에 설명하기 위한 안내입니다.",
    },
    {
        "id": "REF-A-METHODS",
        "paper": "Paper A",
        "label": "Paper A Methods/Results 원고와 결과표",
        "when": "R1 연구자가 Methods, Results, 모델군 해석, 방법론 적합성을 검수할 때 봅니다.",
        "path": ROOT
        / "05_manuscripts/Paper_A/2026-06-15_apa7_model_family_full_manuscript_scaffold/"
        / "PAPER_A_LONGTABLE_PANEL_SUBMISSION_DRAFT_20260616.docx",
        "must_read": "\n".join(
            [
                "05_manuscripts/Paper_A/2026-06-15_apa7_model_family_full_manuscript_scaffold/PAPER_A_LONGTABLE_PANEL_SUBMISSION_DRAFT_20260616.docx",
                "05_manuscripts/Paper_A/2026-06-15_apa7_model_family_full_manuscript_scaffold/tables/",
                "05_manuscripts/Paper_A/2026-06-15_apa7_model_family_full_manuscript_scaffold/supplemental_diagnostics/",
                "03_source_adjudication/Paper_A/2026-06-15_researcher_approved_s048_analysis/PAPER_A_SOURCE_CORRECTED_COMPLETE_CASE_TSSEM_20260615.md",
            ]
        ),
        "note": "full10은 이론적 근거 지도, core7/trust6는 경험적으로 추정 가능한 경로라는 구분이 Methods/Results 전체에서 유지되는지 봅니다.",
    },
    {
        "id": "REF-A-INTRO-REFERENCES",
        "paper": "Paper A",
        "label": "Paper A 선행연구/References 보강 폴더",
        "when": "Introduction과 선행연구 문단을 보강하고 읽은 PDF와 인용 메모를 정리할 때 봅니다.",
        "path": PAPER_A_REFERENCES_DIR,
        "must_read": "\n".join(
            [
                "00_INDEX/2026-06-17_Paper_A_B_work_allocation/References/Paper_A/README.md",
                "00_INDEX/2026-06-17_Paper_A_B_work_allocation/References/Paper_A/pdfs/",
                "00_INDEX/2026-06-17_Paper_A_B_work_allocation/References/Paper_A/notes/",
                "90_repository_mirror/journal_AI-adoption_meta/references/paper_a_apa7_evidence_review_20260615/",
                "90_repository_mirror/journal_AI-adoption_meta/references/paper_a_model_family_masem_20260614/",
            ]
        ),
        "note": "R2가 중심이 되어 PDF 큐와 짧은 주석 메모를 관리합니다. 단순 파일 수집이 아니라 원고에서 어떤 문장을 보강할지까지 남기는 작업입니다.",
    },
    {
        "id": "REF-A-DISCUSSION",
        "paper": "Paper A",
        "label": "Paper A 논의/한계 보강 자료",
        "when": "Discussion, limitations, implications를 초안 단계에서 보강할 때 봅니다.",
        "path": ROOT
        / "05_manuscripts/Paper_A/2026-06-15_apa7_model_family_full_manuscript_scaffold/"
        / "PAPER_A_THEORY_DISCUSSION_WRITING_GUIDE_KR_20260616.docx",
        "must_read": "\n".join(
            [
                "05_manuscripts/Paper_A/2026-06-15_apa7_model_family_full_manuscript_scaffold/PAPER_A_THEORY_DISCUSSION_WRITING_GUIDE_KR_20260616.docx",
                "05_manuscripts/Paper_A/2026-06-15_apa7_model_family_full_manuscript_scaffold/PAPER_A_LONGTABLE_PANEL_SUBMISSION_DRAFT_20260616.docx",
                "05_manuscripts/Paper_A/2026-06-15_apa7_model_family_full_manuscript_scaffold/supplemental_diagnostics/",
                "References/Paper_A/notes/",
            ]
        ),
        "note": "R3는 Results를 과장하지 않으면서 Discussion/limitations/implications 문단을 연구자 관점에서 보강합니다.",
    },
    {
        "id": "REF-A-APA",
        "paper": "Paper A",
        "label": "Paper A APA 7/JARS 형식 점검 자료",
        "when": "표, 그림, References, 결론부, APA 7th style, JARS 항목을 점검할 때 봅니다.",
        "path": ROOT
        / "05_manuscripts/Paper_A/2026-06-15_apa7_model_family_full_manuscript_scaffold",
        "must_read": "\n".join(
            [
                "05_manuscripts/Paper_A/2026-06-15_apa7_model_family_full_manuscript_scaffold/PAPER_A_LONGTABLE_PANEL_SUBMISSION_DRAFT_20260616.docx",
                "05_manuscripts/Paper_A/2026-06-15_apa7_model_family_full_manuscript_scaffold/tables/",
                "05_manuscripts/Paper_A/2026-06-15_apa7_model_family_full_manuscript_scaffold/figures/",
                "05_manuscripts/Paper_A/2026-06-15_apa7_model_family_full_manuscript_scaffold/PAPER_A_EXPANDED_REFERENCE_BANK_20260615.md",
                "90_repository_mirror/journal_AI-adoption_meta/references/paper_a_apa7_evidence_review_20260615/paper_a_crossref_apa7_reference_list_20260615.md",
            ]
        ),
        "note": "APA 7th professional style, JARS 보고 항목, 표/그림 첫 언급 위치, reference list 누락을 보는 작업입니다.",
    },
    {
        "id": "REF-B-MAIN",
        "paper": "Paper B",
        "label": "Paper B 최신 원고 후보",
        "when": "Paper B 방법/결과 문장을 확인하실 때 먼저 보시면 됩니다.",
        "path": ROOT
        / "05_manuscripts/Paper_B/2026-06-12_target_journal/"
        / "PAPER_B_RESEARCH_SYNTHESIS_METHODS_TARGET_DRAFT_20260612.docx",
        "note": "모델 비교 결과는 최종 구조모형 대체 주장이 아니라, 제한된 근거 정리로 읽어야 합니다.",
    },
    {
        "id": "REF-B-REFERENCE",
        "paper": "Paper B",
        "label": "Paper B source-anchored reference 후보",
        "when": "합의값, 출처 확인, frozen reference가 무엇인지 확인하실 때 보시면 됩니다.",
        "path": ROOT
        / "03_source_adjudication/Paper_B/reference_standard_candidates/"
        / "Paper2_Human_Final_Consensus_20260605_v2/Paper2_Human_Final_Consensus_Reference_Document_20260605_v2.md",
        "note": "문서에서는 '절대적 정답'처럼 쓰지 말고, '출처를 확인해 만든 최종 기준표'로 설명해 주세요.",
    },
    {
        "id": "REF-B-WORKBOOKS",
        "paper": "Paper B",
        "label": "R1-R4 최신 워크북 묶음",
        "when": "R1-R4 원자료와 freeze candidate의 위치를 확인하실 때 보시면 됩니다.",
        "path": ROOT / "01_workbooks/latest_collections/20260605_R1_R4",
        "note": "원자료 셀은 덮어쓰지 않고, 결정은 별도 decision log나 작업보드에 남겨 주세요.",
    },
    {
        "id": "REF-B-STEP5",
        "paper": "Paper B",
        "label": "Paper B 모델 비교 분석 결과 위치",
        "when": "2,043행 전체 대상 M1-R 결과, 결과를 나누어 읽는 기준, 예외 항목을 따로 표시한 채점 결과를 확인하실 때 보시면 됩니다.",
        "path": ROOT / "04_analysis_outputs/Paper_B/analysis_input_20260530",
        "note": "전체 구성개념/전체 행에서 구조모형 결과가 안정적이라는 최종 주장으로 바로 연결하지 마세요.",
    },
]


TASKS = [
    {
        "id": "A1",
        "paper": "Paper A",
        "owner": "R1",
        "support": "R2",
        "priority": "높음",
        "title": "Methods/Results의 포함 연구 수와 PRISMA 표현을 잠가 주세요",
        "do": "숫자가 다른 이유를 새로 추측하는 일이 아니라, 원고 Methods/Results/PRISMA에서 같은 기준을 쓰도록 최종 표현을 확인해 주세요. 현재 작업 기준은 225개 포함 행, 중복 DOI 1건 병합, 224개 고유 포함 보고서/연구입니다.",
        "reference": "REF-A-COUNT",
        "example": "산출물 예: '원고에는 225 included screening rows와 224 unique included reports/studies를 구분해 쓰며, PRISMA 본문 표현은 224 unique reports/studies로 통일한다'처럼 문장과 근거 파일명을 함께 남깁니다.",
        "output": "R1/A1_Methods_Results_PRISMA_포함수_잠금메모_20260617.md",
        "done": "Methods, Results, PRISMA 그림/캡션에 쓸 숫자 표현과 근거 파일명이 정리되어 있으면 완료입니다.",
    },
    {
        "id": "A2",
        "paper": "Paper A",
        "owner": "R1",
        "support": "R2",
        "priority": "높음",
        "title": "인간 판단 과정과 AI 보조 선별 과정을 Methods에 맞게 설명해 주세요",
        "do": "새 판단을 만들지 말고, 이미 진행된 인간 검토, AI 보조 선별, 최종 포함 과정이 Methods에서 독자가 이해할 수 있게 설명되어 있는지 확인해 주세요. 누가 무엇을 판단했는지, AI는 어디까지 보조였는지, 최종 포함은 인간 검토 기준으로 어떻게 확정되었는지를 문장으로 정리해 주세요.",
        "reference": "REF-A-PROCESS",
        "example": "산출물 예: Methods에 넣을 절차 문단 초안, 확인한 근거 문서 목록, 'AI가 최종 포함 여부를 결정했다'처럼 쓰면 안 되는 표현 목록.",
        "output": "R1/A2_Methods_포함판단과정_설명검수_20260617.docx",
        "done": "인간 판단, AI 보조 역할, 최종 포함 기준이 분리되어 설명되고, 원고에 넣을 문단 후보가 있으면 완료입니다.",
    },
    {
        "id": "A3",
        "paper": "Paper A",
        "owner": "R1",
        "support": "R3",
        "priority": "높음",
        "title": "Methods/Results와 방법론 적합성을 리뷰해 주세요",
        "do": "Paper A의 핵심은 Methods와 Results입니다. 모델군 MASEM 접근, full10/core7/trust6 구분, complete-case 근거, 표/그림의 결과 해석이 방법론적으로 방어 가능한지 검토해 주세요. 표현 하나를 고치는 작업이 아니라, 원고의 방법-결과 논리가 성립하는지 보는 작업입니다.",
        "reference": "REF-A-METHODS",
        "example": "산출물 예: Methods/Results 검토표. 열 예시는 '원고 위치, 주장, 근거 파일, 방법론상 문제 없음/수정 필요, 수정 문장 후보, PI 확인 필요 여부'입니다.",
        "output": "R1/A3_Methods_Results_방법론적합성_검토표_20260617.xlsx",
        "done": "Methods/Results의 핵심 주장별 근거와 수정 필요 여부가 표로 정리되어 있으면 완료입니다.",
    },
    {
        "id": "A4",
        "paper": "Paper A",
        "owner": "R2",
        "support": "R4",
        "priority": "높음",
        "title": "Introduction과 선행연구를 보강하고 References 폴더를 정리해 주세요",
        "do": "Introduction과 이론적 배경은 아직 초안 단계입니다. AI adoption, UTAUT/TAM 계열, trust/reliance, attitude, anxiety/self-efficacy, MASEM 방법론 선행연구를 읽고 원고에서 보강할 문장을 제안해 주세요. 읽은 PDF는 References/Paper_A/pdfs에 모으고, 각 PDF가 어떤 원고 문장을 보강하는지 notes에 남겨 주세요.",
        "reference": "REF-A-INTRO-REFERENCES",
        "example": "산출물 예: 선행연구 요약표. 열 예시는 'PDF 파일명, 핵심 주장, 원고 보강 위치, 넣을 문장 후보, APA reference, 반드시 인용/선택 인용/보류'입니다.",
        "output": "R2/A4_Introduction_선행연구_References_보강표_20260617.xlsx",
        "done": "References/Paper_A/pdfs와 notes가 채워지고, Introduction에 넣을 문장 후보와 인용 근거가 정리되어 있으면 완료입니다.",
    },
    {
        "id": "A5",
        "paper": "Paper A",
        "owner": "R3",
        "support": "R2",
        "priority": "보통",
        "title": "Discussion, 한계, 시사점 초안을 연구자 관점에서 보강해 주세요",
        "do": "Discussion부터 Conclusion 전까지는 초안 단계입니다. Results에서 실제로 말할 수 있는 범위를 넘지 않도록 하면서, 이론적 기여, 교육/HRD 맥락의 시사점, 데이터와 방법의 한계를 연구자 언어로 보강해 주세요.",
        "reference": "REF-A-DISCUSSION",
        "example": "산출물 예: Discussion 보강안. 각 문단마다 '원고 위치, 보강 문장, 근거 결과/선행연구, 과장 위험 여부, 대체 표현'을 남깁니다.",
        "output": "R3/A5_Discussion_한계_시사점_보강안_20260617.docx",
        "done": "Discussion/limitations/implications 문단 후보가 Results 근거와 연결되어 있으면 완료입니다.",
    },
    {
        "id": "A6",
        "paper": "Paper A",
        "owner": "R4",
        "support": "R1",
        "priority": "높음",
        "title": "APA 7th style, 표/그림, References, Conclusion을 점검해 주세요",
        "do": "Conclusion은 초안 단계이며, 표/그림/References는 투고 전 품질에 직접 연결됩니다. APA 7th professional style, JARS 보고 항목, 표와 그림의 첫 언급 위치, 표 제목/그림 캡션, reference list 누락, 결론부가 Results와 맞는지 확인해 주세요.",
        "reference": "REF-A-APA",
        "example": "산출물 예: APA/JARS 점검표. 열 예시는 '항목, 원고 위치, 현재 상태, 수정 필요 여부, 참고 기준, 수정 제안'입니다.",
        "output": "R4/A6_APA7_JARS_표그림_References_Conclusion_점검표_20260617.xlsx",
        "done": "APA/JARS 점검 결과, 표/그림/References 수정 목록, Conclusion 수정 후보가 정리되어 있으면 완료입니다.",
    },
    {
        "id": "B1",
        "paper": "Paper B",
        "owner": "R1",
        "support": "R4",
        "priority": "높음",
        "title": "Paper B 진행 순서가 지켜졌는지 확인해 주세요",
        "do": "원 코딩 보존, 코더 차이 정리, 원문 확인 결정, 최종 기준표 확정, 모델 비교 순서가 문서와 원고에서 뒤섞이지 않았는지 확인해 주세요.",
        "reference": "REF-B-REFERENCE",
        "example": "예: '절대적 정답'처럼 읽힐 수 있는 표현을 '출처를 확인해 만든 최종 기준표'로 바꿀 후보.",
        "output": "R1/B1_PaperB_진행순서_확인메모_20260617.md",
        "done": "잘못된 순서 표현과 수정 문장이 정리되어 있으면 완료입니다.",
    },
    {
        "id": "B2",
        "paper": "Paper B",
        "owner": "R2",
        "support": "R3",
        "priority": "높음",
        "title": "코더 간 차이를 연구자가 읽을 수 있게 정리해 주세요",
        "do": "단순 숫자 차이가 아니라 포함/제외, 표본 선택, 구성개념 분류, 근거 유형 차이로 묶어서 정리해 주세요.",
        "reference": "REF-B-WORKBOOKS",
        "example": "예: 'HTMT를 상관으로 넣은 경우', '경로계수와 상관계수 r이 섞인 경우', '표본 수 N이 다른 경우'.",
        "output": "R2/B2_코더차이_정리표_20260617.xlsx",
        "done": "차이 유형, 해당 연구 ID, 원문 확인 필요 여부가 보이면 완료입니다.",
    },
    {
        "id": "B3",
        "paper": "Paper B",
        "owner": "R3",
        "support": "R2, R4",
        "priority": "높음",
        "title": "출처 확인 결정이 빠진 항목을 찾아 주세요",
        "do": "코더 간 차이가 원문 확인 결정으로 연결되었는지 확인하고, 빠진 항목을 R1/PI 확인 목록으로 올려 주세요.",
        "reference": "REF-B-REFERENCE",
        "example": "예: 연구 ID, 항목, 원자료 값, 최종값, 원문 쪽수/표 번호, 결정 근거.",
        "output": "R3/B3_원문확인결정_누락목록_20260617.xlsx",
        "done": "원문 확인 결정이 있음/없음/확인 필요로 나뉘어 있으면 완료입니다.",
    },
    {
        "id": "B4",
        "paper": "Paper B",
        "owner": "R4",
        "support": "R1",
        "priority": "높음",
        "title": "모델 비교 결과를 원고용 근거 묶음으로 정리해 주세요",
        "do": "2,043행 전체 대상 M1-R 결과, 중복 작업 행 없음, 모델 실행 오류 없음, 예외 항목을 따로 표시한 채점 결과를 원고 표/부록 후보로 정리해 주세요.",
        "reference": "REF-B-STEP5",
        "example": "예: 결과 파일명, 핵심 숫자, 원고에 쓸 수 있는 문장, 쓰면 안 되는 문장.",
        "output": "R4/B4_모델비교_원고근거묶음_20260617.xlsx",
        "done": "원고에 넣을 표 후보와 주의 문장이 함께 있으면 완료입니다.",
    },
    {
        "id": "B5",
        "paper": "Paper B",
        "owner": "R1",
        "support": "R4",
        "priority": "높음",
        "title": "구조모형 관련 주장을 너무 크게 쓰지 않았는지 확인해 주세요",
        "do": "core-6 확인 결과, core7/core8 확장 확인, 전체 구성개념/전체 행 확인 단계를 분리해서 원고 문장을 점검해 주세요.",
        "reference": "REF-B-MAIN",
        "example": "예: '모델이 사람 코딩을 안정적으로 대체한다' 같은 표현은 쓰지 않고, 일부 대상에서 확인한 결과로 제한.",
        "output": "R1/B5_구조모형_주장범위_점검표_20260617.docx",
        "done": "사용 가능 문장과 금지 문장이 구분되어 있으면 완료입니다.",
    },
    {
        "id": "B6",
        "paper": "Paper B",
        "owner": "R4",
        "support": "R1",
        "priority": "보통",
        "title": "Paper B 표/부록 후보와 결과 문장을 독자 관점에서 점검해 주세요",
        "do": "결과표, 부록 후보, 모델 비교 결과 설명이 연구자가 읽기 쉽게 정리되어 있는지 확인해 주세요. 숫자와 문장이 맞는지, 본문에 넣을 문장과 부록으로 보낼 표가 구분되어 있는지 점검합니다.",
        "reference": "REF-B-MAIN",
        "example": "예: 표/부록 후보명, 본문에 쓸 문장, 부록으로 보낼 이유, 독자가 오해할 수 있는 표현, 수정 제안.",
        "output": "R4/B6_PaperB_표부록_결과문장_점검표_20260617.xlsx",
        "done": "본문 문장 후보, 부록 후보, 수정 필요 표현이 구분되어 있으면 완료입니다.",
    },
]


REFERENCES = [
    {
        "short": "PRISMA 2020",
        "use": "Paper A의 체계적 문헌고찰/메타분석 보고와 흐름도 확인",
        "citation": "Page MJ et al. (2021). The PRISMA 2020 statement. BMJ, 372, n71.",
        "url": "https://www.bmj.com/content/372/bmj.n71",
    },
    {
        "short": "APA JARS",
        "use": "원고 보고 항목의 충분성과 양적 연구/메타분석 보고 확인",
        "citation": "APA Style. Journal Article Reporting Standards.",
        "url": "https://apastyle.apa.org/jars",
    },
]


def archive_old_shared_files() -> list[str]:
    ARCHIVE.mkdir(parents=True, exist_ok=True)
    moved: list[str] = []
    patterns = [
        "PAPER_A_B_TASK_TRACKER_SEED_20260617.csv",
        "PAPER_A_B_WORK_ALLOCATION_AND_TRACKING_PLAN_KO_20260617.docx",
        "PAPER_A_B_WORK_ALLOCATION_AND_TRACKING_PLAN_KO_20260617.md",
        "~$PER_A_B_WORK_ALLOCATION_AND_TRACKING_PLAN_KO_20260617.docx",
    ]
    for name in patterns:
        src = SHARED / name
        if not src.exists():
            continue
        dst = ARCHIVE / name
        if dst.exists():
            dst = ARCHIVE / f"{src.stem}_archived{src.suffix}"
        shutil.move(str(src), str(dst))
        moved.append(name)
    for role in ["R1", "R2", "R3", "R4"]:
        src = WORK_DIR / role / f"README_{role}_TASKS_20260617.md"
        if not src.exists():
            continue
        dst = ARCHIVE / f"{role}_README_{role}_TASKS_20260617.md"
        if dst.exists():
            dst = ARCHIVE / f"{role}_README_{role}_TASKS_20260617_archived.md"
        shutil.move(str(src), str(dst))
        moved.append(f"{role}/README_{role}_TASKS_20260617.md")
    return moved


def ref_by_id(ref_id: str) -> dict:
    return next(r for r in REFERENCE_FILES if r["id"] == ref_id)


def set_korean_font(run, font_name: str = "Malgun Gothic") -> None:
    run.font.name = font_name
    run._element.rPr.rFonts.set(qn("w:eastAsia"), font_name)


def style_doc(doc: Document) -> None:
    section = doc.sections[0]
    section.top_margin = Inches(1)
    section.bottom_margin = Inches(1)
    section.left_margin = Inches(1)
    section.right_margin = Inches(1)

    styles = doc.styles
    for style_name in ["Normal", "Heading 1", "Heading 2", "Heading 3"]:
        style = styles[style_name]
        style.font.name = "Malgun Gothic"
        style._element.rPr.rFonts.set(qn("w:eastAsia"), "Malgun Gothic")

    normal = styles["Normal"]
    normal.font.size = Pt(10.5)
    normal.paragraph_format.space_after = Pt(6)
    normal.paragraph_format.line_spacing = 1.18

    h1 = styles["Heading 1"]
    h1.font.size = Pt(16)
    h1.font.color.rgb = RGBColor(46, 116, 181)
    h1.paragraph_format.space_before = Pt(14)
    h1.paragraph_format.space_after = Pt(8)

    h2 = styles["Heading 2"]
    h2.font.size = Pt(13)
    h2.font.color.rgb = RGBColor(46, 116, 181)
    h2.paragraph_format.space_before = Pt(10)
    h2.paragraph_format.space_after = Pt(6)


def add_hyperlink(paragraph, text: str, target: str) -> None:
    part = paragraph.part
    rel_id = part.relate_to(
        target,
        "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink",
        is_external=True,
    )
    hyperlink = OxmlElement("w:hyperlink")
    hyperlink.set(qn("r:id"), rel_id)
    new_run = OxmlElement("w:r")
    r_pr = OxmlElement("w:rPr")
    color = OxmlElement("w:color")
    color.set(qn("w:val"), "0563C1")
    r_pr.append(color)
    underline = OxmlElement("w:u")
    underline.set(qn("w:val"), "single")
    r_pr.append(underline)
    new_run.append(r_pr)
    text_el = OxmlElement("w:t")
    text_el.text = text
    new_run.append(text_el)
    hyperlink.append(new_run)
    paragraph._p.append(hyperlink)


def add_bullet(doc: Document, text: str) -> None:
    p = doc.add_paragraph(style="List Bullet")
    run = p.add_run(text)
    set_korean_font(run)


def add_numbered(doc: Document, text: str) -> None:
    p = doc.add_paragraph(style="List Number")
    run = p.add_run(text)
    set_korean_font(run)


def add_table(doc: Document, headers: list[str], rows: list[list[str]]) -> None:
    table = doc.add_table(rows=1, cols=len(headers))
    table.style = "Table Grid"
    hdr = table.rows[0].cells
    for idx, header in enumerate(headers):
        p = hdr[idx].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(header)
        r.bold = True
        set_korean_font(r)
    for row in rows:
        cells = table.add_row().cells
        for idx, value in enumerate(row):
            p = cells[idx].paragraphs[0]
            r = p.add_run(value)
            set_korean_font(r)


def build_guide_docx() -> None:
    doc = Document()
    style_doc(doc)

    title = doc.add_paragraph()
    title.paragraph_format.space_after = Pt(3)
    run = title.add_run("Paper A/B 연구자 작업안내")
    run.font.size = Pt(22)
    run.font.bold = True
    run.font.color.rgb = RGBColor(31, 78, 121)
    set_korean_font(run)

    subtitle = doc.add_paragraph()
    subtitle_run = subtitle.add_run(
        "R1-R4 연구자가 자신의 할 일을 확인하고, 진행 상태와 산출물을 남기기 위한 안내 문서입니다. "
        "기술 운영 문서가 아니라 실제 작업 배분과 완료 확인을 위한 문서입니다."
    )
    set_korean_font(subtitle_run)

    doc.add_heading("1. 먼저 여실 파일", level=1)
    p = doc.add_paragraph()
    p.add_run("작업 상태는 ").bold = False
    r_file = p.add_run("연구자_작업보드_20260617.xlsx")
    r_file.bold = True
    set_korean_font(r_file)
    r = p.add_run("에서 표시해 주세요. 상태는 시작 전, 진행 중, 검토 요청, 완료, 막힘 중 하나로 바꿔 주시면 됩니다.")
    set_korean_font(r)

    add_bullet(doc, "완료하셨으면 작업보드의 상태를 '완료'로 바꾸고, 완료 표시일과 산출물 위치를 적어 주세요.")
    add_bullet(doc, "PI가 확인해야 할 작업은 상태가 '완료'일 때 보드에서 자동으로 'PI 확인 필요'가 보이도록 해 두었습니다.")
    add_bullet(doc, "자동 이메일 알림은 이번 버전에서 사용하지 않습니다. 대신 PI가 보드에서 완료된 행을 필터링해 확인하실 수 있습니다.")
    add_bullet(doc, "OneDrive 웹 공유 링크는 실제 SharePoint/OneDrive에서 '링크 복사'로 만든 뒤 보드의 웹 링크 열에 붙여 넣어 주세요.")

    doc.add_heading("2. 상태 표시 기준", level=1)
    add_table(
        doc,
        ["상태", "의미", "연구자가 남길 것"],
        [
            ["시작 전", "아직 착수하지 않은 일입니다.", "비워 두셔도 됩니다."],
            ["진행 중", "파일을 확인하고 있거나 산출물을 작성 중입니다.", "막힌 점이 있으면 메모 열에 적어 주세요."],
            ["검토 요청", "본인은 작성했지만 PI 또는 다른 연구자 확인이 필요합니다.", "확인받을 파일 위치 또는 웹 링크와 질문을 남겨 주세요."],
            ["완료", "완료 기준을 충족했고 산출물 위치를 남긴 상태입니다.", "완료 표시일, 산출물 위치, 한 줄 요약을 남겨 주세요."],
            ["막힘", "자료 접근, 판단 기준, 원고 표현 때문에 진행이 멈춘 상태입니다.", "무엇이 막혔는지와 누구의 판단이 필요한지 적어 주세요."],
        ],
    )

    doc.add_heading("3. 역할별로 먼저 볼 일", level=1)
    add_table(
        doc,
        ["역할", "먼저 확인할 작업", "주로 남길 산출물"],
        [
            ["R1", "A1, A2, A3, B1, B5", "Paper A Methods/Results 검수, 포함 판단 과정 설명, 방법론 적합성 검토"],
            ["R2", "A4, B2", "Paper A Introduction/선행연구 보강, References PDF/메모 큐, 코더 차이 정리표"],
            ["R3", "A5, B3", "Paper A Discussion/한계/시사점 보강안, 원문 확인 결정 누락 목록"],
            ["R4", "A6, B4, B6", "Paper A APA 7/JARS/표그림/References/Conclusion 점검, 모델 비교 결과의 원고 근거 묶음"],
            ["PI", "완료 또는 검토 요청으로 표시된 행", "승인/수정 요청/추가 확인 결정"],
        ],
    )

    doc.add_heading("4. Paper A 작업 설명", level=1)
    add_bullet(doc, "Paper A에서 Methods와 Results는 R1 연구자가 중심적으로 검수합니다.")
    add_bullet(doc, "Introduction부터 Discussion, Conclusion까지는 아직 초안 단계로 표시하고, R2-R4가 보강 작업을 나누어 맡습니다.")
    add_bullet(doc, "연구자에게 부여한 일은 읽기, 판단, 원고 보강, APA/JARS 점검, References 정리입니다. 새 AI 판단을 수행하라는 과업은 포함하지 않았습니다.")
    for task in [t for t in TASKS if t["paper"] == "Paper A"]:
        doc.add_heading(f"{task['id']}. {task['title']}", level=2)
        add_bullet(doc, f"담당: {task['owner']} / 함께 볼 사람: {task['support']}")
        add_bullet(doc, f"하실 일: {task['do']}")
        add_bullet(doc, f"산출물 예시: {task['example']}")
        add_bullet(doc, f"남길 위치 예시: {task['output']}")
        add_bullet(doc, f"완료 기준: {task['done']}")

    doc.add_heading("5. Paper B 작업 설명", level=1)
    for task in [t for t in TASKS if t["paper"] == "Paper B"]:
        doc.add_heading(f"{task['id']}. {task['title']}", level=2)
        add_bullet(doc, f"담당: {task['owner']} / 함께 볼 사람: {task['support']}")
        add_bullet(doc, f"하실 일: {task['do']}")
        add_bullet(doc, f"산출물 예시: {task['example']}")
        add_bullet(doc, f"남길 위치 예시: {task['output']}")
        add_bullet(doc, f"완료 기준: {task['done']}")

    doc.add_heading("6. 파일을 못 찾으실 때", level=1)
    add_bullet(doc, "Paper A 포함 판단 과정은 00_shared/Paper_A_포함판단_과정_설명서_20260617.docx를 먼저 보시면 됩니다.")
    add_bullet(doc, "Paper A 선행연구 PDF와 메모는 00_INDEX/2026-06-17_Paper_A_B_work_allocation/References/Paper_A 안에 모읍니다.")
    add_bullet(doc, "원고는 보통 05_manuscripts 안에서 찾으시면 됩니다.")
    add_bullet(doc, "R1-R4 원자료와 워크북은 01_workbooks 안에서 찾으시면 됩니다.")
    add_bullet(doc, "원문 확인 결정, 최종 기준표, 출처 확인 관련 파일은 03_source_adjudication 안에서 찾으시면 됩니다.")
    add_bullet(doc, "분석 결과, 모델 비교 산출물, MASEM 관련 표는 04_analysis_outputs 안에서 먼저 찾아 주세요.")
    add_bullet(doc, "원자료, 원고 원본, 기존 결과표는 덮어쓰지 말고, 검토 메모와 수정 제안은 각자 담당 폴더에 새 파일로 남겨 주세요.")

    doc.add_heading("7. 참고 기준", level=1)
    add_table(
        doc,
        ["기준", "이 문서에서 쓰는 이유", "링크"],
        [[r["short"], r["use"], r["url"]] for r in REFERENCES],
    )

    doc.add_heading("8. 중요한 표현", level=1)
    add_bullet(doc, "Paper A의 full10은 이론적 목표 구조와 근거 지도를 보여주는 것입니다. 단일 최종 구조모형 추정처럼 쓰지 말아 주세요.")
    add_bullet(doc, "Paper A의 core7과 trust6는 현재 경험적으로 추정 가능한 모델군 경로입니다.")
    add_bullet(doc, "Paper B는 출처를 확인해 만든 최종 기준표를 기준으로 설명해 주세요. 절대적 정답처럼 읽히는 표현은 피해 주세요.")
    add_bullet(doc, "Paper B 모델 비교 결과는 원고 근거로 쓸 수 있지만, 전체 구성개념/전체 행에서 구조모형 대체가 안정적이라는 최종 주장으로 바로 쓰면 안 됩니다.")

    footer = doc.sections[0].footer.paragraphs[0]
    footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
    fr = footer.add_run(f"생성일 {date.today().isoformat()} | AI Adoption Meta Analysis")
    fr.font.size = Pt(8)
    set_korean_font(fr)

    doc.save(GUIDE_DOCX)


def build_paper_a_process_docs() -> None:
    lines = [
        "# Paper A 포함 판단 과정 설명서",
        "",
        "이 문서는 A2 작업을 위한 연구자용 설명서입니다. 새 포함/제외 판단을 만들라는 문서가 아니라, 이미 진행된 인간 검토와 AI 보조 선별 절차를 Methods에 정확히 설명하기 위한 기준 문서입니다.",
        "",
        "## 핵심 구분",
        "",
        "- 인간 검토: 최종 포함/제외 판단과 원문 확인의 책임이 있는 단계입니다.",
        "- AI 보조 선별: 대량 문헌 후보를 줄이고 검토 우선순위를 돕는 단계입니다. 최종 포함 결정을 AI가 했다고 쓰면 안 됩니다.",
        "- 최종 포함 기준: 현재 작업 기준은 225개 포함 행, 중복 DOI 1건 병합, 224개 고유 포함 보고서/연구입니다.",
        "",
        "## 반드시 확인할 파일",
        "",
        "- 루트: `90_repository_mirror/journal_AI-adoption_meta`",
        "- `data/02_screening/screening_summary.json`",
        "- `data/02_screening/human_screening_results_consolidated.csv`",
        "- `paper_a/PRISMA_COUNTS_LOCK_20260615.md`",
        "- `paper_a/PRISMA_COUNTS_REVIEW_NEEDED_20260615.md`",
        "- `03_source_adjudication/Paper_A/2026-06-14_human_process_candidate_audit/REVIEW_THIS_PAPER_A_HUMAN_PROCESS_AUDIT_20260614.docx`",
        "- `03_source_adjudication/Paper_A/2026-06-14_human_style_source_adjudication/PAPER_A_HUMAN_STYLE_SOURCE_ADJUDICATION_GUIDE_20260614.docx`",
        "",
        "## Methods에 반영할 때 확인할 질문",
        "",
        "1. 검색, 중복 제거, AI 보조 선별, 인간 검토, 원문 확인, 최종 포함이 순서대로 설명되어 있습니까?",
        "2. AI 보조 선별이 최종 포함 판단처럼 읽히지 않습니까?",
        "3. 657개 인간 검토, 225개 포함 행, 224개 고유 포함 보고서/연구의 관계가 독자에게 분명합니까?",
        "4. PRISMA 수치와 Methods 문장이 서로 다른 기준을 쓰지 않습니까?",
        "5. 불확실한 항목은 원고에 단정적으로 쓰지 않고 PI 확인 대상으로 남겨 두었습니까?",
        "",
        "## 피해야 할 표현",
        "",
        "- AI가 최종 포함 연구를 결정했다.",
        "- 225개 연구가 최종 분석에 포함되었다.",
        "- PRISMA 수치가 이미 최종 확정되었다.",
        "",
        "## 권장 표현 방향",
        "",
        "- AI 보조 선별은 인간 검토를 돕는 후보 축소 및 우선순위화 절차로 설명합니다.",
        "- 최종 포함 판단은 인간 검토와 원문 확인을 거친 연구자 판단으로 설명합니다.",
        "- 225개 포함 행과 224개 고유 포함 보고서/연구는 서로 다른 단위라는 점을 Methods와 Results에서 일관되게 씁니다.",
    ]
    PAPER_A_PROCESS_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")

    doc = Document()
    style_doc(doc)
    title = doc.add_paragraph()
    run = title.add_run("Paper A 포함 판단 과정 설명서")
    run.font.size = Pt(20)
    run.font.bold = True
    run.font.color.rgb = RGBColor(31, 78, 121)
    set_korean_font(run)

    intro = doc.add_paragraph()
    intro_run = intro.add_run(
        "이 문서는 A2 작업을 위한 연구자용 설명서입니다. 새 포함/제외 판단을 만들라는 문서가 아니라, "
        "이미 진행된 인간 검토와 AI 보조 선별 절차를 Methods에 정확히 설명하기 위한 기준 문서입니다."
    )
    set_korean_font(intro_run)

    doc.add_heading("1. 핵심 구분", level=1)
    add_bullet(doc, "인간 검토: 최종 포함/제외 판단과 원문 확인의 책임이 있는 단계입니다.")
    add_bullet(doc, "AI 보조 선별: 대량 문헌 후보를 줄이고 검토 우선순위를 돕는 단계입니다. 최종 포함 결정을 AI가 했다고 쓰면 안 됩니다.")
    add_bullet(doc, "최종 포함 기준: 현재 작업 기준은 225개 포함 행, 중복 DOI 1건 병합, 224개 고유 포함 보고서/연구입니다.")

    doc.add_heading("2. 반드시 확인할 파일", level=1)
    for item in [
        "루트: 90_repository_mirror/journal_AI-adoption_meta",
        "data/02_screening/screening_summary.json",
        "data/02_screening/human_screening_results_consolidated.csv",
        "paper_a/PRISMA_COUNTS_LOCK_20260615.md",
        "paper_a/PRISMA_COUNTS_REVIEW_NEEDED_20260615.md",
        "03_source_adjudication/Paper_A/2026-06-14_human_process_candidate_audit/REVIEW_THIS_PAPER_A_HUMAN_PROCESS_AUDIT_20260614.docx",
        "03_source_adjudication/Paper_A/2026-06-14_human_style_source_adjudication/PAPER_A_HUMAN_STYLE_SOURCE_ADJUDICATION_GUIDE_20260614.docx",
    ]:
        add_bullet(doc, item)

    doc.add_heading("3. Methods에 반영할 때 확인할 질문", level=1)
    for item in [
        "검색, 중복 제거, AI 보조 선별, 인간 검토, 원문 확인, 최종 포함이 순서대로 설명되어 있습니까?",
        "AI 보조 선별이 최종 포함 판단처럼 읽히지 않습니까?",
        "657개 인간 검토, 225개 포함 행, 224개 고유 포함 보고서/연구의 관계가 독자에게 분명합니까?",
        "PRISMA 수치와 Methods 문장이 서로 다른 기준을 쓰지 않습니까?",
        "불확실한 항목은 원고에 단정적으로 쓰지 않고 PI 확인 대상으로 남겨 두었습니까?",
    ]:
        add_numbered(doc, item)

    doc.add_heading("4. 피해야 할 표현과 권장 방향", level=1)
    add_table(
        doc,
        ["피해야 할 표현", "권장 방향"],
        [
            ["AI가 최종 포함 연구를 결정했다.", "AI 보조 선별은 인간 검토를 돕는 후보 축소 및 우선순위화 절차로 설명합니다."],
            ["225개 연구가 최종 분석에 포함되었다.", "225개 포함 행과 224개 고유 포함 보고서/연구는 서로 다른 단위라고 씁니다."],
            ["PRISMA 수치가 이미 최종 확정되었다.", "Methods/Results 투고 전 최종 확인 대상으로 남겨 둡니다."],
        ],
    )
    doc.save(PAPER_A_PROCESS_DOCX)


def build_paper_a_references_folder() -> None:
    pdf_dir = PAPER_A_REFERENCES_DIR / "pdfs"
    notes_dir = PAPER_A_REFERENCES_DIR / "notes"
    request_dir = PAPER_A_REFERENCES_DIR / "to_request"
    for folder in [pdf_dir, notes_dir, request_dir]:
        folder.mkdir(parents=True, exist_ok=True)

    if LOCAL_PAPER_A_REFERENCE_PDFS.exists():
        for src in sorted(LOCAL_PAPER_A_REFERENCE_PDFS.glob("*.pdf")):
            dst = pdf_dir / src.name
            if not dst.exists():
                shutil.copy2(src, dst)

    (PAPER_A_REFERENCES_DIR / "README.md").write_text(
        "\n".join(
            [
                "# Paper A References",
                "",
                "이 폴더는 Paper A의 Introduction, 이론적 배경, Discussion, References를 보강하기 위한 연구자용 선행연구 큐입니다.",
                "",
                "## 폴더",
                "",
                "- `pdfs/`: R2-R4가 읽고 원고 보강에 사용할 선행연구 PDF",
                "- `notes/`: PDF별 핵심 주장, 원고 보강 위치, 인용 문장 후보",
                "- `to_request/`: 아직 확보하지 못했거나 도서관 접근이 필요한 문헌 목록",
                "",
                "## 기록 방법",
                "",
                "각 PDF를 읽은 뒤 `notes/`에 같은 파일명 또는 저자명으로 짧은 메모를 남겨 주세요. 메모에는 원고 어느 위치를 보강할지, 어떤 문장 후보를 넣을지, APA reference가 무엇인지 적어 주세요.",
                "",
                "이 폴더는 원고 보강을 위한 내부 연구자 작업 폴더입니다. 작업보드의 A4-A6 산출물과 함께 사용해 주세요.",
            ]
        )
        + "\n",
        encoding="utf-8",
    )


def build_markdown_files() -> None:
    guide_lines = [
        "# Paper A/B 연구자 작업안내",
        "",
        "이 문서는 R1-R4 연구자가 자신의 업무를 확인하고 진행 상태를 남기기 위한 안내입니다.",
        "",
        "## 먼저 열 파일",
        "",
        f"- 작업 상태 입력: `{BOARD_XLSX.name}`",
        f"- 자세한 안내 문서: `{GUIDE_DOCX.name}`",
        f"- Paper A 포함 판단 과정 설명: `{PAPER_A_PROCESS_DOCX.name}`",
        "- Paper A 선행연구 폴더: `../References/Paper_A/`",
        "",
        "## 상태 표시",
        "",
        "- 시작 전: 아직 착수하지 않은 일입니다.",
        "- 진행 중: 파일을 확인하거나 산출물을 작성 중입니다.",
        "- 검토 요청: PI 또는 다른 연구자 확인이 필요합니다.",
        "- 완료: 완료 기준을 충족했고 산출물 위치를 남긴 상태입니다.",
        "- 막힘: 자료 접근, 판단 기준, 원고 표현 때문에 진행이 멈춘 상태입니다.",
        "",
        "## 알림",
        "",
        "자동 이메일 알림은 이번 버전에서 사용하지 않습니다. 대신 작업보드에서 상태가 `완료`인 행을 PI가 확인할 수 있게 만들었습니다.",
        "",
        "## OneDrive 링크",
        "",
        "작업보드에는 OneDrive 공유공간 최상위 폴더 기준 경로 텍스트를 넣었습니다. SharePoint/OneDrive 웹 공유 링크를 발급하신 뒤에는 `웹 링크` 열에 붙여 넣으시면 됩니다.",
    ]
    GUIDE_MD.write_text("\n".join(guide_lines) + "\n", encoding="utf-8")

    README_MD.write_text(
        "\n".join(
            [
                "# 먼저 읽어주세요",
                "",
                "이 폴더는 Paper A/B 연구자 작업보드의 최신 공유 위치입니다.",
                "",
                f"1. 먼저 `{BOARD_XLSX.name}`를 열어 자신의 담당 행을 확인해 주세요.",
                f"2. 작업 설명은 `{GUIDE_DOCX.name}`에서 확인해 주세요.",
                f"3. Paper A 포함 판단 과정은 `{PAPER_A_PROCESS_DOCX.name}`에서 확인해 주세요.",
                "4. Paper A 선행연구 PDF와 메모는 `../References/Paper_A/`에 모아 주세요.",
                "5. 완료하셨으면 작업보드에서 상태를 `완료`로 바꾸고 산출물 위치를 적어 주세요.",
                "6. 자동 이메일 알림은 사용하지 않습니다. PI가 완료 행을 필터링해서 확인하는 방식입니다.",
                "7. 기존 기술 운영 문서는 `../99_archive/previous_technical_plan_20260617/`에 보관했습니다.",
                "",
                "웹 공유 링크가 필요한 경우 OneDrive/SharePoint에서 해당 파일의 `링크 복사`를 사용해 작업보드의 `웹 링크` 열에 붙여 넣어 주세요.",
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    template = "\n".join(
        [
            "# 완료 메모 템플릿",
            "",
            "- 작업 ID:",
            "- 담당자:",
            "- 완료일:",
            "- 확인한 파일:",
            "- 남긴 산출물:",
            "- 핵심 판단:",
            "- PI 확인이 필요한 점:",
            "- 다음 사람이 이어서 볼 점:",
            "",
        ]
    )
    (SHARED / "완료메모_템플릿_20260617.md").write_text(template, encoding="utf-8")


def write_role_readmes() -> None:
    for role in ["R1", "R2", "R3", "R4"]:
        role_dir = WORK_DIR / role
        role_dir.mkdir(parents=True, exist_ok=True)
        role_tasks = [t for t in TASKS if t["owner"] == role]
        lines = [
            f"# {role} 작업 폴더",
            "",
            "이 폴더에는 본인이 작성한 메모, 확인표, 수정안만 넣어 주세요. 공유 원자료나 원고 원본을 덮어쓰지 말아 주세요.",
            "",
            "## 먼저 여실 파일",
            "",
            f"- 전체 작업보드: `../00_shared/{BOARD_XLSX.name}`",
            f"- 작업안내: `../00_shared/{GUIDE_DOCX.name}`",
            "",
            "## 맡은 작업",
            "",
        ]
        for task in role_tasks:
            ref = ref_by_id(task["reference"])
            must_read = ref.get("must_read", "작업보드 참고파일 시트를 확인해 주세요.").replace("\n", "; ")
            lines.extend(
                [
                    f"### {task['id']}. {task['title']}",
                    "",
                    f"- 하실 일: {task['do']}",
                    f"- 참고 위치: {ref['label']}",
                    f"- 반드시 볼 파일: {must_read}",
                    f"- 산출물 예시: {task['example']}",
                    f"- 남길 위치 예시: `{task['output']}`",
                    f"- 완료 기준: {task['done']}",
                    "",
                ]
            )
        lines.extend(
            [
                "## 완료 메모",
                "",
                "작업을 끝내시면 `완료메모_템플릿_20260617.md` 형식으로 간단한 메모를 남겨 주세요.",
                "",
            ]
        )
        (role_dir / f"README_{role}_해야할일_20260617.md").write_text("\n".join(lines), encoding="utf-8")
        (role_dir / "완료메모_템플릿_20260617.md").write_text(
            "\n".join(
                [
                    "# 완료 메모",
                    "",
                    f"- 담당자: {role}",
                    "- 작업 ID:",
                    "- 완료일:",
                    "- 확인한 파일:",
                    "- 남긴 산출물:",
                    "- 핵심 판단:",
                    "- PI 확인이 필요한 점:",
                    "- 다음 사람이 이어서 볼 점:",
                    "",
                ]
            ),
            encoding="utf-8",
        )


def style_sheet(ws, title: str) -> None:
    ws.sheet_view.showGridLines = False
    ws.freeze_panes = "A7"
    ws["A1"] = title
    ws["A1"].font = Font(name="Malgun Gothic", size=16, bold=True, color="FFFFFF")
    ws["A1"].fill = PatternFill("solid", fgColor="1F4E79")
    ws["A1"].alignment = Alignment(horizontal="left", vertical="center")
    ws.row_dimensions[1].height = 28
    for row in ws.iter_rows():
        for cell in row:
            cell.font = Font(name="Malgun Gothic", size=10, color="1F1F1F")
            cell.alignment = Alignment(vertical="top", wrap_text=True)


def apply_table_style(ws, table_range: str, table_name: str) -> None:
    del table_name
    ws.auto_filter.ref = table_range


def add_validations(ws, first_row: int, last_row: int) -> None:
    status = DataValidation(type="list", formula1=f'"{",".join(STATUS_VALUES)}"', allow_blank=True)
    owner = DataValidation(type="list", formula1=f'"{",".join(ROLE_VALUES)}"', allow_blank=True)
    priority = DataValidation(type="list", formula1=f'"{",".join(PRIORITY_VALUES)}"', allow_blank=True)
    ws.add_data_validation(status)
    ws.add_data_validation(owner)
    ws.add_data_validation(priority)
    status.add(f"I{first_row}:I{last_row}")
    owner.add(f"C{first_row}:C{last_row}")
    priority.add(f"D{first_row}:D{last_row}")


def write_task_sheet(ws, tasks: list[dict], title: str, table_name: str) -> None:
    style_sheet(ws, title)
    ws["A2"] = "사용 방법"
    ws["B2"] = "상태를 바꾸고, 완료 표시일과 산출물 위치를 적어 주세요. 완료 행은 PI 확인 필요로 표시됩니다."
    ws["A3"] = "상태 값"
    ws["B3"] = "시작 전 / 진행 중 / 검토 요청 / 완료 / 막힘"
    ws["A4"] = "웹 링크"
    ws["B4"] = "SharePoint/OneDrive에서 링크 복사 후 붙여 넣을 수 있도록 빈 열을 두었습니다."
    headers = [
        "작업 ID",
        "논문",
        "담당자",
        "우선순위",
        "작업 이름",
        "지금 하실 일",
        "참고 위치",
        "산출물 예시",
        "상태",
        "완료 표시일",
        "PI 확인 필요",
        "PI 확인일",
        "남길 위치",
        "막힌 점/메모",
        "웹 링크",
    ]
    start = 6
    for col, header in enumerate(headers, 1):
        cell = ws.cell(start, col, header)
        cell.font = Font(name="Malgun Gothic", bold=True, color="FFFFFF")
        cell.fill = PatternFill("solid", fgColor="5B9BD5")
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    for r_idx, task in enumerate(tasks, start + 1):
        ref = ref_by_id(task["reference"])
        values = [
            task["id"],
            task["paper"],
            task["owner"],
            task["priority"],
            task["title"],
            task["do"],
            ref["label"],
            task["example"],
            "시작 전",
            "",
            f'=IF(I{r_idx}="완료","예","")',
            "",
            task["output"],
            "",
            ref.get("web", ""),
        ]
        for c_idx, value in enumerate(values, 1):
            cell = ws.cell(r_idx, c_idx, value)
            cell.alignment = Alignment(vertical="top", wrap_text=True)
        # Local OneDrive file links trigger repeated macOS Excel "Grant File Access"
        # prompts. Keep internal locations as readable text, and make only web
        # URLs clickable.
        if ref.get("web"):
            ws.cell(r_idx, 15).hyperlink = ref["web"]
            ws.cell(r_idx, 15).style = "Hyperlink"

    last = start + len(tasks)
    if tasks:
        apply_table_style(ws, f"A{start}:O{last}", table_name)
        add_validations(ws, start + 1, last)
        done_fill = PatternFill("solid", fgColor="E2F0D9")
        review_fill = PatternFill("solid", fgColor="FFF2CC")
        blocked_fill = PatternFill("solid", fgColor="F4CCCC")
        ws.conditional_formatting.add(f"A{start + 1}:O{last}", FormulaRule(formula=[f'$I{start + 1}="완료"'], fill=done_fill))
        ws.conditional_formatting.add(f"A{start + 1}:O{last}", FormulaRule(formula=[f'$I{start + 1}="검토 요청"'], fill=review_fill))
        ws.conditional_formatting.add(f"A{start + 1}:O{last}", FormulaRule(formula=[f'$I{start + 1}="막힘"'], fill=blocked_fill))

    widths = [10, 10, 10, 10, 28, 46, 28, 44, 14, 14, 14, 14, 32, 36, 34]
    for idx, width in enumerate(widths, 1):
        ws.column_dimensions[chr(64 + idx)].width = width
    for row in range(start + 1, last + 1):
        ws.row_dimensions[row].height = 72


def write_dashboard(ws) -> None:
    write_task_sheet(ws, TASKS, "전체 작업보드", "AllTasks")
    ws["D2"] = "전체 작업 수"
    ws["E2"] = '=COUNTA(A7:A200)'
    ws["D3"] = "완료"
    ws["E3"] = '=COUNTIF(I7:I200,"완료")'
    ws["D4"] = "막힘"
    ws["E4"] = '=COUNTIF(I7:I200,"막힘")'
    for cell in ["D2", "D3", "D4"]:
        ws[cell].font = Font(name="Malgun Gothic", bold=True, color="1F4E79")
    for cell in ["E2", "E3", "E4"]:
        ws[cell].font = Font(name="Malgun Gothic", bold=True)
        ws[cell].fill = PatternFill("solid", fgColor="EAF2F8")


def write_reference_sheet(ws) -> None:
    style_sheet(ws, "참고파일 목록")
    headers = ["ID", "논문", "파일 이름/위치", "언제 보나요", "OneDrive 내부 경로", "반드시 볼 파일", "웹 링크", "주의할 점"]
    start = 4
    for col, header in enumerate(headers, 1):
        c = ws.cell(start, col, header)
        c.font = Font(name="Malgun Gothic", bold=True, color="FFFFFF")
        c.fill = PatternFill("solid", fgColor="70AD47")
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    for row_idx, ref in enumerate(REFERENCE_FILES, start + 1):
        values = [
            ref["id"],
            ref["paper"],
            ref["label"],
            ref["when"],
            rel_link(ref["path"]) if ref.get("path") else "",
            ref.get("must_read", ""),
            ref.get("web", ""),
            ref["note"],
        ]
        for col_idx, value in enumerate(values, 1):
            cell = ws.cell(row_idx, col_idx, value)
            cell.alignment = Alignment(vertical="top", wrap_text=True)
        if ref.get("web"):
            ws.cell(row_idx, 7).hyperlink = ref["web"]
            ws.cell(row_idx, 7).style = "Hyperlink"
    apply_table_style(ws, f"A{start}:H{start + len(REFERENCE_FILES)}", "ReferenceFiles")
    widths = [14, 12, 34, 48, 56, 70, 38, 50]
    for idx, width in enumerate(widths, 1):
        ws.column_dimensions[chr(64 + idx)].width = width
    for row in range(start + 1, start + len(REFERENCE_FILES) + 1):
        ws.row_dimensions[row].height = 112


def write_use_sheet(ws) -> None:
    style_sheet(ws, "사용방법")
    rows = [
        ("1", "자신의 시트 또는 전체보기에서 담당자 열을 필터링합니다."),
        ("2", "참고파일 시트에서 루트 폴더와 반드시 볼 파일명을 확인한 뒤 OneDrive에서 해당 파일을 열어 주세요."),
        ("3", "작업을 시작하면 상태를 진행 중으로 바꿉니다."),
        ("4", "완료하셨으면 상태를 완료로 바꾸고 완료 표시일, 남길 위치, 메모를 적습니다."),
        ("5", "판단이 필요하면 상태를 검토 요청 또는 막힘으로 바꾸고, 메모에 질문을 구체적으로 남겨 주세요."),
    ]
    ws["A3"] = "순서"
    ws["B3"] = "하실 일"
    for c in ["A3", "B3"]:
        ws[c].font = Font(name="Malgun Gothic", bold=True, color="FFFFFF")
        ws[c].fill = PatternFill("solid", fgColor="5B9BD5")
    for idx, row in enumerate(rows, 4):
        ws.cell(idx, 1, row[0])
        ws.cell(idx, 2, row[1])
    ws["A10"] = "주의"
    ws["B10"] = "원자료, 원고 원본, 기존 결과표는 덮어쓰지 말고, 검토 메모와 수정 제안은 각자 담당 폴더에 새 파일로 남겨 주세요."
    ws["A11"] = "링크"
    ws["B11"] = "macOS Word/Excel 권한 팝업을 피하기 위해 로컬 OneDrive 파일은 클릭 링크가 아니라 경로 텍스트로 넣었습니다. 실제 공유 링크가 필요하면 SharePoint/OneDrive에서 링크 복사 후 웹 링크 열에 붙여 넣어 주세요."
    for row in range(4, 12):
        ws.row_dimensions[row].height = 34
    ws.column_dimensions["A"].width = 14
    ws.column_dimensions["B"].width = 110
    for row in ws.iter_rows(min_row=3, max_row=11, min_col=1, max_col=2):
        for cell in row:
            cell.alignment = Alignment(vertical="top", wrap_text=True)


def write_citations_sheet(ws) -> None:
    style_sheet(ws, "참고 기준")
    headers = ["기준", "이 보드에서 쓰는 이유", "인용/출처", "URL"]
    start = 4
    for col, header in enumerate(headers, 1):
        c = ws.cell(start, col, header)
        c.font = Font(name="Malgun Gothic", bold=True, color="FFFFFF")
        c.fill = PatternFill("solid", fgColor="70AD47")
    for row_idx, ref in enumerate(REFERENCES, start + 1):
        ws.cell(row_idx, 1, ref["short"])
        ws.cell(row_idx, 2, ref["use"])
        ws.cell(row_idx, 3, ref["citation"])
        ws.cell(row_idx, 4, ref["url"])
        ws.cell(row_idx, 4).hyperlink = ref["url"]
        ws.cell(row_idx, 4).style = "Hyperlink"
    apply_table_style(ws, f"A{start}:D{start + len(REFERENCES)}", "Citations")
    widths = [18, 58, 62, 52]
    for idx, width in enumerate(widths, 1):
        ws.column_dimensions[chr(64 + idx)].width = width
    for row in range(start + 1, start + len(REFERENCES) + 1):
        ws.row_dimensions[row].height = 48


def build_workbook() -> None:
    wb = Workbook()
    ws = wb.active
    ws.title = "전체보기"
    write_dashboard(ws)

    paper_a = wb.create_sheet("Paper A")
    write_task_sheet(paper_a, [t for t in TASKS if t["paper"] == "Paper A"], "Paper A 작업", "PaperATasks")

    paper_b = wb.create_sheet("Paper B")
    write_task_sheet(paper_b, [t for t in TASKS if t["paper"] == "Paper B"], "Paper B 작업", "PaperBTasks")

    for role in ["R1", "R2", "R3", "R4"]:
        sheet = wb.create_sheet(role)
        write_task_sheet(sheet, [t for t in TASKS if t["owner"] == role], f"{role} 담당 작업", f"{role}Tasks")

    refs = wb.create_sheet("참고파일")
    write_reference_sheet(refs)

    use = wb.create_sheet("사용방법")
    write_use_sheet(use)

    citations = wb.create_sheet("참고 기준")
    write_citations_sheet(citations)

    for ws in wb.worksheets:
        thin = Side(style="thin", color="D9E2F3")
        for row in ws.iter_rows():
            for cell in row:
                cell.border = Border(left=thin, right=thin, top=thin, bottom=thin)
        ws.sheet_properties.pageSetUpPr.fitToPage = True
        ws.page_setup.fitToWidth = 1
        ws.page_setup.fitToHeight = 0

    wb.calculation.fullCalcOnLoad = True
    wb.calculation.forceFullCalc = True
    wb.properties.title = "Paper A/B 연구자 작업보드"
    wb.properties.subject = "AI Adoption Meta Analysis researcher task board"
    wb.properties.creator = "Codex"
    wb.save(BOARD_XLSX)


def main() -> None:
    SHARED.mkdir(parents=True, exist_ok=True)
    for role in ["R1", "R2", "R3", "R4"]:
        (WORK_DIR / role).mkdir(parents=True, exist_ok=True)
    moved = archive_old_shared_files()
    build_paper_a_references_folder()
    build_paper_a_process_docs()
    build_workbook()
    build_guide_docx()
    build_markdown_files()
    write_role_readmes()
    print(f"shared={SHARED}")
    print(f"board={BOARD_XLSX}")
    print(f"guide={GUIDE_DOCX}")
    print(f"archived={len(moved)}")
    for item in moved:
        print(f"archived_file={item}")


if __name__ == "__main__":
    main()
