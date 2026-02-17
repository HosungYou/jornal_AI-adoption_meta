#!/usr/bin/env python3
"""
Generate PRISMA 2020 flow diagram for systematic review.
"""

import logging
from typing import Dict, Any
from pathlib import Path

logger = logging.getLogger(__name__)


class PRISMAGenerator:
    """Generates PRISMA 2020 flow diagram."""

    def __init__(self):
        """Initialize PRISMA generator."""
        pass

    def generate_text_diagram(self, counts: Dict[str, int], output_path: Path):
        """
        Generate text-based PRISMA flow diagram.

        Args:
            counts: Dictionary with counts for each PRISMA stage
            output_path: Path to save diagram
        """
        diagram = f"""
PRISMA 2020 FLOW DIAGRAM
{'=' * 80}

IDENTIFICATION
┌─────────────────────────────────────────────────────────────┐
│ Records identified from databases (n = {counts.get('database_records', 0):,})        │
│ - Database 1: {counts.get('db1_records', 0):,}                                  │
│ - Database 2: {counts.get('db2_records', 0):,}                                  │
│ - Database 3: {counts.get('db3_records', 0):,}                                  │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
SCREENING
┌─────────────────────────────────────────────────────────────┐
│ Records after duplicates removed (n = {counts.get('after_dedup', 0):,})         │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│ Records screened (title/abstract) (n = {counts.get('screened', 0):,})           │
├─────────────────────────────────────────────────────────────┤
│ Records excluded (n = {counts.get('excluded_screening', 0):,})                  │
│ - Not AI adoption: {counts.get('excluded_not_ai', 0):,}                         │
│ - Not quantitative: {counts.get('excluded_not_quant', 0):,}                     │
│ - No correlations: {counts.get('excluded_no_corr', 0):,}                        │
│ - Language: {counts.get('excluded_language', 0):,}                              │
│ - Other: {counts.get('excluded_other', 0):,}                                    │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
ELIGIBILITY
┌─────────────────────────────────────────────────────────────┐
│ Full-text articles assessed (n = {counts.get('full_text_assessed', 0):,})       │
├─────────────────────────────────────────────────────────────┤
│ Full-text articles excluded (n = {counts.get('excluded_full_text', 0):,})       │
│ - Insufficient data: {counts.get('excluded_insufficient_data', 0):,}            │
│ - Wrong population: {counts.get('excluded_wrong_population', 0):,}              │
│ - Duplicate data: {counts.get('excluded_duplicate_data', 0):,}                  │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
INCLUDED
┌─────────────────────────────────────────────────────────────┐
│ Studies included in meta-analysis (n = {counts.get('included', 0):,})           │
│ - Total correlations extracted: {counts.get('total_correlations', 0):,}         │
│ - Unique construct pairs: {counts.get('unique_pairs', 0):,}                     │
└─────────────────────────────────────────────────────────────┘

{'=' * 80}
"""
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(diagram)

        logger.info(f"PRISMA diagram saved to {output_path}")

    def generate_summary_table(self, counts: Dict[str, int], output_path: Path):
        """
        Generate summary table of PRISMA counts.

        Args:
            counts: Dictionary with counts for each stage
            output_path: Path to save table
        """
        import pandas as pd

        # Create summary DataFrame
        summary_data = [
            {'Stage': 'Identification', 'Substage': 'Database records', 'Count': counts.get('database_records', 0)},
            {'Stage': 'Screening', 'Substage': 'After deduplication', 'Count': counts.get('after_dedup', 0)},
            {'Stage': 'Screening', 'Substage': 'Records screened', 'Count': counts.get('screened', 0)},
            {'Stage': 'Screening', 'Substage': 'Records excluded', 'Count': counts.get('excluded_screening', 0)},
            {'Stage': 'Eligibility', 'Substage': 'Full-text assessed', 'Count': counts.get('full_text_assessed', 0)},
            {'Stage': 'Eligibility', 'Substage': 'Full-text excluded', 'Count': counts.get('excluded_full_text', 0)},
            {'Stage': 'Included', 'Substage': 'Studies in meta-analysis', 'Count': counts.get('included', 0)},
            {'Stage': 'Included', 'Substage': 'Total correlations', 'Count': counts.get('total_correlations', 0)},
        ]

        df = pd.DataFrame(summary_data)

        # Save as CSV
        df.to_csv(output_path, index=False)
        logger.info(f"PRISMA summary table saved to {output_path}")

        return df


def main():
    """Main entry point."""
    import argparse
    import json

    parser = argparse.ArgumentParser(description="Generate PRISMA 2020 flow diagram")
    parser.add_argument('--counts', type=str, required=True,
                       help='Path to JSON file with PRISMA counts')
    parser.add_argument('--output-diagram', type=str, default='prisma_diagram.txt',
                       help='Path to save text diagram')
    parser.add_argument('--output-table', type=str, default='prisma_summary.csv',
                       help='Path to save summary table')

    args = parser.parse_args()

    # Setup logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    # Load counts
    with open(args.counts, 'r') as f:
        counts = json.load(f)

    # Generate diagram
    generator = PRISMAGenerator()
    generator.generate_text_diagram(counts, Path(args.output_diagram))
    generator.generate_summary_table(counts, Path(args.output_table))

    logger.info("PRISMA diagram generation complete")


if __name__ == "__main__":
    # Example counts for testing
    example_counts = {
        'database_records': 1250,
        'db1_records': 450,
        'db2_records': 520,
        'db3_records': 280,
        'after_dedup': 890,
        'screened': 890,
        'excluded_screening': 654,
        'excluded_not_ai': 320,
        'excluded_not_quant': 180,
        'excluded_no_corr': 120,
        'excluded_language': 24,
        'excluded_other': 10,
        'full_text_assessed': 236,
        'excluded_full_text': 104,
        'excluded_insufficient_data': 62,
        'excluded_wrong_population': 28,
        'excluded_duplicate_data': 14,
        'included': 132,
        'total_correlations': 1584,
        'unique_pairs': 48
    }

    generator = PRISMAGenerator()
    generator.generate_text_diagram(example_counts, Path('example_prisma.txt'))
    print("Example PRISMA diagram generated: example_prisma.txt")
