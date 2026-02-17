#!/usr/bin/env python3
"""
Main orchestrator for the 7-phase AI coding pipeline.
Executes all phases sequentially with error handling, logging, and cost tracking.
"""

import argparse
import logging
import sys
from pathlib import Path
from datetime import datetime
import yaml
from typing import Dict, Any, Optional

# Import all phase modules
from phase0_rag_index import build_rag_index
from phase1_extract_correlations import extract_correlations
from phase2_construct_mapping import map_constructs
from phase3_consensus import run_consensus
from phase4_sampling_icr import sample_for_icr
from phase5_resolution import resolve_discrepancies
from phase6_qa_final import run_qa_final

from utils.cost_tracker import CostTracker
from utils.audit import AuditLogger


class PipelineOrchestrator:
    """Orchestrates the 7-phase AI coding pipeline."""

    def __init__(self, config_path: str = "scripts/ai_coding_pipeline/config.yaml"):
        """Initialize orchestrator with configuration."""
        self.config_path = Path(config_path)
        self.config = self._load_config()
        self._setup_logging()
        self._setup_directories()

        self.cost_tracker = CostTracker()
        self.audit_logger = AuditLogger(self.config['paths']['logs'])

        self.phases = {
            0: ("RAG Index Building", build_rag_index),
            1: ("Correlation Extraction", extract_correlations),
            2: ("Construct Mapping", map_constructs),
            3: ("Three-Model Consensus", run_consensus),
            4: ("Sampling for ICR", sample_for_icr),
            5: ("Discrepancy Resolution", resolve_discrepancies),
            6: ("QA Final", run_qa_final)
        }

    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from YAML file."""
        if not self.config_path.exists():
            raise FileNotFoundError(f"Configuration file not found: {self.config_path}")

        with open(self.config_path, 'r') as f:
            return yaml.safe_load(f)

    def _setup_logging(self):
        """Configure logging for the pipeline."""
        log_dir = Path(self.config['paths']['logs'])
        log_dir.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        log_file = log_dir / f"pipeline_run_{timestamp}.log"

        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler(sys.stdout)
            ]
        )
        self.logger = logging.getLogger(__name__)
        self.logger.info(f"Pipeline initialized. Log file: {log_file}")

    def _setup_directories(self):
        """Create all required directories."""
        for path_key, path_value in self.config['paths'].items():
            Path(path_value).mkdir(parents=True, exist_ok=True)
        self.logger.info("All directories created/verified")

    def run_phase(self, phase_num: int) -> bool:
        """
        Run a single phase of the pipeline.

        Args:
            phase_num: Phase number (0-6)

        Returns:
            True if phase completed successfully, False otherwise
        """
        if phase_num not in self.phases:
            self.logger.error(f"Invalid phase number: {phase_num}")
            return False

        phase_name, phase_func = self.phases[phase_num]
        self.logger.info(f"{'='*60}")
        self.logger.info(f"Starting Phase {phase_num}: {phase_name}")
        self.logger.info(f"{'='*60}")

        start_time = datetime.now()

        try:
            # Run the phase function with config and trackers
            result = phase_func(
                config=self.config,
                cost_tracker=self.cost_tracker,
                audit_logger=self.audit_logger
            )

            elapsed = (datetime.now() - start_time).total_seconds()

            if result.get('success', False):
                self.logger.info(f"Phase {phase_num} completed successfully in {elapsed:.1f}s")
                self.logger.info(f"Phase {phase_num} summary: {result.get('summary', {})}")
                return True
            else:
                self.logger.error(f"Phase {phase_num} failed: {result.get('error', 'Unknown error')}")
                return False

        except Exception as e:
            elapsed = (datetime.now() - start_time).total_seconds()
            self.logger.error(f"Phase {phase_num} crashed after {elapsed:.1f}s: {str(e)}", exc_info=True)
            return False

    def run_all(self, start_phase: int = 0, end_phase: int = 6) -> bool:
        """
        Run all phases sequentially.

        Args:
            start_phase: First phase to run (default: 0)
            end_phase: Last phase to run (default: 6)

        Returns:
            True if all phases completed successfully
        """
        self.logger.info(f"Starting pipeline execution: Phases {start_phase} to {end_phase}")
        pipeline_start = datetime.now()

        for phase_num in range(start_phase, end_phase + 1):
            success = self.run_phase(phase_num)

            if not success:
                self.logger.error(f"Pipeline halted at Phase {phase_num}")
                self._generate_final_report(success=False, completed_phase=phase_num)
                return False

        # All phases completed
        elapsed = (datetime.now() - pipeline_start).total_seconds()
        self.logger.info(f"{'='*60}")
        self.logger.info(f"ALL PHASES COMPLETED SUCCESSFULLY in {elapsed/60:.1f} minutes")
        self.logger.info(f"{'='*60}")

        self._generate_final_report(success=True, completed_phase=6)
        return True

    def _generate_final_report(self, success: bool, completed_phase: int):
        """Generate final pipeline execution report."""
        report_path = Path(self.config['paths']['logs']) / f"pipeline_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

        with open(report_path, 'w') as f:
            f.write("AI CODING PIPELINE EXECUTION REPORT\n")
            f.write("=" * 60 + "\n\n")
            f.write(f"Status: {'SUCCESS' if success else 'FAILED'}\n")
            f.write(f"Completed through Phase: {completed_phase}\n")
            f.write(f"Timestamp: {datetime.now().isoformat()}\n\n")

            f.write("COST SUMMARY\n")
            f.write("-" * 60 + "\n")
            cost_summary = self.cost_tracker.get_summary()
            for model, costs in cost_summary.items():
                f.write(f"{model}:\n")
                f.write(f"  Input tokens: {costs['input_tokens']:,}\n")
                f.write(f"  Output tokens: {costs['output_tokens']:,}\n")
                f.write(f"  Total cost: ${costs['total_cost']:.2f}\n\n")

            total_cost = sum(c['total_cost'] for c in cost_summary.values())
            f.write(f"TOTAL PIPELINE COST: ${total_cost:.2f}\n\n")

            f.write(f"\nFull report saved to: {report_path}\n")

        self.logger.info(f"Pipeline report generated: {report_path}")
        self.logger.info(f"Total cost: ${total_cost:.2f}")


def main():
    """Main entry point with command-line argument parsing."""
    parser = argparse.ArgumentParser(
        description="AI Coding Pipeline for MASEM Data Extraction",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Run entire pipeline
  python run_pipeline.py

  # Run only phase 1
  python run_pipeline.py --phase 1

  # Run phases 2-4
  python run_pipeline.py --start 2 --end 4

  # Use custom config
  python run_pipeline.py --config /path/to/config.yaml
        """
    )

    parser.add_argument(
        '--config',
        type=str,
        default='scripts/ai_coding_pipeline/config.yaml',
        help='Path to configuration file (default: scripts/ai_coding_pipeline/config.yaml)'
    )

    parser.add_argument(
        '--phase',
        type=int,
        choices=range(7),
        help='Run only a single phase (0-6)'
    )

    parser.add_argument(
        '--start',
        type=int,
        default=0,
        choices=range(7),
        help='Start phase (default: 0)'
    )

    parser.add_argument(
        '--end',
        type=int,
        default=6,
        choices=range(7),
        help='End phase (default: 6)'
    )

    args = parser.parse_args()

    # Initialize orchestrator
    try:
        orchestrator = PipelineOrchestrator(config_path=args.config)
    except Exception as e:
        print(f"Failed to initialize pipeline: {e}", file=sys.stderr)
        return 1

    # Run requested phases
    if args.phase is not None:
        # Single phase mode
        success = orchestrator.run_phase(args.phase)
    else:
        # Range mode
        success = orchestrator.run_all(start_phase=args.start, end_phase=args.end)

    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
