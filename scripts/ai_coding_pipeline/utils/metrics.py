#!/usr/bin/env python3
"""
Agreement metrics for inter-coder reliability.
Includes Cohen's kappa, Fleiss' kappa, ICC, and MAE.
"""

import numpy as np
from typing import List, Dict, Any
from collections import Counter


def cohens_kappa(rater1: List[Any], rater2: List[Any]) -> float:
    """
    Calculate Cohen's kappa for categorical agreement between two raters.

    Args:
        rater1: Ratings from first rater
        rater2: Ratings from second rater

    Returns:
        Cohen's kappa coefficient
    """
    if len(rater1) != len(rater2):
        raise ValueError("Rater lists must have same length")

    n = len(rater1)

    # Create confusion matrix
    categories = sorted(set(rater1) | set(rater2))
    cat_to_idx = {cat: i for i, cat in enumerate(categories)}

    matrix = np.zeros((len(categories), len(categories)))

    for r1, r2 in zip(rater1, rater2):
        i = cat_to_idx[r1]
        j = cat_to_idx[r2]
        matrix[i, j] += 1

    # Observed agreement
    p_o = np.trace(matrix) / n

    # Expected agreement
    marginal_1 = matrix.sum(axis=1) / n
    marginal_2 = matrix.sum(axis=0) / n
    p_e = np.sum(marginal_1 * marginal_2)

    # Cohen's kappa
    if p_e == 1.0:
        return 1.0 if p_o == 1.0 else 0.0

    kappa = (p_o - p_e) / (1 - p_e)

    return kappa


def fleiss_kappa(ratings: List[List[Any]]) -> float:
    """
    Calculate Fleiss' kappa for agreement among multiple raters.

    Args:
        ratings: List of rating lists (one list per item, containing ratings from all raters)

    Returns:
        Fleiss' kappa coefficient
    """
    n_items = len(ratings)
    n_raters = len(ratings[0]) if ratings else 0

    if n_items == 0 or n_raters == 0:
        return 0.0

    # Get all categories
    all_categories = set()
    for item_ratings in ratings:
        all_categories.update(item_ratings)

    categories = sorted(all_categories)
    n_categories = len(categories)
    cat_to_idx = {cat: i for i, cat in enumerate(categories)}

    # Create frequency matrix (items x categories)
    freq_matrix = np.zeros((n_items, n_categories))

    for i, item_ratings in enumerate(ratings):
        for rating in item_ratings:
            j = cat_to_idx[rating]
            freq_matrix[i, j] += 1

    # Calculate P_i (proportion of agreement for each item)
    P_i = np.sum(freq_matrix ** 2, axis=1) - n_raters
    P_i = P_i / (n_raters * (n_raters - 1))

    # Mean observed agreement
    P_bar = np.mean(P_i)

    # Calculate p_j (proportion of all assignments to category j)
    p_j = np.sum(freq_matrix, axis=0) / (n_items * n_raters)

    # Expected agreement
    P_e = np.sum(p_j ** 2)

    # Fleiss' kappa
    if P_e == 1.0:
        return 1.0 if P_bar == 1.0 else 0.0

    kappa = (P_bar - P_e) / (1 - P_e)

    return kappa


def icc_2_1(rater1_scores: List[float], rater2_scores: List[float]) -> float:
    """
    Calculate Intraclass Correlation Coefficient (ICC(2,1)).
    Two-way random effects, single rater/measurement.

    Args:
        rater1_scores: Scores from rater 1
        rater2_scores: Scores from rater 2

    Returns:
        ICC(2,1) coefficient
    """
    if len(rater1_scores) != len(rater2_scores):
        raise ValueError("Rater score lists must have same length")

    n = len(rater1_scores)

    # Convert to numpy arrays
    r1 = np.array(rater1_scores, dtype=float)
    r2 = np.array(rater2_scores, dtype=float)

    # Stack ratings
    ratings = np.column_stack([r1, r2])

    # Calculate means
    grand_mean = np.mean(ratings)
    item_means = np.mean(ratings, axis=1)
    rater_means = np.mean(ratings, axis=0)

    # Calculate sum of squares
    # Total SS
    SS_total = np.sum((ratings - grand_mean) ** 2)

    # Between items SS
    SS_items = 2 * np.sum((item_means - grand_mean) ** 2)

    # Between raters SS
    SS_raters = n * np.sum((rater_means - grand_mean) ** 2)

    # Residual SS
    SS_residual = SS_total - SS_items - SS_raters

    # Degrees of freedom
    df_items = n - 1
    df_raters = 1  # 2 raters - 1
    df_residual = (n - 1) * (2 - 1)

    # Mean squares
    MS_items = SS_items / df_items if df_items > 0 else 0
    MS_raters = SS_raters / df_raters if df_raters > 0 else 0
    MS_residual = SS_residual / df_residual if df_residual > 0 else 0

    # ICC(2,1) calculation
    numerator = MS_items - MS_residual
    denominator = MS_items + (2 - 1) * MS_residual + 2 * (MS_raters - MS_residual) / n

    if denominator == 0:
        return 0.0

    icc = numerator / denominator

    # Clip to valid range
    icc = np.clip(icc, -1.0, 1.0)

    return float(icc)


def mae(values1: List[float], values2: List[float]) -> float:
    """
    Calculate Mean Absolute Error between two sets of values.

    Args:
        values1: First set of values
        values2: Second set of values

    Returns:
        Mean absolute error
    """
    if len(values1) != len(values2):
        raise ValueError("Value lists must have same length")

    v1 = np.array(values1, dtype=float)
    v2 = np.array(values2, dtype=float)

    mae_value = np.mean(np.abs(v1 - v2))

    return float(mae_value)


def rmse(values1: List[float], values2: List[float]) -> float:
    """
    Calculate Root Mean Squared Error between two sets of values.

    Args:
        values1: First set of values
        values2: Second set of values

    Returns:
        Root mean squared error
    """
    if len(values1) != len(values2):
        raise ValueError("Value lists must have same length")

    v1 = np.array(values1, dtype=float)
    v2 = np.array(values2, dtype=float)

    rmse_value = np.sqrt(np.mean((v1 - v2) ** 2))

    return float(rmse_value)


def agreement_report(ai_values: Dict[str, List[Any]], human_values: Dict[str, List[Any]],
                    quality_targets: Dict[str, float]) -> Dict[str, Any]:
    """
    Generate comprehensive agreement report.

    Args:
        ai_values: Dictionary of AI-coded values by field
        human_values: Dictionary of human-coded values by field
        quality_targets: Target thresholds for quality metrics

    Returns:
        Comprehensive agreement report
    """
    report = {
        'timestamp': str(np.datetime64('now')),
        'categorical_fields': {},
        'numerical_fields': {},
        'overall_summary': {}
    }

    # Process categorical fields
    categorical_fields = []
    for field in ai_values.keys():
        if field in human_values:
            ai_vals = ai_values[field]
            human_vals = human_values[field]

            # Check if categorical (strings or limited unique values)
            unique_count = len(set(ai_vals) | set(human_vals))

            if isinstance(ai_vals[0], str) or unique_count <= 20:
                categorical_fields.append(field)

                # Calculate Cohen's kappa
                kappa = cohens_kappa(ai_vals, human_vals)

                # Calculate raw agreement
                n_agree = sum(1 for a, h in zip(ai_vals, human_vals) if a == h)
                agreement_rate = n_agree / len(ai_vals)

                target_kappa = quality_targets.get('kappa_categorical', 0.85)

                report['categorical_fields'][field] = {
                    'cohens_kappa': round(kappa, 4),
                    'agreement_rate': round(agreement_rate, 4),
                    'n_items': len(ai_vals),
                    'target_kappa': target_kappa,
                    'passed': kappa >= target_kappa
                }

    # Process numerical fields
    numerical_fields = []
    for field in ai_values.keys():
        if field in human_values and field not in categorical_fields:
            ai_vals = ai_values[field]
            human_vals = human_values[field]

            numerical_fields.append(field)

            # Calculate ICC
            icc_value = icc_2_1(ai_vals, human_vals)

            # Calculate MAE
            mae_value = mae(ai_vals, human_vals)

            # Calculate RMSE
            rmse_value = rmse(ai_vals, human_vals)

            # Calculate correlation
            correlation = np.corrcoef(ai_vals, human_vals)[0, 1]

            target_icc = quality_targets.get('icc_numerical', 0.95)
            target_mae = quality_targets.get('mae_correlation', 0.03)

            report['numerical_fields'][field] = {
                'icc_2_1': round(icc_value, 4),
                'mae': round(mae_value, 4),
                'rmse': round(rmse_value, 4),
                'correlation': round(correlation, 4),
                'n_items': len(ai_vals),
                'target_icc': target_icc,
                'target_mae': target_mae,
                'icc_passed': icc_value >= target_icc,
                'mae_passed': mae_value <= target_mae
            }

    # Overall summary
    cat_passed = sum(1 for f in report['categorical_fields'].values() if f['passed'])
    num_icc_passed = sum(1 for f in report['numerical_fields'].values() if f['icc_passed'])
    num_mae_passed = sum(1 for f in report['numerical_fields'].values() if f['mae_passed'])

    report['overall_summary'] = {
        'n_categorical_fields': len(categorical_fields),
        'n_numerical_fields': len(numerical_fields),
        'categorical_passed': cat_passed,
        'numerical_icc_passed': num_icc_passed,
        'numerical_mae_passed': num_mae_passed,
        'all_passed': (
            cat_passed == len(categorical_fields) and
            num_icc_passed == len(numerical_fields) and
            num_mae_passed == len(numerical_fields)
        )
    }

    return report


def test_metrics():
    """Test agreement metrics."""
    print("Testing agreement metrics...\n")

    # Test Cohen's kappa
    print("1. Cohen's Kappa:")
    rater1 = ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B']
    rater2 = ['A', 'B', 'C', 'A', 'C', 'C', 'B', 'B']
    kappa = cohens_kappa(rater1, rater2)
    print(f"   Kappa: {kappa:.3f}")

    # Test Fleiss' kappa
    print("\n2. Fleiss' Kappa:")
    ratings = [
        ['A', 'A', 'B'],  # Item 1: 3 raters
        ['B', 'B', 'B'],  # Item 2
        ['A', 'A', 'A'],  # Item 3
        ['C', 'C', 'B']   # Item 4
    ]
    fleiss_k = fleiss_kappa(ratings)
    print(f"   Fleiss' Kappa: {fleiss_k:.3f}")

    # Test ICC
    print("\n3. Intraclass Correlation (ICC):")
    scores1 = [0.5, 0.6, 0.7, 0.8, 0.9]
    scores2 = [0.52, 0.58, 0.71, 0.79, 0.88]
    icc_value = icc_2_1(scores1, scores2)
    print(f"   ICC(2,1): {icc_value:.3f}")

    # Test MAE
    print("\n4. Mean Absolute Error:")
    mae_value = mae(scores1, scores2)
    print(f"   MAE: {mae_value:.3f}")

    # Test RMSE
    print("\n5. Root Mean Squared Error:")
    rmse_value = rmse(scores1, scores2)
    print(f"   RMSE: {rmse_value:.3f}")

    # Test agreement report
    print("\n6. Agreement Report:")
    ai_vals = {
        'ai_type': ['generative', 'predictive', 'generative', 'conversational'],
        'correlation': [0.5, 0.6, 0.7, 0.8]
    }
    human_vals = {
        'ai_type': ['generative', 'predictive', 'conversational', 'conversational'],
        'correlation': [0.52, 0.58, 0.71, 0.79]
    }
    targets = {
        'kappa_categorical': 0.85,
        'icc_numerical': 0.95,
        'mae_correlation': 0.03
    }

    report = agreement_report(ai_vals, human_vals, targets)
    print(f"   Overall passed: {report['overall_summary']['all_passed']}")
    print(f"   Categorical kappa: {report['categorical_fields']['ai_type']['cohens_kappa']:.3f}")
    print(f"   Numerical ICC: {report['numerical_fields']['correlation']['icc_2_1']:.3f}")


if __name__ == "__main__":
    test_metrics()
