#!/usr/bin/env python3
"""
Generate forest plots for meta-analysis results.
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from pathlib import Path
import logging
from typing import List, Optional
import numpy as np

logger = logging.getLogger(__name__)


class ForestPlotGenerator:
    """Generates forest plots for meta-analysis results."""

    def __init__(self, figsize=(10, 8)):
        """
        Initialize forest plot generator.

        Args:
            figsize: Figure size (width, height)
        """
        self.figsize = figsize

    def create_forest_plot(self, data: pd.DataFrame, correlation_pair: str,
                          output_path: Path, title: Optional[str] = None):
        """
        Create forest plot for a single correlation.

        Args:
            data: DataFrame with columns ['study', 'r', 'ci_lower', 'ci_upper', 'n']
            correlation_pair: Name of correlation (e.g., "PE-BI")
            output_path: Path to save plot
            title: Optional custom title
        """
        logger.info(f"Generating forest plot for {correlation_pair}")

        # Sort by effect size
        data_sorted = data.sort_values('r', ascending=True).reset_index(drop=True)

        # Create figure
        fig, ax = plt.subplots(figsize=self.figsize)

        # Y positions for studies
        y_positions = np.arange(len(data_sorted))

        # Plot individual studies
        for i, row in data_sorted.iterrows():
            # Confidence interval line
            ax.plot([row['ci_lower'], row['ci_upper']], [i, i],
                   'k-', linewidth=1.5, zorder=1)

            # Point estimate (square sized by sample size)
            marker_size = np.sqrt(row['n']) * 2  # Scale by sqrt of n
            ax.scatter(row['r'], i, s=marker_size, marker='s',
                      color='steelblue', edgecolor='black', linewidth=0.5,
                      zorder=2)

        # Add study labels
        ax.set_yticks(y_positions)
        ax.set_yticklabels(data_sorted['study'])

        # Add pooled estimate if available
        if 'pooled_r' in data.columns and 'pooled_ci_lower' in data.columns:
            pooled_r = data['pooled_r'].iloc[0]
            pooled_ci_lower = data['pooled_ci_lower'].iloc[0]
            pooled_ci_upper = data['pooled_ci_upper'].iloc[0]

            # Add horizontal line above studies
            y_pooled = len(data_sorted) + 0.5

            # Draw pooled estimate
            ax.plot([pooled_ci_lower, pooled_ci_upper], [y_pooled, y_pooled],
                   'k-', linewidth=2.5, zorder=3)
            ax.scatter(pooled_r, y_pooled, s=200, marker='D',
                      color='darkred', edgecolor='black', linewidth=1,
                      zorder=4)

            # Add label
            ax.text(ax.get_xlim()[0], y_pooled, 'Pooled Effect',
                   ha='right', va='center', fontweight='bold', fontsize=10)

        # Add vertical line at zero effect
        ax.axvline(x=0, color='gray', linestyle='--', linewidth=1, alpha=0.5)

        # Labels and title
        ax.set_xlabel('Correlation Coefficient (r)', fontsize=12, fontweight='bold')
        ax.set_ylabel('Study', fontsize=12, fontweight='bold')

        if title:
            ax.set_title(title, fontsize=14, fontweight='bold', pad=20)
        else:
            ax.set_title(f'Forest Plot: {correlation_pair}',
                        fontsize=14, fontweight='bold', pad=20)

        # Add heterogeneity statistics if available
        if 'I2' in data.columns and 'Q_p' in data.columns:
            I2 = data['I2'].iloc[0]
            Q_p = data['Q_p'].iloc[0]

            stats_text = f"I² = {I2:.1f}%, p(Q) = {Q_p:.3f}"
            ax.text(0.02, 0.98, stats_text,
                   transform=ax.transAxes,
                   verticalalignment='top',
                   bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5),
                   fontsize=9)

        # Grid
        ax.grid(axis='x', alpha=0.3, linestyle=':', linewidth=0.5)

        # Tight layout
        plt.tight_layout()

        # Save
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.close()

        logger.info(f"Forest plot saved to {output_path}")

    def create_multiple_forest_plots(self, results_file: Path, output_dir: Path,
                                    correlations: Optional[List[str]] = None):
        """
        Create forest plots for multiple correlations.

        Args:
            results_file: Path to CSV with meta-analysis results
            output_dir: Directory to save plots
            correlations: List of correlation pairs to plot (None = all)
        """
        # Load results
        results = pd.read_csv(results_file)

        # Get unique correlation pairs
        if 'correlation_pair' not in results.columns:
            logger.error("Results file must have 'correlation_pair' column")
            return

        all_pairs = results['correlation_pair'].unique()

        if correlations is None:
            correlations = all_pairs

        # Create output directory
        output_dir.mkdir(parents=True, exist_ok=True)

        # Generate plot for each correlation
        for pair in correlations:
            if pair not in all_pairs:
                logger.warning(f"Correlation pair not found in results: {pair}")
                continue

            pair_data = results[results['correlation_pair'] == pair]

            output_path = output_dir / f"forest_plot_{pair.replace('-', '_')}.png"

            self.create_forest_plot(
                pair_data,
                pair,
                output_path
            )

        logger.info(f"Generated {len(correlations)} forest plots in {output_dir}")


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="Generate forest plots for meta-analysis")
    parser.add_argument('--results', type=str, required=True,
                       help='Path to meta-analysis results CSV file')
    parser.add_argument('--output-dir', type=str, default='forest_plots',
                       help='Directory to save forest plots')
    parser.add_argument('--correlations', nargs='+',
                       help='Specific correlation pairs to plot (e.g., PE-BI EE-BI)')

    args = parser.parse_args()

    # Setup logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    # Generate plots
    generator = ForestPlotGenerator()
    generator.create_multiple_forest_plots(
        Path(args.results),
        Path(args.output_dir),
        args.correlations
    )


if __name__ == "__main__":
    # Example usage with dummy data
    example_data = pd.DataFrame({
        'study': ['Smith et al. (2023)', 'Jones et al. (2023)', 'Lee et al. (2024)',
                 'Wang et al. (2024)', 'Brown et al. (2024)'],
        'r': [0.45, 0.52, 0.38, 0.61, 0.48],
        'ci_lower': [0.35, 0.42, 0.28, 0.51, 0.38],
        'ci_upper': [0.55, 0.62, 0.48, 0.71, 0.58],
        'n': [150, 200, 120, 180, 160],
        'pooled_r': [0.49] * 5,
        'pooled_ci_lower': [0.44] * 5,
        'pooled_ci_upper': [0.54] * 5,
        'I2': [42.3] * 5,
        'Q_p': [0.042] * 5,
        'correlation_pair': ['PE-BI'] * 5
    })

    generator = ForestPlotGenerator()
    generator.create_forest_plot(
        example_data,
        'PE-BI',
        Path('example_forest_plot.png')
    )
    print("Example forest plot generated: example_forest_plot.png")
