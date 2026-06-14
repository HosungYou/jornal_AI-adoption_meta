#!/usr/bin/env python3
"""Build Paper A model-family submission-run packet and Intro/Theory/Methods scaffold."""

from __future__ import annotations

import csv
import shutil
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
ONEDRIVE = Path(
    "/Users/newhosung/Library/CloudStorage/OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity/"
    "AI Adoption Meta Analysis - Documents"
)
RUN_DIR = REPO / "data/04_extraction/05_llm_masem_substitution/results/paper_a_model_family_masem_submission_run_20260614"
INPUT_DIR = REPO / "data/04_extraction/05_llm_masem_substitution/results/paper_a_source_clean_submission_input_20260614"
OUT_DIR = REPO / "data/04_extraction/05_llm_masem_substitution/results/paper_a_model_family_masem_submission_run_packet_20260614"
MANUSCRIPT_DIR = REPO / "paper_a/manuscript/model_family_masem_20260614"
ONEDRIVE_PACKET = ONEDRIVE / "Meta/AI Adoption/04_analysis_strategy/Paper_A/2026-06-14_model_family_masem_submission_run_packet"
ONEDRIVE_MANUSCRIPT = ONEDRIVE / "Meta/AI Adoption/05_manuscript/Paper_A/2026-06-14_model_family_masem_intro_theory_methods"

ROUTE_LABELS = {
    "paper_a_core7_att_mediation": "core7 ATT mediation",
    "paper_a_trust6_mechanism": "trust6 trust mechanism",
    "paper_a_full10_theory_target": "full10 theoretical target",
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, object]], headers: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=headers, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def fnum(value: object, digits: int = 3) -> str:
    try:
        if value in (None, ""):
            return ""
        return f"{float(value):.{digits}f}"
    except (TypeError, ValueError):
        return str(value)


def md_table(rows: list[dict[str, object]], headers: list[str]) -> str:
    lines = ["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(headers)) + " |"]
    for row in rows:
        cells = [str(row.get(h, "")).replace("\n", " ").replace("|", "\\|") for h in headers]
        lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines)


def fit_wide(route: str) -> dict[str, str]:
    rows = read_csv(RUN_DIR / f"{route}_complete_case_stage2_fit_indices_20260614.csv")
    out = {"route": route, "model_family": ROUTE_LABELS[route]}
    for row in rows:
        out[row["fit_index"]] = row["value"]
    return out


def paths(route: str) -> list[dict[str, object]]:
    rows = read_csv(RUN_DIR / f"{route}_complete_case_stage2_paths_20260614.csv")
    out = []
    for row in rows:
        if row.get("parameter_family") == "structural_path":
            out.append({
                "model_family": ROUTE_LABELS[route],
                "path": row["parameter"].replace("_to_", " -> "),
                "estimate": fnum(row["estimate"]),
            })
    return out


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    MANUSCRIPT_DIR.mkdir(parents=True, exist_ok=True)
    ONEDRIVE_PACKET.mkdir(parents=True, exist_ok=True)
    ONEDRIVE_MANUSCRIPT.mkdir(parents=True, exist_ok=True)

    summary = read_csv(RUN_DIR / "paper_a_source_corrected_complete_case_summary_20260614.csv")
    coverage = read_csv(INPUT_DIR / "paper_a_source_clean_submission_input_route_coverage_20260614.csv")

    eligibility = []
    coverage_by_route = {row["route"]: row for row in coverage}
    coverage_key = {
        "paper_a_core7_att_mediation": "core7_att_mediation",
        "paper_a_trust6_mechanism": "trust6_mechanism",
        "paper_a_full10_theory_target": "full10_theory_target",
    }
    for row in summary:
        route = row["route"]
        cov = coverage_by_route[coverage_key[route]]
        role = "primary empirical model-family member" if route in {"paper_a_core7_att_mediation", "paper_a_trust6_mechanism"} else "theoretical target and evidence map"
        status = "eligible and converged" if row["stage2_status"] == "converged" else "not empirically estimable as one SEM"
        eligibility.append({
            "model_family": ROUTE_LABELS[route],
            "constructs": row["constructs"],
            "required_pairs": row["required_pairs"],
            "observed_pairs": cov["observed_pairs"],
            "complete_case_studies": row["positive_definite_complete_case_studies"],
            "complete_case_ids": row["positive_definite_complete_case_ids"] or "none",
            "stage1": row["stage1_status"],
            "stage2": row["stage2_status"],
            "role": role,
            "submission_status": status,
        })

    fit_rows = [fit_wide("paper_a_core7_att_mediation"), fit_wide("paper_a_trust6_mechanism")]
    fit_table = []
    for row in fit_rows:
        fit_table.append({
            "model_family": row["model_family"],
            "chisq": fnum(row.get("chisq")),
            "df": fnum(row.get("df"), 0),
            "p": fnum(row.get("p")),
            "CFI": fnum(row.get("CFI")),
            "TLI": fnum(row.get("TLI")),
            "RMSEA": fnum(row.get("RMSEA")),
            "SRMR": fnum(row.get("SRMR")),
            "AIC": fnum(row.get("AIC")),
            "BIC": fnum(row.get("BIC")),
        })
    path_table = paths("paper_a_core7_att_mediation") + paths("paper_a_trust6_mechanism")

    write_csv(OUT_DIR / "paper_a_submission_run_model_family_eligibility_20260614.csv", eligibility, list(eligibility[0].keys()))
    write_csv(OUT_DIR / "paper_a_submission_run_model_family_fit_20260614.csv", fit_table, list(fit_table[0].keys()))
    write_csv(OUT_DIR / "paper_a_submission_run_model_family_paths_20260614.csv", path_table, list(path_table[0].keys()))

    core_fit = fit_table[0]
    trust_fit = fit_table[1]
    packet = f"""# Paper A model-family MASEM submission run packet

Date: 2026-06-14

## Execution status

The Paper A source-clean submission input was used for the model-family MASEM run. This is the modified direction: full10 is retained as the theoretical target and evidence map, while `core7` and `trust6` are the empirical primary model-family members.

## Eligibility

{md_table(eligibility, list(eligibility[0].keys()))}

## Fit table

{md_table(fit_table, list(fit_table[0].keys()))}

## Structural paths

{md_table(path_table, list(path_table[0].keys()))}

## Interpretation

The full10 network has complete pairwise coverage in the source-clean input but zero complete-case studies, so it remains a theoretical target and evidence-map result rather than a single primary SEM. The core7 and trust6 models both converged from positive-definite complete-case matrices and therefore form the current primary empirical model-family MASEM route.
"""
    packet_path = OUT_DIR / "PAPER_A_MODEL_FAMILY_MASEM_SUBMISSION_RUN_PACKET_20260614.md"
    packet_path.write_text(packet, encoding="utf-8")

    manuscript = f"""# Paper A Draft: Introduction, Theoretical Background, and Methods

Date: 2026-06-14
Working title: Understanding AI Adoption in Education: A Model-Family Meta-Analytic Structural Equation Modeling Study

## Introduction

Artificial intelligence has moved rapidly from a specialized technical domain into everyday educational practice. Students, instructors, institutions, and platform designers increasingly encounter AI systems as writing assistants, tutoring tools, feedback engines, analytics dashboards, and decision-support interfaces. This rapid diffusion has intensified a familiar but still unresolved question in technology acceptance research: why do users intend to adopt and continue using a new technology when the technology is powerful, uncertain, and unevenly trusted?

Research on educational technology adoption has often relied on established acceptance theories such as the Technology Acceptance Model and the Unified Theory of Acceptance and Use of Technology. These frameworks converge on a core proposition: adoption is shaped by beliefs about performance benefits, effort demands, social influence, facilitating conditions, attitudes, intentions, and use behavior. In AI adoption, however, the same core adoption pathway is complicated by additional mechanism constructs. Trust is central because AI systems require users to decide whether the system is reliable, explainable, and appropriate to rely on. Anxiety is relevant because AI can produce uncertainty, threat, or discomfort. Self-efficacy is relevant because users' perceived capability to work with AI may shape whether AI feels useful, manageable, or worth adopting.

Despite the size of the AI adoption literature, the evidence base is fragmented. Primary studies do not always measure the same constructs, report the same correlation matrices, or use the same construct labels. As a result, a conventional narrative review can identify recurring predictors, but it cannot test whether the theory-implied paths cohere across studies. Meta-analytic structural equation modeling offers a stronger approach because it can synthesize correlation structures and test theory-driven path models. At the same time, MASEM should not be used to force a theoretical network that the source matrices do not support. If no primary study provides a complete matrix for a broad construct network, and if sparse partial-matrix estimation produces non-positive-definite covariance structures, the more defensible strategy is to separate the theoretical target model from the empirically estimable model family.

This study therefore treats the 10-construct AI adoption framework as the theoretical target and evidence map, while using model-family MASEM as the primary empirical route. The full framework includes performance expectancy, effort expectancy, social influence, facilitating conditions, attitude, behavioral intention, use behavior, trust, anxiety, and self-efficacy. The empirical MASEM analyses focus on source-supported submodels that are theoretically nested within this framework and sufficiently co-measured across studies. This approach preserves the theoretical ambition of the full AI adoption framework without overstating what the available correlation evidence can estimate as a single structural model.

The study makes three contributions. First, it clarifies the structure of AI adoption evidence by distinguishing the full theoretical network from the empirically estimable model family. Second, it tests two central adoption mechanisms using MASEM: a core UTAUT/TAM attitude-intention-use pathway and an AI-specific trust mechanism. Third, it provides a transparent feasibility account for anxiety and self-efficacy, treating them as mechanism constructs that should be retained in the theory map but not forced into a full SEM when the source matrices do not support stable estimation.

## Theoretical Background

### Core technology acceptance pathway

The Technology Acceptance Model argues that users' acceptance of technology is shaped by perceived usefulness and perceived ease of use, which influence attitudes, intentions, and use. UTAUT extends this tradition by integrating performance expectancy, effort expectancy, social influence, and facilitating conditions as central determinants of behavioral intention and use. In the present construct map, performance expectancy captures the perceived instrumental benefit of AI, effort expectancy captures perceived ease or difficulty, social influence captures perceived social pressure or normative support, and facilitating conditions capture the perceived availability of resources and support.

The core7 model represents this adoption pathway with seven constructs: performance expectancy, effort expectancy, social influence, facilitating conditions, attitude, behavioral intention, and use behavior. The model is theoretically conservative. It does not attempt to estimate every construct in the broader AI adoption framework. Instead, it tests the central adoption sequence that is most consistently measured across the corpus: belief constructs shape attitude and intention, and intention predicts use behavior. Facilitating conditions are allowed to shape attitude and use behavior because resource availability can influence both users' evaluations of AI and their ability to enact use.

### Trust as an AI adoption mechanism

Trust has a special role in AI adoption. In conventional technology acceptance, usefulness and ease may be sufficient to explain much of intention. In AI contexts, however, users also evaluate whether the system is dependable, competent, fair, transparent, and appropriate for the task. Trust does not simply add another predictor; it represents a mechanism through which beliefs about AI become willingness to rely on AI.

The trust6 model captures this mechanism with six constructs: performance expectancy, effort expectancy, social influence, trust, behavioral intention, and use behavior. Performance expectancy and effort expectancy can shape trust because systems that appear useful and manageable may be judged as more dependable or appropriate. Social influence can shape trust because institutional endorsement, peer use, and expert recommendation can signal legitimacy. Trust, in turn, is expected to support behavioral intention, which predicts use behavior. This model is especially appropriate for AI adoption because it links standard acceptance beliefs to the reliance problem that distinguishes AI from many earlier educational technologies.

### Anxiety and self-efficacy as mechanism constructs

Anxiety and self-efficacy remain important in the 10-construct theoretical framework. They should not be treated as moderators under the current Paper A route. Instead, they are mechanism constructs. Self-efficacy reflects users' beliefs about their capability to use AI effectively and can shape perceived effort, attitudes, and intentions. Anxiety reflects discomfort, uncertainty, or threat associated with AI and can inhibit trust, ease, attitudes, or intentions.

However, theory relevance does not guarantee SEM estimability. In the current source-clean input, anxiety and self-efficacy help complete the full theoretical construct map at the pairwise level, but no study provides a complete same-study 10-construct matrix. Therefore, anxiety and self-efficacy are retained in the full10 evidence map and considered for supplementary mechanism analyses only when source-supported reduced matrices are sufficient. This is a methodological constraint, not a theoretical rejection of these constructs.

### Model-family logic

The primary empirical route is model-family MASEM. The full10 model defines the conceptual target and organizes evidence coverage, but it is not currently treated as a single estimable SEM. The model family consists of theoretically meaningful, source-supported submodels that can be estimated without arbitrary matrix repair or unsupported construct remapping. This strategy reduces the risk of overclaiming while preserving a coherent theoretical account of AI adoption.

## Methods

### Design

This study used meta-analytic structural equation modeling to synthesize correlation evidence on AI adoption in education. The analysis proceeded in two stages. First, we constructed a source-clean correlation input that preserved researcher-approved source corrections and excluded evidence types that were not acceptable as primary correlation inputs. Second, we evaluated the full 10-construct framework as a coverage and feasibility map and estimated the empirically supported model-family MASEM routes.

### Construct framework

The theoretical target framework included 10 constructs: performance expectancy, effort expectancy, social influence, facilitating conditions, attitude, self-efficacy, trust, anxiety, behavioral intention, and use behavior. Performance expectancy, effort expectancy, social influence, facilitating conditions, behavioral intention, and use behavior were anchored in UTAUT. Attitude and the belief-attitude-intention sequence were anchored in TAM. Trust, anxiety, and self-efficacy were retained as AI-specific or mechanism-relevant constructs rather than moderators.

### Source-clean input construction

The source-clean submission input incorporated the approved source-correction layer and researcher-approved ANX-TRU supplement. Specifically, the input retained the S048 source correction and the S036/S102 ANX-TRU rows approved for Paper A supplemental use. The S004 PKC-to-self-efficacy remap remained rejected. Beta/path coefficients, HTMT values, factor loadings, reliability coefficients, descriptive-only statistics, and theory-only statements were excluded from the primary correlation input unless separately labeled for sensitivity analysis. This input contained 834 rows.

The source-clean input produced complete pairwise coverage for the full 10-construct network, but no complete same-study 10-construct matrix. The full10 network therefore functioned as the theoretical target and evidence map. The core7 route had 21 of 21 required pairs and four positive-definite complete-case studies. The trust6 route had 15 of 15 required pairs and seven positive-definite complete-case studies.

### MASEM strategy

The primary empirical strategy was model-family MASEM. We did not force the full10 framework into a single primary SEM because the source-clean input had zero complete-case full10 matrices and prior sparse partial-matrix TSSEM attempts produced non-positive-definite implied covariance structures. Instead, we estimated two theory-consistent empirical model-family members that had sufficient same-study co-measurement: the core7 attitude-mediation model and the trust6 trust-mechanism model.

The core7 model included paths from performance expectancy, effort expectancy, social influence, and facilitating conditions to attitude; paths from performance expectancy, effort expectancy, social influence, and attitude to behavioral intention; and paths from facilitating conditions and behavioral intention to use behavior. The trust6 model included paths from performance expectancy, effort expectancy, and social influence to trust; paths from performance expectancy, effort expectancy, social influence, and trust to behavioral intention; and a path from behavioral intention to use behavior.

### Estimation

Complete-case TSSEM was used for the empirical model-family run. For each model-family member, study-level correlation matrices were built from studies that contained all required construct pairs and were positive definite. Stage 1 synthesized the eligible correlation matrices using random-effects TSSEM where possible, with fixed-effect estimation used only as a fallback if random-effects estimation failed. Stage 2 fitted the specified structural model to the pooled matrix. Model fit was evaluated using chi-square, degrees of freedom, p value, CFI, TLI, RMSEA, SRMR, AIC, and BIC.

The source-clean submission run converged for both empirical model-family members. The core7 model converged with CFI = {core_fit['CFI']}, TLI = {core_fit['TLI']}, RMSEA = {core_fit['RMSEA']}, and SRMR = {core_fit['SRMR']}. The trust6 model converged with CFI = {trust_fit['CFI']}, TLI = {trust_fit['TLI']}, RMSEA = {trust_fit['RMSEA']}, and SRMR = {trust_fit['SRMR']}. The full10 model was not estimated as a single primary SEM because no complete-case full10 matrices were available.

### Reporting boundary

The full10 framework is reported as the theoretical target model and evidence map. The core7 and trust6 models are reported as the primary empirical MASEM family. Anxiety and self-efficacy are retained as theoretical mechanism constructs, but they are not interpreted as moderators and are not forced into the primary SEM unless future source-supported matrices satisfy the same eligibility rules. This distinction is central to the interpretation of the results: the study tests empirically estimable submodels of a broader theory rather than claiming that the full 10-construct network has been estimated as one structural model.

## Immediate revision needs

1. Add target-journal-specific framing and word limits.
2. Insert PRISMA/sample description from the final Paper A corpus file.
3. Add formal hypotheses or research questions after the theory section.
4. Replace any provisional source-clean counts if the final reference input changes.
5. Integrate the final Results section after figures and tables are generated.
"""
    manuscript_path = MANUSCRIPT_DIR / "PAPER_A_MODEL_FAMILY_INTRO_THEORY_METHODS_DRAFT_20260614.md"
    manuscript_path.write_text(manuscript, encoding="utf-8")

    for path in [
        packet_path,
        OUT_DIR / "paper_a_submission_run_model_family_eligibility_20260614.csv",
        OUT_DIR / "paper_a_submission_run_model_family_fit_20260614.csv",
        OUT_DIR / "paper_a_submission_run_model_family_paths_20260614.csv",
    ]:
        shutil.copy2(path, ONEDRIVE_PACKET / path.name)
    shutil.copy2(manuscript_path, ONEDRIVE_MANUSCRIPT / manuscript_path.name)

    print(f"packet_out={OUT_DIR}")
    print(f"manuscript={manuscript_path}")
    print(f"onedrive_packet={ONEDRIVE_PACKET}")
    print(f"onedrive_manuscript={ONEDRIVE_MANUSCRIPT}")
    print(f"eligibility_rows={len(eligibility)}")
    print(f"path_rows={len(path_table)}")


if __name__ == "__main__":
    main()
