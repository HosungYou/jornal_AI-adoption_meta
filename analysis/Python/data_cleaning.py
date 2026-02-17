#!/usr/bin/env python3
"""
Data cleaning utilities for AI adoption meta-analysis.
Standardizes field names, handles missing values, validates data types.
"""

import pandas as pd
import numpy as np
from pathlib import Path
import logging
from typing import Dict, Any, List

logger = logging.getLogger(__name__)


class DataCleaner:
    """Cleans and standardizes extracted meta-analysis data."""

    def __init__(self):
        """Initialize data cleaner."""
        # Standard field names
        self.field_mapping = {
            # Study metadata
            'study_id': 'Study_ID',
            'studyid': 'Study_ID',
            'id': 'Study_ID',
            'authors': 'Authors',
            'author': 'Authors',
            'year': 'Year',
            'publication_year': 'Year',
            'title': 'Title',
            'sample_size': 'Sample_Size',
            'n': 'Sample_Size',
            'samplesize': 'Sample_Size',

            # Correlation fields
            'construct_1': 'Construct_1',
            'construct1': 'Construct_1',
            'construct_2': 'Construct_2',
            'construct2': 'Construct_2',
            'r': 'Pearson_r',
            'correlation': 'Pearson_r',
            'pearson_r': 'Pearson_r',

            # Categorical fields
            'ai_type': 'AI_Type',
            'aitype': 'AI_Type',
            'region': 'Region',
            'country': 'Country',
            'education_level': 'Education_Level',
            'user_role': 'User_Role',
            'discipline': 'Discipline',
            'ai_tool_type': 'AI_Tool_Type',
            'institutional_type': 'Institutional_Type'
        }

        # Valid ranges for numeric fields
        self.valid_ranges = {
            'Pearson_r': (-1.0, 1.0),
            'Year': (1990, 2030),
            'Sample_Size': (10, 100000)
        }

    def standardize_column_names(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Standardize column names using field mapping.

        Args:
            df: Input DataFrame

        Returns:
            DataFrame with standardized column names
        """
        # Convert all column names to lowercase for matching
        df_renamed = df.copy()
        df_renamed.columns = df_renamed.columns.str.lower().str.strip()

        # Apply mapping
        df_renamed = df_renamed.rename(columns=self.field_mapping)

        logger.info(f"Standardized {len(df.columns)} column names")
        return df_renamed

    def handle_missing_values(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Handle missing values appropriately for each field type.

        Args:
            df: Input DataFrame

        Returns:
            DataFrame with missing values handled
        """
        df_clean = df.copy()

        # Required fields - remove rows if missing
        required_fields = ['Study_ID', 'Construct_1', 'Construct_2', 'Pearson_r']

        for field in required_fields:
            if field in df_clean.columns:
                n_missing = df_clean[field].isna().sum()
                if n_missing > 0:
                    logger.warning(f"Removing {n_missing} rows with missing {field}")
                    df_clean = df_clean[df_clean[field].notna()]

        # Optional fields - flag but keep
        optional_fields = ['Sample_Size', 'Year', 'AI_Type', 'Region']

        for field in optional_fields:
            if field in df_clean.columns:
                n_missing = df_clean[field].isna().sum()
                if n_missing > 0:
                    logger.info(f"{field}: {n_missing} missing values retained")

        return df_clean

    def validate_numeric_ranges(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Validate numeric fields are within expected ranges.

        Args:
            df: Input DataFrame

        Returns:
            DataFrame with out-of-range values flagged
        """
        df_validated = df.copy()

        for field, (min_val, max_val) in self.valid_ranges.items():
            if field not in df_validated.columns:
                continue

            # Check range
            out_of_range = (df_validated[field] < min_val) | (df_validated[field] > max_val)
            n_invalid = out_of_range.sum()

            if n_invalid > 0:
                logger.warning(f"{field}: {n_invalid} values out of range [{min_val}, {max_val}]")

                # Flag invalid values
                if 'validation_flags' not in df_validated.columns:
                    df_validated['validation_flags'] = ''

                df_validated.loc[out_of_range, 'validation_flags'] += f'{field}_out_of_range;'

        return df_validated

    def standardize_categorical_fields(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Standardize categorical field values.

        Args:
            df: Input DataFrame

        Returns:
            DataFrame with standardized categorical values
        """
        df_std = df.copy()

        # Construct names - uppercase
        for col in ['Construct_1', 'Construct_2']:
            if col in df_std.columns:
                df_std[col] = df_std[col].str.upper().str.strip()

        # AI Type - title case
        if 'AI_Type' in df_std.columns:
            df_std['AI_Type'] = df_std['AI_Type'].str.title().str.strip()

        # Region - title case
        if 'Region' in df_std.columns:
            df_std['Region'] = df_std['Region'].str.title().str.strip()

        # Country - title case
        if 'Country' in df_std.columns:
            df_std['Country'] = df_std['Country'].str.title().str.strip()

        logger.info("Standardized categorical fields")
        return df_std

    def enforce_data_types(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Enforce correct data types for all fields.

        Args:
            df: Input DataFrame

        Returns:
            DataFrame with enforced data types
        """
        df_typed = df.copy()

        # Define data types
        type_mapping = {
            'Study_ID': 'str',
            'Authors': 'str',
            'Year': 'Int64',  # Nullable integer
            'Title': 'str',
            'Sample_Size': 'Int64',
            'Pearson_r': 'float64',
            'Construct_1': 'str',
            'Construct_2': 'str',
            'AI_Type': 'str',
            'Region': 'str',
            'Country': 'str',
            'Industry_Sector': 'str'
        }

        for col, dtype in type_mapping.items():
            if col in df_typed.columns:
                try:
                    if dtype == 'Int64':
                        df_typed[col] = pd.to_numeric(df_typed[col], errors='coerce').astype('Int64')
                    elif dtype == 'float64':
                        df_typed[col] = pd.to_numeric(df_typed[col], errors='coerce')
                    elif dtype == 'str':
                        df_typed[col] = df_typed[col].astype(str).str.strip()
                except Exception as e:
                    logger.warning(f"Failed to convert {col} to {dtype}: {e}")

        logger.info("Enforced data types")
        return df_typed

    def clean_dataset(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Run full cleaning pipeline.

        Args:
            df: Raw input DataFrame

        Returns:
            Cleaned DataFrame
        """
        logger.info(f"Starting data cleaning pipeline on {len(df)} rows")

        # Run cleaning steps
        df_clean = df.copy()
        df_clean = self.standardize_column_names(df_clean)
        df_clean = self.standardize_categorical_fields(df_clean)
        df_clean = self.enforce_data_types(df_clean)
        df_clean = self.handle_missing_values(df_clean)
        df_clean = self.validate_numeric_ranges(df_clean)

        logger.info(f"Cleaning complete: {len(df_clean)} rows retained")

        return df_clean


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="Clean meta-analysis data")
    parser.add_argument('input', type=str, help='Path to raw data CSV file')
    parser.add_argument('output', type=str, help='Path to save cleaned data CSV file')
    parser.add_argument('--report', type=str, default='cleaning_report.txt',
                       help='Path to save cleaning report')

    args = parser.parse_args()

    # Setup logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    # Load data
    logger.info(f"Loading data from {args.input}")
    df_raw = pd.read_csv(args.input)

    # Clean data
    cleaner = DataCleaner()
    df_clean = cleaner.clean_dataset(df_raw)

    # Save cleaned data
    df_clean.to_csv(args.output, index=False)
    logger.info(f"Cleaned data saved to {args.output}")

    # Generate report
    with open(args.report, 'w') as f:
        f.write("DATA CLEANING REPORT\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"Input file: {args.input}\n")
        f.write(f"Output file: {args.output}\n\n")
        f.write(f"Rows before cleaning: {len(df_raw)}\n")
        f.write(f"Rows after cleaning: {len(df_clean)}\n")
        f.write(f"Rows removed: {len(df_raw) - len(df_clean)}\n\n")

        f.write("COLUMN SUMMARY\n")
        f.write("-" * 60 + "\n")
        for col in df_clean.columns:
            n_missing = df_clean[col].isna().sum()
            dtype = df_clean[col].dtype
            f.write(f"{col}: {dtype}, {n_missing} missing\n")

    logger.info(f"Cleaning report saved to {args.report}")


if __name__ == "__main__":
    main()
