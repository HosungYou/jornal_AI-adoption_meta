#!/usr/bin/env python3
from pathlib import Path
import pandas as pd

REPO = Path(__file__).resolve().parents[2]
RESULTS = REPO / 'data/04_extraction/05_llm_masem_substitution/results'
OUT = RESULTS / 'paper_a_year_moderator_merge_20260612'
OUT.mkdir(parents=True, exist_ok=True)
INPUT = RESULTS / 'paper2_masem_substitution_rerun_input_n_weighted_all_source_supported_20260612.csv'
YEAR_SRC = REPO / 'data/04_extraction/04_reference_standard_freeze/full_corpus_freeze_gap_map_20260608.csv'

def era(year):
    if pd.isna(year):
        return ''
    try:
        y = int(year)
    except Exception:
        return ''
    return 'post_2023_generative_ai_era' if y >= 2023 else 'pre_2023_or_non_generative_era'


def main():
    inp = pd.read_csv(INPUT)
    inp['study_id'] = inp['study_id'].astype(str)
    year = pd.read_csv(YEAR_SRC)[['study_id','title','year','doi']].drop_duplicates()
    year['study_id'] = year['study_id'].astype(str)
    year['year_numeric'] = pd.to_numeric(year['year'], errors='coerce')
    year['generative_era'] = year['year_numeric'].map(era)

    # If a study appears multiple times with conflicting year, flag it.
    conflicts = year.groupby('study_id')['year_numeric'].nunique(dropna=True).reset_index(name='unique_year_count')
    merged = inp.merge(year, on='study_id', how='left', suffixes=('','_yearsrc'))
    merged = merged.merge(conflicts, on='study_id', how='left')
    merged.to_csv(OUT / 'paper_a_input_with_year_generative_era_20260612.csv', index=False)

    study = merged.groupby('study_id').agg(
        rows=('analysis_record_id','count'),
        construct_pairs=('construct_pair_canonical','nunique'),
        n_ready_pairs=('construct_pair_canonical', lambda s: s.nunique()),
        year_numeric=('year_numeric','first'),
        generative_era=('generative_era','first'),
        unique_year_count=('unique_year_count','first'),
        title=('title','first'),
    ).reset_index()
    study['year_available'] = study['year_numeric'].notna()
    study.to_csv(OUT / 'paper_a_year_generative_era_study_level_20260612.csv', index=False)

    summary = study.groupby(['generative_era'], dropna=False).agg(
        study_count=('study_id','nunique'),
        median_construct_pairs=('construct_pairs','median'),
        min_construct_pairs=('construct_pairs','min'),
        max_construct_pairs=('construct_pairs','max'),
    ).reset_index()
    summary.to_csv(OUT / 'paper_a_year_generative_era_summary_20260612.csv', index=False)

    available = study[study['year_available']]
    level_counts = available['generative_era'].value_counts()
    min_level = int(level_counts.min()) if len(level_counts) else 0
    status = 'eligible_main_candidate' if len(available) >= 20 and len(level_counts) >= 2 and min_level >= 10 else ('sensitivity_candidate' if len(available) >= 15 and len(level_counts) >= 2 and min_level >= 5 else 'not_feasible_current_input')

    lines = [
        '# Paper A Year / Generative-Era Moderator Merge',
        '',
        'Date: 2026-06-12',
        '',
        f'MASEM input: `{INPUT.relative_to(REPO)}`',
        f'Year source: `{YEAR_SRC.relative_to(REPO)}`',
        '',
        '## Rule',
        '',
        '- `post_2023_generative_ai_era`: publication year >= 2023.',
        '- `pre_2023_or_non_generative_era`: publication year < 2023.',
        '',
        '## Coverage',
        '',
        f'- Study IDs in MASEM input: {inp.study_id.nunique()}',
        f'- Study IDs with year after merge: {available.study_id.nunique()}',
        f'- Study IDs missing year after merge: {study.study_id.nunique() - available.study_id.nunique()}',
        f'- Era moderator gate status: `{status}`',
        '',
        '| Era | Study count | Median construct pairs | Min pairs | Max pairs |',
        '| --- | ---: | ---: | ---: | ---: |',
    ]
    for _, r in summary.iterrows():
        label = r['generative_era'] if isinstance(r['generative_era'], str) and r['generative_era'] else 'missing_year'
        lines.append(f"| {label} | {int(r['study_count'])} | {r['median_construct_pairs']} | {int(r['min_construct_pairs'])} | {int(r['max_construct_pairs'])} |")
    lines += [
        '',
        '## Interpretation',
        '',
        f'The year/generative-era moderator is `{status}` under the first-pass merge. If retained, it should be treated as a true study-level moderator distinct from the mediator/mechanism constructs.',
    ]
    (OUT / 'PAPER_A_YEAR_GENERATIVE_ERA_MODERATOR_MERGE_20260612.md').write_text('\n'.join(lines) + '\n')
    print('wrote', OUT.relative_to(REPO))
    print(summary.to_string(index=False))
    print('gate_status', status)

if __name__ == '__main__':
    main()
