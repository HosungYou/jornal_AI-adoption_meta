#!/usr/bin/env Rscript

suppressPackageStartupMessages({
  library(readr)
  library(dplyr)
  library(tidyr)
  library(purrr)
})

command_args <- commandArgs(trailingOnly = FALSE)
file_arg <- grep("^--file=", command_args, value = TRUE)
script_path <- if (length(file_arg) > 0) {
  normalizePath(sub("^--file=", "", file_arg[[1]]), mustWork = TRUE)
} else {
  normalizePath("scripts/llm_scoring_20260606/check_paper2_r_masem_readiness_20260611.R", mustWork = TRUE)
}
repo <- normalizePath(file.path(dirname(script_path), "..", ".."), mustWork = TRUE)
date_tag <- "20260611"
results_arg <- grep("^--results-dir=", command_args, value = TRUE)
results_dir <- if (length(results_arg) > 0) {
  normalizePath(sub("^--results-dir=", "", results_arg[[1]]), mustWork = FALSE)
} else {
  file.path(
    repo,
    "data/04_extraction/05_llm_masem_substitution/results/r_masem_readiness_20260611"
  )
}
dir.create(results_dir, recursive = TRUE, showWarnings = FALSE)

input_arg <- grep("^--input=", command_args, value = TRUE)
input_path <- if (length(input_arg) > 0) {
  normalizePath(sub("^--input=", "", input_arg[[1]]), mustWork = TRUE)
} else {
  file.path(
    repo,
    "data/04_extraction/05_llm_masem_substitution/results/paper2_masem_substitution_rerun_input_20260611.csv"
  )
}

required_packages <- c("readr", "dplyr", "tidyr", "purrr", "tibble", "OpenMx", "metaSEM", "Matrix", "jsonlite")
package_status <- tibble(
  package = required_packages,
  available = map_lgl(required_packages, requireNamespace, quietly = TRUE),
  version = map_chr(
    required_packages,
    \(pkg) if (requireNamespace(pkg, quietly = TRUE)) as.character(utils::packageVersion(pkg)) else NA_character_
  )
)

data <- read_csv(input_path, show_col_types = FALSE)
readiness <- data %>%
  mutate(
    sample_size_numeric = suppressWarnings(as.numeric(sample_size_numeric)),
    r_numeric = suppressWarnings(as.numeric(r_numeric)),
    has_sample_size = !is.na(sample_size_numeric),
    has_r = !is.na(r_numeric)
  )

overall <- tibble(
  metric = c(
    "total_rows",
    "rows_with_r_numeric",
    "rows_with_sample_size_numeric",
    "rows_missing_sample_size_numeric",
    "unique_studies",
    "unique_construct_pairs"
  ),
  value = c(
    nrow(readiness),
    sum(readiness$has_r),
    sum(readiness$has_sample_size),
    sum(!readiness$has_sample_size),
    n_distinct(readiness$study_id),
    n_distinct(readiness$construct_pair_canonical)
  )
)

by_scenario <- readiness %>%
  count(substitution_scenario, has_sample_size, name = "rows") %>%
  arrange(substitution_scenario, desc(has_sample_size))

by_action <- readiness %>%
  count(substitution_action, has_sample_size, name = "rows") %>%
  arrange(substitution_action, desc(has_sample_size))

package_csv <- file.path(results_dir, "paper2_r_package_status_20260611.csv")
overall_csv <- file.path(results_dir, "paper2_masem_readiness_overall_20260611.csv")
scenario_csv <- file.path(results_dir, "paper2_masem_readiness_by_scenario_20260611.csv")
action_csv <- file.path(results_dir, "paper2_masem_readiness_by_action_20260611.csv")
write_csv(package_status, package_csv)
write_csv(overall, overall_csv)
write_csv(by_scenario, scenario_csv)
write_csv(by_action, action_csv)

all_packages_available <- all(package_status$available)
sample_size_rows <- sum(readiness$has_sample_size)
missing_sample_size_rows <- sum(!readiness$has_sample_size)
sample_size_ready <- sample_size_rows == nrow(readiness)
stage_status <- if (all_packages_available && sample_size_ready) {
  "ready_for_full_tssem"
} else if (all_packages_available) {
  "r_environment_ready_input_sample_size_blocked"
} else {
  "r_environment_incomplete"
}

report <- c(
  "# Paper2 R/metaSEM Readiness Check",
  "",
  "Date: 2026-06-11",
  "",
  "## Status",
  "",
  paste0("- R version: ", R.version.string),
  paste0("- Platform: ", R.version$platform),
  paste0("- Stage status: `", stage_status, "`"),
  paste0("- Input file: `", input_path, "`"),
  paste0("- Required R packages available: ", sum(package_status$available), "/", nrow(package_status)),
  paste0("- Input rows: ", nrow(readiness)),
  paste0("- Rows with `r_numeric`: ", sum(readiness$has_r), "/", nrow(readiness)),
  paste0("- Rows with `sample_size_numeric`: ", sum(readiness$has_sample_size), "/", nrow(readiness)),
  paste0("- Rows missing `sample_size_numeric`: ", sum(!readiness$has_sample_size), "/", nrow(readiness)),
  "",
  "## Claim Boundary",
  "",
  if (sample_size_ready) {
    "The current input carries numeric sample sizes for all rows, so remaining TSSEM readiness depends on analysis-specification decisions rather than N coverage."
  } else {
    paste0(
      "The local R environment is ready for Paper2 meta-analytic scripting: `Rscript`, `OpenMx`, and `metaSEM` load successfully. The current input is not yet ready for an all-row final TSSEM Stage 1/Stage 2 claim because ",
      missing_sample_size_rows,
      " of ",
      nrow(readiness),
      " rows still lack numeric `sample_size_numeric`."
    )
  },
  "",
  "A documented missing-N exclusion rule can support N-weighted analyses on the eligible subset, but excluded missing-N rows must remain outside final TSSEM weighting until a later source check supplies numeric N. This evidence supports deterministic substitution-input readiness and pooled-correlation sensitivity checks, not final SEM path/model-fit stability.",
  "",
  "## Output Tables",
  "",
  "- `paper2_r_package_status_20260611.csv`",
  "- `paper2_masem_readiness_overall_20260611.csv`",
  "- `paper2_masem_readiness_by_scenario_20260611.csv`",
  "- `paper2_masem_readiness_by_action_20260611.csv`"
)

writeLines(report, file.path(results_dir, "PAPER2_R_MASEM_READINESS_20260611.md"))
cat(stage_status, "\n")
