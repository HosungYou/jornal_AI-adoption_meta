# Drive Sync Verification - 2026-06-18

## Roots

- Local full clone: `/Users/newhosung/Documents/Codex/2026-06-18/google-drive-onedrive-library-cloudstorage-googledrive/work/AI_Adoption_Meta_Analysis_Documents_FULL_CLONE_20260618`
- Google Drive local sync target: `/Users/newhosung/Library/CloudStorage/GoogleDrive-newhosung@gmail.com/Other computers/My Mac/Pycharm/Hosung You_Google Drive/Academic/AI Adoption/AI Adoption Meta Analysis - Documents`

## Counts

- Local full clone files: 14147
- Google Drive local target files: 14175
- Missing from Google target: 0
- Extra in Google target: 28
- Size mismatches: 0

## Interpretation

The Google Drive local target contains every file from the local full clone when `Missing from Google target` and `Size mismatches` are both zero. Extra files are non-destructive leftovers already present in Google Drive and were not deleted.

## Boundary Checks

- Paper A folder was checked for Paper2/Paper B file-name patterns.
- Paper B folder was checked for Paper A working manuscript and A tracking file-name patterns.

## Generated Files

- `drive_sync_manifest_local_20260618.csv`
- `drive_sync_manifest_google_local_20260618.csv`
- `drive_sync_missing_from_google_20260618.txt`
- `drive_sync_extra_in_google_20260618.txt`
- `drive_sync_size_mismatch_20260618.txt`
