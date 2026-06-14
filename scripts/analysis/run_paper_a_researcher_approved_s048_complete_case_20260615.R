#!/usr/bin/env Rscript

suppressPackageStartupMessages({
  library(readr)
  library(dplyr)
  library(purrr)
  library(tibble)
  library(metaSEM)
  library(OpenMx)
})

args <- commandArgs(trailingOnly = FALSE)
script_path <- normalizePath(sub('^--file=', '', grep('^--file=', args, value = TRUE)[1]), mustWork = TRUE)
repo <- normalizePath(file.path(dirname(script_path), '..', '..'), mustWork = TRUE)
input_path <- Sys.getenv(
  'PAPER_A_COMPLETE_CASE_INPUT',
  unset = file.path(repo, 'data/04_extraction/05_llm_masem_substitution/results/paper_a_researcher_approved_s048_supplement_20260615/paper_a_source_corrected_plus_researcher_approved_anx_tru_pe_se_s048_input_20260615.csv')
)
out_dir <- Sys.getenv(
  'PAPER_A_COMPLETE_CASE_OUT_DIR',
  unset = file.path(repo, 'data/04_extraction/05_llm_masem_substitution/results/paper_a_researcher_approved_s048_complete_case_20260615')
)
onedrive_out <- '/Users/newhosung/Library/CloudStorage/OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity/AI Adoption Meta Analysis - Documents/Meta/AI Adoption/03_source_adjudication/Paper_A/2026-06-15_researcher_approved_s048_analysis'
dir.create(out_dir, recursive = TRUE, showWarnings = FALSE)
dir.create(onedrive_out, recursive = TRUE, showWarnings = FALSE)

safe_num <- function(x) suppressWarnings(as.numeric(x))
canonical_pair <- function(a, b) paste(sort(c(a, b)), collapse = '-')
status_code <- function(fit) {
  code <- tryCatch(fit$mx.fit@output$status$code, error = function(e) NA_integer_)
  if (is.null(code)) NA_integer_ else code
}
compact_error <- function(x) {
  msg <- if (inherits(x, 'error')) conditionMessage(x) else as.character(x)
  msg <- gsub('[[:space:]]+', ' ', msg)
  if (grepl('not positive definite', msg, fixed = TRUE)) {
    return('metaSEM/OpenMx fit is not finite because an implied covariance or asymptotic covariance matrix is not positive definite.')
  }
  if (nchar(msg) > 280) paste0(substr(msg, 1, 280), '...') else msg
}
fit_stat <- function(stage2_fit, name) {
  stat_map <- c(
    chisq = 'Chi-square of target model', df = 'DF of target model', p = 'p value of target model',
    CFI = 'CFI', TLI = 'TLI', RMSEA = 'RMSEA', SRMR = 'SRMR', AIC = 'AIC', BIC = 'BIC'
  )
  row_name <- unname(stat_map[[name]])
  value <- tryCatch(summary(stage2_fit)$stat[row_name, 'Value'], error = function(e) NA_real_)
  if (is.null(value)) NA_real_ else as.numeric(value)
}

raw <- read_csv(input_path, show_col_types = FALSE) %>%
  mutate(
    study_id = as.character(study_id),
    c1 = as.character(construct_1),
    c2 = as.character(construct_2),
    r_numeric = safe_num(r_numeric),
    sample_size_numeric = safe_num(sample_size_numeric),
    pair = map2_chr(c1, c2, canonical_pair)
  ) %>%
  filter(!is.na(r_numeric), abs(r_numeric) < 1, !is.na(sample_size_numeric), sample_size_numeric > 3)

routes <- list(
  paper_a_core7_att_mediation = list(
    constructs = c('PE','EE','SI','FC','ATT','BI','UB'),
    paths = tribble(
      ~from, ~to, ~label,
      'PE','ATT','PE_to_ATT', 'EE','ATT','EE_to_ATT', 'SI','ATT','SI_to_ATT', 'FC','ATT','FC_to_ATT',
      'ATT','BI','ATT_to_BI', 'PE','BI','PE_to_BI', 'EE','BI','EE_to_BI', 'SI','BI','SI_to_BI',
      'FC','UB','FC_to_UB', 'BI','UB','BI_to_UB'
    ),
    claim = 'Complete-case ATT mediation diagnostic only; not full10 primary.'
  ),
  paper_a_trust6_mechanism = list(
    constructs = c('PE','EE','SI','TRU','BI','UB'),
    paths = tribble(
      ~from, ~to, ~label,
      'PE','TRU','PE_to_TRU', 'EE','TRU','EE_to_TRU', 'SI','TRU','SI_to_TRU',
      'TRU','BI','TRU_to_BI', 'PE','BI','PE_to_BI', 'EE','BI','EE_to_BI', 'SI','BI','SI_to_BI',
      'BI','UB','BI_to_UB'
    ),
    claim = 'Complete-case TRU mechanism diagnostic; defensible only as reduced sensitivity route.'
  ),
  paper_a_full10_theory_target = list(
    constructs = c('PE','EE','SI','FC','ATT','SE','TRU','ANX','BI','UB'),
    paths = tribble(
      ~from, ~to, ~label,
      'PE','ATT','PE_to_ATT', 'EE','ATT','EE_to_ATT', 'SI','ATT','SI_to_ATT', 'FC','ATT','FC_to_ATT',
      'ATT','BI','ATT_to_BI', 'PE','BI','PE_to_BI', 'EE','BI','EE_to_BI', 'SI','BI','SI_to_BI',
      'PE','TRU','PE_to_TRU', 'EE','TRU','EE_to_TRU', 'TRU','BI','TRU_to_BI',
      'PE','SE','PE_to_SE', 'EE','SE','EE_to_SE', 'SI','SE','SI_to_SE', 'FC','SE','FC_to_SE', 'SE','BI','SE_to_BI',
      'ANX','BI','ANX_to_BI', 'FC','UB','FC_to_UB', 'BI','UB','BI_to_UB'
    ),
    claim = 'Full10 primary target; not estimable without complete-case or defensible missing-data route.'
  )
)

make_complete_mats <- function(data, constructs) {
  construct_vec <- unname(unlist(constructs))
  required_pairs <- combn(construct_vec, 2, FUN = function(x) canonical_pair(x[1], x[2]))
  pair_data <- data %>%
    filter(c1 %in% construct_vec, c2 %in% construct_vec, c1 != c2) %>%
    group_by(study_id, c1, c2, pair) %>%
    summarise(r = mean(r_numeric, na.rm = TRUE), n = median(sample_size_numeric, na.rm = TRUE), row_n = n(), .groups = 'drop')
  by_study <- split(pair_data, pair_data$study_id)
  candidate_complete <- names(by_study)[map_lgl(by_study, ~all(required_pairs %in% .x$pair))]
  mats <- list()
  n_vec <- c()
  eigen_rows <- list()
  for (sid in candidate_complete) {
    rows <- by_study[[sid]]
    mat <- matrix(NA_real_, length(construct_vec), length(construct_vec), dimnames = list(construct_vec, construct_vec))
    diag(mat) <- 1
    for (i in seq_len(nrow(rows))) {
      mat[rows$c1[i], rows$c2[i]] <- rows$r[i]
      mat[rows$c2[i], rows$c1[i]] <- rows$r[i]
    }
    eig <- eigen(mat, symmetric = TRUE, only.values = TRUE)$values
    eigen_rows[[sid]] <- tibble(route = NA_character_, study_id = sid, min_eigen = min(eig), positive_definite = min(eig) > 1e-8)
    if (all(!is.na(mat[upper.tri(mat)])) && min(eig) > 1e-8) {
      mats[[sid]] <- mat
      n_vec <- c(n_vec, median(rows$n, na.rm = TRUE))
      names(n_vec)[length(n_vec)] <- sid
    }
  }
  list(
    pair_data = pair_data,
    required_pairs = required_pairs,
    candidate_complete = candidate_complete,
    mats = mats,
    n_vec = n_vec,
    eigen_rows = bind_rows(eigen_rows)
  )
}

make_stage2_matrices <- function(constructs, paths) {
  construct_vec <- unname(unlist(constructs))
  paths <- paths %>% filter(from %in% construct_vec, to %in% construct_vec)
  p <- length(construct_vec)
  idx <- setNames(seq_along(construct_vec), construct_vec)
  A <- mxMatrix(type = 'Full', nrow = p, ncol = p, free = FALSE, values = 0, labels = NA, name = 'A')
  for (i in seq_len(nrow(paths))) {
    A$free[idx[[paths$to[i]]], idx[[paths$from[i]]]] <- TRUE
    A$labels[idx[[paths$to[i]]], idx[[paths$from[i]]]] <- paths$label[i]
    A$values[idx[[paths$to[i]]], idx[[paths$from[i]]]] <- 0.15
  }
  endogenous <- unique(paths$to)
  exogenous <- setdiff(construct_vec, endogenous)
  S <- mxMatrix(type = 'Symm', nrow = p, ncol = p, free = FALSE, values = 0, labels = NA, name = 'S')
  for (name in exogenous) S$values[idx[[name]], idx[[name]]] <- 1
  for (name in endogenous) {
    S$free[idx[[name]], idx[[name]]] <- TRUE
    S$values[idx[[name]], idx[[name]]] <- 0.5
    S$labels[idx[[name]], idx[[name]]] <- paste0('Var_e_', name)
  }
  if (length(exogenous) >= 2) {
    exo_pairs <- combn(exogenous, 2)
    for (col in seq_len(ncol(exo_pairs))) {
      a <- idx[[exo_pairs[1, col]]]
      b <- idx[[exo_pairs[2, col]]]
      label <- paste0('Cov_', exo_pairs[1, col], '_', exo_pairs[2, col])
      S$free[a, b] <- TRUE
      S$free[b, a] <- TRUE
      S$values[a, b] <- 0.3
      S$values[b, a] <- 0.3
      S$labels[a, b] <- label
      S$labels[b, a] <- label
    }
  }
  list(A = A, S = S, paths = paths)
}

run_route <- function(route_name, spec) {
  built <- make_complete_mats(raw, spec$constructs)
  eigen_rows <- built$eigen_rows
  if (nrow(eigen_rows) > 0) {
    eigen_rows$route <- route_name
    write_csv(eigen_rows, file.path(out_dir, paste0(route_name, '_complete_case_matrix_eigen_20260615.csv')))
  }
  complete_ids <- names(built$mats)
  stage1_status <- 'not_run'
  stage1_method <- 'none'
  stage1_error <- ''
  stage2_status <- 'not_run'
  stage2_error <- ''
  stage2_code <- NA_integer_
  stage2_path_count <- 0L
  stage2_fit_count <- 0L
  if (length(built$mats) >= 2) {
    fit1 <- tryCatch(tssem1(Cov = built$mats, n = built$n_vec, method = 'REM', RE.type = 'Diag'), error = function(e) e)
    if (inherits(fit1, 'error')) {
      stage1_error <- compact_error(fit1)
      fit1 <- tryCatch(tssem1(Cov = built$mats, n = built$n_vec, method = 'FEM'), error = function(e) e)
      stage1_method <- 'REM_then_FEM'
      if (inherits(fit1, 'error')) {
        stage1_status <- 'failed'
        stage1_error <- paste(stage1_error, 'FEM:', compact_error(fit1))
        fit1 <- NULL
      } else {
        stage1_status <- ifelse(identical(status_code(fit1), 0L), 'converged', paste0('status_', status_code(fit1)))
      }
    } else {
      stage1_method <- 'REM'
      stage1_status <- ifelse(identical(status_code(fit1), 0L), 'converged', paste0('status_', status_code(fit1)))
    }
    if (!is.null(fit1)) {
      saveRDS(fit1, file.path(out_dir, paste0(route_name, '_complete_case_tssem1_fit_20260615.rds')))
      mats2 <- make_stage2_matrices(spec$constructs, spec$paths)
      fit2 <- tryCatch(tssem2(fit1, Amatrix = mats2$A, Smatrix = mats2$S, diag.constraints = TRUE, intervals.type = 'LB', model.name = route_name), error = function(e) e)
      if (inherits(fit2, 'error')) {
        stage2_status <- 'failed'
        stage2_error <- compact_error(fit2)
      } else {
        stage2_code <- status_code(fit2)
        stage2_status <- ifelse(identical(stage2_code, 0L), 'converged', paste0('status_', stage2_code))
        coefs <- coef(fit2)
        paths <- tibble(
          route = route_name,
          parameter = names(coefs),
          estimate = as.numeric(coefs),
          parameter_family = case_when(
            grepl('_to_', names(coefs)) ~ 'structural_path',
            grepl('^Cov_', names(coefs)) ~ 'exogenous_covariance',
            grepl('^Var_e_', names(coefs)) ~ 'residual_variance',
            TRUE ~ 'other'
          )
        )
        fit_names <- c('chisq','df','p','CFI','TLI','RMSEA','SRMR','AIC','BIC')
        fit_indices <- tibble(route = route_name, fit_index = fit_names, value = map_dbl(fit_names, ~fit_stat(fit2, .x)))
        write_csv(paths, file.path(out_dir, paste0(route_name, '_complete_case_stage2_paths_20260615.csv')))
        write_csv(fit_indices, file.path(out_dir, paste0(route_name, '_complete_case_stage2_fit_indices_20260615.csv')))
        saveRDS(fit2, file.path(out_dir, paste0(route_name, '_complete_case_tssem2_fit_20260615.rds')))
        stage2_path_count <- nrow(paths)
        stage2_fit_count <- nrow(fit_indices)
      }
    }
  } else {
    stage1_error <- 'fewer than 2 positive-definite complete-case matrices'
  }
  tibble(
    route = route_name,
    constructs = paste(spec$constructs, collapse = ','),
    required_pairs = length(built$required_pairs),
    candidate_complete_case_studies = length(built$candidate_complete),
    positive_definite_complete_case_studies = length(built$mats),
    positive_definite_complete_case_ids = paste(complete_ids, collapse = ';'),
    stage1_status = stage1_status,
    stage1_method = stage1_method,
    stage1_error = stage1_error,
    stage2_status = stage2_status,
    stage2_status_code = stage2_code,
    stage2_error = stage2_error,
    stage2_path_count = stage2_path_count,
    stage2_fit_count = stage2_fit_count,
    claim_boundary = spec$claim
  )
}

summary_rows <- imap_dfr(routes, ~run_route(.y, .x))
summary_path <- file.path(out_dir, 'paper_a_source_corrected_complete_case_summary_20260615.csv')
write_csv(summary_rows, summary_path)

report <- c(
  '# Paper A researcher-approved S048 complete-case TSSEM diagnostic',
  '',
  'Date: 2026-06-15',
  '',
  paste0('Input: `', input_path, '`'),
  '',
  '## Summary',
  '',
  '| Route | Candidate complete cases | Positive-definite complete cases | Stage 1 | Stage 2 | Boundary |',
  '| --- | ---: | ---: | --- | --- | --- |'
)
for (i in seq_len(nrow(summary_rows))) {
  report <- c(report, paste0(
    '| ', summary_rows$route[i], ' | ',
    summary_rows$candidate_complete_case_studies[i], ' | ',
    summary_rows$positive_definite_complete_case_studies[i], ' | ',
    summary_rows$stage1_status[i], ' | ',
    summary_rows$stage2_status[i], ' | ',
    summary_rows$claim_boundary[i], ' |'
  ))
}
report <- c(
  report,
  '',
  '## Interpretation boundary',
  '',
  'This is a diagnostic complete-case rerun after researcher-approved S048 staging plus ANX/TRU and S121 PE-SE supplements. Full10 remains non-estimable by complete-case TSSEM because it has zero complete-case studies. Reduced trust6/core7 routes may be reported only as sensitivity or diagnostic routes unless the researcher changes the primary model claim.',
  '',
  '## Output files',
  '',
  '- `paper_a_source_corrected_complete_case_summary_20260615.csv`',
  '- per-route `*_complete_case_matrix_eigen_20260615.csv`',
  '- per-route `*_complete_case_stage2_paths_20260615.csv` and `*_complete_case_stage2_fit_indices_20260615.csv` when Stage 2 succeeds'
)
report_path <- file.path(out_dir, 'PAPER_A_SOURCE_CORRECTED_COMPLETE_CASE_TSSEM_20260615.md')
writeLines(report, report_path)
file.copy(summary_path, file.path(onedrive_out, 'paper_a_source_corrected_complete_case_summary_20260615.csv'), overwrite = TRUE)
file.copy(report_path, file.path(onedrive_out, 'PAPER_A_SOURCE_CORRECTED_COMPLETE_CASE_TSSEM_20260615.md'), overwrite = TRUE)
cat(paste(capture.output(print(summary_rows)), collapse = '\n'), '\n')
