#!/usr/bin/env python3
"""
Phase 2: Construct Mapping
Map extracted construct names to the 12 standard constructs.
"""

import logging
from pathlib import Path
from typing import Dict, Any, List, Set
import json
from datetime import datetime

from utils.llm_clients import ClaudeClient

logger = logging.getLogger(__name__)


class ConstructMapper:
    """Maps author-reported construct names to standard MASEM constructs."""

    def __init__(self, config: Dict[str, Any], cost_tracker, audit_logger):
        self.config = config
        self.cost_tracker = cost_tracker
        self.audit_logger = audit_logger

        # Standard constructs
        self.standard_constructs = config['constructs']['names']
        self.construct_full_names = config['constructs']['full_names']

        # Initialize Claude client
        self.claude = ClaudeClient(
            model=config['models']['claude']['model'],
            cost_tracker=cost_tracker
        )

        # Load mapping prompt
        prompt_path = Path(config['paths']['prompts']) / 'construct_identification.txt'
        with open(prompt_path, 'r') as f:
            self.mapping_prompt = f.read()

        # Valid construct pairs (all 66 combinations)
        self.valid_pairs = self._generate_valid_pairs()

    def _generate_valid_pairs(self) -> Set[tuple]:
        """Generate all valid construct pairs (n=66 for 12 constructs)."""
        valid_pairs = set()
        constructs = self.standard_constructs

        for i, c1 in enumerate(constructs):
            for c2 in constructs[i+1:]:
                valid_pairs.add(tuple(sorted([c1, c2])))

        logger.info(f"Generated {len(valid_pairs)} valid construct pairs")
        return valid_pairs

    def map_construct(self, construct_name: str, study_context: str = "") -> Dict[str, Any]:
        """
        Map a single construct name to standard construct.

        Args:
            construct_name: Author's construct name
            study_context: Additional context about the construct

        Returns:
            Mapping result with confidence and rationale
        """
        user_prompt = f"""Author's construct name: "{construct_name}"

Study context: {study_context if study_context else "Not provided"}

Map this construct to ONE of the 12 standard constructs listed in your instructions. Provide your response as JSON with the following structure:

{{
  "original_name": "{construct_name}",
  "mapped_construct": "ABBREVIATION",
  "confidence": "exact|high|moderate|low",
  "rationale": "Brief explanation of the mapping decision"
}}"""

        response = self.claude.send_prompt(
            system=self.mapping_prompt,
            user=user_prompt,
            temperature=0.0,
            max_tokens=512
        )

        # Parse response
        try:
            mapping = json.loads(response['content'])
        except json.JSONDecodeError:
            # Try to extract from markdown
            if '```json' in response['content']:
                json_start = response['content'].find('```json') + 7
                json_end = response['content'].find('```', json_start)
                mapping = json.loads(response['content'][json_start:json_end])
            else:
                mapping = {
                    'original_name': construct_name,
                    'mapped_construct': 'UNKNOWN',
                    'confidence': 'low',
                    'rationale': 'Failed to parse response'
                }

        # Validate mapped construct
        if mapping['mapped_construct'] not in self.standard_constructs:
            logger.warning(f"Invalid mapping: {construct_name} -> {mapping['mapped_construct']}")
            mapping['confidence'] = 'low'
            mapping['validation_warning'] = 'Mapped construct not in standard set'

        # Add metadata
        mapping['tokens_used'] = response.get('input_tokens', 0) + response.get('output_tokens', 0)

        return mapping

    def map_study_correlations(self, study_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Map all constructs in a study's correlation data.

        Args:
            study_data: Extracted correlation data from Phase 1

        Returns:
            Study data with standardized construct names
        """
        study_id = study_data['study_id']
        logger.info(f"Mapping constructs for study: {study_id}")

        # Extract unique construct names from correlations
        construct_names = set()
        for corr in study_data.get('correlations', []):
            construct_names.add(corr.get('construct_1', ''))
            construct_names.add(corr.get('construct_2', ''))

        construct_names.discard('')  # Remove empty strings

        # Map each construct
        mappings = {}
        for construct_name in construct_names:
            mapping = self.map_construct(
                construct_name,
                study_context=study_data.get('study_description', '')
            )
            mappings[construct_name] = mapping

            # Log to audit
            self.audit_logger.log_extraction(
                study_id=study_id,
                phase='phase2',
                field=f'construct_mapping_{construct_name}',
                value=mapping['mapped_construct'],
                confidence=mapping['confidence'],
                model=self.config['models']['claude']['model'],
                tokens=mapping['tokens_used']
            )

        # Apply mappings to correlations
        standardized_correlations = []
        invalid_pairs = []

        for corr in study_data.get('correlations', []):
            c1_original = corr.get('construct_1', '')
            c2_original = corr.get('construct_2', '')

            if not c1_original or not c2_original:
                continue

            c1_mapped = mappings[c1_original]['mapped_construct']
            c2_mapped = mappings[c2_original]['mapped_construct']

            # Check if this is a valid pair
            pair = tuple(sorted([c1_mapped, c2_mapped]))

            if pair in self.valid_pairs:
                standardized_correlations.append({
                    'construct_1': c1_mapped,
                    'construct_2': c2_mapped,
                    'r': corr.get('r'),
                    'n': corr.get('n', study_data.get('sample_size')),
                    'original_construct_1': c1_original,
                    'original_construct_2': c2_original,
                    'mapping_confidence_1': mappings[c1_original]['confidence'],
                    'mapping_confidence_2': mappings[c2_original]['confidence'],
                    'source': corr.get('source', 'unknown'),
                    'page': corr.get('page')
                })
            else:
                invalid_pairs.append({
                    'construct_1': c1_mapped,
                    'construct_2': c2_mapped,
                    'reason': 'Not in valid 66 pairs'
                })

        # Prepare result
        result = {
            'study_id': study_id,
            'mapping_timestamp': datetime.now().isoformat(),
            'n_original_constructs': len(construct_names),
            'n_standardized_correlations': len(standardized_correlations),
            'n_invalid_pairs': len(invalid_pairs),
            'construct_mappings': mappings,
            'standardized_correlations': standardized_correlations,
            'invalid_pairs': invalid_pairs,
            'original_data': study_data
        }

        return result

    def map_all_studies(self, input_dir: Path, output_dir: Path) -> Dict[str, Any]:
        """
        Map constructs for all extracted studies.

        Args:
            input_dir: Directory with Phase 1 extraction results
            output_dir: Directory to save mapped results

        Returns:
            Summary statistics
        """
        extraction_files = list(input_dir.glob("*_extracted.json"))
        logger.info(f"Processing {len(extraction_files)} extraction files")

        output_dir.mkdir(parents=True, exist_ok=True)

        results = []
        total_correlations = 0
        total_invalid = 0

        for file_path in extraction_files:
            try:
                with open(file_path, 'r') as f:
                    study_data = json.load(f)

                if study_data.get('status') != 'success':
                    logger.info(f"Skipping {file_path.name} (status: {study_data.get('status')})")
                    continue

                mapped_result = self.map_study_correlations(study_data)

                # Save result
                output_path = output_dir / f"{study_data['study_id']}_mapped.json"
                with open(output_path, 'w') as f:
                    json.dump(mapped_result, indent=2, fp=f)

                results.append(mapped_result)
                total_correlations += mapped_result['n_standardized_correlations']
                total_invalid += mapped_result['n_invalid_pairs']

            except Exception as e:
                logger.error(f"Failed to process {file_path.name}: {e}", exc_info=True)

        # Summary statistics
        summary = {
            'n_studies_processed': len(results),
            'total_standardized_correlations': total_correlations,
            'total_invalid_pairs': total_invalid,
            'avg_correlations_per_study': round(total_correlations / len(results), 2) if results else 0
        }

        # Save summary
        summary_path = output_dir / 'mapping_summary.json'
        with open(summary_path, 'w') as f:
            json.dump(summary, indent=2, fp=f)

        # Save combined results
        combined_path = output_dir / 'all_mapped_studies.json'
        with open(combined_path, 'w') as f:
            json.dump(results, indent=2, fp=f)

        return summary


def map_constructs(config: Dict[str, Any], cost_tracker, audit_logger) -> Dict[str, Any]:
    """
    Phase 2 entry point: Map constructs to standard names.

    Args:
        config: Pipeline configuration
        cost_tracker: Cost tracking instance
        audit_logger: Audit logging instance

    Returns:
        Result dictionary with success status and statistics
    """
    logger.info("Starting Phase 2: Construct Mapping")

    try:
        mapper = ConstructMapper(config, cost_tracker, audit_logger)

        input_dir = Path(config['paths']['extracted'])
        output_dir = Path(config['paths']['extracted']) / 'mapped'

        summary = mapper.map_all_studies(input_dir, output_dir)

        logger.info(f"Phase 2 complete: {summary}")

        return {
            'success': True,
            'summary': summary,
            'output_path': str(output_dir)
        }

    except Exception as e:
        logger.error(f"Phase 2 failed: {e}", exc_info=True)
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

    result = map_constructs(
        config,
        CostTracker(),
        AuditLogger(config['paths']['logs'])
    )

    print(json.dumps(result, indent=2))
