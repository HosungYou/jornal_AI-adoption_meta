#!/usr/bin/env python3
"""
Validate correlation matrices for positive definiteness and completeness.
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / 'ai_coding_pipeline'))

import pandas as pd
import json
import logging
from typing import Dict, Any, List

from utils.matrix_utils import (
    long_to_matrix, check_positive_definite, validate_correlation_matrix,
    matrix_completeness, nearest_pd
)

logger = logging.getLogger(__name__)


class MatrixValidator:
    """Validates correlation matrices from coded data."""

    def __init__(self):
        """Initialize validator."""
        pass

    def validate_study_matrix(self, study_df: pd.DataFrame, study_id: str) -> Dict[str, Any]:
        """
        Validate correlation matrix for a single study.

        Args:
            study_df: DataFrame with correlation data for one study
            study_id: Study identifier

        Returns:
            Validation results
        """
        logger.info(f"Validating matrix for study: {study_id}")

        # Build correlation matrix
        try:
            matrix = long_to_matrix(
                study_df,
                construct_cols=('Construct_1', 'Construct_2'),
                value_col='Pearson_r'
            )
        except Exception as e:
            return {
                'study_id': study_id,
                'status': 'error',
                'error': f"Failed to build matrix: {str(e)}"
            }

        # Validate matrix
        validation_result = validate_correlation_matrix(matrix, check_pd=True)

        # Check completeness
        completeness_result = matrix_completeness(matrix)

        # Compile results
        result = {
            'study_id': study_id,
            'status': 'valid' if validation_result['valid'] else 'invalid',
            'matrix_dimension': validation_result['dimension'],
            'is_positive_definite': validation_result['is_positive_definite'],
            'min_eigenvalue': validation_result['min_eigenvalue'],
            'max_eigenvalue': validation_result['max_eigenvalue'],
            'completeness_rate': completeness_result['completeness_rate'],
            'filled_correlations': completeness_result['filled_correlations'],
            'missing_correlations': completeness_result['missing_correlations'],
            'validation_details': validation_result
        }

        # If not positive definite, suggest nearest PD matrix
        if not validation_result['is_positive_definite']:
            logger.warning(f"Study {study_id} matrix is not positive definite")
            result['needs_correction'] = True

            # Compute nearest PD matrix
            try:
                nearest_matrix = nearest_pd(matrix)
                nearest_validation = validate_correlation_matrix(nearest_matrix, check_pd=True)

                if nearest_validation['is_positive_definite']:
                    result['nearest_pd_available'] = True
                    result['nearest_pd_min_eigenvalue'] = nearest_validation['min_eigenvalue']
                else:
                    result['nearest_pd_available'] = False

            except Exception as e:
                result['nearest_pd_available'] = False
                result['nearest_pd_error'] = str(e)

        return result

    def validate_all_studies(self, correlation_df: pd.DataFrame) -> Dict[str, Any]:
        """
        Validate all study matrices.

        Args:
            correlation_df: DataFrame with all correlation data

        Returns:
            Validation summary
        """
        study_ids = correlation_df['Study_ID'].unique()
        logger.info(f"Validating matrices for {len(study_ids)} studies")

        results = []
        valid_count = 0
        invalid_count = 0
        error_count = 0

        for study_id in study_ids:
            study_df = correlation_df[correlation_df['Study_ID'] == study_id]

            result = self.validate_study_matrix(study_df, study_id)
            results.append(result)

            if result['status'] == 'valid':
                valid_count += 1
            elif result['status'] == 'invalid':
                invalid_count += 1
            else:
                error_count += 1

        summary = {
            'total_studies': len(study_ids),
            'valid_matrices': valid_count,
            'invalid_matrices': invalid_count,
            'errors': error_count,
            'validation_rate': round(valid_count / len(study_ids), 3) if study_ids.size > 0 else 0,
            'results': results
        }

        return summary

    def generate_report(self, summary: Dict[str, Any], output_path: Path):
        """
        Generate validation report.

        Args:
            summary: Validation summary
            output_path: Path to save report
        """
        report_lines = [
            "CORRELATION MATRIX VALIDATION REPORT",
            "=" * 60,
            "",
            f"Total studies validated: {summary['total_studies']}",
            f"Valid matrices: {summary['valid_matrices']}",
            f"Invalid matrices: {summary['invalid_matrices']}",
            f"Errors: {summary['errors']}",
            f"Validation rate: {summary['validation_rate'] * 100:.1f}%",
            "",
            "INVALID MATRICES",
            "-" * 60
        ]

        # List invalid matrices
        for result in summary['results']:
            if result['status'] == 'invalid':
                report_lines.append(f"\nStudy: {result['study_id']}")
                report_lines.append(f"  Dimension: {result['matrix_dimension']}")
                report_lines.append(f"  Positive definite: {result['is_positive_definite']}")
                report_lines.append(f"  Min eigenvalue: {result['min_eigenvalue']:.6f}")
                report_lines.append(f"  Completeness: {result['completeness_rate'] * 100:.1f}%")

                if result.get('needs_correction'):
                    if result.get('nearest_pd_available'):
                        report_lines.append("  → Nearest PD matrix available")
                    else:
                        report_lines.append("  → Could not compute nearest PD matrix")

        # List errors
        if summary['errors'] > 0:
            report_lines.extend([
                "",
                "ERRORS",
                "-" * 60
            ])

            for result in summary['results']:
                if result['status'] == 'error':
                    report_lines.append(f"\nStudy: {result['study_id']}")
                    report_lines.append(f"  Error: {result['error']}")

        # Write report
        with open(output_path, 'w') as f:
            f.write('\n'.join(report_lines))

        logger.info(f"Validation report saved to {output_path}")


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="Validate correlation matrices")
    parser.add_argument('input', type=str, help='Path to correlation data CSV file')
    parser.add_argument('--output', type=str, default='validation_summary.json',
                       help='Path to save validation summary JSON')
    parser.add_argument('--report', type=str, default='validation_report.txt',
                       help='Path to save validation report')

    args = parser.parse_args()

    # Setup logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    # Load correlation data
    logger.info(f"Loading correlation data from {args.input}")
    correlation_df = pd.read_csv(args.input)

    # Validate
    validator = MatrixValidator()
    summary = validator.validate_all_studies(correlation_df)

    # Save summary
    with open(args.output, 'w') as f:
        json.dump(summary, indent=2, fp=f)

    logger.info(f"Validation summary saved to {args.output}")

    # Generate report
    validator.generate_report(summary, Path(args.report))

    # Print summary to console
    logger.info(f"\nValidation Summary:")
    logger.info(f"  Valid: {summary['valid_matrices']}/{summary['total_studies']}")
    logger.info(f"  Invalid: {summary['invalid_matrices']}/{summary['total_studies']}")
    logger.info(f"  Errors: {summary['errors']}/{summary['total_studies']}")


if __name__ == "__main__":
    main()
