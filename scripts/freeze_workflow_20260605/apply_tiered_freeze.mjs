import fs from "node:fs/promises";
import path from "node:path";
import crypto from "node:crypto";
import { FileBlob, SpreadsheetFile } from "@oai/artifact-tool";

const repo = process.cwd();
const oneDriveRoot =
  "/Users/newhosung/Library/CloudStorage/OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity/AI Adoption Meta Analysis - Documents";
const aiAdoptionRoot = path.join(oneDriveRoot, "Meta/AI Adoption");
const phase2Dir = path.join(repo, "data/04_extraction/03_source_document_adjudication/phase2");
const freezeDir = path.join(repo, "data/04_extraction/04_reference_standard_freeze");
const paper1FreezeDir = path.join(
  aiAdoptionRoot,
  "Paper1_MASEM_Working_20260605/09_model_ready_tiered_freeze",
);
const paper2FreezeDir = path.join(
  aiAdoptionRoot,
  "Paper2_LLM_Extraction_Working_20260605/09_reference_freeze",
);

const files = {
  repoR1FreezeCandidate: path.join(
    repo,
    "data/04_extraction/01_raw_human_coder_data_freeze/phase2/freeze_candidates/R1/AI_Adoption_MASEM_Coding_v3_R1_Phase0_1_2_freeze_candidate_20260525.xlsx",
  ),
  oneDriveR1Latest: path.join(
    aiAdoptionRoot,
    "Coding_Latest_R1_R4_20260605/AI_Adoption_MASEM_Coding_v3_R1_Phase0_1_2_20260425.xlsx",
  ),
  paper1Primary: path.join(
    aiAdoptionRoot,
    "Paper1_MASEM_Working_20260605/07_analysis_ready/paper1_direct_r_primary_analysis_ready_20260605.csv",
  ),
  paper2TaskUnits: path.join(
    aiAdoptionRoot,
    "Paper2_LLM_Extraction_Working_20260605/08_llm_task_units/paper2_llm_task_units_labeled_pre_freeze_20260605.csv",
  ),
  sourceEvidence: path.join(phase2Dir, "source_pdf_evidence_snippets_20260605.json"),
};

const today = "2026-06-05";

const workbookMutationTemplate = [
  {
    sheet: "STUDY_METADATA",
    range: "Y106:Z106",
    study_id: "S014",
    construct_pair: "PE-UB; SI-UB",
    old_value_source: "backup_workbook_same_range",
    new_value_summary:
      "Mark source-audited freeze; retain PE-UB/SI-UB as sensitivity-only indirect path evidence via perceived risk.",
    rationale:
      "Source confirms path-analysis evidence but not source-reported zero-order/direct-r correlations.",
  },
  {
    sheet: "STUDY_METADATA",
    range: "T112:Z112",
    study_id: "S195",
    construct_pair: "study_status",
    old_value_source: "backup_workbook_same_range",
    new_value_summary: "Set excluded_source_freeze with duplicate/unusable source-statistic rationale.",
    rationale:
      "Same DOI/PDF as S206; PLSR/component-loading or item-level evidence is not usable construct-level MASEM evidence.",
  },
  {
    sheet: "CORRELATIONS",
    range: "E6921:M6921",
    study_id: "S014",
    construct_pair: "PE-UB",
    old_value_source: "backup_workbook_same_range",
    new_value_summary: "Set beta_converted_sensitivity r=0.262 with source-audited freeze note.",
    rationale: "Indirect path via perceived risk is sensitivity-only, not primary direct-r.",
  },
  {
    sheet: "CORRELATIONS",
    range: "E6928:M6928",
    study_id: "S014",
    construct_pair: "SI-UB",
    old_value_source: "backup_workbook_same_range",
    new_value_summary: "Set beta_converted_sensitivity r=0.247 with source-audited freeze note.",
    rationale: "Indirect path via perceived risk is sensitivity-only, not primary direct-r.",
  },
  ...[7294, 7299, 7306, 7317, 7324].map((row) => ({
    sheet: "CORRELATIONS",
    range: `D${row}:M${row}`,
    study_id: "S195",
    construct_pair: "S195 correlation row",
    old_value_source: "backup_workbook_same_range",
    new_value_summary: "Set excluded_source_freeze and freeze rationale.",
    rationale:
      "Duplicate/unusable source-statistic evidence; same DOI/PDF as S206 and PLSR/component-loading or item-level source only.",
  })),
  {
    sheet: "EXCLUSION_LOG",
    range: "I10:I10",
    study_id: "S224",
    construct_pair: "exclusion_note",
    old_value_source: "repo freeze-candidate backup row 10",
    new_value_summary: "Restore original S224 source-check note in repo freeze candidate only.",
    rationale: "Preserve prior S224 exclusion note while applying the S195 freeze note to the correct row.",
    applies_to: "repo_freeze_candidate",
  },
  {
    sheet: "EXCLUSION_LOG",
    range: "I11:I11",
    study_id: "S195",
    construct_pair: "exclusion_note",
    old_value_source: "repo freeze-candidate backup row 11",
    new_value_summary: "Set S195 duplicate/unusable-source freeze note in repo freeze candidate.",
    rationale: "Apply source-audited exclusion note to existing S195 row.",
    applies_to: "repo_freeze_candidate",
  },
  {
    sheet: "EXCLUSION_LOG",
    range: "A10:I10",
    study_id: "S195",
    construct_pair: "exclusion_row",
    old_value_source: "OneDrive latest backup row 10 blank",
    new_value_summary: "Insert S195 exclusion row and freeze note in OneDrive working workbook.",
    rationale: "Mirror the source-audited exclusion in the active R1 working workbook.",
    applies_to: "onedrive_latest",
  },
  {
    sheet: "DISCREPANCY_LOG",
    range: "A2:J4",
    study_id: "S014; S195; S072",
    construct_pair: "PE-UB/SI-UB; study rows; ANX-EE",
    old_value_source: "backup_workbook_same_range",
    new_value_summary: "Record source-audited discrepancy resolutions for S014, S195, and S072.",
    rationale: "Keep workbook-visible audit trail for sensitivity-only, duplicate exclusion, and r=1.0 trace decisions.",
  },
];

const studyDecisions = [
  {
    study_id: "S014",
    decision: "retain_sensitivity_only",
    freeze_tier: "frozen_sensitivity_converted_indirect_path",
    model_eligibility: "exclude_primary_direct_r",
    scoring_eligibility: "eligible_converted_effect_size_after_locked_llm_output",
    source_locator: "S014.pdf; Table 4; path analysis",
    rationale:
      "R1 coded indirect effects through perceived risk. Source confirms path-analysis evidence, but these are not source-reported zero-order/direct-r correlations.",
  },
  {
    study_id: "S021",
    decision: "retain_sensitivity_only",
    freeze_tier: "frozen_sensitivity_pre_post_path_model",
    model_eligibility: "exclude_primary_direct_r",
    scoring_eligibility: "eligible_path_task_after_locked_llm_output",
    source_locator: "S021.pdf; structural paths; Supplementary Table S4/f2 path note",
    rationale:
      "Source reports pre/post genAI acceptance structural paths. Treat as path-model evidence with temporal-design labels, not as direct zero-order r.",
  },
  {
    study_id: "S056",
    decision: "retain_sensitivity_only",
    freeze_tier: "frozen_sensitivity_path_coefficients",
    model_eligibility: "exclude_primary_direct_r",
    scoring_eligibility: "eligible_path_task_after_locked_llm_output",
    source_locator: "S056.pdf; Table 3 path significance and coefficients",
    rationale:
      "Source Table 3 confirms standardized path coefficients for ChatGPT acceptance; usable for converted/path task family only.",
  },
  {
    study_id: "S072",
    decision: "exclude_r_abs_equals_1_primary",
    freeze_tier: "frozen_trace_influence_diagnostic_only",
    model_eligibility: "exclude_primary_direct_r",
    scoring_eligibility: "not_scorable_as_accuracy_answer",
    source_locator: "S072.pdf; Table 2 Fornell-Larcker/latent correlations; Table 3 path analysis",
    rationale:
      "The R3 ANX-EE r=1.0 value is incompatible with primary direct-r model input and likely reflects table/diagonal or construct-mapping confusion. User approved primary exclusion.",
  },
  {
    study_id: "S092",
    decision: "retain_sensitivity_only",
    freeze_tier: "frozen_sensitivity_sem_path_coefficients",
    model_eligibility: "exclude_primary_direct_r",
    scoring_eligibility: "eligible_path_task_after_locked_llm_output",
    source_locator: "S092.pdf; SEM results; Figure/Table path evidence",
    rationale:
      "Source confirms SEM/path evidence for ChatGPT adoption among students; preserve as converted/path task family, not primary zero-order r.",
  },
  {
    study_id: "S097",
    decision: "exclude_primary_source_statistic",
    freeze_tier: "frozen_sensitivity_source_statistic_only",
    model_eligibility: "exclude_primary_direct_r",
    scoring_eligibility: "eligible_source_statistic_task_after_locked_llm_output",
    source_locator: "S097.pdf; abstract/results mention correlations/regression",
    rationale:
      "Paper1 primary rows were source-blank/source-statistic review candidates. Keep as trace/sensitivity until an explicit direct-r table locator is locked.",
  },
  {
    study_id: "S121",
    decision: "retain_sensitivity_only",
    freeze_tier: "frozen_sensitivity_latent_sem_or_path",
    model_eligibility: "exclude_primary_direct_r",
    scoring_eligibility: "eligible_path_or_latent_task_after_locked_llm_output",
    source_locator: "S121.pdf; SEM/PLS-SEM results and Figure 2 path/correlation evidence",
    rationale:
      "Source confirms SEM/PLS-SEM evidence; retain in a separated path/latent tier and do not pool as direct observed zero-order r.",
  },
  {
    study_id: "S146",
    decision: "exclude_primary_source_statistic",
    freeze_tier: "frozen_sensitivity_source_statistic_only",
    model_eligibility: "exclude_primary_direct_r",
    scoring_eligibility: "eligible_source_statistic_task_after_locked_llm_output",
    source_locator: "S146.pdf; tables/source-statistic evidence",
    rationale:
      "Paper1 primary rows were source-blank/source-statistic review candidates. Keep as trace/sensitivity until an explicit direct-r table locator is locked.",
  },
  {
    study_id: "S184",
    decision: "exclude_primary_source_statistic",
    freeze_tier: "frozen_sensitivity_source_statistic_only",
    model_eligibility: "exclude_primary_direct_r",
    scoring_eligibility: "eligible_source_statistic_task_after_locked_llm_output",
    source_locator: "S184.pdf; SEM/facilitating-environment source evidence",
    rationale:
      "Paper1 FC-SI primary row was a source-blank/source-statistic review candidate. Keep as trace/sensitivity, not primary direct-r.",
  },
  {
    study_id: "S195",
    decision: "exclude_duplicate_source",
    freeze_tier: "frozen_excluded_duplicate_unusable_source_statistic",
    model_eligibility: "exclude_study",
    scoring_eligibility: "not_scorable_excluded_duplicate_source",
    source_locator: "S195.pdf; same DOI/PDF as S206; PLSR/component-loading evidence",
    rationale:
      "Same source/DOI as S206 and source uses PLSR component loadings/item-level evidence rather than usable construct-level MASEM statistics.",
  },
  {
    study_id: "S202",
    decision: "retain_sensitivity_only",
    freeze_tier: "frozen_sensitivity_fornell_larcker_or_path",
    model_eligibility: "exclude_primary_direct_r",
    scoring_eligibility: "eligible_latent_or_path_task_after_locked_llm_output",
    source_locator: "S202.pdf; Table 4 construct correlations; Table 5 path coefficients",
    rationale:
      "Source reports Fornell-Larcker-style latent correlations and SEM path coefficients. Preserve source type separation before MASEM/LLM scoring.",
  },
  {
    study_id: "S206",
    decision: "exclude_duplicate_source",
    freeze_tier: "frozen_excluded_duplicate_unusable_source_statistic",
    model_eligibility: "exclude_study",
    scoring_eligibility: "not_scorable_excluded_duplicate_source",
    source_locator: "S206.pdf; same DOI/PDF as S195; PLSR/component-loading evidence",
    rationale:
      "Same source/DOI as S195 and source uses PLSR component loadings/item-level evidence rather than usable construct-level MASEM statistics.",
  },
];

const studyDecisionById = new Map(studyDecisions.map((row) => [row.study_id, row]));
const paper1PrimaryExcludedPairs = new Set([
  "S097|ATT-EE",
  "S097|ATT-PE",
  "S072|ANX-EE",
  "S072|BI-PE",
  "S072|BI-UB",
  "S072|FC-UB",
  "S072|PE-UB",
  "S146|BI-EE",
  "S146|BI-PE",
  "S146|BI-SE",
  "S146|BI-SI",
  "S146|EE-PE",
  "S146|EE-SE",
  "S146|EE-SI",
  "S146|PE-SE",
  "S146|PE-SI",
  "S146|SE-SI",
  "S184|FC-SI",
]);

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

function toCsv(rows, header) {
  const escape = (value) => {
    const text = value == null ? "" : String(value);
    return /[",\n\r]/.test(text) ? `"${text.replaceAll('"', '""')}"` : text;
  };
  return [header, ...rows.map((row) => header.map((key) => row[key] ?? ""))]
    .map((row) => row.map(escape).join(","))
    .join("\n") + "\n";
}

async function readCsvObjects(file) {
  const text = await fs.readFile(file, "utf8");
  const rows = parseCsv(text.replace(/^\uFEFF/, ""));
  const header = rows.shift();
  return {
    header,
    rows: rows
      .filter((row) => row.some((value) => value !== ""))
      .map((row) => Object.fromEntries(header.map((key, index) => [key, row[index] ?? ""]))),
  };
}

async function sha256(file) {
  const data = await fs.readFile(file);
  return crypto.createHash("sha256").update(data).digest("hex");
}

function assertCells(sheetName, range, values, expected) {
  const row = values[0] || [];
  for (const { index, value, label } of expected) {
    if (row[index] !== value) {
      throw new Error(
        `Workbook identity check failed for ${sheetName}!${range}: expected ${label || index}=${value}, found ${row[index]}`,
      );
    }
  }
}

function assertWorkbookTargets({ metadata, correlations, exclusions, discrepancy, isRepoFreezeCandidate }) {
  assertCells("STUDY_METADATA", "A106:Z106", metadata.getRange("A106:Z106").values, [
    { index: 0, value: "S014", label: "study_id" },
  ]);
  assertCells("STUDY_METADATA", "A112:Z112", metadata.getRange("A112:Z112").values, [
    { index: 0, value: "S195", label: "study_id" },
  ]);
  for (const [range, c1, c2] of [
    ["A6921:M6921", "PE", "UB"],
    ["A6928:M6928", "SI", "UB"],
  ]) {
    assertCells("CORRELATIONS", range, correlations.getRange(range).values, [
      { index: 0, value: "S014", label: "study_id" },
      { index: 1, value: c1, label: "construct_1" },
      { index: 2, value: c2, label: "construct_2" },
    ]);
  }
  for (const [range, c1, c2] of [
    ["A7294:M7294", "BI", "PE"],
    ["A7299:M7299", "BI", "UB"],
    ["A7306:M7306", "EE", "UB"],
    ["A7317:M7317", "PE", "UB"],
    ["A7324:M7324", "SI", "UB"],
  ]) {
    assertCells("CORRELATIONS", range, correlations.getRange(range).values, [
      { index: 0, value: "S195", label: "study_id" },
      { index: 1, value: c1, label: "construct_1" },
      { index: 2, value: c2, label: "construct_2" },
    ]);
  }
  if (isRepoFreezeCandidate) {
    assertCells("EXCLUSION_LOG", "A10:I10", exclusions.getRange("A10:I10").values, [
      { index: 0, value: "S224", label: "study_id" },
    ]);
    assertCells("EXCLUSION_LOG", "A11:I11", exclusions.getRange("A11:I11").values, [
      { index: 0, value: "S195", label: "study_id" },
    ]);
  } else {
    const row10 = exclusions.getRange("A10:I10").values[0] || [];
    if (row10[0] && row10[0] !== "S195") {
      throw new Error(
        `Workbook identity check failed for EXCLUSION_LOG!A10:I10: expected blank or S195, found ${row10[0]}`,
      );
    }
  }
  assertCells("DISCREPANCY_LOG", "A2:J2", discrepancy.getRange("A2:J2").values, [
    { index: 0, value: "S014", label: "study_id" },
  ]);
  assertCells("DISCREPANCY_LOG", "A3:J3", discrepancy.getRange("A3:J3").values, [
    { index: 0, value: "S195", label: "study_id" },
  ]);
  assertCells("DISCREPANCY_LOG", "A4:J4", discrepancy.getRange("A4:J4").values, [
    { index: 0, value: "S072", label: "study_id" },
  ]);
}

async function validateSourceEvidence() {
  const evidence = JSON.parse(await fs.readFile(files.sourceEvidence, "utf8"));
  const missing = [];
  for (const { study_id } of studyDecisions) {
    const record = evidence[study_id];
    if (!record || record.status !== "pdf_found" || !Array.isArray(record.hits) || record.hits.length === 0) {
      missing.push(study_id);
    }
  }
  if (missing.length) {
    throw new Error(`Missing source PDF evidence hits for freeze decisions: ${missing.join(", ")}`);
  }
}

async function updateWorkbook(file) {
  const backup = `${file}.bak_20260605_tiered_freeze`;
  try {
    await fs.access(backup);
  } catch {
    await fs.copyFile(file, backup);
  }
  const workbook = await SpreadsheetFile.importXlsx(await FileBlob.load(file));
  const metadata = workbook.worksheets.getItem("STUDY_METADATA");
  const correlations = workbook.worksheets.getItem("CORRELATIONS");
  const exclusions = workbook.worksheets.getItem("EXCLUSION_LOG");
  const discrepancy = workbook.worksheets.getItem("DISCREPANCY_LOG");
  const isRepoFreezeCandidate = file.includes("/data/04_extraction/");

  assertWorkbookTargets({ metadata, correlations, exclusions, discrepancy, isRepoFreezeCandidate });

  metadata.getRange("Y106:Z106").values = [
    [
      "Y",
      "Freeze 2026-06-05: source-audited; retain PE-UB and SI-UB as sensitivity-only beta-converted indirect path evidence via perceived risk, not primary direct-r.",
    ],
  ];
  metadata.getRange("T112:Z112").values = [
    [
      "excluded_source_freeze",
      "not_addressed",
      "R1",
      46165,
      "Phase 2",
      "Y",
      "Freeze 2026-06-05: exclude. Same DOI/PDF as S206; source uses PLSR/component-loading or item-level evidence, not usable construct-level MASEM statistic.",
    ],
  ];

  correlations.getRange("E6921:M6921").values = [
    [
      "beta_converted_sensitivity",
      0.262,
      0,
      "p<.001",
      "Performance expectancy / perceived usefulness",
      "Use behavior / adoption",
      "Table 4",
      "Y",
      "Freeze 2026-06-05: sensitivity-only indirect path via perceived risk; exclude from primary direct-r.",
    ],
  ];
  correlations.getRange("E6928:M6928").values = [
    [
      "beta_converted_sensitivity",
      0.247,
      0.001,
      "p<.01",
      "Social influence",
      "Use behavior / adoption",
      "Table 4",
      "Y",
      "Freeze 2026-06-05: sensitivity-only indirect path via perceived risk; exclude from primary direct-r.",
    ],
  ];

  const s195Rows = [7294, 7299, 7306, 7317, 7324];
  for (const row of s195Rows) {
    correlations.getRange(`D${row}:M${row}`).values = [
      [
        null,
        "excluded_source_freeze",
        null,
        null,
        "excluded",
        null,
        null,
        "Figure 3/Table 3/Table 4",
        "Y",
        "Freeze 2026-06-05: excluded duplicate/unusable source-statistic evidence; same DOI/PDF as S206; PLSR/component-loading or item-level source only.",
      ],
    ];
  }

  if (isRepoFreezeCandidate) {
    exclusions.getRange("I10:I10").values = [["Source check 2026-05-25."]];
    exclusions.getRange("I11:I11").values = [
      [
        "Freeze 2026-06-05: confirmed exclusion; duplicate with S206 and unusable PLSR/component-loading/item-level evidence for construct-level MASEM.",
      ],
    ];
  } else {
    exclusions.getRange("A10:I10").values = [
      [
        "S195",
        "Patterson",
        2024,
        "Examining generative artificial intelligence adoption in academia: a UTAUT perspective",
        "data_extraction",
        "E-FT1",
        "Same DOI/PDF as S206. The source uses PLSR component loadings and an image-only item-level correlation matrix, not a usable construct-level inter-construct correlation matrix or standardized SEM/path table for the project model.",
        "review",
        "Freeze 2026-06-05: confirmed exclusion; duplicate with S206 and unusable PLSR/component-loading/item-level evidence for construct-level MASEM.",
      ],
    ];
  }

  const discrepancyRows = [
    [
      "S014",
      "PE-UB; SI-UB",
      "R1 beta-converted indirect paths",
      "R4 review_source/no coded value",
      "source_type_mismatch",
      "retain_sensitivity_only",
      "source-audited freeze",
      today,
      "Y",
      "Table 4 path-analysis evidence; indirect via perceived risk; not primary direct-r.",
    ],
    [
      "S195",
      "study and correlation rows",
      "R1 item/path-like values",
      "R4 excluded",
      "duplicate_source_unusable_statistic",
      "exclude_study",
      "source-audited freeze",
      today,
      "Y",
      "Same DOI/PDF as S206; PLSR/component-loading evidence only.",
    ],
    [
      "S072",
      "ANX-EE",
      "R3 r=1.0",
      "R4 source Table 2 value differs",
      "r_abs_equals_1_influence",
      "exclude_primary_trace_only",
      "source-audited freeze",
      today,
      "Y",
      "Approved user decision: remove r=1.0 from primary model input and keep as influence diagnostic/trace only.",
    ],
  ];
  discrepancy.getRange("A2:J4").values = discrepancyRows;

  const output = await SpreadsheetFile.exportXlsx(workbook);
  await output.save(file);
}

function paper1DecisionFor(row) {
  const key = `${row.study_id}|${row.construct_pair}`;
  if (paper1PrimaryExcludedPairs.has(key)) {
    if (key === "S072|ANX-EE") {
      return {
        freeze_tier: "frozen_trace_influence_diagnostic_only",
        include_primary_model_ready: "0",
        freeze_decision: "exclude_primary_r_abs_equals_1",
      };
    }
    return {
      freeze_tier: "frozen_sensitivity_source_statistic_only",
      include_primary_model_ready: "0",
      freeze_decision: "exclude_primary_source_statistic_review_candidate",
    };
  }
  return {
    freeze_tier: "frozen_primary_direct_or_direct_like",
    include_primary_model_ready: row.include_primary || "1",
    freeze_decision: "retain_primary",
  };
}

function paper2Tier(row) {
  if (["S195", "S206"].includes(row.study_id)) {
    return {
      freeze_tier: "frozen_excluded_duplicate_unusable_source_statistic",
      scoring_eligibility: "not_scorable_excluded_duplicate_source",
      denominator_family: "excluded_duplicate_source",
    };
  }
  if (row.study_id === "S072" && row.construct_pair === "ANX-EE") {
    return {
      freeze_tier: "frozen_trace_influence_diagnostic_only",
      scoring_eligibility: "not_scorable_r_abs_equals_1_primary_exclusion",
      denominator_family: "trace_influence_diagnostic",
    };
  }
  if (row.source_evidence_status === "source_pointer_present_no_evidence_text") {
    return {
      freeze_tier: "frozen_source_pointer_only_not_evidence_scored",
      scoring_eligibility: "not_scorable_for_evidence_text_accuracy",
      denominator_family: row.llm_task_family || "source_pointer_only",
    };
  }
  if (row.label_derivation_status === "not_derivable") {
    return {
      freeze_tier: "frozen_trace_not_derivable_not_scorable",
      scoring_eligibility: "not_scorable_reference_label_not_derivable",
      denominator_family: "not_derivable_trace",
    };
  }
  if ((row.llm_task_family || "").includes("converted") || (row.downstream_masem_impact || "").includes("sensitivity")) {
    return {
      freeze_tier: "frozen_sensitivity_converted_or_model_derived",
      scoring_eligibility: "eligible_after_locked_llm_output_with_source_type_denominator",
      denominator_family: row.llm_task_family || "converted_or_model_derived_effect_size",
    };
  }
  return {
    freeze_tier: "frozen_scorable_candidate_after_locked_llm_output",
    scoring_eligibility: "eligible_after_locked_llm_output",
    denominator_family: row.llm_task_family || "unspecified_task_family",
  };
}

async function writeArtifacts() {
  await validateSourceEvidence();

  await fs.mkdir(phase2Dir, { recursive: true });
  await fs.mkdir(freezeDir, { recursive: true });
  await fs.mkdir(paper1FreezeDir, { recursive: true });
  await fs.mkdir(paper2FreezeDir, { recursive: true });

  const decisionHeader = [
    "study_id",
    "decision",
    "freeze_tier",
    "model_eligibility",
    "scoring_eligibility",
    "source_locator",
    "rationale",
  ];
  const decisionCsv = toCsv(studyDecisions, decisionHeader);
  const decisionPaths = [
    path.join(phase2Dir, "source_adjudication_decisions_20260605.csv"),
    path.join(freezeDir, "source_adjudication_decisions_20260605.csv"),
    path.join(paper2FreezeDir, "source_adjudication_decisions_20260605.csv"),
  ];
  await Promise.all(decisionPaths.map((file) => fs.writeFile(file, decisionCsv)));

  const workbookMutationRows = [];
  for (const [workbook_id, file] of Object.entries({
    repo_freeze_candidate: files.repoR1FreezeCandidate,
    onedrive_latest: files.oneDriveR1Latest,
  })) {
    const backup_path = `${file}.bak_20260605_tiered_freeze`;
    for (const row of workbookMutationTemplate) {
      if (row.applies_to && row.applies_to !== workbook_id) {
        continue;
      }
      if (!row.applies_to && row.range === "I10:I10") {
        continue;
      }
      workbookMutationRows.push({
        workbook_id,
        workbook_path: file,
        backup_path,
        sheet: row.sheet,
        range: row.range,
        study_id: row.study_id,
        construct_pair: row.construct_pair,
        old_value_source: row.old_value_source,
        new_value_summary: row.new_value_summary,
        rationale: row.rationale,
      });
    }
  }
  const workbookMutationHeader = [
    "workbook_id",
    "workbook_path",
    "backup_path",
    "sheet",
    "range",
    "study_id",
    "construct_pair",
    "old_value_source",
    "new_value_summary",
    "rationale",
  ];
  const mutationManifest = toCsv(workbookMutationRows, workbookMutationHeader);
  const mutationManifestPaths = [
    path.join(freezeDir, "workbook_mutation_manifest_20260605.csv"),
    path.join(paper2FreezeDir, "workbook_mutation_manifest_20260605.csv"),
  ];
  await Promise.all(mutationManifestPaths.map((file) => fs.writeFile(file, mutationManifest)));

  const { header: paper1Header, rows: paper1Rows } = await readCsvObjects(files.paper1Primary);
  const paper1FrozenRows = paper1Rows.map((row) => ({ ...row, ...paper1DecisionFor(row) }));
  const paper1ModelReadyRows = paper1FrozenRows.filter((row) => row.include_primary_model_ready === "1");
  const paper1HeaderOut = [
    ...paper1Header,
    "freeze_tier",
    "include_primary_model_ready",
    "freeze_decision",
  ];
  const paper1AllPath = path.join(
    paper1FreezeDir,
    "paper1_direct_r_primary_tiered_freeze_decisions_20260605.csv",
  );
  const paper1ModelReadyPath = path.join(
    paper1FreezeDir,
    "paper1_direct_r_primary_model_ready_tiered_freeze_20260605.csv",
  );
  await fs.writeFile(paper1AllPath, toCsv(paper1FrozenRows, paper1HeaderOut));
  await fs.writeFile(paper1ModelReadyPath, toCsv(paper1ModelReadyRows, paper1HeaderOut));

  const { header: paper2Header, rows: paper2Rows } = await readCsvObjects(files.paper2TaskUnits);
  const paper2FrozenRows = paper2Rows.map((row) => {
    const tier = paper2Tier(row);
    return {
      ...row,
      reference_standard_status: "source_anchored_human_reference_tiered_frozen_20260605",
      llm_scoring_status: "not_scored_no_locked_llm_output",
      freeze_tier: tier.freeze_tier,
      scoring_eligibility: tier.scoring_eligibility,
      denominator_family: tier.denominator_family,
    };
  });
  const paper2HeaderOut = [
    ...paper2Header,
    "freeze_tier",
    "scoring_eligibility",
    "denominator_family",
  ];
  const paper2FrozenPath = path.join(
    paper2FreezeDir,
    "paper2_llm_task_units_labeled_tiered_freeze_20260605.csv",
  );
  await fs.writeFile(paper2FrozenPath, toCsv(paper2FrozenRows, paper2HeaderOut));

  const counts = {
    paper1_primary_input_rows: paper1Rows.length,
    paper1_primary_model_ready_rows: paper1ModelReadyRows.length,
    paper1_primary_excluded_rows: paper1Rows.length - paper1ModelReadyRows.length,
    paper2_task_unit_rows: paper2Rows.length,
    paper2_freeze_tier_counts: Object.fromEntries(
      Object.entries(
        paper2FrozenRows.reduce((acc, row) => {
          acc[row.freeze_tier] = (acc[row.freeze_tier] || 0) + 1;
          return acc;
        }, {}),
      ).sort(),
    ),
    paper2_denominator_counts: Object.fromEntries(
      Object.entries(
        paper2FrozenRows.reduce((acc, row) => {
          acc[row.denominator_family] = (acc[row.denominator_family] || 0) + 1;
          return acc;
        }, {}),
      ).sort(),
    ),
  };

  const freezeNote = `# Paper2 Reference Standard Freeze Note

Date: ${today}

This packet freezes the current source-audited human reference layer as a tiered reference standard for downstream audit, denominator design, and scoring preparation. It does not claim that all 8,783 task units are one LLM accuracy denominator, and it does not start final LLM accuracy or MASEM substitution analysis because locked LLM outputs are not present.

## Freeze rule

- Raw returned coder workbooks remain preserved as raw returns.
- The R1 freeze-candidate/working workbook was updated where R1-owned Phase 2 rows required source-audited freeze handling.
- Final analysis should use the frozen reference layer and decision logs, not silent raw-return overwrites.
- Rows are frozen as trace records, scorable candidates, sensitivity-only evidence, source-pointer-only records, not-derivable records, or excluded records.

## Source decisions

- S014: retained as sensitivity-only beta-converted indirect path evidence through perceived risk; excluded from primary direct-r.
- S021: retained as pre/post path-model evidence; excluded from primary direct-r.
- S056: retained as path-coefficient evidence from Table 3; excluded from primary direct-r.
- S072: ANX-EE r=1.0 excluded from primary and retained only as trace/influence diagnostic.
- S092: retained as SEM/path evidence; excluded from primary direct-r.
- S097, S146, S184: Paper1 source-blank/source-statistic review candidates excluded from primary direct-r and retained only as trace/sensitivity candidates until direct-r source locators are locked.
- S121: retained as latent SEM/path evidence with source-type separation.
- S195/S206: excluded as duplicate same DOI/PDF source with unusable PLSR/component-loading or item-level evidence for construct-level MASEM.
- S202: retained as Fornell-Larcker/path evidence with source-type separation.

## Counts

- Paper1 primary input rows: ${counts.paper1_primary_input_rows}
- Paper1 primary model-ready rows after tiered freeze: ${counts.paper1_primary_model_ready_rows}
- Paper1 primary excluded rows after tiered freeze: ${counts.paper1_primary_excluded_rows}
- Paper2 task units frozen: ${counts.paper2_task_unit_rows}

## Paper2 denominator boundary

Do not use 8,783 as a single accuracy denominator. Use \`denominator_family\` and \`scoring_eligibility\` in \`paper2_llm_task_units_labeled_tiered_freeze_20260605.csv\`. Not-derivable rows and source-pointer-only rows remain frozen as trace records but are not scored as final evidence-content accuracy rows.

## Locked LLM boundary

No final LLM accuracy, substitution, or empirical validity claim is made in this freeze. Accuracy analysis requires a locked model/run/output file and the scoring rule to be applied by task family.
`;

  const freezeNotePaths = [
    path.join(freezeDir, "paper2_reference_standard_freeze_note.md"),
    path.join(paper2FreezeDir, "paper2_reference_standard_freeze_note.md"),
  ];
  await Promise.all(freezeNotePaths.map((file) => fs.writeFile(file, freezeNote)));

  const manifestRows = [];
  for (const file of [
    ...decisionPaths,
    ...mutationManifestPaths,
    paper1AllPath,
    paper1ModelReadyPath,
    paper2FrozenPath,
    ...freezeNotePaths,
  ]) {
    manifestRows.push({
      file,
      bytes: String((await fs.stat(file)).size),
      sha256: await sha256(file),
    });
  }
  for (const file of [
    files.repoR1FreezeCandidate,
    `${files.repoR1FreezeCandidate}.bak_20260605_tiered_freeze`,
    files.oneDriveR1Latest,
    `${files.oneDriveR1Latest}.bak_20260605_tiered_freeze`,
  ]) {
    manifestRows.push({
      file,
      bytes: String((await fs.stat(file)).size),
      sha256: await sha256(file),
    });
  }
  const manifest = toCsv(manifestRows, ["file", "bytes", "sha256"]);
  await fs.writeFile(path.join(freezeDir, "CHECKSUMS_TIERED_FREEZE_20260605.csv"), manifest);
  await fs.writeFile(path.join(paper2FreezeDir, "CHECKSUMS_TIERED_FREEZE_20260605.csv"), manifest);
  return counts;
}

async function main() {
  await updateWorkbook(files.repoR1FreezeCandidate);
  await updateWorkbook(files.oneDriveR1Latest);
  const counts = await writeArtifacts();
  console.log(JSON.stringify(counts, null, 2));
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
