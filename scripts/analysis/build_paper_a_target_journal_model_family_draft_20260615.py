#!/usr/bin/env python3
"""Build the 2026-06-15 target-journal Paper A draft with model-family MASEM results."""

from __future__ import annotations

import re
import shutil
from pathlib import Path

import pandas as pd

REPO = Path(__file__).resolve().parents[2]
SRC = REPO / "paper_a/manuscript/target_journal/PAPER_A_COMPUTERS_AND_EDUCATION_TARGET_DRAFT_20260612.md"
OUT_DIR = REPO / "paper_a/manuscript/target_journal/model_family_results_20260615"
OUT = OUT_DIR / "PAPER_A_COMPUTERS_AND_EDUCATION_TARGET_DRAFT_MODEL_FAMILY_RESULTS_20260615.md"
FIG_SRC = REPO / "data/04_extraction/05_llm_masem_substitution/results/paper_a_researcher_approved_s048_inference_figures_manuscript_20260615/figures"
FIG_OUT = OUT_DIR / "figures"
INF_DIR = REPO / "data/04_extraction/05_llm_masem_substitution/results/paper_a_researcher_approved_s048_inference_figures_manuscript_20260615"
ONEDRIVE = Path("/Users/newhosung/Library/CloudStorage/OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity/AI Adoption Meta Analysis - Documents/Meta/AI Adoption/05_manuscripts/Paper_A/2026-06-15_target_journal_model_family_results")


def md_table(df: pd.DataFrame) -> str:
    values = df.fillna("").astype(str)
    lines = ["| " + " | ".join(values.columns) + " |", "| " + " | ".join(["---"] * len(values.columns)) + " |"]
    for _, row in values.iterrows():
        cells = [str(row[c]).replace("|", "\\|").replace("\n", " ") for c in values.columns]
        lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines)


def fmt(x: object, digits: int = 3) -> str:
    try:
        if pd.isna(x):
            return ""
        return f"{float(x):.{digits}f}"
    except Exception:
        return str(x)


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    if FIG_OUT.exists():
        shutil.rmtree(FIG_OUT)
    shutil.copytree(FIG_SRC, FIG_OUT)

    text = SRC.read_text(encoding="utf-8")
    paths = pd.read_csv(INF_DIR / "paper_a_model_family_structural_paths_ci_inference_20260615.csv")
    fit = pd.read_csv(INF_DIR / "paper_a_model_family_fit_with_n_20260615.csv")

    path_display = paths[["model_family", "parameter", "estimate", "ci_text", "inference_symbol", "inference_class"]].copy()
    path_display["estimate"] = path_display["estimate"].map(lambda x: fmt(x, 3))
    fit_display = fit[["model_family", "complete_case_k", "effective_sample_size", "chisq", "df", "p", "CFI", "TLI", "RMSEA", "SRMR", "AIC", "BIC"]].copy()
    for col in ["effective_sample_size", "chisq", "df", "p", "CFI", "TLI", "RMSEA", "SRMR", "AIC", "BIC"]:
        fit_display[col] = fit_display[col].map(lambda x: fmt(x, 3))

    submission_state = """## Submission Package State

This target-journal draft supersedes the 2026-06-12/2026-06-14 analysis boundary. The 2026-06-15 researcher-approved rerun promoted seven S048 Table 2 source-visible Pearson correlations into Paper A supplemental analysis provenance without mutating the Paper B source-anchored adjudicated human reference standard. The updated analysis supports a model-family MASEM manuscript structure: the full 10-construct framework is retained as the theoretical evidence map, while the empirically estimable structural results are reported through complete-case core7 and trust6 MASEM routes.

Current claim boundary:

- Full10 is the theoretical target and evidence map, not a converged single SEM estimate.
- Core7 attitude mediation and trust6 trust mechanism are the converged empirical model-family MASEM results.
- Trust, anxiety, and self-efficacy are mechanism constructs, not study-level moderators. Trust is estimable in the current empirical model family; anxiety and self-efficacy remain theory-relevant full10/supplementary mechanism candidates.
- Path-level support is classified by likelihood-based 95% confidence intervals from Stage 2 because finite standard errors and z-based path p values were not returned.
"""

    abstract = """## Abstract

Artificial intelligence tools are increasingly embedded in higher education, but the empirical adoption literature remains fragmented across constructs, samples, tools, and reporting formats. This study synthesizes higher-education AI adoption evidence using meta-analytic structural equation modeling. The theoretical target integrated performance expectancy, effort expectancy, social influence, facilitating conditions, attitude, self-efficacy, trust in AI, AI anxiety, behavioral intention, and use behavior. Because the full 10-construct network reached complete pairwise coverage but had no complete same-study 10-construct matrices, and sparse partial-matrix TSSEM remained non-estimable, we used a model-family MASEM strategy. The full 10-construct framework was retained as the theoretical evidence map, while complete-case core7 and trust6 models were estimated as empirical structural submodels. The core7 attitude-mediation model and trust6 mechanism model both converged with strong global fit. In the core7 model, facilitating conditions predicted attitude and use behavior, attitude predicted behavioral intention, and behavioral intention predicted use behavior. In the trust6 model, trust predicted behavioral intention and behavioral intention predicted use behavior, supporting trust as an AI-specific mechanism in adoption. These findings provide a defensible structural synthesis of AI adoption in higher education while preserving explicit boundaries around non-estimable full-network claims.

Keywords: artificial intelligence; technology acceptance; higher education; MASEM; UTAUT; trust; anxiety
"""

    analysis_plan = """### Analysis Plan

We treated the 10-construct AI adoption framework as the theoretical target and first evaluated whether the source-supported evidence base could sustain a single full-network MASEM. The target framework included performance expectancy, effort expectancy, social influence, facilitating conditions, attitude, self-efficacy, trust, AI anxiety, behavioral intention, and use behavior. Rows entered the primary analysis only when the correlation value and sample size were source-supported or researcher-approved with provenance.

Because no study supplied a complete 10-construct correlation matrix and sparse partial-matrix TSSEM produced non-positive-definite implied covariance structures, we did not force the full network into a single structural estimate. Instead, we used a model-family MASEM strategy. The full 10-construct network was retained as the theoretical evidence map. Empirically estimable submodels were then fit as complete-case TSSEM/MASEM models when all required construct pairs were present within a study and the resulting study-level correlation matrix was positive definite.

The empirical model family included two theory-consistent routes. The core7 attitude-mediation model estimated the central TAM/UTAUT adoption pathway among performance expectancy, effort expectancy, social influence, facilitating conditions, attitude, behavioral intention, and use behavior. The trust6 mechanism model estimated an AI-specific trust pathway among performance expectancy, effort expectancy, social influence, trust, behavioral intention, and use behavior. Stage 1 used random-effects TSSEM. Stage 2 fit the prespecified structural model to the pooled correlation matrix.

Path-level support was evaluated with likelihood-based 95% confidence intervals from Stage 2. Paths were interpreted as supported when the interval excluded zero. Because finite standard errors and z-based p values were not returned for individual paths, paths with incomplete intervals were flagged as indeterminate rather than treated as significant. OSMASEM or moderator meta-regression remains a separate analysis layer and is not used to reinterpret trust, anxiety, or self-efficacy as study-level moderators.
"""

    results = f"""## Results

### Analysis-Ready Evidence Base

The 2026-06-15 researcher-approved input contains 836 analysis rows. Seven S048 Table 2 values were already present in the source-correction layer and were promoted to researcher-approved supplemental Paper A provenance without duplicate insertion. The full 10-construct target reached complete pairwise coverage across the source-supported evidence base: 45 of 45 construct pairs were available for pairwise pooled evidence mapping.

| Input or gate | Current value | Submission interpretation |
| --- | ---: | --- |
| Researcher-approved analysis input rows | 836 | Current Paper A model-family input after ANX/TRU, S121 PE-SE, and S048 supplemental approval |
| Full10 pairwise construct-pair coverage | 45/45 | Sufficient for a theoretical evidence map |
| Full10 complete-case studies | 0 | Not sufficient for a single full10 SEM estimate |
| Sparse partial-matrix TSSEM | Failed | Non-positive-definite implied covariance under sparse partial matrices |
| Core7 complete-case matrices | 4 | Empirically estimable model-family route |
| Trust6 complete-case matrices | 7 | Empirically estimable model-family route |

### Full10 Theoretical Evidence Map

The full 10-construct model remains the theoretical target because pairwise evidence exists for all 45 construct pairs. However, no study supplied a complete same-study 10-construct correlation matrix. Sparse partial-matrix TSSEM remained non-estimable because the implied covariance structure was not positive definite. Therefore, the full10 model is reported as a theoretical evidence map rather than as a single primary SEM result.

![Figure 1. Full10 theoretical evidence map](figures/figure_1_full10_theoretical_evidence_map_heatmap_ci_20260615.png)

### Empirical Model-Family MASEM Fit

The reduced empirical model-family routes converged in complete-case TSSEM/MASEM. The core7 attitude-mediation model used four positive-definite complete-case matrices and fit the pooled matrix well. The trust6 mechanism model used seven positive-definite complete-case matrices and also showed strong fit.

{md_table(fit_display)}

### Core7 Attitude-Mediation Model

The core7 model estimated the central TAM/UTAUT adoption pathway. Supported paths, defined by likelihood-based 95% confidence intervals excluding zero, were facilitating conditions to attitude, social influence to behavioral intention, attitude to behavioral intention, facilitating conditions to use behavior, and behavioral intention to use behavior. Performance expectancy to attitude and social influence to attitude had intervals that included zero. Effort expectancy to attitude, performance expectancy to behavioral intention, and effort expectancy to behavioral intention had incomplete likelihood-based intervals and are not interpreted as supported.

![Figure 2. Core7 complete-case MASEM path diagram](figures/figure_2_core7_att_mediation_masem_path_ci_20260615.png)

### Trust6 Mechanism Model

The trust6 model estimated an AI-specific trust pathway. Supported paths were effort expectancy to behavioral intention, trust to behavioral intention, and behavioral intention to use behavior. Effort expectancy to trust, social influence to trust, and social influence to behavioral intention had intervals that included zero. Performance expectancy to trust and performance expectancy to behavioral intention had incomplete likelihood-based intervals and are not interpreted as supported. The supported trust-to-intention path indicates that trust can be reported as an empirical AI-specific mechanism in the current model family. Anxiety and self-efficacy remain theory-relevant constructs in the full10 evidence map or future reduced extensions, but they are not confirmed mediators in the current converged MASEM results.

![Figure 3. Trust6 complete-case MASEM path diagram](figures/figure_3_trust6_mechanism_masem_path_ci_20260615.png)

### Path-Level Inference Table

{md_table(path_display)}

### Figure Captions

Figure 1. Full 10-construct theoretical evidence map. Cells report pairwise random-effects pooled correlations and the number of contributing studies for each construct pair. The figure is an evidence-map summary, not a full 10-construct SEM estimate, because no primary study supplied a complete 10-construct correlation matrix and sparse partial-matrix TSSEM did not yield a positive-definite implied covariance structure.

Figure 2. Core7 attitude-mediation complete-case MASEM path diagram. Solid black paths have likelihood-based 95% confidence intervals excluding zero, dashed gray paths have intervals including zero, and dotted light-gray paths have incomplete intervals and are not classified as supported. Exogenous covariances and residual variances were estimated but omitted from the diagram for readability.

Figure 3. Trust6 mechanism complete-case MASEM path diagram. Solid black paths have likelihood-based 95% confidence intervals excluding zero, dashed gray paths have intervals including zero, and dotted light-gray paths have incomplete intervals and are not classified as supported. Exogenous covariances and residual variances were estimated but omitted from the diagram for readability.
"""

    text = re.sub(r"## Submission Package State\n\n.*?\n\n## Highlights", submission_state + "\n## Highlights", text, flags=re.S)
    text = re.sub(r"## Abstract\n\n.*?\n\nKeywords:.*?\n\n## Introduction", abstract + "\n## Introduction", text, flags=re.S)
    text = re.sub(r"### Analysis Plan\n\n.*?\n\n## Results", analysis_plan + "\n\n## Results", text, flags=re.S)
    text = re.sub(r"## Results\n\n.*?\n\n## Discussion", results + "\n\n## Discussion", text, flags=re.S)
    text = re.sub(r"\n\n## 2026-06-14 latest-human-workbook correction\n\n.*\Z", "", text, flags=re.S)
    text = text.replace("Draft date: 2026-06-12", "Draft date: 2026-06-15")
    text += "\n\n## Analysis Provenance and Reproducibility\n\nThe 2026-06-15 model-family results are generated from `data/04_extraction/05_llm_masem_substitution/results/paper_a_researcher_approved_s048_inference_figures_manuscript_20260615/` and the upstream complete-case and pairwise MASEM outputs in `paper_a_researcher_approved_s048_complete_case_20260615/` and `paper_a_researcher_approved_s048_model_family_masem_20260615/`. The associated Git release is `paper-a-s048-masem-20260615`; the present draft adds path-level CI classification and manuscript-ready figures.\n"
    OUT.write_text(text, encoding="utf-8")

    readme = OUT_DIR / "README_MODEL_FAMILY_RESULTS_DRAFT_20260615.md"
    readme.write_text("""# Paper A target-journal model-family results draft

This folder contains the 2026-06-15 target-journal Markdown draft integrating the researcher-approved S048 model-family MASEM rerun.

## Main file

- `PAPER_A_COMPUTERS_AND_EDUCATION_TARGET_DRAFT_MODEL_FAMILY_RESULTS_20260615.md`

## Figure files

- `figures/figure_1_full10_theoretical_evidence_map_heatmap_ci_20260615.png`
- `figures/figure_2_core7_att_mediation_masem_path_ci_20260615.png`
- `figures/figure_3_trust6_mechanism_masem_path_ci_20260615.png`

## Boundary

Full10 is reported as a theoretical evidence map. Core7 and trust6 are the converged empirical model-family MASEM routes. Path-level support uses likelihood-based 95% CI exclusion of zero, not z-based p values.
""", encoding="utf-8")

    if ONEDRIVE.exists():
        shutil.rmtree(ONEDRIVE)
    shutil.copytree(OUT_DIR, ONEDRIVE)
    print(f"out={OUT}")
    print(f"onedrive={ONEDRIVE}")
    print(f"path_rows={len(paths)}")


if __name__ == "__main__":
    main()
