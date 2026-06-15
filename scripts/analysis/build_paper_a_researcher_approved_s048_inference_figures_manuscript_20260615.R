#!/usr/bin/env Rscript

suppressPackageStartupMessages({library(metaSEM); library(OpenMx)})

args <- commandArgs(trailingOnly = FALSE)
script_path <- normalizePath(sub('^--file=', '', grep('^--file=', args, value = TRUE)[1]), mustWork = TRUE)
repo <- normalizePath(file.path(dirname(script_path), '..', '..'), mustWork = TRUE)
results <- file.path(repo, 'data/04_extraction/05_llm_masem_substitution/results')
complete_dir <- file.path(results, 'paper_a_researcher_approved_s048_complete_case_20260615')
masem_dir <- file.path(results, 'paper_a_researcher_approved_s048_model_family_masem_20260615')
out_dir <- file.path(results, 'paper_a_researcher_approved_s048_inference_figures_manuscript_20260615')
fig_dir <- file.path(out_dir, 'figures')
onedrive_dir <- '/Users/newhosung/Library/CloudStorage/OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity/AI Adoption Meta Analysis - Documents/Meta/AI Adoption/04_analysis_strategy/Paper_A/2026-06-15_inference_figures_manuscript'
dir.create(out_dir, recursive = TRUE, showWarnings = FALSE)
dir.create(fig_dir, recursive = TRUE, showWarnings = FALSE)

fmt3 <- function(x) ifelse(is.na(x), 'NA', sprintf('%.3f', as.numeric(x)))
fmt2 <- function(x) ifelse(is.na(x), 'NA', sprintf('%.2f', as.numeric(x)))
fmt_p <- function(x) {
  x <- as.numeric(x)
  if (is.na(x)) return('NA')
  if (x < .001) return('< .001')
  sub('^0', '', sprintf('%.3f', x))
}
ci_text <- function(lo, hi) paste0('[', fmt3(lo), ', ', fmt3(hi), ']')
ci_class <- function(lo, hi) {
  if (is.na(lo) || is.na(hi)) return('ci_incomplete')
  if (lo > 0 && hi > 0) return('supported_positive_95ci')
  if (lo < 0 && hi < 0) return('supported_negative_95ci')
  return('not_supported_95ci_includes_zero')
}
ci_symbol <- function(cls) {
  if (cls %in% c('supported_positive_95ci','supported_negative_95ci')) return('CI+')
  if (cls == 'not_supported_95ci_includes_zero') return('ns')
  'CI?'
}
plot_style <- function(cls) {
  if (cls %in% c('supported_positive_95ci','supported_negative_95ci')) return('solid_black')
  if (cls == 'not_supported_95ci_includes_zero') return('dashed_gray')
  'dotted_light_gray'
}

extract_fit <- function(route, label, rds_path, complete_k) {
  fit <- readRDS(rds_path)
  s <- summary(fit)
  stat <- as.data.frame(s$stat)
  get_stat <- function(name) as.numeric(stat[name, 'Value'])
  data.frame(
    model_family = label,
    route = route,
    complete_case_k = complete_k,
    effective_sample_size = get_stat('Sample size'),
    chisq = get_stat('Chi-square of target model'),
    df = get_stat('DF of target model'),
    p = get_stat('p value of target model'),
    CFI = get_stat('CFI'),
    TLI = get_stat('TLI'),
    RMSEA = get_stat('RMSEA'),
    RMSEA_low = get_stat('RMSEA lower 95% CI'),
    RMSEA_high = get_stat('RMSEA upper 95% CI'),
    SRMR = get_stat('SRMR'),
    AIC = get_stat('AIC'),
    BIC = get_stat('BIC'),
    stringsAsFactors = FALSE
  )
}
extract_paths <- function(route, label, rds_path) {
  fit <- readRDS(rds_path)
  coef <- as.data.frame(summary(fit)$coefficients)
  coef$parameter <- rownames(coef)
  coef <- coef[grepl('_to_', coef$parameter, fixed = TRUE), ]
  parts <- strsplit(coef$parameter, '_to_', fixed = TRUE)
  out <- data.frame(
    model_family = label,
    route = route,
    parameter = coef$parameter,
    from = vapply(parts, `[`, character(1), 1),
    to = vapply(parts, `[`, character(1), 2),
    estimate = as.numeric(coef$Estimate),
    std_error = as.numeric(coef$Std.Error),
    ci_low = as.numeric(coef$lbound),
    ci_high = as.numeric(coef$ubound),
    z_value = as.numeric(coef$`z value`),
    p_value = as.numeric(coef$`Pr(>|z|)`),
    stringsAsFactors = FALSE
  )
  out$ci_text <- mapply(ci_text, out$ci_low, out$ci_high)
  out$inference_class <- mapply(ci_class, out$ci_low, out$ci_high)
  out$inference_symbol <- vapply(out$inference_class, ci_symbol, character(1))
  out$plot_style <- vapply(out$inference_class, plot_style, character(1))
  out$figure_label <- paste0('b=', fmt2(out$estimate), '\n', out$inference_symbol)
  out$manuscript_label <- paste0('b = ', fmt3(out$estimate), ', 95% CI ', out$ci_text, ', ', out$inference_symbol)
  out
}

core_route <- 'paper_a_core7_att_mediation'
trust_route <- 'paper_a_trust6_mechanism'
core_rds <- file.path(complete_dir, paste0(core_route, '_complete_case_tssem2_fit_20260615.rds'))
trust_rds <- file.path(complete_dir, paste0(trust_route, '_complete_case_tssem2_fit_20260615.rds'))
paths <- rbind(
  extract_paths(core_route, 'Core7 ATT mediation', core_rds),
  extract_paths(trust_route, 'Trust6 trust mechanism', trust_rds)
)
fit_table <- rbind(
  extract_fit(core_route, 'Core7 ATT mediation', core_rds, 4),
  extract_fit(trust_route, 'Trust6 trust mechanism', trust_rds, 7)
)
write.csv(paths, file.path(out_dir, 'paper_a_model_family_structural_paths_ci_inference_20260615.csv'), row.names = FALSE)
write.csv(fit_table, file.path(out_dir, 'paper_a_model_family_fit_with_n_20260615.csv'), row.names = FALSE)

md_table <- function(df) {
  df[] <- lapply(df, as.character)
  lines <- c(paste0('| ', paste(names(df), collapse = ' | '), ' |'), paste0('| ', paste(rep('---', ncol(df)), collapse = ' | '), ' |'))
  for (i in seq_len(nrow(df))) lines <- c(lines, paste0('| ', paste(gsub('\\|', '\\\\|', unlist(df[i, ], use.names = FALSE)), collapse = ' | '), ' |'))
  paste(lines, collapse = '\n')
}
path_md <- paths[, c('model_family','parameter','estimate','ci_text','inference_symbol','inference_class')]
path_md$estimate <- fmt3(path_md$estimate)
writeLines(md_table(path_md), file.path(out_dir, 'paper_a_model_family_structural_paths_ci_inference_20260615.md'))
fit_md <- fit_table
for (nm in c('effective_sample_size','chisq','df','p','CFI','TLI','RMSEA','RMSEA_low','RMSEA_high','SRMR','AIC','BIC')) fit_md[[nm]] <- if (nm == 'p') vapply(fit_md[[nm]], fmt_p, character(1)) else fmt3(fit_md[[nm]])
writeLines(md_table(fit_md), file.path(out_dir, 'paper_a_model_family_fit_with_n_20260615.md'))

save_plot <- function(name, width, height, expr) {
  png(file.path(fig_dir, paste0(name, '.png')), width = width, height = height, units = 'in', res = 300)
  force(expr); dev.off()
  svg(file.path(fig_dir, paste0(name, '.svg')), width = width, height = height)
  force(expr); dev.off()
}
style_args <- function(cls) {
  if (cls %in% c('supported_positive_95ci','supported_negative_95ci')) return(list(col = '#111111', lwd = 2.6, lty = 1))
  if (cls == 'not_supported_95ci_includes_zero') return(list(col = '#777777', lwd = 1.7, lty = 2))
  list(col = '#b2b2b2', lwd = 1.4, lty = 3)
}
quad_arrow <- function(x1, y1, x2, y2, curve = 0, col = '#111111', lwd = 2, lty = 1) {
  mx <- (x1 + x2) / 2; my <- (y1 + y2) / 2
  dx <- x2 - x1; dy <- y2 - y1
  nx <- -dy; ny <- dx
  len <- sqrt(nx^2 + ny^2)
  if (len > 0) { nx <- nx / len; ny <- ny / len }
  cx <- mx + curve * nx; cy <- my + curve * ny
  t <- seq(0, 1, length.out = 80)
  x <- (1 - t)^2 * x1 + 2 * (1 - t) * t * cx + t^2 * x2
  y <- (1 - t)^2 * y1 + 2 * (1 - t) * t * cy + t^2 * y2
  lines(x, y, col = col, lwd = lwd, lty = lty)
  n <- length(x)
  arrows(x[n-2], y[n-2], x[n], y[n], length = 0.075, col = col, lwd = lwd, lty = lty)
  c(mean(x), mean(y))
}
node_box <- function(x, y, label, w = .105, h = .06) {
  rect(x - w/2, y - h/2, x + w/2, y + h/2, col = '#ffffff', border = '#1f2d33', lwd = 1.3)
  text(x, y, label, cex = 0.92, font = 2, col = '#111111')
}
plot_path_model <- function(route, model_label, file_name, positions, curves, fit_row, k_note) {
  sub <- paths[paths$route == route, ]
  save_plot(file_name, 10.2, 6.5, {
    par(mar = c(1.8, 1.2, 4.5, 1.2), family = 'serif')
    plot.new(); plot.window(xlim = c(0, 1), ylim = c(0, 1), asp = 1)
    title(main = model_label, cex.main = 1.25)
    text(0.5, 0.965, 'Complete-case two-stage MASEM path diagram with likelihood-based 95% CI classification', cex = 0.82)
    for (i in seq_len(nrow(sub))) {
      from <- sub$from[i]; to <- sub$to[i]
      st <- style_args(sub$inference_class[i])
      p1 <- positions[[from]]; p2 <- positions[[to]]
      cv <- ifelse(paste(from, to, sep = '_to_') %in% names(curves), curves[[paste(from, to, sep = '_to_')]], 0)
      mid <- quad_arrow(p1[1], p1[2], p2[1], p2[2], curve = cv, col = st$col, lwd = st$lwd, lty = st$lty)
      label <- paste0('b=', fmt2(sub$estimate[i]), ' ', sub$inference_symbol[i])
      text(mid[1], mid[2] + 0.022, label, cex = 0.70, col = st$col, bg = 'white')
    }
    for (nm in names(positions)) node_box(positions[[nm]][1], positions[[nm]][2], nm)
    legend('bottomleft', legend = c('95% CI excludes 0', '95% CI includes 0', 'CI incomplete'), col = c('#111111','#777777','#b2b2b2'), lwd = c(2.6,1.7,1.4), lty = c(1,2,3), bty = 'n', cex = 0.76)
    fit_line <- paste0(k_note, '; chi-square(', round(fit_row$df), ')=', fmt2(fit_row$chisq), ', p=', fmt_p(fit_row$p), ', CFI=', fmt3(fit_row$CFI), ', TLI=', fmt3(fit_row$TLI), ', RMSEA=', fmt3(fit_row$RMSEA), ', SRMR=', fmt3(fit_row$SRMR))
    text(0.5, 0.035, fit_line, cex = 0.74)
    text(0.5, 0.005, 'Note. Exogenous covariances and residual variances were estimated but omitted from the diagram for readability.', cex = 0.68)
  })
}

full10 <- c('PE','EE','SI','FC','ATT','SE','TRU','ANX','BI','UB')
build_heatmap <- function() {
  pooled <- read.csv(file.path(masem_dir, 'paper_a_full10_theory_target_pairwise_random_effects_stage1_20260615.csv'), stringsAsFactors = FALSE)
  mat <- matrix(NA_real_, length(full10), length(full10), dimnames = list(full10, full10)); diag(mat) <- 1
  kmat <- matrix(NA_integer_, length(full10), length(full10), dimnames = list(full10, full10)); diag(kmat) <- NA_integer_
  for (i in seq_len(nrow(pooled))) {
    parts <- strsplit(pooled$pair[i], '-', fixed = TRUE)[[1]]
    if (all(parts %in% full10)) {
      mat[parts[1], parts[2]] <- pooled$pooled_r[i]; mat[parts[2], parts[1]] <- pooled$pooled_r[i]
      kmat[parts[1], parts[2]] <- pooled$k[i]; kmat[parts[2], parts[1]] <- pooled$k[i]
    }
  }
  pal <- colorRampPalette(c('#315f86', '#f7f2e8', '#ad3f34'))(101)
  save_plot('figure_1_full10_theoretical_evidence_map_heatmap_ci_20260615', 9.1, 8.0, {
    par(mar = c(7.5, 7.2, 4.5, 6), family = 'serif')
    image(seq_along(full10), seq_along(full10), t(mat[full10, rev(full10)]), col = pal, zlim = c(-.2,.85), axes = FALSE, xlab = '', ylab = '', main = 'Full10 theoretical evidence map')
    axis(1, at = seq_along(full10), labels = full10, las = 2)
    axis(2, at = seq_along(full10), labels = rev(full10), las = 2)
    box()
    for (i in seq_along(full10)) for (j in seq_along(full10)) {
      row <- rev(full10)[i]; col <- full10[j]; v <- mat[row, col]
      if (!is.na(v)) {
        txt <- ifelse(row == col, '1.00', paste0(fmt2(v), '\n(k=', kmat[row,col], ')'))
        tcol <- ifelse(abs(v) > .55, 'white', '#242424')
        text(j, i, txt, cex = 0.55, col = tcol)
      }
    }
    mtext('Cells show pairwise random-effects pooled r and k. This is an evidence map, not a full10 SEM path estimate.', side = 1, line = 5.8, cex = .72)
    usr <- par('usr'); yseq <- seq(usr[3], usr[4], length.out = length(pal) + 1); xleft <- usr[2] + .45; xright <- usr[2] + .75
    for (k in seq_along(pal)) rect(xleft, yseq[k], xright, yseq[k+1], col = pal[k], border = NA, xpd = TRUE)
    text(xright + .35, yseq[1], '-.20', cex = .7, xpd = TRUE)
    text(xright + .35, yseq[length(yseq)], '.85', cex = .7, xpd = TRUE)
  })
}

build_heatmap()
core_pos <- list(PE=c(.10,.80), EE=c(.10,.62), SI=c(.10,.44), FC=c(.10,.26), ATT=c(.42,.60), BI=c(.68,.60), UB=c(.90,.42))
core_curves <- list(PE_to_BI=-.12, EE_to_BI=-.05, SI_to_BI=.06, FC_to_UB=.10, ATT_to_BI=0, BI_to_UB=0)
trust_pos <- list(PE=c(.10,.78), EE=c(.10,.55), SI=c(.10,.32), TRU=c(.43,.60), BI=c(.68,.53), UB=c(.91,.53))
trust_curves <- list(PE_to_BI=-.12, EE_to_BI=0, SI_to_BI=.10, TRU_to_BI=0, BI_to_UB=0)
plot_path_model(core_route, 'Core7 ATT mediation model-family MASEM', 'figure_2_core7_att_mediation_masem_path_ci_20260615', core_pos, core_curves, fit_table[fit_table$route == core_route, ], 'k=4 positive-definite complete-case matrices; N_eff=3,172')
plot_path_model(trust_route, 'Trust6 mechanism model-family MASEM', 'figure_3_trust6_mechanism_masem_path_ci_20260615', trust_pos, trust_curves, fit_table[fit_table$route == trust_route, ], 'k=7 positive-definite complete-case matrices; N_eff=10,315')

caption_lines <- c(
  '# Paper A model-family MASEM figure captions and inference notes',
  '',
  'Date: 2026-06-15',
  '',
  '## Figure 1',
  '',
  'Figure 1. Full 10-construct theoretical evidence map. Cells report pairwise random-effects pooled correlations and the number of contributing studies for each construct pair. The figure is an evidence-map summary, not a full 10-construct SEM estimate, because no primary study supplied a complete 10-construct correlation matrix and sparse partial-matrix TSSEM did not yield a positive-definite implied covariance structure.',
  '',
  '## Figure 2',
  '',
  paste0('Figure 2. Core7 attitude-mediation complete-case MASEM path diagram. Solid black paths have likelihood-based 95% confidence intervals excluding zero, dashed gray paths have intervals including zero, and dotted light-gray paths have incomplete intervals and are not classified as supported. The model used k = 4 positive-definite complete-case matrices (N_eff = 3,172) and showed good fit, chi-square(5) = ', fmt2(fit_table$chisq[fit_table$route==core_route]), ', p = ', fmt_p(fit_table$p[fit_table$route==core_route]), ', CFI = ', fmt3(fit_table$CFI[fit_table$route==core_route]), ', TLI = ', fmt3(fit_table$TLI[fit_table$route==core_route]), ', RMSEA = ', fmt3(fit_table$RMSEA[fit_table$route==core_route]), ', SRMR = ', fmt3(fit_table$SRMR[fit_table$route==core_route]), '.'),
  '',
  '## Figure 3',
  '',
  paste0('Figure 3. Trust6 mechanism complete-case MASEM path diagram. Solid black paths have likelihood-based 95% confidence intervals excluding zero, dashed gray paths have intervals including zero, and dotted light-gray paths have incomplete intervals and are not classified as supported. The model used k = 7 positive-definite complete-case matrices (N_eff = 10,315) and showed good fit, chi-square(4) = ', fmt2(fit_table$chisq[fit_table$route==trust_route]), ', p = ', fmt_p(fit_table$p[fit_table$route==trust_route]), ', CFI = ', fmt3(fit_table$CFI[fit_table$route==trust_route]), ', TLI = ', fmt3(fit_table$TLI[fit_table$route==trust_route]), ', RMSEA = ', fmt3(fit_table$RMSEA[fit_table$route==trust_route]), ', SRMR = ', fmt3(fit_table$SRMR[fit_table$route==trust_route]), '.'),
  '',
  '## Inference rule for figures and tables',
  '',
  'Because the metaSEM Stage 2 summaries returned likelihood-based confidence intervals but not finite standard errors or z-based p values for individual paths, path-level support is classified by whether the reported 95% confidence interval excludes zero. Paths with incomplete intervals are shown separately and are not interpreted as statistically supported.'
)
writeLines(caption_lines, file.path(out_dir, 'PAPER_A_MODEL_FAMILY_FIGURE_CAPTIONS_AND_INFERENCE_NOTES_20260615.md'))

methods_results <- c(
  '# Paper A Methods and Results insert: model-family MASEM',
  '',
  'Date: 2026-06-15',
  '',
  '## Methods insert',
  '',
  'We treated the 10-construct AI adoption framework as the theoretical target and first evaluated whether the source-supported evidence base could sustain a single full-network MASEM. The target framework included performance expectancy, effort expectancy, social influence, facilitating conditions, attitude, self-efficacy, trust, AI anxiety, behavioral intention, and use behavior. Because no study supplied a complete 10-construct correlation matrix and sparse partial-matrix TSSEM produced non-positive-definite implied covariance structures, we did not force the full network into a single structural estimate. Instead, we used a model-family MASEM strategy in which the full 10-construct network was retained as the theoretical evidence map and empirically estimable submodels were fit as complete-case TSSEM/MASEM models.',
  '',
  'The empirical model family included a seven-construct attitude-mediation model and a six-construct trust-mechanism model. Complete-case matrices were retained only when all required construct pairs were present and the study-level correlation matrix was positive definite. Stage 1 used random-effects TSSEM. Stage 2 fit the prespecified structural model to the pooled correlation matrix. Path-level support was evaluated using likelihood-based 95% confidence intervals from the Stage 2 model; paths were interpreted as supported when the interval excluded zero. Because finite standard errors and z-based p values were not returned for individual paths, paths with incomplete intervals were flagged as indeterminate rather than treated as significant.',
  '',
  '## Results insert',
  '',
  'The full 10-construct target reached complete pairwise coverage across the source-supported evidence base (45/45 construct pairs), but no study provided a complete same-study 10-construct matrix. Sparse partial-matrix TSSEM remained non-estimable because the implied covariance structure was not positive definite. The full10 model was therefore retained as a theoretical evidence map rather than reported as a single SEM result.',
  '',
  paste0('The core7 attitude-mediation model was estimable with four positive-definite complete-case matrices. The model fit the pooled matrix well, chi-square(5) = ', fmt2(fit_table$chisq[fit_table$route==core_route]), ', p = ', fmt_p(fit_table$p[fit_table$route==core_route]), ', CFI = ', fmt3(fit_table$CFI[fit_table$route==core_route]), ', TLI = ', fmt3(fit_table$TLI[fit_table$route==core_route]), ', RMSEA = ', fmt3(fit_table$RMSEA[fit_table$route==core_route]), ', and SRMR = ', fmt3(fit_table$SRMR[fit_table$route==core_route]), '. Supported paths included FC -> ATT, SI -> BI, ATT -> BI, FC -> UB, and BI -> UB. PE -> ATT and SI -> ATT had intervals that included zero, while EE -> ATT, PE -> BI, and EE -> BI had incomplete likelihood-based intervals and were not classified as supported.'),
  '',
  paste0('The trust6 mechanism model was estimable with seven positive-definite complete-case matrices. Model fit was also strong, chi-square(4) = ', fmt2(fit_table$chisq[fit_table$route==trust_route]), ', p = ', fmt_p(fit_table$p[fit_table$route==trust_route]), ', CFI = ', fmt3(fit_table$CFI[fit_table$route==trust_route]), ', TLI = ', fmt3(fit_table$TLI[fit_table$route==trust_route]), ', RMSEA = ', fmt3(fit_table$RMSEA[fit_table$route==trust_route]), ', and SRMR = ', fmt3(fit_table$SRMR[fit_table$route==trust_route]), '. Supported paths included EE -> BI, TRU -> BI, and BI -> UB. EE -> TRU, SI -> TRU, and SI -> BI had intervals that included zero, while PE -> TRU and PE -> BI had incomplete likelihood-based intervals and were not classified as supported. These results support trust as an AI-specific mechanism linking adoption beliefs to behavioral intention, while anxiety and self-efficacy remain theory-relevant constructs for the full10 evidence map or future reduced extensions rather than confirmed mediators in the current empirical MASEM family.'),
  '',
  '## Table: path-level inference',
  '',
  md_table(path_md),
  '',
  '## Table: model fit',
  '',
  md_table(fit_md)
)
writeLines(methods_results, file.path(out_dir, 'PAPER_A_MODEL_FAMILY_METHODS_RESULTS_INSERT_20260615.md'))

if (dir.exists(onedrive_dir)) unlink(onedrive_dir, recursive = TRUE)
dir.create(dirname(onedrive_dir), recursive = TRUE, showWarnings = FALSE)
file.copy(out_dir, dirname(onedrive_dir), recursive = TRUE)
cat('out_dir=', out_dir, '\n', sep='')
cat('fig_dir=', fig_dir, '\n', sep='')
cat('onedrive_dir=', onedrive_dir, '\n', sep='')
cat('path_rows=', nrow(paths), '\n', sep='')
