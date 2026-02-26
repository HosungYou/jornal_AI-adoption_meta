#!/usr/bin/env python3
"""
Paper B: Stratified Random Sampling (~300 → 100)
Selects 100 studies for gold standard using proportional stratified sampling.

Usage:
    python select_paper_b_sample.py

Input:  data/00_fulltext_eligibility/fulltext_eligibility_decisions.csv
Output: data/01_sample_selection/paper_b_sample_100.csv
        data/01_sample_selection/sampling_report.md
        data/01_sample_selection/sample_vs_population_comparison.csv
"""

import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime

# =============================================================================
# Configuration
# =============================================================================
SEED = 42
TARGET_N = 100
DATA_DIR = Path(__file__).parent.parent / "data"
INPUT_FILE = DATA_DIR / "00_fulltext_eligibility" / "fulltext_eligibility_decisions.csv"
OUTPUT_DIR = DATA_DIR / "01_sample_selection"

# =============================================================================
# Load Data
# =============================================================================
print(f"Loading data from {INPUT_FILE}...")
df = pd.read_csv(INPUT_FILE)
eligible = df[df['decision'] == 'include'].copy()
print(f"Total eligible studies: {len(eligible)}")

# =============================================================================
# Define Strata
# =============================================================================
# Year stratum
eligible['year_stratum'] = pd.cut(
    eligible['year'],
    bins=[2014, 2019, 2022, 2026],
    labels=['2015-2019', '2020-2022', '2023-2025']
)

# Stratification variables
strata_vars = ['year_stratum', 'ai_tool_type', 'education_level', 'region']

# Check for missing strata values
for var in strata_vars:
    missing = eligible[var].isna().sum()
    if missing > 0:
        print(f"WARNING: {missing} missing values in {var}")

# =============================================================================
# Calculate Proportional Allocation
# =============================================================================
strata_counts = eligible.groupby(strata_vars).size()
print(f"\nNumber of strata: {len(strata_counts)}")
print(f"Strata sizes range: {strata_counts.min()} - {strata_counts.max()}")

# Proportional allocation
proportions = strata_counts / len(eligible)
sample_sizes = (proportions * TARGET_N).round().astype(int)

# Minimum 1 per stratum (or all if stratum smaller than allocation)
sample_sizes = sample_sizes.clip(lower=1)

# Adjust to exactly TARGET_N
iteration = 0
while sample_sizes.sum() != TARGET_N:
    iteration += 1
    if iteration > 100:
        print("WARNING: Could not converge to exact target N. Proceeding with closest.")
        break

    if sample_sizes.sum() > TARGET_N:
        # Remove from largest stratum (that has more allocated than 1)
        adjustable = sample_sizes[sample_sizes > 1]
        if len(adjustable) > 0:
            idx = adjustable.idxmax()
            sample_sizes[idx] -= 1
    else:
        # Add to stratum with largest remaining pool
        remaining = strata_counts - sample_sizes
        adjustable = remaining[remaining > 0]
        if len(adjustable) > 0:
            idx = adjustable.idxmax()
            sample_sizes[idx] += 1

print(f"\nFinal allocation: {sample_sizes.sum()} studies")

# =============================================================================
# Perform Sampling
# =============================================================================
np.random.seed(SEED)
sampled = []

for stratum, n in sample_sizes.items():
    mask = pd.Series([True] * len(eligible), index=eligible.index)
    for i, var in enumerate(strata_vars):
        mask &= (eligible[var] == stratum[i])

    stratum_df = eligible[mask]

    if len(stratum_df) <= n:
        sampled.append(stratum_df)
        if len(stratum_df) < n:
            print(f"  Stratum {stratum}: requested {n}, only {len(stratum_df)} available")
    else:
        sampled.append(stratum_df.sample(n=n, random_state=SEED))

sample = pd.concat(sampled)
print(f"\nSelected {len(sample)} studies for Paper B gold standard")

# =============================================================================
# Save Sample
# =============================================================================
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

sample.to_csv(OUTPUT_DIR / "paper_b_sample_100.csv", index=False)
print(f"Saved to {OUTPUT_DIR / 'paper_b_sample_100.csv'}")

# =============================================================================
# Generate Comparison Table
# =============================================================================
comparison = []
for var in strata_vars:
    pop_dist = eligible[var].value_counts(normalize=True)
    sam_dist = sample[var].value_counts(normalize=True)

    for category in pop_dist.index:
        comparison.append({
            'variable': var,
            'category': category,
            'population_n': eligible[var].value_counts().get(category, 0),
            'population_pct': round(pop_dist.get(category, 0) * 100, 1),
            'sample_n': sample[var].value_counts().get(category, 0),
            'sample_pct': round(sam_dist.get(category, 0) * 100, 1),
        })

comparison_df = pd.DataFrame(comparison)
comparison_df.to_csv(OUTPUT_DIR / "sample_vs_population_comparison.csv", index=False)

# =============================================================================
# Generate Sampling Report
# =============================================================================
report = f"""# Sampling Report

## Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
## Random Seed: {SEED}

## Summary
- Population (MASEM-eligible): {len(eligible)} studies
- Sample (Paper B gold standard): {len(sample)} studies
- Sampling method: Proportional stratified random sampling

## Stratification Variables
- Year: {eligible['year_stratum'].value_counts().to_dict()}
- AI Tool Type: {eligible['ai_tool_type'].value_counts().to_dict()}
- Education Level: {eligible['education_level'].value_counts().to_dict()}
- Region: {eligible['region'].value_counts().to_dict()}

## Sample Distribution
"""

for var in strata_vars:
    report += f"\n### {var}\n"
    report += comparison_df[comparison_df['variable'] == var].to_string(index=False)
    report += "\n"

with open(OUTPUT_DIR / "sampling_report.md", 'w') as f:
    f.write(report)

# Save seed log
with open(OUTPUT_DIR / "sampling_seed_log.txt", 'w') as f:
    f.write(f"Random seed: {SEED}\n")
    f.write(f"Timestamp: {datetime.now().isoformat()}\n")
    f.write(f"Script: select_paper_b_sample.py\n")
    f.write(f"Python: {pd.__version__} (pandas), {np.__version__} (numpy)\n")
    f.write(f"Population N: {len(eligible)}\n")
    f.write(f"Sample N: {len(sample)}\n")

print("\nDone! Files created:")
print(f"  1. {OUTPUT_DIR / 'paper_b_sample_100.csv'}")
print(f"  2. {OUTPUT_DIR / 'sampling_report.md'}")
print(f"  3. {OUTPUT_DIR / 'sample_vs_population_comparison.csv'}")
print(f"  4. {OUTPUT_DIR / 'sampling_seed_log.txt'}")
