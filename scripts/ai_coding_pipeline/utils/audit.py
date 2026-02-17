#!/usr/bin/env python3
"""
Audit logging for AI coding pipeline.
Tracks all extractions, decisions, and modifications.
"""

import json
import logging
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, Optional


logger = logging.getLogger(__name__)


class AuditLogger:
    """Comprehensive audit logging for the AI coding pipeline."""

    def __init__(self, log_dir: str):
        """
        Initialize audit logger.

        Args:
            log_dir: Directory to store audit logs
        """
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(parents=True, exist_ok=True)

        # Create timestamped audit log file
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        self.log_file = self.log_dir / f"audit_log_{timestamp}.jsonl"

        logger.info(f"Audit logger initialized: {self.log_file}")

    def _write_entry(self, entry: Dict[str, Any]):
        """
        Write an entry to the audit log.

        Args:
            entry: Audit log entry
        """
        # Add timestamp if not present
        if 'timestamp' not in entry:
            entry['timestamp'] = datetime.now().isoformat()

        # Write as JSON line
        with open(self.log_file, 'a') as f:
            f.write(json.dumps(entry) + '\n')

    def log_extraction(self, study_id: str, phase: str, field: str,
                      value: Any, confidence: str, model: str,
                      tokens: int):
        """
        Log an AI extraction.

        Args:
            study_id: Study identifier
            phase: Pipeline phase
            field: Field being extracted
            value: Extracted value
            confidence: Confidence level
            model: Model used
            tokens: Token count
        """
        entry = {
            'type': 'extraction',
            'study_id': study_id,
            'phase': phase,
            'field': field,
            'value': value,
            'confidence': confidence,
            'model': model,
            'tokens': tokens
        }

        self._write_entry(entry)

    def log_consensus(self, study_id: str, field: str, ai_value: Any,
                     human_value: Any, resolution: Any, reason: str):
        """
        Log a consensus resolution.

        Args:
            study_id: Study identifier
            field: Field being resolved
            ai_value: AI-extracted value
            human_value: Human-coded value
            resolution: Final resolved value
            reason: Resolution reason
        """
        entry = {
            'type': 'consensus',
            'study_id': study_id,
            'field': field,
            'ai_value': ai_value,
            'human_value': human_value,
            'resolution': resolution,
            'reason': reason
        }

        self._write_entry(entry)

    def log_event(self, phase: str, event_type: str, details: Dict[str, Any]):
        """
        Log a general pipeline event.

        Args:
            phase: Pipeline phase
            event_type: Type of event
            details: Event details
        """
        entry = {
            'type': 'event',
            'phase': phase,
            'event_type': event_type,
            'details': details
        }

        self._write_entry(entry)

    def log_error(self, phase: str, error_type: str, error_message: str,
                 context: Optional[Dict[str, Any]] = None):
        """
        Log an error.

        Args:
            phase: Pipeline phase
            error_type: Type of error
            error_message: Error message
            context: Additional context
        """
        entry = {
            'type': 'error',
            'phase': phase,
            'error_type': error_type,
            'error_message': error_message,
            'context': context or {}
        }

        self._write_entry(entry)

    def log_quality_check(self, gate_name: str, passed: bool,
                         details: Dict[str, Any]):
        """
        Log a quality gate check.

        Args:
            gate_name: Name of quality gate
            passed: Whether the check passed
            details: Check details
        """
        entry = {
            'type': 'quality_check',
            'gate_name': gate_name,
            'passed': passed,
            'details': details
        }

        self._write_entry(entry)

    def get_summary(self) -> Dict[str, Any]:
        """
        Generate summary statistics from audit log.

        Returns:
            Summary dictionary
        """
        if not self.log_file.exists():
            return {'error': 'No audit log file found'}

        # Read all entries
        entries = []
        with open(self.log_file, 'r') as f:
            for line in f:
                entries.append(json.loads(line))

        # Count by type
        type_counts = {}
        for entry in entries:
            entry_type = entry.get('type', 'unknown')
            type_counts[entry_type] = type_counts.get(entry_type, 0) + 1

        # Phase statistics
        phase_counts = {}
        for entry in entries:
            phase = entry.get('phase')
            if phase:
                phase_counts[phase] = phase_counts.get(phase, 0) + 1

        # Model usage
        model_usage = {}
        for entry in entries:
            if entry.get('type') == 'extraction':
                model = entry.get('model')
                if model:
                    model_usage[model] = model_usage.get(model, 0) + 1

        # Error summary
        errors = [e for e in entries if e.get('type') == 'error']

        summary = {
            'total_entries': len(entries),
            'type_counts': type_counts,
            'phase_counts': phase_counts,
            'model_usage': model_usage,
            'n_errors': len(errors),
            'errors': errors if len(errors) <= 10 else errors[:10]  # First 10 errors
        }

        return summary

    def export_summary(self, output_path: Optional[Path] = None):
        """
        Export audit log summary to JSON.

        Args:
            output_path: Path to save summary (default: log_dir/audit_summary.json)
        """
        summary = self.get_summary()

        if output_path is None:
            output_path = self.log_dir / 'audit_summary.json'

        with open(output_path, 'w') as f:
            json.dump(summary, indent=2, fp=f)

        logger.info(f"Audit summary exported to: {output_path}")

    def query_extractions(self, study_id: Optional[str] = None,
                         phase: Optional[str] = None,
                         field: Optional[str] = None) -> list:
        """
        Query extraction entries from audit log.

        Args:
            study_id: Filter by study ID
            phase: Filter by phase
            field: Filter by field

        Returns:
            List of matching extraction entries
        """
        if not self.log_file.exists():
            return []

        matches = []

        with open(self.log_file, 'r') as f:
            for line in f:
                entry = json.loads(line)

                if entry.get('type') != 'extraction':
                    continue

                # Apply filters
                if study_id and entry.get('study_id') != study_id:
                    continue

                if phase and entry.get('phase') != phase:
                    continue

                if field and entry.get('field') != field:
                    continue

                matches.append(entry)

        return matches

    def get_study_timeline(self, study_id: str) -> list:
        """
        Get chronological timeline of all events for a study.

        Args:
            study_id: Study identifier

        Returns:
            List of events in chronological order
        """
        if not self.log_file.exists():
            return []

        timeline = []

        with open(self.log_file, 'r') as f:
            for line in f:
                entry = json.loads(line)

                if entry.get('study_id') == study_id:
                    timeline.append(entry)

        # Sort by timestamp
        timeline.sort(key=lambda x: x.get('timestamp', ''))

        return timeline


def test_audit_logger():
    """Test audit logger functionality."""
    import tempfile
    import shutil

    # Create temp directory
    temp_dir = tempfile.mkdtemp()

    try:
        print(f"Testing audit logger in: {temp_dir}\n")

        # Initialize logger
        logger = AuditLogger(temp_dir)

        # Test extraction logging
        print("1. Logging extractions...")
        logger.log_extraction(
            study_id='study_001',
            phase='phase1',
            field='correlation_PE_BI',
            value=0.65,
            confidence='high',
            model='claude-sonnet-4-5',
            tokens=1500
        )

        logger.log_extraction(
            study_id='study_001',
            phase='phase2',
            field='construct_mapping',
            value={'PE': 'Performance Expectancy'},
            confidence='exact',
            model='claude-sonnet-4-5',
            tokens=800
        )

        # Test consensus logging
        print("2. Logging consensus...")
        logger.log_consensus(
            study_id='study_001',
            field='sample_size',
            ai_value=150,
            human_value=152,
            resolution=152,
            reason='human_override'
        )

        # Test event logging
        print("3. Logging event...")
        logger.log_event(
            phase='phase3',
            event_type='three_model_consensus',
            details={'agreement_rate': 0.95}
        )

        # Test error logging
        print("4. Logging error...")
        logger.log_error(
            phase='phase1',
            error_type='extraction_failed',
            error_message='Failed to parse PDF',
            context={'study_id': 'study_002'}
        )

        # Test quality check logging
        print("5. Logging quality check...")
        logger.log_quality_check(
            gate_name='Gate 1: Positive Definite',
            passed=True,
            details={'n_studies_checked': 10}
        )

        # Test summary
        print("\n6. Generating summary...")
        summary = logger.get_summary()
        print(f"   Total entries: {summary['total_entries']}")
        print(f"   Type counts: {summary['type_counts']}")

        # Test querying
        print("\n7. Querying extractions...")
        extractions = logger.query_extractions(study_id='study_001')
        print(f"   Found {len(extractions)} extractions for study_001")

        # Test timeline
        print("\n8. Getting study timeline...")
        timeline = logger.get_study_timeline('study_001')
        print(f"   Timeline has {len(timeline)} events")

        # Export summary
        print("\n9. Exporting summary...")
        logger.export_summary()
        print(f"   Summary exported successfully")

        print("\nAll tests passed!")

    finally:
        # Cleanup
        shutil.rmtree(temp_dir)


if __name__ == "__main__":
    test_audit_logger()
