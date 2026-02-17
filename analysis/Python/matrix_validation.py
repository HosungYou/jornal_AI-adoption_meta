#!/usr/bin/env python3
"""
Matrix validation for meta-analysis.
Python version of matrix validation utilities.
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / 'scripts' / 'ai_coding_pipeline'))

import pandas as pd
import numpy as np
import json
from typing import Dict, Any, List
import logging

from utils.matrix_utils import (
    long_to_matrix, check_positive_definite, validate_correlation_matrix,
    matrix_completeness, nearest_pd
)

logger = logging.getLogger(__name__)


def validate_all_matrices(data_path: Path, output_dir: Path) -> Dict[str, Any]:
    """
    Validate all correlation matrices in the dataset.

    Args:
        data_path: Path to correlation data CSV
        output_dir: Directory to save validation results

    Returns:
        Validation summary
    """
    logger.info(f"Loading data from {data_path}")
    df = pd.read_csv(data_path)

    # Get unique studies
    study_ids = df['Study_ID'].unique()
    logger.info(f"Validating {len(study_ids)} studies")

    output_dir.mkdir(parents=True, exist_ok=True)

    results = []
    summary = {
        'total_studies': len(study_ids),
        'valid_count': 0,
        'invalid_count': 0,
        'error_count': 0,
        'completeness_stats': [],
        'eigenvalue_stats': []
    }

    for study_id in study_ids:
        study_df = df[df['Study_ID'] == study_id]

        try:
            # Build matrix
            matrix = long_to_matrix(
                study_df,
                construct_cols=('Construct_1', 'Construct_2'),
                value_col='Pearson_r'
            )

            # Validate
            validation = validate_correlation_matrix(matrix, check_pd=True)
            completeness = matrix_completeness(matrix)

            # Check PD
            is_pd, eigenvalues = check_positive_definite(matrix)

            result = {
                'study_id': study_id,
                'status': 'valid' if validation['valid'] else 'invalid',
                'dimension': validation['dimension'],
                'is_positive_definite': is_pd,
                'min_eigenvalue': float(np.min(eigenvalues)),
                'max_eigenvalue': float(np.max(eigenvalues)),
                'completeness_rate': completeness['completeness_rate'],
                'n_correlations': completeness['filled_correlations']
            }

            # Track statistics
            summary['eigenvalue_stats'].append(float(np.min(eigenvalues)))
            summary['completeness_stats'].append(completeness['completeness_rate'])

            if validation['valid']:
                summary['valid_count'] += 1
            else:
                summary['invalid_count'] += 1
                logger.warning(f"Invalid matrix: {study_id}")

            results.append(result)

        except Exception as e:
            logger.error(f"Error validating {study_id}: {e}")
            summary['error_count'] += 1
            results.append({
                'study_id': study_id,
                'status': 'error',
                'error': str(e)
            })

    # Save results
    results_df = pd.DataFrame(results)
    results_df.to_csv(output_dir / 'validation_results.csv', index=False)

    # Calculate aggregate statistics
    if summary['eigenvalue_stats']:
        summary['mean_min_eigenvalue'] = float(np.mean(summary['eigenvalue_stats']))
        summary['min_eigenvalue_overall'] = float(np.min(summary['eigenvalue_stats']))

    if summary['completeness_stats']:
        summary['mean_completeness'] = float(np.mean(summary['completeness_stats']))

    # Save summary
    with open(output_dir / 'validation_summary.json', 'w') as f:
        json.dump(summary, indent=2, fp=f)

    logger.info(f"Validation complete: {summary['valid_count']}/{summary['total_studies']} valid")

    return summary


def generate_validation_report(summary: Dict[str, Any], output_path: Path):
    """
    Generate human-readable validation report.

    Args:
        summary: Validation summary
        output_path: Path to save report
    """
    with open(output_path, 'w') as f:
        f.write("CORRELATION MATRIX VALIDATION REPORT\n")
        f.write("=" * 60 + "\n\n")

        f.write(f"Total studies: {summary['total_studies']}\n")
        f.write(f"Valid matrices: {summary['valid_count']}\n")
        f.write(f"Invalid matrices: {summary['invalid_count']}\n")
        f.write(f"Errors: {summary['error_count']}\n")
        f.write(f"Validation rate: {summary['valid_count'] / summary['total_studies'] * 100:.1f}%\n\n")

        if 'mean_min_eigenvalue' in summary:
            f.write("EIGENVALUE STATISTICS\n")
            f.write("-" * 60 + "\n")
            f.write(f"Mean minimum eigenvalue: {summary['mean_min_eigenvalue']:.6f}\n")
            f.write(f"Overall minimum eigenvalue: {summary['min_eigenvalue_overall']:.6f}\n\n")

        if 'mean_completeness' in summary:
            f.write("COMPLETENESS STATISTICS\n")
            f.write("-" * 60 + "\n")
            f.write(f"Mean completeness rate: {summary['mean_completeness'] * 100:.1f}%\n\n")

    logger.info(f"Validation report saved to {output_path}")


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="Validate correlation matrices")
    parser.add_argument('input', type=str, help='Path to correlation data CSV')
    parser.add_argument('--output-dir', type=str, default='validation_output',
                       help='Directory to save validation results')

    args = parser.parse_args()

    # Setup logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    # Validate
    summary = validate_all_matrices(Path(args.input), Path(args.output_dir))

    # Generate report
    generate_validation_report(summary, Path(args.output_dir) / 'validation_report.txt')


if __name__ == "__main__":
    main()
