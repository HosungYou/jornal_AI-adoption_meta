#!/usr/bin/env python3
from __future__ import annotations

import math
import re
from pathlib import Path

import pandas as pd

REPO = Path(__file__).resolve().parents[2]
RESULTS = REPO / 'data/04_extraction/05_llm_masem_substitution/results'
OUT = RESULTS / 'initial_execution_validation_20260612'
OUT.mkdir(parents=True, exist_ok=True)

MASEM_INPUT = RESULTS / 'paper2_masem_substitution_rerun_input_n_weighted_all_source_supported_20260612.csv'
RQ3_TASKS = RESULTS / 'paper2_rq3_triage_task_units_20260611.csv'
SET_COMPLETENESS = RESULTS / 'paper2_masem_matrix_construct_set_completeness_20260612.csv'
PAIR_COVERAGE = RESULTS / 'paper2_masem_matrix_pair_coverage_after_n_override_20260612.csv'
STUDY_PAIR_COVERAGE = RESULTS / 'paper2_masem_matrix_study_pair_coverage_20260612.csv'
READINESS_OVERALL = RESULTS / 'r_masem_readiness_n_pdf_override_20260612/paper2_masem_readiness_overall_20260612.csv'

DATE = '2026-06-12'


def clean_missing(v):
    if pd.isna(v):
        return ''
    s = str(v).strip()
    if s.lower() in {'', 'na', 'n/a', 'none', 'null', 'nan', 'not reported', 'not_reported', 'unknown'}:
        return ''
    return s


def norm_bool(v):
    if pd.isna(v):
        return pd.NA
    s = str(v).strip().lower()
    if s in {'true', 't', '1', '1.0', 'yes', 'y'}:
        return True
    if s in {'false', 'f', '0', '0.0', 'no', 'n'}:
        return False
    return pd.NA

COUNTRY_NORMAL = {
    'austrian': 'Austria',
    'pakistani': 'Pakistan',
    'indian': 'India',
    'nigerian': 'Nigeria',
    'palestine': 'Palestine',
    'saudi arabia': 'Saudi Arabia',
    'qatar': 'Qatar',
    'germany': 'Germany',
}
REGION_BY_COUNTRY = {
    'Austria': 'Europe', 'Germany': 'Europe', 'Spain': 'Europe', 'United Kingdom': 'Europe', 'UK': 'Europe',
    'Pakistan': 'South Asia', 'India': 'South Asia', 'Bangladesh': 'South Asia', 'Sri Lanka': 'South Asia',
    'Saudi Arabia': 'Middle East', 'Qatar': 'Middle East', 'Palestine': 'Middle East', 'Jordan': 'Middle East', 'UAE': 'Middle East',
    'Nigeria': 'Africa',
    'China': 'East Asia', 'Japan': 'East Asia', 'South Korea': 'East Asia', 'Korea': 'East Asia', 'Taiwan': 'East Asia', 'Hong Kong': 'East Asia',
    'New Zealand': 'Oceania', 'Australia': 'Oceania',
    'United States': 'North America', 'USA': 'North America', 'Canada': 'North America',
}


def normalize_country(raw):
    s = clean_missing(raw)
    if not s:
        return ''
    low = s.lower()
    if low.startswith('mixed'):
        return 'mixed'
    return COUNTRY_NORMAL.get(low, s)


def derive_region(raw):
    c = normalize_country(raw)
    if not c:
        return ''
    if c == 'mixed':
        raw_s = str(raw)
        regions = set()
        for country, region in REGION_BY_COUNTRY.items():
            if re.search(r'\b' + re.escape(country) + r'\b', raw_s, flags=re.I):
                regions.add(region)
        if len(regions) == 1:
            return next(iter(regions))
        if len(regions) > 1:
            return 'mixed_region'
        return 'mixed_region'
    return REGION_BY_COUNTRY.get(c, 'unmapped_country')


def study_level_value(group, field):
    vals = sorted({clean_missing(v) for v in group[field].tolist() if clean_missing(v)})
    if len(vals) == 0:
        return ''
    if len(vals) == 1:
        return vals[0]
    return 'MULTIPLE_VALUES'


def gate_status(nonmissing_studies, level_count, min_level_studies, pair_coverage, ambiguous_studies=0):
    if nonmissing_studies >= 20 and level_count >= 2 and min_level_studies >= 10 and pair_coverage >= 20 and ambiguous_studies == 0:
        return 'eligible_main_candidate'
    if nonmissing_studies >= 15 and level_count >= 2 and min_level_studies >= 5 and pair_coverage >= 15:
        return 'sensitivity_candidate'
    if nonmissing_studies >= 8 and level_count >= 2 and min_level_studies >= 3:
        return 'descriptive_only'
    return 'not_feasible_current_input'


def safe_pct(num, den):
    if den in (0, None) or pd.isna(den):
        return math.nan
    return 100.0 * num / den


def fmt_num(x):
    if pd.isna(x):
        return 'NA'
    if isinstance(x, float):
        if abs(x - round(x)) < 1e-9:
            return str(int(round(x)))
        return f'{x:.3f}'
    return str(x)


def analyze_paper_a():
    df = pd.read_csv(MASEM_INPUT)
    df['study_id'] = df['study_id'].astype(str)
    df['sample_size_numeric_num'] = pd.to_numeric(df.get('sample_size_numeric'), errors='coerce')
    df['r_numeric_num'] = pd.to_numeric(df.get('r_numeric'), errors='coerce')
    df['country_normalized'] = df.get('country', '').map(normalize_country)
    df['region_derived_initial'] = df.get('country', '').map(derive_region)
    df['tool_type_ai_type'] = df.get('ai_type', '').map(clean_missing)
    df['education_level_clean'] = df.get('education_level', '').map(clean_missing)
    df['user_role_clean'] = df.get('user_role', '').map(clean_missing)
    df['common_method_bias_clean'] = df.get('common_method_bias', '').map(clean_missing)
    df['framework_family_clean'] = df.get('theoretical_framework', '').map(clean_missing)

    candidates = [
        ('ai_type', 'tool_type_ai_type', 'AI tool type / generative vs general'),
        ('user_role', 'user_role_clean', 'User role'),
        ('common_method_bias', 'common_method_bias_clean', 'Common-method-bias handling'),
        ('education_level', 'education_level_clean', 'Education level'),
        ('country', 'country_normalized', 'Country / cultural context'),
        ('region_derived_initial', 'region_derived_initial', 'Initial derived region'),
        ('theoretical_framework', 'framework_family_clean', 'Theory/framework family'),
    ]

    study_rows = []
    level_rows = []
    total_studies = df['study_id'].nunique()
    total_pairs = df['construct_pair_canonical'].nunique() if 'construct_pair_canonical' in df else df['construct_pair'].nunique()
    pair_col = 'construct_pair_canonical' if 'construct_pair_canonical' in df else 'construct_pair'

    for key, field, label in candidates:
        per_study = df.groupby('study_id').apply(lambda g: study_level_value(g, field), include_groups=False).reset_index(name='study_level_value')
        nonmissing = per_study[per_study['study_level_value'] != ''].copy()
        ambiguous = int((nonmissing['study_level_value'] == 'MULTIPLE_VALUES').sum())
        usable = nonmissing[nonmissing['study_level_value'] != 'MULTIPLE_VALUES'].copy()
        level_counts = usable['study_level_value'].value_counts().sort_values(ascending=False)
        level_count = int(level_counts.shape[0])
        min_level = int(level_counts.min()) if level_count else 0
        max_level = int(level_counts.max()) if level_count else 0
        rows_nonmissing = int(df[field].map(clean_missing).ne('').sum())
        pair_coverage = int(df[df[field].map(clean_missing).ne('')][pair_col].nunique())
        n_ready_rows = int(df[df[field].map(clean_missing).ne('')]['sample_size_numeric_num'].notna().sum())
        status = gate_status(int(nonmissing.shape[0]), level_count, min_level, pair_coverage, ambiguous)
        study_rows.append({
            'moderator_candidate': key,
            'label': label,
            'rows_nonmissing': rows_nonmissing,
            'studies_nonmissing': int(nonmissing.shape[0]),
            'studies_usable_unambiguous': int(usable.shape[0]),
            'ambiguous_studies': ambiguous,
            'level_count': level_count,
            'min_level_studies': min_level,
            'max_level_studies': max_level,
            'construct_pairs_with_nonmissing': pair_coverage,
            'n_ready_rows_nonmissing': n_ready_rows,
            'total_studies': total_studies,
            'total_construct_pairs': total_pairs,
            'gate_status': status,
            'top_levels': '; '.join([f'{idx}={val}' for idx, val in level_counts.head(8).items()]),
        })
        for value, count in level_counts.items():
            level_rows.append({
                'moderator_candidate': key,
                'study_level_value': value,
                'study_count': int(count),
            })

    feasibility = pd.DataFrame(study_rows).sort_values(['gate_status', 'studies_nonmissing'], ascending=[True, False])
    levels = pd.DataFrame(level_rows)
    feasibility.to_csv(OUT / 'paper_a_moderator_feasibility_20260612.csv', index=False)
    levels.to_csv(OUT / 'paper_a_moderator_level_counts_20260612.csv', index=False)
    return feasibility, levels, df


def analyze_rq3():
    df = pd.read_csv(RQ3_TASKS)
    df['cross_model_flag'] = df['cross_model_behavior_disagreement'].map(norm_bool).fillna(False)
    df['primary_correct_bool'] = df['primary_is_correct'].map(norm_bool)
    df['available_model_count_num'] = pd.to_numeric(df['available_model_count'], errors='coerce').fillna(0)
    state = df.get('primary_answer_state', pd.Series([''] * len(df))).astype(str).str.lower()
    status = df.get('primary_score_status', pd.Series([''] * len(df))).astype(str).str.lower()
    df['primary_abstention_like'] = state.str.contains('abstain|missing|no_answer|no answer|blank', regex=True) | status.str.contains('abstain|missing|no_model|blank', regex=True)
    df['scorable_primary'] = df['primary_correct_bool'].notna()
    df['multi_model_available'] = df['available_model_count_num'] >= 2
    df['review_needed'] = (
        (df['primary_correct_bool'] == False)
        | df['primary_abstention_like']
        | status.str.contains('not_scored|no_locked_answer|reference_only', regex=True)
        | df.get('triage_signals', pd.Series([''] * len(df))).fillna('').astype(str).str.contains('primary_incorrect|primary_abstention|primary_not_scored|primary_missing_model_row', regex=True)
    )
    scoped = df[df['multi_model_available']].copy()

    def signal_metrics(frame, flag_col, signal_name):
        n = int(frame.shape[0])
        flagged = frame[frame[flag_col]].copy()
        review = frame[frame['review_needed']].copy()
        tp = int((frame[flag_col] & frame['review_needed']).sum())
        fp = int((frame[flag_col] & ~frame['review_needed']).sum())
        fn = int((~frame[flag_col] & frame['review_needed']).sum())
        flagged_n = int(flagged.shape[0])
        review_n = int(review.shape[0])
        precision = tp / flagged_n if flagged_n else math.nan
        recall = tp / review_n if review_n else math.nan
        burden = flagged_n / n if n else math.nan
        baseline = review_n / n if n else math.nan
        lift = precision / baseline if baseline and not math.isnan(precision) else math.nan
        return {
            'signal': signal_name,
            'scope_n': n,
            'flagged_n': flagged_n,
            'review_needed_n': review_n,
            'true_positive_n': tp,
            'false_positive_n': fp,
            'false_negative_n': fn,
            'precision_review_needed': precision,
            'recall_review_needed': recall,
            'review_burden_share': burden,
            'baseline_review_needed_rate': baseline,
            'precision_lift_vs_baseline': lift,
        }

    metrics = [signal_metrics(scoped, 'cross_model_flag', 'cross_model_behavior_disagreement')]

    signals = set()
    if 'triage_signals' in scoped.columns:
        for raw in scoped['triage_signals'].fillna(''):
            for part in re.split(r'[;|,]+', str(raw)):
                part = part.strip()
                if part:
                    signals.add(part)
        for sig in sorted(signals):
            col = 'sig_' + re.sub(r'[^A-Za-z0-9_]+', '_', sig)
            scoped[col] = scoped['triage_signals'].fillna('').astype(str).str.contains(re.escape(sig), regex=True)
            metrics.append(signal_metrics(scoped, col, sig))

    triage = pd.DataFrame(metrics).sort_values(['precision_lift_vs_baseline', 'recall_review_needed'], ascending=[False, False])
    triage.to_csv(OUT / 'paper_b_rq3_signal_validation_20260612.csv', index=False)

    by_family = []
    for family, fam_df in scoped.groupby('denominator_family', dropna=False):
        by_family.append(signal_metrics(fam_df, 'cross_model_flag', f'cross_model_behavior_disagreement | {family}'))
    by_family_df = pd.DataFrame(by_family).sort_values('precision_lift_vs_baseline', ascending=False)
    by_family_df.to_csv(OUT / 'paper_b_rq3_cross_model_by_family_20260612.csv', index=False)

    priority = scoped.groupby(['review_priority'], dropna=False).agg(
        task_n=('task_unit_id', 'count'),
        cross_model_flag_n=('cross_model_flag', 'sum'),
        review_needed_n=('review_needed', 'sum'),
    ).reset_index()
    priority.to_csv(OUT / 'paper_b_rq3_review_priority_summary_20260612.csv', index=False)
    return triage, by_family_df, priority, scoped


def analyze_masem_feasibility():
    sets = pd.read_csv(SET_COMPLETENESS)
    pairs = pd.read_csv(PAIR_COVERAGE)
    studies = pd.read_csv(STUDY_PAIR_COVERAGE)
    readiness = pd.read_csv(READINESS_OVERALL) if READINESS_OVERALL.exists() else pd.DataFrame(columns=['metric','value'])
    input_df = pd.read_csv(MASEM_INPUT)

    input_df['sample_size_numeric_num'] = pd.to_numeric(input_df.get('sample_size_numeric'), errors='coerce')
    input_df['r_numeric_num'] = pd.to_numeric(input_df.get('r_numeric'), errors='coerce')
    n_total = len(input_df)
    n_ready = int(input_df['sample_size_numeric_num'].notna().sum())
    r_ready = int(input_df['r_numeric_num'].notna().sum())
    unique_studies = int(input_df['study_id'].nunique())
    unique_pairs = int(input_df['construct_pair_canonical'].nunique() if 'construct_pair_canonical' in input_df else input_df['construct_pair'].nunique())

    pairs['studies_with_numeric_n_num'] = pd.to_numeric(pairs['studies_with_numeric_n'], errors='coerce')
    pairs['rows_with_numeric_n_num'] = pd.to_numeric(pairs['rows_with_numeric_n'], errors='coerce')
    pair_summary = {
        'total_pairs': int(pairs.shape[0]),
        'pairs_with_1plus_n_ready_study': int((pairs['studies_with_numeric_n_num'] >= 1).sum()),
        'pairs_with_3plus_n_ready_studies': int((pairs['studies_with_numeric_n_num'] >= 3).sum()),
        'pairs_with_5plus_n_ready_studies': int((pairs['studies_with_numeric_n_num'] >= 5).sum()),
        'pairs_with_10plus_n_ready_studies': int((pairs['studies_with_numeric_n_num'] >= 10).sum()),
        'min_n_ready_studies_per_pair': float(pairs['studies_with_numeric_n_num'].min()),
        'median_n_ready_studies_per_pair': float(pairs['studies_with_numeric_n_num'].median()),
        'max_n_ready_studies_per_pair': float(pairs['studies_with_numeric_n_num'].max()),
    }

    studies['n_ready_construct_pairs_num'] = pd.to_numeric(studies['n_ready_construct_pairs'], errors='coerce')
    study_thresholds = []
    for threshold in [6, 10, 15, 21, 28, 36, 45]:
        study_thresholds.append({
            'n_ready_pair_threshold': threshold,
            'study_count': int((studies['n_ready_construct_pairs_num'] >= threshold).sum()),
        })
    study_thresholds_df = pd.DataFrame(study_thresholds)
    study_thresholds_df.to_csv(OUT / 'paper_b_broader_masem_study_pair_thresholds_20260612.csv', index=False)

    rows = []
    for _, row in sets.iterrows():
        required = pd.to_numeric(row.get('required_pairs'), errors='coerce')
        covered = pd.to_numeric(row.get('covered_pairs'), errors='coerce')
        complete_cases = pd.to_numeric(row.get('complete_case_studies'), errors='coerce')
        min_pair = pd.to_numeric(row.get('min_pair_study_count'), errors='coerce')
        coverage_rate = covered / required if required else math.nan
        if complete_cases >= 10 and min_pair >= 3:
            initial_route = 'candidate_for_main_or_extended_diagnostic'
        elif complete_cases >= 5 and min_pair >= 2:
            initial_route = 'candidate_for_sensitivity_only'
        elif covered == required and min_pair >= 1:
            initial_route = 'sparse_broader_rebuild_probe_only'
        else:
            initial_route = 'not_ready_current_input'
        rows.append({
            'construct_set': row.get('construct_set'),
            'constructs': row.get('constructs'),
            'construct_count': row.get('construct_count'),
            'required_pairs': row.get('required_pairs'),
            'covered_pairs': row.get('covered_pairs'),
            'coverage_rate': coverage_rate,
            'missing_pairs': row.get('missing_pairs'),
            'min_pair_study_count': row.get('min_pair_study_count'),
            'complete_case_studies': row.get('complete_case_studies'),
            'identification_gate_original': row.get('identification_gate'),
            'initial_execution_validation': initial_route,
        })
    feasibility = pd.DataFrame(rows)
    feasibility.to_csv(OUT / 'paper_b_broader_masem_feasibility_20260612.csv', index=False)

    overall = pd.DataFrame([{
        'input_rows': n_total,
        'rows_with_r_numeric': r_ready,
        'rows_with_sample_size_numeric': n_ready,
        'rows_missing_sample_size_numeric': n_total - n_ready,
        'unique_studies': unique_studies,
        'unique_construct_pairs': unique_pairs,
        **pair_summary,
    }])
    overall.to_csv(OUT / 'paper_b_broader_masem_overall_20260612.csv', index=False)
    return feasibility, overall, study_thresholds_df, pairs, studies, readiness


def write_report(paper_a, triage, by_family, priority, masem, masem_overall, thresholds):
    pa = paper_a.sort_values(['gate_status', 'studies_nonmissing'], ascending=[True, False])
    cm = triage[triage['signal'] == 'cross_model_behavior_disagreement'].iloc[0]
    best_signals = triage.head(8)
    m_over = masem_overall.iloc[0]

    lines = [
        '# Initial Execution Validation for Paper A and Paper B',
        '',
        f'Date: {DATE}',
        '',
        '## Inputs',
        '',
        f'- MASEM input: `{MASEM_INPUT.relative_to(REPO)}`',
        f'- RQ3 task units: `{RQ3_TASKS.relative_to(REPO)}`',
        f'- Construct-set completeness: `{SET_COMPLETENESS.relative_to(REPO)}`',
        f'- Pair coverage: `{PAIR_COVERAGE.relative_to(REPO)}`',
        '',
        '## Question 1. Paper A moderator feasibility',
        '',
        'Initial criterion: a main-candidate moderator needs at least 20 nonmissing studies, at least 2 usable levels, at least 10 studies in the smallest usable level, at least 20 construct pairs represented, and no study-level ambiguity. A sensitivity candidate needs at least 15 nonmissing studies, at least 2 usable levels, at least 5 studies in the smallest usable level, and at least 15 construct pairs represented.',
        '',
        '| Moderator | Studies nonmissing | Levels | Smallest level | Pair coverage | Gate | Top levels |',
        '| --- | ---: | ---: | ---: | ---: | --- | --- |',
    ]
    for _, row in pa.iterrows():
        lines.append(
            f"| {row['moderator_candidate']} | {int(row['studies_nonmissing'])} | {int(row['level_count'])} | {int(row['min_level_studies'])} | {int(row['construct_pairs_with_nonmissing'])} | {row['gate_status']} | {row['top_levels']} |"
        )
    lines += [
        '',
        'Answer: `ai_type` and `common_method_bias` are the only current main-candidate study-level moderators under the first-pass thresholds. `user_role` has enough nonmissing studies but fails level-balance requirements because instructor/both studies are sparse. `education_level`, `country`, initial derived region, and `theoretical_framework` are not feasible from the current input. `year/generative-AI era` cannot be validated from this MASEM input because no year column is present; it requires a bibliographic merge before OSMASEM.',
        '',
        'Trust, anxiety, and self-efficacy remain non-moderator constructs; after researcher clarification they should be audited separately as candidate mediator/mechanism constructs inside the MASEM path model.',
        '',
        '## Question 2. Paper B cross-model disagreement as RQ3 triage signal',
        '',
        '| Metric | Value |',
        '| --- | ---: |',
        f"| Multi-model scorable task units | {int(cm['scope_n'])} |",
        f"| Cross-model disagreement flagged units | {int(cm['flagged_n'])} |",
        f"| Review-needed units in scope | {int(cm['review_needed_n'])} |",
        f"| Precision among flagged units | {cm['precision_review_needed']:.3f} |",
        f"| Recall of review-needed units | {cm['recall_review_needed']:.3f} |",
        f"| Review burden share | {cm['review_burden_share']:.3f} |",
        f"| Baseline review-needed rate | {cm['baseline_review_needed_rate']:.3f} |",
        f"| Precision lift vs baseline | {cm['precision_lift_vs_baseline']:.3f} |",
        '',
        'Top triage signals by lift:',
        '',
        '| Signal | Flagged n | Precision | Recall | Lift |',
        '| --- | ---: | ---: | ---: | ---: |',
    ]
    for _, row in best_signals.iterrows():
        lines.append(f"| {row['signal']} | {int(row['flagged_n'])} | {row['precision_review_needed']:.3f} | {row['recall_review_needed']:.3f} | {row['precision_lift_vs_baseline']:.3f} |")
    lines += [
        '',
        'Answer: cross-model disagreement is usable as a main RQ3 descriptive triage dimension, but the first-pass evidence does not support treating it as a standalone high-yield threshold. Precision is high because the baseline review-needed rate is already extremely high, and lift is only about 1.0. It flags many blank/absence-behavior rows and has high recall, but it does not identify the high-consequence direct-r or converted numeric families in this first-pass file. The defensible operationalization is to report cross-model disagreement in the main RQ3 table together with review burden, family-specific coverage, human disagreement, source-risk flags, and primary abstention/error status; do not use it alone as a numeric-extraction triage rule.',
        '',
        '## Question 3. Paper B broader TSSEM/MASEM rebuild feasibility',
        '',
        '| Overall metric | Value |',
        '| --- | ---: |',
    ]
    for col, value in m_over.items():
        lines.append(f'| {col} | {fmt_num(value)} |')
    lines += [
        '',
        'Construct-set feasibility:',
        '',
        '| Construct set | Construct count | Required pairs | Covered pairs | Complete-case studies | Min pair study count | Validation |',
        '| --- | ---: | ---: | ---: | ---: | ---: | --- |',
    ]
    for _, row in masem.iterrows():
        lines.append(
            f"| {row['construct_set']} | {row['construct_count']} | {row['required_pairs']} | {row['covered_pairs']} | {row['complete_case_studies']} | {row['min_pair_study_count']} | {row['initial_execution_validation']} |"
        )
    lines += [
        '',
        'Answer: the broader rebuild is justified as a staged execution attempt because the N-coverage gate is closed for the source-supported derived input and most construct pairs are represented. It is not yet justified as a replacement for the core-6 diagnostic in the main text because the full 10-construct route has 44/45 covered pairs, zero complete-case studies, and least-covered pairs with no N-ready studies. The defensible next route is to retain core-6 as the completed diagnostic, then attempt `core7_add_att` and `core8_add_tru` as sparse broader probes. Full 9- or 10-construct claims should remain blocked unless a later rebuild closes the missing-pair and complete-case/sparse-identification gates.',
        '',
        '## Output files',
        '',
        '- `paper_a_moderator_feasibility_20260612.csv`',
        '- `paper_a_moderator_level_counts_20260612.csv`',
        '- `paper_b_rq3_signal_validation_20260612.csv`',
        '- `paper_b_rq3_cross_model_by_family_20260612.csv`',
        '- `paper_b_rq3_review_priority_summary_20260612.csv`',
        '- `paper_b_broader_masem_feasibility_20260612.csv`',
        '- `paper_b_broader_masem_overall_20260612.csv`',
        '- `paper_b_broader_masem_study_pair_thresholds_20260612.csv`',
    ]
    (OUT / 'PAPER_A_B_INITIAL_EXECUTION_VALIDATION_20260612.md').write_text('\n'.join(lines) + '\n')


def main():
    paper_a, _levels, _input = analyze_paper_a()
    triage, by_family, priority, _scoped = analyze_rq3()
    masem, masem_overall, thresholds, _pairs, _studies, _readiness = analyze_masem_feasibility()
    write_report(paper_a, triage, by_family, priority, masem, masem_overall, thresholds)
    print('wrote', OUT.relative_to(REPO))
    print('paper_a_moderator_feasibility')
    print(paper_a[['moderator_candidate','studies_nonmissing','level_count','min_level_studies','construct_pairs_with_nonmissing','gate_status']].to_string(index=False))
    cm = triage[triage['signal'] == 'cross_model_behavior_disagreement'].iloc[0]
    print('cross_model_precision', round(cm['precision_review_needed'], 3), 'recall', round(cm['recall_review_needed'], 3), 'lift', round(cm['precision_lift_vs_baseline'], 3))
    print('masem_feasibility')
    print(masem[['construct_set','construct_count','required_pairs','covered_pairs','complete_case_studies','min_pair_study_count','initial_execution_validation']].to_string(index=False))

if __name__ == '__main__':
    main()
