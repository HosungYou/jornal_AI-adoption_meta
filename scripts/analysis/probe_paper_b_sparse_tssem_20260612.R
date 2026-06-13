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
input_path <- file.path(repo, 'data/04_extraction/05_llm_masem_substitution/results/paper2_masem_substitution_rerun_input_n_weighted_all_source_supported_20260612.csv')
out_dir <- file.path(repo, 'data/04_extraction/05_llm_masem_substitution/results/paper_b_sparse_tssem_probe_20260612')
dir.create(out_dir, recursive = TRUE, showWarnings = FALSE)

safe_num <- function(x) suppressWarnings(as.numeric(x))
canonical_pair <- function(a, b) paste(sort(c(a, b)), collapse = '-')
repo_rel <- function(path) sub(paste0(repo, .Platform$file.sep), '', normalizePath(path, mustWork = FALSE), fixed = TRUE)

status_code <- function(fit) {
  code <- tryCatch(fit$mx.fit@output$status$code, error = function(e) NA_integer_)
  if (is.null(code)) NA_integer_ else code
}

fit_stat <- function(stage2_fit, name) {
  stat_map <- c(
    chisq = 'Chi-square of target model',
    df = 'DF of target model',
    p = 'p value of target model',
    CFI = 'CFI',
    TLI = 'TLI',
    RMSEA = 'RMSEA',
    SRMR = 'SRMR',
    AIC = 'AIC',
    BIC = 'BIC'
  )
  row_name <- unname(stat_map[[name]])
  value <- tryCatch(summary(stage2_fit)$stat[row_name, 'Value'], error = function(e) NA_real_)
  if (is.null(value)) NA_real_ else as.numeric(value)
}

make_stage2_matrices <- function(constructs, probe_name) {
  p <- length(constructs)
  idx <- setNames(seq_along(constructs), constructs)
  path_table <- tibble::tribble(
    ~from, ~to, ~label,
    'PE', 'ATT', 'PE_to_ATT',
    'EE', 'ATT', 'EE_to_ATT',
    'SI', 'ATT', 'SI_to_ATT',
    'FC', 'ATT', 'FC_to_ATT',
    'ATT', 'BI', 'ATT_to_BI',
    'PE', 'BI', 'PE_to_BI',
    'EE', 'BI', 'EE_to_BI',
    'SI', 'BI', 'SI_to_BI',
    'FC', 'UB', 'FC_to_UB',
    'BI', 'UB', 'BI_to_UB',
    'PE', 'TRU', 'PE_to_TRU',
    'EE', 'TRU', 'EE_to_TRU',
    'SI', 'TRU', 'SI_to_TRU',
    'TRU', 'BI', 'TRU_to_BI'
  ) %>%
    filter(from %in% constructs, to %in% constructs)

  A <- mxMatrix(type = 'Full', nrow = p, ncol = p, free = FALSE, values = 0, labels = NA, name = 'A')
  for (i in seq_len(nrow(path_table))) {
    from <- path_table$from[[i]]
    to <- path_table$to[[i]]
    A$free[idx[[to]], idx[[from]]] <- TRUE
    A$labels[idx[[to]], idx[[from]]] <- path_table$label[[i]]
    A$values[idx[[to]], idx[[from]]] <- 0.15
  }

  endogenous <- unique(path_table$to)
  exogenous <- setdiff(constructs, endogenous)
  S <- mxMatrix(type = 'Symm', nrow = p, ncol = p, free = FALSE, values = 0, labels = NA, name = 'S')
  for (name in exogenous) {
    S$values[idx[[name]], idx[[name]]] <- 1
  }
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
  list(A = A, S = S, paths = path_table)
}

data <- read_csv(input_path, show_col_types = FALSE) %>%
  mutate(
    c1 = as.character(construct_1),
    c2 = as.character(construct_2),
    r_numeric = safe_num(r_numeric),
    sample_size_numeric = safe_num(sample_size_numeric),
    pair = map2_chr(c1, c2, canonical_pair)
  )

make_complete_mats <- function(constructs) {
  constructs <- unname(unlist(constructs))
  pair_data <- data %>%
    filter(c1 %in% constructs, c2 %in% constructs, c1 != c2, !is.na(r_numeric), abs(r_numeric) < 1, !is.na(sample_size_numeric), sample_size_numeric > 3) %>%
    group_by(study_id, c1, c2, pair) %>%
    summarise(r = mean(r_numeric, na.rm = TRUE), n = median(sample_size_numeric, na.rm = TRUE), .groups = 'drop')
  study_n <- pair_data %>% group_by(study_id) %>% summarise(n = median(n, na.rm = TRUE), .groups = 'drop')
  mats <- list(); n_values <- c(); complete_ids <- c()
  for (sid in sort(unique(pair_data$study_id))) {
    mat <- matrix(NA_real_, length(constructs), length(constructs), dimnames = list(constructs, constructs))
    diag(mat) <- 1
    rows <- pair_data %>% filter(study_id == sid)
    for (i in seq_len(nrow(rows))) {
      mat[rows$c1[i], rows$c2[i]] <- rows$r[i]
      mat[rows$c2[i], rows$c1[i]] <- rows$r[i]
    }
    if (all(!is.na(mat[upper.tri(mat)]))) {
      mats[[sid]] <- mat
      n_values <- c(n_values, study_n$n[match(sid, study_n$study_id)])
      names(n_values)[length(n_values)] <- sid
      complete_ids <- c(complete_ids, sid)
    }
  }
  list(pair_data = pair_data, mats = mats, n_vec = n_values, complete_ids = complete_ids)
}

run_probe <- function(name, constructs) {
  construct_vec <- unname(unlist(constructs))
  built <- make_complete_mats(construct_vec)
  pair_cov <- built$pair_data %>% count(pair, name = 'study_pair_rows') %>% mutate(probe = name, .before = 1)
  write_csv(pair_cov, file.path(out_dir, paste0(name, '_pair_coverage_20260612.csv')))
  n_complete <- length(built$mats)
  summary <- tibble(
    probe = name,
    constructs = paste(construct_vec, collapse = ','),
    construct_count = length(construct_vec),
    required_pairs = length(construct_vec) * (length(construct_vec) - 1) / 2,
    observed_pairs = n_distinct(built$pair_data$pair),
    complete_case_studies = n_complete,
    complete_case_study_ids = paste(built$complete_ids, collapse = ';'),
    stage1_status = 'not_run',
    stage1_error = '',
    stage2_status = 'not_run',
    claim_boundary = ''
  )
  if (n_complete < 3) {
    summary$stage1_status <- 'not_run_insufficient_complete_case_studies'
    summary$claim_boundary <- 'Sparse probe only; not enough complete-case studies for conservative TSSEM probe.'
    return(summary)
  }
  fit <- tryCatch(
    tssem1(Cov = built$mats, n = built$n_vec, method = 'REM', RE.type = 'Diag', acov = 'weighted'),
    error = function(e) e
  )
  if (inherits(fit, 'error')) {
    summary$stage1_status <- 'failed'
    summary$stage1_error <- conditionMessage(fit)
    summary$claim_boundary <- 'Probe attempted but Stage 1 failed; retain core6 diagnostic boundary.'
    return(summary)
  }
  summary$stage1_status <- 'completed'
  summary$claim_boundary <- 'Stage 1 probe completed; do not promote to main-text extension unless Stage 2 specification and stability are separately accepted.'
  saveRDS(fit, file.path(out_dir, paste0(name, '_tssem1_fit_20260612.rds')))
  pooled <- tryCatch({
    fixed <- coef(fit, select = 'fixed')
    mat <- vec2symMat(fixed, diag = FALSE, byrow = FALSE)
    dimnames(mat) <- list(constructs, constructs)
    diag(mat) <- 1
    as.data.frame(as.table(mat))
  }, error = function(e) NULL)
  if (!is.null(pooled)) {
    names(pooled) <- c('construct_1', 'construct_2', 'pooled_r')
    pooled$probe <- name
    write_csv(pooled, file.path(out_dir, paste0(name, '_pooled_correlations_20260612.csv')))
  }
  stage2_mats <- make_stage2_matrices(construct_vec, name)
  stage2_error <- ''
  stage2_fit <- tryCatch(
    tssem2(
      tssem1.obj = fit,
      Amatrix = stage2_mats$A,
      Smatrix = stage2_mats$S,
      diag.constraints = TRUE,
      intervals.type = 'LB',
      model.name = paste0('PaperB_', name, '_sparse_probe')
    ),
    error = function(e) {
      stage2_error <<- conditionMessage(e)
      NULL
    }
  )
  if (is.null(stage2_fit)) {
    summary$stage2_status <- 'failed'
    summary$stage1_error <- paste(trimws(summary$stage1_error), paste('Stage2:', stage2_error)) %>% trimws()
  } else {
    code <- status_code(stage2_fit)
    summary$stage2_status <- ifelse(identical(code, 0L), 'converged', paste0('status_', code))
    coefs <- coef(stage2_fit)
    path_rows <- tibble(
      probe = name,
      parameter = names(coefs),
      estimate = as.numeric(coefs),
      parameter_family = case_when(
        grepl('_to_', names(coefs)) ~ 'structural_path',
        grepl('^Cov_', names(coefs)) ~ 'exogenous_covariance',
        grepl('^Var_e_', names(coefs)) ~ 'residual_variance',
        TRUE ~ 'other'
      )
    )
    fit_names <- c('chisq', 'df', 'p', 'CFI', 'TLI', 'RMSEA', 'SRMR', 'AIC', 'BIC')
    fit_rows <- tibble(
      probe = name,
      fit_index = fit_names,
      value = map_dbl(fit_names, function(fname) fit_stat(stage2_fit, fname))
    )
    write_csv(path_rows, file.path(out_dir, paste0(name, '_stage2_paths_20260612.csv')))
    write_csv(fit_rows, file.path(out_dir, paste0(name, '_stage2_fit_indices_20260612.csv')))
    saveRDS(stage2_fit, file.path(out_dir, paste0(name, '_tssem2_fit_20260612.rds')))
  }
  summary
}

probes <- list(
  core7_add_att = c('PE','EE','SI','FC','ATT','BI','UB'),
  core8_add_tru = c('PE','EE','SI','FC','ATT','TRU','BI','UB')
)

summaries <- bind_rows(imap(probes, ~run_probe(.y, .x)))
write_csv(summaries, file.path(out_dir, 'paper_b_sparse_tssem_probe_summary_20260612.csv'))

report <- c(
  '# Paper B Sparse TSSEM Probe',
  '',
  'Date: 2026-06-12',
  '',
  paste0('Input: `', repo_rel(input_path), '`'),
  '',
  '## Probe boundary',
  '',
  'These probes are not main-text all-construct claims. They test whether the selected broader route can move beyond the completed core-6 diagnostic under a conservative complete-case matrix rule.',
  '',
  '## Results',
  '',
  '| Probe | Constructs | Complete-case studies | Stage 1 status | Stage 2 status | Error | Claim boundary |',
  '| --- | --- | ---: | --- | --- | --- | --- |'
)
for (i in seq_len(nrow(summaries))) {
  report <- c(report, paste0('| ', summaries$probe[i], ' | ', summaries$constructs[i], ' | ', summaries$complete_case_studies[i], ' | ', summaries$stage1_status[i], ' | ', summaries$stage2_status[i], ' | ', summaries$stage1_error[i], ' | ', summaries$claim_boundary[i], ' |'))
}
report <- c(
  report,
  '',
  '## Manuscript implication',
  '',
  'Core-6 remains the completed SEM diagnostic. The core7_add_att probe completed Stage 1 but failed the Stage 2 path-model probe because the asymptotic covariance matrix was not positive definite. The core8_add_tru probe lacked enough complete-case studies for conservative TSSEM. Broader construct sets should therefore remain sparse probes unless later model-specific diagnostics support stronger reporting.'
)
writeLines(report, file.path(out_dir, 'PAPER_B_SPARSE_TSSEM_PROBE_20260612.md'))
cat(paste(capture.output(print(summaries)), collapse = '\n'), '\n')
