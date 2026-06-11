#!/usr/bin/env python3
"""Generate Paper2 RQ1 extraction-validity summaries.

The report deliberately avoids one overall 8,783-row denominator. It uses
model-explicit locked outputs, denominator families, and source/type strata.
"""

from __future__ import annotations

import argparse
import csv
import os
import re
from collections import defaultdict
from pathlib import Path
from statistics import mean, median


REPO = Path(__file__).resolve().parents[2]
AI_ADOPTION_ROOT = Path(
    os.environ.get(
        "AI_ADOPTION_META_ROOT",
        str(
            Path.home()
            / "<PRIVATE_ONEDRIVE_SHARED_LIBRARY>"
            / "AI Adoption Meta Analysis - Documents/Meta/AI Adoption"
        ),
    )
)
DEFAULT_REFERENCE = (
    AI_ADOPTION_ROOT
    / "Paper2_LLM_Extraction_Working_20260605/09_reference_freeze/"
    "paper2_llm_task_units_labeled_tiered_freeze_20260605.csv"
)
STEP5 = REPO / "data/04_extraction/05_llm_masem_substitution"
DEFAULT_SCORED = STEP5 / "results/paper2_locked_output_scored_20260606.csv"
DEFAULT_OUTPUT_CSV = STEP5 / "results/paper2_rq1_extraction_validity_20260611.csv"
DEFAULT_OUTPUT_MD = STEP5 / "results/PAPER2_RQ1_EXTRACTION_VALIDITY_20260611.md"

MODEL_ROLES = {
    "codex:gpt-5.5": "primary_prespecified_workflow",
    "gemini:gemini-3-flash-preview": "supplementary_cross_model_sensitivity",
    "claude:sonnet": "supplementary_cross_model_sensitivity",
}
SCORED_STATUSES = {"scored", "scored_abstention"}
NUMERIC_FAMILIES = {
    "direct_r_effect_size_extraction",
    "converted_or_model_derived_effect_size",
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def normalize_basic(value: str) -> str:
    return re.sub(r"\s+", " ", (value or "").strip().lower())


def normalize_relaxed(value: str) -> str:
    text = (value or "").strip().lower()
    text = text.replace("&", " and ")
    text = re.sub(r"[_/\-]+", " ", text)
    text = re.sub(r"[^a-z0-9.]+", " ", text)
    text = re.sub(r"\b(n a|n/a|not applicable|not reported|not available)\b", "na", text)
    return re.sub(r"\s+", " ", text).strip()


def parse_float(value: str) -> float | None:
    match = re.search(r"[-+]?(?:\d+\.\d+|\d+|\.\d+)", value or "")
    if not match:
        return None
    try:
        return float(match.group(0))
    except ValueError:
        return None


def ratio(num: int, den: int) -> str:
    return "" if den == 0 else f"{num / den:.6f}"


def fmt_stat(values: list[float], fn: str) -> str:
    if not values:
        return ""
    value = mean(values) if fn == "mean" else median(values)
    return f"{value:.6f}"


def task_stratum(row: dict[str, str]) -> str:
    family = row.get("denominator_family", "")
    notes = normalize_basic(row.get("reference_notes", ""))
    stat_source = normalize_basic(row.get("statistic_source_type", ""))
    if family == "direct_r_effect_size_extraction":
        if "source_blank" in notes:
            return "source_blank_direct_r"
        return "source_reported_direct_r"
    if family == "converted_or_model_derived_effect_size":
        if stat_source:
            return f"converted_or_model_derived_{stat_source}"
        return "converted_or_model_derived_untyped"
    if family == "metadata_extraction":
        field = normalize_relaxed(row.get("field_key", "")) or "metadata_unspecified"
        return f"metadata_{field.replace(' ', '_')}"
    return family or "unclassified"


def enrich_rows(scored: list[dict[str, str]], reference: dict[str, dict[str, str]]) -> list[dict[str, str]]:
    rows = []
    for row in scored:
        model_id = row.get("model_id", "")
        if model_id not in MODEL_ROLES:
            continue
        ref = reference.get(row.get("task_unit_id", ""), {})
        enriched = dict(row)
        enriched.update(
            {
                "analysis_role": MODEL_ROLES[model_id],
                "reference_notes": ref.get("notes", ""),
                "field_key": ref.get("field_key", ""),
                "construct_pair": ref.get("construct_pair", ""),
                "expected_answer_type": ref.get("expected_answer_type", ""),
                "statistic_source_type": ref.get("statistic_source_type", ""),
                "source_evidence_status": ref.get("source_evidence_status", ""),
                "downstream_masem_impact": ref.get("downstream_masem_impact", ""),
                "task_stratum": "",
            }
        )
        enriched["task_stratum"] = task_stratum(enriched)
        rows.append(enriched)
    return rows


def summarize(rows: list[dict[str, str]], scope: str) -> list[dict[str, object]]:
    groups: dict[tuple[str, str, str], list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        groups[(row["model_id"], row["denominator_family"], row["task_stratum"])].append(row)

    output: list[dict[str, object]] = []
    for (model_id, family, stratum), group in sorted(groups.items()):
        scored = [row for row in group if row.get("score_status") in SCORED_STATUSES]
        correct = sum(1 for row in scored if row.get("is_correct") == "1")
        abstentions = sum(1 for row in scored if row.get("score_status") == "scored_abstention")

        strict_denom = 0
        strict_correct = 0
        relaxed_correct = 0
        if family == "metadata_extraction":
            for row in scored:
                if row.get("score_status") == "scored_abstention":
                    strict_denom += 1
                    continue
                expected = (row.get("expected_value") or "").strip()
                observed = (row.get("model_value") or "").strip()
                strict_denom += 1
                strict_correct += int(expected == observed)
                relaxed_correct += int(normalize_relaxed(expected) == normalize_relaxed(observed))

        numeric_errors: list[float] = []
        numeric_exact = 0
        numeric_within_005 = 0
        numeric_within_020 = 0
        numeric_within_050 = 0
        numeric_over_050 = 0
        sign_reversal = 0
        numeric_denom = 0
        if family in NUMERIC_FAMILIES:
            for row in scored:
                if row.get("score_status") == "scored_abstention":
                    numeric_denom += 1
                    continue
                err = parse_float(row.get("absolute_error", ""))
                expected_num = parse_float(row.get("expected_value", ""))
                observed_num = parse_float(row.get("model_value", ""))
                numeric_denom += 1
                if err is None:
                    continue
                numeric_errors.append(err)
                numeric_exact += int(err <= 0.0005)
                numeric_within_005 += int(err <= 0.005)
                numeric_within_020 += int(err <= 0.020)
                numeric_within_050 += int(err <= 0.050)
                numeric_over_050 += int(err > 0.050)
                if (
                    expected_num is not None
                    and observed_num is not None
                    and abs(expected_num) > 0
                    and abs(observed_num) > 0
                    and expected_num * observed_num < 0
                ):
                    sign_reversal += 1

        output.append(
            {
                "comparison_scope": scope,
                "analysis_role": MODEL_ROLES[model_id],
                "model_id": model_id,
                "denominator_family": family,
                "task_stratum": stratum,
                "row_n": len(group),
                "scored_n": len(scored),
                "correct_n": correct,
                "accuracy": ratio(correct, len(scored)),
                "abstention_n": abstentions,
                "abstention_rate": ratio(abstentions, len(scored)),
                "not_scored_n": len(group) - len(scored),
                "metadata_strict_denom": strict_denom,
                "metadata_strict_correct_n": strict_correct,
                "metadata_strict_accuracy": ratio(strict_correct, strict_denom),
                "metadata_relaxed_correct_n": relaxed_correct,
                "metadata_relaxed_accuracy": ratio(relaxed_correct, strict_denom),
                "numeric_denom": numeric_denom,
                "numeric_exact_or_rounding_n": numeric_exact,
                "numeric_within_0_005_n": numeric_within_005,
                "numeric_within_0_020_n": numeric_within_020,
                "numeric_within_0_050_n": numeric_within_050,
                "numeric_over_0_050_n": numeric_over_050,
                "numeric_sign_reversal_n": sign_reversal,
                "mean_abs_error": fmt_stat(numeric_errors, "mean"),
                "median_abs_error": fmt_stat(numeric_errors, "median"),
            }
        )
    return output


def model_family_totals(rows: list[dict[str, object]], model_id: str) -> list[dict[str, object]]:
    return [
        row
        for row in rows
        if row["comparison_scope"] == "model_explicit_available_rows"
        and row["model_id"] == model_id
    ]


def md_table(rows: list[dict[str, object]], fields: list[str]) -> list[str]:
    lines = [
        "| " + " | ".join(fields) + " |",
        "|" + "|".join("---" for _ in fields) + "|",
    ]
    for row in rows:
        lines.append("| " + " | ".join(str(row.get(field, "")) for field in fields) + " |")
    return lines


def format_md(summary_rows: list[dict[str, object]]) -> str:
    codex = model_family_totals(summary_rows, "codex:gpt-5.5")
    codex_core = [
        row
        for row in codex
        if row["denominator_family"]
        in {
            "direct_r_effect_size_extraction",
            "converted_or_model_derived_effect_size",
            "metadata_extraction",
        }
    ]
    overlap = [
        row
        for row in summary_rows
        if row["comparison_scope"] == "overlap_codex_gpt55_claude_sonnet_gemini3flash"
        and row["denominator_family"] in NUMERIC_FAMILIES | {"metadata_extraction"}
    ]

    lines = [
        "# Paper2 RQ1 Extraction Validity",
        "",
        "Date: 2026-06-11",
        "",
        "## Boundary",
        "",
        "This table evaluates extraction validity by task family and stratum. It does",
        "not collapse the 8,783 task units into one denominator. Codex GPT-5.5 is",
        "the primary prespecified workflow; Claude Sonnet and Gemini 3 Flash are",
        "supplementary cross-model sensitivity evidence.",
        "",
        "Abstentions on scorable rows are counted as incorrect and reported as",
        "abstentions. Metadata rows report strict exact match and relaxed normalized",
        "match. Converted beta/path/source-statistic rows are numeric extraction",
        "strata, not source-reported direct-r rows.",
        "",
        "## Primary Codex Core Families",
        "",
    ]
    lines.extend(
        md_table(
            codex_core,
            [
                "denominator_family",
                "task_stratum",
                "row_n",
                "scored_n",
                "correct_n",
                "accuracy",
                "abstention_n",
                "metadata_strict_accuracy",
                "metadata_relaxed_accuracy",
                "numeric_within_0_005_n",
                "mean_abs_error",
            ],
        )
    )
    lines.extend(["", "## Three-Model Overlap Core Families", ""])
    lines.extend(
        md_table(
            overlap,
            [
                "model_id",
                "denominator_family",
                "task_stratum",
                "row_n",
                "scored_n",
                "correct_n",
                "accuracy",
                "abstention_n",
                "numeric_within_0_005_n",
            ],
        )
    )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "- Use the Codex rows as the primary workflow-validity evidence.",
            "- Use the overlap rows only for supplementary cross-model sensitivity.",
            "- High abstention counts are substantive behavior, not missing denominator",
            "  artifacts, because scorable-row abstentions count as incorrect.",
            "- `source_blank_direct_r` remains in the direct-r extraction family but",
            "  should be flagged as weaker source-evidence quality.",
            "- Converted/source-statistic rows should be discussed as numeric recovery",
            "  under source-type separation, not as direct-r equivalence.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scored", type=Path, default=DEFAULT_SCORED)
    parser.add_argument("--reference", type=Path, default=DEFAULT_REFERENCE)
    parser.add_argument("--output-csv", type=Path, default=DEFAULT_OUTPUT_CSV)
    parser.add_argument("--output-md", type=Path, default=DEFAULT_OUTPUT_MD)
    args = parser.parse_args()

    reference = {row["task_unit_id"]: row for row in read_csv(args.reference)}
    rows = enrich_rows(read_csv(args.scored), reference)
    task_models: dict[str, set[str]] = defaultdict(set)
    for row in rows:
        task_models[row["task_unit_id"]].add(row["model_id"])
    overlap_ids = {
        task_id for task_id, models in task_models.items() if set(MODEL_ROLES).issubset(models)
    }

    summary_rows = []
    summary_rows.extend(summarize(rows, "model_explicit_available_rows"))
    summary_rows.extend(
        summarize(
            [row for row in rows if row["task_unit_id"] in overlap_ids],
            "overlap_codex_gpt55_claude_sonnet_gemini3flash",
        )
    )

    fields = [
        "comparison_scope",
        "analysis_role",
        "model_id",
        "denominator_family",
        "task_stratum",
        "row_n",
        "scored_n",
        "correct_n",
        "accuracy",
        "abstention_n",
        "abstention_rate",
        "not_scored_n",
        "metadata_strict_denom",
        "metadata_strict_correct_n",
        "metadata_strict_accuracy",
        "metadata_relaxed_correct_n",
        "metadata_relaxed_accuracy",
        "numeric_denom",
        "numeric_exact_or_rounding_n",
        "numeric_within_0_005_n",
        "numeric_within_0_020_n",
        "numeric_within_0_050_n",
        "numeric_over_0_050_n",
        "numeric_sign_reversal_n",
        "mean_abs_error",
        "median_abs_error",
    ]
    write_csv(args.output_csv, summary_rows, fields)
    args.output_md.write_text(format_md(summary_rows), encoding="utf-8")
    print(f"rq1_summary_rows={len(summary_rows)}")
    print(args.output_csv)
    print(args.output_md)


if __name__ == "__main__":
    main()
