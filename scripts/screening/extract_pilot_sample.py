#!/usr/bin/env python3
"""Extract a stratified pilot sample from the screening master CSV."""

import argparse
import pandas as pd
from pathlib import Path


def stratified_sample(df: pd.DataFrame, n: int, stratum_col: str = "source_database",
                      seed: int = 42) -> pd.DataFrame:
    """
    Extract a stratified sample maintaining proportions of stratum_col.

    Args:
        df: Full DataFrame
        n: Target sample size
        stratum_col: Column to stratify by
        seed: Random seed

    Returns:
        Stratified sample DataFrame
    """
    proportions = df[stratum_col].value_counts(normalize=True)
    samples = []

    remaining = n
    strata = list(proportions.index)

    for i, stratum in enumerate(strata):
        stratum_df = df[df[stratum_col] == stratum]
        if i == len(strata) - 1:
            stratum_n = max(0, remaining)
        else:
            stratum_n = max(1, round(proportions[stratum] * n))
            remaining -= stratum_n

        stratum_n = min(stratum_n, len(stratum_df))
        if stratum_n > 0:
            samples.append(stratum_df.sample(n=stratum_n, random_state=seed))

    result = pd.concat(samples, ignore_index=True)
    return result.sort_values("record_id").reset_index(drop=True)


def main():
    parser = argparse.ArgumentParser(description="Extract stratified pilot sample")
    parser.add_argument("--input", type=str,
                        default="data/processed/screening_master_16189_20260217.csv")
    parser.add_argument("--output", type=str,
                        default="data/processed/pilot_100_sample.csv")
    parser.add_argument("--n", type=int, default=100)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    df = pd.read_csv(args.input)
    print(f"Loaded {len(df)} records from {args.input}")

    sample = stratified_sample(df, n=args.n, seed=args.seed)

    # Report stratification
    print(f"\nPilot sample: {len(sample)} records")
    print("\nStratification (source_database):")
    orig_pct = df["source_database"].value_counts(normalize=True)
    sample_pct = sample["source_database"].value_counts(normalize=True)
    for db in orig_pct.index:
        orig_p = orig_pct.get(db, 0) * 100
        samp_p = sample_pct.get(db, 0) * 100
        samp_n = int((sample["source_database"] == db).sum())
        print(f"  {db}: {samp_n} records ({samp_p:.1f}% vs {orig_p:.1f}% original)")

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    sample.to_csv(output_path, index=False)
    print(f"\nSaved to {output_path}")


if __name__ == "__main__":
    main()
