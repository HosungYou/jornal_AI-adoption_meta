#!/usr/bin/env python3
"""Normalize the pre-flatten AI Adoption OneDrive workspace layout.

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


LOCAL_ROOT = Path("/Users/newhosung/Academic/2026/AI Adoption Meta Analysis")
BASE = Path(
    "/Users/newhosung/Library/CloudStorage/"
    "OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity/"
    "AI Adoption Meta Analysis - Documents"
)
CANON = BASE / "Meta" / "AI Adoption"
INDEX = CANON / "00_INDEX"
ARCHIVE = CANON / "99_archive" / "structure_cleanup_20260617"
SOURCE_PACKAGES = CANON / "02_source_packages" / "source_pdfs"
WORK_ALLOC = INDEX / "2026-06-17_Paper_A_B_work_allocation"
WORK_SHARED = WORK_ALLOC / "00_shared"
WORK_INTERNAL_ARCHIVE = WORK_ALLOC / "99_archive"

DATE_TAG = "20260617"

ROOT_MANUSCRIPTS = BASE / "05_manuscripts"
CANON_MANUSCRIPTS = CANON / "05_manuscripts"
SINGULAR_MANUSCRIPT = CANON / "05_manuscript"
META_SOURCE_PDFS = BASE / "Meta" / "source_pdfs"
CANON_PDFS = CANON / "PDFs"

INVENTORY_CSV = INDEX / f"STRUCTURE_CLEANUP_INVENTORY_{DATE_TAG}.csv"
MOVED_FROM_CSV = INDEX / f"MOVED_FROM_{DATE_TAG}.csv"
CONFLICTS_CSV = INDEX / f"STRUCTURE_CLEANUP_CONFLICTS_{DATE_TAG}.csv"
README_PATH = INDEX / f"README_STRUCTURE_CLEANUP_{DATE_TAG}.md"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def iso_mtime(path: Path) -> str:
    return datetime.fromtimestamp(path.stat().st_mtime).isoformat(timespec="seconds")


def rel_to_base(path: Path) -> str:
    try:
        return str(path.relative_to(BASE))
    except ValueError:
        return str(path)


def iter_files(root: Path):
    if not root.exists():
        return
    if root.is_file():
        yield root
        return
    for path in sorted(root.rglob("*")):
        if path.is_file():
            yield path


def ensure_dirs() -> None:
    for path in [
        INDEX,
        ARCHIVE,
        CANON_MANUSCRIPTS / "Paper_A",
        CANON_MANUSCRIPTS / "Paper_B",
        SOURCE_PACKAGES,
        WORK_SHARED,
        WORK_INTERNAL_ARCHIVE,
        WORK_ALLOC / "R1",
        WORK_ALLOC / "R2",
        WORK_ALLOC / "R3",
        WORK_ALLOC / "R4",
    ]:
        path.mkdir(parents=True, exist_ok=True)


def proposed_destination(path: Path) -> str:
    if path.name == ".DS_Store":
        return "archive_only"
    if ROOT_MANUSCRIPTS.exists() and path.is_relative_to(ROOT_MANUSCRIPTS):
        return rel_to_base(CANON_MANUSCRIPTS / path.relative_to(ROOT_MANUSCRIPTS))
    if SINGULAR_MANUSCRIPT.exists() and path.is_relative_to(SINGULAR_MANUSCRIPT):
        return rel_to_base(CANON_MANUSCRIPTS / path.relative_to(SINGULAR_MANUSCRIPT))
    if CANON_MANUSCRIPTS.exists() and path.is_relative_to(CANON_MANUSCRIPTS):
        return rel_to_base(path)
    if META_SOURCE_PDFS.exists() and path.is_relative_to(META_SOURCE_PDFS):
        return rel_to_base(SOURCE_PACKAGES / path.relative_to(META_SOURCE_PDFS))
    if CANON_PDFS.exists() and path.is_relative_to(CANON_PDFS):
        return rel_to_base(SOURCE_PACKAGES / "all_project_pdfs" / path.relative_to(CANON_PDFS))
    if WORK_ALLOC.exists() and path.parent == WORK_ALLOC:
        return rel_to_base(WORK_SHARED / path.name)
    return ""


def write_inventory() -> int:
    roots = [
        ROOT_MANUSCRIPTS,
        CANON_MANUSCRIPTS,
        SINGULAR_MANUSCRIPT,
        META_SOURCE_PDFS,
        CANON_PDFS,
        SOURCE_PACKAGES,
        WORK_ALLOC,
    ]
    rows = []
    seen = set()
    for root in roots:
        for path in iter_files(root) or []:
            if path in seen:
                continue
            seen.add(path)
            rows.append(
                {
                    "absolute_path": str(path),
                    "relative_to_onedrive_base": rel_to_base(path),
                    "size_bytes": path.stat().st_size,
                    "mtime": iso_mtime(path),
                    "sha256": sha256(path),
                    "proposed_destination": proposed_destination(path),
                }
            )
    with INVENTORY_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()) if rows else [
            "absolute_path",
            "relative_to_onedrive_base",
            "size_bytes",
            "mtime",
            "sha256",
            "proposed_destination",
        ])
        writer.writeheader()
        writer.writerows(rows)
    return len(rows)


def unique_path(path: Path) -> Path:
    if not path.exists():
        return path
    for i in range(1, 1000):
        candidate = path.with_name(f"{path.stem}_{i}{path.suffix}")
        if not candidate.exists():
            return candidate
    raise RuntimeError(f"Could not allocate unique path for {path}")


def collision_path(dest: Path, source_label: str) -> Path:
    candidate = dest.with_name(f"{dest.stem}__from_{source_label}{dest.suffix}")
    return unique_path(candidate)


def copy_file_verified(src: Path, dest: Path, source_label: str, rows: list[dict], conflicts: list[dict]) -> Path:
    if src.name == ".DS_Store":
        rows.append({
            "action": "skip_ds_store",
            "source": rel_to_base(src),
            "destination": "",
            "sha256": "",
            "note": "macOS metadata file archived with source shell",
        })
        return dest

    source_hash = sha256(src)
    final_dest = dest
    action = "copied"
    note = ""

    if dest.exists():
        dest_hash = sha256(dest)
        if dest_hash == source_hash:
            rows.append({
                "action": "skip_existing_same_hash",
                "source": rel_to_base(src),
                "destination": rel_to_base(dest),
                "sha256": source_hash,
                "note": "destination already identical",
            })
            return dest
        final_dest = collision_path(dest, source_label)
        action = "copied_with_collision_suffix"
        note = f"same destination name had different hash; original destination preserved at {rel_to_base(dest)}"
        conflicts.append({
            "source": rel_to_base(src),
            "intended_destination": rel_to_base(dest),
            "actual_destination": rel_to_base(final_dest),
            "source_sha256": source_hash,
            "existing_destination_sha256": dest_hash,
            "resolution": "preserved both files",
        })

    final_dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, final_dest)
    copied_hash = sha256(final_dest)
    if copied_hash != source_hash:
        raise RuntimeError(f"Checksum mismatch after copy: {src} -> {final_dest}")
    rows.append({
        "action": action,
        "source": rel_to_base(src),
        "destination": rel_to_base(final_dest),
        "sha256": source_hash,
        "note": note,
    })
    return final_dest


def copy_tree_contents(src_root: Path, dest_root: Path, source_label: str, rows: list[dict], conflicts: list[dict]) -> None:
    if not src_root.exists():
        rows.append({
            "action": "missing_source_skip",
            "source": rel_to_base(src_root),
            "destination": rel_to_base(dest_root),
            "sha256": "",
            "note": "source path not present",
        })
        return
    for src in iter_files(src_root) or []:
        rel = src.relative_to(src_root)
        copy_file_verified(src, dest_root / rel, source_label, rows, conflicts)


def archive_shell(path: Path, label: str, rows: list[dict]) -> None:
    if not path.exists():
        return
    destination = unique_path(ARCHIVE / f"{label}_pre_cleanup_{DATE_TAG}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(path), str(destination))
    rows.append({
        "action": "archived_noncanonical_shell",
        "source": rel_to_base(path),
        "destination": rel_to_base(destination),
        "sha256": "",
        "note": "source shell moved out of active workspace after verified canonical copy",
    })


def archive_work_alloc_root_files(rows: list[dict]) -> None:
    if not WORK_ALLOC.exists():
        return
    archive_dir = WORK_INTERNAL_ARCHIVE / f"root_files_before_shared_{DATE_TAG}"
    archive_dir.mkdir(parents=True, exist_ok=True)
    for path in sorted(WORK_ALLOC.iterdir()):
        if path.is_file() and path.name != ".DS_Store":
            dest = unique_path(archive_dir / path.name)
            source_hash = sha256(path)
            shutil.move(str(path), str(dest))
            moved_hash = sha256(dest)
            if moved_hash != source_hash:
                raise RuntimeError(f"Checksum mismatch after work allocation move: {path} -> {dest}")
            rows.append({
                "action": "moved_work_allocation_root_file_to_archive",
                "source": rel_to_base(path),
                "destination": rel_to_base(dest),
                "sha256": source_hash,
                "note": "active copy is recreated in 00_shared from local repo",
            })


def replace_active_file(src: Path, dest: Path, source_label: str, rows: list[dict]) -> None:
    if not src.exists():
        raise FileNotFoundError(src)
    src_hash = sha256(src)
    if dest.exists():
        dest_hash = sha256(dest)
        if dest_hash != src_hash:
            backup_dir = WORK_INTERNAL_ARCHIVE / f"replaced_active_files_{DATE_TAG}"
            backup_dir.mkdir(parents=True, exist_ok=True)
            backup = unique_path(backup_dir / dest.name)
            shutil.move(str(dest), str(backup))
            rows.append({
                "action": "archived_replaced_active_file",
                "source": rel_to_base(dest),
                "destination": rel_to_base(backup),
                "sha256": dest_hash,
                "note": "newer local repo version copied into active shared folder",
            })
        else:
            rows.append({
                "action": "active_file_already_current",
                "source": str(src),
                "destination": rel_to_base(dest),
                "sha256": src_hash,
                "note": source_label,
            })
            return
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dest)
    if sha256(dest) != src_hash:
        raise RuntimeError(f"Checksum mismatch after active file copy: {src} -> {dest}")
    rows.append({
        "action": "copied_active_shared_file",
        "source": str(src),
        "destination": rel_to_base(dest),
        "sha256": src_hash,
        "note": source_label,
    })


def write_role_readmes(rows: list[dict]) -> None:
    role_notes = {
        "R1": [
            "Paper A PRISMA/source-lock final gate",
            "duplicate DOI interpretation",
            "Paper B reference-standard protocol guard",
            "weekly release register",
        ],
        "R2": [
            "Paper A screening/eligibility independent review",
            "Paper B disagreement/adjudication trace support",
            "IRR or agreement-summary evidence",
        ],
        "R3": [
            "Paper A independent review paired with R2",
            "Paper B cross-pair adjudication support",
            "construct remap and escalation list",
        ],
        "R4": [
            "Paper B data/package QA",
            "checksum/run manifest review",
            "source-type boundary and public/private release audit",
        ],
    }
    for role, tasks in role_notes.items():
        path = WORK_ALLOC / role / f"README_{role}_TASKS_{DATE_TAG}.md"
        text = [
            f"# {role} task folder",
            "",
            "Canonical shared plan files are in `../00_shared/`.",
            "",
            "## Current task lanes",
            "",
        ]
        for task in tasks:
            text.append(f"- {task}")
        text.extend([
            "",
            "Add reviewer-specific notes, completed workbooks, or handoff files here without overwriting shared source files.",
            "",
        ])
        old_hash = sha256(path) if path.exists() else ""
        path.write_text("\n".join(text), encoding="utf-8")
        rows.append({
            "action": "wrote_role_readme",
            "source": "",
            "destination": rel_to_base(path),
            "sha256": sha256(path),
            "note": f"previous_sha256={old_hash}" if old_hash else "",
        })


def update_text_file(path: Path, replacements: dict[str, str], rows: list[dict]) -> None:
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    old_text = text
    for old, new in replacements.items():
        text = text.replace(old, new)
    if text == old_text:
        rows.append({
            "action": "text_update_noop",
            "source": rel_to_base(path),
            "destination": rel_to_base(path),
            "sha256": sha256(path),
            "note": "no matching stale text found",
        })
        return
    old_hash = sha256(path)
    backup_dir = ARCHIVE / "updated_pointer_backups"
    backup_dir.mkdir(parents=True, exist_ok=True)
    backup = unique_path(backup_dir / path.name)
    shutil.copy2(path, backup)
    path.write_text(text, encoding="utf-8")
    rows.append({
        "action": "updated_pointer_text",
        "source": rel_to_base(path),
        "destination": rel_to_base(path),
        "sha256": sha256(path),
        "note": f"backup={rel_to_base(backup)}; previous_sha256={old_hash}",
    })


def write_readme(rows_count: int, move_count: int, conflict_count: int) -> None:
    text = f"""# Structure cleanup {DATE_TAG}

Canonical OneDrive human-facing root:

`{CANON}`

Canonical local Git root:

`{LOCAL_ROOT}`

## What changed

- Merged root-level `05_manuscripts/` into `Meta/AI Adoption/05_manuscripts/`.
- Merged singular `Meta/AI Adoption/05_manuscript/` into plural `05_manuscripts/`.
- Moved source PDF pools toward `Meta/AI Adoption/02_source_packages/source_pdfs/`.
- Normalized the Paper A/B work allocation package with `00_shared/`, `R1/`, `R2/`, `R3/`, `R4/`, and `99_archive/`.
- Archived noncanonical active shells under `Meta/AI Adoption/99_archive/structure_cleanup_20260617/`.

## Evidence

- Inventory rows: {rows_count}
- Move/copy log rows: {move_count}
- Conflict rows: {conflict_count}

## Logs

- `{rel_to_base(INVENTORY_CSV)}`
- `{rel_to_base(MOVED_FROM_CSV)}`
- `{rel_to_base(CONFLICTS_CSV)}`
"""
    README_PATH.write_text(text, encoding="utf-8")


def write_csv(path: Path, rows: list[dict], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    if not CANON.exists() and (BASE / "00_INDEX").exists():
        raise SystemExit(
            "This pre-flatten cleanup script is not applicable after OneDrive "
            "root promotion. Use the root-level canonical tree instead."
        )
    ensure_dirs()
    inventory_count = write_inventory()

    rows: list[dict] = []
    conflicts: list[dict] = []

    copy_tree_contents(ROOT_MANUSCRIPTS, CANON_MANUSCRIPTS, "root_05_manuscripts", rows, conflicts)
    copy_tree_contents(SINGULAR_MANUSCRIPT, CANON_MANUSCRIPTS, "singular_05_manuscript", rows, conflicts)
    copy_tree_contents(META_SOURCE_PDFS, SOURCE_PACKAGES, "meta_source_pdfs", rows, conflicts)
    copy_tree_contents(CANON_PDFS, SOURCE_PACKAGES / "all_project_pdfs", "legacy_pdfs_pool", rows, conflicts)

    archive_work_alloc_root_files(rows)

    local_ops = LOCAL_ROOT / "docs" / "08_operations"
    for filename in [
        "PAPER_A_B_WORK_ALLOCATION_AND_TRACKING_PLAN_KO_20260617.docx",
        "PAPER_A_B_WORK_ALLOCATION_AND_TRACKING_PLAN_KO_20260617.md",
        "PAPER_A_B_TASK_TRACKER_SEED_20260617.csv",
    ]:
        replace_active_file(local_ops / filename, WORK_SHARED / filename, "local repo operation artifact", rows)

    write_role_readmes(rows)

    update_text_file(
        BASE / "AGENTS.md",
        {
            "/Users/newhosung/Academic/2026/AI Adoption Meta Analysis/Git/jornal_AI-adoption_meta": str(LOCAL_ROOT),
            "If operating in the OneDrive clone `Git/jornal_AI-adoption_meta`, check for sync conflicts before writing large generated outputs.": (
                "If operating in the OneDrive repository mirror `Meta/AI Adoption/90_repository_mirror/journal_AI-adoption_meta`, "
                "treat it as a review mirror rather than the execution repository."
            ),
        },
        rows,
    )
    update_text_file(
        INDEX / "PROJECT_WORKSPACE_LAYOUT_20260614.md",
        {
            "/Users/newhosung/Academic/2026/AI Adoption Meta Analysis/Git/jornal_AI-adoption_meta": str(LOCAL_ROOT),
            "Git 추적 파일 최신 작업본 + 팀 편집용 문서": "Git 추적 파일 검토용 복제본",
        },
        rows,
    )

    archive_shell(ROOT_MANUSCRIPTS, "root_05_manuscripts", rows)
    archive_shell(SINGULAR_MANUSCRIPT, "singular_05_manuscript", rows)
    archive_shell(META_SOURCE_PDFS, "meta_source_pdfs", rows)
    archive_shell(CANON_PDFS, "legacy_pdfs_pool", rows)

    write_csv(
        MOVED_FROM_CSV,
        rows,
        ["action", "source", "destination", "sha256", "note"],
    )
    write_csv(
        CONFLICTS_CSV,
        conflicts,
        [
            "source",
            "intended_destination",
            "actual_destination",
            "source_sha256",
            "existing_destination_sha256",
            "resolution",
        ],
    )
    write_readme(inventory_count, len(rows), len(conflicts))

    print(f"inventory_rows={inventory_count}")
    print(f"move_log_rows={len(rows)}")
    print(f"conflict_rows={len(conflicts)}")
    print(f"canonical_root={CANON}")
    print(f"work_allocation={WORK_ALLOC}")


if __name__ == "__main__":
    main()
