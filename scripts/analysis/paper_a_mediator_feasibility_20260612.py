#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import pandas as pd

REPO = Path(__file__).resolve().parents[2]
RESULTS = REPO / 'data/04_extraction/05_llm_masem_substitution/results'
OUT = RESULTS / 'paper_a_mediator_feasibility_20260612'
OUT.mkdir(parents=True, exist_ok=True)
INPUT = RESULTS / 'paper2_masem_substitution_rerun_input_n_weighted_all_source_supported_20260612.csv'


def pair(a: str, b: str) -> str:
    return '-'.join(sorted([a, b]))


def clean_pair(s):
    if pd.isna(s):
        return ''
    parts = str(s).replace('_', '-').split('-')
    if len(parts) >= 2:
        return pair(parts[0].strip(), parts[1].strip())
    return str(s).strip()


def classify(a_studies, b_studies, c_studies, ab_overlap, abc_overlap):
    if a_studies >= 10 and b_studies >= 10 and c_studies >= 10 and ab_overlap >= 5:
        return 'main_indirect_candidate'
    if a_studies >= 5 and b_studies >= 5 and ab_overlap >= 3:
        return 'sensitivity_indirect_candidate'
    if a_studies >= 3 and b_studies >= 3:
        return 'theory_only_underpowered'
    return 'not_identified_current_input'


def main():
    df = pd.read_csv(INPUT)
    df['study_id'] = df['study_id'].astype(str)
    df['sample_size_numeric_num'] = pd.to_numeric(df['sample_size_numeric'], errors='coerce')
    df['r_numeric_num'] = pd.to_numeric(df['r_numeric'], errors='coerce')
    df['pair'] = df.apply(lambda r: pair(str(r['construct_1']).strip(), str(r['construct_2']).strip()), axis=1)
    df = df[df['r_numeric_num'].notna() & df['sample_size_numeric_num'].notna()].copy()

    pair_stats = df.groupby('pair').agg(
        rows=('analysis_record_id', 'count'),
        studies=('study_id', 'nunique'),
        median_n=('sample_size_numeric_num', 'median'),
    ).reset_index()
    pair_stats.to_csv(OUT / 'paper_a_pair_coverage_for_mediation_20260612.csv', index=False)

    studies_by_pair = {p: set(g['study_id']) for p, g in df.groupby('pair')}
    rows_by_pair = pair_stats.set_index('pair')['rows'].to_dict()
    study_count_by_pair = pair_stats.set_index('pair')['studies'].to_dict()

    specs = [
        # Baseline TAM/UTAUT attitude mediation.
        ('ATT', 'standard_attitude_mediation', 'PE', 'ATT', 'BI', 'PE -> ATT -> BI'),
        ('ATT', 'standard_attitude_mediation', 'EE', 'ATT', 'BI', 'EE -> ATT -> BI'),
        ('ATT', 'standard_attitude_mediation', 'SI', 'ATT', 'BI', 'SI -> ATT -> BI'),
        ('ATT', 'standard_attitude_mediation', 'FC', 'ATT', 'BI', 'FC -> ATT -> BI'),
        # Self-efficacy as mechanism.
        ('SE', 'self_efficacy_mechanism', 'FC', 'SE', 'BI', 'FC -> SE -> BI'),
        ('SE', 'self_efficacy_mechanism', 'EE', 'SE', 'BI', 'EE -> SE -> BI'),
        ('SE', 'self_efficacy_mechanism', 'PE', 'SE', 'BI', 'PE -> SE -> BI'),
        ('SE', 'self_efficacy_mechanism', 'SI', 'SE', 'BI', 'SI -> SE -> BI'),
        ('SE', 'self_efficacy_to_attitude', 'FC', 'SE', 'ATT', 'FC -> SE -> ATT'),
        ('SE', 'self_efficacy_to_attitude', 'EE', 'SE', 'ATT', 'EE -> SE -> ATT'),
        ('SE', 'self_efficacy_to_attitude', 'PE', 'SE', 'ATT', 'PE -> SE -> ATT'),
        # Trust as AI-specific mechanism.
        ('TRU', 'trust_mechanism', 'PE', 'TRU', 'BI', 'PE -> TRU -> BI'),
        ('TRU', 'trust_mechanism', 'EE', 'TRU', 'BI', 'EE -> TRU -> BI'),
        ('TRU', 'trust_mechanism', 'SI', 'TRU', 'BI', 'SI -> TRU -> BI'),
        ('TRU', 'trust_mechanism', 'FC', 'TRU', 'BI', 'FC -> TRU -> BI'),
        ('TRU', 'trust_mechanism', 'ATT', 'TRU', 'BI', 'ATT -> TRU -> BI'),
        ('TRU', 'trust_mechanism', 'SE', 'TRU', 'BI', 'SE -> TRU -> BI'),
        # Anxiety as AI-specific inhibitory mechanism.
        ('ANX', 'anxiety_mechanism', 'SE', 'ANX', 'BI', 'SE -> ANX -> BI'),
        ('ANX', 'anxiety_mechanism', 'FC', 'ANX', 'BI', 'FC -> ANX -> BI'),
        ('ANX', 'anxiety_mechanism', 'EE', 'ANX', 'BI', 'EE -> ANX -> BI'),
        ('ANX', 'anxiety_mechanism', 'PE', 'ANX', 'BI', 'PE -> ANX -> BI'),
        ('ANX', 'anxiety_to_attitude', 'SE', 'ANX', 'ATT', 'SE -> ANX -> ATT'),
        ('ANX', 'anxiety_to_attitude', 'FC', 'ANX', 'ATT', 'FC -> ANX -> ATT'),
        ('ANX', 'anxiety_to_attitude', 'EE', 'ANX', 'ATT', 'EE -> ANX -> ATT'),
        ('ANX', 'anxiety_to_attitude', 'PE', 'ANX', 'ATT', 'PE -> ANX -> ATT'),
    ]

    rows = []
    for mediator, family, x, m, y, label in specs:
        a_pair = pair(x, m)
        b_pair = pair(m, y)
        c_pair = pair(x, y)
        a_set = studies_by_pair.get(a_pair, set())
        b_set = studies_by_pair.get(b_pair, set())
        c_set = studies_by_pair.get(c_pair, set())
        ab = a_set & b_set
        abc = ab & c_set
        status = classify(len(a_set), len(b_set), len(c_set), len(ab), len(abc))
        rows.append({
            'mediator': mediator,
            'mechanism_family': family,
            'path_label': label,
            'x': x,
            'm': m,
            'y': y,
            'a_pair': a_pair,
            'b_pair': b_pair,
            'c_pair': c_pair,
            'a_rows': int(rows_by_pair.get(a_pair, 0)),
            'a_studies': int(study_count_by_pair.get(a_pair, 0)),
            'b_rows': int(rows_by_pair.get(b_pair, 0)),
            'b_studies': int(study_count_by_pair.get(b_pair, 0)),
            'c_rows': int(rows_by_pair.get(c_pair, 0)),
            'c_studies': int(study_count_by_pair.get(c_pair, 0)),
            'ab_same_study_overlap': len(ab),
            'abc_same_study_overlap': len(abc),
            'feasibility_status': status,
        })
    audit = pd.DataFrame(rows)
    audit.to_csv(OUT / 'paper_a_mediator_path_feasibility_20260612.csv', index=False)

    summary = audit.groupby(['mediator', 'feasibility_status']).size().reset_index(name='path_count')
    summary.to_csv(OUT / 'paper_a_mediator_feasibility_summary_20260612.csv', index=False)

    best = audit.sort_values(
        ['mediator', 'feasibility_status', 'a_studies', 'b_studies', 'ab_same_study_overlap'],
        ascending=[True, True, False, False, False]
    )

    lines = [
        '# Paper A Mediator/Mechanism Feasibility Audit',
        '',
        'Date: 2026-06-12',
        '',
        f'Input: `{INPUT.relative_to(REPO)}`',
        '',
        'Researcher correction: Trust, anxiety, and self-efficacy are not moderators. They are candidate mediator/mechanism constructs inside the MASEM path model.',
        '',
        '## Feasibility rule',
        '',
        '- `main_indirect_candidate`: a, b, and c paths each have at least 10 studies, and at least 5 studies contain both a and b paths.',
        '- `sensitivity_indirect_candidate`: a and b paths each have at least 5 studies, and at least 3 studies contain both a and b paths.',
        '- `theory_only_underpowered`: a and b paths each have at least 3 studies but overlap is too sparse for strong indirect-effect reporting.',
        '- `not_identified_current_input`: current input does not support the proposed mechanism path.',
        '',
        '## Path-level results',
        '',
        '| Mediator | Path | a studies | b studies | c studies | a/b overlap | Status |',
        '| --- | --- | ---: | ---: | ---: | ---: | --- |',
    ]
    for _, r in audit.iterrows():
        lines.append(f"| {r['mediator']} | {r['path_label']} | {r['a_studies']} | {r['b_studies']} | {r['c_studies']} | {r['ab_same_study_overlap']} | {r['feasibility_status']} |")

    lines.extend([
        '',
        '## Interpretation',
        '',
        'Attitude remains the strongest standard mediator in the current Paper A MASEM logic if its a/b paths clear coverage in the table above.',
        '',
        'Self-efficacy, trust, and anxiety should be tested as theory-specified mechanism constructs only where the path-level audit supports both the upstream a path and downstream b path. If the full indirect path is sparse, the manuscript should describe the construct as a theoretically motivated antecedent/mechanism candidate rather than claim a confirmed mediation effect.',
        '',
        'The next analytic step is not another moderator table. It is a Stage 2 path-model specification that includes candidate indirect effects for feasible mechanism paths and labels underpowered mechanisms as sensitivity or theory-only.',
        '',
        '## Output files',
        '',
        '- `paper_a_pair_coverage_for_mediation_20260612.csv`',
        '- `paper_a_mediator_path_feasibility_20260612.csv`',
        '- `paper_a_mediator_feasibility_summary_20260612.csv`',
    ])
    (OUT / 'PAPER_A_MEDIATOR_FEASIBILITY_AUDIT_20260612.md').write_text('\n'.join(lines) + '\n')

    print('wrote', OUT.relative_to(REPO))
    print(summary.to_string(index=False))
    print('\nTop feasible paths:')
    print(audit.sort_values(['feasibility_status','ab_same_study_overlap','a_studies','b_studies'], ascending=[True,False,False,False]).head(12)[['mediator','path_label','a_studies','b_studies','c_studies','ab_same_study_overlap','feasibility_status']].to_string(index=False))

if __name__ == '__main__':
    main()
