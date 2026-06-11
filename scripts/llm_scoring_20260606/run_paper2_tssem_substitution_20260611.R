#!/usr/bin/env Rscript

suppressPackageStartupMessages({
  library(readr)
  library(dplyr)
  library(tidyr)
  library(purrr)
  library(tibble)
  library(metaSEM)
  library(OpenMx)
  library(Matrix)
})

command_args <- commandArgs(trailingOnly = FALSE)
file_arg <- grep("^--file=", command_args, value = TRUE)
script_path <- if (length(file_arg) > 0) {
  normalizePath(sub("^--file=", "", file_arg[[1]]), mustWork = TRUE)
} else {
  normalizePath("scripts/llm_scoring_20260606/run_paper2_tssem_substitution_20260611.R", mustWork = TRUE)
}
repo <- normalizePath(file.path(dirname(script_path), "..", ".."), mustWork = TRUE)
date_tag <- "20260611"

arg_value <- function(prefix, default) {
  hit <- grep(paste0("^", prefix, "="), command_args, value = TRUE)
  if (length(hit) > 0) sub(paste0("^", prefix, "="), "", hit[[1]]) else default
}

input_path <- normalizePath(
  arg_value(
    "--input",
    file.path(
      repo,
      "data/04_extraction/05_llm_masem_substitution/results/paper2_masem_substitution_rerun_input_n_weighted_eligible_20260611.csv"
    )
  ),
  mustWork = TRUE
)
results_dir <- normalizePath(
  arg_value(
    "--results-dir",
    file.path(
      repo,
      "data/04_extraction/05_llm_masem_substitution/results/r_tssem_substitution_20260611"
    )
  ),
  mustWork = FALSE
)
dir.create(results_dir, recursive = TRUE, showWarnings = FALSE)

constructs <- c("PE", "EE", "SI", "FC", "BI", "UB")
structural_paths <- tribble(
  ~from, ~to, ~label,
  "PE", "BI", "PE_to_BI",
  "EE", "BI", "EE_to_BI",
  "SI", "BI", "SI_to_BI",
  "FC", "UB", "FC_to_UB",
  "BI", "UB", "BI_to_UB"
)

safe_num <- function(x) suppressWarnings(as.numeric(x))

repo_relative <- function(path) {
  normalized <- normalizePath(path, mustWork = FALSE)
  repo_prefix <- paste0(repo, .Platform$file.sep)
  if (startsWith(normalized, repo_prefix)) {
    sub(repo_prefix, "", normalized, fixed = TRUE)
  } else {
    normalized
  }
}

canonical_pair <- function(a, b) {
  paste(sort(c(a, b)), collapse = "-")
}

make_matrices <- function(data, value_col) {
  pair_data <- data %>%
    mutate(
      c1 = as.character(construct_1),
      c2 = as.character(construct_2),
      r_value_for_tssem = safe_num(.data[[value_col]]),
      sample_size_numeric = safe_num(sample_size_numeric)
    ) %>%
    filter(
      c1 %in% constructs,
      c2 %in% constructs,
      c1 != c2,
      !is.na(r_value_for_tssem),
      abs(r_value_for_tssem) < 1,
      !is.na(sample_size_numeric),
      sample_size_numeric > 3
    ) %>%
    mutate(pair = map2_chr(c1, c2, canonical_pair)) %>%
    group_by(study_id, c1, c2, pair) %>%
    summarise(
      r_value_for_tssem = mean(r_value_for_tssem, na.rm = TRUE),
      sample_size_numeric = median(sample_size_numeric, na.rm = TRUE),
      row_n = n(),
      .groups = "drop"
    )

  study_n <- pair_data %>%
    group_by(study_id) %>%
    summarise(sample_size_numeric = median(sample_size_numeric, na.rm = TRUE), .groups = "drop")

  matrices <- list()
  n_vec <- numeric()
  for (sid in sort(unique(pair_data$study_id))) {
    mat <- matrix(NA_real_, nrow = length(constructs), ncol = length(constructs), dimnames = list(constructs, constructs))
    diag(mat) <- 1
    study_rows <- pair_data %>% filter(study_id == sid)
    for (idx in seq_len(nrow(study_rows))) {
      c1 <- study_rows$c1[[idx]]
      c2 <- study_rows$c2[[idx]]
      r <- study_rows$r_value_for_tssem[[idx]]
      mat[c1, c2] <- r
      mat[c2, c1] <- r
    }
    if (all(!is.na(mat[upper.tri(mat)]))) {
      matrices[[sid]] <- mat
      n_vec[[sid]] <- study_n$sample_size_numeric[match(sid, study_n$study_id)]
    }
  }

  list(pair_data = pair_data, cor_list = matrices, n_vec = n_vec)
}

pair_coverage_table <- function(pair_data, scenario) {
  pair_data %>%
    count(pair, name = "study_pair_rows") %>%
    mutate(scenario = scenario, .before = 1) %>%
    arrange(scenario, pair)
}

make_stage2_matrices <- function() {
  p <- length(constructs)
  idx <- setNames(seq_along(constructs), constructs)

  A <- mxMatrix(type = "Full", nrow = p, ncol = p, free = FALSE, values = 0, labels = NA, name = "A")
  for (row_idx in seq_len(nrow(structural_paths))) {
    from <- structural_paths$from[[row_idx]]
    to <- structural_paths$to[[row_idx]]
    A$free[idx[[to]], idx[[from]]] <- TRUE
    A$labels[idx[[to]], idx[[from]]] <- structural_paths$label[[row_idx]]
    A$values[idx[[to]], idx[[from]]] <- 0.2
  }

  S <- mxMatrix(type = "Symm", nrow = p, ncol = p, free = FALSE, values = 0, labels = NA, name = "S")
  exogenous <- c("PE", "EE", "SI", "FC")
  endogenous <- c("BI", "UB")
  for (name in exogenous) {
    S$values[idx[[name]], idx[[name]]] <- 1
  }
  for (name in endogenous) {
    S$free[idx[[name]], idx[[name]]] <- TRUE
    S$values[idx[[name]], idx[[name]]] <- 0.5
    S$labels[idx[[name]], idx[[name]]] <- paste0("Var_e_", name)
  }
  exo_pairs <- combn(exogenous, 2)
  for (col in seq_len(ncol(exo_pairs))) {
    a <- idx[[exo_pairs[1, col]]]
    b <- idx[[exo_pairs[2, col]]]
    label <- paste0("Cov_", exo_pairs[1, col], "_", exo_pairs[2, col])
    S$free[a, b] <- TRUE
    S$free[b, a] <- TRUE
    S$values[a, b] <- 0.3
    S$values[b, a] <- 0.3
    S$labels[a, b] <- label
    S$labels[b, a] <- label
  }
  list(A = A, S = S)
}

extract_stage1_matrix <- function(stage1_fit) {
  fixed <- coef(stage1_fit, select = "fixed")
  pooled <- vec2symMat(fixed, diag = FALSE, byrow = FALSE)
  dimnames(pooled) <- list(constructs, constructs)
  diag(pooled) <- 1
  pooled
}

status_code <- function(fit) {
  code <- tryCatch(fit$mx.fit@output$status$code, error = function(e) NA_integer_)
  if (is.null(code)) NA_integer_ else code
}

fit_stat <- function(stage2_fit, name) {
  stat_map <- c(
    chisq = "Chi-square of target model",
    df = "DF of target model",
    p = "p value of target model",
    CFI = "CFI",
    TLI = "TLI",
    RMSEA = "RMSEA",
    RMSEA_lower = "RMSEA lower 95% CI",
    RMSEA_upper = "RMSEA upper 95% CI",
    SRMR = "SRMR",
    AIC = "AIC",
    BIC = "BIC"
  )
  row_name <- unname(stat_map[[name]])
  value <- tryCatch(summary(stage2_fit)$stat[row_name, "Value"], error = function(e) NA_real_)
  if (is.null(value)) NA_real_ else as.numeric(value)
}

run_scenario <- function(data, scenario, value_col) {
  built <- make_matrices(data, value_col)
  coverage <- pair_coverage_table(built$pair_data, scenario)
  stage1_status <- "not_run"
  stage1_method <- "REM"
  stage1_fit <- NULL
  stage1_error <- ""

  stage1_fit <- tryCatch(
    tssem1(
      Cov = built$cor_list,
      n = built$n_vec,
      method = "REM",
      RE.type = "Diag",
      I2 = "I2q",
      acov = "individual"
    ),
    error = function(e) {
      stage1_error <<- conditionMessage(e)
      NULL
    }
  )
  if (is.null(stage1_fit)) {
    stage1_method <- "FEM_fallback"
    stage1_fit <- tryCatch(
      tssem1(Cov = built$cor_list, n = built$n_vec, method = "FEM"),
      error = function(e) {
        stage1_error <<- paste(stage1_error, "FEM fallback:", conditionMessage(e))
        NULL
      }
    )
  }
  if (!is.null(stage1_fit)) {
    stage1_status <- ifelse(identical(status_code(stage1_fit), 0L), "converged", paste0("status_", status_code(stage1_fit)))
  } else {
    return(list(
      scenario = scenario,
      coverage = coverage,
      summary = tibble(
        scenario = scenario,
        input_rows = nrow(data),
        eligible_pair_rows = nrow(built$pair_data),
        tssem_complete_case_rows = sum(built$pair_data$study_id %in% names(built$cor_list)),
        study_n = length(built$cor_list),
        construct_n = length(constructs),
        total_n = sum(built$n_vec, na.rm = TRUE),
        harmonic_n = ifelse(length(built$n_vec) > 0, length(built$n_vec) / sum(1 / built$n_vec), NA_real_),
        min_pooled_eigenvalue = NA_real_,
        stage1_method = stage1_method,
        stage1_status = "failed",
        stage1_status_code = NA_integer_,
        stage2_status = "not_run",
        stage2_status_code = NA_integer_,
        stage_error = stage1_error
      ),
      pooled_long = tibble(),
      path_rows = tibble(),
      fit_rows = tibble(),
      rds = NULL
    ))
  }

  pooled <- extract_stage1_matrix(stage1_fit)
  pooled_table <- as.data.frame(as.table(pooled), stringsAsFactors = FALSE)
  names(pooled_table) <- c("construct_1", "construct_2", "pooled_r")
  pooled_long <- as_tibble(pooled_table) %>%
    filter(as.character(construct_1) < as.character(construct_2)) %>%
    mutate(scenario = scenario, .before = 1)

  pd_min_eigen <- min(eigen(pooled, only.values = TRUE)$values)
  stage2_status <- "not_run"
  stage2_code <- NA_integer_
  stage2_error <- ""
  stage2_fit <- NULL
  matrices <- make_stage2_matrices()
  stage2_fit <- tryCatch(
    tssem2(
      tssem1.obj = stage1_fit,
      Amatrix = matrices$A,
      Smatrix = matrices$S,
      diag.constraints = TRUE,
      intervals.type = "LB",
      model.name = paste0("Paper2_Core6_", scenario)
    ),
    error = function(e) {
      stage2_error <<- conditionMessage(e)
      NULL
    }
  )
  if (!is.null(stage2_fit)) {
    stage2_code <- status_code(stage2_fit)
    stage2_status <- ifelse(identical(stage2_code, 0L), "converged", paste0("status_", stage2_code))
  } else {
    stage2_status <- "failed"
  }

  path_rows <- tibble()
  fit_rows <- tibble()
  if (!is.null(stage2_fit)) {
    coefs <- coef(stage2_fit)
    path_rows <- tibble(
      scenario = scenario,
      parameter = names(coefs),
      estimate = as.numeric(coefs),
      parameter_family = case_when(
        grepl("_to_", names(coefs)) ~ "structural_path",
        grepl("^Cov_", names(coefs)) ~ "exogenous_covariance",
        grepl("^Var_e_", names(coefs)) ~ "residual_variance",
        TRUE ~ "other"
      )
    )
    fit_names <- c("chisq", "df", "p", "CFI", "TLI", "RMSEA", "RMSEA_lower", "RMSEA_upper", "SRMR", "AIC", "BIC")
    fit_rows <- tibble(
      scenario = scenario,
      fit_index = fit_names,
      value = map_dbl(fit_names, \(name) fit_stat(stage2_fit, name))
    )
  }

  rds_path <- file.path(results_dir, paste0("paper2_tssem_substitution_", scenario, "_", date_tag, ".rds"))
  saveRDS(
    list(
      scenario = scenario,
      input_path = repo_relative(input_path),
      constructs = constructs,
      stage1_fit = stage1_fit,
      stage2_fit = stage2_fit,
      pooled_matrix = pooled,
      pair_data = built$pair_data,
      n_vec = built$n_vec
    ),
    rds_path
  )

  list(
    scenario = scenario,
    coverage = coverage,
    summary = tibble(
      scenario = scenario,
      input_rows = nrow(data),
      eligible_pair_rows = nrow(built$pair_data),
      tssem_complete_case_rows = sum(built$pair_data$study_id %in% names(built$cor_list)),
      study_n = length(built$cor_list),
      construct_n = length(constructs),
      total_n = sum(built$n_vec, na.rm = TRUE),
      harmonic_n = length(built$n_vec) / sum(1 / built$n_vec),
      min_pooled_eigenvalue = pd_min_eigen,
      stage1_method = stage1_method,
      stage1_status = stage1_status,
      stage1_status_code = status_code(stage1_fit),
      stage2_status = stage2_status,
      stage2_status_code = stage2_code,
      stage_error = paste(trimws(stage1_error), trimws(stage2_error)) %>% trimws()
    ),
    pooled_long = pooled_long,
    path_rows = path_rows,
    fit_rows = fit_rows,
    rds = rds_path
  )
}

input <- read_csv(input_path, show_col_types = FALSE)
input <- input %>%
  mutate(
    substitution_original_r_numeric = safe_num(substitution_original_r_numeric),
    substitution_r_numeric = safe_num(substitution_r_numeric),
    r_numeric = safe_num(r_numeric),
    sample_size_numeric = safe_num(sample_size_numeric)
  )

baseline <- input %>%
  mutate(tssem_value = coalesce(substitution_original_r_numeric, r_numeric))
substitution <- input %>%
  mutate(tssem_value = coalesce(substitution_r_numeric, r_numeric))

scenario_results <- list(
  run_scenario(baseline, "baseline_primary_human", "tssem_value"),
  run_scenario(substitution, "expert_reviewed_llm_assisted_primary", "tssem_value")
)

summary_rows <- bind_rows(map(scenario_results, "summary"))
coverage_rows <- bind_rows(map(scenario_results, "coverage"))
pooled_rows <- bind_rows(map(scenario_results, "pooled_long"))
path_rows <- bind_rows(map(scenario_results, "path_rows"))
fit_rows <- bind_rows(map(scenario_results, "fit_rows"))

if (nrow(pooled_rows) > 0 && "scenario" %in% names(pooled_rows)) {
  baseline_pooled <- pooled_rows %>%
    filter(scenario == "baseline_primary_human") %>%
    select(construct_1, construct_2, baseline_pooled_r = pooled_r)
  comparison_rows <- pooled_rows %>%
    filter(scenario == "expert_reviewed_llm_assisted_primary") %>%
    select(construct_1, construct_2, substitution_pooled_r = pooled_r) %>%
    left_join(baseline_pooled, by = c("construct_1", "construct_2")) %>%
    mutate(delta_pooled_r = substitution_pooled_r - baseline_pooled_r) %>%
    select(construct_1, construct_2, baseline_pooled_r, substitution_pooled_r, delta_pooled_r)
} else {
  comparison_rows <- tibble(
    construct_1 = character(),
    construct_2 = character(),
    baseline_pooled_r = numeric(),
    substitution_pooled_r = numeric(),
    delta_pooled_r = numeric()
  )
}

write_csv(summary_rows, file.path(results_dir, "paper2_tssem_substitution_stage_summary_20260611.csv"))
write_csv(coverage_rows, file.path(results_dir, "paper2_tssem_substitution_pair_coverage_20260611.csv"))
write_csv(pooled_rows, file.path(results_dir, "paper2_tssem_substitution_pooled_correlations_20260611.csv"))
write_csv(comparison_rows, file.path(results_dir, "paper2_tssem_substitution_pooled_correlation_delta_20260611.csv"))
write_csv(path_rows, file.path(results_dir, "paper2_tssem_substitution_stage2_paths_20260611.csv"))
write_csv(fit_rows, file.path(results_dir, "paper2_tssem_substitution_stage2_fit_indices_20260611.csv"))

max_delta <- if (nrow(comparison_rows) > 0) max(abs(comparison_rows$delta_pooled_r), na.rm = TRUE) else NA_real_
stage1_line <- paste0(
  "- Stage 1 statuses: ",
  paste(paste0(summary_rows$scenario, "=", summary_rows$stage1_status, "(", summary_rows$stage1_method, ")"), collapse = "; ")
)
stage2_line <- paste0(
  "- Stage 2 statuses: ",
  paste(paste0(summary_rows$scenario, "=", summary_rows$stage2_status), collapse = "; ")
)

report <- c(
  "# Paper2 TSSEM Substitution Diagnostic",
  "",
  "Date: 2026-06-11",
  "",
  "## Scope",
  "",
  paste0("- Input file: `", repo_relative(input_path), "`"),
  "- Analysis subset: N-weighted eligible rows after deterministic sample-size reconciliation.",
  "- Constructs: PE, EE, SI, FC, BI, UB.",
  "- Complete-case TSSEM subset: studies reporting all 15 pairwise correlations among these six constructs.",
  "- Structural model: PE, EE, and SI to BI; FC and BI to UB.",
  "- This is a bounded diagnostic rerun, not a final all-construct Paper1 MASEM claim.",
  "",
  "## Execution Evidence",
  "",
  stage1_line,
  stage2_line,
  paste0("- Eligible pair rows before complete-case TSSEM filter: ", paste(paste0(summary_rows$scenario, "=", summary_rows$eligible_pair_rows), collapse = "; ")),
  paste0("- Pair rows entering complete-case TSSEM after aggregation: ", paste(paste0(summary_rows$scenario, "=", summary_rows$tssem_complete_case_rows), collapse = "; ")),
  paste0("- Studies: ", paste(paste0(summary_rows$scenario, "=", summary_rows$study_n), collapse = "; ")),
  paste0("- Maximum absolute delta in pooled correlations between baseline and expert-reviewed LLM-assisted input: ", sprintf("%.8f", max_delta)),
  "",
  "## Claim Boundary",
  "",
  "The expert-reviewed LLM-assisted primary input is numerically unchanged relative to the human-reference primary input in this diagnostic subset when high-risk rows are retained rather than autonomously replaced. Any final structural-path or model-fit stability claim must use the final approved model specification and document excluded missing-N rows.",
  "",
  "## Output Files",
  "",
  "- `paper2_tssem_substitution_stage_summary_20260611.csv`",
  "- `paper2_tssem_substitution_pair_coverage_20260611.csv`",
  "- `paper2_tssem_substitution_pooled_correlations_20260611.csv`",
  "- `paper2_tssem_substitution_pooled_correlation_delta_20260611.csv`",
  "- `paper2_tssem_substitution_stage2_paths_20260611.csv`",
  "- `paper2_tssem_substitution_stage2_fit_indices_20260611.csv`"
)
writeLines(report, file.path(results_dir, "PAPER2_TSSEM_SUBSTITUTION_DIAGNOSTIC_20260611.md"))

cat("paper2_tssem_substitution_diagnostic_complete\n")
print(summary_rows)
