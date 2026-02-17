#!/usr/bin/env python3
"""
Phase 1: Extract Correlations
Use Claude Sonnet with RAG to extract correlation matrices from study PDFs.
"""

import logging
from pathlib import Path
from typing import Dict, Any, List, Optional
import json
from datetime import datetime

from phase0_rag_index import RAGIndexBuilder
from utils.llm_clients import ClaudeClient
from utils.pdf_processor import PDFProcessor

logger = logging.getLogger(__name__)


class CorrelationExtractor:
    """Extracts correlation matrices from research papers using Claude + RAG."""

    def __init__(self, config: Dict[str, Any], cost_tracker, audit_logger):
        self.config = config
        self.cost_tracker = cost_tracker
        self.audit_logger = audit_logger

        # Initialize RAG
        self.rag = RAGIndexBuilder(config)

        # Initialize Claude client
        self.claude = ClaudeClient(
            model=config['models']['claude']['model'],
            cost_tracker=cost_tracker
        )

        self.pdf_processor = PDFProcessor()

        # Load extraction prompt
        prompt_path = Path(config['paths']['prompts']) / 'correlation_extraction.txt'
        with open(prompt_path, 'r') as f:
            self.extraction_prompt = f.read()

    def query_relevant_chunks(self, study_id: str, n_chunks: int = 5) -> List[str]:
        """
        Query RAG index for correlation-relevant chunks.

        Args:
            study_id: Study identifier (PDF filename without extension)
            n_chunks: Number of chunks to retrieve

        Returns:
            List of relevant text chunks
        """
        # Query for correlation-related content
        queries = [
            f"{study_id} correlation matrix table",
            f"{study_id} pearson correlations results",
            f"{study_id} descriptive statistics correlations"
        ]

        all_chunks = []
        for query in queries:
            chunks = self.rag.query(query, n_results=n_chunks)
            all_chunks.extend(chunks)

        # Deduplicate by chunk ID
        unique_chunks = {chunk['id']: chunk for chunk in all_chunks}

        # Return just the text, sorted by relevance (distance)
        sorted_chunks = sorted(
            unique_chunks.values(),
            key=lambda x: x.get('distance', float('inf'))
        )

        return [chunk['text'] for chunk in sorted_chunks[:n_chunks * 2]]

    def extract_from_study(self, pdf_path: Path) -> Dict[str, Any]:
        """
        Extract correlations from a single study.

        Args:
            pdf_path: Path to study PDF

        Returns:
            Extraction result with metadata and correlations
        """
        study_id = pdf_path.stem
        logger.info(f"Extracting correlations from: {study_id}")

        # Get relevant chunks from RAG
        relevant_chunks = self.query_relevant_chunks(study_id)

        if not relevant_chunks:
            logger.warning(f"No relevant chunks found for {study_id}")
            return {
                'study_id': study_id,
                'status': 'no_chunks',
                'correlations': []
            }

        # Build context from chunks
        context = "\n\n---CHUNK BREAK---\n\n".join(relevant_chunks)

        # Prepare prompt
        user_prompt = f"""Study ID: {study_id}

RELEVANT EXCERPTS FROM THE PAPER:
{context}

Please extract all correlation coefficients between measured constructs following the instructions provided."""

        # Call Claude
        start_time = datetime.now()
        response = self.claude.send_prompt(
            system=self.extraction_prompt,
            user=user_prompt,
            temperature=0.0,
            max_tokens=4096
        )
        extraction_time = (datetime.now() - start_time).total_seconds()

        # Parse response (expecting JSON)
        try:
            extracted_data = json.loads(response['content'])
        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse JSON response for {study_id}: {e}")
            # Attempt to extract JSON from markdown code block
            if '```json' in response['content']:
                json_start = response['content'].find('```json') + 7
                json_end = response['content'].find('```', json_start)
                try:
                    extracted_data = json.loads(response['content'][json_start:json_end])
                except:
                    extracted_data = {'correlations': [], 'parse_error': True}
            else:
                extracted_data = {'correlations': [], 'parse_error': True}

        # Add metadata
        result = {
            'study_id': study_id,
            'source_file': pdf_path.name,
            'extraction_timestamp': datetime.now().isoformat(),
            'extraction_time_seconds': extraction_time,
            'model': self.config['models']['claude']['model'],
            'n_chunks_used': len(relevant_chunks),
            'tokens_input': response.get('input_tokens', 0),
            'tokens_output': response.get('output_tokens', 0),
            'status': 'success' if not extracted_data.get('parse_error') else 'parse_error',
            **extracted_data
        }

        # Log to audit
        self.audit_logger.log_extraction(
            study_id=study_id,
            phase='phase1',
            field='correlations',
            value=extracted_data.get('correlations', []),
            confidence=extracted_data.get('confidence', 'unknown'),
            model=self.config['models']['claude']['model'],
            tokens=response.get('input_tokens', 0) + response.get('output_tokens', 0)
        )

        return result

    def extract_all(self, pdf_dir: Path, output_dir: Path) -> Dict[str, Any]:
        """
        Extract correlations from all PDFs.

        Args:
            pdf_dir: Directory containing PDF files
            output_dir: Directory to save extraction results

        Returns:
            Summary statistics
        """
        pdf_files = list(pdf_dir.glob("*.pdf"))
        logger.info(f"Processing {len(pdf_files)} PDF files")

        output_dir.mkdir(parents=True, exist_ok=True)

        results = []
        successful = 0
        failed = 0

        for pdf_path in pdf_files:
            try:
                result = self.extract_from_study(pdf_path)

                # Save individual result
                output_path = output_dir / f"{pdf_path.stem}_extracted.json"
                with open(output_path, 'w') as f:
                    json.dump(result, indent=2, fp=f)

                results.append(result)

                if result['status'] == 'success':
                    successful += 1
                else:
                    failed += 1

            except Exception as e:
                logger.error(f"Failed to process {pdf_path.name}: {e}", exc_info=True)
                failed += 1
                results.append({
                    'study_id': pdf_path.stem,
                    'status': 'error',
                    'error': str(e)
                })

        # Calculate summary statistics
        total_correlations = sum(
            len(r.get('correlations', [])) for r in results
            if r['status'] == 'success'
        )

        summary = {
            'n_studies_processed': len(pdf_files),
            'n_successful': successful,
            'n_failed': failed,
            'total_correlations_extracted': total_correlations,
            'avg_correlations_per_study': round(total_correlations / successful, 2) if successful > 0 else 0
        }

        # Save summary
        summary_path = output_dir / 'extraction_summary.json'
        with open(summary_path, 'w') as f:
            json.dump(summary, indent=2, fp=f)

        # Save all results
        all_results_path = output_dir / 'all_extractions.json'
        with open(all_results_path, 'w') as f:
            json.dump(results, indent=2, fp=f)

        return summary


def extract_correlations(config: Dict[str, Any], cost_tracker, audit_logger) -> Dict[str, Any]:
    """
    Phase 1 entry point: Extract correlations from all studies.

    Args:
        config: Pipeline configuration
        cost_tracker: Cost tracking instance
        audit_logger: Audit logging instance

    Returns:
        Result dictionary with success status and statistics
    """
    logger.info("Starting Phase 1: Correlation Extraction")

    try:
        extractor = CorrelationExtractor(config, cost_tracker, audit_logger)

        pdf_dir = Path(config['paths']['pdfs'])
        output_dir = Path(config['paths']['extracted'])

        summary = extractor.extract_all(pdf_dir, output_dir)

        logger.info(f"Phase 1 complete: {summary}")

        return {
            'success': True,
            'summary': summary,
            'output_path': str(output_dir)
        }

    except Exception as e:
        logger.error(f"Phase 1 failed: {e}", exc_info=True)
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

    result = extract_correlations(
        config,
        CostTracker(),
        AuditLogger(config['paths']['logs'])
    )

    print(json.dumps(result, indent=2))
