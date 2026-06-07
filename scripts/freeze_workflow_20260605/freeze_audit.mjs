import fs from "node:fs/promises";
import path from "node:path";
import { FileBlob, SpreadsheetFile } from "@oai/artifact-tool";

const repo = process.cwd();
const oneDriveRoot =
  "/Users/newhosung/Library/CloudStorage/OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity/AI Adoption Meta Analysis - Documents";
const aiAdoptionRoot = path.join(oneDriveRoot, "Meta/AI Adoption");

const targetStudies = new Set([
  "S014",
  "S021",
  "S056",
  "S072",
  "S092",
  "S121",
  "S195",
  "S202",
  "S206",
]);

const files = {
  r1FreezeCandidate: path.join(
    repo,
    "data/04_extraction/01_raw_human_coder_data_freeze/phase2/freeze_candidates/R1/AI_Adoption_MASEM_Coding_v3_R1_Phase0_1_2_freeze_candidate_20260525.xlsx",
  ),
  r1LatestOneDrive: path.join(
    aiAdoptionRoot,
    "Coding_Latest_R1_R4_20260605/AI_Adoption_MASEM_Coding_v3_R1_Phase0_1_2_20260425.xlsx",
  ),
  combinedReviewQueue: path.join(
    repo,
    "data/04_extraction/02_pre_adjudication_disagreement/combined/derived/combined_correlation_review_queue_20260525.csv",
  ),
  combinedCoderLong: path.join(
    repo,
    "data/04_extraction/02_pre_adjudication_disagreement/combined/derived/combined_coder_values_long_20260525.csv",
  ),
  phase2Candidates: path.join(
    repo,
    "data/04_extraction/03_source_document_adjudication/phase2/phase2_source_check_candidates_20260525.csv",
  ),
  paper1Primary: path.join(
    aiAdoptionRoot,
    "Paper1_MASEM_Working_20260605/07_analysis_ready/paper1_direct_r_primary_analysis_ready_20260605.csv",
  ),
  paper1Qc: path.join(
    aiAdoptionRoot,
    "Paper1_MASEM_Working_20260605/08_qc_reports/paper1_numeric_qc_20260605.csv",
  ),
  paper2TaskUnits: path.join(
    aiAdoptionRoot,
    "Paper2_LLM_Extraction_Working_20260605/08_llm_task_units/paper2_llm_task_units_labeled_pre_freeze_20260605.csv",
  ),
  paper2Consensus: path.join(
    aiAdoptionRoot,
    "Paper2_LLM_Extraction_Working_20260605/03_reference_standard_v2/Paper2_Unified_Human_Final_Consensus_Decisions_20260605_v2.csv",
  ),
};

function parseCsv(text) {
  const rows = [];
  let row = [];
  let cell = "";
  let inQuotes = false;
  for (let i = 0; i < text.length; i += 1) {
    const ch = text[i];
    const next = text[i + 1];
    if (inQuotes) {
      if (ch === '"' && next === '"') {
        cell += '"';
        i += 1;
      } else if (ch === '"') {
        inQuotes = false;
      } else {
        cell += ch;
      }
    } else if (ch === '"') {
      inQuotes = true;
    } else if (ch === ",") {
      row.push(cell);
      cell = "";
    } else if (ch === "\n") {
      row.push(cell.replace(/\r$/, ""));
      rows.push(row);
      row = [];
      cell = "";
    } else {
      cell += ch;
    }
  }
  if (cell.length || row.length) {
    row.push(cell.replace(/\r$/, ""));
    rows.push(row);
  }
  return rows;
}

async function readCsvObjects(file) {
  const text = await fs.readFile(file, "utf8");
  const rows = parseCsv(text.replace(/^\uFEFF/, ""));
  const header = rows.shift();
  return rows
    .filter((row) => row.some((value) => value !== ""))
    .map((row) => Object.fromEntries(header.map((key, index) => [key, row[index] ?? ""])));
}

async function inspectWorkbook(file) {
  const input = await FileBlob.load(file);
  const workbook = await SpreadsheetFile.importXlsx(input);
  const workbookSummary = await workbook.inspect({
    kind: "workbook",
    summary: "workbook structure",
  });
  return workbookSummary.ndjson;
}

function countBy(rows, key) {
  const counts = {};
  for (const row of rows) {
    const value = row[key] || "";
    counts[value] = (counts[value] || 0) + 1;
  }
  return counts;
}

async function main() {
  const [phase2, reviewQueue, coderLong, paper1Primary, paper1Qc, paper2TaskUnits] =
    await Promise.all([
      readCsvObjects(files.phase2Candidates),
      readCsvObjects(files.combinedReviewQueue),
      readCsvObjects(files.combinedCoderLong),
      readCsvObjects(files.paper1Primary),
      readCsvObjects(files.paper1Qc),
      readCsvObjects(files.paper2TaskUnits),
    ]);

  const targetPhase2 = phase2.filter((row) => targetStudies.has(row.study_id));
  const targetReview = reviewQueue.filter((row) => targetStudies.has(row.study_id));
  const targetCoderLong = coderLong.filter((row) => targetStudies.has(row.study_id));
  const paper1ReviewCandidates = paper1Primary.filter(
    (row) =>
      row.is_source_reported_or_direct === "0" ||
      row.is_model_derived_or_converted === "1" ||
      row.study_id === "S072",
  );
  const paper1S072Qc = paper1Qc.filter((row) => row.study_id === "S072");
  const paper2LabelCounts = countBy(paper2TaskUnits, "label_derivation_status");
  const paper2EvidenceCounts = countBy(paper2TaskUnits, "source_evidence_status");

  const workbookInspections = {};
  for (const [name, file] of Object.entries({
    r1FreezeCandidate: files.r1FreezeCandidate,
    r1LatestOneDrive: files.r1LatestOneDrive,
  })) {
    try {
      workbookInspections[name] = await inspectWorkbook(file);
    } catch (error) {
      workbookInspections[name] = `ERROR: ${error.message}`;
    }
  }

  const out = {
    generatedAt: new Date().toISOString(),
    files,
    workbookInspections,
    targetPhase2,
    targetReview,
    targetCoderLongCount: targetCoderLong.length,
    targetCoderLongSample: targetCoderLong.slice(0, 30),
    paper1ReviewCandidateCount: paper1ReviewCandidates.length,
    paper1ReviewCandidates,
    paper1S072Qc,
    paper2LabelCounts,
    paper2EvidenceCounts,
  };

  await fs.mkdir(path.join(repo, "data/04_extraction/03_source_document_adjudication/phase2"), {
    recursive: true,
  });
  const outPath = path.join(
    repo,
    "data/04_extraction/03_source_document_adjudication/phase2/source_freeze_audit_inventory_20260605.json",
  );
  await fs.writeFile(outPath, `${JSON.stringify(out, null, 2)}\n`);
  console.log(outPath);
  console.log(
    JSON.stringify(
      {
        targetPhase2: targetPhase2.length,
        targetReview: targetReview.length,
        targetCoderLong: targetCoderLong.length,
        paper1ReviewCandidateCount: paper1ReviewCandidates.length,
        paper2LabelCounts,
        paper2EvidenceCounts,
      },
      null,
      2,
    ),
  );
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
