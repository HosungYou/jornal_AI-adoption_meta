#!/usr/bin/env python3
"""Build Paper A remaining C-tier full10 batch triage after S121 ANX rejection.

This script keeps AI/source-trace rows as review evidence only. It does not create
analytic MASEM input. Rows move to supplemental input only after researcher
confirmation of source value, evidence type, and source location.
"""
from __future__ import annotations

from collections import Counter, OrderedDict
from pathlib import Path
import csv
import re
import shutil
import zipfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "data/04_extraction/05_llm_masem_substitution/results/paper_a_ai_candidate_source_trace_20260614"
TRIAGE = ROOT / "data/04_extraction/05_llm_masem_substitution/results/paper_a_broader_ai_candidate_triage_20260614/paper_a_broader_ai_candidate_construct_support_triage_20260614.csv"
QUEUE = BASE / "paper_a_C_full10_pair_ordered_densification_review_queue_20260614.csv"
TEMPLATE = BASE / "paper_a_human_confirmation_template_from_ai_trace_20260614.csv"
PAIR07_CSV = BASE / "paper_a_C_pair07_ANX_PE_source_evidence_draft_20260614.csv"
PAIR07_LOG = BASE / "PAPER_A_C_PAIR07_ANX_PE_REVIEW_LOG_KO_20260614.md"
ORDERED_LOG = BASE / "PAPER_A_C_FULL10_ORDERED_REVIEW_LOG_KO_20260614.md"
WORKBOOK = BASE / "PAPER_A_AI_CANDIDATE_REVIEW_WORKBOOK_20260614.xlsx"
CURRENT = ROOT / "CURRENT.md"

OUT_BATCH = BASE / "paper_a_C_remaining_full10_batch_triage_20260615.csv"
OUT_SHORT = BASE / "paper_a_C_remaining_full10_batch_review_shortlist_20260615.csv"
OUT_LOG = BASE / "PAPER_A_C_REMAINING_FULL10_BATCH_TRIAGE_KO_20260615.md"

REVIEWED_LABELS = {"03_FC-PE", "04_ATT-PE", "05_PE-SE", "06_PE-TRU", "07_ANX-PE"}

S048_VALUES = {
    "BI-FC": ("0.424", "INT x FC"),
    "BI-PE": ("0.659", "INT x PE"),
    "BI-SI": ("0.626", "INT x SI"),
    "EE-UB": ("0.398", "EE x USE"),
    "FC-UB": ("0.340", "FC x USE"),
    "SI-UB": ("0.589", "SI x USE"),
    "TRU-UB": ("0.442", "TRU x USE"),
}
S048_LOCATOR = "S048_doc1 page 13 chunk 1; Table 2 descriptive statistics and correlations"
S004_REJECT_PAIRS = {"BI-SE", "EE-SE", "FC-SE", "SE-SI", "SE-TRU", "SE-UB"}
S072_MAPPING_AUDIT_PAIRS = {"ANX-ATT", "ATT-UB"}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)


def label_order(rows: list[dict[str, str]]) -> dict[str, int]:
    order: dict[str, int] = {}
    for row in rows:
        lab = row["full10_pair_order_label"]
        if lab not in order:
            order[lab] = int(row.get("full10_pair_order") or 999)
    return order


def update_pair07_rejection() -> None:
    rows = read_csv(PAIR07_CSV)
    fields = list(rows[0].keys())
    for row in rows:
        if row.get("study_id") in {"S121-1", "S121-2"} and row.get("missing_pair") == "ANX-PE":
            row["ANX_status"] = "rejected_mapping_threat_appraisal_not_ANX"
            row["preliminary_decision"] = "do_not_promote_researcher_rejected_threat_appraisal_to_ANX"
            row["promote_to_supplemental_input"] = "no"
            row["confidence"] = "high"
            row["researcher_action"] = "none_rejected_by_researcher_20260615"
            row["rationale_ko"] = (
                row["rationale_ko"].split(" The value is source-visible")[0]
                + " The value remains source-visible, but the researcher rejected mapping threat appraisal to full10 ANX on 2026-06-15; do not promote."
            )
    write_csv(PAIR07_CSV, rows, fields)

    text = PAIR07_LOG.read_text(encoding="utf-8")
    block = """
## 2026-06-15 researcher decision

- Researcher decision: do not approve `threat appraisal` -> full10 `ANX`.
- Consequence: `S121-1 ANX-PE=-0.23` and `S121-2 ANX-PE=-0.08` remain source-visible review evidence but are not promoted to Paper A supplemental input.
- Final pair 07 outcome after researcher decision: immediate promotion 0, conditional candidates 0, promoted rows 0.
"""
    if "2026-06-15 researcher decision" not in text:
        PAIR07_LOG.write_text(text.rstrip() + "\n\n" + block.lstrip(), encoding="utf-8")


def build_batch_rows() -> tuple[list[dict[str, str]], list[dict[str, str]], dict[str, int]]:
    queue_rows = read_csv(QUEUE)
    triage_rows = read_csv(TRIAGE)
    order = label_order(queue_rows)
    queue_key_to_label = {(r["study_id"], r["missing_pair"]): r["full10_pair_order_label"] for r in queue_rows}
    queue_key_to_source_file = {(r["study_id"], r["missing_pair"]): r["source_packet_file"] for r in queue_rows}
    triage_by_key = {(r["study_id"], r["missing_pair"]): r for r in triage_rows}

    fields = [
        "full10_pair_order_label",
        "study_id",
        "missing_pair",
        "batch_decision_class",
        "candidate_value",
        "candidate_value_metric",
        "source_packet_file",
        "source_locator",
        "construct_mapping_issue",
        "promote_to_supplemental_input",
        "researcher_action",
        "rationale_ko",
        "original_triage_class",
        "construct_1_human_supported",
        "construct_2_human_supported",
        "supported_constructs_in_human_reference",
        "paper_b_boundary",
    ]

    batch_rows: list[dict[str, str]] = []
    shortlist: list[dict[str, str]] = []
    for q in queue_rows:
        lab = q["full10_pair_order_label"]
        if lab in REVIEWED_LABELS:
            continue
        key = (q["study_id"], q["missing_pair"])
        t = triage_by_key.get(key, {})
        original = t.get("triage_class", "not_found_in_construct_support_triage")
        value = ""
        metric = ""
        locator = ""
        mapping_issue = ""
        promote = "no"
        action = "do_not_add_unless_reopened_by_source_evidence"
        decision = original
        rationale = ""

        if q["study_id"] == "S004" and q["missing_pair"] in S004_REJECT_PAIRS:
            decision = "excluded_researcher_rejected_PKC_to_SE_mapping"
            mapping_issue = "PKC/perceived knowledge of ChatGPT is not approved as full10 SE"
            action = "no_action_researcher_mapping_rejected"
            rationale = "S004 source table uses PKC, not an approved full10 SE construct. Researcher previously rejected PKC mapping; do not promote SE-pair candidates."
        elif q["study_id"] == "S048" and q["missing_pair"] in S048_VALUES:
            value, cell = S048_VALUES[q["missing_pair"]]
            metric = "source_reported_pearson_correlation_matrix"
            locator = f"{S048_LOCATOR}; {cell}"
            decision = "numeric_cell_candidate_pending_researcher_confirmation"
            promote = "pending_researcher_confirmation"
            action = "researcher_confirm_source_value_evidence_type_and_location"
            rationale = "Both constructs are human/frozen-supported and Table 2 reports a source-visible Pearson r cell. Keep as review evidence until researcher confirms value, evidence type, and source location."
        elif q["study_id"] == "S072" and q["missing_pair"] in S072_MAPPING_AUDIT_PAIRS:
            decision = "construct_mapping_audit_required_not_promote"
            mapping_issue = "source table labels are PC/RA/VU rather than direct full10 ANX/ATT/UB labels"
            locator = "S072_doc1 page 10 chunk 1; Table 2 Fornell-Larcker discriminant validity"
            action = "manual_construct_mapping_audit_before_any_value_entry"
            rationale = "Existing support gate flags this as a priority, but source labels require construct-mapping audit before any numeric cell can be treated as full10 ANX/ATT/UB. Do not promote now."
        elif original == "source_review_priority_both_constructs_human_supported":
            decision = "source_review_priority_pending_pdf_numeric_cell"
            promote = "pending_source_review"
            action = "review_pdf_for_numeric_cell_and_add_if_confirmed"
            rationale = "Both constructs are human/frozen-supported but no batch-safe value was extracted in this pass."
        elif original == "already_in_human_or_frozen_reference":
            decision = "already_in_human_or_frozen_reference"
            action = "do_not_add_duplicate"
            rationale = "Exact unordered pair is already present in latest/frozen human-supported rows."
        elif original == "likely_false_positive_no_construct_human_supported":
            decision = "excluded_no_construct_human_supported"
            rationale = "Neither construct is human/frozen-supported for this study; likely AI term-hit overreach or source mismatch."
        elif original == "likely_false_positive_one_construct_not_human_supported":
            decision = "excluded_one_construct_not_human_supported"
            rationale = "Only one construct is human/frozen-supported for this study; do not add unless source adjudication reopens construct mapping."
        else:
            decision = "defer_unclassified"
            action = "manual_review_required"
            rationale = "Candidate did not match the expected triage classes; keep out of supplemental input."

        out = {
            "full10_pair_order_label": lab,
            "study_id": q["study_id"],
            "missing_pair": q["missing_pair"],
            "batch_decision_class": decision,
            "candidate_value": value,
            "candidate_value_metric": metric,
            "source_packet_file": queue_key_to_source_file.get(key, q.get("source_packet_file", "")),
            "source_locator": locator,
            "construct_mapping_issue": mapping_issue,
            "promote_to_supplemental_input": promote,
            "researcher_action": action,
            "rationale_ko": rationale,
            "original_triage_class": original,
            "construct_1_human_supported": t.get("construct_1_human_supported", ""),
            "construct_2_human_supported": t.get("construct_2_human_supported", ""),
            "supported_constructs_in_human_reference": t.get("supported_constructs_in_human_reference", ""),
            "paper_b_boundary": "candidate_only_not_analytic_input_until_human_confirmed",
        }
        batch_rows.append(out)
        if out["batch_decision_class"] == "numeric_cell_candidate_pending_researcher_confirmation":
            shortlist.append(out)

    batch_rows.sort(key=lambda r: (order.get(r["full10_pair_order_label"], 999), r["study_id"], r["missing_pair"]))
    shortlist.sort(key=lambda r: (r["study_id"], r["missing_pair"]))
    write_csv(OUT_BATCH, batch_rows, fields)
    write_csv(OUT_SHORT, shortlist, fields)
    return batch_rows, shortlist, Counter(r["batch_decision_class"] for r in batch_rows)


def update_template(shortlist: list[dict[str, str]]) -> None:
    rows = read_csv(TEMPLATE)
    fields = list(rows[0].keys())
    short_by_key = {(r["study_id"], r["missing_pair"]): r for r in shortlist}
    for row in rows:
        key = (row.get("study_id", ""), row.get("pair", ""))
        if key in {("S121-1", "ANX-PE"), ("S121-2", "ANX-PE")}: 
            row["human_decision"] = "reject"
            row["human_decision_date"] = "2026-06-15"
            row["human_reviewer"] = "researcher"
            row["final_value_if_confirmed"] = ""
            row["decision_rationale"] = "Researcher rejected mapping threat appraisal to full10 ANX; source-visible value not promoted."
            row["promote_to_supplemental_input"] = "no"
        elif key in short_by_key:
            s = short_by_key[key]
            row["candidate_value_or_human_value"] = s["candidate_value"]
            row["final_value_if_confirmed"] = ""
            row["evidence_type"] = s["candidate_value_metric"]
            row["source_location_confirmed"] = s["source_locator"]
            row["decision_rationale"] = "Batch-safe source-visible candidate; researcher must confirm source value, evidence type, and source location before promotion."
            row["promote_to_supplemental_input"] = "pending_researcher_confirmation"
        elif row.get("study_id") == "S004" and row.get("pair") in S004_REJECT_PAIRS:
            row["decision_rationale"] = "Do not promote: PKC/perceived knowledge is not approved as full10 SE."
            row["promote_to_supplemental_input"] = "no"
        elif row.get("study_id") == "S072" and row.get("pair") in S072_MAPPING_AUDIT_PAIRS:
            row["decision_rationale"] = "Do not promote now: source labels require construct-mapping audit before treating cells as full10 ANX/ATT/UB."
            row["promote_to_supplemental_input"] = "no"
    write_csv(TEMPLATE, rows, fields)


def write_logs(batch_rows: list[dict[str, str]], shortlist: list[dict[str, str]], counts: dict[str, int]) -> None:
    pair_counts: OrderedDict[str, int] = OrderedDict()
    for row in batch_rows:
        pair_counts[row["full10_pair_order_label"]] = pair_counts.get(row["full10_pair_order_label"], 0) + 1

    short_lines = []
    for r in shortlist:
        short_lines.append(
            f"| {r['study_id']} | {r['missing_pair']} | {r['candidate_value']} | {r['candidate_value_metric']} | {r['source_locator']} | pending researcher confirmation |"
        )
    count_lines = [f"- {k}: {v}" for k, v in sorted(counts.items())]
    pair_lines = [f"- {k}: {v}" for k, v in pair_counts.items()]
    log = f"""# Paper A/C remaining full10 batch triage

Date: 2026-06-15

## Researcher decision carried forward

- `S121 threat appraisal -> full10 ANX`: not approved by researcher.
- Consequence: `S121-1 ANX-PE=-0.23` and `S121-2 ANX-PE=-0.08` are rejected for supplemental input despite being source-visible in Figure 2.

## Batch scope

- Reviewed pair-by-pair work already completed: `03_FC-PE`, `04_ATT-PE`, `05_PE-SE`, `06_PE-TRU`, `07_ANX-PE`.
- Remaining C-tier queue rows triaged in this batch: {len(batch_rows)}
- Remaining pair labels triaged: {len(pair_counts)}
- Rule: no value enters Paper A supplemental input until researcher confirms source value, evidence type, and source location.

## Batch decision counts

{chr(10).join(count_lines)}

## Remaining pair-label coverage

{chr(10).join(pair_lines)}

## Source-visible numeric-cell shortlist

These are the only rows from the remaining batch with a batch-safe numeric cell candidate. They are not yet supplemental input.

| study_id | pair | value | evidence type | source locator | status |
| --- | --- | --- | --- | --- | --- |
{chr(10).join(short_lines)}

## Closed or held groups

- `S004` SE-related priority rows are closed for now because they depend on `PKC/perceived knowledge -> SE`, which the researcher did not approve.
- `S072` priority rows are held for construct-mapping audit because the source matrix labels are `PC`, `RA`, and `VU`, not direct full10 `ANX`, `ATT`, or `UB` labels.
- The large majority of remaining rows are excluded at construct-support gate: at least one target construct is not human/frozen-supported for that study.

## Output files

- `paper_a_C_remaining_full10_batch_triage_20260615.csv`
- `paper_a_C_remaining_full10_batch_review_shortlist_20260615.csv`
- Updated confirmation template: `paper_a_human_confirmation_template_from_ai_trace_20260614.csv`
- Updated workbook: `PAPER_A_AI_CANDIDATE_REVIEW_WORKBOOK_20260614.xlsx`

## Next analytic condition

Do not rerun model-family MASEM from these rows until the researcher explicitly confirms the seven `S048` source-visible values or rejects them.
"""
    OUT_LOG.write_text(log, encoding="utf-8")

    ordered = ORDERED_LOG.read_text(encoding="utf-8")
    append = f"""
## 2026-06-15 batch triage after S121 ANX rejection

- Researcher rejected `threat appraisal` -> full10 `ANX`; pair 07 final promoted rows remain 0.
- Remaining C-tier full10 queue rows triaged at once: {len(batch_rows)} rows across {len(pair_counts)} pair labels.
- Batch-safe source-visible numeric-cell candidates: {len(shortlist)} rows, all from `S048` Table 2.
- Rows closed/held without promotion: S004 SE-related rows closed because `PKC -> SE` is not approved; S072 rows held for construct-mapping audit; all one/no-human-supported-construct rows remain excluded unless reopened by source adjudication.
- Next action: researcher confirms or rejects the seven S048 source-visible values before any supplemental input or model-family MASEM rerun.
"""
    if "2026-06-15 batch triage after S121 ANX rejection" not in ordered:
        ORDERED_LOG.write_text(ordered.rstrip() + "\n\n" + append.lstrip(), encoding="utf-8")

    current = CURRENT.read_text(encoding="utf-8")
    current = re.sub(
        r"- Next action: .*",
        "- Next action: Researcher confirms or rejects the seven S048 source-visible numeric-cell candidates before any supplemental input or model-family MASEM rerun.",
        current,
        count=1,
    )
    current = current.replace(
        "- For S121, should `threat appraisal` be accepted as full10 `ANX` for the conditional ANX-PE values?\n",
        "",
    )
    current = current.replace(
        "## Pending Decision Questions\n- Researcher checkpoint pending: decide whether S121 `threat appraisal` can be mapped to full10 `ANX` for conditional ANX-PE supplemental input.",
        "## Pending Decision Questions\n- Researcher checkpoint pending: confirm or reject the seven S048 source-visible values in `paper_a_C_remaining_full10_batch_review_shortlist_20260615.csv`.",
    )
    append_current = f"""
## 2026-06-15 update - S121 ANX rejection and remaining C-tier batch triage

- Researcher rejected mapping `threat appraisal` to full10 `ANX`; `S121-1 ANX-PE=-0.23` and `S121-2 ANX-PE=-0.08` are not promoted.
- Completed a remaining-queue batch triage instead of continuing pair-by-pair: {len(batch_rows)} rows across {len(pair_counts)} full10 pair labels.
- Batch-safe source-visible numeric-cell candidates: {len(shortlist)} rows, all from `S048` Table 2 Pearson correlation matrix.
- Held/excluded groups: S004 SE rows depend on rejected `PKC -> SE`; S072 rows require construct-mapping audit before any value entry; one/no-human-supported-construct rows remain excluded unless source adjudication reopens mapping.
- Generated evidence artifacts under `data/04_extraction/05_llm_masem_substitution/results/paper_a_ai_candidate_source_trace_20260614/`:
  - `paper_a_C_remaining_full10_batch_triage_20260615.csv`
  - `paper_a_C_remaining_full10_batch_review_shortlist_20260615.csv`
  - `PAPER_A_C_REMAINING_FULL10_BATCH_TRIAGE_KO_20260615.md`
- Current next action: researcher confirms or rejects the seven S048 values before supplemental input or model-family MASEM rerun.
"""
    if "update - S121 ANX rejection and remaining C-tier batch triage" not in current:
        current = current.rstrip() + "\n\n" + append_current.lstrip()
    CURRENT.write_text(current, encoding="utf-8")


def add_sheet_to_workbook(sheet_name: str, rows: list[dict[str, str]], fields: list[str]) -> None:
    NS_MAIN = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
    NS_REL = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
    NS_PKG_REL = "http://schemas.openxmlformats.org/package/2006/relationships"
    NS_CT = "http://schemas.openxmlformats.org/package/2006/content-types"
    ET.register_namespace("", NS_MAIN)
    ET.register_namespace("r", NS_REL)
    tmp = WORKBOOK.with_suffix(".tmp.xlsx")
    with zipfile.ZipFile(WORKBOOK, "r") as zin:
        wb_xml = ET.fromstring(zin.read("xl/workbook.xml"))
        rels_xml = ET.fromstring(zin.read("xl/_rels/workbook.xml.rels"))
        ct_xml = ET.fromstring(zin.read("[Content_Types].xml"))
        sheets_el = wb_xml.find(f"{{{NS_MAIN}}}sheets")
        removed_targets = set()
        for sh in list(sheets_el):
            if sh.attrib.get("name") == sheet_name:
                rid = sh.attrib.get(f"{{{NS_REL}}}id")
                sheets_el.remove(sh)
                for rel in list(rels_xml):
                    if rel.attrib.get("Id") == rid:
                        target = rel.attrib.get("Target")
                        if target:
                            removed_targets.add("xl/" + target.lstrip("/"))
                        rels_xml.remove(rel)
                break
        for override in list(ct_xml):
            part = override.attrib.get("PartName", "")
            if part.startswith("/xl/") and part[1:] in removed_targets:
                ct_xml.remove(override)
        sheet_ids = [int(s.attrib.get("sheetId", "0")) for s in sheets_el if s.attrib.get("sheetId", "0").isdigit()]
        new_sheet_id = max(sheet_ids or [0]) + 1
        rids = []
        for rel in rels_xml:
            m = re.match(r"rId(\d+)$", rel.attrib.get("Id", ""))
            if m:
                rids.append(int(m.group(1)))
        new_rid = f"rId{max(rids or [0]) + 1}"
        sheet_nums = []
        for name in zin.namelist():
            m = re.match(r"xl/worksheets/sheet(\d+)\.xml$", name)
            if m and name not in removed_targets:
                sheet_nums.append(int(m.group(1)))
        new_sheet_num = max(sheet_nums or [0]) + 1
        new_target = f"worksheets/sheet{new_sheet_num}.xml"
        ET.SubElement(sheets_el, f"{{{NS_MAIN}}}sheet", {"name": sheet_name, "sheetId": str(new_sheet_id), f"{{{NS_REL}}}id": new_rid})
        ET.SubElement(rels_xml, f"{{{NS_PKG_REL}}}Relationship", {
            "Id": new_rid,
            "Type": "http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet",
            "Target": new_target,
        })
        ET.SubElement(ct_xml, f"{{{NS_CT}}}Override", {
            "PartName": f"/xl/worksheets/sheet{new_sheet_num}.xml",
            "ContentType": "application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml",
        })

        def col_letter(n: int) -> str:
            s = ""
            while n:
                n, rem = divmod(n - 1, 26)
                s = chr(65 + rem) + s
            return s

        ws = ET.Element(f"{{{NS_MAIN}}}worksheet")
        views = ET.SubElement(ws, f"{{{NS_MAIN}}}sheetViews")
        ET.SubElement(views, f"{{{NS_MAIN}}}sheetView", {"workbookViewId": "0"})
        ET.SubElement(ws, f"{{{NS_MAIN}}}sheetFormatPr", {"defaultRowHeight": "15"})
        data = ET.SubElement(ws, f"{{{NS_MAIN}}}sheetData")
        table = [fields] + [[r.get(c, "") for c in fields] for r in rows]
        for ri, vals in enumerate(table, 1):
            row_el = ET.SubElement(data, f"{{{NS_MAIN}}}row", {"r": str(ri)})
            for ci, val in enumerate(vals, 1):
                cell = ET.SubElement(row_el, f"{{{NS_MAIN}}}c", {"r": f"{col_letter(ci)}{ri}", "t": "inlineStr"})
                is_el = ET.SubElement(cell, f"{{{NS_MAIN}}}is")
                t = ET.SubElement(is_el, f"{{{NS_MAIN}}}t")
                if val != val.strip():
                    t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
                t.text = val
        ET.SubElement(ws, f"{{{NS_MAIN}}}pageMargins", {"left": "0.7", "right": "0.7", "top": "0.75", "bottom": "0.75", "header": "0.3", "footer": "0.3"})
        ws_xml = ET.tostring(ws, encoding="utf-8", xml_declaration=True)
        with zipfile.ZipFile(tmp, "w", compression=zipfile.ZIP_DEFLATED) as zout:
            for item in zin.infolist():
                if item.filename in {"xl/workbook.xml", "xl/_rels/workbook.xml.rels", "[Content_Types].xml"} or item.filename in removed_targets:
                    continue
                zout.writestr(item, zin.read(item.filename))
            zout.writestr("xl/workbook.xml", ET.tostring(wb_xml, encoding="utf-8", xml_declaration=True))
            zout.writestr("xl/_rels/workbook.xml.rels", ET.tostring(rels_xml, encoding="utf-8", xml_declaration=True))
            zout.writestr("[Content_Types].xml", ET.tostring(ct_xml, encoding="utf-8", xml_declaration=True))
            zout.writestr(f"xl/{new_target}", ws_xml)
    shutil.move(str(tmp), str(WORKBOOK))


def main() -> None:
    update_pair07_rejection()
    batch_rows, shortlist, counts = build_batch_rows()
    update_template(shortlist)
    write_logs(batch_rows, shortlist, counts)
    fields = list(batch_rows[0].keys())
    add_sheet_to_workbook("C_remaining_triage", batch_rows, fields)
    add_sheet_to_workbook("C_shortlist_0615", shortlist, fields)
    print(f"batch_rows={len(batch_rows)}")
    print(f"shortlist_rows={len(shortlist)}")
    print("counts=" + ";".join(f"{k}:{v}" for k, v in sorted(counts.items())))
    print(f"wrote={OUT_BATCH.relative_to(ROOT)}")
    print(f"wrote={OUT_SHORT.relative_to(ROOT)}")
    print(f"wrote={OUT_LOG.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
