#!/usr/bin/env python3
from pathlib import Path
import pandas as pd

REPO = Path(__file__).resolve().parents[2]
SRC = REPO / 'data/04_extraction/05_llm_masem_substitution/results/paper_a_mediator_feasibility_20260612/paper_a_mediator_path_feasibility_20260612.csv'
OUT = REPO / 'data/04_extraction/05_llm_masem_substitution/results/paper_a_mediator_feasibility_20260612'

def role(status):
    if status == 'main_indirect_candidate':
        return 'main_indirect_effect'
    if status == 'sensitivity_indirect_candidate':
        return 'sensitivity_indirect_effect'
    if status == 'theory_only_underpowered':
        return 'theory_specified_underpowered_no_confirmed_mediation_claim'
    return 'exclude_from_indirect_effect_claim_current_input'


def main():
    df = pd.read_csv(SRC)
    df['reporting_role'] = df['feasibility_status'].map(role)
    df['stage2_parameterization'] = df.apply(
        lambda r: f"a={r['x']}_to_{r['m']}; b={r['m']}_to_{r['y']}; indirect={r['x']}_to_{r['y']}_via_{r['m']}", axis=1
    )
    df['claim_boundary'] = df['reporting_role'].map({
        'main_indirect_effect': 'Eligible for primary Stage 2 indirect-effect reporting if the structural model converges.',
        'sensitivity_indirect_effect': 'Report only as sensitivity/mechanism evidence; do not overstate as confirmed primary mediation.',
        'theory_specified_underpowered_no_confirmed_mediation_claim': 'Mention as theory-specified but underpowered; no confirmed mediation claim.',
        'exclude_from_indirect_effect_claim_current_input': 'Do not report as indirect effect from current input.',
    })
    spec_cols = [
        'mediator','mechanism_family','path_label','x','m','y','a_pair','b_pair','c_pair',
        'a_studies','b_studies','c_studies','ab_same_study_overlap','feasibility_status',
        'reporting_role','stage2_parameterization','claim_boundary'
    ]
    spec = df[spec_cols].copy()
    spec.to_csv(OUT / 'paper_a_stage2_indirect_effect_spec_20260612.csv', index=False)

    lines = [
        '# Paper A Stage 2 Indirect-Effect Specification',
        '',
        'Date: 2026-06-12',
        '',
        f'Source audit: `{SRC.relative_to(REPO)}`',
        '',
        '## Specification rule',
        '',
        '- `main_indirect_effect`: include in primary Stage 2 reporting if model convergence and fit are acceptable.',
        '- `sensitivity_indirect_effect`: estimate/report only as sensitivity or mechanism evidence.',
        '- `theory_specified_underpowered_no_confirmed_mediation_claim`: keep in theory narrative but do not claim confirmed mediation.',
        '- `exclude_from_indirect_effect_claim_current_input`: do not report as an indirect effect from current data.',
        '',
        '## Indirect-effect candidates',
        '',
        '| Role | Mediator | Path | a studies | b studies | a/b overlap | Claim boundary |',
        '| --- | --- | --- | ---: | ---: | ---: | --- |',
    ]
    role_order = {
        'main_indirect_effect': 0,
        'sensitivity_indirect_effect': 1,
        'theory_specified_underpowered_no_confirmed_mediation_claim': 2,
        'exclude_from_indirect_effect_claim_current_input': 3,
    }
    spec = spec.sort_values(by=['reporting_role','mediator','ab_same_study_overlap'], key=lambda s: s.map(role_order).fillna(s) if s.name == 'reporting_role' else s, ascending=[True, True, False])
    for _, r in spec.iterrows():
        lines.append(f"| {r['reporting_role']} | {r['mediator']} | {r['path_label']} | {r['a_studies']} | {r['b_studies']} | {r['ab_same_study_overlap']} | {r['claim_boundary']} |")
    lines += [
        '',
        '## Manuscript implication',
        '',
        'Paper A should report attitude mediation as the strongest standard TAM mechanism. Trust mediation can be tested as an AI-specific mechanism for `PE -> TRU -> BI` and `EE -> TRU -> BI`, with `SI -> TRU -> BI` as sensitivity. Self-efficacy paths should be sensitivity-level. Anxiety paths are theory-specified but underpowered or not identified in the current input.',
    ]
    (OUT / 'PAPER_A_STAGE2_INDIRECT_EFFECT_SPEC_20260612.md').write_text('\n'.join(lines) + '\n')
    print('wrote', OUT / 'PAPER_A_STAGE2_INDIRECT_EFFECT_SPEC_20260612.md')
    print(spec[['reporting_role','mediator','path_label','a_studies','b_studies','ab_same_study_overlap']].to_string(index=False))

if __name__ == '__main__':
    main()
