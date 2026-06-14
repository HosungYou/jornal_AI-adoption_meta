#!/usr/bin/env python3
"""Build Paper A AI-candidate-only source-trace review packets.

This does not create analytic-input rows. It creates human-review queues that
respect the Paper B reference-standard boundary: AI traces are candidate-only
until a human confirms a source-table decision.
"""
from __future__ import annotations

import csv
import itertools
import json
import re
import shutil
import subprocess
from collections import Counter, defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
RESULT_ROOT = REPO / "data/04_extraction/05_llm_masem_substitution/results"
SOURCE_AUDIT = RESULT_ROOT / "paper_a_human_ai_source_evidence_audit_20260614"
OUT = RESULT_ROOT / "paper_a_ai_candidate_source_trace_20260614"
OUT.mkdir(parents=True, exist_ok=True)
REVIEW_CANDIDATES = SOURCE_AUDIT / "paper_a_latest_human_source_pdf_review_candidates_20260614.csv"
DENSIFY_CANDIDATES = SOURCE_AUDIT / "paper_a_full10_high_coverage_densification_candidates_20260614.csv"
LATEST_INPUT = RESULT_ROOT / "paper_a_latest_human_workbook_audit_20260614/paper_a_latest_human_workbook_direct_r_input_20260614.csv"
SOURCE_REFERENCE_PACKAGE = REPO / "data/04_extraction/07_paper_c_harness_benchmark/private/paper_a_source_reference_package_20260614"
SOURCE_PACKET_DIR = SOURCE_REFERENCE_PACKAGE / "source_packets"
PDF_ROOTS = [
    SOURCE_REFERENCE_PACKAGE / "pdfs",
    Path("/Users/newhosung/Library/CloudStorage/OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity/AI Adoption Meta Analysis - Documents/Meta/AI Adoption/PDFs"),
    Path("/Users/newhosung/Library/CloudStorage/OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity/AI Adoption Meta Analysis - Documents/Meta/AI Adoption/R1/PDFs"),
    Path("/Users/newhosung/Library/CloudStorage/OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity/AI Adoption Meta Analysis - Documents/Meta/AI Adoption/R2/PDFs"),
    Path("/Users/newhosung/Library/CloudStorage/OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity/AI Adoption Meta Analysis - Documents/Meta/AI Adoption/R3/PDFs"),
    Path("/Users/newhosung/Library/CloudStorage/OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity/AI Adoption Meta Analysis - Documents/Meta/AI Adoption/R4/PDFs"),
    REPO / "data/02_screening/pdfs",
]
PAPER_A_FULL10 = ["PE", "EE", "SI", "ATT", "TRU", "ANX", "SE", "BI", "UB", "FC"]
FULL10_PAIRS = {"-".join(sorted(p)) for p in itertools.combinations(PAPER_A_FULL10, 2)}
PD_TEXT = shutil.which("pdftotext")

CONSTRUCT_TERMS = {
    "PE": ["performance expectancy", "perceived usefulness", "usefulness", "useful", "PU", "PE"],
    "EE": ["effort expectancy", "perceived ease of use", "ease of use", "easy to use", "PEOU", "EE"],
    "SI": ["social influence", "subjective norm", "social norm", "SI"],
    "FC": ["facilitating conditions", "facilitating condition", "facilitating", "resources", "support", "FC"],
    "TRU": ["trust", "trustworthiness", "trusting belief", "TRU"],
    "ANX": ["anxiety", "anxious", "fear", "apprehension", "AI anxiety", "ANX"],
    "SE": ["self-efficacy", "self efficacy", "computer self-efficacy", "AI self-efficacy", "efficacy", "SE"],
    "ATT": ["attitude", "attitudes", "attitude toward", "ATT"],
    "BI": ["behavioral intention", "behavioural intention", "intention to use", "usage intention", "continuance intention", "BI"],
    "UB": ["use behavior", "use behaviour", "actual use", "usage behavior", "usage behaviour", "use", "UB"],
}
TABLE_TERMS = ["correlation", "correlations", "pearson", "matrix", "fornell", "larcker", "latent", "construct correlation", "inter-construct", "table"]


def read_csv(path: Path):
    with path.open(newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows, fields):
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)


def pair(a: str, b: str) -> str:
    return "-".join(sorted([str(a).strip(), str(b).strip()]))


def base_study_id(study_id: str) -> str:
    """Map split-sample labels such as S121-1/S121-2/S179b to base PDF ID."""
    m = re.match(r"^(S\d+)", str(study_id).strip())
    return m.group(1) if m else str(study_id).strip()


def find_pdf(study_id: str) -> tuple[Path | None, str]:
    candidates = [str(study_id).strip()]
    base = base_study_id(study_id)
    if base not in candidates:
        candidates.append(base)
    for stem in candidates:
        for root in PDF_ROOTS:
            p = root / f"{stem}.pdf"
            if p.exists():
                return p, stem
    return None, ""


def read_text_file(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return ""


def pdf_text(path: Path | None) -> tuple[str, str]:
    if not path:
        return "", "missing_pdf"
    if not PD_TEXT:
        return "", "missing_pdftotext"
    try:
        r = subprocess.run([PD_TEXT, "-layout", str(path), "-"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=25)
        if r.returncode == 0:
            return r.stdout, "ok"
        return "", f"pdftotext_exit_{r.returncode}"
    except subprocess.TimeoutExpired:
        return "", "pdftotext_timeout"
    except Exception as e:
        return "", f"pdftotext_error_{type(e).__name__}"


def value_variants(value: str) -> list[str]:
    try:
        f = float(str(value).strip())
    except Exception:
        return []
    variants = set()
    for d in [1, 2, 3, 4]:
        s = f"{f:.{d}f}"
        variants.add(s)
        variants.add(s.replace("0.", "."))
        variants.add(s.replace("-0.", "-."))
        variants.add(s.replace(".", ","))
        variants.add(s.replace("0.", ".").replace(".", ","))
    # table extraction sometimes separates decimal point with spaces
    if abs(f) < 1:
        core = f"{abs(f):.2f}".split(".")[1]
        variants.add(core)
    return sorted([v for v in variants if v and v not in {"0", "0.0", ".0"}], key=len, reverse=True)


def normalized(text: str) -> str:
    return re.sub(r"\s+", " ", text).lower()


def exact_value_hit(text: str, variants: list[str]) -> bool:
    if not text:
        return False
    nt = normalized(text)
    for v in variants:
        vv = re.escape(v.lower())
        if re.search(r"(?<![0-9])" + vv + r"(?![0-9])", nt):
            return True
    return False


def broad_value_hit(text: str, variants: list[str]) -> bool:
    if not text:
        return False
    compact = re.sub(r"\s+", "", text).lower()
    for v in variants:
        vv = re.sub(r"\s+", "", v.lower())
        if vv and vv in compact:
            return True
    return False


def term_hits(text: str, terms: list[str]) -> list[str]:
    nt = normalized(text)
    hits = []
    for t in terms:
        if re.search(r"(?<![A-Za-z0-9])" + re.escape(t.lower()) + r"(?![A-Za-z0-9])", nt):
            hits.append(t)
    return hits


def source_location_terms(source_location: str) -> list[str]:
    if not source_location:
        return []
    terms = []
    for m in re.finditer(r"table\s*\d+[A-Za-z]?", source_location, flags=re.I):
        terms.append(m.group(0))
    for m in re.finditer(r"p\.?\s*\d+", source_location, flags=re.I):
        terms.append(m.group(0))
    return terms


def source_location_hits(text: str, source_location: str) -> list[str]:
    return term_hits(text, source_location_terms(source_location))


def status_for_existing(value_hit_pdf, value_hit_packet, broad_hit_pdf, broad_hit_packet, loc_hit, c1_hit, c2_hit, pdf_status, packet_exists):
    if value_hit_pdf or value_hit_packet:
        return "ai_trace_auto_value_visible_exact"
    if broad_hit_pdf or broad_hit_packet:
        return "ai_trace_possible_value_visible_broad_match"
    if loc_hit and c1_hit and c2_hit:
        return "ai_trace_source_location_and_constructs_visible_value_not_found"
    if loc_hit:
        return "ai_trace_source_location_visible_value_not_found"
    if c1_hit and c2_hit:
        return "ai_trace_construct_terms_visible_value_not_found"
    if pdf_status != "ok" and not packet_exists:
        return "ai_trace_source_text_unavailable"
    return "ai_trace_needs_manual_table_review"


def human_action_for_status(status: str) -> str:
    return {
        "ai_trace_auto_value_visible_exact": "human_confirm_source_table_before_any_use",
        "ai_trace_possible_value_visible_broad_match": "human_check_broad_numeric_match_for_false_positive",
        "ai_trace_source_location_and_constructs_visible_value_not_found": "human_open_source_location_and_check_row_column_alignment",
        "ai_trace_source_location_visible_value_not_found": "human_open_source_location_and_check_value_rendering_or_coder_transcription",
        "ai_trace_construct_terms_visible_value_not_found": "human_search_construct_terms_and_correlation_table",
        "ai_trace_source_text_unavailable": "human_materialize_pdf_or_source_packet_then_review",
        "ai_trace_needs_manual_table_review": "human_manual_pdf_table_review_required",
    }.get(status, "human_manual_review_required")


def densification_status(c1_hit, c2_hit, table_hit, pdf_status, packet_exists):
    if not packet_exists and pdf_status != "ok":
        return "ai_trace_source_text_unavailable"
    if c1_hit and c2_hit and table_hit:
        return "possible_densification_source_review_candidate"
    if c1_hit and c2_hit:
        return "possible_construct_pair_present_no_table_anchor"
    if c1_hit or c2_hit:
        return "likely_not_densifiable_one_construct_not_visible"
    return "likely_not_densifiable_construct_pair_not_visible"


latest_rows = read_csv(LATEST_INPUT)
source_lookup = defaultdict(list)
for r in latest_rows:
    source_lookup[(r["study_id"], pair(r["construct_1"], r["construct_2"]), r.get("r_numeric", ""))].append(r)

text_cache = {}
def get_texts(study_id: str):
    if study_id in text_cache:
        return text_cache[study_id]
    base = base_study_id(study_id)
    packet_candidates = [SOURCE_PACKET_DIR / f"{study_id}_source_packet_20260609.txt"]
    if base != study_id:
        packet_candidates.append(SOURCE_PACKET_DIR / f"{base}_source_packet_20260609.txt")
    packet = next((candidate for candidate in packet_candidates if candidate.exists()), packet_candidates[0])
    packet_text = read_text_file(packet) if packet.exists() else ""
    pdf, pdf_stem = find_pdf(study_id)
    ptxt, pstatus = pdf_text(pdf)
    text_cache[study_id] = {
        "base_study_id_used_for_source_text": base,
        "packet_exists": packet.exists(),
        "packet_text": packet_text,
        "packet_file": packet.name if packet.exists() else "",
        "pdf_exists": pdf is not None,
        "pdf_matched_stem": pdf_stem,
        "pdf_path_local_only": str(pdf) if pdf else "",
        "pdf_text_status": pstatus,
        "pdf_text": ptxt,
    }
    return text_cache[study_id]

existing_records = []
for r in read_csv(REVIEW_CANDIDATES):
    sid = r["study_id"]
    pr = r["pair"]
    matched = source_lookup.get((sid, pr, r.get("r_numeric", "")), [])
    source_location = matched[0].get("source_location", "") if matched else ""
    texts = get_texts(sid)
    combined_packet = texts["packet_text"]
    combined_pdf = texts["pdf_text"]
    variants = value_variants(r.get("r_numeric", ""))
    exact_packet = exact_value_hit(combined_packet, variants)
    exact_pdf = exact_value_hit(combined_pdf, variants)
    broad_packet = broad_value_hit(combined_packet, variants)
    broad_pdf = broad_value_hit(combined_pdf, variants)
    loc_hits = sorted(set(source_location_hits(combined_packet, source_location) + source_location_hits(combined_pdf, source_location)))
    c1_hits = sorted(set(term_hits(combined_packet + "\n" + combined_pdf, CONSTRUCT_TERMS.get(r["construct_1"], [r["construct_1"]]))))
    c2_hits = sorted(set(term_hits(combined_packet + "\n" + combined_pdf, CONSTRUCT_TERMS.get(r["construct_2"], [r["construct_2"]]))))
    table_hits = sorted(set(term_hits(combined_packet + "\n" + combined_pdf, TABLE_TERMS)))
    status = status_for_existing(exact_pdf, exact_packet, broad_pdf, broad_packet, bool(loc_hits), bool(c1_hits), bool(c2_hits), texts["pdf_text_status"], texts["packet_exists"])
    existing_records.append({
        "ai_trace_status": status,
        "candidate_status": "ai_candidate_only_existing_human_value_under_review",
        "recommended_human_action": human_action_for_status(status),
        "review_priority": r["review_priority"],
        "study_id": sid,
        "pair": pr,
        "construct_1": r["construct_1"],
        "construct_2": r["construct_2"],
        "human_coded_value_to_check": r.get("r_numeric", ""),
        "sample_size_numeric": r.get("sample_size_numeric", ""),
        "source_file": r.get("source_file", ""),
        "source_location": source_location,
        "source_location_terms_found": ";".join(loc_hits),
        "construct_1_terms_found": ";".join(c1_hits[:8]),
        "construct_2_terms_found": ";".join(c2_hits[:8]),
        "table_terms_found": ";".join(table_hits[:8]),
        "base_study_id_used_for_source_text": texts.get("base_study_id_used_for_source_text", sid),
        "source_packet_exists": "true" if texts["packet_exists"] else "false",
        "source_packet_file": texts["packet_file"],
        "exact_value_found_in_source_packet_text": "true" if exact_packet else "false",
        "broad_value_found_in_source_packet_text": "true" if broad_packet else "false",
        "pdf_exists": "true" if texts["pdf_exists"] else "false",
        "pdf_matched_stem": texts.get("pdf_matched_stem", ""),
        "pdf_text_status": texts["pdf_text_status"],
        "exact_value_found_in_pdf_text": "true" if exact_pdf else "false",
        "broad_value_found_in_pdf_text": "true" if broad_pdf else "false",
        "pdf_path_local_only": texts["pdf_path_local_only"],
        "paper_b_boundary": "candidate_only_not_analytic_input_until_human_confirmed",
    })

existing_fields = [
    "ai_trace_status", "candidate_status", "recommended_human_action", "review_priority", "study_id", "pair", "construct_1", "construct_2", "human_coded_value_to_check", "sample_size_numeric", "source_file", "source_location", "source_location_terms_found", "construct_1_terms_found", "construct_2_terms_found", "table_terms_found", "base_study_id_used_for_source_text", "source_packet_exists", "source_packet_file", "exact_value_found_in_source_packet_text", "broad_value_found_in_source_packet_text", "pdf_exists", "pdf_matched_stem", "pdf_text_status", "exact_value_found_in_pdf_text", "broad_value_found_in_pdf_text", "pdf_path_local_only", "paper_b_boundary"
]
write_csv(OUT / "paper_a_ai_candidate_source_trace_existing_human_values_20260614.csv", existing_records, existing_fields)

# Densification queue for high-coverage studies.
densify_records = []
for row in read_csv(DENSIFY_CANDIDATES):
    sid = row["study_id"]
    texts = get_texts(sid)
    all_text = texts["packet_text"] + "\n" + texts["pdf_text"]
    table_hits = sorted(set(term_hits(all_text, TABLE_TERMS)))
    for pr in [p for p in row["missing_pairs"].split(";") if p]:
        c1, c2 = pr.split("-")
        c1_hits = sorted(set(term_hits(all_text, CONSTRUCT_TERMS.get(c1, [c1]))))
        c2_hits = sorted(set(term_hits(all_text, CONSTRUCT_TERMS.get(c2, [c2]))))
        status = densification_status(bool(c1_hits), bool(c2_hits), bool(table_hits), texts["pdf_text_status"], texts["packet_exists"])
        action = {
            "possible_densification_source_review_candidate": "human_check_source_table_for_missing_pair_value",
            "possible_construct_pair_present_no_table_anchor": "human_search_pdf_for_correlation_or_latent_matrix",
            "likely_not_densifiable_one_construct_not_visible": "human_verify_construct_absence_before_excluding_pair",
            "likely_not_densifiable_construct_pair_not_visible": "human_verify_construct_absence_or mapping mismatch",
            "ai_trace_source_text_unavailable": "human_materialize_pdf_or_source_packet_then_review",
        }.get(status, "human_manual_review_required")
        densify_records.append({
            "ai_trace_status": status,
            "candidate_status": "ai_candidate_only_missing_pair_no_value_added",
            "recommended_human_action": action,
            "study_id": sid,
            "missing_pair": pr,
            "construct_1": c1,
            "construct_2": c2,
            "present_full10_pairs": row["present_full10_pairs"],
            "missing_full10_pairs": row["missing_full10_pairs"],
            "sample_size_values_seen": row["sample_size_values_seen"],
            "candidate_value": "",
            "construct_1_terms_found": ";".join(c1_hits[:8]),
            "construct_2_terms_found": ";".join(c2_hits[:8]),
            "table_terms_found": ";".join(table_hits[:8]),
            "base_study_id_used_for_source_text": texts.get("base_study_id_used_for_source_text", sid),
            "source_packet_exists": "true" if texts["packet_exists"] else "false",
            "source_packet_file": texts["packet_file"],
            "pdf_exists": "true" if texts["pdf_exists"] else "false",
            "pdf_matched_stem": texts.get("pdf_matched_stem", ""),
            "pdf_text_status": texts["pdf_text_status"],
            "pdf_path_local_only": texts["pdf_path_local_only"],
            "paper_b_boundary": "candidate_only_not_analytic_input_until_human_confirmed",
        })

densify_fields = [
    "ai_trace_status", "candidate_status", "recommended_human_action", "study_id", "missing_pair", "construct_1", "construct_2", "present_full10_pairs", "missing_full10_pairs", "sample_size_values_seen", "candidate_value", "construct_1_terms_found", "construct_2_terms_found", "table_terms_found", "base_study_id_used_for_source_text", "source_packet_exists", "source_packet_file", "pdf_exists", "pdf_matched_stem", "pdf_text_status", "pdf_path_local_only", "paper_b_boundary"
]
write_csv(OUT / "paper_a_ai_candidate_full10_densification_trace_20260614.csv", densify_records, densify_fields)

summary_rows = []
def add(metric, value, notes=""):
    summary_rows.append({"metric": metric, "value": str(value), "notes": notes})
add("existing_human_value_review_rows", len(existing_records), "from source/PDF review candidates")
for k, v in Counter(r["ai_trace_status"] for r in existing_records).items():
    add(f"existing_status::{k}", v)
for k, v in Counter(r["review_priority"] for r in existing_records).items():
    add(f"existing_review_priority::{k}", v)
add("densification_missing_pair_rows", len(densify_records), "from high-coverage full10 candidate studies")
for k, v in Counter(r["ai_trace_status"] for r in densify_records).items():
    add(f"densification_status::{k}", v)
add("densification_studies", len({r["study_id"] for r in densify_records}))
add("paper_b_boundary", "candidate_only", "No row is analytic input until human confirmation")
write_csv(OUT / "paper_a_ai_candidate_source_trace_summary_20260614.csv", summary_rows, ["metric", "value", "notes"])

# Human confirmation template intentionally blank for decisions.
confirmation_fields = [
    "human_decision", "human_decision_date", "human_reviewer", "study_id", "pair", "candidate_value_or_human_value", "final_value_if_confirmed", "evidence_type", "source_location_confirmed", "decision_rationale", "promote_to_supplemental_input"
]
confirmation_rows = []
for r in existing_records:
    confirmation_rows.append({
        "human_decision": "", "human_decision_date": "", "human_reviewer": "", "study_id": r["study_id"], "pair": r["pair"], "candidate_value_or_human_value": r["human_coded_value_to_check"], "final_value_if_confirmed": "", "evidence_type": "", "source_location_confirmed": r["source_location"], "decision_rationale": "", "promote_to_supplemental_input": "no"
    })
for r in densify_records:
    if r["ai_trace_status"] in {"possible_densification_source_review_candidate", "possible_construct_pair_present_no_table_anchor"}:
        confirmation_rows.append({
            "human_decision": "", "human_decision_date": "", "human_reviewer": "", "study_id": r["study_id"], "pair": r["missing_pair"], "candidate_value_or_human_value": "", "final_value_if_confirmed": "", "evidence_type": "", "source_location_confirmed": "", "decision_rationale": "", "promote_to_supplemental_input": "no"
        })
write_csv(OUT / "paper_a_human_confirmation_template_from_ai_trace_20260614.csv", confirmation_rows, confirmation_fields)

# Markdown report.
existing_counts = Counter(r["ai_trace_status"] for r in existing_records)
densify_counts = Counter(r["ai_trace_status"] for r in densify_records)
report = [
    "# Paper A AI-Candidate Source Trace Packet",
    "",
    "Date: 2026-06-14",
    "",
    "## LongTable decision boundary",
    "",
    "Decision selected by researcher: `candidate_only_now`.",
    "",
    "AI traces are review evidence only. They do not modify the Paper A analytic input, the Paper B frozen human reference, or any source-anchored adjudicated value. A row can be promoted only after human confirmation in the confirmation template.",
    "",
    "## Existing human-coded values under source review",
    "",
    f"Rows traced: {len(existing_records)}",
    "",
    "| AI trace status | Rows |",
    "| --- | ---: |",
]
for k, v in sorted(existing_counts.items()):
    report.append(f"| `{k}` | {v} |")
report += [
    "",
    "## Full10 missing-pair densification trace",
    "",
    f"Missing-pair rows traced: {len(densify_records)}",
    f"Studies traced: {len({r['study_id'] for r in densify_records})}",
    "",
    "| AI trace status | Rows |",
    "| --- | ---: |",
]
for k, v in sorted(densify_counts.items()):
    report.append(f"| `{k}` | {v} |")
report += [
    "",
    "## Files for researcher review",
    "",
    "- `paper_a_ai_candidate_source_trace_existing_human_values_20260614.csv`",
    "- `paper_a_ai_candidate_full10_densification_trace_20260614.csv`",
    "- `paper_a_human_confirmation_template_from_ai_trace_20260614.csv`",
    "- `paper_a_ai_candidate_source_trace_summary_20260614.csv`",
    "",
    "## How to use this packet",
    "",
    "1. Use the existing-values trace to decide whether a currently coded value is source-confirmed, source-corrected, excluded, or still ambiguous.",
    "2. Use the densification trace to decide whether a missing full10 pair has enough source evidence to justify manual table review.",
    "3. Record human decisions in the confirmation template. Keep `promote_to_supplemental_input=no` unless you personally confirm the source value and evidence type.",
    "4. Only human-confirmed rows may be used to build a supplemental densification input or rerun Paper A MASEM.",
]
(OUT / "PAPER_A_AI_CANDIDATE_SOURCE_TRACE_PACKET_20260614.md").write_text("\n".join(report) + "\n", encoding="utf-8")
print("\n".join(report))
