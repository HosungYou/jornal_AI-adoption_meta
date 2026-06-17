#!/usr/bin/env python3
"""Move legacy OneDrive top-level project folders into the pre-flatten tree.

This script was used before `flatten_onedrive_ai_adoption_root_20260617.py`.
It is intentionally guarded so it does not recreate `Meta/AI Adoption` after
the OneDrive root has been promoted to the canonical workspace root.
"""

from __future__ import annotations

import csv
import hashlib
import shutil
from datetime import datetime
from pathlib import Path


BASE = Path(
    "/Users/newhosung/Library/CloudStorage/"
    "OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity/"
    "AI Adoption Meta Analysis - Documents"
)
CANON = BASE / "Meta" / "AI Adoption"
INDEX = CANON / "00_INDEX"
DATE_TAG = "20260617"

INVENTORY_CSV = INDEX / f"LEGACY_TOPLEVEL_CLEANUP_INVENTORY_{DATE_TAG}.csv"
MOVED_CSV = INDEX / f"LEGACY_TOPLEVEL_MOVED_FROM_{DATE_TAG}.csv"
README = INDEX / f"README_LEGACY_TOPLEVEL_CLEANUP_{DATE_TAG}.md"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def iter_files(root: Path):
    if not root.exists():
        return
    if root.is_file():
        yield root
        return
    for path in sorted(root.rglob("*")):
        if path.is_file():
            yield path


def rel_base(path: Path) -> str:
    try:
        return str(path.relative_to(BASE))
    except ValueError:
        return str(path)


def rel_src(path: Path, root: Path) -> str:
    return str(path.relative_to(root)) if path != root else path.name


def unique_path(path: Path) -> Path:
    if not path.exists():
        return path
    for i in range(1, 1000):
        candidate = path.with_name(f"{path.stem}_{i}{path.suffix}")
        if not candidate.exists():
            return candidate
    raise RuntimeError(f"Could not allocate unique path for {path}")


def manifest(root: Path) -> list[dict]:
    rows = []
    for file_path in iter_files(root) or []:
        rows.append({
            "relative_path": rel_src(file_path, root),
            "size_bytes": file_path.stat().st_size,
            "sha256": sha256(file_path),
        })
    return rows


def tree_digest(rows: list[dict]) -> str:
    h = hashlib.sha256()
    for row in sorted(rows, key=lambda x: x["relative_path"]):
        h.update(row["relative_path"].encode("utf-8"))
        h.update(b"\0")
        h.update(str(row["size_bytes"]).encode("ascii"))
        h.update(b"\0")
        h.update(row["sha256"].encode("ascii"))
        h.update(b"\n")
    return h.hexdigest()


def verify_manifest(root: Path, before: list[dict]) -> None:
    after = {row["relative_path"]: row for row in manifest(root)}
    before_map = {row["relative_path"]: row for row in before}
    if before_map != after:
        raise RuntimeError(f"Manifest mismatch after move into {root}")


def move_verified(src: Path, dest: Path, label: str, rows: list[dict]) -> None:
    if not src.exists():
        rows.append({
            "label": label,
            "action": "missing_source_skip",
            "source": rel_base(src),
            "destination": rel_base(dest),
            "file_count": 0,
            "size_bytes": 0,
            "tree_digest": "",
            "note": "source path not present",
        })
        return

    before = manifest(src)
    digest = tree_digest(before)
    size = sum(int(row["size_bytes"]) for row in before)
    file_count = len(before)
    final_dest = unique_path(dest)
    final_dest.parent.mkdir(parents=True, exist_ok=True)

    shutil.move(str(src), str(final_dest))
    verify_manifest(final_dest, before)
    rows.append({
        "label": label,
        "action": "moved_verified",
        "source": rel_base(src),
        "destination": rel_base(final_dest),
        "file_count": file_count,
        "size_bytes": size,
        "tree_digest": digest,
        "note": "destination suffixed automatically if needed",
    })


def write_inventory(sources: list[Path]) -> int:
    rows = []
    for src in sources:
        for file_path in iter_files(src) or []:
            rows.append({
                "source_root": rel_base(src),
                "absolute_path": str(file_path),
                "relative_to_source_root": rel_src(file_path, src),
                "relative_to_onedrive_base": rel_base(file_path),
                "size_bytes": file_path.stat().st_size,
                "mtime": datetime.fromtimestamp(file_path.stat().st_mtime).isoformat(timespec="seconds"),
                "sha256": sha256(file_path),
            })
    with INVENTORY_CSV.open("w", newline="", encoding="utf-8") as f:
        fieldnames = [
            "source_root",
            "absolute_path",
            "relative_to_source_root",
            "relative_to_onedrive_base",
            "size_bytes",
            "mtime",
            "sha256",
        ]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    return len(rows)


def write_csv(path: Path, rows: list[dict]) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        fieldnames = ["label", "action", "source", "destination", "file_count", "size_bytes", "tree_digest", "note"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_readme(inventory_count: int, rows: list[dict]) -> None:
    total_files = sum(int(row["file_count"]) for row in rows)
    total_bytes = sum(int(row["size_bytes"]) for row in rows)
    text = f"""# Legacy top-level cleanup {DATE_TAG}

This pass moved legacy top-level folders under the canonical OneDrive tree:

`{CANON}`

## Mapping principles

- R1-R4 workbook/manual files -> `01_workbooks/raw_coder_returns/by_rater/`
- R1-R4 PDF subfolders -> `02_source_packages/source_pdfs/by_rater/`
- Latest coder collections -> `01_workbooks/latest_collections/`
- Consensus/review/reference-standard materials -> `03_source_adjudication/`
- Paper A/B working analysis packages -> `04_analysis_outputs/`
- Structure notes and trackers -> `00_INDEX/` or the matching source/workbook tracker folder

## Evidence

- Inventory rows: {inventory_count}
- Move summary rows: {len(rows)}
- Files moved: {total_files}
- Bytes moved: {total_bytes}

## Logs

- `{rel_base(INVENTORY_CSV)}`
- `{rel_base(MOVED_CSV)}`
"""
    README.write_text(text, encoding="utf-8")


def main() -> None:
    if not CANON.exists() and (BASE / "00_INDEX").exists():
        raise SystemExit(
            "This pre-flatten legacy cleanup script is not applicable after "
            "OneDrive root promotion. Use the root-level canonical tree instead."
        )
    INDEX.mkdir(parents=True, exist_ok=True)

    top_level_sources = [
        CANON / "R1",
        CANON / "R2",
        CANON / "R3",
        CANON / "R4",
        CANON / "Coding_Latest_R1_R4_20260605",
        CANON / "Consensus",
        CANON / "Review_Packets_20260530",
        CANON / "Paper2_Analysis_Input_20260530",
        CANON / "Paper1_MASEM_Working_20260605",
        CANON / "Paper2_LLM_Extraction_Working_20260605",
        CANON / "Paper2_Human_Final_Consensus_20260605",
        CANON / "Paper2_Human_Final_Consensus_20260605_v2",
        CANON / "04_analysis_strategy",
        CANON / "PAPER1_PAPER2_WORKING_STRUCTURE_20260605.md",
        CANON / "STRUCTURE_PROPOSAL_20260605.md",
        CANON / "construct_harmonization.docx",
        CANON / "human_review_sheet_v8_0306.xlsx",
        CANON / "pdf_download_tracker.xlsx",
    ]
    inventory_count = write_inventory(top_level_sources)

    rows: list[dict] = []

    for role in ["R1", "R2", "R3", "R4"]:
        role_root = CANON / role
        if not role_root.exists():
            continue
        pdf_root = role_root / "PDFs"
        move_verified(
            pdf_root,
            CANON / "02_source_packages" / "source_pdfs" / "by_rater" / role,
            f"{role}_pdfs",
            rows,
        )
        for child in sorted(role_root.iterdir()):
            if child.name == "PDFs":
                continue
            move_verified(
                child,
                CANON / "01_workbooks" / "raw_coder_returns" / "by_rater" / role / child.name,
                f"{role}_workbook_or_manual",
                rows,
            )
        try:
            role_root.rmdir()
            rows.append({
                "label": role,
                "action": "removed_empty_legacy_role_shell",
                "source": rel_base(role_root),
                "destination": "",
                "file_count": 0,
                "size_bytes": 0,
                "tree_digest": "",
                "note": "empty top-level role folder removed after split move",
            })
        except OSError:
            rows.append({
                "label": role,
                "action": "legacy_role_shell_not_empty",
                "source": rel_base(role_root),
                "destination": "",
                "file_count": 0,
                "size_bytes": 0,
                "tree_digest": "",
                "note": "manual inspection required",
            })

    mappings = [
        ("latest_r1_r4_collection", CANON / "Coding_Latest_R1_R4_20260605", CANON / "01_workbooks" / "latest_collections" / "20260605_R1_R4"),
        ("consensus_calibration", CANON / "Consensus", CANON / "03_source_adjudication" / "consensus_calibration_legacy" / "Consensus"),
        ("review_packets_20260530", CANON / "Review_Packets_20260530", CANON / "03_source_adjudication" / "review_packets_20260530"),
        ("paper2_analysis_input_20260530", CANON / "Paper2_Analysis_Input_20260530", CANON / "04_analysis_outputs" / "Paper_B" / "analysis_input_20260530"),
        ("paper1_masem_working_package", CANON / "Paper1_MASEM_Working_20260605", CANON / "04_analysis_outputs" / "Paper_A" / "working_packages" / "Paper1_MASEM_Working_20260605"),
        ("paper2_llm_working_package", CANON / "Paper2_LLM_Extraction_Working_20260605", CANON / "04_analysis_outputs" / "Paper_B" / "working_packages" / "Paper2_LLM_Extraction_Working_20260605"),
        ("paper2_human_reference_candidate_v1", CANON / "Paper2_Human_Final_Consensus_20260605", CANON / "03_source_adjudication" / "Paper_B" / "reference_standard_candidates" / "Paper2_Human_Final_Consensus_20260605"),
        ("paper2_human_reference_candidate_v2", CANON / "Paper2_Human_Final_Consensus_20260605_v2", CANON / "03_source_adjudication" / "Paper_B" / "reference_standard_candidates" / "Paper2_Human_Final_Consensus_20260605_v2"),
        ("analysis_strategy", CANON / "04_analysis_strategy", CANON / "04_analysis_outputs" / "analysis_strategy"),
        ("working_structure_note", CANON / "PAPER1_PAPER2_WORKING_STRUCTURE_20260605.md", CANON / "00_INDEX" / "legacy_structure_notes" / "PAPER1_PAPER2_WORKING_STRUCTURE_20260605.md"),
        ("structure_proposal_note", CANON / "STRUCTURE_PROPOSAL_20260605.md", CANON / "00_INDEX" / "legacy_structure_notes" / "STRUCTURE_PROPOSAL_20260605.md"),
        ("construct_harmonization_doc", CANON / "construct_harmonization.docx", CANON / "01_workbooks" / "protocol_support" / "construct_harmonization.docx"),
        ("human_review_sheet", CANON / "human_review_sheet_v8_0306.xlsx", CANON / "01_workbooks" / "review_sheets" / "human_review_sheet_v8_0306.xlsx"),
        ("pdf_download_tracker", CANON / "pdf_download_tracker.xlsx", CANON / "02_source_packages" / "source_tracking" / "pdf_download_tracker.xlsx"),
    ]
    for label, src, dest in mappings:
        move_verified(src, dest, label, rows)

    write_csv(MOVED_CSV, rows)
    write_readme(inventory_count, rows)

    print(f"inventory_rows={inventory_count}")
    print(f"move_summary_rows={len(rows)}")
    print(f"moved_files={sum(int(row['file_count']) for row in rows)}")
    print(f"moved_bytes={sum(int(row['size_bytes']) for row in rows)}")


if __name__ == "__main__":
    main()
