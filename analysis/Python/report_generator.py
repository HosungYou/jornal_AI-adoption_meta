#!/usr/bin/env python3
"""
Generate manuscript-ready tables and reports from meta-analysis results.
"""

import pandas as pd
import numpy as np
from pathlib import Path
import logging
from typing import Dict, Any, List

logger = logging.getLogger(__name__)


class ReportGenerator:
    """Generates manuscript-ready tables and reports."""

    def __init__(self):
        """Initialize report generator."""
        self.construct_full_names = {
            'PE': 'Performance Expectancy',
            'EE': 'Effort Expectancy',
            'SI': 'Social Influence',
            'FC': 'Facilitating Conditions',
            'BI': 'Behavioral Intention',
            'UB': 'Use Behavior',
            'ATT': 'Attitude',
            'SE': 'Self-Efficacy',
            'TRU': 'AI Trust',
            'ANX': 'AI Anxiety',
            'TRA': 'AI Transparency',
            'AUT': 'Perceived AI Autonomy'
        }

    def create_descriptive_statistics_table(self, data: pd.DataFrame,
                                           output_path: Path):
        """
        Create APA-formatted descriptive statistics table.

        Args:
            data: Meta-analysis dataset
            output_path: Path to save table
        """
        stats = {
            'Total Studies': len(data['Study_ID'].unique()),
            'Total Correlations': len(data),
            'Mean Sample Size': data.groupby('Study_ID')['Sample_Size'].first().mean(),
            'SD Sample Size': data.groupby('Study_ID')['Sample_Size'].first().std(),
            'Total Participants': data.groupby('Study_ID')['Sample_Size'].first().sum(),
            'Year Range': f"{data['Year'].min()}-{data['Year'].max()}"
        }

        # Create markdown table
        lines = [
            "# Table 1",
            "## Descriptive Statistics of Included Studies",
            "",
            "| Statistic | Value |",
            "|-----------|-------|"
        ]

        for stat, value in stats.items():
            if isinstance(value, float):
                lines.append(f"| {stat} | {value:.2f} |")
            else:
                lines.append(f"| {stat} | {value} |")

        lines.append("")

        # Add categorical breakdowns
        if 'AI_Type' in data.columns:
            lines.extend([
                "### Distribution by AI Type",
                "",
                "| AI Type | n | % |",
                "|---------|---|---|"
            ])

            ai_type_counts = data.groupby('Study_ID')['AI_Type'].first().value_counts()
            total = len(data['Study_ID'].unique())

            for ai_type, count in ai_type_counts.items():
                pct = count / total * 100
                lines.append(f"| {ai_type} | {count} | {pct:.1f}% |")

            lines.append("")

        # Save
        with open(output_path, 'w') as f:
            f.write('\n'.join(lines))

        logger.info(f"Descriptive statistics table saved to {output_path}")

    def create_meta_analysis_results_table(self, results: pd.DataFrame,
                                          output_path: Path):
        """
        Create APA-formatted meta-analysis results table.

        Args:
            results: Meta-analysis results with columns:
                     ['construct_pair', 'k', 'N', 'r', 'CI_lower', 'CI_upper', 'I2', 'Q', 'p']
            output_path: Path to save table
        """
        lines = [
            "# Table 2",
            "## Meta-Analytic Correlations Among Constructs",
            "",
            "| Relationship | k | N | r | 95% CI | I² | Q | p |",
            "|--------------|---|---|---|--------|----|----|---|"
        ]

        for _, row in results.iterrows():
            pair = row['construct_pair']
            k = row['k']
            N = row['N']
            r = row['r']
            ci = f"[{row['CI_lower']:.3f}, {row['CI_upper']:.3f}]"
            I2 = row['I2']
            Q = row['Q']
            p = row['p']

            # Format p-value
            if p < 0.001:
                p_str = "< .001"
            else:
                p_str = f"{p:.3f}"

            # Expand construct names
            c1, c2 = pair.split('-')
            relationship = f"{self.construct_full_names.get(c1, c1)} → {self.construct_full_names.get(c2, c2)}"

            lines.append(
                f"| {relationship} | {k} | {N:,} | {r:.3f}* | {ci} | {I2:.1f}% | {Q:.2f} | {p_str} |"
            )

        lines.extend([
            "",
            "*Note.* k = number of studies; N = total sample size; r = weighted mean correlation; ",
            "CI = confidence interval; I² = heterogeneity index; Q = Cochran's Q statistic; ",
            "p = significance level. All correlations significant at p < .05 unless otherwise noted.",
            ""
        ])

        # Save
        with open(output_path, 'w') as f:
            f.write('\n'.join(lines))

        logger.info(f"Meta-analysis results table saved to {output_path}")

    def create_moderator_analysis_table(self, moderator_results: pd.DataFrame,
                                       output_path: Path):
        """
        Create moderator analysis results table.

        Args:
            moderator_results: Results with columns:
                              ['construct_pair', 'moderator', 'level', 'k', 'r', 'Q_between', 'p']
            output_path: Path to save table
        """
        lines = [
            "# Table 3",
            "## Moderator Analysis Results",
            "",
            "| Relationship | Moderator | Level | k | r | Q_between | p |",
            "|--------------|-----------|-------|---|---|-----------|---|"
        ]

        for _, row in moderator_results.iterrows():
            pair = row['construct_pair']
            moderator = row['moderator']
            level = row['level']
            k = row['k']
            r = row['r']
            Q_between = row['Q_between']
            p = row['p']

            # Format p-value
            if p < 0.001:
                p_str = "< .001"
            elif p < 0.05:
                p_str = f"{p:.3f}*"
            else:
                p_str = f"{p:.3f}"

            lines.append(
                f"| {pair} | {moderator} | {level} | {k} | {r:.3f} | {Q_between:.2f} | {p_str} |"
            )

        lines.extend([
            "",
            "*Note.* k = number of studies; r = weighted mean correlation; ",
            "Q_between = between-groups heterogeneity; * p < .05.",
            ""
        ])

        # Save
        with open(output_path, 'w') as f:
            f.write('\n'.join(lines))

        logger.info(f"Moderator analysis table saved to {output_path}")

    def create_summary_report(self, data: pd.DataFrame, results: pd.DataFrame,
                            output_path: Path):
        """
        Create comprehensive summary report.

        Args:
            data: Meta-analysis dataset
            results: Meta-analysis results
            output_path: Path to save report
        """
        lines = [
            "# Meta-Analysis Summary Report",
            "## AI Adoption: Technology Acceptance and AI-Specific Factors",
            "",
            "### Dataset Overview",
            ""
        ]

        # Dataset statistics
        n_studies = len(data['Study_ID'].unique())
        n_correlations = len(data)
        n_participants = data.groupby('Study_ID')['Sample_Size'].first().sum()
        year_range = f"{data['Year'].min()}-{data['Year'].max()}"

        lines.extend([
            f"- **Number of studies**: {n_studies}",
            f"- **Total correlations**: {n_correlations}",
            f"- **Total participants**: {n_participants:,}",
            f"- **Year range**: {year_range}",
            "",
            "### Key Findings",
            ""
        ])

        # Top 5 strongest correlations
        top_5 = results.nlargest(5, 'r')
        lines.append("**Strongest Relationships:**")
        lines.append("")

        for i, row in enumerate(top_5.iterrows(), 1):
            _, row_data = row
            pair = row_data['construct_pair']
            r = row_data['r']
            k = row_data['k']

            lines.append(f"{i}. {pair}: r = {r:.3f} (k = {k})")

        lines.extend([
            "",
            "### Publication Characteristics",
            ""
        ])

        # Year distribution
        year_counts = data.groupby('Study_ID')['Year'].first().value_counts().sort_index()
        lines.append("**Studies by Year:**")
        lines.append("")
        for year, count in year_counts.items():
            lines.append(f"- {year}: {count} studies")

        # Save
        with open(output_path, 'w') as f:
            f.write('\n'.join(lines))

        logger.info(f"Summary report saved to {output_path}")


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="Generate manuscript tables and reports")
    parser.add_argument('--data', type=str, required=True,
                       help='Path to cleaned meta-analysis data CSV')
    parser.add_argument('--results', type=str, required=True,
                       help='Path to meta-analysis results CSV')
    parser.add_argument('--output-dir', type=str, default='reports',
                       help='Directory to save reports')

    args = parser.parse_args()

    # Setup logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    # Load data
    data = pd.read_csv(args.data)
    results = pd.read_csv(args.results)

    # Create output directory
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Generate reports
    generator = ReportGenerator()

    generator.create_descriptive_statistics_table(
        data,
        output_dir / 'table1_descriptives.md'
    )

    generator.create_meta_analysis_results_table(
        results,
        output_dir / 'table2_meta_results.md'
    )

    generator.create_summary_report(
        data,
        results,
        output_dir / 'summary_report.md'
    )

    logger.info("Report generation complete")


if __name__ == "__main__":
    main()
