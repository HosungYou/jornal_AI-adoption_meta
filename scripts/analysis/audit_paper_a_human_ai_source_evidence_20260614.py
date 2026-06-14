#!/usr/bin/env python3
"""Audit Paper A latest-human rows and Paper B/C AI procedure evidence.

This script is deliberately share-safe: it records source/PDF presence and
numeric hit/miss flags, but it does not copy PDFs, source packets, model raw
transcripts, or source quotes into Git-tracked outputs.
"""
import csv, itertools, math, re, shutil, subprocess
from collections import Counter, defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
RESULT_ROOT = REPO / 'data/04_extraction/05_llm_masem_substitution/results'
OUT = RESULT_ROOT / 'paper_a_human_ai_source_evidence_audit_20260614'
OUT.mkdir(parents=True, exist_ok=True)
LATEST_INPUT = RESULT_ROOT / 'paper_a_latest_human_workbook_audit_20260614/paper_a_latest_human_workbook_direct_r_input_20260614.csv'
SOURCE_REFERENCE_PACKAGE = REPO / 'data/04_extraction/07_paper_c_harness_benchmark/private/paper_a_source_reference_package_20260614'
SOURCE_PACKET_DIR = SOURCE_REFERENCE_PACKAGE / 'source_packets'
TASK_SHELL = REPO / 'data/04_extraction/05_llm_masem_substitution/full_corpus_step5_task_unit_shell_20260609.csv'
AI_MANIFEST = REPO / 'data/04_extraction/05_llm_masem_substitution/locked_outputs/FULL_CORPUS_M1_R_FULL_RUN_MANIFEST_20260612.csv'
AI_SCORE = RESULT_ROOT / 'paper_b_full_corpus_m1_raw_full_scored_20260612.csv'
AI_EXCEPTION_SCORE = RESULT_ROOT / 'paper_b_full_corpus_m1_raw_full_exception_layer_scored_20260612.csv'
AI_SCORE_SUMMARY = RESULT_ROOT / 'paper_b_full_corpus_m1_raw_full_score_summary_20260612.csv'
AI_EXCEPTION_SUMMARY = RESULT_ROOT / 'paper_b_full_corpus_m1_raw_full_exception_layer_scored_summary_20260612.csv'
PDF_ROOTS = [
    SOURCE_REFERENCE_PACKAGE / 'pdfs',
    Path('/Users/newhosung/Library/CloudStorage/OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity/AI Adoption Meta Analysis - Documents/Meta/AI Adoption/PDFs'),
    Path('/Users/newhosung/Library/CloudStorage/OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity/AI Adoption Meta Analysis - Documents/Meta/AI Adoption/R1/PDFs'),
    Path('/Users/newhosung/Library/CloudStorage/OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity/AI Adoption Meta Analysis - Documents/Meta/AI Adoption/R2/PDFs'),
    Path('/Users/newhosung/Library/CloudStorage/OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity/AI Adoption Meta Analysis - Documents/Meta/AI Adoption/R3/PDFs'),
    Path('/Users/newhosung/Library/CloudStorage/OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity/AI Adoption Meta Analysis - Documents/Meta/AI Adoption/R4/PDFs'),
    REPO / 'data/02_screening/pdfs',
]
FULL10 = ['PE','EE','SI','FC','HM','PV','TRU','ANX','SE','ATT','BI','UB']
# The current Paper A full10 route excludes FC/HM/PV and uses these 10 targets.
PAPER_A_FULL10 = ['PE','EE','SI','ATT','TRU','ANX','SE','BI','UB','FC']
PAPER_A_FULL10_PAIRS = {'-'.join(sorted(p)) for p in itertools.combinations(PAPER_A_FULL10, 2)}
PD_TEXT = shutil.which('pdftotext')

def read_csv(path):
    if not path.exists():
        return []
    with path.open(newline='', encoding='utf-8-sig') as f:
        return list(csv.DictReader(f))

def write_csv(path, rows, fields):
    with path.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader(); w.writerows(rows)

def pair(a, b):
    return '-'.join(sorted([str(a).strip(), str(b).strip()]))

def value_variants(x):
    try:
        f = float(str(x).strip())
    except Exception:
        return []
    vals = set()
    for d in (1, 2, 3, 4):
        s = f'{f:.{d}f}'
        vals.add(s)
        vals.add(s.replace('0.', '.'))
        vals.add(s.replace('-0.', '-.'))
        vals.add(s.replace('.', ','))
        vals.add(s.replace('0.', '.').replace('.', ','))
    vals.add(str(f))
    return sorted([v for v in vals if v not in {'0', '0.0', '.0'}], key=len, reverse=True)

def text_hit(text, variants):
    if not text:
        return False
    for v in variants:
        # avoid matching .46 inside 1.46, while still allowing table punctuation
        if re.search(r'(?<![0-9])' + re.escape(v) + r'(?![0-9])', text):
            return True
    return False

def read_text(path):
    try:
        return path.read_text(encoding='utf-8', errors='ignore')
    except Exception:
        return ''

def find_pdf(study_id):
    for root in PDF_ROOTS:
        p = root / f'{study_id}.pdf'
        if p.exists():
            return p
    return None

def pdf_text(path):
    if not path or not PD_TEXT:
        return '', 'missing_pdftotext' if not PD_TEXT else 'missing_pdf'
    try:
        r = subprocess.run([PD_TEXT, str(path), '-'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=20)
        if r.returncode == 0:
            return r.stdout, 'ok'
        return '', f'pdftotext_exit_{r.returncode}'
    except subprocess.TimeoutExpired:
        return '', 'pdftotext_timeout'
    except Exception as e:
        return '', f'pdftotext_error_{type(e).__name__}'

def boolstr(x):
    return 'true' if x else 'false'

def pct(num, den):
    return '' if den == 0 else f'{(100*num/den):.1f}'

human = [r for r in read_csv(LATEST_INPUT) if str(r.get('r_numeric','')).strip()]
pdf_cache = {}
packet_cache = {}
audit_rows = []
for r in human:
    sid = r['study_id']
    packet = SOURCE_PACKET_DIR / f'{sid}_source_packet_20260609.txt'
    if sid not in packet_cache:
        packet_cache[sid] = (packet.exists(), read_text(packet) if packet.exists() else '')
    pdf = find_pdf(sid)
    if sid not in pdf_cache:
        txt, status = pdf_text(pdf)
        pdf_cache[sid] = (pdf, txt, status)
    packet_exists, packet_text = packet_cache[sid]
    pdf_path, ptxt, pstatus = pdf_cache[sid]
    variants = value_variants(r['r_numeric'])
    audit_rows.append({
        'study_id': sid,
        'pair': pair(r.get('construct_1',''), r.get('construct_2','')),
        'construct_1': r.get('construct_1',''),
        'construct_2': r.get('construct_2',''),
        'r_numeric': r.get('r_numeric',''),
        'sample_size_numeric': r.get('sample_size_numeric',''),
        'source_file': r.get('source_file',''),
        'source_location_present': boolstr(bool(str(r.get('source_location','')).strip())),
        'flag_present': boolstr(bool(str(r.get('flag','')).strip())),
        'notes_present': boolstr(bool(str(r.get('notes','')).strip())),
        'source_packet_exists': boolstr(packet_exists),
        'value_found_in_source_packet_text': boolstr(text_hit(packet_text, variants)),
        'pdf_exists': boolstr(pdf_path is not None),
        'pdf_text_status': pstatus,
        'value_found_in_pdf_text': boolstr(text_hit(ptxt, variants)),
        'pdf_path_local_only': str(pdf_path) if pdf_path else '',
    })
fields = ['study_id','pair','construct_1','construct_2','r_numeric','sample_size_numeric','source_file','source_location_present','flag_present','notes_present','source_packet_exists','value_found_in_source_packet_text','pdf_exists','pdf_text_status','value_found_in_pdf_text','pdf_path_local_only']
write_csv(OUT / 'paper_a_latest_human_full_pdf_source_value_audit_20260614.csv', audit_rows, fields)

summary_rows = []
def summarize(group_name, rows):
    n = len(rows)
    summary_rows.append({
        'group': group_name,
        'rows': n,
        'studies': len({r['study_id'] for r in rows}),
        'pairs': len({r['pair'] for r in rows}),
        'source_packet_exists_rows': sum(r['source_packet_exists']=='true' for r in rows),
        'source_packet_value_hit_rows': sum(r['value_found_in_source_packet_text']=='true' for r in rows),
        'pdf_exists_rows': sum(r['pdf_exists']=='true' for r in rows),
        'pdf_text_ok_rows': sum(r['pdf_text_status']=='ok' for r in rows),
        'pdf_value_hit_rows': sum(r['value_found_in_pdf_text']=='true' for r in rows),
        'source_packet_value_hit_pct': pct(sum(r['value_found_in_source_packet_text']=='true' for r in rows), n),
        'pdf_value_hit_pct': pct(sum(r['value_found_in_pdf_text']=='true' for r in rows), n),
    })
summarize('all_latest_human_numeric_target_rows', audit_rows)
for source_file, rows in sorted(defaultdict(list, {k:[r for r in audit_rows if r['source_file']==k] for k in {r['source_file'] for r in audit_rows}}).items()):
    summarize(f'source_file::{source_file}', rows)
write_csv(OUT / 'paper_a_latest_human_full_pdf_source_value_audit_summary_20260614.csv', summary_rows, list(summary_rows[0].keys()))

# Full10 densification gaps from latest-human rows.
study_pairs = defaultdict(set)
study_n = defaultdict(set)
for r in human:
    sid = r['study_id']
    pr = pair(r.get('construct_1',''), r.get('construct_2',''))
    if pr in PAPER_A_FULL10_PAIRS:
        study_pairs[sid].add(pr)
        if r.get('sample_size_numeric'):
            study_n[sid].add(r['sample_size_numeric'])
gap_rows = []
for sid, pairs in sorted(study_pairs.items()):
    missing = sorted(PAPER_A_FULL10_PAIRS - pairs)
    gap_rows.append({
        'study_id': sid,
        'present_full10_pairs': len(pairs),
        'missing_full10_pairs': len(missing),
        'has_complete_full10_matrix': boolstr(len(missing)==0),
        'sample_size_values_seen': ';'.join(sorted(study_n[sid])),
        'missing_pairs': ';'.join(missing),
    })
write_csv(OUT / 'paper_a_full10_latest_human_densification_gaps_20260614.csv', gap_rows, ['study_id','present_full10_pairs','missing_full10_pairs','has_complete_full10_matrix','sample_size_values_seen','missing_pairs'])

# AI procedure evidence summary.
task_rows = read_csv(TASK_SHELL)
manifest_rows = read_csv(AI_MANIFEST)
score_rows = read_csv(AI_SCORE)
exception_rows = read_csv(AI_EXCEPTION_SCORE)
score_summary = read_csv(AI_SCORE_SUMMARY)
exception_summary = read_csv(AI_EXCEPTION_SUMMARY)
task_studies = {r['study_id'] for r in task_rows if r.get('study_id')}
packet_studies = {p.name.split('_')[0] for p in SOURCE_PACKET_DIR.glob('S*_source_packet_20260609.txt')}
manifest_locked = [r for r in manifest_rows if r.get('locked_status') == 'locked_model_output']
ai_proc_rows = []
def add_metric(metric, value, notes=''):
    ai_proc_rows.append({'metric': metric, 'value': str(value), 'notes': notes})
add_metric('task_shell_rows', len(task_rows), str(TASK_SHELL))
add_metric('task_shell_studies', len(task_studies), 'post-freeze target-row studies')
add_metric('source_packet_files_available', len(packet_studies), str(SOURCE_PACKET_DIR))
add_metric('task_shell_studies_with_source_packets', len(task_studies & packet_studies), 'study-id matched source packets')
add_metric('task_shell_studies_missing_source_packets', len(task_studies - packet_studies), ';'.join(sorted(task_studies - packet_studies)))
for k,v in Counter(r.get('denominator_family','') for r in task_rows).items():
    add_metric(f'task_denominator_family::{k}', v)
for k,v in Counter(r.get('evidence_family','') for r in task_rows).items():
    add_metric(f'task_evidence_family::{k}', v)
add_metric('locked_model_output_files', len(manifest_locked), str(AI_MANIFEST))
add_metric('locked_model_output_bytes_total', sum(int(r.get('bytes') or 0) for r in manifest_locked), 'registered locked model output files only')
add_metric('scored_rows_file_rows', len(score_rows), str(AI_SCORE))
add_metric('exception_layer_rows_file_rows', len(exception_rows), str(AI_EXCEPTION_SCORE))
for k,v in Counter(r.get('model_provider','') for r in score_rows).items():
    add_metric(f'scored_model_provider::{k}', v)
for k,v in Counter(r.get('model_id','') for r in score_rows).items():
    add_metric(f'scored_model_id::{k}', v)
for row in score_summary:
    label = row.get('denominator_family') or row.get('group') or row.get('metric') or 'score_summary_row'
    add_metric(f'score_summary::{label}', row, 'raw row serialized from score summary')
for row in exception_summary:
    label = row.get('post_exception_score_status') or row.get('denominator_family') or row.get('group') or 'exception_summary_row'
    add_metric(f'exception_summary::{label}', row, 'raw row serialized from exception summary')
write_csv(OUT / 'paper_a_ai_procedure_evidence_summary_20260614.csv', ai_proc_rows, ['metric','value','notes'])

report = []
report += ['# Paper A Human/AI Source Evidence Audit', '', 'Date: 2026-06-14', '']
report += ['## Scope', '', 'This audit documents the 2026-06-14 correction after the latest-human-workbook recheck. It is share-safe: PDFs, source packets, and raw model transcripts are not copied into the tracked output. The audit records whether local source packets/PDF text exist and whether coded numeric values are visible in extracted text.', '']
report += ['## Human coding evidence', '', f'- Latest-human numeric target rows audited: {len(audit_rows)}', f'- Studies represented: {len({r["study_id"] for r in audit_rows})}', f'- Construct pairs represented: {len({r["pair"] for r in audit_rows})}', f'- Rows with source packet present: {sum(r["source_packet_exists"]=="true" for r in audit_rows)}/{len(audit_rows)}', f'- Rows with coded value found in source-packet text: {sum(r["value_found_in_source_packet_text"]=="true" for r in audit_rows)}/{len(audit_rows)}', f'- Rows with local PDF present: {sum(r["pdf_exists"]=="true" for r in audit_rows)}/{len(audit_rows)}', f'- Rows with `pdftotext` status `ok`: {sum(r["pdf_text_status"]=="ok" for r in audit_rows)}/{len(audit_rows)}', f'- Rows with coded value found in PDF text: {sum(r["value_found_in_pdf_text"]=="true" for r in audit_rows)}/{len(audit_rows)}', '']
report += ['Important boundary: a missing string hit is not proof that the coding is wrong. PDF tables split values, remove leading zeroes, or render rows/columns in ways that defeat simple text search. Positive hits are supportive evidence; negative hits become source-level review candidates.', '']
report += ['## Full10 densification status from latest human workbooks', '', f'- Paper A full10 pair universe audited: {len(PAPER_A_FULL10_PAIRS)} pairs', f'- Studies with at least one full10 pair: {len(gap_rows)}', f'- Complete full10 study matrices: {sum(r["has_complete_full10_matrix"]=="true" for r in gap_rows)}', f'- Highest observed full10 pair count in one study: {max([int(r["present_full10_pairs"]) for r in gap_rows] or [0])}', '']
report += ['## AI coding procedure evidence', '', f'- Post-freeze Step 5 task-shell rows: {len(task_rows)}', f'- Post-freeze target studies: {len(task_studies)}', f'- Source-packet files available: {len(packet_studies)}', f'- Task-shell studies with matching source packets: {len(task_studies & packet_studies)}/{len(task_studies)}', f'- Locked M1-R model-output files registered: {len(manifest_locked)}', f'- Scored row file rows: {len(score_rows)}', f'- Exception-layer score rows: {len(exception_rows)}', '']
report += ['## Procedure-equivalence judgment', '', 'The AI coding procedure was not identical to the human coding procedure. Human coding used independent coder workbooks, pairwise disagreement review, and source-anchored adjudication before freezing the human reference. The AI M1-R condition used post-freeze source packets and locked-output schemas keyed to the frozen reference task shell. That design is appropriate for Paper B/Paper C validation because it prevents AI outputs from defining the reference standard.', '', 'For Paper A, the defensible primary premise is the source-anchored human/reference extraction, not that AI followed the same procedure as the human coders. AI-derived or AI-assisted rows can support substitution/sensitivity diagnostics only when they remain locked, source-packet-based, denominator-family separated, and compared against the frozen human reference.', '']
report += ['## Generated artifacts', '', '- `paper_a_latest_human_full_pdf_source_value_audit_20260614.csv`', '- `paper_a_latest_human_full_pdf_source_value_audit_summary_20260614.csv`', '- `paper_a_full10_latest_human_densification_gaps_20260614.csv`', '- `paper_a_ai_procedure_evidence_summary_20260614.csv`', '']
(OUT / 'PAPER_A_HUMAN_AI_SOURCE_EVIDENCE_AUDIT_20260614.md').write_text('\n'.join(report) + '\n', encoding='utf-8')
print('\n'.join(report))
