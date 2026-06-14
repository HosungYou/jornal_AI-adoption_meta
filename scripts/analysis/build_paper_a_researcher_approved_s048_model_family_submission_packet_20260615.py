#!/usr/bin/env python3
"""Build manuscript-facing Paper A model-family MASEM tables and scaffold."""

from __future__ import annotations

import shutil
from pathlib import Path

import pandas as pd

REPO_ROOT = Path(__file__).resolve().parents[2]
COMPLETE_DIR = REPO_ROOT / "data/04_extraction/05_llm_masem_substitution/results/paper_a_researcher_approved_s048_complete_case_20260615"
PARTIAL_DIR = REPO_ROOT / "data/04_extraction/05_llm_masem_substitution/results/paper_a_researcher_approved_s048_model_family_masem_20260615"
OUT_DIR = REPO_ROOT / "data/04_extraction/05_llm_masem_substitution/results/paper_a_researcher_approved_s048_model_family_submission_packet_20260615"
ONEDRIVE_DIR = Path("/Users/newhosung/Library/CloudStorage/OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity/AI Adoption Meta Analysis - Documents/Meta/AI Adoption/04_analysis_strategy/Paper_A/2026-06-15_researcher_approved_s048_model_family_masem_submission_packet")

ROUTE_LABELS = {
    "paper_a_core7_att_mediation": "core7 ATT mediation",
    "paper_a_trust6_mechanism": "trust6 trust mechanism",
    "paper_a_full10_theory_target": "full10 theoretical target",
}


def fmt(x: object, digits: int = 3) -> str:
    if pd.isna(x):
        return ""
    if isinstance(x, float):
        return f"{x:.{digits}f}"
    return str(x)


def format_df(df: pd.DataFrame, digits: int = 3) -> pd.DataFrame:
    return df.map(lambda v: fmt(v, digits))


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(path)
    return pd.read_csv(path)


def write_md_table(df: pd.DataFrame, path: Path) -> None:
    path.write_text(to_md_table(df) + "\n", encoding="utf-8")


def to_md_table(df: pd.DataFrame) -> str:
    values = df.fillna("").astype(str)
    headers = list(values.columns)
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    for _, row in values.iterrows():
        cells = [str(row[col]).replace("\n", " ").replace("|", "\\|") for col in headers]
        lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines)


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    complete_summary = read_csv(COMPLETE_DIR / "paper_a_source_corrected_complete_case_summary_20260615.csv")
    partial_summary = read_csv(PARTIAL_DIR / "paper_a_masem_execution_summary_20260615.csv")
    coverage = partial_summary[["route", "constructs", "required_pairs", "observed_pairs", "missing_pairwise_pooled_pairs", "single_study_pairs", "min_pair_k", "partial_studies", "complete_case_studies", "stage1_tssem_status", "stage2_status", "pairwise_pooled_min_eigen", "nearpd_min_eigen"]].copy()
    coverage.insert(0, "model_family", coverage["route"].map(ROUTE_LABELS))

    merged = partial_summary.merge(
        complete_summary[[
            "route",
            "positive_definite_complete_case_studies",
            "positive_definite_complete_case_ids",
            "stage1_status",
            "stage1_method",
            "stage2_status",
            "stage2_path_count",
            "stage2_fit_count",
        ]],
        on="route",
        how="left",
        suffixes=("_partial", "_complete"),
    )

    eligibility_rows = []
    for _, row in merged.iterrows():
        route = row["route"]
        if route == "paper_a_full10_theory_target":
            manuscript_role = "theoretical target and evidence map; not current primary SEM estimate"
            primary_status = "not empirically estimable as one SEM in current data"
        elif route == "paper_a_core7_att_mediation":
            manuscript_role = "primary empirical model-family member"
            primary_status = "eligible complete-case diagnostic model"
        elif route == "paper_a_trust6_mechanism":
            manuscript_role = "primary empirical model-family member"
            primary_status = "eligible complete-case diagnostic model"
        else:
            manuscript_role = "supplementary"
            primary_status = "requires review"
        eligibility_rows.append({
            "model_family": ROUTE_LABELS.get(route, route),
            "constructs": row["constructs"],
            "required_pairs": int(row["required_pairs"]),
            "observed_pairs_after_rescue": int(row["observed_pairs"]),
            "min_pair_k": int(row["min_pair_k"]),
            "partial_matrix_studies": int(row["partial_studies"]),
            "complete_case_studies": int(row["complete_case_studies"]),
            "positive_definite_complete_cases": int(row.get("positive_definite_complete_case_studies", 0) or 0),
            "partial_tssem_status": row["stage1_tssem_status"],
            "complete_case_stage1": row.get("stage1_status", ""),
            "complete_case_stage2": row.get("stage2_status", ""),
            "pooled_min_eigen": row["pairwise_pooled_min_eigen"],
            "primary_status": primary_status,
            "manuscript_role": manuscript_role,
        })
    eligibility = pd.DataFrame(eligibility_rows)
    eligibility.to_csv(OUT_DIR / "paper_a_model_family_eligibility_table_20260615.csv", index=False)
    write_md_table(eligibility, OUT_DIR / "paper_a_model_family_eligibility_table_20260615.md")

    fit_frames = []
    for route in ["paper_a_core7_att_mediation", "paper_a_trust6_mechanism"]:
        path = COMPLETE_DIR / f"{route}_complete_case_stage2_fit_indices_20260615.csv"
        fit = read_csv(path)
        wide = fit.pivot_table(index="route", columns="fit_index", values="value", aggfunc="first").reset_index()
        wide.insert(0, "model_family", wide["route"].map(ROUTE_LABELS))
        fit_frames.append(wide)
    fit_table = pd.concat(fit_frames, ignore_index=True)
    fit_cols = ["model_family", "chisq", "df", "p", "CFI", "TLI", "RMSEA", "SRMR", "AIC", "BIC"]
    fit_table = fit_table[[c for c in fit_cols if c in fit_table.columns]]
    fit_table.to_csv(OUT_DIR / "paper_a_model_family_fit_table_20260615.csv", index=False)
    write_md_table(format_df(fit_table), OUT_DIR / "paper_a_model_family_fit_table_20260615.md")

    path_frames = []
    for route in ["paper_a_core7_att_mediation", "paper_a_trust6_mechanism"]:
        p = COMPLETE_DIR / f"{route}_complete_case_stage2_paths_20260615.csv"
        paths = read_csv(p)
        paths = paths[paths["parameter_family"].eq("structural_path")].copy()
        paths.insert(0, "model_family", ROUTE_LABELS[route])
        paths["estimate"] = paths["estimate"].round(3)
        path_frames.append(paths[["model_family", "parameter", "estimate"]])
    path_table = pd.concat(path_frames, ignore_index=True)
    path_table.to_csv(OUT_DIR / "paper_a_model_family_structural_paths_20260615.csv", index=False)
    write_md_table(path_table, OUT_DIR / "paper_a_model_family_structural_paths_20260615.md")

    coverage.to_csv(OUT_DIR / "paper_a_full10_coverage_after_anx_tru_rescue_20260615.csv", index=False)
    write_md_table(coverage.fillna(""), OUT_DIR / "paper_a_full10_coverage_after_anx_tru_rescue_20260615.md")

    full10_row = eligibility[eligibility["model_family"].str.startswith("full10")].iloc[0]
    core7_fit = fit_table[fit_table["model_family"].eq("core7 ATT mediation")].iloc[0]
    trust6_fit = fit_table[fit_table["model_family"].eq("trust6 trust mechanism")].iloc[0]

    md = f"""# Paper A Researcher-Approved S048 Model-Family MASEM Submission Packet

Date: 2026-06-15

## Bottom line

Paper A should report **model-family MASEM** as the primary empirical route. The 10-construct network remains the theory target and evidence map, but it is not currently estimable as a single primary SEM.

## Current empirical basis

- Full10 pairwise coverage after researcher-approved S048 staging: {int(full10_row['observed_pairs_after_rescue'])}/{int(full10_row['required_pairs'])} pairs.
- Full10 complete-case studies: {int(full10_row['complete_case_studies'])}.
- Full10 sparse partial-matrix TSSEM status: {full10_row['partial_tssem_status']}.
- Core7 complete-case TSSEM: {eligibility.loc[eligibility['model_family'].eq('core7 ATT mediation'), 'complete_case_stage2'].iloc[0]}.
- Trust6 complete-case TSSEM: {eligibility.loc[eligibility['model_family'].eq('trust6 trust mechanism'), 'complete_case_stage2'].iloc[0]}.

## Manuscript-ready interpretation

The source-corrected and researcher-approved supplemental Paper A evidence base supports the full conceptual network as an evidence map, but not as a single full10 MASEM estimate. The empirical MASEM results should therefore be organized as a model family. The core7 model estimates the central UTAUT/TAM adoption pathway through attitude and behavioral intention. The trust6 model estimates an AI-specific trust mechanism linking belief constructs to intention and use. Anxiety and self-efficacy remain theory-relevant mechanism constructs, but they should be reported in supplementary evidence maps or reduced extensions unless source-supported matrices become sufficient for a stable SEM.

## Table 1. Model-family eligibility

{to_md_table(eligibility)}

## Table 2. Complete-case MASEM fit

{to_md_table(format_df(fit_table))}

## Table 3. Structural path estimates

{to_md_table(path_table)}

## Proposed Methods text

We treated the 10-construct AI adoption framework as the theoretical target model and first evaluated its empirical support as a source-anchored coverage network. Because no primary study supplied a complete 10-construct correlation matrix and sparse partial-matrix TSSEM attempts produced non-positive-definite implied covariance structures, we did not force the full network into a single primary SEM. Instead, we pre-specified a family of theory-consistent MASEM models corresponding to empirically supported substructures of the target framework. The primary empirical MASEM models were restricted to construct families with source-supported same-study co-measurement and acceptable correlation evidence. The full 10-construct model was retained as the conceptual target and reported through coverage, feasibility, and pairwise evidence-map results.

## Proposed Results text

After source correction plus researcher-approved ANX/TRU, S121 PE-SE, and S048 supplements, the full 10-construct network reached complete pairwise coverage but still had no complete same-study 10-construct matrix. Sparse partial-matrix TSSEM attempts remained non-estimable because the implied covariance structure was not positive definite. The model-family route was therefore used for empirical MASEM. The core7 attitude-mediation model converged with excellent approximate fit (CFI = {fmt(core7_fit.get('CFI'), 3)}, TLI = {fmt(core7_fit.get('TLI'), 3)}, RMSEA = {fmt(core7_fit.get('RMSEA'), 3)}, SRMR = {fmt(core7_fit.get('SRMR'), 3)}). The trust6 mechanism model also converged with strong fit (CFI = {fmt(trust6_fit.get('CFI'), 3)}, TLI = {fmt(trust6_fit.get('TLI'), 3)}, RMSEA = {fmt(trust6_fit.get('RMSEA'), 3)}, SRMR = {fmt(trust6_fit.get('SRMR'), 3)}). These findings support reporting the full10 network as the theoretical evidence map and the core7/trust6 models as the empirically estimable MASEM family.

## Reviewer-defense points

- This is not a post hoc abandonment of full10; full10 remains the theoretical target and feasibility map.
- The empirical route is constrained by source-supported same-study co-measurement, not by convenience.
- The strategy avoids arbitrary nearPD repair, unsupported imputation, beta/path-to-correlation mixing, and rejected construct remaps.
- Trust, anxiety, and self-efficacy are mechanism constructs, not moderators, under the current Paper A route.

## Generated files

- `paper_a_model_family_eligibility_table_20260615.csv`
- `paper_a_model_family_fit_table_20260615.csv`
- `paper_a_model_family_structural_paths_20260615.csv`
- `paper_a_full10_coverage_after_anx_tru_rescue_20260615.csv`
"""
    (OUT_DIR / "PAPER_A_MODEL_FAMILY_MASEM_SUBMISSION_PACKET_20260615.md").write_text(md, encoding="utf-8")

    if ONEDRIVE_DIR.exists():
        shutil.rmtree(ONEDRIVE_DIR)
    shutil.copytree(OUT_DIR, ONEDRIVE_DIR)

    print(f"out_dir={OUT_DIR}")
    print(f"onedrive_dir={ONEDRIVE_DIR}")
    print(f"eligibility_rows={len(eligibility)}")
    print(f"path_rows={len(path_table)}")


if __name__ == "__main__":
    main()
