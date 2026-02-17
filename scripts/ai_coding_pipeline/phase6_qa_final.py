#!/usr/bin/env python3
"""
Phase 6: QA Final
Run 6 quality gates on the final dataset before MASEM analysis.
"""

import logging
from pathlib import Path
from typing import Dict, Any, List, Tuple
import json
from datetime import datetime
import pandas as pd
import numpy as np

from utils.matrix_utils import (
    long_to_matrix, check_positive_definite, validate_correlation_matrix,
    matrix_completeness
)

logger = logging.getLogger(__name__)


class QAFinalChecker:
    """Runs comprehensive quality checks on final dataset."""

    def __init__(self, config: Dict[str, Any], cost_tracker, audit_logger):
        self.config = config
        self.cost_tracker = cost_tracker
        self.audit_logger = audit_logger
        self.quality_targets = config['quality_targets']

        self.gates = [
            ('Gate 1: Positive Definite Matrices', self.gate1_positive_definite),
            ('Gate 2: ICR Thresholds', self.gate2_icr_thresholds),
            ('Gate 3: No Duplicates', self.gate3_no_duplicates),
            ('Gate 4: Valid Constructs', self.gate4_valid_constructs),
            ('Gate 5: Correlation Range', self.gate5_correlation_range),
            ('Gate 6: Sample Size Consistency', self.gate6_sample_size_consistency)
        ]

    def load_consensus_and_resolved_data(self, consensus_dir: Path,
                                        resolved_dir: Path) -> pd.DataFrame:
        """
        Load and merge consensus data with resolved discrepancies.

        Args:
            consensus_dir: Directory with consensus results
            resolved_dir: Directory with resolved discrepancies

        Returns:
            Unified DataFrame with all studies
        """
        # Load all consensus files
        consensus_files = list(consensus_dir.glob("*_consensus.json"))

        # Load resolved files if they exist
        resolved_files = {}
        if resolved_dir.exists():
            for file_path in resolved_dir.glob("*_resolved.json"):
                with open(file_path, 'r') as f:
                    data = json.load(f)
                    resolved_files[data['study_id']] = data

        # Build unified dataset
        all_rows = []

        for consensus_file in consensus_files:
            with open(consensus_file, 'r') as f:
                consensus_data = json.load(f)

            study_id = consensus_data['study_id']

            # Check if this study was resolved
            if study_id in resolved_files:
                # Use resolved data
                resolved_data = resolved_files[study_id]

                for corr in resolved_data['resolved_correlations']:
                    all_rows.append({
                        'study_id': study_id,
                        'construct_1': corr['construct_1'],
                        'construct_2': corr['construct_2'],
                        'r': corr['r'],
                        'n': resolved_data['resolved_metadata']['sample_size'],
                        'year': resolved_data['resolved_metadata']['year'],
                        'ai_type': resolved_data['resolved_metadata']['ai_type'],
                        'region': resolved_data['resolved_metadata']['region'],
                        'data_source': 'resolved'
                    })

            else:
                # Use consensus data
                field_agreement = consensus_data.get('agreement_analysis', {}).get('field_agreement', {})

                sample_size = field_agreement.get('sample_size', {}).get('mode')
                year = field_agreement.get('study_year', {}).get('mode')
                ai_type = field_agreement.get('ai_type', {}).get('mode')
                region = field_agreement.get('region', {}).get('mode')

                for corr in consensus_data['consensus_correlations']:
                    all_rows.append({
                        'study_id': study_id,
                        'construct_1': corr['construct_1'],
                        'construct_2': corr['construct_2'],
                        'r': corr['r_consensus'],
                        'n': sample_size[0] if sample_size else None,
                        'year': year[0] if year else None,
                        'ai_type': ai_type[0] if ai_type else None,
                        'region': region[0] if region else None,
                        'data_source': 'consensus'
                    })

        df = pd.DataFrame(all_rows)
        logger.info(f"Loaded {len(df)} correlation entries from {df['study_id'].nunique()} studies")

        return df

    def gate1_positive_definite(self, df: pd.DataFrame) -> Tuple[bool, Dict[str, Any]]:
        """
        Gate 1: All correlation matrices must be positive definite.

        Args:
            df: Unified dataset

        Returns:
            (passed, details)
        """
        logger.info("Running Gate 1: Positive Definite Matrices")

        study_ids = df['study_id'].unique()
        issues = []
        n_passed = 0

        for study_id in study_ids:
            study_df = df[df['study_id'] == study_id]

            # Build correlation matrix
            try:
                matrix = long_to_matrix(
                    study_df,
                    construct_cols=('construct_1', 'construct_2'),
                    value_col='r'
                )

                # Check positive definite
                is_pd, eigenvalues = check_positive_definite(matrix)

                if is_pd:
                    n_passed += 1
                else:
                    issues.append({
                        'study_id': study_id,
                        'issue': 'not_positive_definite',
                        'min_eigenvalue': float(np.min(eigenvalues))
                    })

            except Exception as e:
                issues.append({
                    'study_id': study_id,
                    'issue': 'matrix_construction_failed',
                    'error': str(e)
                })

        passed = len(issues) == 0

        details = {
            'n_studies_checked': len(study_ids),
            'n_passed': n_passed,
            'n_failed': len(issues),
            'issues': issues
        }

        logger.info(f"Gate 1: {'PASSED' if passed else 'FAILED'} ({n_passed}/{len(study_ids)} studies)")

        return passed, details

    def gate2_icr_thresholds(self, df: pd.DataFrame) -> Tuple[bool, Dict[str, Any]]:
        """
        Gate 2: ICR metrics must meet threshold requirements.

        Args:
            df: Unified dataset

        Returns:
            (passed, details)
        """
        logger.info("Running Gate 2: ICR Thresholds")

        # Load agreement metrics from Phase 5
        metrics_path = Path(self.config['paths']['verified']) / 'resolved' / 'agreement_metrics.json'

        if not metrics_path.exists():
            logger.warning("No agreement metrics found (Phase 5 may not have run)")
            return True, {'status': 'not_applicable', 'reason': 'no_human_coding'}

        with open(metrics_path, 'r') as f:
            metrics = json.load(f)

        # Check thresholds
        corr_metrics = metrics.get('correlation_metrics', {})
        cat_metrics = metrics.get('categorical_metrics', {})

        icc_passed = corr_metrics.get('icc_passed', False)
        mae_passed = corr_metrics.get('mae_passed', False)
        ai_type_passed = cat_metrics.get('ai_type_passed', False)
        region_passed = cat_metrics.get('region_passed', False)

        all_passed = icc_passed and mae_passed and ai_type_passed and region_passed

        details = {
            'icc_2_1': corr_metrics.get('icc_2_1'),
            'icc_target': corr_metrics.get('target_icc'),
            'icc_passed': icc_passed,
            'mae': corr_metrics.get('mae'),
            'mae_target': corr_metrics.get('target_mae'),
            'mae_passed': mae_passed,
            'ai_type_kappa': cat_metrics.get('ai_type_kappa'),
            'ai_type_passed': ai_type_passed,
            'region_kappa': cat_metrics.get('region_kappa'),
            'region_passed': region_passed,
            'all_passed': all_passed
        }

        logger.info(f"Gate 2: {'PASSED' if all_passed else 'FAILED'}")

        return all_passed, details

    def gate3_no_duplicates(self, df: pd.DataFrame) -> Tuple[bool, Dict[str, Any]]:
        """
        Gate 3: No duplicate study entries.

        Args:
            df: Unified dataset

        Returns:
            (passed, details)
        """
        logger.info("Running Gate 3: No Duplicates")

        # Check for duplicate correlations within studies
        df['pair'] = df.apply(lambda row: tuple(sorted([row['construct_1'], row['construct_2']])), axis=1)

        duplicates = df[df.duplicated(subset=['study_id', 'pair'], keep=False)]

        if len(duplicates) > 0:
            duplicate_details = duplicates.groupby(['study_id', 'pair']).size().reset_index(name='count')
            duplicate_list = duplicate_details.to_dict('records')
        else:
            duplicate_list = []

        passed = len(duplicates) == 0

        details = {
            'n_duplicates': len(duplicates),
            'duplicates': duplicate_list
        }

        logger.info(f"Gate 3: {'PASSED' if passed else 'FAILED'} ({len(duplicates)} duplicates)")

        return passed, details

    def gate4_valid_constructs(self, df: pd.DataFrame) -> Tuple[bool, Dict[str, Any]]:
        """
        Gate 4: All construct names must be in the standard set.

        Args:
            df: Unified dataset

        Returns:
            (passed, details)
        """
        logger.info("Running Gate 4: Valid Constructs")

        valid_constructs = set(self.config['constructs']['names'])

        all_constructs = set(df['construct_1'].unique()) | set(df['construct_2'].unique())
        invalid_constructs = all_constructs - valid_constructs

        passed = len(invalid_constructs) == 0

        details = {
            'valid_constructs': list(valid_constructs),
            'invalid_constructs': list(invalid_constructs),
            'n_invalid': len(invalid_constructs)
        }

        logger.info(f"Gate 4: {'PASSED' if passed else 'FAILED'} ({len(invalid_constructs)} invalid)")

        return passed, details

    def gate5_correlation_range(self, df: pd.DataFrame) -> Tuple[bool, Dict[str, Any]]:
        """
        Gate 5: All r values must be in [-1, 1] range.

        Args:
            df: Unified dataset

        Returns:
            (passed, details)
        """
        logger.info("Running Gate 5: Correlation Range")

        # Check for out-of-range values
        out_of_range = df[(df['r'] < -1) | (df['r'] > 1)]

        passed = len(out_of_range) == 0

        details = {
            'n_out_of_range': len(out_of_range),
            'min_r': float(df['r'].min()),
            'max_r': float(df['r'].max()),
            'out_of_range_entries': out_of_range[['study_id', 'construct_1', 'construct_2', 'r']].to_dict('records') if len(out_of_range) > 0 else []
        }

        logger.info(f"Gate 5: {'PASSED' if passed else 'FAILED'} ({len(out_of_range)} out of range)")

        return passed, details

    def gate6_sample_size_consistency(self, df: pd.DataFrame) -> Tuple[bool, Dict[str, Any]]:
        """
        Gate 6: Sample sizes must be consistent within studies.

        Args:
            df: Unified dataset

        Returns:
            (passed, details)
        """
        logger.info("Running Gate 6: Sample Size Consistency")

        # Check for varying sample sizes within studies
        study_n_variance = df.groupby('study_id')['n'].nunique()
        inconsistent_studies = study_n_variance[study_n_variance > 1].index.tolist()

        passed = len(inconsistent_studies) == 0

        details = {
            'n_inconsistent_studies': len(inconsistent_studies),
            'inconsistent_studies': inconsistent_studies
        }

        logger.info(f"Gate 6: {'PASSED' if passed else 'FAILED'} ({len(inconsistent_studies)} inconsistent)")

        return passed, details

    def run_all_gates(self, df: pd.DataFrame) -> Dict[str, Any]:
        """
        Run all quality gates.

        Args:
            df: Unified dataset

        Returns:
            QA report with all gate results
        """
        logger.info("Running all quality gates...")

        gate_results = []
        all_passed = True

        for gate_name, gate_func in self.gates:
            passed, details = gate_func(df)
            gate_results.append({
                'gate': gate_name,
                'passed': passed,
                'details': details
            })

            if not passed:
                all_passed = False

        qa_report = {
            'qa_timestamp': datetime.now().isoformat(),
            'all_gates_passed': all_passed,
            'gate_results': gate_results,
            'dataset_summary': {
                'n_studies': df['study_id'].nunique(),
                'n_correlations': len(df),
                'constructs_used': sorted(set(df['construct_1'].unique()) | set(df['construct_2'].unique())),
                'year_range': [int(df['year'].min()), int(df['year'].max())] if df['year'].notna().any() else None,
                'sample_size_range': [int(df['n'].min()), int(df['n'].max())] if df['n'].notna().any() else None
            }
        }

        return qa_report

    def export_final_dataset(self, df: pd.DataFrame, output_path: Path):
        """
        Export final dataset to CSV.

        Args:
            df: Unified dataset
            output_path: Path to save CSV
        """
        # Clean and prepare for export
        df_export = df.copy()

        # Sort by study_id and construct pairs
        df_export = df_export.sort_values(['study_id', 'construct_1', 'construct_2'])

        # Save to CSV
        df_export.to_csv(output_path, index=False)
        logger.info(f"Final dataset exported to: {output_path}")

        # Also save as Excel for easier viewing
        excel_path = output_path.with_suffix('.xlsx')
        df_export.to_excel(excel_path, index=False, sheet_name='AI_Adoption_MASEM')
        logger.info(f"Final dataset also saved as Excel: {excel_path}")


def run_qa_final(config: Dict[str, Any], cost_tracker, audit_logger) -> Dict[str, Any]:
    """
    Phase 6 entry point: Run QA Final quality gates.

    Args:
        config: Pipeline configuration
        cost_tracker: Cost tracking instance
        audit_logger: Audit logging instance

    Returns:
        Result dictionary with success status and QA report
    """
    logger.info("Starting Phase 6: QA Final")

    try:
        qa_checker = QAFinalChecker(config, cost_tracker, audit_logger)

        # Load consensus and resolved data
        consensus_dir = Path(config['paths']['verified'])
        resolved_dir = Path(config['paths']['verified']) / 'resolved'

        df = qa_checker.load_consensus_and_resolved_data(consensus_dir, resolved_dir)

        # Run all quality gates
        qa_report = qa_checker.run_all_gates(df)

        # Save QA report
        output_dir = Path(config['paths']['final'])
        output_dir.mkdir(parents=True, exist_ok=True)

        report_path = output_dir / 'qa_report.json'
        with open(report_path, 'w') as f:
            json.dump(qa_report, indent=2, fp=f)

        # Export final dataset
        dataset_path = output_dir / 'AI_Adoption_MASEM_Final_Dataset.csv'
        qa_checker.export_final_dataset(df, dataset_path)

        # Log to audit
        audit_logger.log_event(
            phase='phase6',
            event_type='qa_final',
            details={
                'all_gates_passed': qa_report['all_gates_passed'],
                'n_studies': qa_report['dataset_summary']['n_studies'],
                'n_correlations': qa_report['dataset_summary']['n_correlations']
            }
        )

        summary = {
            'all_gates_passed': qa_report['all_gates_passed'],
            'n_studies': qa_report['dataset_summary']['n_studies'],
            'n_correlations': qa_report['dataset_summary']['n_correlations'],
            'failed_gates': [
                g['gate'] for g in qa_report['gate_results'] if not g['passed']
            ]
        }

        logger.info(f"Phase 6 complete: {summary}")

        return {
            'success': qa_report['all_gates_passed'],
            'summary': summary,
            'output_path': str(output_dir),
            'dataset_path': str(dataset_path),
            'qa_report': qa_report
        }

    except Exception as e:
        logger.error(f"Phase 6 failed: {e}", exc_info=True)
        return {
            'success': False,
            'error': str(e)
        }


if __name__ == "__main__":
    # For testing independently
    import yaml
    from utils.cost_tracker import CostTracker
    from utils.audit import AuditLogger

    with open('scripts/ai_coding_pipeline/config.yaml') as f:
        config = yaml.safe_load(f)

    result = run_qa_final(
        config,
        CostTracker(),
        AuditLogger(config['paths']['logs'])
    )

    print(json.dumps(result, indent=2))
