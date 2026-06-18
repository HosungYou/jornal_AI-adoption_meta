# AI Adoption Meta Analysis - Drive Sync Release Notes

Date: 2026-06-18

## Goal

OneDrive의 `AI Adoption Meta Analysis - Documents` 전체 자료를 유지하면서, Google Drive 공유 루트에도 같은 구조를 복제합니다. 동시에 연구자 작업 입구를 Paper A와 Paper B로 분리합니다.

## Canonical Roots

- OneDrive: `/Users/newhosung/Library/CloudStorage/OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity/AI Adoption Meta Analysis - Documents`
- Google Drive shared root: `https://drive.google.com/drive/folders/18QIScKKbkoAliH7R_9KUXatpTJmKCq9V`
- Google Drive parent shared folder: `https://drive.google.com/drive/folders/1QShrxAReX_u1EKE_ubd_MrRkae1OPcyY`

## Collaboration Entry Points

- `00_START_HERE`: 전체 작업 안내와 동기화 기준
- `01_Paper_A`: Paper A 전용 작업 입구
- `02_Paper_B`: Paper B 전용 작업 입구

## Preservation Rule

기존 OneDrive 상위 구조와 파일은 보존합니다. Paper별 폴더는 연구자가 자기 범위만 보도록 만든 작업 뷰입니다. 원본 전체 자료는 루트의 기존 구조에서도 계속 접근할 수 있습니다.

## Paper A Boundary

Paper A 폴더에는 Track Changes 작업원고, 원본 원고, A 작업보드, APA/JARS checklist, reference matrix, 결정로그, A source adjudication, A manuscript archive, A repository docs만 둡니다.

Paper A 폴더에는 Paper B/Paper2 consensus, direct-r analysis, R2/R3 analysis-ready 파일을 두지 않습니다.

## Paper B Boundary

Paper B 폴더에는 Paper2/Paper B reference standard candidates, analysis inputs/outputs, B status/requirements, B manuscript/repository docs, B source adjudication만 둡니다.

Paper B 폴더에는 Paper A Track Changes 원고, Paper A original, Paper A APA/JARS checklist, Paper A 포함판단 설명서를 두지 않습니다.

## Git Release Boundary

Git release는 구조와 검증 상태를 배포하기 위한 기록입니다. 전체 4.3GB 연구 자료는 Drive에 두고, Git에는 안내문, 매니페스트, 검증 로그, 재현 스크립트만 포함합니다.

## Verification Targets

- OneDrive and Google Drive root file counts match after non-destructive sync.
- Paper A folder contains no Paper B/Paper2 files.
- Paper B folder contains no Paper A working manuscript or A tracking files.
- Google Drive root is under folder ID `1QShrxAReX_u1EKE_ubd_MrRkae1OPcyY`.
- Git tag and GitHub release point to this sync note and manifest.
