#!/usr/bin/env python3
"""Build Paper A S004/S048 source-corrected diagnostic input.

This script applies the 2026-06-14 source-review decision without modifying the
canonical frozen reference or human workbooks. It replaces only S004/S048 rows
in a diagnostic copy of the N-ready Paper A input and writes coverage summaries.
"""

from __future__ import annotations

import csv
import itertools
import math
from collections import defaultdict
from copy import deepcopy
from pathlib import Path


REPO = Path("/Users/newhosung/Academic/2026/AI Adoption Meta Analysis/Git/journal_AI-adoption_meta")
ONEDRIVE = Path(
    "/Users/newhosung/Library/CloudStorage/OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity/"
    "AI Adoption Meta Analysis - Documents"
)
BASELINE_INPUT = REPO / (
    "data/04_extraction/05_llm_masem_substitution/results/"
    "paper2_masem_substitution_rerun_input_n_weighted_all_source_supported_20260612.csv"
)
FROZEN_REFERENCE = REPO / (
    "data/04_extraction/04_reference_standard_freeze/"
    "full_corpus_reference_standard_frozen_20260609.csv"
)
CORRECTION_PROPOSAL = ONEDRIVE / (
    "Meta/AI Adoption/03_source_adjudication/Paper_A/"
    "2026-06-14_priority15_detailed_source_review/"
    "paper_a_s004_s048_source_correction_proposal_20260614.csv"
)
OUT = REPO / (
    "data/04_extraction/05_llm_masem_substitution/results/"
    "paper_a_source_corrected_s004_s048_20260614"
)
ONEDRIVE_OUT = ONEDRIVE / (
    "Meta/AI Adoption/03_source_adjudication/Paper_A/"
    "2026-06-14_priority15_detailed_source_review"
)

FULL10 = ["PE", "EE", "SI", "FC", "ATT", "SE", "TRU", "ANX", "BI", "UB"]
TRUST6 = ["PE", "EE", "SI", "TRU", "BI", "UB"]
CORE7_ATT = ["PE", "EE", "SI", "FC", "ATT", "BI", "UB"]
ROUTES = {
    "paper_a_full10_theory_target": FULL10,
    "paper_a_trust6_mechanism": TRUST6,
    "paper_a_core7_att_mediation": CORE7_ATT,
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def canonical_pair(a: str, b: str) -> str:
    return "-".join(sorted([str(a).strip(), str(b).strip()]))


def safe_float(x: str) -> float | None:
    try:
        return float(str(x).strip())
    except Exception:
        return None


def numeric_median(values: list[str]) -> str:
    nums = sorted(v for v in (safe_float(x) for x in values) if v is not None)
    if not nums:
        return ""
    mid = len(nums) // 2
    if len(nums) % 2:
        val = nums[mid]
    else:
        val = (nums[mid - 1] + nums[mid]) / 2
    if abs(val - round(val)) < 1e-9:
        return str(int(round(val)))
    return f"{val:.6g}"


def route_pairs(constructs: list[str]) -> set[str]:
    return {canonical_pair(a, b) for a, b in itertools.combinations(constructs, 2)}


def row_pair(row: dict[str, str]) -> str:
    return canonical_pair(row.get("construct_1", ""), row.get("construct_2", ""))


def build_study_defaults(
    baseline_rows: list[dict[str, str]],
    frozen_rows: list[dict[str, str]],
) -> dict[str, dict[str, str]]:
    defaults: dict[str, dict[str, str]] = {}
    for sid in ["S004", "S048"]:
        b = [r for r in baseline_rows if r.get("study_id") == sid]
        f = [r for r in frozen_rows if r.get("study_id") == sid]
        sample_size = numeric_median(
            [r.get("sample_size_numeric", "") for r in b]
            + [r.get("sample_size", "") for r in b]
            + [r.get("n", "") for r in f]
        )
        defaults[sid] = {
            "sample_size": sample_size,
            "country": first_nonblank(b, "country"),
            "education_level": first_nonblank(b, "education_level"),
            "user_role": first_nonblank(b, "user_role") or "student",
            "ai_type": first_nonblank(b, "ai_type") or "generative",
            "common_method_bias": first_nonblank(b, "common_method_bias"),
            "theoretical_framework": first_nonblank(b, "theoretical_framework"),
        }
    return defaults


def first_nonblank(rows: list[dict[str, str]], field: str) -> str:
    for row in rows:
        val = str(row.get(field, "")).strip()
        if val:
            return val
    return ""


def make_corrected_row(
    fields: list[str],
    template: dict[str, str],
    proposal: dict[str, str],
    defaults: dict[str, str],
) -> dict[str, str]:
    sid = proposal["study_id"]
    c1 = proposal["construct_1"]
    c2 = proposal["construct_2"]
    pp = canonical_pair(c1, c2)
    rv = proposal["proposed_source_r_value"]
    row = {field: "" for field in fields}
    row.update({k: v for k, v in template.items() if k in row})
    row.update(
        {
            "analysis_record_id": f"PAPER_A_SRC_CORR_20260614_{sid}_{pp}",
            "analysis_set": "primary",
            "analysis_role": "source-adjudication corrected direct-r diagnostic input",
            "input_id": f"PAPER_A_SRC_CORR_20260614_{sid}_{pp}",
            "source_decision_id": "paper_a_pkc_not_se_s048_source_correction_20260614",
            "source_pair": "PDF_SOURCE_REVIEW_20260614",
            "study_id": sid,
            "construct_1": c1,
            "construct_2": c2,
            "construct_pair": pp,
            "construct_pair_canonical": pp,
            "construct_pair_direction": "canonical source-correction proposal",
            "r_value": rv,
            "r_numeric": rv,
            "r_abs": f"{abs(float(rv)):.6g}" if rv else "",
            "r_source": "direct",
            "statistic_family": "source_reported_direct_correlation_or_latent_correlation",
            "evidence_type": "source_reported_direct_correlation_or_latent_correlation",
            "is_source_reported_or_direct": "1",
            "is_model_derived_or_converted": "0",
            "include_primary": "1",
            "include_expanded": "1",
            "include_sensitivity": "0",
            "sample_size": defaults.get("sample_size", ""),
            "sample_size_numeric": defaults.get("sample_size", ""),
            "country": defaults.get("country", ""),
            "education_level": defaults.get("education_level", ""),
            "user_role": defaults.get("user_role", ""),
            "ai_type": defaults.get("ai_type", ""),
            "common_method_bias": defaults.get("common_method_bias", ""),
            "theoretical_framework": defaults.get("theoretical_framework", ""),
            "significance": "NR",
            "confidence": "source_review_proposal_20260614",
            "consensus_basis": "PDF source review; researcher rejected PKC->SE; S048 INT->BI and USE->UB accepted",
            "conversion_rule": "none_direct_source_matrix",
            "override_rule": proposal["action"],
            "source_location": proposal["source_location"],
            "source_artifact": f"{sid}.pdf",
            "source_locator": proposal["source_location"],
            "notes": (
                f"Diagnostic source-correction proposal generated 2026-06-14. "
                f"Action={proposal['action']}. Mapping={proposal['source_mapping']}."
            ),
            "freeze_tier": "source_review_correction_proposal_not_frozen",
            "include_primary_model_ready": "1" if rv and defaults.get("sample_size") else "0",
            "freeze_decision": "diagnostic_not_frozen",
            "substitution_scenario": "paper_a_source_correction_diagnostic",
            "substitution_action": proposal["action"],
            "substitution_source_task_unit_id": "",
            "substitution_review_priority": "researcher_confirmed_source_correction_rule",
            "substitution_model_id": "",
            "substitution_original_r_numeric": "",
            "substitution_r_numeric": rv,
            "substitution_delta": "",
            "sample_size_original": "",
            "sample_size_numeric_original": "",
            "sample_size_reconciliation_status": "filled_from_existing_study_or_frozen_reference_n",
            "sample_size_reconciliation_source": "baseline input or frozen reference study median",
            "sample_size_reconciliation_rule": "study_level_n_reused_for_source_correction",
            "sample_size_reconciliation_note": "Diagnostic input only; canonical workbook/frozen reference not modified.",
            "masem_n_weighted_eligibility": "include_n_weighted_masem" if rv and defaults.get("sample_size") else "exclude_missing_n_or_r",
            "sample_size_pdf_override_original_status": "",
            "sample_size_pdf_override_value": "",
            "sample_size_pdf_override_source": "",
            "sample_size_pdf_override_status": "not_applied_diagnostic_source_correction",
            "sample_size_pdf_override_note": "No new PDF N extraction in this script.",
        }
    )
    return row


def summarize_route(rows: list[dict[str, str]], route: str, constructs: list[str]) -> dict[str, str]:
    pairs_needed = route_pairs(constructs)
    study_pairs: dict[str, set[str]] = defaultdict(set)
    pair_studies: dict[str, set[str]] = defaultdict(set)
    for row in rows:
        c1 = row.get("construct_1", "")
        c2 = row.get("construct_2", "")
        if c1 not in constructs or c2 not in constructs or c1 == c2:
            continue
        rv = safe_float(row.get("r_numeric", ""))
        n = safe_float(row.get("sample_size_numeric", ""))
        if rv is None or n is None or abs(rv) >= 1 or n <= 3:
            continue
        pp = row_pair(row)
        if pp not in pairs_needed:
            continue
        sid = row["study_id"]
        study_pairs[sid].add(pp)
        pair_studies[pp].add(sid)
    missing_pairs = sorted(pairs_needed - set(pair_studies))
    complete = sorted(sid for sid, ps in study_pairs.items() if pairs_needed <= ps)
    max_pairs = max((len(ps) for ps in study_pairs.values()), default=0)
    return {
        "route": route,
        "constructs": ",".join(constructs),
        "required_pairs": str(len(pairs_needed)),
        "observed_pairs": str(len(pair_studies)),
        "missing_pairs": str(len(missing_pairs)),
        "numeric_studies": str(len(study_pairs)),
        "complete_case_studies": str(len(complete)),
        "max_pairs_in_one_study": str(max_pairs),
        "min_pair_k": str(min((len(v) for v in pair_studies.values()), default=0)),
        "complete_case_study_ids": ";".join(complete),
        "missing_pair_list": ";".join(missing_pairs),
    }


def write_report(
    baseline_summary: list[dict[str, str]],
    corrected_summary: list[dict[str, str]],
    changelog: list[dict[str, str]],
) -> None:
    lines = [
        "# Paper A S004/S048 source-corrected diagnostic input",
        "",
        "Date: 2026-06-14",
        "",
        "## Decision encoded",
        "",
        "- `PKC -> SE` is rejected for S004.",
        "- S004 PKC-derived SE rows are excluded from the diagnostic corrected input.",
        "- S048 Table 2 is accepted as Pearson correlation evidence with `INT -> BI` and `USE -> UB`.",
        "- This is not a frozen-reference edit and not a workbook overwrite.",
        "",
        "## Diagnostic input changes",
        "",
        "| action | rows |",
        "| --- | ---: |",
    ]
    counts = defaultdict(int)
    for row in changelog:
        counts[row["change_action"]] += 1
    for action, count in sorted(counts.items()):
        lines.append(f"| {action} | {count} |")
    lines += [
        "",
        "## Coverage before and after",
        "",
        "| Dataset | Route | Required pairs | Observed pairs | Missing pairs | Numeric studies | Complete-case studies | Max pairs in one study | Min pair k |",
        "| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for label, rows in [("baseline", baseline_summary), ("corrected", corrected_summary)]:
        for r in rows:
            lines.append(
                f"| {label} | {r['route']} | {r['required_pairs']} | {r['observed_pairs']} | "
                f"{r['missing_pairs']} | {r['numeric_studies']} | {r['complete_case_studies']} | "
                f"{r['max_pairs_in_one_study']} | {r['min_pair_k']} |"
            )
    lines += [
        "",
        "## Boundary",
        "",
        "Use this input for diagnostic reruns only. If the rerun materially improves Paper A feasibility, the same S004/S048 corrections still need a final human source-adjudication promotion step before they become the canonical Paper A analytic input.",
        "",
        "## Output files",
        "",
        f"- `{OUT / 'paper_a_source_corrected_s004_s048_input_20260614.csv'}`",
        f"- `{OUT / 'paper_a_source_corrected_s004_s048_changelog_20260614.csv'}`",
        f"- `{OUT / 'paper_a_source_corrected_s004_s048_coverage_summary_20260614.csv'}`",
    ]
    report = "\n".join(lines) + "\n"
    (OUT / "PAPER_A_SOURCE_CORRECTED_S004_S048_INPUT_20260614.md").write_text(report, encoding="utf-8")
    (ONEDRIVE_OUT / "PAPER_A_SOURCE_CORRECTED_S004_S048_INPUT_20260614.md").write_text(report, encoding="utf-8")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    ONEDRIVE_OUT.mkdir(parents=True, exist_ok=True)
    baseline = read_csv(BASELINE_INPUT)
    fields = list(baseline[0].keys())
    frozen = read_csv(FROZEN_REFERENCE)
    proposal = read_csv(CORRECTION_PROPOSAL)

    replace_studies = {"S004", "S048"}
    baseline_kept = [r for r in baseline if r.get("study_id") not in replace_studies]
    templates = {
        sid: deepcopy(next((r for r in baseline if r.get("study_id") == sid), {}))
        for sid in replace_studies
    }
    defaults = build_study_defaults(baseline, frozen)

    include_actions = {
        "keep_existing_frozen_value",
        "correct_existing_frozen_value",
        "add_priority_candidate",
        "add_source_visible_non_candidate",
    }
    corrected_study_rows: list[dict[str, str]] = []
    changelog: list[dict[str, str]] = []
    baseline_by_study_pair = {(r.get("study_id"), row_pair(r)): r for r in baseline if r.get("study_id") in replace_studies}

    for p in proposal:
        sid = p["study_id"]
        pp = canonical_pair(p["construct_1"], p["construct_2"])
        old = baseline_by_study_pair.get((sid, pp))
        if p["action"] in include_actions:
            corrected = make_corrected_row(fields, templates.get(sid, {}), p, defaults[sid])
            corrected_study_rows.append(corrected)
            changelog.append(
                {
                    "study_id": sid,
                    "construct_pair": pp,
                    "change_action": p["action"],
                    "old_r_numeric": "" if old is None else old.get("r_numeric", ""),
                    "new_r_numeric": corrected.get("r_numeric", ""),
                    "old_present_in_baseline": "yes" if old is not None else "no",
                    "included_in_corrected_input": "yes",
                    "reason": p["source_mapping"],
                }
            )
        else:
            changelog.append(
                {
                    "study_id": sid,
                    "construct_pair": pp,
                    "change_action": p["action"],
                    "old_r_numeric": "" if old is None else old.get("r_numeric", ""),
                    "new_r_numeric": "",
                    "old_present_in_baseline": "yes" if old is not None else "no",
                    "included_in_corrected_input": "no",
                    "reason": p["source_mapping"],
                }
            )

    corrected = baseline_kept + corrected_study_rows
    write_csv(OUT / "paper_a_source_corrected_s004_s048_input_20260614.csv", corrected, fields)
    write_csv(OUT / "paper_a_source_corrected_s004_s048_changelog_20260614.csv", changelog, list(changelog[0].keys()))
    write_csv(ONEDRIVE_OUT / "paper_a_source_corrected_s004_s048_input_20260614.csv", corrected, fields)
    write_csv(ONEDRIVE_OUT / "paper_a_source_corrected_s004_s048_changelog_20260614.csv", changelog, list(changelog[0].keys()))

    baseline_summary = [summarize_route(baseline, route, constructs) for route, constructs in ROUTES.items()]
    corrected_summary = [summarize_route(corrected, route, constructs) for route, constructs in ROUTES.items()]
    summary_rows: list[dict[str, str]] = []
    for label, rows in [("baseline", baseline_summary), ("corrected", corrected_summary)]:
        for row in rows:
            r = dict(row)
            r["dataset"] = label
            summary_rows.append(r)
    summary_fields = ["dataset"] + list(baseline_summary[0].keys())
    write_csv(OUT / "paper_a_source_corrected_s004_s048_coverage_summary_20260614.csv", summary_rows, summary_fields)
    write_csv(ONEDRIVE_OUT / "paper_a_source_corrected_s004_s048_coverage_summary_20260614.csv", summary_rows, summary_fields)
    write_report(baseline_summary, corrected_summary, changelog)

    print("corrected_input_rows", len(corrected))
    print("change_rows", len(changelog))
    for row in corrected_summary:
        print(row["route"], "observed", row["observed_pairs"], "missing", row["missing_pairs"], "complete", row["complete_case_studies"])
    print("output_dir", OUT)


if __name__ == "__main__":
    main()
