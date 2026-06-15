#!/usr/bin/env Rscript

suppressPackageStartupMessages({
  library(readr)
  library(dplyr)
  library(purrr)
  library(tibble)
  library(tidyr)
  library(metaSEM)
  library(OpenMx)
})

args <- commandArgs(trailingOnly = FALSE)
script_path <- normalizePath(sub('^--file=', '', grep('^--file=', args, value = TRUE)[1]), mustWork = TRUE)
repo <- normalizePath(file.path(dirname(script_path), '..', '..'), mustWork = TRUE)
date_tag <- '20260615'
input_path <- file.path(repo, 'data/04_extraction/05_llm_masem_substitution/results/paper_a_researcher_approved_s048_supplement_20260615/paper_a_source_corrected_plus_researcher_approved_anx_tru_pe_se_s048_input_20260615.csv')
model_family_dir <- file.path(repo, 'data/04_extraction/05_llm_masem_substitution/results/paper_a_researcher_approved_s048_model_family_masem_20260615')
primary_dir <- file.path(repo, 'data/04_extraction/05_llm_masem_substitution/results/paper_a_researcher_approved_s048_inference_figures_manuscript_20260615')
out_dir <- file.path(repo, 'data/04_extraction/05_llm_masem_substitution/results/paper_a_model_family_supplemental_diagnostics_20260615')
ms_dir <- file.path(repo, 'paper_a/manuscript/target_journal/apa7_model_family_full_manuscript_scaffold_20260615/supplemental_diagnostics')
onedrive_dir <- '/Users/newhosung/Library/CloudStorage/OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity/AI Adoption Meta Analysis - Documents/05_manuscripts/Paper_A/2026-06-15_apa7_model_family_full_manuscript_scaffold/supplemental_diagnostics'
dir.create(out_dir, recursive = TRUE, showWarnings = FALSE)
dir.create(ms_dir, recursive = TRUE, showWarnings = FALSE)
dir.create(onedrive_dir, recursive = TRUE, showWarnings = FALSE)

safe_num <- function(x) suppressWarnings(as.numeric(x))
canonical_pair <- function(a, b) paste(sort(c(a, b)), collapse = '-')
fmt3 <- function(x) ifelse(is.na(x), 'NA', sprintf('%.3f', as.numeric(x)))
fmt_p <- function(x) {
  x <- suppressWarnings(as.numeric(x))
  if (is.na(x)) return('NA')
  if (x < .001) return('< .001')
  sub('^0', '', sprintf('%.3f', x))
}
compact_error <- function(x) {
  msg <- if (inherits(x, 'error')) conditionMessage(x) else as.character(x)
  msg <- gsub('[[:space:]]+', ' ', msg)
  if (grepl('not positive definite', msg, fixed = TRUE)) return('not_positive_definite')
  if (nchar(msg) > 220) paste0(substr(msg, 1, 220), '...') else msg
}
status_code <- function(fit) {
  code <- tryCatch(fit$mx.fit@output$status$code, error = function(e) NA_integer_)
  if (is.null(code)) NA_integer_ else code
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
ci_class <- function(lo, hi) {
  if (is.na(lo) || is.na(hi)) return('ci_incomplete')
  if (lo > 0 && hi > 0) return('supported_positive_95ci')
  if (lo < 0 && hi < 0) return('supported_negative_95ci')
  'not_supported_95ci_includes_zero'
}
md_table <- function(df) {
  if (nrow(df) == 0) return('')
  df[] <- lapply(df, as.character)
  lines <- c(
    paste0('| ', paste(names(df), collapse = ' | '), ' |'),
    paste0('| ', paste(rep('---', ncol(df)), collapse = ' | '), ' |')
  )
  for (i in seq_len(nrow(df))) {
    lines <- c(lines, paste0('| ', paste(gsub('\\|', '\\\\|', unlist(df[i, ], use.names = FALSE)), collapse = ' | '), ' |'))
  }
  paste(lines, collapse = '\n')
}
write_both <- function(df, stem) {
  csv_path <- file.path(out_dir, paste0(stem, '_', date_tag, '.csv'))
  md_path <- file.path(out_dir, paste0(stem, '_', date_tag, '.md'))
  write_csv(df, csv_path)
  writeLines(md_table(df), md_path)
  file.copy(csv_path, file.path(ms_dir, basename(csv_path)), overwrite = TRUE)
  file.copy(md_path, file.path(ms_dir, basename(md_path)), overwrite = TRUE)
  file.copy(csv_path, file.path(onedrive_dir, basename(csv_path)), overwrite = TRUE)
  file.copy(md_path, file.path(onedrive_dir, basename(md_path)), overwrite = TRUE)
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

make_complete_mats <- function(data, constructs) {
  construct_vec <- unname(unlist(constructs))
  required_pairs <- combn(construct_vec, 2, FUN = function(x) canonical_pair(x[1], x[2]))
  pair_data <- data %>%
    filter(c1 %in% construct_vec, c2 %in% construct_vec, c1 != c2) %>%
    group_by(study_id, c1, c2, pair) %>%
    summarise(r = mean(r_numeric, na.rm = TRUE), n = median(sample_size_numeric, na.rm = TRUE), row_n = n(), .groups = 'drop')
  by_study <- split(pair_data, pair_data$study_id)
  candidate_complete <- names(by_study)[map_lgl(by_study, ~all(required_pairs %in% .x$pair))]
  mats <- list(); n_vec <- c(); eigen_rows <- list()
  for (sid in candidate_complete) {
    rows <- by_study[[sid]]
    mat <- matrix(NA_real_, length(construct_vec), length(construct_vec), dimnames = list(construct_vec, construct_vec))
    diag(mat) <- 1
    for (i in seq_len(nrow(rows))) {
      mat[rows$c1[i], rows$c2[i]] <- rows$r[i]
      mat[rows$c2[i], rows$c1[i]] <- rows$r[i]
    }
    eig <- eigen(mat, symmetric = TRUE, only.values = TRUE)$values
    eigen_rows[[sid]] <- tibble(study_id = sid, min_eigen = min(eig), positive_definite = min(eig) > 1e-8)
    if (all(!is.na(mat[upper.tri(mat)])) && min(eig) > 1e-8) {
      mats[[sid]] <- mat
      n_vec <- c(n_vec, median(rows$n, na.rm = TRUE))
      names(n_vec)[length(n_vec)] <- sid
    }
  }
  list(required_pairs = required_pairs, candidate_complete = candidate_complete, mats = mats, n_vec = n_vec, eigen_rows = bind_rows(eigen_rows))
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
      S$free[a, b] <- TRUE; S$free[b, a] <- TRUE
      S$values[a, b] <- 0.3; S$values[b, a] <- 0.3
      S$labels[a, b] <- label; S$labels[b, a] <- label
    }
  }
  list(A = A, S = S, paths = paths)
}

path_tbl <- function(...) tribble(~from, ~to, ~label, ...)
core_full <- path_tbl(
  'PE','ATT','PE_to_ATT','EE','ATT','EE_to_ATT','SI','ATT','SI_to_ATT','FC','ATT','FC_to_ATT',
  'ATT','BI','ATT_to_BI','PE','BI','PE_to_BI','EE','BI','EE_to_BI','SI','BI','SI_to_BI','FC','UB','FC_to_UB','BI','UB','BI_to_UB'
)
trust_full <- path_tbl(
  'PE','TRU','PE_to_TRU','EE','TRU','EE_to_TRU','SI','TRU','SI_to_TRU',
  'TRU','BI','TRU_to_BI','PE','BI','PE_to_BI','EE','BI','EE_to_BI','SI','BI','SI_to_BI','BI','UB','BI_to_UB'
)
models <- list(
  core7_full = list(family='core7_attitude', constructs=c('PE','EE','SI','FC','ATT','BI','UB'), paths=core_full, rationale='Baseline core7 attitude-mediation model.'),
  core6_no_PE_EE_SI_FC_ATT_BI_UB = list(family='core7_attitude', constructs=c('EE','SI','FC','ATT','BI','UB'), paths=core_full %>% filter(from!='PE', to!='PE'), rationale='PE removed: tests whether effort-based and social/condition routes can carry the attitude-intention backbone.'),
  core6_no_EE_PE_SI_FC_ATT_BI_UB = list(family='core7_attitude', constructs=c('PE','SI','FC','ATT','BI','UB'), paths=core_full %>% filter(from!='EE', to!='EE'), rationale='EE removed: tests whether usefulness-based and social/condition routes can carry the attitude-intention backbone.'),
  core6_no_SI_PE_EE_FC_ATT_BI_UB = list(family='core7_attitude', constructs=c('PE','EE','FC','ATT','BI','UB'), paths=core_full %>% filter(from!='SI', to!='SI'), rationale='SI removed: tests social influence contribution to the core adoption backbone.'),
  core6_no_FC_PE_EE_SI_ATT_BI_UB = list(family='core7_attitude', constructs=c('PE','EE','SI','ATT','BI','UB'), paths=core_full %>% filter(from!='FC', to!='FC'), rationale='FC removed: tests whether infrastructure/condition paths are needed.'),
  core6_no_ATT_direct_beliefs = list(family='core7_attitude', constructs=c('PE','EE','SI','FC','BI','UB'), paths=path_tbl('PE','BI','PE_to_BI','EE','BI','EE_to_BI','SI','BI','SI_to_BI','FC','BI','FC_to_BI','FC','UB','FC_to_UB','BI','UB','BI_to_UB'), rationale='Attitude removed: direct belief-intention model against mediation logic.'),
  core7_pure_ATT_mediation_no_direct_belief_BI = list(family='core7_attitude', constructs=c('PE','EE','SI','FC','ATT','BI','UB'), paths=core_full %>% filter(!(to=='BI' & from %in% c('PE','EE','SI'))), rationale='Pure mediation: removes direct PE/EE/SI -> BI paths to test whether ATT carries belief effects.'),
  trust6_full = list(family='trust6_mechanism', constructs=c('PE','EE','SI','TRU','BI','UB'), paths=trust_full, rationale='Baseline trust6 mechanism model.'),
  trust5_no_TRU_direct_acceptance = list(family='trust6_mechanism', constructs=c('PE','EE','SI','BI','UB'), paths=path_tbl('PE','BI','PE_to_BI','EE','BI','EE_to_BI','SI','BI','SI_to_BI','BI','UB','BI_to_UB'), rationale='Trust removed: classic direct acceptance model for testing added value of trust.'),
  trust5_no_PE_EE_SI_TRU_BI_UB = list(family='trust6_mechanism', constructs=c('EE','SI','TRU','BI','UB'), paths=trust_full %>% filter(from!='PE', to!='PE'), rationale='PE removed: tests effort/social trust route without usefulness.'),
  trust5_no_EE_PE_SI_TRU_BI_UB = list(family='trust6_mechanism', constructs=c('PE','SI','TRU','BI','UB'), paths=trust_full %>% filter(from!='EE', to!='EE'), rationale='EE removed: tests usefulness/social trust route without effort expectancy.'),
  trust6_trust_mediator_no_direct_belief_BI = list(family='trust6_mechanism', constructs=c('PE','EE','SI','TRU','BI','UB'), paths=trust_full %>% filter(!(to=='BI' & from %in% c('PE','EE','SI'))), rationale='Trust-only mediation: removes direct PE/EE/SI -> BI paths.'),
  trust6_parallel_trust_no_belief_TRU = list(family='trust6_mechanism', constructs=c('PE','EE','SI','TRU','BI','UB'), paths=trust_full %>% filter(!(to=='TRU' & from %in% c('PE','EE','SI'))), rationale='Trust as parallel predictor: removes PE/EE/SI -> TRU antecedent paths.'),
  se4_capability_effort_intention = list(family='anx_se_feasibility', constructs=c('SE','EE','BI','UB'), paths=path_tbl('SE','EE','SE_to_EE','EE','BI','EE_to_BI','SE','BI','SE_to_BI','BI','UB','BI_to_UB'), rationale='Self-efficacy feasibility: capability -> effort/intention.'),
  se4_capability_attitude_intention = list(family='anx_se_feasibility', constructs=c('SE','ATT','BI','UB'), paths=path_tbl('SE','ATT','SE_to_ATT','ATT','BI','ATT_to_BI','SE','BI','SE_to_BI','BI','UB','BI_to_UB'), rationale='Self-efficacy feasibility: capability -> attitude/intention.'),
  anx4_threat_attitude_intention = list(family='anx_se_feasibility', constructs=c('ANX','ATT','BI','UB'), paths=path_tbl('ANX','ATT','ANX_to_ATT','ATT','BI','ATT_to_BI','ANX','BI','ANX_to_BI','BI','UB','BI_to_UB'), rationale='Anxiety feasibility: threat affect -> attitude/intention.'),
  anx4_trust_threat_reliance = list(family='anx_se_feasibility', constructs=c('ANX','TRU','BI','UB'), paths=path_tbl('ANX','TRU','ANX_to_TRU','TRU','BI','TRU_to_BI','ANX','BI','ANX_to_BI','BI','UB','BI_to_UB'), rationale='Anxiety feasibility: threat -> trust/reliance/intention.'),
  se_anx_bi_capability_threat = list(family='anx_se_feasibility', constructs=c('SE','ANX','BI','UB'), paths=path_tbl('SE','ANX','SE_to_ANX','SE','BI','SE_to_BI','ANX','BI','ANX_to_BI','BI','UB','BI_to_UB'), rationale='Capability-threat feasibility: self-efficacy and anxiety as competing mechanisms.'),
  se_anx_tru_bi = list(family='anx_se_feasibility', constructs=c('SE','ANX','TRU','BI'), paths=path_tbl('SE','ANX','SE_to_ANX','ANX','TRU','ANX_to_TRU','SE','TRU','SE_to_TRU','TRU','BI','TRU_to_BI','ANX','BI','ANX_to_BI','SE','BI','SE_to_BI'), rationale='Capability-threat-trust feasibility scan without use behavior.' )
)

run_model <- function(model_id, spec) {
  built <- make_complete_mats(raw, spec$constructs)
  complete_ids <- names(built$mats)
  if (nrow(built$eigen_rows) > 0) {
    write_csv(built$eigen_rows %>% mutate(model_id=model_id, .before=1), file.path(out_dir, paste0(model_id, '_matrix_eigen_', date_tag, '.csv')))
  }
  base <- tibble(
    model_id = model_id, family = spec$family, constructs = paste(spec$constructs, collapse=','),
    structural_path_count = nrow(spec$paths), required_pairs = length(built$required_pairs),
    candidate_complete_case_studies = length(built$candidate_complete), positive_definite_complete_case_studies = length(built$mats),
    positive_definite_complete_case_ids = paste(complete_ids, collapse=';'), rationale = spec$rationale,
    stage1_status='not_run', stage1_method='none', stage1_error='', stage2_status='not_run', stage2_error='', status_code=NA_integer_,
    chisq=NA_real_, df=NA_real_, p=NA_real_, CFI=NA_real_, TLI=NA_real_, RMSEA=NA_real_, SRMR=NA_real_, AIC=NA_real_, BIC=NA_real_
  )
  if (length(built$mats) < 2) {
    base$stage1_error <- 'fewer_than_2_positive_definite_complete_case_matrices'
    return(list(summary=base, paths=tibble()))
  }
  fit1 <- tryCatch(tssem1(Cov=built$mats, n=built$n_vec, method='REM', RE.type='Diag'), error=function(e) e)
  if (inherits(fit1, 'error')) {
    rem_error <- compact_error(fit1)
    fit1 <- tryCatch(tssem1(Cov=built$mats, n=built$n_vec, method='FEM'), error=function(e) e)
    base$stage1_method <- 'REM_then_FEM'
    if (inherits(fit1, 'error')) {
      base$stage1_status <- 'failed'
      base$stage1_error <- paste(rem_error, 'FEM:', compact_error(fit1))
      return(list(summary=base, paths=tibble()))
    }
  } else {
    base$stage1_method <- 'REM'
  }
  base$stage1_status <- ifelse(identical(status_code(fit1), 0L), 'converged', paste0('status_', status_code(fit1)))
  saveRDS(fit1, file.path(out_dir, paste0(model_id, '_tssem1_fit_', date_tag, '.rds')))
  mats2 <- make_stage2_matrices(spec$constructs, spec$paths)
  fit2 <- tryCatch(tssem2(fit1, Amatrix=mats2$A, Smatrix=mats2$S, diag.constraints=TRUE, intervals.type='LB', model.name=model_id), error=function(e) e)
  if (inherits(fit2, 'error')) {
    base$stage2_status <- 'failed'
    base$stage2_error <- compact_error(fit2)
    return(list(summary=base, paths=tibble()))
  }
  saveRDS(fit2, file.path(out_dir, paste0(model_id, '_tssem2_fit_', date_tag, '.rds')))
  base$status_code <- status_code(fit2)
  base$stage2_status <- ifelse(identical(base$status_code, 0L), 'converged', paste0('status_', base$status_code))
  for (nm in c('chisq','df','p','CFI','TLI','RMSEA','SRMR','AIC','BIC')) base[[nm]] <- fit_stat(fit2, nm)
  coefs <- as.data.frame(summary(fit2)$coefficients)
  coefs$parameter <- rownames(coefs)
  path_rows <- coefs %>%
    filter(grepl('_to_', parameter, fixed=TRUE)) %>%
    transmute(
      model_id=model_id, family=spec$family, parameter=parameter,
      from=sub('_to_.*','',parameter), to=sub('.*_to_','',parameter),
      estimate=as.numeric(Estimate), std_error=as.numeric(Std.Error),
      ci_low=as.numeric(lbound), ci_high=as.numeric(ubound),
      inference_class=map2_chr(ci_low, ci_high, ci_class)
    )
  list(summary=base, paths=path_rows)
}

results <- imap(models, ~run_model(.y, .x))
summary_rows <- bind_rows(map(results, 'summary')) %>%
  mutate(across(c(chisq,p,CFI,TLI,RMSEA,SRMR,AIC,BIC), ~round(.x, 6)))
path_rows <- bind_rows(map(results, 'paths')) %>%
  mutate(across(c(estimate,std_error,ci_low,ci_high), ~round(.x, 6)))
write_both(summary_rows, 'paper_a_supplemental_model_comparison')
write_both(path_rows, 'paper_a_supplemental_structural_paths')

primary_paths <- read_csv(file.path(primary_dir, 'paper_a_model_family_structural_paths_ci_inference_20260615.csv'), show_col_types=FALSE) %>%
  mutate(pair=map2_chr(from, to, canonical_pair))
pe_ee_pairs <- primary_paths %>%
  filter(from %in% c('PE','EE'), to %in% c('ATT','BI','TRU')) %>%
  transmute(source='primary_path', family=model_family, target=to, predictor=from, model_id=route, parameter, estimate=round(estimate, 6), ci_low=round(ci_low, 6), ci_high=round(ci_high, 6), inference_class)
pe_ee_models <- summary_rows %>%
  filter(model_id %in% c('core7_full','core6_no_PE_EE_SI_FC_ATT_BI_UB','core6_no_EE_PE_SI_FC_ATT_BI_UB','trust6_full','trust5_no_PE_EE_SI_TRU_BI_UB','trust5_no_EE_PE_SI_TRU_BI_UB')) %>%
  transmute(source='model_comparison', family=family, target='model_fit', predictor=case_when(
    grepl('no_PE', model_id) ~ 'EE_retained_PE_removed',
    grepl('no_EE', model_id) ~ 'PE_retained_EE_removed',
    TRUE ~ 'PE_and_EE_retained'
  ), model_id=model_id, parameter=paste0('k=', positive_definite_complete_case_studies, '; CFI=', fmt3(CFI), '; RMSEA=', fmt3(RMSEA), '; AIC=', fmt3(AIC)), estimate=NA_real_, ci_low=NA_real_, ci_high=NA_real_, inference_class=stage2_status)
pe_ee_diagnostic <- bind_rows(pe_ee_pairs, pe_ee_models) %>%
  mutate(interpretive_note=case_when(
    source=='primary_path' & predictor=='PE' ~ 'Performance/usefulness role: instrumental value and expected outcome improvement.',
    source=='primary_path' & predictor=='EE' ~ 'Effort/ease role: usability burden and cognitive/operational effort.',
    source=='model_comparison' ~ 'Reduced model comparison for relative necessity; interpret cautiously because construct removal can change complete-case k and df.',
    TRUE ~ ''
  ))
write_both(pe_ee_diagnostic, 'paper_a_pe_vs_ee_role_comparison')

full10_pool <- read_csv(file.path(model_family_dir, 'paper_a_full10_theory_target_pairwise_random_effects_stage1_20260615.csv'), show_col_types=FALSE) %>%
  mutate(pair=as.character(pair))
primary_structural_pairs <- unique(primary_paths$pair)
construct_roles <- tibble(
  construct=c('PE','EE','SI','FC','ATT','SE','TRU','ANX','BI','UB'),
  role=c('usefulness/performance belief','effort/usability belief','social-norm belief','resource/condition belief','evaluative mediator','capability mechanism','reliance/trust mechanism','threat/anxiety mechanism','intention mediator/outcome','behavioral outcome')
)
omitted <- full10_pool %>%
  mutate(
    c_a=sub('-.*','',pair), c_b=sub('.*-','',pair),
    in_primary_structural_path=pair %in% primary_structural_pairs,
    contains_future_mechanism=grepl('ANX|SE', pair),
    contains_trust=grepl('TRU', pair),
    contains_attitude=grepl('ATT', pair),
    diagnostic_priority=case_when(
      in_primary_structural_path ~ 'already_primary_structural_path',
      contains_future_mechanism ~ 'future_mechanism_feasibility_or_pairwise_only',
      contains_trust ~ 'trust_extension_diagnostic',
      contains_attitude ~ 'attitude_extension_diagnostic',
      TRUE ~ 'theoretical_covariance_or_control_relation'
    ),
    manuscript_use=case_when(
      in_primary_structural_path ~ 'main Results path table',
      contains_future_mechanism ~ 'supplemental ANX/SE feasibility and future-mechanism discussion',
      contains_trust ~ 'trust-system theoretical framework or supplemental diagnostic',
      contains_attitude ~ 'attitude-mediation theoretical framework or supplemental diagnostic',
      TRUE ~ 'supplemental omitted-pair table'
    )
  ) %>%
  left_join(construct_roles, by=c('c_a'='construct')) %>% rename(c_a_role=role) %>%
  left_join(construct_roles, by=c('c_b'='construct')) %>% rename(c_b_role=role) %>%
  select(pair, c_a, c_a_role, c_b, c_b_role, k, total_n, pooled_r, ci_low, ci_high, i2, in_primary_structural_path, diagnostic_priority, manuscript_use) %>%
  arrange(in_primary_structural_path, diagnostic_priority, pair)
write_both(omitted, 'paper_a_full10_omitted_pair_diagnostic')

subset_scan <- map_dfr(3:6, function(size) {
  combn(c('PE','EE','SI','FC','ATT','SE','TRU','ANX','BI','UB'), size, simplify=FALSE) %>%
    keep(~any(.x %in% c('ANX','SE')) && 'BI' %in% .x) %>%
    map_dfr(function(constructs) {
      built <- make_complete_mats(raw, constructs)
      tibble(
        construct_set=paste(constructs, collapse=','), size=size,
        includes_anxiety='ANX' %in% constructs, includes_self_efficacy='SE' %in% constructs,
        candidate_complete_case_studies=length(built$candidate_complete),
        positive_definite_complete_case_studies=length(built$mats),
        positive_definite_complete_case_ids=paste(names(built$mats), collapse=';'),
        feasibility=case_when(
          length(built$mats) >= 4 ~ 'potential_primary_or_supplemental_candidate',
          length(built$mats) >= 2 ~ 'minimal_estimable_but_fragile',
          length(built$mats) == 1 ~ 'single_matrix_not_masem_estimable',
          TRUE ~ 'not_complete_case_estimable'
        )
      )
    })
}) %>% arrange(desc(positive_definite_complete_case_studies), size, construct_set)
write_both(subset_scan, 'paper_a_anx_se_complete_case_feasibility_scan')

anx_se_models <- summary_rows %>% filter(family == 'anx_se_feasibility') %>%
  select(model_id, constructs, structural_path_count, positive_definite_complete_case_studies, positive_definite_complete_case_ids, stage1_status, stage2_status, chisq, df, p, CFI, TLI, RMSEA, SRMR, AIC, BIC, rationale)
write_both(anx_se_models, 'paper_a_anx_se_targeted_model_attempts')

brief <- c(
  '# Paper A Supplemental Diagnostics: Model-Family Justification and Feasibility',
  '',
  paste0('Generated: ', date_tag),
  '',
  '## Decision recorded',
  '',
  'Paper A remains one manuscript. The primary claim is model-family MASEM: full10 is the theory-generating target and evidence map, whereas core7 and trust6 are empirical complete-case model-family members. Anxiety and self-efficacy are retained as theory-relevant mechanisms but evaluated through feasibility diagnostics rather than forced into the primary MASEM.',
  '',
  '## Supplemental analyses generated',
  '',
  '- `paper_a_supplemental_model_comparison_20260615.csv/md`: nested/reduced model comparison for core7, trust6, and targeted ANX/SE attempts.',
  '- `paper_a_supplemental_structural_paths_20260615.csv/md`: path estimates for successfully estimated supplemental models.',
  '- `paper_a_pe_vs_ee_role_comparison_20260615.csv/md`: PE and EE role comparison as usefulness versus effort mechanisms, not a PE-EE association test.',
  '- `paper_a_full10_omitted_pair_diagnostic_20260615.csv/md`: full10 relations not represented as primary structural paths and their manuscript use.',
  '- `paper_a_anx_se_complete_case_feasibility_scan_20260615.csv/md`: complete-case feasibility scan for ANX/SE-inclusive construct sets.',
  '- `paper_a_anx_se_targeted_model_attempts_20260615.csv/md`: targeted ANX/SE MASEM attempts and fit status.',
  '',
  '## Interpretation guardrail',
  '',
  'Reduced model comparisons are diagnostic rather than definitive nested chi-square tests because removing constructs can alter the complete-case study set, degrees of freedom, and matrix structure. They should be reported as sensitivity/model-family diagnostics, not as a single mechanical model-selection tournament.'
)
brief_path <- file.path(out_dir, paste0('PAPER_A_SUPPLEMENTAL_DIAGNOSTICS_SUMMARY_', date_tag, '.md'))
writeLines(brief, brief_path)
file.copy(brief_path, file.path(ms_dir, basename(brief_path)), overwrite=TRUE)
file.copy(brief_path, file.path(onedrive_dir, basename(brief_path)), overwrite=TRUE)

cat('Wrote supplemental diagnostics to:', out_dir, '\n')
