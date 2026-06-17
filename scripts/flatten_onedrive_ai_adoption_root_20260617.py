#!/usr/bin/env python3
"""Promote OneDrive Meta/AI Adoption contents to the OneDrive library root."""

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
OLD_ROOT = BASE / "Meta" / "AI Adoption"
DATE_TAG = "20260617"

ROOT_INDEX = BASE / "00_INDEX"
ROOT_ARCHIVE = BASE / "99_archive" / "root_flatten_20260617"
INVENTORY_CSV = ROOT_INDEX / f"ROOT_FLATTEN_INVENTORY_{DATE_TAG}.csv"
MOVED_CSV = ROOT_INDEX / f"ROOT_FLATTEN_MOVED_FROM_{DATE_TAG}.csv"
README = ROOT_INDEX / f"README_ROOT_FLATTEN_{DATE_TAG}.md"

CANONICAL_ENTRIES = [
    "00_INDEX",
    "01_workbooks",
    "02_source_packages",
    "03_source_adjudication",
    "04_analysis_outputs",
    "05_manuscripts",
    "90_repository_mirror",
    "99_archive",
]


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


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(BASE))
    except ValueError:
        return str(path)


def manifest(root: Path) -> list[dict]:
    rows = []
    for file_path in iter_files(root) or []:
        rows.append({
            "relative_path": str(file_path.relative_to(root)),
            "size_bytes": file_path.stat().st_size,
            "sha256": sha256(file_path),
        })
    return rows


def tree_digest(rows: list[dict]) -> str:
    h = hashlib.sha256()
    for row in sorted(rows, key=lambda r: r["relative_path"]):
        h.update(row["relative_path"].encode("utf-8"))
        h.update(b"\0")
        h.update(str(row["size_bytes"]).encode("ascii"))
        h.update(b"\0")
        h.update(row["sha256"].encode("ascii"))
        h.update(b"\n")
    return h.hexdigest()


def verify_manifest(root: Path, before: list[dict]) -> None:
    if {r["relative_path"]: r for r in manifest(root)} != {r["relative_path"]: r for r in before}:
        raise RuntimeError(f"Manifest mismatch after moving {root}")


def unique_path(path: Path) -> Path:
    if not path.exists():
        return path
    for i in range(1, 1000):
        candidate = path.with_name(f"{path.name}_{i}")
        if not candidate.exists():
            return candidate
    raise RuntimeError(f"Could not allocate unique path for {path}")


def move_verified(src: Path, dst: Path, label: str, rows: list[dict]) -> None:
    if not src.exists():
        rows.append({
            "label": label,
            "action": "missing_source_skip",
            "source": rel(src),
            "destination": rel(dst),
            "file_count": 0,
            "size_bytes": 0,
            "tree_digest": "",
            "note": "source absent",
        })
        return
    before = manifest(src)
    digest = tree_digest(before)
    size = sum(int(row["size_bytes"]) for row in before)
    dst = unique_path(dst)
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(src), str(dst))
    verify_manifest(dst, before)
    rows.append({
        "label": label,
        "action": "moved_verified",
        "source": rel(src),
        "destination": rel(dst),
        "file_count": len(before),
        "size_bytes": size,
        "tree_digest": digest,
        "note": "promoted from Meta/AI Adoption to OneDrive root",
    })


def write_inventory() -> int:
    rows = []
    if OLD_ROOT.exists():
        for file_path in iter_files(OLD_ROOT) or []:
            rows.append({
                "absolute_path": str(file_path),
                "relative_to_old_root": str(file_path.relative_to(OLD_ROOT)),
                "relative_to_onedrive_root": rel(file_path),
                "size_bytes": file_path.stat().st_size,
                "mtime": datetime.fromtimestamp(file_path.stat().st_mtime).isoformat(timespec="seconds"),
                "sha256": sha256(file_path),
            })
    ROOT_INDEX.mkdir(parents=True, exist_ok=True)
    with INVENTORY_CSV.open("w", newline="", encoding="utf-8") as f:
        fieldnames = [
            "absolute_path",
            "relative_to_old_root",
            "relative_to_onedrive_root",
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


def update_text(path: Path, replacements: dict[str, str], rows: list[dict]) -> None:
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    new = text
    for old, repl in replacements.items():
        new = new.replace(old, repl)
    if new == text:
        rows.append({
            "label": "pointer_update",
            "action": "text_update_noop",
            "source": rel(path),
            "destination": rel(path),
            "file_count": 1,
            "size_bytes": path.stat().st_size,
            "tree_digest": sha256(path),
            "note": "no stale text matched",
        })
        return
    backup_dir = ROOT_ARCHIVE / "updated_pointer_backups"
    backup_dir.mkdir(parents=True, exist_ok=True)
    backup = unique_path(backup_dir / path.name)
    before_hash = sha256(path)
    shutil.copy2(path, backup)
    path.write_text(new, encoding="utf-8")
    rows.append({
        "label": "pointer_update",
        "action": "updated_text_pointer",
        "source": rel(path),
        "destination": rel(path),
        "file_count": 1,
        "size_bytes": path.stat().st_size,
        "tree_digest": sha256(path),
        "note": f"backup={rel(backup)}; previous_sha256={before_hash}",
    })


def write_readme(inventory_count: int, rows: list[dict]) -> None:
    total_files = sum(int(row["file_count"]) for row in rows if row["action"] == "moved_verified")
    total_bytes = sum(int(row["size_bytes"]) for row in rows if row["action"] == "moved_verified")
    text = f"""# OneDrive root flatten {DATE_TAG}

The AI Adoption OneDrive library now uses its root as the human-facing canonical tree.

## Canonical root

`{BASE}`

## Previous wrapper

`{OLD_ROOT}`

## Active folders

- `00_INDEX`
- `01_workbooks`
- `02_source_packages`
- `03_source_adjudication`
- `04_analysis_outputs`
- `05_manuscripts`
- `90_repository_mirror`
- `99_archive`

`AGENTS.md` and `CLAUDE.md` remain at the OneDrive root because they are workspace-level agent instructions, not research-stage folders.

## Evidence

- Inventory rows before flatten: {inventory_count}
- Move rows: {len([row for row in rows if row["action"] == "moved_verified"])}
- Files moved: {total_files}
- Bytes moved: {total_bytes}

## Logs

- `{rel(INVENTORY_CSV)}`
- `{rel(MOVED_CSV)}`
"""
    README.write_text(text, encoding="utf-8")


def archive_empty_wrapper(rows: list[dict]) -> None:
    meta = BASE / "Meta"
    shell_archive = ROOT_ARCHIVE / "meta_wrapper_shell"
    shell_archive.mkdir(parents=True, exist_ok=True)

    for path in [OLD_ROOT, meta]:
        if not path.exists():
            continue
        leftovers = list(path.iterdir())
        if not leftovers:
            path.rmdir()
            rows.append({
                "label": "meta_wrapper",
                "action": "removed_empty_wrapper_dir",
                "source": rel(path),
                "destination": "",
                "file_count": 0,
                "size_bytes": 0,
                "tree_digest": "",
                "note": "empty after root flatten",
            })
            continue
        for child in leftovers:
            dst = unique_path(shell_archive / child.name)
            shutil.move(str(child), str(dst))
            rows.append({
                "label": "meta_wrapper_leftover",
                "action": "archived_wrapper_leftover",
                "source": rel(child),
                "destination": rel(dst),
                "file_count": len(manifest(dst)) if dst.exists() else 0,
                "size_bytes": sum(int(r["size_bytes"]) for r in manifest(dst)) if dst.exists() else 0,
                "tree_digest": tree_digest(manifest(dst)) if dst.exists() else "",
                "note": "leftover wrapper file or folder archived",
            })
        try:
            path.rmdir()
            rows.append({
                "label": "meta_wrapper",
                "action": "removed_wrapper_dir_after_archiving_leftovers",
                "source": rel(path),
                "destination": "",
                "file_count": 0,
                "size_bytes": 0,
                "tree_digest": "",
                "note": "wrapper removed from active root",
            })
        except OSError:
            rows.append({
                "label": "meta_wrapper",
                "action": "wrapper_dir_not_empty",
                "source": rel(path),
                "destination": "",
                "file_count": 0,
                "size_bytes": 0,
                "tree_digest": "",
                "note": "manual inspection required",
            })


def main() -> None:
    if not OLD_ROOT.exists():
        raise SystemExit(f"Old root is missing: {OLD_ROOT}")

    ROOT_INDEX.mkdir(parents=True, exist_ok=True)
    ROOT_ARCHIVE.mkdir(parents=True, exist_ok=True)
    inventory_count = write_inventory()
    rows: list[dict] = []

    for entry in CANONICAL_ENTRIES:
        move_verified(OLD_ROOT / entry, BASE / entry, entry, rows)

    replacements = {
        str(OLD_ROOT): str(BASE),
        "Human-facing outputs live under `Meta/AI Adoption/`.": "Human-facing outputs live directly under the OneDrive root stage folders.",
        "Source-adjudication review packets live under `Meta/AI Adoption/03_source_adjudication/`.": "Source-adjudication review packets live under `03_source_adjudication/`.",
        "Private source packages and PDFs live under `Meta/AI Adoption/02_source_packages/` and must not be committed to Git.": "Private source packages and PDFs live under `02_source_packages/` and must not be committed to Git.",
        "OneDrive `Meta/AI Adoption` tree": "OneDrive root canonical tree",
        "`/Users/newhosung/Library/CloudStorage/OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity/AI Adoption Meta Analysis - Documents/Meta/AI Adoption`": f"`{BASE}`",
        "Meta/AI Adoption/00_INDEX": "00_INDEX",
        "Meta/AI Adoption/02_source_packages": "02_source_packages",
        "Meta/AI Adoption/05_manuscripts": "05_manuscripts",
        "Meta/AI Adoption/90_repository_mirror": "90_repository_mirror",
        "Meta/AI Adoption/99_archive": "99_archive",
    }
    update_text(BASE / "AGENTS.md", replacements, rows)
    update_text(ROOT_INDEX / "PROJECT_WORKSPACE_LAYOUT_20260614.md", replacements, rows)

    archive_empty_wrapper(rows)
    write_csv(MOVED_CSV, rows)
    write_readme(inventory_count, rows)

    print(f"inventory_rows={inventory_count}")
    print(f"log_rows={len(rows)}")
    print(f"moved_files={sum(int(row['file_count']) for row in rows if row['action'] == 'moved_verified')}")
    print(f"canonical_root={BASE}")


if __name__ == "__main__":
    main()
