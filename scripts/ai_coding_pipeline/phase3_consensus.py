#!/usr/bin/env python3
"""
Phase 3: Three-Model Consensus
Run Claude, GPT-4o, and Groq independently and synthesize consensus.
"""

import logging
from pathlib import Path
from typing import Dict, Any, List
import json
from datetime import datetime
from collections import Counter

from utils.llm_clients import ClaudeClient, GPT4oClient, GroqClient
from utils.metrics import fleiss_kappa

logger = logging.getLogger(__name__)


class ConsensusBuilder:
    """Builds consensus across three LLM models for extracted data."""

    def __init__(self, config: Dict[str, Any], cost_tracker, audit_logger):
        self.config = config
        self.cost_tracker = cost_tracker
        self.audit_logger = audit_logger

        # Initialize all three models
        self.claude = ClaudeClient(
            model=config['models']['claude']['model'],
            cost_tracker=cost_tracker
        )

        self.gpt4o = GPT4oClient(
            model=config['models']['gpt4o']['model'],
            cost_tracker=cost_tracker
        )

        self.groq = GroqClient(
            model=config['models']['groq']['model'],
            cost_tracker=cost_tracker
        )

        self.models = {
            'claude': self.claude,
            'gpt4o': self.gpt4o,
            'groq': self.groq
        }

    def extract_with_model(self, model_name: str, study_data: Dict[str, Any],
                          prompt_template: str) -> Dict[str, Any]:
        """
        Extract data using a specific model.

        Args:
            model_name: Name of model to use
            study_data: Study data to extract from
            prompt_template: Prompt template to use

        Returns:
            Extraction result from the model
        """
        model = self.models[model_name]

        # Prepare prompt with study context
        user_prompt = f"""Study ID: {study_data['study_id']}

Original Extraction Data:
{json.dumps(study_data.get('original_data', {}), indent=2)}

Mapped Correlations:
{json.dumps(study_data.get('standardized_correlations', []), indent=2)}

Please verify and validate this extracted data. Respond with a JSON object containing:
{{
  "verified_correlations": [list of verified correlation objects],
  "sample_size": integer,
  "study_year": integer,
  "ai_type": "string",
  "region": "string",
  "confidence": "high|moderate|low",
  "concerns": [list of any concerns or issues noted]
}}"""

        response = model.send_prompt(
            system=prompt_template,
            user=user_prompt,
            temperature=0.0,
            max_tokens=4096
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
                result = {'error': 'Failed to parse', 'raw_response': response['content']}

        result['model'] = model_name
        result['tokens_used'] = response.get('input_tokens', 0) + response.get('output_tokens', 0)

        return result

    def build_consensus(self, study_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Build consensus across three models for a single study.

        Args:
            study_data: Mapped study data from Phase 2

        Returns:
            Consensus result with agreement statistics
        """
        study_id = study_data['study_id']
        logger.info(f"Building consensus for study: {study_id}")

        # Load verification prompt
        prompt_path = Path(self.config['paths']['prompts']) / 'correlation_extraction.txt'
        with open(prompt_path, 'r') as f:
            prompt_template = f.read()

        # Extract with all three models
        model_results = {}
        for model_name in ['claude', 'gpt4o', 'groq']:
            try:
                result = self.extract_with_model(model_name, study_data, prompt_template)
                model_results[model_name] = result

                # Log to audit
                self.audit_logger.log_extraction(
                    study_id=study_id,
                    phase='phase3',
                    field='consensus_extraction',
                    value=result.get('verified_correlations', []),
                    confidence=result.get('confidence', 'unknown'),
                    model=model_name,
                    tokens=result.get('tokens_used', 0)
                )

            except Exception as e:
                logger.error(f"Model {model_name} failed for {study_id}: {e}")
                model_results[model_name] = {'error': str(e)}

        # Analyze agreement
        agreement_analysis = self._analyze_agreement(model_results, study_data)

        # Build consensus values
        consensus_correlations = self._synthesize_correlations(model_results, agreement_analysis)

        result = {
            'study_id': study_id,
            'consensus_timestamp': datetime.now().isoformat(),
            'model_results': model_results,
            'agreement_analysis': agreement_analysis,
            'consensus_correlations': consensus_correlations,
            'original_mapped_data': study_data
        }

        return result

    def _analyze_agreement(self, model_results: Dict[str, Any],
                          study_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze agreement between models on key fields.

        Args:
            model_results: Results from all three models
            study_data: Original study data

        Returns:
            Agreement analysis
        """
        # Extract correlation pairs from each model
        model_pairs = {}
        for model_name, result in model_results.items():
            if 'error' in result:
                continue

            pairs = set()
            for corr in result.get('verified_correlations', []):
                c1 = corr.get('construct_1', '')
                c2 = corr.get('construct_2', '')
                if c1 and c2:
                    pairs.add(tuple(sorted([c1, c2])))

            model_pairs[model_name] = pairs

        # Calculate pairwise agreement
        if len(model_pairs) >= 2:
            all_pairs = set()
            for pairs in model_pairs.values():
                all_pairs.update(pairs)

            # Count agreements
            pair_agreements = {}
            for pair in all_pairs:
                count = sum(1 for pairs in model_pairs.values() if pair in pairs)
                pair_agreements[pair] = count

            # Agreement rates
            three_agree = sum(1 for c in pair_agreements.values() if c == 3)
            two_agree = sum(1 for c in pair_agreements.values() if c == 2)
            one_only = sum(1 for c in pair_agreements.values() if c == 1)

            agreement_analysis = {
                'n_models_completed': len(model_pairs),
                'total_unique_pairs': len(all_pairs),
                'three_way_agreement': three_agree,
                'two_way_agreement': two_agree,
                'one_model_only': one_only,
                'agreement_rate': round(three_agree / len(all_pairs), 3) if all_pairs else 0,
                'pair_agreements': {f"{p[0]}-{p[1]}": c for p, c in pair_agreements.items()}
            }

        else:
            agreement_analysis = {
                'n_models_completed': len(model_pairs),
                'error': 'Insufficient models completed successfully'
            }

        # Check categorical field agreement
        sample_sizes = [r.get('sample_size') for r in model_results.values() if 'sample_size' in r]
        study_years = [r.get('study_year') for r in model_results.values() if 'study_year' in r]
        ai_types = [r.get('ai_type') for r in model_results.values() if 'ai_type' in r]
        regions = [r.get('region') for r in model_results.values() if 'region' in r]

        agreement_analysis['field_agreement'] = {
            'sample_size': {
                'values': sample_sizes,
                'mode': Counter(sample_sizes).most_common(1)[0] if sample_sizes else None,
                'agreement': len(set(sample_sizes)) == 1 if sample_sizes else False
            },
            'study_year': {
                'values': study_years,
                'mode': Counter(study_years).most_common(1)[0] if study_years else None,
                'agreement': len(set(study_years)) == 1 if study_years else False
            },
            'ai_type': {
                'values': ai_types,
                'mode': Counter(ai_types).most_common(1)[0] if ai_types else None,
                'agreement': len(set(ai_types)) == 1 if ai_types else False
            },
            'region': {
                'values': regions,
                'mode': Counter(regions).most_common(1)[0] if regions else None,
                'agreement': len(set(regions)) == 1 if regions else False
            }
        }

        return agreement_analysis

    def _synthesize_correlations(self, model_results: Dict[str, Any],
                                 agreement_analysis: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Synthesize consensus correlations from model results.

        Args:
            model_results: Results from all models
            agreement_analysis: Agreement analysis

        Returns:
            List of consensus correlations
        """
        # Collect all correlations by construct pair
        pair_correlations = {}

        for model_name, result in model_results.items():
            if 'error' in result:
                continue

            for corr in result.get('verified_correlations', []):
                c1 = corr.get('construct_1', '')
                c2 = corr.get('construct_2', '')
                r_value = corr.get('r')

                if not c1 or not c2 or r_value is None:
                    continue

                pair = tuple(sorted([c1, c2]))

                if pair not in pair_correlations:
                    pair_correlations[pair] = []

                pair_correlations[pair].append({
                    'model': model_name,
                    'r': r_value,
                    'n': corr.get('n')
                })

        # Build consensus for each pair
        consensus_correlations = []

        for pair, values in pair_correlations.items():
            n_models_agree = len(values)
            r_values = [v['r'] for v in values]
            r_consensus = sum(r_values) / len(r_values)  # Average

            # Determine consensus quality
            if n_models_agree == 3:
                consensus_quality = '3/3_agree'
                flag = None
            elif n_models_agree == 2:
                consensus_quality = '2/3_agree'
                flag = 'majority_consensus'
            else:
                consensus_quality = '1/3_only'
                flag = 'human_review_needed'

            consensus_correlations.append({
                'construct_1': pair[0],
                'construct_2': pair[1],
                'r_consensus': round(r_consensus, 3),
                'r_values': r_values,
                'r_std': round(float(sum((r - r_consensus)**2 for r in r_values) / len(r_values))**0.5, 4) if len(r_values) > 1 else 0,
                'n_models_agree': n_models_agree,
                'consensus_quality': consensus_quality,
                'flag': flag,
                'model_details': values
            })

        return consensus_correlations

    def process_all_studies(self, input_dir: Path, output_dir: Path) -> Dict[str, Any]:
        """
        Build consensus for all mapped studies.

        Args:
            input_dir: Directory with Phase 2 mapped results
            output_dir: Directory to save consensus results

        Returns:
            Summary statistics
        """
        mapped_files = list(input_dir.glob("*_mapped.json"))
        logger.info(f"Processing {len(mapped_files)} mapped studies")

        output_dir.mkdir(parents=True, exist_ok=True)

        results = []
        total_three_agree = 0
        total_two_agree = 0
        total_one_only = 0

        for file_path in mapped_files:
            try:
                with open(file_path, 'r') as f:
                    study_data = json.load(f)

                consensus_result = self.build_consensus(study_data)

                # Save result
                output_path = output_dir / f"{study_data['study_id']}_consensus.json"
                with open(output_path, 'w') as f:
                    json.dump(consensus_result, indent=2, fp=f)

                results.append(consensus_result)

                # Aggregate statistics
                agreement = consensus_result.get('agreement_analysis', {})
                total_three_agree += agreement.get('three_way_agreement', 0)
                total_two_agree += agreement.get('two_way_agreement', 0)
                total_one_only += agreement.get('one_model_only', 0)

            except Exception as e:
                logger.error(f"Failed to process {file_path.name}: {e}", exc_info=True)

        # Summary statistics
        total_pairs = total_three_agree + total_two_agree + total_one_only

        summary = {
            'n_studies_processed': len(results),
            'total_correlation_pairs': total_pairs,
            'three_way_agreement': total_three_agree,
            'two_way_agreement': total_two_agree,
            'one_model_only': total_one_only,
            'agreement_rate': round(total_three_agree / total_pairs, 3) if total_pairs > 0 else 0
        }

        # Save summary
        summary_path = output_dir / 'consensus_summary.json'
        with open(summary_path, 'w') as f:
            json.dump(summary, indent=2, fp=f)

        # Save all results
        all_results_path = output_dir / 'all_consensus_results.json'
        with open(all_results_path, 'w') as f:
            json.dump(results, indent=2, fp=f)

        return summary


def run_consensus(config: Dict[str, Any], cost_tracker, audit_logger) -> Dict[str, Any]:
    """
    Phase 3 entry point: Build three-model consensus.

    Args:
        config: Pipeline configuration
        cost_tracker: Cost tracking instance
        audit_logger: Audit logging instance

    Returns:
        Result dictionary with success status and statistics
    """
    logger.info("Starting Phase 3: Three-Model Consensus")

    try:
        consensus_builder = ConsensusBuilder(config, cost_tracker, audit_logger)

        input_dir = Path(config['paths']['extracted']) / 'mapped'
        output_dir = Path(config['paths']['verified'])

        summary = consensus_builder.process_all_studies(input_dir, output_dir)

        logger.info(f"Phase 3 complete: {summary}")

        return {
            'success': True,
            'summary': summary,
            'output_path': str(output_dir)
        }

    except Exception as e:
        logger.error(f"Phase 3 failed: {e}", exc_info=True)
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

    result = run_consensus(
        config,
        CostTracker(),
        AuditLogger(config['paths']['logs'])
    )

    print(json.dumps(result, indent=2))
