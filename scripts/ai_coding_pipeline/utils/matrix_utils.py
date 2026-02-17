#!/usr/bin/env python3
"""
Matrix utility functions for correlation matrix operations.
Includes positive definiteness checks, beta-to-r conversion, and validation.
"""

import numpy as np
import pandas as pd
from typing import Dict, Any, List, Tuple, Optional
from scipy import linalg


def long_to_matrix(df: pd.DataFrame, construct_cols: Tuple[str, str] = ('construct_1', 'construct_2'),
                  value_col: str = 'r') -> np.ndarray:
    """
    Convert long-format correlation data to symmetric matrix.

    Args:
        df: DataFrame with correlation pairs
        construct_cols: Tuple of column names for construct pairs
        value_col: Column name for correlation values

    Returns:
        Symmetric correlation matrix as numpy array
    """
    # Get unique constructs
    constructs = sorted(set(df[construct_cols[0]].unique()) | set(df[construct_cols[1]].unique()))
    n = len(constructs)

    # Create construct to index mapping
    construct_idx = {c: i for i, c in enumerate(constructs)}

    # Initialize matrix with 1s on diagonal
    matrix = np.eye(n)

    # Fill in correlations
    for _, row in df.iterrows():
        c1 = row[construct_cols[0]]
        c2 = row[construct_cols[1]]
        r = row[value_col]

        if pd.notna(r):
            i = construct_idx[c1]
            j = construct_idx[c2]

            # Set both triangles (symmetric)
            matrix[i, j] = r
            matrix[j, i] = r

    return matrix


def check_positive_definite(matrix: np.ndarray, tol: float = 1e-8) -> Tuple[bool, np.ndarray]:
    """
    Check if a matrix is positive definite using eigenvalues.

    Args:
        matrix: Correlation matrix
        tol: Tolerance for considering eigenvalue as zero

    Returns:
        Tuple of (is_positive_definite, eigenvalues)
    """
    # Compute eigenvalues
    eigenvalues = linalg.eigvalsh(matrix)

    # Check if all eigenvalues are positive (within tolerance)
    is_pd = np.all(eigenvalues > -tol)

    return is_pd, eigenvalues


def nearest_pd(matrix: np.ndarray) -> np.ndarray:
    """
    Find the nearest positive definite matrix.
    Uses Higham's algorithm (1988).

    Args:
        matrix: Input matrix (potentially not positive definite)

    Returns:
        Nearest positive definite matrix
    """
    # Symmetrize
    B = (matrix + matrix.T) / 2

    # Compute eigendecomposition
    eigenvalues, eigenvectors = linalg.eigh(B)

    # Replace negative eigenvalues with small positive values
    eigenvalues[eigenvalues < 0] = 1e-10

    # Reconstruct matrix
    matrix_pd = eigenvectors @ np.diag(eigenvalues) @ eigenvectors.T

    # Force diagonal to 1 (correlation matrix)
    d = np.sqrt(np.diag(matrix_pd))
    matrix_pd = matrix_pd / d[:, None] / d[None, :]

    # Ensure exactly 1 on diagonal
    np.fill_diagonal(matrix_pd, 1.0)

    return matrix_pd


def beta_to_r(beta: float, lambda_val: float = 0.0, method: str = 'peterson_brown_2005') -> float:
    """
    Convert standardized regression coefficient (beta) to correlation (r).

    Args:
        beta: Standardized regression coefficient
        lambda_val: Lambda parameter (default 0 for simple conversion)
        method: Conversion method

    Returns:
        Approximate correlation coefficient
    """
    if method == 'peterson_brown_2005':
        # Peterson & Brown (2005): r ≈ beta + 0.05 * lambda
        # where lambda represents additional predictors' influence
        r = beta + 0.05 * lambda_val

    elif method == 'simple':
        # Simple assumption: r ≈ beta when other predictors are uncorrelated
        r = beta

    else:
        raise ValueError(f"Unknown conversion method: {method}")

    # Clip to valid correlation range
    r = np.clip(r, -1.0, 1.0)

    return r


def validate_correlation_matrix(matrix: np.ndarray, check_pd: bool = True) -> Dict[str, Any]:
    """
    Comprehensive validation of a correlation matrix.

    Args:
        matrix: Correlation matrix to validate
        check_pd: Whether to check positive definiteness

    Returns:
        Dictionary with validation results
    """
    n = matrix.shape[0]

    # Check square
    is_square = matrix.shape[0] == matrix.shape[1]

    # Check symmetric
    is_symmetric = np.allclose(matrix, matrix.T)

    # Check diagonal is 1
    diagonal_ones = np.allclose(np.diag(matrix), 1.0)

    # Check range [-1, 1]
    in_range = np.all((matrix >= -1 - 1e-8) & (matrix <= 1 + 1e-8))

    # Check positive definite
    if check_pd and is_square:
        is_pd, eigenvalues = check_positive_definite(matrix)
        min_eigenvalue = float(np.min(eigenvalues))
        max_eigenvalue = float(np.max(eigenvalues))
    else:
        is_pd = None
        eigenvalues = None
        min_eigenvalue = None
        max_eigenvalue = None

    # Overall validity
    valid = is_square and is_symmetric and diagonal_ones and in_range

    if check_pd:
        valid = valid and is_pd

    results = {
        'valid': valid,
        'is_square': is_square,
        'is_symmetric': is_symmetric,
        'diagonal_ones': diagonal_ones,
        'in_range': in_range,
        'is_positive_definite': is_pd,
        'min_eigenvalue': min_eigenvalue,
        'max_eigenvalue': max_eigenvalue,
        'dimension': n
    }

    return results


def matrix_completeness(matrix: np.ndarray) -> Dict[str, Any]:
    """
    Analyze completeness of a correlation matrix.

    Args:
        matrix: Correlation matrix

    Returns:
        Dictionary with completeness statistics
    """
    n = matrix.shape[0]

    # Total possible correlations (excluding diagonal)
    total_cells = n * (n - 1) // 2

    # Count filled cells (non-diagonal, non-zero, not close to 1)
    filled_cells = 0
    for i in range(n):
        for j in range(i + 1, n):
            # Consider filled if not exactly 0 and not exactly 1 (unless diagonal)
            if abs(matrix[i, j]) > 1e-10 and abs(matrix[i, j] - 1.0) > 1e-10:
                filled_cells += 1

    completeness = filled_cells / total_cells if total_cells > 0 else 0

    return {
        'total_possible_correlations': total_cells,
        'filled_correlations': filled_cells,
        'completeness_rate': round(completeness, 3),
        'missing_correlations': total_cells - filled_cells
    }


def fishers_z_transform(r: float) -> float:
    """
    Fisher's Z transformation of correlation coefficient.

    Args:
        r: Correlation coefficient

    Returns:
        Z-transformed value
    """
    # Clip to avoid log(0)
    r = np.clip(r, -0.9999, 0.9999)

    z = 0.5 * np.log((1 + r) / (1 - r))

    return z


def inverse_fishers_z(z: float) -> float:
    """
    Inverse Fisher's Z transformation.

    Args:
        z: Z-transformed value

    Returns:
        Correlation coefficient
    """
    r = (np.exp(2 * z) - 1) / (np.exp(2 * z) + 1)

    return r


def aggregate_correlations(correlations: List[float], sample_sizes: List[int],
                          method: str = 'fisher') -> Tuple[float, float]:
    """
    Aggregate multiple correlation estimates using Fisher's Z.

    Args:
        correlations: List of correlation coefficients
        sample_sizes: List of corresponding sample sizes
        method: Aggregation method ('fisher' or 'simple')

    Returns:
        Tuple of (aggregated_r, standard_error)
    """
    if len(correlations) != len(sample_sizes):
        raise ValueError("correlations and sample_sizes must have same length")

    if method == 'fisher':
        # Fisher's Z transformation
        z_values = [fishers_z_transform(r) for r in correlations]

        # Weights based on sample size
        weights = [n - 3 for n in sample_sizes]  # Fisher's Z variance is 1/(n-3)
        total_weight = sum(weights)

        # Weighted mean
        z_mean = sum(z * w for z, w in zip(z_values, weights)) / total_weight

        # Transform back
        r_aggregated = inverse_fishers_z(z_mean)

        # Standard error
        se = np.sqrt(1 / total_weight)

    elif method == 'simple':
        # Simple weighted average
        weights = sample_sizes
        total_weight = sum(weights)

        r_aggregated = sum(r * w for r, w in zip(correlations, weights)) / total_weight

        # Simple standard error
        se = np.std(correlations) / np.sqrt(len(correlations))

    else:
        raise ValueError(f"Unknown method: {method}")

    return r_aggregated, se


def test_matrix_utils():
    """Test matrix utility functions."""
    print("Testing matrix utilities...")

    # Create test data
    test_data = pd.DataFrame([
        {'construct_1': 'PE', 'construct_2': 'BI', 'r': 0.65},
        {'construct_1': 'EE', 'construct_2': 'BI', 'r': 0.45},
        {'construct_1': 'PE', 'construct_2': 'EE', 'r': 0.50}
    ])

    # Test long_to_matrix
    print("\n1. Long to matrix conversion:")
    matrix = long_to_matrix(test_data)
    print(matrix)

    # Test positive definite check
    print("\n2. Positive definite check:")
    is_pd, eigenvalues = check_positive_definite(matrix)
    print(f"Is PD: {is_pd}")
    print(f"Eigenvalues: {eigenvalues}")

    # Test validation
    print("\n3. Matrix validation:")
    validation = validate_correlation_matrix(matrix)
    print(validation)

    # Test completeness
    print("\n4. Matrix completeness:")
    completeness = matrix_completeness(matrix)
    print(completeness)

    # Test beta to r conversion
    print("\n5. Beta to r conversion:")
    beta = 0.6
    r = beta_to_r(beta)
    print(f"Beta {beta} -> r {r}")

    # Test Fisher's Z
    print("\n6. Fisher's Z transformation:")
    r_test = 0.5
    z = fishers_z_transform(r_test)
    r_back = inverse_fishers_z(z)
    print(f"r {r_test} -> z {z} -> r {r_back}")

    # Test aggregation
    print("\n7. Correlation aggregation:")
    cors = [0.5, 0.6, 0.55]
    ns = [100, 150, 120]
    r_agg, se = aggregate_correlations(cors, ns)
    print(f"Aggregated r: {r_agg:.3f}, SE: {se:.3f}")


if __name__ == "__main__":
    test_matrix_utils()
