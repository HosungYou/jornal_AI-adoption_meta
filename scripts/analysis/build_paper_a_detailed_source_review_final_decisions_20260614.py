#!/usr/bin/env python3
"""Create final detailed source-review decisions for Paper A AI candidate rows."""
from pathlib import Path
import csv
from collections import Counter

ROOT = Path(__file__).resolve().parents[2]
ONEDRIVE_BASE = Path('/Users/newhosung/Library/CloudStorage/OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity/AI Adoption Meta Analysis - Documents')
CANON = ONEDRIVE_BASE / 'Meta/AI Adoption/03_source_adjudication/Paper_A/2026-06-14_detailed_source_review_final_decisions'
REPO_OUT = ROOT / 'data/04_extraction/05_llm_masem_substitution/results/paper_a_detailed_source_review_final_decisions_20260614'
TRACE = ROOT / 'data/04_extraction/05_llm_masem_substitution/results/paper_a_ai_candidate_source_trace_20260614/paper_a_ai_candidate_full10_densification_trace_20260614.csv'
CSV_NAME = 'paper_a_detailed_source_review_final_decisions_20260614.csv'
MD_NAME = 'PAPER_A_DETAILED_SOURCE_REVIEW_FINAL_DECISIONS_20260614.md'

EVIDENCE = {
    'S057': {
        'source_matrix': 'S057.pdf Table 2 Results of the measurement model evaluation',
        'source_constructs': 'PEOU, PU, ATT, SN, EXP, PE, ANX, SE, PV, FC, HBT, INT',
        'source_lines': '/tmp/S057_layout.txt lines 811-828',
        'decision': 'exclude_ai_false_positive_no_target_construct_in_source_matrix',
        'rationale': 'The AI candidates all require TRU and/or UB, but the source Table 2 does not contain TRU or UB. INT may map to BI; no actual use/use behavior construct is present. Therefore these candidates are not addable Paper A target pairs.',
    },
    'S138_ANX': {
        'source_matrix': 'S138.pdf Table 5 Fornell-Larcker Criterion',
        'source_constructs': 'AC, AT, AU, BI, PE, PR, PU, SE, SI, ST',
        'source_lines': '/tmp/S138_layout.txt lines 785-797; Table 2 lines 482-499',
        'decision': 'exclude_ai_false_positive_perceived_risk_not_anxiety',
        'rationale': 'The source matrix contains PR (Perceived Risk), not ANX (Anxiety). Perceived Risk cannot be automatically remapped to Anxiety without a researcher-approved construct remap.',
    },
    'S138_FC': {
        'source_matrix': 'S138.pdf Table 5 Fornell-Larcker Criterion',
        'source_constructs': 'AC, AT, AU, BI, PE, PR, PU, SE, SI, ST',
        'source_lines': '/tmp/S138_layout.txt lines 785-797; Table 2 lines 607-645',
        'decision': 'exclude_ai_false_positive_no_facilitating_conditions_construct',
        'rationale': 'The source matrix does not contain FC (Facilitating Conditions). AC is Acceptance and cannot be automatically remapped to FC.',
    },
    'S176': {
        'source_matrix': 'S176.pdf Table 4 Discriminant validity',
        'source_constructs': 'HM, UB, BI, EE, FC, HA, PE, PI, SI, TR',
        'source_lines': '/tmp/S176_layout.txt lines 617-630',
        'decision': 'exclude_ai_false_positive_no_target_construct_in_source_matrix',
        'rationale': 'The AI candidates require ANX and/or SE, but the source Table 4 does not contain ANX or SE. PI/HA/TR must not be automatically remapped to SE or ANX.',
    },
}


def decision_for(row):
    sid = row['study_id']
    cset = {row['construct_1'], row['construct_2']}
    if sid == 'S057':
        e = EVIDENCE['S057']
    elif sid == 'S138' and 'ANX' in cset:
        e = EVIDENCE['S138_ANX']
    elif sid == 'S138' and 'FC' in cset:
        e = EVIDENCE['S138_FC']
    elif sid == 'S176':
        e = EVIDENCE['S176']
    else:
        e = {
            'source_matrix': '',
            'source_constructs': '',
            'source_lines': '',
            'decision': 'defer_unclear',
            'rationale': 'No detailed source-review rule matched this candidate.',
        }
    return e


def load_rows():
    out = []
    with TRACE.open(newline='', encoding='utf-8-sig') as f:
        for r in csv.DictReader(f):
            if r['study_id'] not in {'S057', 'S138', 'S176'}:
                continue
            e = decision_for(r)
            out.append({
                'study_id': r['study_id'],
                'missing_pair': r['missing_pair'],
                'candidate_value': r['candidate_value'],
                'final_decision': e['decision'],
                'add_to_matrix': 'no',
                'source_matrix_reviewed': e['source_matrix'],
                'source_constructs_seen': e['source_constructs'],
                'source_evidence_locator': e['source_lines'],
                'human_process_status': 'not_human_exact_pair_not_human_excluded',
                'decision_rationale': e['rationale'],
            })
    return sorted(out, key=lambda r: (r['study_id'], r['missing_pair']))


def write_csv(rows):
    for outdir in [REPO_OUT, CANON]:
        outdir.mkdir(parents=True, exist_ok=True)
        with (outdir / CSV_NAME).open('w', newline='', encoding='utf-8-sig') as f:
            writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            writer.writeheader()
            writer.writerows(rows)


def write_md(rows):
    counts = Counter(r['final_decision'] for r in rows)
    lines = []
    lines.append('# Paper A detailed source-review final decisions')
    lines.append('')
    lines.append('Date: 2026-06-14')
    lines.append('')
    lines.append('## Bottom line')
    lines.append('')
    lines.append('After detailed source review of S057, S138, and S176, none of the 51 AI/source-trace missing-pair candidates should be added to the matrix at this time.')
    lines.append('')
    lines.append('Reason: each candidate requires a construct that is absent from the reviewed source matrix or would require an unapproved construct remap.')
    lines.append('')
    lines.append('## Final decision counts')
    lines.append('')
    for k, v in sorted(counts.items()):
        lines.append(f'- {k}: {v}')
    lines.append('- add_to_matrix=yes: 0')
    lines.append('')
    lines.append('## Study-level source evidence')
    lines.append('')
    lines.append('| Study/group | Source matrix reviewed | Constructs visible in source matrix | Decision | Rationale |')
    lines.append('|---|---|---|---|---|')
    groups = [
        ('S057 all 17 TRU/UB candidates', EVIDENCE['S057']),
        ('S138 9 ANX candidates', EVIDENCE['S138_ANX']),
        ('S138 8 FC candidates', EVIDENCE['S138_FC']),
        ('S176 all 17 ANX/SE candidates', EVIDENCE['S176']),
    ]
    for label, e in groups:
        lines.append(f"| {label} | {e['source_matrix']} ({e['source_lines']}) | {e['source_constructs']} | {e['decision']} | {e['rationale']} |")
    lines.append('')
    lines.append('## Row-level final decision table')
    lines.append('')
    lines.append('| study_id | missing_pair | final_decision | add_to_matrix |')
    lines.append('|---|---|---|---|')
    for r in rows:
        lines.append(f"| {r['study_id']} | {r['missing_pair']} | {r['final_decision']} | {r['add_to_matrix']} |")
    lines.append('')
    for outdir in [REPO_OUT, CANON]:
        (outdir / MD_NAME).write_text('\n'.join(lines), encoding='utf-8')
        (outdir / 'README_DETAILED_SOURCE_REVIEW_FINAL_DECISIONS_20260614.md').write_text(
            f"# Detailed source-review final decisions\n\nPrimary report:\n\n`{outdir / MD_NAME}`\n\nRow-level CSV:\n\n`{outdir / CSV_NAME}`\n\nConclusion: add_to_matrix=yes count is 0 across the 51 reviewed AI candidates.\n",
            encoding='utf-8'
        )


def main():
    rows = load_rows()
    write_csv(rows)
    write_md(rows)
    print(CANON / MD_NAME)
    print(CANON / CSV_NAME)
    print('rows=', len(rows))
    print('counts=', dict(Counter(r['final_decision'] for r in rows)))

if __name__ == '__main__':
    main()
