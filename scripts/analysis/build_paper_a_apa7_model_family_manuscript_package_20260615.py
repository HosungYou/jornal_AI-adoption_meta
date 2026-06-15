#!/usr/bin/env python3
from __future__ import annotations

import csv
import shutil
from pathlib import Path
from textwrap import dedent

ROOT = Path('/Users/newhosung/Academic/2026/AI Adoption Meta Analysis')
DATE = '20260615'
REF_BANK = ROOT / 'paper_a/analysis_strategy/PAPER_A_MODEL_FAMILY_MASEM_REFERENCE_BANK_20260614.csv'
RESULT_DIR = ROOT / 'data/04_extraction/05_llm_masem_substitution/results/paper_a_researcher_approved_s048_inference_figures_manuscript_20260615'
FIT_CSV = RESULT_DIR / 'paper_a_model_family_fit_with_n_20260615.csv'
PATH_CSV = RESULT_DIR / 'paper_a_model_family_structural_paths_ci_inference_20260615.csv'
FIG_DIR = RESULT_DIR / 'figures'
OUT_DIR = ROOT / 'paper_a/manuscript/target_journal/apa7_model_family_full_manuscript_scaffold_20260615'
DATA_OUT_DIR = ROOT / 'data/04_extraction/05_llm_masem_substitution/results/paper_a_apa7_model_family_manuscript_package_20260615'
ONEDRIVE_OUT_DIR = Path('/Users/newhosung/Library/CloudStorage/OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity/AI Adoption Meta Analysis - Documents/05_manuscripts/Paper_A/2026-06-15_apa7_model_family_full_manuscript_scaffold')
CURRENT = ROOT / 'CURRENT.md'

ADDITIONAL_REFS = [
    {
        'category': 'theory',
        'citation': 'Ajzen, I. (1991). The theory of planned behavior. Organizational Behavior and Human Decision Processes, 50(2), 179-211.',
        'doi_or_url': 'https://doi.org/10.1016/0749-5978(91)90020-T',
        'use_in_paper_a': 'Attitude-intention-behavior logic supporting attitude mediation framing.',
        'notes': 'Added for Paper A introduction/theoretical framework draft.',
    },
    {
        'category': 'theory',
        'citation': 'Fishbein, M., & Ajzen, I. (1975). Belief, attitude, intention, and behavior: An introduction to theory and research.',
        'doi_or_url': 'https://people.umass.edu/aizen/f&a1975.html',
        'use_in_paper_a': 'Classic attitude-intention framework for positioning ATT as a mediating evaluative mechanism.',
        'notes': 'Added for Paper A introduction/theoretical framework draft.',
    },
    {
        'category': 'theory',
        'citation': 'Rogers, E. M. (2003). Diffusion of innovations (5th ed.). Free Press.',
        'doi_or_url': 'https://www.worldcat.org/title/52030797',
        'use_in_paper_a': 'Macro adoption/diffusion framing for educational technology uptake.',
        'notes': 'Added for Paper A introduction/theoretical framework draft.',
    },
    {
        'category': 'trust',
        'citation': 'Hancock, P. A., Billings, D. R., Schaefer, K. E., Chen, J. Y. C., De Visser, E. J., & Parasuraman, R. (2011). A meta-analysis of factors affecting trust in human-robot interaction. Human Factors, 53(5), 517-527.',
        'doi_or_url': 'https://doi.org/10.1177/0018720811417254',
        'use_in_paper_a': 'Trust as a central mechanism in human-automation and AI-adjacent adoption contexts.',
        'notes': 'Added for Paper A trust-mechanism positioning.',
    },
    {
        'category': 'mechanism',
        'citation': 'Celik, I. (2023). Towards intelligent-TPACK: An empirical study on teachers\' professional knowledge to ethically integrate artificial intelligence-based tools into education. Computers in Human Behavior, 138, 107468.',
        'doi_or_url': 'https://doi.org/10.1016/j.chb.2022.107468',
        'use_in_paper_a': 'AI-in-education readiness and competence framing for self-efficacy-related mechanisms.',
        'notes': 'Added as an AI-education mechanism reference; team should verify fit before final reference lock.',
    },
]


def read_csv(path: Path):
    with path.open(newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows, fieldnames):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for row in rows:
            w.writerow({k: row.get(k, '') for k in fieldnames})


def md_table(rows, columns):
    if not rows:
        return ''
    header = '| ' + ' | '.join(columns) + ' |'
    sep = '| ' + ' | '.join(['---'] * len(columns)) + ' |'
    body = []
    for row in rows:
        vals = []
        for c in columns:
            v = str(row.get(c, '')).replace('\n', ' ').replace('|', '\\|')
            vals.append(v)
        body.append('| ' + ' | '.join(vals) + ' |')
    return '\n'.join([header, sep] + body)


def as_float(value):
    try:
        if value is None or value == '' or value.upper() == 'NA':
            return None
        return float(value)
    except Exception:
        return None


def fmt3(value):
    x = as_float(value)
    if x is None:
        return 'NA'
    return f'{x:.3f}'.replace('-0.000', '0.000')


def fmt_ci(row):
    lo = fmt3(row.get('ci_lower_95', ''))
    hi = fmt3(row.get('ci_upper_95', ''))
    return f'[{lo}, {hi}]'


def normalize_refs(rows):
    fieldnames = ['category', 'citation', 'doi_or_url', 'use_in_paper_a', 'notes']
    normalized = []
    for row in rows:
        normalized.append({k: row.get(k, '') for k in fieldnames})
    for row in ADDITIONAL_REFS:
        normalized.append(row)
    seen = set()
    deduped = []
    for row in normalized:
        key = (row.get('citation', '').strip().lower(), row.get('doi_or_url', '').strip().lower())
        if key in seen:
            continue
        seen.add(key)
        deduped.append(row)
    return sorted(deduped, key=lambda r: (r.get('category', ''), r.get('citation', '')))


def reference_list(refs):
    lines = []
    for row in sorted(refs, key=lambda r: r.get('citation', '')):
        url = row.get('doi_or_url', '').strip()
        citation = row.get('citation', '').strip()
        if url:
            lines.append(f'{citation} {url}')
        else:
            lines.append(citation)
    return '\n\n'.join(lines)


def grouped_reference_md(refs):
    chunks = ['# Paper A Expanded Reference Bank for Introduction/Theoretical Framework', '', f'Generated: {DATE}', '', 'This bank combines the existing model-family MASEM reference bank with a small number of added theory/mechanism references for the Paper A Introduction and Theoretical Framework draft. The manuscript may cite these sources, but final reference metadata should be checked before journal submission.', '']
    categories = sorted({r.get('category', 'uncategorized') or 'uncategorized' for r in refs})
    for category in categories:
        chunks += [f'## {category}', '']
        rows = [r for r in refs if (r.get('category', '') or 'uncategorized') == category]
        chunks.append(md_table(rows, ['citation', 'doi_or_url', 'use_in_paper_a', 'notes']))
        chunks.append('')
    return '\n'.join(chunks).rstrip() + '\n'


def fit_rows_for_text(fit_rows):
    lines = []
    for row in fit_rows:
        model = row.get('model_family', row.get('model', 'model'))
        n_studies = row.get('n_studies', '') or row.get('k', '')
        n_rows = row.get('n_effect_size_rows', '') or row.get('n_rows', '')
        chi = fmt3(row.get('chisq', row.get('chi_square', '')))
        df = row.get('df', '')
        p = fmt3(row.get('pvalue', row.get('p', '')))
        cfi = fmt3(row.get('CFI', row.get('cfi', '')))
        tli = fmt3(row.get('TLI', row.get('tli', '')))
        rmsea = fmt3(row.get('RMSEA', row.get('rmsea', '')))
        srmr = fmt3(row.get('SRMR', row.get('srmr', '')))
        lines.append(f'{model}: k = {n_studies}, effect-size rows = {n_rows}, chi-square({df}) = {chi}, p = {p}, CFI = {cfi}, TLI = {tli}, RMSEA = {rmsea}, SRMR = {srmr}.')
    return '\n'.join(lines)


def path_summary_rows(path_rows, model_name):
    return [r for r in path_rows if r.get('model_family') == model_name]


def path_narrative(rows):
    supported = [r for r in rows if r.get('inference') == 'supported_ci_excludes_zero']
    includes = [r for r in rows if r.get('inference') == 'ci_includes_zero']
    incomplete = [r for r in rows if r.get('inference') == 'ci_incomplete']
    def label(row):
        return f"{row.get('path', '')} (beta = {fmt3(row.get('estimate', ''))}, 95% CI {fmt_ci(row)})"
    parts = []
    if supported:
        parts.append('Supported paths were ' + '; '.join(label(r) for r in supported) + '.')
    if includes:
        parts.append('Paths whose likelihood-based interval included zero were ' + '; '.join(label(r) for r in includes) + '.')
    if incomplete:
        parts.append('Paths with incomplete interval bounds were retained descriptively rather than interpreted as confirmatory: ' + '; '.join(label(r) for r in incomplete) + '.')
    return ' '.join(parts)


def write_main_manuscript(refs, fit_rows, path_rows):
    core_rows = path_summary_rows(path_rows, 'core7_att_mediation_complete_case')
    trust_rows = path_summary_rows(path_rows, 'trust6_mechanism_complete_case')
    fit_text = fit_rows_for_text(fit_rows)
    refs_text = reference_list(refs)
    manuscript = f"""\
# Paper A APA 7th Professional-Style Manuscript Scaffold: AI Adoption Meta-Analytic Structural Equation Modeling

**Running head:** AI Adoption MASEM  
**Target-journal working fit:** Computers & Education / adjacent educational technology journal  
**Draft status:** Team handoff scaffold, generated {DATE}.  
**Data boundary:** Source-anchored adjudicated human reference standard plus researcher-approved S048 additions. Paper B reference standard remains unchanged.

## Author Note

Author affiliations, acknowledgments, funding, conflicts of interest, data availability, preregistration status, and reproducibility materials will be inserted after the team confirms the final submission venue and repository visibility policy.

## Abstract

Artificial intelligence (AI) adoption research in education has expanded rapidly, but the field remains theoretically fragmented because individual primary studies rarely estimate the full acceptance mechanism implied by technology acceptance and unified acceptance theories. This study synthesizes AI adoption evidence using a model-family meta-analytic structural equation modeling (MASEM) strategy. A full 10-construct acceptance network was retained as the theoretical target to preserve the field-level model implied by technology acceptance, unified theory, trust, anxiety, and self-efficacy traditions. Because no primary study reported a complete 10-construct correlation matrix, empirical MASEM was conducted through complete-case model families that tested structurally defensible submodels. The full10 evidence map showed complete pair-level theoretical coverage across all 45 construct pairs, but no complete-case full10 study. The core7 attitude-mediation model showed excellent fit, and paths from facilitating conditions to attitude, social influence to behavioral intention, attitude to behavioral intention, facilitating conditions to use behavior, and behavioral intention to use behavior were supported by likelihood-based confidence intervals. The trust6 model also showed excellent fit, with supported paths from effort expectancy to behavioral intention, trust to behavioral intention, and behavioral intention to use behavior. Anxiety and self-efficacy remain theoretically important but empirically underidentified in the present source-anchored matrix structure. The study contributes a transparent model-family MASEM template for distinguishing theoretical coverage from estimable structural evidence in AI adoption meta-analysis.

**Keywords:** artificial intelligence adoption, MASEM, technology acceptance, trust, attitude mediation, educational technology

## Introduction

Artificial intelligence is becoming part of routine educational work, including tutoring, writing support, learning analytics, feedback generation, and administrative decision support. This rapid diffusion has produced a broad empirical literature on learners' and educators' intentions to use AI-supported systems, but the evidence base is uneven. Many studies adopt the language of the technology acceptance model (TAM), the unified theory of acceptance and use of technology (UTAUT), trust in automation, self-efficacy, anxiety, or related adoption frameworks; however, primary studies often estimate only selected paths from these theories. As a result, the literature contains many construct-pair correlations but relatively few complete correlation matrices capable of estimating the full acceptance system in one structural model (Davis, 1989; Davis et al., 1989; Venkatesh & Davis, 2000; Venkatesh et al., 2003; Venkatesh et al., 2012).

The central methodological problem is therefore not only whether AI adoption is associated with perceived usefulness, ease of use, social influence, trust, or other constructs. The harder question is whether the accumulated evidence can support a structural account of how those constructs work together. Meta-analytic structural equation modeling (MASEM) is well suited to this question because it synthesizes correlation matrices and tests theoretically specified structural models at the meta-analytic level (Cheung & Chan, 2005; Cheung, 2014, 2015; Jak & Cheung, 2018, 2020, 2024). Yet MASEM requires a defensible matrix structure. When construct coverage is sparse or uneven, a model that is theoretically appealing may be empirically underidentified or unstable. Paper A is designed to make that boundary explicit rather than hide it.

### The Full10 Theoretical Target

The full10 model is not treated as the primary estimable complete-case model. Instead, it is retained as the theoretical target that defines the intended acceptance network for AI adoption in educational contexts. The 10 constructs are perceived usefulness or performance expectancy, perceived ease of use or effort expectancy, social influence, facilitating conditions, attitude, behavioral intention, use behavior, trust, anxiety, and self-efficacy. This target preserves the cumulative logic of TAM, TAM2, UTAUT, UTAUT2, trust-in-automation, and self-efficacy/anxiety traditions. It also prevents the manuscript from narrowing the theory simply because the available matrices are incomplete.

This distinction is important for the team. The full10 result should be written as a theoretical evidence map: all 45 pairwise construct relations are represented somewhere in the source-anchored dataset, which means the field has empirical contact with the complete acceptance network. However, the dataset does not yet contain enough complete 10-construct correlation matrices to estimate full10 MASEM as a primary empirical model. The contribution is therefore diagnostic and theory-preserving: the field has broad pair-level coverage, but not enough complete matrix density for a single omnibus MASEM.

### Attitude Mediation as a Core Acceptance Mechanism

Attitude remains a theoretically meaningful mediator because classic reasoned-action and technology acceptance traditions position evaluative orientation as a mechanism linking beliefs to intention (Fishbein & Ajzen, 1975; Ajzen, 1991; Davis, 1989; Davis et al., 1989). In AI adoption, this matters because learners and educators may recognize a tool as useful or easy to use without necessarily forming a favorable evaluative stance toward using it in learning or teaching. Attitude captures this evaluative translation. It helps explain whether cognitive beliefs about the system become a motivational orientation that supports intention.

The Paper A core7 model uses attitude mediation as the main empirical acceptance mechanism. This route is more defensible than forcing the full10 model because the core7 subset has complete-case matrices and preserves the central TAM/UTAUT chain from beliefs and conditions to attitude, intention, and behavior. The core7 model therefore lets the manuscript test whether the accumulated AI adoption literature supports the classic belief-attitude-intention-behavior logic in a meta-analytic structural framework.

### Trust as a Distinct AI Adoption Mechanism

Trust is not merely another predictor of intention in AI adoption. It is conceptually tied to the delegation, opacity, autonomy, and risk characteristics of AI-supported systems. Users often cannot fully inspect the reasoning process of AI tools, and educational contexts introduce additional stakes related to fairness, accuracy, privacy, assessment integrity, and dependency. Trust in automation and information systems research therefore provides a strong basis for treating trust as a mechanism that may transmit or supplement standard usefulness and ease-of-use pathways (Lee & See, 2004; McKnight et al., 2002; Gefen et al., 2003; Pavlou, 2003; Hancock et al., 2011; Glikson & Woolley, 2020).

The trust6 model contributes by testing whether a trust-centered acceptance mechanism is empirically supported in the available complete-case data. This is especially important for AI because traditional acceptance models may understate the role of perceived reliability, benevolence, competence, and vulnerability. A supported trust-to-intention path would indicate that AI adoption cannot be fully reduced to usefulness or ease-of-use beliefs. Instead, acceptance depends in part on whether users are willing to rely on AI systems under uncertainty.

### Why Anxiety and Self-Efficacy Are Not Yet Confirmed

Anxiety and self-efficacy are theoretically important in AI adoption. Self-efficacy is grounded in social cognitive theory and computer self-efficacy research, where users' perceived capability shapes effort, persistence, and technology use (Bandura, 1977, 1997; Compeau & Higgins, 1995; Compeau et al., 1999; Marakas et al., 1998). Anxiety is similarly important because AI tools may evoke uncertainty, loss-of-control concerns, replacement concerns, performance pressure, or discomfort with algorithmic systems (Parasuraman, 2000; Meuter et al., 2003). In a full theory of AI adoption, both constructs can plausibly function as antecedents, moderators, or mediating mechanisms depending on the model specification.

The present manuscript should not claim that anxiety or self-efficacy are unimportant. The correct claim is narrower: the current source-anchored complete-case matrix structure does not yet allow a defensible primary MASEM that tests anxiety or self-efficacy as mediating mechanisms alongside the full acceptance network. Their status is therefore unresolved, not rejected. This distinction is central for team writing. Anxiety and self-efficacy belong in the full10 theoretical target and should be discussed as next-stage mechanisms, but the Results section should report them as underidentified in the current empirical MASEM route.

### A Model-Family MASEM Strategy

Model-family MASEM is the primary empirical route for Paper A. Instead of treating failure to estimate a full10 model as a failed analysis, the study separates theoretical coverage from empirical estimability. The full10 model defines the comprehensive theory and provides a pairwise evidence map. Complete-case submodels then test structurally meaningful mechanisms that the data can support. This strategy aligns with methodological guidance that MASEM models must respect the correlation structure and missingness pattern of the evidence base, and with broader model-comparison logic that favors theoretically justified, estimable alternatives over a single forced omnibus model (Cheung & Chan, 2005; Cheung, 2014, 2015; Jak & Cheung, 2018, 2020, 2024; Burnham & Anderson, 2002; Landis, 2013; Valentine et al., 2022).

The study makes three contributions. First, it preserves the full AI adoption theory as a transparent 10-construct target rather than reducing the theory to the easiest estimable subset. Second, it tests two empirically supported model families: a core attitude-mediation model and a trust-mechanism model. Third, it documents why anxiety and self-efficacy remain theoretically important but empirically unresolved in the current matrix structure. This framing gives team members a stable foundation for future coding, adjudication, and manuscript development.

## Theoretical Framework

### Acceptance Beliefs, Attitude, Intention, and Use

TAM and UTAUT traditions argue that adoption begins with beliefs about usefulness, ease of use, social expectations, and enabling conditions. These beliefs shape attitude and behavioral intention, which in turn predict actual use (Davis, 1989; Davis et al., 1989; Venkatesh & Davis, 2000; Venkatesh, 2000; Venkatesh et al., 2003, 2012). In educational AI contexts, perceived usefulness can refer to learning support, productivity, personalization, or instructional efficiency. Ease of use can refer to interaction burden, prompt usability, or the effort needed to integrate AI into study or teaching routines. Social influence can capture peer, instructor, institutional, or professional norms. Facilitating conditions can include access, technical support, training, policy guidance, and infrastructure.

Attitude is positioned as a mediator because it represents the evaluative interpretation of these beliefs. A learner or educator may see an AI tool as useful but still develop a negative attitude if the tool feels unreliable, unfair, intrusive, or misaligned with educational values. Conversely, a favorable attitude can translate beliefs into intention even when use behavior depends on institutional conditions. The core7 model operationalizes this framework by testing paths from acceptance beliefs and conditions to attitude, intention, and behavior.

### Trust in AI Systems

Trust becomes more salient as educational technologies become more autonomous and opaque. AI systems may generate recommendations, explanations, assessments, or feedback that users cannot fully verify. Trust therefore captures willingness to rely on a system under uncertainty (Lee & See, 2004; McKnight et al., 2002; Gefen et al., 2003; Pavlou, 2003; Glikson & Woolley, 2020). In the Paper A framework, trust is expected to connect standard acceptance beliefs to intention. Perceived usefulness and ease of use may increase trust because systems that appear competent and manageable are easier to rely on. Social influence may also shape trust when credible others endorse AI tools. Trust may then predict behavioral intention because users must be willing to depend on AI outputs before they incorporate them into consequential learning or teaching decisions.

### Anxiety and Self-Efficacy as Future Mechanisms

Anxiety and self-efficacy are retained in the full10 target because they describe capability and affective threat mechanisms that standard acceptance models may miss. Self-efficacy may precede ease of use, reduce anxiety, or directly influence intention. Anxiety may reduce attitude, trust, or intention, especially when AI tools are perceived as threatening or difficult to control. However, the current empirical route cannot adjudicate these mechanisms because the available complete-case matrices do not yet include enough studies with anxiety/self-efficacy and the required surrounding constructs. The manuscript should therefore treat these constructs as theoretically specified but empirically pending.

### Research Questions

**RQ1:** What does the full10 theoretical evidence map reveal about pairwise construct coverage and complete-case matrix feasibility in AI adoption research?

**RQ2:** Does a core acceptance model centered on attitude mediation fit the source-anchored complete-case data, and which structural paths are supported?

**RQ3:** Does a trust-centered acceptance model fit the source-anchored complete-case data, and which structural paths are supported?

**RQ4:** What do the current MASEM data structure and complete-case constraints imply for testing anxiety and self-efficacy as AI adoption mechanisms?

## Method

### Design

This study used meta-analytic structural equation modeling to synthesize AI adoption evidence. The analysis followed a model-family strategy. The full10 construct network was specified as the theoretical target and used to evaluate pairwise evidence coverage. Empirical structural models were then estimated only for complete-case model families that met the matrix requirements for MASEM. This design separates theory preservation from statistical estimability.

### Literature Search and Eligibility

The broader project screened a large AI adoption evidence base and retained studies that reported quantitative associations among adoption constructs relevant to AI, educational technology, or AI-supported learning and teaching systems. Eligible studies reported sufficient information to extract or reconstruct correlation coefficients among the target constructs. The current Paper A scaffold uses the source-anchored adjudicated human reference standard with researcher-approved S048 additions. The final manuscript should update the PRISMA-style counts directly from the locked screening workbook before submission.

### Coding and Source-Anchored Adjudication

Construct coding harmonized study-specific variables into the full10 construct taxonomy: perceived usefulness/performance expectancy, perceived ease of use/effort expectancy, social influence, facilitating conditions, attitude, behavioral intention, use behavior, trust, anxiety, and self-efficacy. Correlation values were treated as source-anchored when they could be traced to the original article, table, supplementary material, or adjudicated extraction record. Human-coded values form the reference standard for Paper A. AI-assisted additions are not treated as replacements for human judgment; they are included only when researcher-approved and documented as source-traced additions. The current analysis includes the researcher-approved S048 additions and leaves the Paper B reference standard unchanged.

### Data Structure and Model Families

The analysis-ready input contained 836 extracted effect-size rows after the S048 approval update. The full10 theoretical target contains 45 unique construct pairs. All 45 pairwise relations were observed at least once, indicating broad theoretical coverage. However, no primary study supplied a complete 10-construct correlation matrix, so full10 TSSEM was not used as a primary empirical structural model. This limitation is a property of the available matrix structure, not evidence that the full10 theory is invalid.

Two complete-case empirical model families were retained. The core7 attitude-mediation model included perceived usefulness/performance expectancy, perceived ease of use/effort expectancy, social influence, facilitating conditions, attitude, behavioral intention, and use behavior. The trust6 mechanism model included perceived usefulness/performance expectancy, perceived ease of use/effort expectancy, social influence, trust, behavioral intention, and use behavior. Anxiety and self-efficacy remained in the full10 theoretical target but were not estimated as primary MASEM mechanisms because the complete-case matrix structure was insufficient for a defensible model-family estimate.

### Meta-Analytic Structural Equation Modeling

MASEM analyses followed a two-stage structural equation modeling approach. Stage 1 synthesized study-level correlation matrices while accounting for between-study heterogeneity. Stage 2 estimated structural paths from the pooled correlation structure for each complete-case model family. Model fit was evaluated using chi-square, comparative fit index (CFI), Tucker-Lewis index (TLI), root mean square error of approximation (RMSEA), and standardized root mean square residual (SRMR). Structural paths were interpreted using likelihood-based 95% confidence intervals. Because standard errors, z statistics, and p values were not available for all path estimates, inferential language is based on whether likelihood-based confidence intervals excluded zero.

### Reproducibility Materials

The manuscript scaffold, reference bank, model-family figures, fit table, and structural path table are stored in the project repository. The current package is located at `paper_a/manuscript/target_journal/apa7_model_family_full_manuscript_scaffold_20260615/`. The analysis inputs and derived tables are mirrored under `data/04_extraction/05_llm_masem_substitution/results/paper_a_apa7_model_family_manuscript_package_20260615/`.

## Results

### Full10 Theoretical Evidence Map

The full10 theoretical evidence map showed that all 45 construct pairs were observed at least once in the source-anchored dataset. This finding supports the use of full10 as the organizing theoretical target. At the same time, zero studies contained a complete 10-construct matrix. The full10 model therefore provides field-level theoretical coverage evidence but does not provide an estimable complete-case empirical MASEM in the current dataset.

### Model-Family Fit

{fit_text}

Both retained model families showed excellent approximate fit. The fit pattern supports the model-family route as the primary empirical strategy: rather than forcing a sparse full10 matrix, Paper A estimates theoretically meaningful submodels that are compatible with the available complete-case data.

### Core7 Attitude-Mediation Model

The core7 model tested whether the accumulated AI adoption evidence supports a belief/condition-attitude-intention-behavior pathway. {path_narrative(core_rows)} These results support attitude and behavioral intention as central mechanisms in the AI adoption process while also showing that not all belief-to-attitude or belief-to-intention links are equally stable in the current complete-case evidence base.

### Trust6 Mechanism Model

The trust6 model tested whether trust operates as a distinct acceptance mechanism in the available AI adoption evidence. {path_narrative(trust_rows)} The supported trust-to-intention path indicates that AI adoption cannot be reduced to usefulness and effort beliefs alone. Trust appears to capture an additional reliance mechanism that is theoretically appropriate for AI systems.

### Anxiety and Self-Efficacy Boundary

Anxiety and self-efficacy could not be tested as confirmed mediating mechanisms in the current primary MASEM route. This result should be interpreted as a data-structure limitation rather than a theoretical rejection. The constructs remain part of the full10 theoretical target, but additional source-level correlation extraction or future primary studies with fuller matrices are needed before their mediating role can be evaluated with the same confidence as the core7 and trust6 families.

## Discussion: Writing Scaffold for Team Completion

The Discussion should develop four points. First, Paper A contributes a transparent distinction between theoretical coverage and estimable structural evidence. Second, the core7 findings provide meta-analytic support for an attitude/intention pathway in AI adoption. Third, the trust6 findings show that trust is a necessary AI-specific mechanism rather than a peripheral add-on. Fourth, the anxiety/self-efficacy boundary identifies a concrete agenda for future extraction and primary-study reporting.

The manuscript should avoid claiming that full10 MASEM was successfully estimated. It should also avoid claiming that anxiety or self-efficacy are unsupported. The accurate claim is that full10 has complete pair-level coverage but no complete-case omnibus model, whereas core7 and trust6 are the current empirical model-family results. Anxiety and self-efficacy are theoretically retained but empirically unresolved.

## Tables and Figures to Insert

**Table 1.** Full10 construct taxonomy and theoretical role.  
**Table 2.** Model-family data structure, complete-case study counts, and fit indices.  
**Table 3.** Structural path estimates and likelihood-based confidence intervals.  
**Figure 1.** Full10 theoretical evidence map.  
**Figure 2.** Core7 attitude-mediation MASEM path diagram.  
**Figure 3.** Trust6 mechanism MASEM path diagram.

## References

{refs_text}
"""
    (OUT_DIR / f'PAPER_A_APA7_MODEL_FAMILY_FULL_MANUSCRIPT_SCAFFOLD_{DATE}.md').write_text(manuscript, encoding='utf-8')
    (DATA_OUT_DIR / f'PAPER_A_APA7_MODEL_FAMILY_FULL_MANUSCRIPT_SCAFFOLD_{DATE}.md').write_text(manuscript, encoding='utf-8')


def write_team_brief(refs):
    brief = f"""\
# Paper A 팀 작업 브리프: Introduction, Theoretical Framework, Methods, Results

생성일: {DATE}  
현재 상태: 팀원이 바로 이어서 쓸 수 있는 manuscript scaffold 생성 완료  
핵심 원칙: full10은 theoretical target/evidence map이고, empirical MASEM은 core7/trust6 model-family로 쓴다.

## 1. 현재 확정된 주장 경계

- full10은 이론적으로 포기하지 않는다. TAM/UTAUT, trust, anxiety, self-efficacy까지 포함한 AI adoption 전체 이론 네트워크다.
- full10은 현재 primary empirical MASEM 결과가 아니다. 모든 45개 pair는 관찰되었지만 complete-case 10-construct matrix가 없어서 omnibus full10 MASEM은 주 결과로 쓰면 안 된다.
- core7은 attitude mediation을 검증하는 현재 primary empirical model family다.
- trust6는 AI adoption에서 trust mechanism을 검증하는 현재 primary empirical model family다.
- anxiety/self-efficacy는 이론적으로 중요하지만 현재 complete-case MASEM에서 매개 메커니즘으로 확인되지 않았다. “중요하지 않다”가 아니라 “현재 matrix 구조로는 검증되지 않았다”라고 써야 한다.

## 2. full10 theoretical target의 의미

full10은 AI adoption 이론의 전체 구조를 보존하기 위한 target이다. 개별 논문들이 일부 construct만 보고했기 때문에 바로 full SEM을 추정할 수는 없지만, 전체 field가 어떤 관계들을 다루고 있는지 보여주는 evidence map 역할을 한다. 따라서 Introduction에서는 full10을 “우리가 실제로 추정한 모델”이 아니라 “이론적으로 보존해야 하는 전체 acceptance network”로 설명해야 한다.

## 3. trust mechanism의 기여

Trust는 AI adoption에서 독립적인 메커니즘이다. AI는 opaque/autonomous system이기 때문에 사용자는 단순히 유용하고 쉬운지뿐 아니라, 그 시스템을 신뢰하고 의존할 수 있는지를 판단한다. trust6 결과에서 trust -> behavioral intention 경로가 지지되므로, Paper A는 AI adoption 이론이 classic TAM/UTAUT만으로 충분하지 않고 trust mechanism을 포함해야 한다고 주장할 수 있다.

## 4. attitude mediation의 기여

Attitude는 belief와 intention 사이의 evaluative translation이다. perceived usefulness/ease, social influence, facilitating conditions가 바로 intention으로만 가는 것이 아니라, AI 사용에 대한 전반적 평가를 거쳐 intention으로 이어질 수 있다. core7 결과는 attitude -> behavioral intention 및 behavioral intention -> use behavior를 지지하므로, attitude mediation을 Paper A의 중심 이론 기여 중 하나로 쓸 수 있다.

## 5. anxiety/self-efficacy가 아직 확인되지 않은 이유

현재 문제는 construct가 의미 없어서가 아니라 matrix density가 부족해서다. anxiety와 self-efficacy는 full10 target에는 들어가지만, 이들을 포함해 매개 경로까지 검증할 complete-case study set이 부족하다. 팀원은 이 부분을 limitation이자 future research agenda로 써야 한다.

## 6. Methods/Results 작성 시 금지 문장

- “The full10 MASEM was supported.” 금지.
- “Anxiety and self-efficacy were not important.” 금지.
- “AI values replaced human coding.” 금지.
- “All paths were significant.” 금지. 현재 inference는 likelihood-based 95% CI 기준이다.

## 7. 권장 문장

- “The full10 model was retained as a theoretical evidence map rather than estimated as the primary complete-case MASEM.”
- “The core7 and trust6 models constituted the primary empirical model-family MASEM route.”
- “Anxiety and self-efficacy remain theoretically specified but empirically underidentified in the current complete-case matrix structure.”
- “Path-level interpretation relied on likelihood-based confidence intervals because standard errors and p values were unavailable for several estimates.”

## 8. 팀원이 우선 보강할 부분

1. PRISMA/search/screening 숫자를 locked workbook에서 최종 확인.
2. Introduction에 AI-in-education 최근 연구를 더 추가.
3. Theoretical Framework에서 construct별 operational definition table 작성.
4. Discussion에서 full10 coverage vs empirical model-family distinction을 강조.
5. References APA 7th metadata 최종 점검.

## 9. 레퍼런스 클러스터

### TAM/UTAUT 및 acceptance theory

Davis (1989); Davis et al. (1989); Venkatesh and Davis (2000); Venkatesh (2000); Venkatesh et al. (2003, 2012); King and He (2006); Schepers and Wetzels (2007); Yousafzai et al. (2007); Dwivedi et al. (2019); Scherer et al. (2019).

### Attitude mediation

Fishbein and Ajzen (1975); Ajzen (1991); Davis (1989); Davis et al. (1989); TAM/TAM2/UTAUT lineage.

### Trust mechanism

Lee and See (2004); McKnight et al. (2002); Gefen et al. (2003); Pavlou (2003); Hancock et al. (2011); Glikson and Woolley (2020).

### Anxiety/self-efficacy

Bandura (1977, 1997); Compeau and Higgins (1995); Compeau et al. (1999); Marakas et al. (1998); Parasuraman (2000); Meuter et al. (2003).

### MASEM/model-family method

Cheung and Chan (2005); Cheung (2014, 2015); Jak and Cheung (2018, 2020, 2024); Valentine et al. (2022); Landis (2013); Burnham and Anderson (2002).
"""
    (OUT_DIR / f'TEAM_WRITING_BRIEF_PAPER_A_INTRO_THEORY_METHODS_RESULTS_{DATE}_KO.md').write_text(brief, encoding='utf-8')
    (DATA_OUT_DIR / f'TEAM_WRITING_BRIEF_PAPER_A_INTRO_THEORY_METHODS_RESULTS_{DATE}_KO.md').write_text(brief, encoding='utf-8')


def write_readme():
    readme = f"""\
# Paper A APA 7 Model-Family Manuscript Package

Generated: {DATE}

## Purpose

This package gives the Paper A team a submission-oriented scaffold for Introduction, Theoretical Framework, Methods, and Results. It uses the current source-anchored model-family MASEM route:

- `full10`: theoretical target and evidence map.
- `core7`: empirical attitude-mediation complete-case MASEM.
- `trust6`: empirical trust-mechanism complete-case MASEM.
- `anxiety/self-efficacy`: retained in theory, not confirmed as mediating mechanisms in the current complete-case data structure.

## Main files

- `PAPER_A_APA7_MODEL_FAMILY_FULL_MANUSCRIPT_SCAFFOLD_{DATE}.md`
- `TEAM_WRITING_BRIEF_PAPER_A_INTRO_THEORY_METHODS_RESULTS_{DATE}_KO.md`
- `PAPER_A_EXPANDED_REFERENCE_BANK_{DATE}.csv`
- `PAPER_A_EXPANDED_REFERENCE_BANK_{DATE}.md`
- `tables/paper_a_model_family_fit_with_n_20260615.csv`
- `tables/paper_a_model_family_structural_paths_ci_inference_20260615.csv`
- `figures/figure_1_full10_theoretical_evidence_map_heatmap_ci_20260615.png`
- `figures/figure_2_core7_att_mediation_masem_path_ci_20260615.png`
- `figures/figure_3_trust6_mechanism_masem_path_ci_20260615.png`

## Claims that are safe now

- The full10 target has all 45 construct pairs observed at least once.
- The full10 target has zero complete-case 10-construct studies, so it is not the primary empirical MASEM.
- Core7 and trust6 are the current empirical model-family MASEM results.
- Anxiety and self-efficacy are theoretically retained but empirically underidentified in the current complete-case route.

## Claims still needing team verification

- Final PRISMA/search/screening counts.
- Final target-journal formatting requirements.
- Final APA 7th reference metadata.
- Whether to convert this Markdown scaffold into a tracked DOCX submission draft.
"""
    (OUT_DIR / f'README_PAPER_A_APA7_MODEL_FAMILY_MANUSCRIPT_PACKAGE_{DATE}.md').write_text(readme, encoding='utf-8')
    (DATA_OUT_DIR / f'README_PAPER_A_APA7_MODEL_FAMILY_MANUSCRIPT_PACKAGE_{DATE}.md').write_text(readme, encoding='utf-8')


def copy_support_files():
    (OUT_DIR / 'tables').mkdir(parents=True, exist_ok=True)
    (OUT_DIR / 'figures').mkdir(parents=True, exist_ok=True)
    (DATA_OUT_DIR / 'tables').mkdir(parents=True, exist_ok=True)
    (DATA_OUT_DIR / 'figures').mkdir(parents=True, exist_ok=True)
    for src in [FIT_CSV, PATH_CSV, RESULT_DIR / 'paper_a_model_family_fit_with_n_20260615.md', RESULT_DIR / 'paper_a_model_family_structural_paths_ci_inference_20260615.md']:
        if src.exists():
            shutil.copy2(src, OUT_DIR / 'tables' / src.name)
            shutil.copy2(src, DATA_OUT_DIR / 'tables' / src.name)
    for src in FIG_DIR.glob('figure_*_20260615.*'):
        shutil.copy2(src, OUT_DIR / 'figures' / src.name)
        shutil.copy2(src, DATA_OUT_DIR / 'figures' / src.name)


def mirror_to_onedrive():
    if ONEDRIVE_OUT_DIR.exists():
        shutil.rmtree(ONEDRIVE_OUT_DIR)
    ONEDRIVE_OUT_DIR.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(OUT_DIR, ONEDRIVE_OUT_DIR)


def update_current():
    marker = f"""\
\n## 2026-06-15 Paper A APA7 model-family manuscript scaffold\n\n- Generated a submission-oriented Paper A scaffold for Introduction, Theoretical Framework, Methods, and Results.\n- Location: `paper_a/manuscript/target_journal/apa7_model_family_full_manuscript_scaffold_20260615/`.\n- Mirrored OneDrive package: `AI Adoption Meta Analysis - Documents/05_manuscripts/Paper_A/2026-06-15_apa7_model_family_full_manuscript_scaffold/`.\n- Analysis boundary: full10 remains the theoretical target/evidence map; core7 and trust6 remain empirical model-family MASEM; anxiety/self-efficacy remain theoretically specified but empirically underidentified in the current complete-case route.\n- Next recommended work: team verifies PRISMA counts and APA 7 references, then expands Discussion/Limitations and optionally converts the scaffold to DOCX.\n"""
    text = CURRENT.read_text(encoding='utf-8') if CURRENT.exists() else '# Current Project State\n'
    if '2026-06-15 Paper A APA7 model-family manuscript scaffold' not in text:
        CURRENT.write_text(text.rstrip() + '\n' + marker, encoding='utf-8')


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    DATA_OUT_DIR.mkdir(parents=True, exist_ok=True)
    refs = normalize_refs(read_csv(REF_BANK))
    fit_rows = read_csv(FIT_CSV)
    path_rows = read_csv(PATH_CSV)
    fieldnames = ['category', 'citation', 'doi_or_url', 'use_in_paper_a', 'notes']
    write_csv(OUT_DIR / f'PAPER_A_EXPANDED_REFERENCE_BANK_{DATE}.csv', refs, fieldnames)
    write_csv(DATA_OUT_DIR / f'PAPER_A_EXPANDED_REFERENCE_BANK_{DATE}.csv', refs, fieldnames)
    ref_md = grouped_reference_md(refs)
    (OUT_DIR / f'PAPER_A_EXPANDED_REFERENCE_BANK_{DATE}.md').write_text(ref_md, encoding='utf-8')
    (DATA_OUT_DIR / f'PAPER_A_EXPANDED_REFERENCE_BANK_{DATE}.md').write_text(ref_md, encoding='utf-8')
    write_main_manuscript(refs, fit_rows, path_rows)
    write_team_brief(refs)
    write_readme()
    copy_support_files()
    mirror_to_onedrive()
    update_current()
    print(f'Wrote manuscript package: {OUT_DIR}')
    print(f'Wrote data package: {DATA_OUT_DIR}')
    print(f'Mirrored OneDrive package: {ONEDRIVE_OUT_DIR}')


if __name__ == '__main__':
    main()
