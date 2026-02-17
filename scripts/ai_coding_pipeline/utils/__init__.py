"""AI Coding Pipeline Utilities for MASEM Data Extraction."""

from .llm_clients import ClaudeClient, GPT4oClient, GroqClient
from .matrix_utils import (
    long_to_matrix, check_positive_definite, nearest_pd,
    beta_to_r, validate_correlation_matrix, matrix_completeness
)
from .metrics import cohens_kappa, fleiss_kappa, icc_2_1, mae, agreement_report
from .audit import AuditLogger
from .cost_tracker import CostTracker
from .pdf_processor import PDFProcessor

__all__ = [
    # LLM Clients
    'ClaudeClient',
    'GPT4oClient',
    'GroqClient',

    # Matrix utilities
    'long_to_matrix',
    'check_positive_definite',
    'nearest_pd',
    'beta_to_r',
    'validate_correlation_matrix',
    'matrix_completeness',

    # Metrics
    'cohens_kappa',
    'fleiss_kappa',
    'icc_2_1',
    'mae',
    'agreement_report',

    # Logging and tracking
    'AuditLogger',
    'CostTracker',

    # PDF processing
    'PDFProcessor'
]
