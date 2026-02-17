#!/usr/bin/env python3
"""
Phase 5: Discrepancy Resolution
Compare AI consensus with human coding and resolve discrepancies.
Priority: Original text > Human > AI consensus
"""

import logging
from pathlib import Path
from typing import Dict, Any, List, Optional
import json
from datetime import datetime
import pandas as pd
import numpy as np

from utils.metrics import cohens_kappa, icc_2_1, mae

logger = logging.getLogger(__name__)


class DiscrepancyResolver:
    """Resolves discrepancies between AI and human coding."""

    def __init__(self, config: Dict[str, Any], cost_tracker, audit_logger):
        self.config = config
        self.cost_tracker = cost_tracker
        self.audit_logger = audit_logger

        self.quality_targets = config['quality_targets']

    def load_human_coding(self, template_path: Path) -> pd.DataFrame:
        """
        Load completed human coding from ICR template.

        Args:
            template_path: Path to completed ICR Excel template

        Returns:
            DataFrame with human coding
        """
        logger.info(f"Loading human coding from: {template_path}")
        df = pd.read_excel(template_path, sheet_name='ICR_Coding')

        # Filter to only verified entries
        df_verified = df[df['VERIFIED'].notna() & (df['VERIFIED'] != '')]

        logger.info(f"Loaded {len(df_verified)} verified human-coded entries")
        return df_verified

    def compare_values(self, ai_value: Any, human_value: Any,
                      value_type: str) -> Dict[str, Any]:
        """
        Compare AI and human values for a single field.

        Args:
            ai_value: AI-extracted value
            human_value: Human-coded value
            value_type: Type of value ('correlation', 'categorical', 'numerical')

        Returns:
            Comparison result
        """
        if pd.isna(human_value) or human_value == '':
            return {
                'match': None,
                'discrepancy': None,
                'resolution': ai_value,
                'resolution_reason': 'human_not_provided'
            }

        if value_type == 'correlation':
            # Numerical comparison with tolerance
            try:
                ai_val = float(ai_value) if ai_value is not None else None
                human_val = float(human_value)

                if ai_val is None:
                    return {
                        'match': False,
                        'discrepancy': abs(human_val),
                        'resolution': human_val,
                        'resolution_reason': 'ai_missing'
                    }

                discrepancy = abs(ai_val - human_val)
                match = discrepancy <= 0.05  # 5% tolerance

                return {
                    'match': match,
                    'discrepancy': round(discrepancy, 4),
                    'ai_value': ai_val,
                    'human_value': human_val,
                    'resolution': human_val if discrepancy > 0.05 else ai_val,
                    'resolution_reason': 'human_override' if discrepancy > 0.05 else 'ai_confirmed'
                }

            except (ValueError, TypeError) as e:
                logger.warning(f"Failed to parse correlation values: {e}")
                return {
                    'match': False,
                    'error': str(e),
                    'resolution': human_value,
                    'resolution_reason': 'parse_error'
                }

        elif value_type == 'categorical':
            # Exact match for categorical
            match = str(ai_value).strip().lower() == str(human_value).strip().lower()

            return {
                'match': match,
                'ai_value': ai_value,
                'human_value': human_value,
                'resolution': human_value if not match else ai_value,
                'resolution_reason': 'human_override' if not match else 'ai_confirmed'
            }

        elif value_type == 'numerical':
            # Numerical comparison for sample size, year, etc.
            try:
                ai_val = int(ai_value) if ai_value is not None else None
                human_val = int(human_value)

                match = ai_val == human_val

                return {
                    'match': match,
                    'ai_value': ai_val,
                    'human_value': human_val,
                    'resolution': human_val if not match else ai_val,
                    'resolution_reason': 'human_override' if not match else 'ai_confirmed'
                }

            except (ValueError, TypeError) as e:
                logger.warning(f"Failed to parse numerical values: {e}")
                return {
                    'match': False,
                    'error': str(e),
                    'resolution': human_value,
                    'resolution_reason': 'parse_error'
                }

        else:
            raise ValueError(f"Unknown value_type: {value_type}")

    def resolve_study_discrepancies(self, human_coded: pd.DataFrame,
                                    study_id: str) -> Dict[str, Any]:
        """
        Resolve discrepancies for a single study.

        Args:
            human_coded: DataFrame with human coding
            study_id: Study identifier

        Returns:
            Resolution result for the study
        """
        # Filter to this study
        study_rows = human_coded[human_coded['study_id'] == study_id]

        if len(study_rows) == 0:
            logger.warning(f"No human coding found for study: {study_id}")
            return None

        # Compare correlations
        correlation_comparisons = []

        for _, row in study_rows.iterrows():
            corr_comparison = self.compare_values(
                row['AI_r_value'],
                row['HUMAN_r_value'],
                'correlation'
            )

            corr_comparison['construct_1'] = row['construct_1']
            corr_comparison['construct_2'] = row['construct_2']
            correlation_comparisons.append(corr_comparison)

        # Compare metadata fields (use first row since they should be study-level)
        first_row = study_rows.iloc[0]

        sample_size_comparison = self.compare_values(
            first_row['AI_sample_size'],
            first_row['HUMAN_sample_size'],
            'numerical'
        )

        year_comparison = self.compare_values(
            first_row['AI_year'],
            first_row['HUMAN_year'],
            'numerical'
        )

        ai_type_comparison = self.compare_values(
            first_row['AI_ai_type'],
            first_row['HUMAN_ai_type'],
            'categorical'
        )

        region_comparison = self.compare_values(
            first_row['AI_region'],
            first_row['HUMAN_region'],
            'categorical'
        )

        # Calculate agreement statistics
        n_correlations = len(correlation_comparisons)
        n_matches = sum(1 for c in correlation_comparisons if c.get('match') == True)
        match_rate = n_matches / n_correlations if n_correlations > 0 else 0

        result = {
            'study_id': study_id,
            'resolution_timestamp': datetime.now().isoformat(),
            'n_correlations': n_correlations,
            'n_matches': n_matches,
            'match_rate': round(match_rate, 3),
            'correlation_comparisons': correlation_comparisons,
            'metadata_comparisons': {
                'sample_size': sample_size_comparison,
                'year': year_comparison,
                'ai_type': ai_type_comparison,
                'region': region_comparison
            },
            'resolved_correlations': [
                {
                    'construct_1': c['construct_1'],
                    'construct_2': c['construct_2'],
                    'r': c['resolution'],
                    'resolution_reason': c['resolution_reason']
                }
                for c in correlation_comparisons
            ],
            'resolved_metadata': {
                'sample_size': sample_size_comparison['resolution'],
                'year': year_comparison['resolution'],
                'ai_type': ai_type_comparison['resolution'],
                'region': region_comparison['resolution']
            }
        }

        return result

    def calculate_agreement_metrics(self, resolution_results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Calculate overall agreement metrics across all resolved studies.

        Args:
            resolution_results: List of resolution results

        Returns:
            Agreement metrics
        """
        # Collect all correlation comparisons
        ai_values = []
        human_values = []

        for result in resolution_results:
            for comp in result['correlation_comparisons']:
                if comp.get('match') is not None and 'ai_value' in comp and 'human_value' in comp:
                    ai_values.append(comp['ai_value'])
                    human_values.append(comp['human_value'])

        # Calculate ICC for correlations
        if len(ai_values) >= 10:  # Need sufficient data
            icc_value = icc_2_1(ai_values, human_values)
            mae_value = mae(ai_values, human_values)
        else:
            icc_value = None
            mae_value = None

        # Categorical agreement for metadata
        ai_types = []
        human_types = []
        regions = []
        human_regions = []

        for result in resolution_results:
            meta = result.get('metadata_comparisons', {})

            if 'ai_type' in meta and 'ai_value' in meta['ai_type']:
                ai_types.append(meta['ai_type']['ai_value'])
                human_types.append(meta['ai_type']['human_value'])

            if 'region' in meta and 'ai_value' in meta['region']:
                regions.append(meta['region']['ai_value'])
                human_regions.append(meta['region']['human_value'])

        # Cohen's kappa for categorical
        kappa_ai_type = cohens_kappa(ai_types, human_types) if len(ai_types) >= 5 else None
        kappa_region = cohens_kappa(regions, human_regions) if len(regions) >= 5 else None

        metrics = {
            'n_studies': len(resolution_results),
            'n_correlations': len(ai_values),
            'correlation_metrics': {
                'icc_2_1': round(icc_value, 4) if icc_value is not None else None,
                'mae': round(mae_value, 4) if mae_value is not None else None,
                'target_icc': self.quality_targets['icc_numerical'],
                'target_mae': self.quality_targets['mae_correlation'],
                'icc_passed': icc_value >= self.quality_targets['icc_numerical'] if icc_value else False,
                'mae_passed': mae_value <= self.quality_targets['mae_correlation'] if mae_value else False
            },
            'categorical_metrics': {
                'ai_type_kappa': round(kappa_ai_type, 4) if kappa_ai_type is not None else None,
                'region_kappa': round(kappa_region, 4) if kappa_region is not None else None,
                'target_kappa': self.quality_targets['kappa_categorical'],
                'ai_type_passed': kappa_ai_type >= self.quality_targets['kappa_categorical'] if kappa_ai_type else False,
                'region_passed': kappa_region >= self.quality_targets['kappa_categorical'] if kappa_region else False
            }
        }

        return metrics

    def process_all_resolutions(self, human_coded: pd.DataFrame,
                                output_dir: Path) -> Dict[str, Any]:
        """
        Process all resolutions and generate unified dataset.

        Args:
            human_coded: DataFrame with human coding
            output_dir: Directory to save resolution results

        Returns:
            Summary of resolution process
        """
        # Get unique study IDs
        study_ids = human_coded['study_id'].unique()
        logger.info(f"Resolving discrepancies for {len(study_ids)} studies")

        resolution_results = []

        for study_id in study_ids:
            result = self.resolve_study_discrepancies(human_coded, study_id)
            if result:
                resolution_results.append(result)

                # Save individual result
                output_path = output_dir / f"{study_id}_resolved.json"
                with open(output_path, 'w') as f:
                    json.dump(result, indent=2, fp=f)

        # Calculate agreement metrics
        agreement_metrics = self.calculate_agreement_metrics(resolution_results)

        # Save all resolutions
        all_resolutions_path = output_dir / 'all_resolutions.json'
        with open(all_resolutions_path, 'w') as f:
            json.dump(resolution_results, indent=2, fp=f)

        # Save agreement metrics
        metrics_path = output_dir / 'agreement_metrics.json'
        with open(metrics_path, 'w') as f:
            json.dump(agreement_metrics, indent=2, fp=f)

        summary = {
            'n_studies_resolved': len(resolution_results),
            'agreement_metrics': agreement_metrics
        }

        return summary


def resolve_discrepancies(config: Dict[str, Any], cost_tracker, audit_logger) -> Dict[str, Any]:
    """
    Phase 5 entry point: Resolve discrepancies between AI and human coding.

    Args:
        config: Pipeline configuration
        cost_tracker: Cost tracking instance
        audit_logger: Audit logging instance

    Returns:
        Result dictionary with success status and statistics
    """
    logger.info("Starting Phase 5: Discrepancy Resolution")

    try:
        resolver = DiscrepancyResolver(config, cost_tracker, audit_logger)

        # Load human coding
        icr_dir = Path(config['paths']['verified']) / 'icr_sample'
        template_path = icr_dir / 'ICR_coding_template.xlsx'

        if not template_path.exists():
            logger.error(f"Human coding template not found: {template_path}")
            return {
                'success': False,
                'error': 'Human coding template not found. Complete Phase 4 first and have humans code the template.'
            }

        human_coded = resolver.load_human_coding(template_path)

        # Create output directory
        output_dir = Path(config['paths']['verified']) / 'resolved'
        output_dir.mkdir(parents=True, exist_ok=True)

        # Process all resolutions
        summary = resolver.process_all_resolutions(human_coded, output_dir)

        # Log to audit
        audit_logger.log_event(
            phase='phase5',
            event_type='discrepancy_resolution',
            details=summary
        )

        logger.info(f"Phase 5 complete: {summary}")

        return {
            'success': True,
            'summary': summary,
            'output_path': str(output_dir)
        }

    except Exception as e:
        logger.error(f"Phase 5 failed: {e}", exc_info=True)
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

    result = resolve_discrepancies(
        config,
        CostTracker(),
        AuditLogger(config['paths']['logs'])
    )

    print(json.dumps(result, indent=2))
