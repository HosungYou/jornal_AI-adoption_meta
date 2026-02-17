#!/usr/bin/env python3
"""
Phase 4: Sampling for Inter-Coder Reliability (ICR)
Stratified sampling of 20% of studies for human verification.
"""

import logging
from pathlib import Path
from typing import Dict, Any, List
import json
from datetime import datetime
import random
import pandas as pd
from collections import defaultdict

logger = logging.getLogger(__name__)


class ICRSampler:
    """Stratified sampling for inter-coder reliability testing."""

    def __init__(self, config: Dict[str, Any], cost_tracker, audit_logger):
        self.config = config
        self.cost_tracker = cost_tracker
        self.audit_logger = audit_logger
        self.sample_pct = config['quality_targets']['human_sample_pct']

    def load_consensus_data(self, consensus_dir: Path) -> List[Dict[str, Any]]:
        """
        Load all consensus results.

        Args:
            consensus_dir: Directory with consensus results

        Returns:
            List of consensus studies
        """
        consensus_files = list(consensus_dir.glob("*_consensus.json"))
        logger.info(f"Loading {len(consensus_files)} consensus files")

        studies = []
        for file_path in consensus_files:
            with open(file_path, 'r') as f:
                study = json.load(f)
                studies.append(study)

        return studies

    def extract_stratification_vars(self, study: Dict[str, Any]) -> Dict[str, Any]:
        """
        Extract variables for stratification.

        Args:
            study: Consensus study data

        Returns:
            Dictionary with stratification variables
        """
        # Get field agreement from consensus
        field_agreement = study.get('agreement_analysis', {}).get('field_agreement', {})

        # Extract modal values
        study_year = None
        ai_type = None
        region = None

        if 'study_year' in field_agreement:
            year_mode = field_agreement['study_year'].get('mode')
            if year_mode:
                study_year = year_mode[0]  # (value, count) tuple

        if 'ai_type' in field_agreement:
            ai_mode = field_agreement['ai_type'].get('mode')
            if ai_mode:
                ai_type = ai_mode[0]

        if 'region' in field_agreement:
            region_mode = field_agreement['region'].get('mode')
            if region_mode:
                region = region_mode[0]

        # Assign to tertiles for year
        year_tertile = None
        if study_year:
            if study_year < 2020:
                year_tertile = 'early'
            elif study_year < 2023:
                year_tertile = 'middle'
            else:
                year_tertile = 'recent'

        return {
            'study_id': study['study_id'],
            'study_year': study_year,
            'year_tertile': year_tertile,
            'ai_type': ai_type or 'unknown',
            'region': region or 'unknown',
            'n_correlations': len(study.get('consensus_correlations', []))
        }

    def stratified_sample(self, studies: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Perform stratified random sampling.

        Args:
            studies: List of all consensus studies

        Returns:
            Sampling result with selected studies and statistics
        """
        # Extract stratification variables
        study_metadata = [self.extract_stratification_vars(s) for s in studies]

        # Create strata based on year_tertile, ai_type, and region
        strata = defaultdict(list)

        for meta in study_metadata:
            stratum_key = (
                meta['year_tertile'],
                meta['ai_type'],
                meta['region']
            )
            strata[stratum_key].append(meta)

        logger.info(f"Created {len(strata)} strata")

        # Sample from each stratum
        sampled_studies = []
        stratum_stats = []

        for stratum_key, stratum_studies in strata.items():
            n_stratum = len(stratum_studies)
            n_sample = max(1, int(n_stratum * self.sample_pct))  # At least 1 per stratum

            # Random sample
            sample = random.sample(stratum_studies, min(n_sample, n_stratum))
            sampled_studies.extend(sample)

            stratum_stats.append({
                'year_tertile': stratum_key[0],
                'ai_type': stratum_key[1],
                'region': stratum_key[2],
                'n_total': n_stratum,
                'n_sampled': len(sample),
                'sample_rate': round(len(sample) / n_stratum, 3)
            })

        # Overall statistics
        total_studies = len(study_metadata)
        total_sampled = len(sampled_studies)

        result = {
            'sampling_timestamp': datetime.now().isoformat(),
            'total_studies': total_studies,
            'total_sampled': total_sampled,
            'target_sample_pct': self.sample_pct,
            'actual_sample_pct': round(total_sampled / total_studies, 3),
            'n_strata': len(strata),
            'stratum_statistics': stratum_stats,
            'sampled_study_ids': [s['study_id'] for s in sampled_studies],
            'sampled_studies': sampled_studies
        }

        return result

    def create_icr_template(self, sampled_studies: List[Dict[str, Any]],
                           consensus_dir: Path, output_path: Path):
        """
        Create Excel template for human coding.

        Args:
            sampled_studies: List of sampled study metadata
            consensus_dir: Directory with full consensus data
            output_path: Path to save Excel template
        """
        # Load full data for sampled studies
        rows = []

        for study_meta in sampled_studies:
            study_id = study_meta['study_id']
            consensus_file = consensus_dir / f"{study_id}_consensus.json"

            with open(consensus_file, 'r') as f:
                consensus_data = json.load(f)

            # Extract AI consensus values for verification
            field_agreement = consensus_data.get('agreement_analysis', {}).get('field_agreement', {})

            sample_size_mode = field_agreement.get('sample_size', {}).get('mode')
            year_mode = field_agreement.get('study_year', {}).get('mode')
            ai_type_mode = field_agreement.get('ai_type', {}).get('mode')
            region_mode = field_agreement.get('region', {}).get('mode')

            # Create row for each correlation
            for corr in consensus_data.get('consensus_correlations', []):
                rows.append({
                    'study_id': study_id,
                    'construct_1': corr['construct_1'],
                    'construct_2': corr['construct_2'],
                    'AI_r_value': corr['r_consensus'],
                    'AI_sample_size': sample_size_mode[0] if sample_size_mode else None,
                    'AI_year': year_mode[0] if year_mode else None,
                    'AI_ai_type': ai_type_mode[0] if ai_type_mode else None,
                    'AI_region': region_mode[0] if region_mode else None,
                    'consensus_quality': corr['consensus_quality'],
                    'flag': corr.get('flag', ''),
                    # Empty columns for human coder
                    'HUMAN_r_value': '',
                    'HUMAN_sample_size': '',
                    'HUMAN_year': '',
                    'HUMAN_ai_type': '',
                    'HUMAN_region': '',
                    'HUMAN_notes': '',
                    'VERIFIED': ''
                })

        # Create DataFrame
        df = pd.DataFrame(rows)

        # Save to Excel
        with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name='ICR_Coding', index=False)

            # Format worksheet
            worksheet = writer.sheets['ICR_Coding']

            # Set column widths
            column_widths = {
                'A': 20,  # study_id
                'B': 15,  # construct_1
                'C': 15,  # construct_2
                'D': 12,  # AI_r_value
                'E': 15,  # AI_sample_size
                'F': 12,  # AI_year
                'G': 20,  # AI_ai_type
                'H': 15,  # AI_region
                'I': 18,  # consensus_quality
                'J': 20,  # flag
                'K': 12,  # HUMAN_r_value
                'L': 15,  # HUMAN_sample_size
                'M': 12,  # HUMAN_year
                'N': 20,  # HUMAN_ai_type
                'O': 15,  # HUMAN_region
                'P': 30,  # HUMAN_notes
                'Q': 12   # VERIFIED
            }

            for col, width in column_widths.items():
                worksheet.column_dimensions[col].width = width

            # Add header formatting
            from openpyxl.styles import Font, PatternFill, Alignment

            header_fill = PatternFill(start_color="366092", end_color="366092", fill_type="solid")
            header_font = Font(color="FFFFFF", bold=True)

            for cell in worksheet[1]:
                cell.fill = header_fill
                cell.font = header_font
                cell.alignment = Alignment(horizontal='center', vertical='center')

        logger.info(f"ICR template created: {output_path}")
        logger.info(f"Template contains {len(rows)} correlation entries from {len(sampled_studies)} studies")

    def generate_sampling_report(self, sampling_result: Dict[str, Any],
                                output_path: Path):
        """
        Generate detailed sampling report.

        Args:
            sampling_result: Result from stratified_sample
            output_path: Path to save report
        """
        report_lines = [
            "INTER-CODER RELIABILITY SAMPLING REPORT",
            "=" * 60,
            "",
            f"Sampling Date: {sampling_result['sampling_timestamp']}",
            f"Total Studies: {sampling_result['total_studies']}",
            f"Total Sampled: {sampling_result['total_sampled']}",
            f"Target Sample %: {sampling_result['target_sample_pct'] * 100:.1f}%",
            f"Actual Sample %: {sampling_result['actual_sample_pct'] * 100:.1f}%",
            f"Number of Strata: {sampling_result['n_strata']}",
            "",
            "STRATUM BREAKDOWN",
            "-" * 60,
            ""
        ]

        # Add stratum details
        for stratum in sampling_result['stratum_statistics']:
            report_lines.append(
                f"Year: {stratum['year_tertile']}, AI Type: {stratum['ai_type']}, "
                f"Region: {stratum['region']}"
            )
            report_lines.append(
                f"  Total: {stratum['n_total']}, Sampled: {stratum['n_sampled']}, "
                f"Rate: {stratum['sample_rate'] * 100:.1f}%"
            )
            report_lines.append("")

        report_lines.extend([
            "",
            "SAMPLED STUDY IDs",
            "-" * 60,
            ""
        ])

        for study_id in sorted(sampling_result['sampled_study_ids']):
            report_lines.append(f"  - {study_id}")

        # Write report
        with open(output_path, 'w') as f:
            f.write('\n'.join(report_lines))

        logger.info(f"Sampling report generated: {output_path}")


def sample_for_icr(config: Dict[str, Any], cost_tracker, audit_logger) -> Dict[str, Any]:
    """
    Phase 4 entry point: Stratified sampling for ICR.

    Args:
        config: Pipeline configuration
        cost_tracker: Cost tracking instance
        audit_logger: Audit logging instance

    Returns:
        Result dictionary with success status and statistics
    """
    logger.info("Starting Phase 4: Sampling for ICR")

    try:
        sampler = ICRSampler(config, cost_tracker, audit_logger)

        # Load consensus data
        consensus_dir = Path(config['paths']['verified'])
        studies = sampler.load_consensus_data(consensus_dir)

        # Perform stratified sampling
        sampling_result = sampler.stratified_sample(studies)

        # Create output directory
        output_dir = Path(config['paths']['verified']) / 'icr_sample'
        output_dir.mkdir(parents=True, exist_ok=True)

        # Save sampling result
        result_path = output_dir / 'sampling_result.json'
        with open(result_path, 'w') as f:
            json.dump(sampling_result, indent=2, fp=f)

        # Create ICR template
        template_path = output_dir / 'ICR_coding_template.xlsx'
        sampler.create_icr_template(
            sampling_result['sampled_studies'],
            consensus_dir,
            template_path
        )

        # Generate report
        report_path = output_dir / 'sampling_report.txt'
        sampler.generate_sampling_report(sampling_result, report_path)

        # Log to audit
        audit_logger.log_event(
            phase='phase4',
            event_type='icr_sampling',
            details={
                'total_studies': sampling_result['total_studies'],
                'total_sampled': sampling_result['total_sampled'],
                'sample_rate': sampling_result['actual_sample_pct']
            }
        )

        summary = {
            'total_studies': sampling_result['total_studies'],
            'total_sampled': sampling_result['total_sampled'],
            'sample_rate': sampling_result['actual_sample_pct'],
            'n_strata': sampling_result['n_strata']
        }

        logger.info(f"Phase 4 complete: {summary}")

        return {
            'success': True,
            'summary': summary,
            'output_path': str(output_dir),
            'template_path': str(template_path)
        }

    except Exception as e:
        logger.error(f"Phase 4 failed: {e}", exc_info=True)
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

    result = sample_for_icr(
        config,
        CostTracker(),
        AuditLogger(config['paths']['logs'])
    )

    print(json.dumps(result, indent=2))
