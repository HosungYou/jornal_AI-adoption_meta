#!/usr/bin/env python3
"""
AI-assisted title/abstract screening for systematic review.
Uses Claude to score studies on PRISMA dimensions.
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / 'ai_coding_pipeline'))

import pandas as pd
import json
from datetime import datetime
from typing import Dict, Any, List
import logging

from utils.llm_clients import ClaudeClient
from utils.cost_tracker import CostTracker
from utils.audit import AuditLogger

logger = logging.getLogger(__name__)


class AIScreener:
    """AI-assisted screening for systematic review."""

    def __init__(self, config_path: str = "scripts/ai_coding_pipeline/config.yaml"):
        """Initialize AI screener."""
        import yaml

        with open(config_path, 'r') as f:
            self.config = yaml.safe_load(f)

        self.cost_tracker = CostTracker()
        self.audit_logger = AuditLogger(self.config['paths']['logs'])

        self.claude = ClaudeClient(
            model=self.config['models']['claude']['model'],
            cost_tracker=self.cost_tracker
        )

        self.screening_dimensions = self.config['screening']['dimensions']

    def screen_record(self, title: str, abstract: str) -> Dict[str, Any]:
        """
        Screen a single record.

        Args:
            title: Article title
            abstract: Article abstract

        Returns:
            Screening result with scores and decision
        """
        system_prompt = f"""You are an expert systematic reviewer screening studies for a meta-analysis on AI adoption.

Screen the following study on these dimensions:
1. Population: Does it study users/organizations adopting AI technology?
2. Intervention: Does it examine AI adoption, acceptance, or use behavior?
3. Outcome: Does it report correlations or regression results between constructs?
4. Study design: Is it quantitative empirical research?
5. Correlation reporting: Does it report correlations between at least 2 constructs?
6. Language: Is it in English?

For each dimension, respond with YES, NO, or UNCLEAR.

Then provide an overall decision: INCLUDE, EXCLUDE, or UNCERTAIN.

Respond in JSON format:
{{
  "population": "YES|NO|UNCLEAR",
  "intervention": "YES|NO|UNCLEAR",
  "outcome": "YES|NO|UNCLEAR",
  "study_design": "YES|NO|UNCLEAR",
  "correlation_reporting": "YES|NO|UNCLEAR",
  "language": "YES|NO|UNCLEAR",
  "decision": "INCLUDE|EXCLUDE|UNCERTAIN",
  "rationale": "Brief explanation (1-2 sentences)"
}}"""

        user_prompt = f"""Title: {title}

Abstract:
{abstract}

Please screen this study."""

        response = self.claude.send_prompt(
            system=system_prompt,
            user=user_prompt,
            temperature=0.0,
            max_tokens=512
        )

        # Parse response
        try:
            result = json.loads(response['content'])
        except json.JSONDecodeError:
            if '```json' in response['content']:
                json_start = response['content'].find('```json') + 7
                json_end = response['content'].find('```', json_start)
                result = json.loads(response['content'][json_start:json_end])
            else:
                result = {
                    'decision': 'UNCERTAIN',
                    'rationale': 'Failed to parse response'
                }

        result['tokens_used'] = response.get('input_tokens', 0) + response.get('output_tokens', 0)

        return result

    def screen_batch(self, records: pd.DataFrame, output_path: Path) -> pd.DataFrame:
        """
        Screen a batch of records.

        Args:
            records: DataFrame with 'title' and 'abstract' columns
            output_path: Path to save screening results

        Returns:
            DataFrame with screening results
        """
        logger.info(f"Screening {len(records)} records")

        results = []

        for idx, row in records.iterrows():
            try:
                screening_result = self.screen_record(
                    row.get('title', ''),
                    row.get('abstract', '')
                )

                result_row = {
                    'record_id': idx,
                    'title': row.get('title', ''),
                    **screening_result
                }

                results.append(result_row)

                # Log to audit
                self.audit_logger.log_event(
                    phase='screening',
                    event_type='record_screened',
                    details={
                        'record_id': idx,
                        'decision': screening_result.get('decision'),
                        'tokens': screening_result.get('tokens_used')
                    }
                )

                if (idx + 1) % 10 == 0:
                    logger.info(f"Screened {idx + 1}/{len(records)} records")

            except Exception as e:
                logger.error(f"Failed to screen record {idx}: {e}")
                results.append({
                    'record_id': idx,
                    'title': row.get('title', ''),
                    'decision': 'ERROR',
                    'rationale': str(e)
                })

        # Create results DataFrame
        results_df = pd.DataFrame(results)

        # Save results
        results_df.to_csv(output_path, index=False)
        logger.info(f"Screening results saved to {output_path}")

        # Print summary
        decision_counts = results_df['decision'].value_counts()
        logger.info(f"Screening summary: {decision_counts.to_dict()}")

        return results_df


def main():
    """Main entry point for AI screening."""
    import argparse

    parser = argparse.ArgumentParser(description="AI-assisted title/abstract screening")
    parser.add_argument('input', type=str, help='Path to input CSV file with title and abstract columns')
    parser.add_argument('output', type=str, help='Path to output CSV file for screening results')
    parser.add_argument('--config', type=str, default='scripts/ai_coding_pipeline/config.yaml',
                       help='Path to configuration file')

    args = parser.parse_args()

    # Setup logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    # Load records
    logger.info(f"Loading records from {args.input}")
    records = pd.read_csv(args.input)

    # Initialize screener
    screener = AIScreener(config_path=args.config)

    # Screen records
    results = screener.screen_batch(records, Path(args.output))

    # Print cost summary
    logger.info("\nCost Summary:")
    screener.cost_tracker.print_summary()


if __name__ == "__main__":
    main()
