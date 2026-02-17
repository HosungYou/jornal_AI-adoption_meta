#!/usr/bin/env python3
"""
Generate path diagram for the structural model.
Shows relationships between the 12 constructs.
"""

import logging
from pathlib import Path
from typing import Dict, Any, List, Optional
import pandas as pd

logger = logging.getLogger(__name__)


class PathDiagramGenerator:
    """Generates path diagrams for structural models."""

    def __init__(self):
        """Initialize path diagram generator."""
        # Construct groupings
        self.tam_utaut_constructs = ['PE', 'EE', 'SI', 'FC', 'BI', 'UB', 'ATT', 'SE']
        self.ai_specific_constructs = ['TRU', 'ANX', 'TRA', 'AUT']

        # Construct positions for visualization
        self.construct_positions = {
            # TAM/UTAUT constructs
            'PE': (1, 3),
            'EE': (1, 2),
            'SI': (1, 1),
            'FC': (1, 0),
            'ATT': (2, 3),
            'SE': (2, 2),
            'BI': (3, 2),
            'UB': (4, 2),
            # AI-specific constructs
            'TRU': (2, 4),
            'ANX': (2, 1),
            'TRA': (2, 0),
            'AUT': (1, 4)
        }

    def generate_graphviz_diagram(self, path_coefficients: Optional[pd.DataFrame] = None,
                                  output_path: Path = Path('path_diagram.dot')):
        """
        Generate Graphviz DOT file for path diagram.

        Args:
            path_coefficients: DataFrame with columns ['from', 'to', 'coefficient', 'p_value']
            output_path: Path to save DOT file

        Returns:
            DOT source code
        """
        dot_lines = [
            'digraph structural_model {',
            '    // Graph settings',
            '    rankdir=LR;',
            '    node [shape=box, style=filled, fontname="Arial"];',
            '    edge [fontname="Arial", fontsize=10];',
            '',
            '    // TAM/UTAUT constructs (blue)',
        ]

        # Add TAM/UTAUT nodes
        for construct in self.tam_utaut_constructs:
            dot_lines.append(f'    {construct} [fillcolor=lightblue, label="{construct}"];')

        dot_lines.append('')
        dot_lines.append('    // AI-specific constructs (green)')

        # Add AI-specific nodes
        for construct in self.ai_specific_constructs:
            dot_lines.append(f'    {construct} [fillcolor=lightgreen, label="{construct}"];')

        dot_lines.append('')
        dot_lines.append('    // Paths')

        # Add edges
        if path_coefficients is not None:
            for _, row in path_coefficients.iterrows():
                from_node = row['from']
                to_node = row['to']
                coef = row['coefficient']
                p_value = row.get('p_value', 1.0)

                # Style based on significance
                if p_value < 0.001:
                    style = 'bold'
                    color = 'black'
                elif p_value < 0.01:
                    style = 'solid'
                    color = 'black'
                elif p_value < 0.05:
                    style = 'dashed'
                    color = 'gray'
                else:
                    style = 'dotted'
                    color = 'lightgray'

                label = f'{coef:.3f}'
                if p_value < 0.05:
                    label += '*' if p_value < 0.01 else ''
                    label += '*' if p_value < 0.001 else ''

                dot_lines.append(f'    {from_node} -> {to_node} [label="{label}", style={style}, color={color}];')
        else:
            # Add hypothetical paths if no coefficients provided
            hypothetical_paths = [
                ('PE', 'BI'),
                ('EE', 'BI'),
                ('SI', 'BI'),
                ('FC', 'UB'),
                ('ATT', 'BI'),
                ('SE', 'BI'),
                ('BI', 'UB'),
                ('TRU', 'BI'),
                ('ANX', 'BI'),
                ('TRA', 'TRU'),
                ('AUT', 'ANX')
            ]

            for from_node, to_node in hypothetical_paths:
                dot_lines.append(f'    {from_node} -> {to_node};')

        dot_lines.append('}')

        dot_source = '\n'.join(dot_lines)

        # Save to file
        with open(output_path, 'w') as f:
            f.write(dot_source)

        logger.info(f"Graphviz DOT file saved to {output_path}")
        logger.info("To generate PNG: dot -Tpng path_diagram.dot -o path_diagram.png")
        logger.info("To generate PDF: dot -Tpdf path_diagram.dot -o path_diagram.pdf")

        return dot_source

    def generate_text_diagram(self, output_path: Path = Path('path_diagram.txt')):
        """
        Generate simple text-based path diagram.

        Args:
            output_path: Path to save text diagram
        """
        diagram = """
STRUCTURAL MODEL PATH DIAGRAM
================================================================================

TAM/UTAUT CONSTRUCTS (Core Technology Acceptance):
┌─────────────────────────────────────────────────────────────────────────┐
│                                                                         │
│  PE (Performance Expectancy) ──────┐                                   │
│  EE (Effort Expectancy) ────────────┼──→ BI (Behavioral Intention) ──→ │
│  SI (Social Influence) ─────────────┤                                   │
│  ATT (Attitude) ────────────────────┘         │                         │
│  SE (Self-Efficacy) ────────────────┘         │                         │
│                                                ▼                         │
│  FC (Facilitating Conditions) ────────────→ UB (Use Behavior)          │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘

AI-SPECIFIC CONSTRUCTS (AI Trust & Anxiety):
┌─────────────────────────────────────────────────────────────────────────┐
│                                                                         │
│  TRA (AI Transparency) ──────→ TRU (AI Trust) ──────┐                  │
│                                                      │                  │
│  AUT (Perceived AI Autonomy) ──→ ANX (AI Anxiety) ──┼──→ BI           │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘

CONSTRUCT DEFINITIONS:
  PE:  Degree to which AI is expected to improve job performance
  EE:  Ease of using AI technology
  SI:  Influence of important others on AI use
  FC:  Organizational/technical support for AI use
  BI:  Intention to use AI technology
  UB:  Actual AI usage behavior
  ATT: General attitude toward AI
  SE:  Confidence in ability to use AI
  TRU: Trust in AI decisions and recommendations
  ANX: Anxiety or concern about AI
  TRA: Perceived transparency of AI processes
  AUT: Perceived autonomy of AI systems

================================================================================
"""
        with open(output_path, 'w') as f:
            f.write(diagram)

        logger.info(f"Text path diagram saved to {output_path}")


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="Generate path diagram for structural model")
    parser.add_argument('--coefficients', type=str,
                       help='Path to CSV file with path coefficients (columns: from, to, coefficient, p_value)')
    parser.add_argument('--output-dot', type=str, default='path_diagram.dot',
                       help='Path to save Graphviz DOT file')
    parser.add_argument('--output-text', type=str, default='path_diagram.txt',
                       help='Path to save text diagram')

    args = parser.parse_args()

    # Setup logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    # Load path coefficients if provided
    path_coefficients = None
    if args.coefficients:
        path_coefficients = pd.read_csv(args.coefficients)

    # Generate diagrams
    generator = PathDiagramGenerator()
    generator.generate_graphviz_diagram(path_coefficients, Path(args.output_dot))
    generator.generate_text_diagram(Path(args.output_text))

    logger.info("Path diagram generation complete")


if __name__ == "__main__":
    main()
