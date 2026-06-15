#!/usr/bin/env python3
from __future__ import annotations

import csv
import re
import subprocess
from pathlib import Path

ROOT = Path('/Users/newhosung/Academic/2026/AI Adoption Meta Analysis')
BASE = ROOT / 'references/paper_a_apa7_evidence_review_20260615'
PDF_DIR = BASE / 'pdfs'
TEXT_DIR = BASE / 'text_extracts'
NOTE_DIR = BASE / 'notes'
TEXT_DIR.mkdir(parents=True, exist_ok=True)
NOTE_DIR.mkdir(parents=True, exist_ok=True)

MANUAL = {
    'Cheung_2008_fixed_random_mixed_effects_SEM': ('MASEM method', 'Use to justify fixed/random/mixed-effects SEM logic and to explain why heterogeneity and matrix structure govern claims.'),
    'Cheung_2015_metaSEM_Frontiers': ('MASEM implementation', 'Use to describe metaSEM reproducibility, TSSEM workflow, and why code/materials should be archived.'),
    'Dwivedi_2019_reexamining_UTAUT': ('UTAUT theory', 'Use to strengthen model-history narrative from TAM/UTAUT toward AI adoption and to define PE/EE/SI/FC roles.'),
    'Hamkah_2025_engineering_students_AI_acceptance': ('AI adoption empirical exemplar', 'Use as recent AI acceptance reporting exemplar for construct tables, structural model visuals, and student-context framing.'),
    'Jak_2015_MASEM_chapter': ('MASEM method', 'Use to explain Stage 1/Stage 2 MASEM, path diagrams, and model fit reporting.'),
    'Jak_Cheung_2020_MASEM_moderating_effects': ('MASEM moderation/method', 'Use to justify why moderation/future subgroup claims require sufficient matrix structure rather than speculation.'),
    'Labadze_2023_AI_chatbots_education_review': ('AI education review exemplar', 'Use to improve systematic-review narrative, categorization tables, and education-specific AI context.'),
    'Oc_2025_GenAI_higher_ed_risk_trust_UTAUT': ('GenAI UTAUT/trust/risk exemplar', 'Use to strengthen trust/risk mechanism framing and show how UTAUT extensions are diagrammed.'),
    'Zhang_2022_MASEM_primer': ('MASEM reporting exemplar', 'Use to improve explanation of pooled correlation matrices, model diagrams, and fit tables.'),
    'metaSEM_CRAN_manual_2026': ('software/reproducibility', 'Use to document package version, functions, and reproducible TSSEM/MASEM script requirements.'),
}

CAPTION_RE = re.compile(r'^(Table|TABLE|Figure|FIGURE|Fig\.?|FIG\.?)\s+\d+[\w.:-]*\s*(.*)$')
SECTION_RE = re.compile(r'^(Abstract|Introduction|Method|Methods|Results|Discussion|Conclusion|References)\b', re.I)

def pdf_pages(pdf: Path) -> str:
    try:
        out = subprocess.check_output(['pdfinfo', str(pdf)], text=True, stderr=subprocess.DEVNULL)
        for line in out.splitlines():
            if line.startswith('Pages:'):
                return line.split(':', 1)[1].strip()
    except Exception:
        return ''
    return ''

def extract_text(pdf: Path) -> str:
    txt = TEXT_DIR / (pdf.stem + '.txt')
    subprocess.run(['pdftotext', '-layout', str(pdf), str(txt)], check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return txt.read_text(encoding='utf-8', errors='ignore') if txt.exists() else ''

rows = []
md = ['# Paper A reference PDF review: APA7 table/figure and procedure strengthening', '', 'Generated: 2026-06-15', '', 'Copyright boundary: PDFs are stored for local scholarly review only. External tables/figures should not be copied into the manuscript unless license/permission allows it. The manuscript should recreate original tables/figures from project data while citing these sources as design/method exemplars.', '']
for pdf in sorted(PDF_DIR.glob('*.pdf')):
    stem = pdf.stem
    text = extract_text(pdf)
    lines = [re.sub(r'\s+', ' ', line.strip()) for line in text.splitlines() if line.strip()]
    captions = []
    sections = []
    for line in lines:
        if CAPTION_RE.match(line) and len(line) < 220:
            captions.append(line)
        elif SECTION_RE.match(line) and len(line) < 80:
            sections.append(line)
    captions = captions[:12]
    sections = sections[:12]
    role, use = MANUAL.get(stem, ('reference exemplar', 'Use for manuscript strengthening after manual review.'))
    row = {
        'file': str(pdf.relative_to(ROOT)),
        'pages': pdf_pages(pdf),
        'bytes': pdf.stat().st_size,
        'review_role': role,
        'detected_caption_count_first12': len(captions),
        'detected_section_count_first12': len(sections),
        'manuscript_use': use,
        'first_detected_captions': ' || '.join(captions[:5]),
    }
    rows.append(row)
    md += [f'## {stem}', '', f'- File: `{row["file"]}`', f'- Pages: {row["pages"]}', f'- Review role: {role}', f'- Manuscript use: {use}', '- Detected table/figure caption examples:']
    if captions:
        md += [f'  - {c}' for c in captions[:8]]
    else:
        md += ['  - No clean caption lines detected by text extraction; visual/manual review still needed.']
    md += ['']

csv_path = BASE / 'paper_a_reference_pdf_review_20260615.csv'
with csv_path.open('w', newline='', encoding='utf-8') as f:
    fieldnames = ['file','pages','bytes','review_role','detected_caption_count_first12','detected_section_count_first12','manuscript_use','first_detected_captions']
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader(); w.writerows(rows)
md += ['# Cross-paper design implications for Paper A', '', '- Add tables/figures in text near first mention, not only at the end.', '- Add a model genealogy table before results so reviewers understand how full10, core7, trust6, ANX, and SE relate.', '- Add a method flow figure/table that separates theory reconstruction, source-anchored extraction, matrix feasibility diagnosis, TSSEM/MASEM, and supplemental diagnostics.', '- Keep full10 as a theoretical evidence map and report core7/trust6 as estimable model-family descendants.', '- Add a PE-vs-EE role-comparison table because usefulness and effort are different mechanisms, not a single association.', '- Add an ANX/SE feasibility table to show that these mechanisms are retained but currently underidentified.', '- Avoid copying external figures/tables; recreate original visuals with Paper A data and cite methodological exemplars.', '']
md_path = NOTE_DIR / 'PAPER_A_REFERENCE_PDF_REVIEW_AND_MANUSCRIPT_STRENGTHENING_20260615.md'
md_path.write_text('\n'.join(md), encoding='utf-8')
print(f'Wrote {csv_path}')
print(f'Wrote {md_path}')
print(f'Reviewed PDFs: {len(rows)}')
