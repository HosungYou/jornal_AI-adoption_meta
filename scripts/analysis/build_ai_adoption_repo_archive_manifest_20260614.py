#!/usr/bin/env python3
"""Build archive/sync manifests for AI Adoption repo restructuring.

This is an audit-first script. It does not delete or move files.
"""
from __future__ import annotations

import csv
import hashlib
import os
from pathlib import Path
from datetime import datetime, timezone

ACADEMIC_OLD = Path('/Users/newhosung/Academic/2026/AI Adoption Meta Analysis')
ACADEMIC_NEW = Path('/Users/newhosung/Academic/2026/AI Adoption Meta Analysis')
ONEDRIVE_BASE = Path('/Users/newhosung/Library/CloudStorage/OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity/AI Adoption Meta Analysis - Documents')
ONEDRIVE_OLD = ONEDRIVE_BASE / 'Git/journal_AI-adoption_meta'
ONEDRIVE_NEW = ONEDRIVE_BASE / 'Git/journal_AI-adoption_meta'
OUT_REPO = ACADEMIC_OLD / 'docs/08_operations/repo_restructure_20260614'
OUT_ONEDRIVE = ONEDRIVE_BASE / 'Meta/AI Adoption/99_archive/repo_restructure_20260614'
ACADEMIC_GIT_PARENT = ACADEMIC_OLD.parent
ONEDRIVE_GIT_PARENT = ONEDRIVE_BASE / 'Git'
HASH_LIMIT = 250 * 1024 * 1024

EXCLUDE_DIRS = {'.git'}
RUNTIME_PREFIXES = ('.omx/', '.longtable/',)
PRIVATE_MARKERS = (
    '/PDFs/', '/02_source_packages/', '/coder_packages/', '/returned_raw/', '/freeze_candidates/',
    '/raw_human_coder_data_freeze/', '/Review_Packets', '/Coding_Latest',
)
PRIVATE_EXTS = {'.pdf', '.docx', '.xlsx', '.xls', '.xlsm', '.zip'}
SHARE_SAFE_EXTS = {'.md', '.csv', '.tsv', '.json', '.bib', '.txt', '.url', '.py', '.R', '.r', '.sh', '.yml', '.yaml'}


def sha256(path: Path, size: int) -> str:
    if size > HASH_LIMIT:
        return f'SKIPPED_GT_{HASH_LIMIT}'
    h = hashlib.sha256()
    with path.open('rb') as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def classify(rel: str) -> str:
    posix = '/' + rel.replace(os.sep, '/')
    name = Path(rel).name
    suffix = Path(rel).suffix.lower()
    if rel.startswith('.git/') or rel == '.git':
        return 'git_internal_excluded'
    if rel.startswith(RUNTIME_PREFIXES) or rel in {'.DS_Store', 'CURRENT.md'}:
        return 'runtime_or_session_state'
    if any(marker in posix for marker in PRIVATE_MARKERS) or suffix in PRIVATE_EXTS:
        return 'private_or_binary_review_required'
    if suffix in SHARE_SAFE_EXTS:
        return 'share_safe_text_or_data'
    if name.startswith('~$') or name.endswith('.lock'):
        return 'lock_or_temp_file'
    return 'unclassified_review_required'


def walk_manifest(root: Path) -> dict[str, dict[str, str]]:
    manifest: dict[str, dict[str, str]] = {}
    if not root.exists():
        return manifest
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS]
        for filename in filenames:
            path = Path(dirpath) / filename
            try:
                stat = path.stat()
            except OSError:
                continue
            rel = str(path.relative_to(root))
            size = stat.st_size
            manifest[rel] = {
                'relpath': rel,
                'size': str(size),
                'mtime_ns': str(stat.st_mtime_ns),
                'sha256': sha256(path, size),
                'class': classify(rel),
            }
    return manifest


def write_csv(path: Path, rows: list[dict[str, str]], headers: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', newline='', encoding='utf-8') as handle:
        writer = csv.DictWriter(handle, fieldnames=headers, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(rows)


def parent_project_index() -> list[dict[str, str]]:
    acad = {p.name: p for p in ACADEMIC_GIT_PARENT.iterdir() if p.is_dir()} if ACADEMIC_GIT_PARENT.exists() else {}
    od = {p.name: p for p in ONEDRIVE_GIT_PARENT.iterdir() if p.is_dir()} if ONEDRIVE_GIT_PARENT.exists() else {}
    names = sorted(set(acad) | set(od))
    rows = []
    for name in names:
        if name in {'journal_AI-adoption_meta', 'journal_AI-adoption_meta'}:
            role = 'ai_adoption_target_restructure'
            rec = 'rename typo to journal_AI-adoption_meta; archive old OneDrive clone; create read-only mirror'
        elif name.startswith('.'):
            role = 'runtime_or_hidden_workspace'
            rec = 'do not delete automatically; review separately'
        else:
            role = 'unrelated_project_in_shared_git_parent'
            rec = 'do not move/delete in this task; add parent index only'
        rows.append({
            'project_dir_name': name,
            'exists_in_academic_git_parent': str(name in acad).lower(),
            'exists_in_onedrive_git_parent': str(name in od).lower(),
            'classification': role,
            'recommendation': rec,
        })
    return rows


def compare() -> tuple[list[dict[str, str]], dict[str, int]]:
    acad = walk_manifest(ACADEMIC_OLD)
    od = walk_manifest(ONEDRIVE_OLD)
    rels = sorted(set(acad) | set(od))
    rows = []
    counts = {
        'academic_files': len(acad),
        'onedrive_files': len(od),
        'same_rel_identical_hash': 0,
        'same_rel_different': 0,
        'academic_only': 0,
        'onedrive_only': 0,
        'private_or_binary_review_required': 0,
    }
    for rel in rels:
        a = acad.get(rel)
        o = od.get(rel)
        if a and o:
            if a['sha256'] == o['sha256'] and a['size'] == o['size']:
                status = 'same_relative_path_identical_content'
                rec = 'duplicate in old OneDrive clone; safe to remove from active Git area after archive snapshot'
                counts['same_rel_identical_hash'] += 1
            else:
                status = 'same_relative_path_different_content'
                rec = 'preserve old OneDrive version in archive snapshot; canonical Academic version wins for mirror unless researcher reopens'
                counts['same_rel_different'] += 1
        elif a:
            status = 'academic_only'
            rec = 'copy to new OneDrive mirror if not runtime; keep canonical in Academic'
            counts['academic_only'] += 1
        else:
            status = 'onedrive_only'
            rec = 'preserve in old OneDrive archive snapshot; do not promote into canonical without review'
            counts['onedrive_only'] += 1
        cls = (a or o or {}).get('class', 'unknown')
        if cls == 'private_or_binary_review_required':
            counts['private_or_binary_review_required'] += 1
        rows.append({
            'relpath': rel,
            'status': status,
            'classification': cls,
            'academic_size': a['size'] if a else '',
            'onedrive_size': o['size'] if o else '',
            'academic_sha256': a['sha256'] if a else '',
            'onedrive_sha256': o['sha256'] if o else '',
            'recommendation': rec,
        })
    return rows, counts


def main() -> None:
    OUT_REPO.mkdir(parents=True, exist_ok=True)
    OUT_ONEDRIVE.mkdir(parents=True, exist_ok=True)
    rows, counts = compare()
    project_rows = parent_project_index()
    headers = ['relpath','status','classification','academic_size','onedrive_size','academic_sha256','onedrive_sha256','recommendation']
    for out in [OUT_REPO, OUT_ONEDRIVE]:
        write_csv(out / 'ai_adoption_repo_pair_archive_manifest_20260614.csv', rows, headers)
        write_csv(out / 'git_parent_project_index_20260614.csv', project_rows, list(project_rows[0].keys()))
        summary = [
            '# AI Adoption repo restructure archive manifest',
            '',
            f'Date: {datetime.now(timezone.utc).isoformat()}',
            '',
            '## Canonical decision',
            '',
            f'- Canonical execution clone: `{ACADEMIC_NEW}`',
            f'- Old Academic typo path: `{ACADEMIC_OLD}`',
            f'- Old OneDrive active clone to archive: `{ONEDRIVE_OLD}`',
            f'- New OneDrive read-only mirror path: `{ONEDRIVE_NEW}`',
            '',
            '## Counts',
            '',
            *[f'- {k}: {v}' for k, v in counts.items()],
            '',
            '## Safety boundary',
            '',
            '- This manifest was generated before destructive cleanup.',
            '- Identical files in the old OneDrive clone are duplicate active-copy candidates, but the old clone should first be moved to an archive snapshot.',
            '- Different or OneDrive-only files must be preserved in the archive snapshot and not promoted into the canonical Academic clone without source review.',
            '- Parent `Git` folders contain many unrelated projects; they are indexed but not moved or deleted in this task.',
            '',
            '## Files',
            '',
            '- `ai_adoption_repo_pair_archive_manifest_20260614.csv`',
            '- `git_parent_project_index_20260614.csv`',
        ]
        (out / 'ARCHIVE_MANIFEST_README_20260614.md').write_text('\n'.join(summary) + '\n', encoding='utf-8')
    print('manifest_repo=' + str(OUT_REPO))
    print('manifest_onedrive=' + str(OUT_ONEDRIVE))
    for k, v in counts.items():
        print(f'{k}={v}')


if __name__ == '__main__':
    main()
