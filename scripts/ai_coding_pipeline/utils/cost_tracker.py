#!/usr/bin/env python3
"""
Cost tracking for LLM API usage.
Tracks tokens and calculates costs per model and per phase.
"""

import json
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, Optional
from collections import defaultdict


class CostTracker:
    """Tracks token usage and costs across all LLM API calls."""

    def __init__(self):
        """Initialize cost tracker."""
        self.usage_data = defaultdict(lambda: {
            'input_tokens': 0,
            'output_tokens': 0,
            'total_calls': 0
        })

        # Pricing per million tokens (input, output)
        self.pricing = {
            'claude-sonnet-4-5-20250929': (3.00, 15.00),
            'claude-sonnet-3-5-20241022': (3.00, 15.00),
            'claude-opus-3-5-20240229': (15.00, 75.00),
            'gpt-4o': (2.50, 10.00),
            'gpt-4o-2024-11-20': (2.50, 10.00),
            'gpt-4-turbo': (10.00, 30.00),
            'llama-3.3-70b-versatile': (0.59, 0.79),
            'llama-3.1-70b-versatile': (0.59, 0.79),
            'mixtral-8x7b-32768': (0.24, 0.24)
        }

    def track(self, model: str, input_tokens: int, output_tokens: int):
        """
        Track token usage for a model.

        Args:
            model: Model identifier
            input_tokens: Number of input tokens
            output_tokens: Number of output tokens
        """
        self.usage_data[model]['input_tokens'] += input_tokens
        self.usage_data[model]['output_tokens'] += output_tokens
        self.usage_data[model]['total_calls'] += 1

    def get_cost(self, model: str) -> float:
        """
        Calculate total cost for a model.

        Args:
            model: Model identifier

        Returns:
            Total cost in dollars
        """
        if model not in self.usage_data:
            return 0.0

        usage = self.usage_data[model]

        # Get pricing (default to 0 if not found)
        input_price, output_price = self.pricing.get(model, (0.0, 0.0))

        # Calculate cost
        input_cost = (usage['input_tokens'] / 1_000_000) * input_price
        output_cost = (usage['output_tokens'] / 1_000_000) * output_price

        total_cost = input_cost + output_cost

        return total_cost

    def get_summary(self) -> Dict[str, Any]:
        """
        Get summary of all usage and costs.

        Returns:
            Dictionary with usage and cost statistics per model
        """
        summary = {}

        for model, usage in self.usage_data.items():
            cost = self.get_cost(model)

            summary[model] = {
                'input_tokens': usage['input_tokens'],
                'output_tokens': usage['output_tokens'],
                'total_tokens': usage['input_tokens'] + usage['output_tokens'],
                'total_calls': usage['total_calls'],
                'total_cost': round(cost, 4)
            }

        # Add grand total
        total_cost = sum(s['total_cost'] for s in summary.values())
        total_tokens = sum(s['total_tokens'] for s in summary.values())
        total_calls = sum(s['total_calls'] for s in summary.values())

        summary['_TOTAL'] = {
            'input_tokens': sum(s['input_tokens'] for s in summary.values()),
            'output_tokens': sum(s['output_tokens'] for s in summary.values()),
            'total_tokens': total_tokens,
            'total_calls': total_calls,
            'total_cost': round(total_cost, 4)
        }

        return summary

    def export_csv(self, output_path: Path):
        """
        Export usage data to CSV.

        Args:
            output_path: Path to save CSV file
        """
        import csv

        summary = self.get_summary()

        with open(output_path, 'w', newline='') as f:
            writer = csv.writer(f)

            # Header
            writer.writerow([
                'Model',
                'Input Tokens',
                'Output Tokens',
                'Total Tokens',
                'Total Calls',
                'Total Cost ($)'
            ])

            # Data rows
            for model, stats in summary.items():
                writer.writerow([
                    model,
                    stats['input_tokens'],
                    stats['output_tokens'],
                    stats['total_tokens'],
                    stats['total_calls'],
                    stats['total_cost']
                ])

    def export_json(self, output_path: Path):
        """
        Export usage data to JSON.

        Args:
            output_path: Path to save JSON file
        """
        summary = self.get_summary()

        # Add metadata
        export_data = {
            'export_timestamp': datetime.now().isoformat(),
            'usage_summary': summary
        }

        with open(output_path, 'w') as f:
            json.dump(export_data, indent=2, fp=f)

    def reset(self):
        """Reset all usage data."""
        self.usage_data.clear()

    def get_phase_summary(self, phase_usage: Dict[str, Dict[str, int]]) -> Dict[str, Any]:
        """
        Get summary for a specific phase.

        Args:
            phase_usage: Dictionary mapping model to usage dict

        Returns:
            Phase summary with costs
        """
        phase_summary = {}

        for model, usage in phase_usage.items():
            input_tokens = usage.get('input_tokens', 0)
            output_tokens = usage.get('output_tokens', 0)

            # Get pricing
            input_price, output_price = self.pricing.get(model, (0.0, 0.0))

            # Calculate cost
            input_cost = (input_tokens / 1_000_000) * input_price
            output_cost = (output_tokens / 1_000_000) * output_price
            total_cost = input_cost + output_cost

            phase_summary[model] = {
                'input_tokens': input_tokens,
                'output_tokens': output_tokens,
                'total_tokens': input_tokens + output_tokens,
                'total_cost': round(total_cost, 4)
            }

        return phase_summary

    def print_summary(self):
        """Print formatted summary to console."""
        summary = self.get_summary()

        print("\n" + "=" * 80)
        print("COST TRACKER SUMMARY")
        print("=" * 80)

        for model, stats in summary.items():
            if model == '_TOTAL':
                print("\n" + "-" * 80)

            print(f"\n{model}:")
            print(f"  Input tokens:  {stats['input_tokens']:>15,}")
            print(f"  Output tokens: {stats['output_tokens']:>15,}")
            print(f"  Total tokens:  {stats['total_tokens']:>15,}")
            print(f"  Total calls:   {stats['total_calls']:>15,}")
            print(f"  Total cost:    ${stats['total_cost']:>14,.2f}")

        print("\n" + "=" * 80 + "\n")


def test_cost_tracker():
    """Test cost tracker functionality."""
    import tempfile
    import shutil

    print("Testing cost tracker...\n")

    # Create tracker
    tracker = CostTracker()

    # Track some usage
    print("1. Tracking usage...")
    tracker.track('claude-sonnet-4-5-20250929', input_tokens=10000, output_tokens=5000)
    tracker.track('claude-sonnet-4-5-20250929', input_tokens=8000, output_tokens=3000)
    tracker.track('gpt-4o', input_tokens=12000, output_tokens=6000)
    tracker.track('llama-3.3-70b-versatile', input_tokens=15000, output_tokens=8000)

    # Get summary
    print("\n2. Getting summary...")
    summary = tracker.get_summary()
    print(f"   Total models tracked: {len(summary) - 1}")  # -1 for _TOTAL
    print(f"   Total cost: ${summary['_TOTAL']['total_cost']:.2f}")

    # Print summary
    print("\n3. Printing formatted summary...")
    tracker.print_summary()

    # Export to files
    temp_dir = tempfile.mkdtemp()

    try:
        print("\n4. Exporting to CSV...")
        csv_path = Path(temp_dir) / 'usage.csv'
        tracker.export_csv(csv_path)
        print(f"   Exported to: {csv_path}")

        print("\n5. Exporting to JSON...")
        json_path = Path(temp_dir) / 'usage.json'
        tracker.export_json(json_path)
        print(f"   Exported to: {json_path}")

        # Test get_cost
        print("\n6. Getting cost for specific model...")
        claude_cost = tracker.get_cost('claude-sonnet-4-5-20250929')
        print(f"   Claude cost: ${claude_cost:.2f}")

        # Test reset
        print("\n7. Testing reset...")
        tracker.reset()
        summary_after_reset = tracker.get_summary()
        print(f"   Models after reset: {len(summary_after_reset)}")

        print("\nAll tests passed!")

    finally:
        # Cleanup
        shutil.rmtree(temp_dir)


if __name__ == "__main__":
    test_cost_tracker()
