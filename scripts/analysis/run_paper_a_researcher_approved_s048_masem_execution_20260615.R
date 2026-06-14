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

args <- commandArgs(trailingOnly = FALSE)
script_path <- normalizePath(sub('^--file=', '', grep('^--file=', args, value = TRUE)[1]), mustWork = TRUE)
repo <- normalizePath(file.path(dirname(script_path), '..', '..'), mustWork = TRUE)
default_input_path <- file.path(repo, 'data/04_extraction/05_llm_masem_substitution/results/paper_a_researcher_approved_s048_supplement_20260615/paper_a_source_corrected_plus_researcher_approved_anx_tru_pe_se_s048_input_20260615.csv')
input_path <- Sys.getenv('PAPER_A_MASEM_INPUT', unset = default_input_path)
out_dir <- Sys.getenv('PAPER_A_MASEM_OUT_DIR', unset = file.path(repo, 'data/04_extraction/05_llm_masem_substitution/results/paper_a_researcher_approved_s048_model_family_masem_20260615'))
dir.create(out_dir, recursive = TRUE, showWarnings = FALSE)

safe_num <- function(x) suppressWarnings(as.numeric(x))
canonical_pair <- function(a, b) paste(sort(c(a, b)), collapse = '-')
repo_rel <- function(path) sub(paste0(repo, .Platform$file.sep), '', normalizePath(path, mustWork = FALSE), fixed = TRUE)
status_code <- function(fit) {
  code <- tryCatch(fit$mx.fit@output$status$code, error = function(e) NA_integer_)
  if (is.null(code)) NA_integer_ else code
}
compact_error <- function(x) {
  msg <- if (inherits(x, 'error')) conditionMessage(x) else as.character(x)
  msg <- gsub('[[:space:]]+', ' ', msg)
  if (grepl('not positive definite', msg, fixed = TRUE)) {
    return('metaSEM/OpenMx fit is not finite because the implied covariance is not positive definite under sparse partial-matrix input.')
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
    claim = 'Primary feasible ATT mediation route if TSSEM converges.'
  ),
  paper_a_trust6_mechanism = list(
    constructs = c('PE','EE','SI','TRU','BI','UB'),
    paths = tribble(
      ~from, ~to, ~label,
      'PE','TRU','PE_to_TRU', 'EE','TRU','EE_to_TRU', 'SI','TRU','SI_to_TRU',
      'TRU','BI','TRU_to_BI', 'PE','BI','PE_to_BI', 'EE','BI','EE_to_BI', 'SI','BI','SI_to_BI',
      'BI','UB','BI_to_UB'
    ),
    claim = 'AI-specific TRU mechanism route; SI path should be sensitivity if unstable.'
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
    claim = 'Full 10-construct theory target; expected to be sparse and must not be overclaimed if estimation fails.'
  )
)

make_partial_mats <- function(data, constructs) {
  constructs <- unname(unlist(constructs))
  pair_data <- data %>%
    filter(c1 %in% constructs, c2 %in% constructs, c1 != c2) %>%
    group_by(study_id, c1, c2, pair) %>%
    summarise(r = mean(r_numeric, na.rm = TRUE), n = median(sample_size_numeric, na.rm = TRUE), row_n = n(), .groups = 'drop')
  study_n <- pair_data %>% group_by(study_id) %>% summarise(n = median(n, na.rm = TRUE), pair_count = n_distinct(pair), .groups = 'drop')
  mats <- list(); n_values <- c(); complete_ids <- c(); partial_ids <- c()
  for (sid in sort(unique(pair_data$study_id))) {
    mat <- matrix(NA_real_, length(constructs), length(constructs), dimnames = list(constructs, constructs))
    diag(mat) <- 1
    rows <- pair_data %>% filter(study_id == sid)
    for (i in seq_len(nrow(rows))) {
      mat[rows$c1[i], rows$c2[i]] <- rows$r[i]
      mat[rows$c2[i], rows$c1[i]] <- rows$r[i]
    }
    if (any(!is.na(mat[upper.tri(mat)]))) {
      mats[[sid]] <- mat
      n_values <- c(n_values, study_n$n[match(sid, study_n$study_id)])
      names(n_values)[length(n_values)] <- sid
      partial_ids <- c(partial_ids, sid)
      if (all(!is.na(mat[upper.tri(mat)]))) complete_ids <- c(complete_ids, sid)
    }
  }
  list(pair_data = pair_data, mats = mats, n_vec = n_values, partial_ids = partial_ids, complete_ids = complete_ids)
}

make_stage2_matrices <- function(constructs, paths) {
  constructs <- unname(unlist(constructs))
  paths <- paths %>% filter(from %in% constructs, to %in% constructs)
  p <- length(constructs)
  idx <- setNames(seq_along(constructs), constructs)
  A <- mxMatrix(type = 'Full', nrow = p, ncol = p, free = FALSE, values = 0, labels = NA, name = 'A')
  for (i in seq_len(nrow(paths))) {
    A$free[idx[[paths$to[i]]], idx[[paths$from[i]]]] <- TRUE
    A$labels[idx[[paths$to[i]]], idx[[paths$from[i]]]] <- paths$label[i]
    A$values[idx[[paths$to[i]]], idx[[paths$from[i]]]] <- 0.15
  }
  endogenous <- unique(paths$to)
  exogenous <- setdiff(constructs, endogenous)
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
      a <- idx[[exo_pairs[1, col]]]; b <- idx[[exo_pairs[2, col]]]
      label <- paste0('Cov_', exo_pairs[1, col], '_', exo_pairs[2, col])
      S$free[a, b] <- TRUE; S$free[b, a] <- TRUE
      S$values[a, b] <- 0.3; S$values[b, a] <- 0.3
      S$labels[a, b] <- label; S$labels[b, a] <- label
    }
  }
  list(A = A, S = S, paths = paths)
}

pairwise_pool <- function(data, constructs, route_name) {
  pair_rows <- data %>%
    filter(c1 %in% constructs, c2 %in% constructs, c1 != c2) %>%
    group_by(study_id, pair) %>%
    summarise(r = mean(r_numeric, na.rm = TRUE), n = median(sample_size_numeric, na.rm = TRUE), .groups = 'drop') %>%
    mutate(z = atanh(pmax(pmin(r, 0.999999), -0.999999)), v = 1 / pmax(n - 3, 1))
  pooled <- pair_rows %>%
    group_by(pair) %>%
    summarise(
      k = n(),
      total_n = sum(n, na.rm = TRUE),
      fixed_z = sum((1/v) * z) / sum(1/v),
      q = sum((1/v) * (z - fixed_z)^2),
      c_val = sum(1/v) - sum((1/v)^2) / sum(1/v),
      tau2 = ifelse(k > 1 & is.finite(c_val) & c_val > 0, pmax(0, (q - (k - 1)) / c_val), 0),
      pooled_z = sum((1/(v + tau2)) * z) / sum(1/(v + tau2)),
      se_z = sqrt(1 / sum(1/(v + tau2))),
      pooled_r = tanh(pooled_z),
      ci_low = tanh(pooled_z - 1.96 * se_z),
      ci_high = tanh(pooled_z + 1.96 * se_z),
      i2 = ifelse(k > 1 & q > (k - 1), 100 * (q - (k - 1)) / q, 0),
      .groups = 'drop'
    ) %>%
    mutate(route = route_name, .before = 1)
  pooled
}

matrix_from_pooled <- function(pooled, constructs) {
  mat <- matrix(NA_real_, length(constructs), length(constructs), dimnames = list(constructs, constructs))
  diag(mat) <- 1
  for (i in seq_len(nrow(pooled))) {
    parts <- strsplit(pooled$pair[i], '-', fixed = TRUE)[[1]]
    if (length(parts) == 2 && all(parts %in% constructs)) {
      mat[parts[1], parts[2]] <- pooled$pooled_r[i]
      mat[parts[2], parts[1]] <- pooled$pooled_r[i]
    }
  }
  mat
}

run_route <- function(route_name, spec) {
  construct_vec <- unname(unlist(spec$constructs))
  built <- make_partial_mats(raw, construct_vec)
  pair_cov <- built$pair_data %>% count(pair, name = 'study_pair_rows') %>% mutate(route = route_name, .before = 1)
  write_csv(pair_cov, file.path(out_dir, paste0(route_name, '_pair_coverage_20260615.csv')))
  pooled <- pairwise_pool(raw, construct_vec, route_name)
  write_csv(pooled, file.path(out_dir, paste0(route_name, '_pairwise_random_effects_stage1_20260615.csv')))
  pooled_mat <- matrix_from_pooled(pooled, construct_vec)
  missing_pairs <- sum(is.na(pooled_mat[upper.tri(pooled_mat)]))
  min_eigen <- if (missing_pairs == 0) min(eigen(pooled_mat, symmetric = TRUE, only.values = TRUE)$values) else NA_real_
  nearpd_min_eigen <- NA_real_
  if (missing_pairs == 0 && !is.na(min_eigen) && min_eigen <= 0) {
    near_mat <- as.matrix(Matrix::nearPD(pooled_mat, corr = TRUE)$mat)
    nearpd_min_eigen <- min(eigen(near_mat, symmetric = TRUE, only.values = TRUE)$values)
    write_csv(as.data.frame(as.table(near_mat)) %>% rename(construct_1 = Var1, construct_2 = Var2, nearpd_r = Freq) %>% mutate(route = route_name, .before = 1), file.path(out_dir, paste0(route_name, '_nearpd_matrix_20260615.csv')))
  }
  write_csv(as.data.frame(as.table(pooled_mat)) %>% rename(construct_1 = Var1, construct_2 = Var2, pooled_r = Freq) %>% mutate(route = route_name, .before = 1), file.path(out_dir, paste0(route_name, '_pairwise_pooled_matrix_20260615.csv')))

  stage1_status <- 'not_run'; stage1_method <- 'none'; stage1_error <- ''; stage2_status <- 'not_run'; stage2_error <- ''; stage2_code <- NA_integer_
  fit1 <- tryCatch(tssem1(Cov = built$mats, n = built$n_vec, method = 'REM', RE.type = 'Diag', acov = 'individual'), error = function(e) e)
  if (inherits(fit1, 'error')) {
    stage1_error <- compact_error(fit1)
    fit1 <- tryCatch(tssem1(Cov = built$mats, n = built$n_vec, method = 'FEM'), error = function(e) e)
    if (inherits(fit1, 'error')) {
      stage1_status <- 'failed'
      stage1_method <- 'REM_then_FEM'
      stage1_error <- paste(stage1_error, 'FEM:', compact_error(fit1))
      fit1 <- NULL
    } else {
      stage1_method <- 'FEM_fallback'
      stage1_status <- ifelse(identical(status_code(fit1), 0L), 'converged', paste0('status_', status_code(fit1)))
    }
  } else {
    stage1_method <- 'REM'
    stage1_status <- ifelse(identical(status_code(fit1), 0L), 'converged', paste0('status_', status_code(fit1)))
  }

  path_rows <- tibble(); fit_rows <- tibble()
  if (!is.null(fit1)) {
    saveRDS(fit1, file.path(out_dir, paste0(route_name, '_tssem1_fit_20260615.rds')))
    mats2 <- make_stage2_matrices(construct_vec, spec$paths)
    fit2 <- tryCatch(tssem2(tssem1.obj = fit1, Amatrix = mats2$A, Smatrix = mats2$S, diag.constraints = TRUE, intervals.type = 'LB', model.name = route_name), error = function(e) e)
    if (inherits(fit2, 'error')) {
      stage2_status <- 'failed'
      stage2_error <- compact_error(fit2)
    } else {
      stage2_code <- status_code(fit2)
      stage2_status <- ifelse(identical(stage2_code, 0L), 'converged', paste0('status_', stage2_code))
      coefs <- coef(fit2)
      path_rows <- tibble(route = route_name, parameter = names(coefs), estimate = as.numeric(coefs), parameter_family = case_when(grepl('_to_', names(coefs)) ~ 'structural_path', grepl('^Cov_', names(coefs)) ~ 'exogenous_covariance', grepl('^Var_e_', names(coefs)) ~ 'residual_variance', TRUE ~ 'other'))
      fit_names <- c('chisq','df','p','CFI','TLI','RMSEA','SRMR','AIC','BIC')
      fit_rows <- tibble(route = route_name, fit_index = fit_names, value = map_dbl(fit_names, function(x) fit_stat(fit2, x)))
      write_csv(path_rows, file.path(out_dir, paste0(route_name, '_stage2_paths_20260615.csv')))
      write_csv(fit_rows, file.path(out_dir, paste0(route_name, '_stage2_fit_indices_20260615.csv')))
      saveRDS(fit2, file.path(out_dir, paste0(route_name, '_tssem2_fit_20260615.rds')))
    }
  }

  tibble(
    route = route_name,
    constructs = paste(construct_vec, collapse = ','),
    construct_count = length(construct_vec),
    required_pairs = length(construct_vec) * (length(construct_vec) - 1) / 2,
    observed_pairs = n_distinct(built$pair_data$pair),
    missing_pairwise_pooled_pairs = missing_pairs,
    single_study_pairs = sum(pooled$k == 1, na.rm = TRUE),
    min_pair_k = min(pooled$k, na.rm = TRUE),
    partial_studies = length(built$partial_ids),
    complete_case_studies = length(built$complete_ids),
    stage1_tssem_status = stage1_status,
    stage1_method = stage1_method,
    stage1_error = stage1_error,
    pairwise_pooled_min_eigen = min_eigen,
    nearpd_min_eigen = nearpd_min_eigen,
    stage2_status = stage2_status,
    stage2_status_code = stage2_code,
    stage2_error = stage2_error,
    claim_boundary = spec$claim
  )
}

summaries <- imap_dfr(routes, ~run_route(.y, .x))
write_csv(summaries, file.path(out_dir, 'paper_a_masem_execution_summary_20260615.csv'))

report <- c(
  '# Paper A researcher-approved S048 MASEM execution attempt', '', 'Date: 2026-06-15', '',
  paste0('Input: `', repo_rel(input_path), '`'), '',
  '## Execution strategy', '',
  'This run attempts actual Paper A TSSEM/MASEM routes using the researcher-approved S048 836-row input. For each route it attempts `metaSEM::tssem1` with partial study matrices, falls back to fixed-effects Stage 1 if needed, then attempts `tssem2` with a theory-guided path model. Independently, it creates pairwise random-effects pooled correlations for every available construct pair so the Stage 1 evidence remains usable even when full structural estimation fails.', '',
  '## Route summary', '',
  '| Route | Constructs | Required pairs | Observed pairs | Missing/unestimated pairs | Single-study pairs | Min pair k | Partial studies | Complete-case studies | TSSEM1 | Stage 2 | Pairwise min eigen | Boundary |',
  '| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | ---: | --- |'
)
fmt4 <- function(x) ifelse(is.na(x), 'NA', sprintf('%.4f', x))
for (i in seq_len(nrow(summaries))) {
  report <- c(report, paste0('| ', summaries$route[i], ' | ', summaries$constructs[i], ' | ', summaries$required_pairs[i], ' | ', summaries$observed_pairs[i], ' | ', summaries$missing_pairwise_pooled_pairs[i], ' | ', summaries$single_study_pairs[i], ' | ', summaries$min_pair_k[i], ' | ', summaries$partial_studies[i], ' | ', summaries$complete_case_studies[i], ' | ', summaries$stage1_tssem_status[i], ' | ', summaries$stage2_status[i], ' | ', fmt4(summaries$pairwise_pooled_min_eigen[i]), ' | ', summaries$claim_boundary[i], ' |'))
}
report <- c(
  report, '', '## Claim boundary', '',
  'Use converged Stage 2 outputs only where both TSSEM1 and TSSEM2 succeed. If TSSEM2 fails but pairwise Stage 1 pooling exists, report the evidence as pooled-correlation/input-readiness evidence rather than a final structural path model. Full 10-construct claims require successful structural estimation and should not be inferred from pairwise pooled correlations alone.', '',
  '## Output files', '',
  '- `paper_a_masem_execution_summary_20260615.csv`',
  '- per-route `*_pairwise_random_effects_stage1_20260615.csv`',
  '- per-route `*_pairwise_pooled_matrix_20260615.csv`',
  '- per-route `*_stage2_paths_20260615.csv` and `*_stage2_fit_indices_20260615.csv` when Stage 2 succeeds'
)
writeLines(report, file.path(out_dir, 'PAPER_A_MASEM_EXECUTION_ATTEMPT_20260615.md'))
cat(paste(capture.output(print(summaries)), collapse = '\n'), '\n')
