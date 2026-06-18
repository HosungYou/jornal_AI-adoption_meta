# AI Adoption Meta Analysis - Paper A/B 분리 작업 안내

이 공유 루트는 연구자 협업을 위해 Paper A와 Paper B를 분리해 보여주는 작업 공간입니다. 전체 OneDrive 자료는 유지하되, 연구자는 Paper별 입구에서 자기 논문 관련 요구사항만 보도록 구성합니다.

## 현재 권장 입구

- Paper A: `01_Paper_A/`
- Paper B: `02_Paper_B/`

기존 `00_INDEX/2026-06-17_Paper_A_B_work_allocation/`은 앞서 만든 혼합형 작업 묶음입니다. 링크 호환성을 위해 그대로 두었지만, 새 작업은 Paper별 폴더에서 시작하는 것을 권장합니다.

## 구조 원칙

1. Paper A 폴더에는 Paper A 원고, Paper A 요구사항, Paper A tracking 파일만 둡니다.
2. Paper B 폴더에는 Paper B consensus/reference standard, analysis input/output, Paper B 상태 파일만 둡니다.
3. 공통 파일이나 전체 저장소 미러는 루트 또는 별도 공통 폴더에 두고, Paper A/B 폴더 안에는 섞지 않습니다.
4. Word 정본 원고는 `.docx`를 유지합니다. Google Docs 변환본을 별도 정본으로 만들지 않습니다.

## 전체 자료 보존 원칙

OneDrive 원본 전체 구조는 삭제하거나 축소하지 않습니다. Google Drive에는 OneDrive 루트의 기존 전체 구조와 Paper별 작업 입구를 함께 복제합니다.

OneDrive 원본에는 다음 상위 구조가 있습니다.

- `00_START_HERE`
- `01_Paper_A`
- `02_Paper_B`
- `00_INDEX`
- `01_workbooks`
- `02_source_packages`
- `03_source_adjudication`
- `04_analysis_outputs`
- `05_manuscripts`
- `90_repository_mirror`
- `99_archive`
- `Attachments`

## Paper별 분리

Paper A 작업자는 `01_Paper_A`만 열면 됩니다. 이 폴더에는 Paper B/Paper2 consensus 또는 analysis 파일을 넣지 않습니다.

Paper B 작업자는 `02_Paper_B`만 열면 됩니다. 이 폴더에는 Paper A Track Changes 원고나 Paper A APA/JARS tracking을 넣지 않습니다.

## Git 배포 원칙

GitHub에는 4.3GB 원자료를 일반 Git 파일로 직접 넣지 않습니다. Git 배포물에는 구조 안내, 매니페스트, 검증 기록, 재현 스크립트, release note를 둡니다. 전체 원자료의 정본은 OneDrive와 Google Drive 동기화 루트입니다.
