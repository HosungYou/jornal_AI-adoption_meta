#!/usr/bin/env Rscript
suppressPackageStartupMessages({library(readr); library(dplyr); library(purrr); library(tibble); library(metaSEM); library(OpenMx)})
repo <- normalizePath(file.path(dirname(normalizePath(sub('^--file=', '', grep('^--file=', commandArgs(FALSE), value=TRUE)[1]), mustWork=TRUE)), '..', '..'), mustWork=TRUE)
input_path <- file.path(repo, 'data/04_extraction/05_llm_masem_substitution/results/paper_a_latest_human_workbook_audit_20260614/paper_a_latest_human_workbook_direct_r_input_20260614.csv')
out_dir <- file.path(repo, 'data/04_extraction/05_llm_masem_substitution/results/paper_a_complete_case_latest_human_20260614')
dir.create(out_dir, recursive=TRUE, showWarnings=FALSE)
safe_num <- function(x) suppressWarnings(as.numeric(x))
canon_pair <- function(a,b) paste(sort(c(a,b)), collapse='-')
status_code <- function(fit) tryCatch(fit$mx.fit@output$status$code, error=function(e) NA_integer_)
compact_error <- function(e) { msg <- gsub('[[:space:]]+', ' ', conditionMessage(e)); if (nchar(msg)>300) paste0(substr(msg,1,300),'...') else msg }
raw <- read_csv(input_path, show_col_types=FALSE) %>% mutate(study_id=as.character(study_id), c1=as.character(construct_1), c2=as.character(construct_2), r_numeric=safe_num(r_numeric), sample_size_numeric=safe_num(sample_size_numeric), pair=map2_chr(c1,c2,canon_pair)) %>% filter(!is.na(r_numeric), abs(r_numeric)<1, !is.na(sample_size_numeric), sample_size_numeric>3)
routes <- list(
  paper_a_core7_att_complete_case=list(constructs=c('PE','EE','SI','FC','ATT','BI','UB'), paths=tribble(~from,~to,~label,'PE','ATT','PE_to_ATT','EE','ATT','EE_to_ATT','SI','ATT','SI_to_ATT','FC','ATT','FC_to_ATT','ATT','BI','ATT_to_BI','PE','BI','PE_to_BI','EE','BI','EE_to_BI','SI','BI','SI_to_BI','FC','UB','FC_to_UB','BI','UB','BI_to_UB')),
  paper_a_trust6_complete_case=list(constructs=c('PE','EE','SI','TRU','BI','UB'), paths=tribble(~from,~to,~label,'PE','TRU','PE_to_TRU','EE','TRU','EE_to_TRU','SI','TRU','SI_to_TRU','TRU','BI','TRU_to_BI','PE','BI','PE_to_BI','EE','BI','EE_to_BI','SI','BI','SI_to_BI','BI','UB','BI_to_UB'))
)
make_mats <- function(constructs) {
  pair_data <- raw %>% filter(c1 %in% constructs, c2 %in% constructs, c1 != c2) %>% group_by(study_id,c1,c2,pair) %>% summarise(r=mean(r_numeric, na.rm=TRUE), n=median(sample_size_numeric, na.rm=TRUE), .groups='drop')
  required <- length(constructs)*(length(constructs)-1)/2
  keep_ids <- pair_data %>% group_by(study_id) %>% summarise(pair_count=n_distinct(pair), n=median(n, na.rm=TRUE), .groups='drop') %>% filter(pair_count==required)
  mats <- list(); n <- c()
  for (sid in keep_ids$study_id) {
    mat <- diag(length(constructs)); dimnames(mat) <- list(constructs, constructs)
    rows <- pair_data %>% filter(study_id==sid)
    for (i in seq_len(nrow(rows))) { mat[rows$c1[i], rows$c2[i]] <- rows$r[i]; mat[rows$c2[i], rows$c1[i]] <- rows$r[i] }
    eig <- min(eigen(mat, symmetric=TRUE, only.values=TRUE)$values)
    if (eig > 1e-8) { mats[[sid]] <- mat; n <- c(n, keep_ids$n[match(sid, keep_ids$study_id)]); names(n)[length(n)] <- sid }
  }
  list(mats=mats,n=n,complete_ids=names(mats),candidate_complete=nrow(keep_ids))
}
make_stage2 <- function(constructs, paths) {
  p <- length(constructs); idx <- setNames(seq_along(constructs), constructs)
  A <- mxMatrix(type='Full', nrow=p, ncol=p, free=FALSE, values=0, labels=NA, name='A')
  for (i in seq_len(nrow(paths))) { A$free[idx[[paths$to[i]]], idx[[paths$from[i]]]] <- TRUE; A$labels[idx[[paths$to[i]]], idx[[paths$from[i]]]] <- paths$label[i]; A$values[idx[[paths$to[i]]], idx[[paths$from[i]]]] <- 0.15 }
  endogenous <- unique(paths$to); exogenous <- setdiff(constructs, endogenous)
  S <- mxMatrix(type='Symm', nrow=p, ncol=p, free=FALSE, values=0, labels=NA, name='S')
  for (name in exogenous) S$values[idx[[name]],idx[[name]]] <- 1
  for (name in endogenous) { S$free[idx[[name]],idx[[name]]] <- TRUE; S$values[idx[[name]],idx[[name]]] <- .5; S$labels[idx[[name]],idx[[name]]] <- paste0('Var_e_', name) }
  if (length(exogenous)>=2) for (col in seq_len(ncol(combn(exogenous,2)))) { pair <- combn(exogenous,2)[,col]; a <- idx[[pair[1]]]; b <- idx[[pair[2]]]; lab <- paste0('Cov_', pair[1], '_', pair[2]); S$free[a,b] <- S$free[b,a] <- TRUE; S$values[a,b] <- S$values[b,a] <- .3; S$labels[a,b] <- S$labels[b,a] <- lab }
  list(A=A,S=S)
}
results <- list(); path_rows_all <- tibble(); fit_rows_all <- tibble()
for (route in names(routes)) {
  spec <- routes[[route]]; built <- make_mats(spec$constructs)
  stage1_status <- 'not_run'; stage2_status <- 'not_run'; stage1_error <- ''; stage2_error <- ''; method <- 'none'
  fit1 <- NULL; fit2 <- NULL
  if (length(built$mats) >= 2) {
    fit1_try <- tryCatch(tssem1(Cov=built$mats, n=built$n, method='REM', RE.type='Diag'), error=function(e)e)
    if (inherits(fit1_try,'error')) { stage1_error <- compact_error(fit1_try); fit1_try <- tryCatch(tssem1(Cov=built$mats, n=built$n, method='FEM'), error=function(e)e); method <- 'REM_then_FEM' } else method <- 'REM'
    if (inherits(fit1_try,'error')) { stage1_status <- 'failed'; stage1_error <- paste(stage1_error, 'FEM:', compact_error(fit1_try)) } else { fit1 <- fit1_try; stage1_status <- ifelse(identical(status_code(fit1),0L),'converged',paste0('status_',status_code(fit1))); saveRDS(fit1, file.path(out_dir,paste0(route,'_tssem1_fit_20260614.rds'))) }
  } else stage1_error <- 'fewer than 2 positive-definite complete-case matrices'
  if (!is.null(fit1)) {
    mats2 <- make_stage2(spec$constructs, spec$paths)
    fit2_try <- tryCatch(tssem2(fit1, Amatrix=mats2$A, Smatrix=mats2$S, diag.constraints=TRUE, intervals.type='LB', model.name=route), error=function(e)e)
    if (inherits(fit2_try,'error')) { stage2_status <- 'failed'; stage2_error <- compact_error(fit2_try) } else { fit2 <- fit2_try; stage2_status <- ifelse(identical(status_code(fit2),0L),'converged',paste0('status_',status_code(fit2))); co <- coef(fit2); path_rows_all <- bind_rows(path_rows_all, tibble(route=route, parameter=names(co), estimate=as.numeric(co))); saveRDS(fit2, file.path(out_dir,paste0(route,'_tssem2_fit_20260614.rds'))) }
  }
  results[[route]] <- tibble(route=route, constructs=paste(spec$constructs, collapse=','), candidate_complete_case_studies=built$candidate_complete, positive_definite_complete_case_studies=length(built$mats), stage1_status=stage1_status, stage1_method=method, stage1_error=stage1_error, stage2_status=stage2_status, stage2_error=stage2_error)
}
summary <- bind_rows(results)
write_csv(summary, file.path(out_dir,'paper_a_latest_human_complete_case_summary_20260614.csv'))
if (nrow(path_rows_all)>0) write_csv(path_rows_all, file.path(out_dir,'paper_a_latest_human_complete_case_stage2_paths_20260614.csv'))
report <- c('# Paper A Latest Human Complete-Case TSSEM Probe','', 'Date: 2026-06-14','', paste0('Input: `', sub(paste0(repo,'/'),'',input_path), '`'), '', '## Summary','', '| Route | Complete candidates | Positive-definite complete cases | Stage 1 | Stage 2 | Boundary |', '| --- | ---: | ---: | --- | --- | --- |')
for (i in seq_len(nrow(summary))) report <- c(report, paste0('| ', summary$route[i], ' | ', summary$candidate_complete_case_studies[i], ' | ', summary$positive_definite_complete_case_studies[i], ' | ', summary$stage1_status[i], ' | ', summary$stage2_status[i], ' | Diagnostic only; not full10 primary. |'))
report <- c(report, '', '## Claim boundary', '', 'This probe uses only complete-case reduced routes from the latest human workbook input. It can diagnose whether a reduced structural route is technically estimable. It does not solve the full 10-construct primary route, which still has zero full10 complete-case studies.')
writeLines(report, file.path(out_dir,'PAPER_A_LATEST_HUMAN_COMPLETE_CASE_TSSEM_PROBE_20260614.md'))
cat(paste(capture.output(print(summary)), collapse='\n'), '\n')
