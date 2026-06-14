#!/usr/bin/env python3
"""Triage all Paper A AI missing-pair candidates by human-supported construct sets.

This is a gate before source-value extraction. It asks whether each candidate's
two constructs are already source-supported somewhere in the human/latest/frozen
row set for that study. It does not add values to the matrix.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[2]
ONEDRIVE_BASE = Path('/Users/newhosung/Library/CloudStorage/OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity/AI Adoption Meta Analysis - Documents')
CANON = ONEDRIVE_BASE / 'Meta/AI Adoption/03_source_adjudication/Paper_A/2026-06-14_broader_ai_candidate_triage'
REPO_OUT = ROOT / 'data/04_extraction/05_llm_masem_substitution/results/paper_a_broader_ai_candidate_triage_20260614'
TRACE = ROOT / 'data/04_extraction/05_llm_masem_substitution/results/paper_a_ai_candidate_source_trace_20260614/paper_a_ai_candidate_full10_densification_trace_20260614.csv'
LATEST = ROOT / 'data/04_extraction/05_llm_masem_substitution/results/paper_a_latest_human_workbook_audit_20260614/paper_a_latest_human_workbook_direct_r_input_20260614.csv'
FROZEN = ROOT / 'data/04_extraction/04_reference_standard_freeze/full_corpus_reference_standard_frozen_20260609.csv'
STATUS = ROOT / 'data/04_extraction/04_reference_standard_freeze/full_corpus_reference_standard_study_status_frozen_20260609.csv'

CSV_OUT = 'paper_a_broader_ai_candidate_construct_support_triage_20260614.csv'
SUMMARY_OUT = 'PAPER_A_BROADER_AI_CANDIDATE_CONSTRUCT_SUPPORT_TRIAGE_20260614.md'
TOP_OUT = 'paper_a_broader_ai_candidate_source_review_priority_20260614.csv'


def pair_key(c1: str, c2: str) -> str:
    return '--'.join(sorted([c1.strip(), c2.strip()]))


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline='', encoding='utf-8-sig') as f:
        return list(csv.DictReader(f))


def build_reference_indexes() -> tuple[dict[str, set[str]], dict[str, set[str]], dict[tuple[str, str], list[str]], dict[str, str]]:
    constructs_by_study: dict[str, set[str]] = defaultdict(set)
    pairs_by_study: dict[str, set[str]] = defaultdict(set)
    pair_sources: dict[tuple[str, str], list[str]] = defaultdict(list)

    for label, path in [('latest', LATEST), ('frozen', FROZEN)]:
        for row in read_csv(path):
            sid = (row.get('study_id') or '').strip()
            c1 = (row.get('construct_1') or '').strip()
            c2 = (row.get('construct_2') or '').strip()
            if not sid or not c1 or not c2:
                continue
            pk = pair_key(c1, c2)
            constructs_by_study[sid].update([c1, c2])
            pairs_by_study[sid].add(pk)
            source = row.get('source_file') or row.get('decision_status') or label
            pair_sources[(sid, pk)].append(f'{label}:{source}')

    status_by_study: dict[str, str] = {}
    if STATUS.exists():
        for row in read_csv(STATUS):
            sid = (row.get('study_id') or '').strip()
            if not sid:
                continue
            status_by_study[sid] = ';'.join(f'{k}={v}' for k, v in row.items() if k and v and k in {'reference_status','exclusion_code','decision_status','status','rationale','notes'})
    return constructs_by_study, pairs_by_study, pair_sources, status_by_study


def classify_candidate(row: dict[str, str], constructs_by_study: dict[str, set[str]], pairs_by_study: dict[str, set[str]], pair_sources: dict[tuple[str, str], list[str]], status_by_study: dict[str, str]) -> dict[str, str]:
    sid = row['study_id'].strip()
    c1 = row['construct_1'].strip()
    c2 = row['construct_2'].strip()
    pk = pair_key(c1, c2)
    supported = constructs_by_study.get(sid, set())
    pair_present = pk in pairs_by_study.get(sid, set())
    c1_supported = c1 in supported
    c2_supported = c2 in supported
    status = status_by_study.get(sid, '')
    status_l = status.lower()

    if 'excluded' in status_l or 'exclude' in status_l or 'no_target' in status_l:
        triage = 'exclude_human_study_status'
        action = 'do_not_add'
        reason = 'Frozen study status indicates exclusion/no-target handling.'
    elif pair_present:
        triage = 'already_in_human_or_frozen_reference'
        action = 'do_not_add_duplicate'
        reason = 'Exact unordered pair is already present in latest/frozen human-supported rows.'
    elif c1_supported and c2_supported:
        triage = 'source_review_priority_both_constructs_human_supported'
        action = 'review_pdf_for_numeric_cell_and_add_if_confirmed'
        reason = 'Both constructs are already human/frozen-supported for this study, but this exact pair is missing. If the source matrix contains the numeric cell, this is the strongest add-candidate class.'
    elif c1_supported or c2_supported:
        triage = 'likely_false_positive_one_construct_not_human_supported'
        action = 'do_not_add_unless_reopened_by_source_evidence'
        missing = c2 if c1_supported else c1
        reason = f'Only one construct is human/frozen-supported for this study; missing construct={missing}. This usually indicates AI term-hit overreach or unapproved remap.'
    else:
        triage = 'likely_false_positive_no_construct_human_supported'
        action = 'do_not_add_unless_reopened_by_source_evidence'
        reason = 'Neither construct is human/frozen-supported for this study; likely AI term-hit overreach or source mismatch.'

    return {
        'ai_trace_status': row.get('ai_trace_status',''),
        'candidate_status': row.get('candidate_status',''),
        'study_id': sid,
        'missing_pair': row.get('missing_pair',''),
        'construct_1': c1,
        'construct_2': c2,
        'candidate_value': row.get('candidate_value',''),
        'present_full10_pairs': row.get('present_full10_pairs',''),
        'missing_full10_pairs': row.get('missing_full10_pairs',''),
        'supported_constructs_in_human_reference': ';'.join(sorted(supported)),
        'construct_1_human_supported': 'yes' if c1_supported else 'no',
        'construct_2_human_supported': 'yes' if c2_supported else 'no',
        'exact_pair_in_human_or_frozen_reference': 'yes' if pair_present else 'no',
        'exact_pair_sources': ';'.join(pair_sources.get((sid, pk), [])),
        'frozen_study_status_summary': status,
        'triage_class': triage,
        'recommended_action': action,
        'triage_reason': reason,
        'construct_1_terms_found': row.get('construct_1_terms_found',''),
        'construct_2_terms_found': row.get('construct_2_terms_found',''),
        'table_terms_found': row.get('table_terms_found',''),
        'pdf_path_local_only': row.get('pdf_path_local_only',''),
        'paper_b_boundary': row.get('paper_b_boundary',''),
    }


def main() -> None:
    constructs_by_study, pairs_by_study, pair_sources, status_by_study = build_reference_indexes()
    candidates = [r for r in read_csv(TRACE) if r.get('ai_trace_status') == 'possible_densification_source_review_candidate']
    rows = [classify_candidate(r, constructs_by_study, pairs_by_study, pair_sources, status_by_study) for r in candidates]
    rows.sort(key=lambda r: (r['triage_class'], r['study_id'], r['missing_pair']))
    priority = [r for r in rows if r['triage_class'] == 'source_review_priority_both_constructs_human_supported']

    for outdir in [REPO_OUT, CANON]:
        outdir.mkdir(parents=True, exist_ok=True)
        with (outdir / CSV_OUT).open('w', newline='', encoding='utf-8-sig') as f:
            writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            writer.writeheader()
            writer.writerows(rows)
        with (outdir / TOP_OUT).open('w', newline='', encoding='utf-8-sig') as f:
            writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            writer.writeheader()
            writer.writerows(priority)

    counts = Counter(r['triage_class'] for r in rows)
    by_study_priority = Counter(r['study_id'] for r in priority)
    lines = [
        '# Paper A broader AI-candidate construct-support triage',
        '',
        'Date: 2026-06-14',
        '',
        '## Purpose',
        '',
        'This gate reclassifies all possible AI/source-trace densification candidates by checking whether each candidate pair uses constructs already supported in the latest/frozen human reference for that study.',
        '',
        'It does not add values to the matrix. It identifies which candidates deserve PDF-level numeric-cell review.',
        '',
        '## Triage counts',
        '',
    ]
    for k, v in counts.most_common():
        lines.append(f'- {k}: {v}')
    lines.extend(['', '## Source-review priority candidates by study', ''])
    for sid, v in by_study_priority.most_common():
        lines.append(f'- {sid}: {v}')
    lines.extend(['', '## Interpretation', ''])
    lines.append('Candidates in `source_review_priority_both_constructs_human_supported` are the only class that should move to detailed PDF/source numeric-cell extraction now.')
    lines.append('Candidates with one or both constructs unsupported should not be added unless a source review explicitly reopens construct mapping.')
    lines.extend(['', '## Outputs', '', f'- Full triage CSV: `{CSV_OUT}`', f'- Source-review priority CSV: `{TOP_OUT}`', ''])
    for outdir in [REPO_OUT, CANON]:
        (outdir / SUMMARY_OUT).write_text('\n'.join(lines), encoding='utf-8')
        (outdir / 'README_BROADER_AI_CANDIDATE_TRIAGE_20260614.md').write_text(
            f"# Paper A broader AI-candidate triage\n\nPrimary summary:\n\n`{outdir / SUMMARY_OUT}`\n\nPriority CSV:\n\n`{outdir / TOP_OUT}`\n\nFull CSV:\n\n`{outdir / CSV_OUT}`\n",
            encoding='utf-8'
        )

    print(CANON / SUMMARY_OUT)
    print(CANON / TOP_OUT)
    print(CANON / CSV_OUT)
    print('candidates=', len(rows))
    print('counts=', dict(counts))
    print('priority_by_study=', dict(by_study_priority))

if __name__ == '__main__':
    main()
