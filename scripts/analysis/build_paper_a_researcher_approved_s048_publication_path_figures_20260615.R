#!/usr/bin/env Rscript

args <- commandArgs(trailingOnly = FALSE)
script_path <- normalizePath(sub('^--file=', '', grep('^--file=', args, value = TRUE)[1]), mustWork = TRUE)
repo <- normalizePath(file.path(dirname(script_path), '..', '..'), mustWork = TRUE)
results <- file.path(repo, 'data/04_extraction/05_llm_masem_substitution/results')
inf_dir <- file.path(results, 'paper_a_researcher_approved_s048_inference_figures_manuscript_20260615')
fig_dir <- file.path(inf_dir, 'figures')
onedrive_dir <- '/Users/newhosung/Library/CloudStorage/OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity/AI Adoption Meta Analysis - Documents/Meta/AI Adoption/04_analysis_strategy/Paper_A/2026-06-15_inference_figures_manuscript'
paths <- read.csv(file.path(inf_dir, 'paper_a_model_family_structural_paths_ci_inference_20260615.csv'), stringsAsFactors = FALSE)
fit <- read.csv(file.path(inf_dir, 'paper_a_model_family_fit_with_n_20260615.csv'), stringsAsFactors = FALSE)

fmt2 <- function(x) sprintf('%.2f', as.numeric(x))
fmt3 <- function(x) sprintf('%.3f', as.numeric(x))
fmt_p <- function(x) { x <- as.numeric(x); if (x < .001) '< .001' else sub('^0', '', sprintf('%.3f', x)) }
style_args <- function(cls) {
  if (cls %in% c('supported_positive_95ci','supported_negative_95ci')) return(list(col = '#111111', lwd = 2.4, lty = 1))
  if (cls == 'not_supported_95ci_includes_zero') return(list(col = '#6f6f6f', lwd = 1.7, lty = 2))
  list(col = '#a9a9a9', lwd = 1.5, lty = 3)
}

save_plot <- function(name, width, height, expr) {
  png(file.path(fig_dir, paste0(name, '.png')), width = width, height = height, units = 'in', res = 300)
  force(expr); dev.off()
  svg(file.path(fig_dir, paste0(name, '.svg')), width = width, height = height)
  force(expr); dev.off()
}

quad_arrow <- function(x1, y1, x2, y2, curve = 0, col = '#111111', lwd = 2, lty = 1) {
  mx <- (x1 + x2) / 2; my <- (y1 + y2) / 2
  dx <- x2 - x1; dy <- y2 - y1
  nx <- -dy; ny <- dx
  len <- sqrt(nx^2 + ny^2)
  if (len > 0) { nx <- nx / len; ny <- ny / len }
  cx <- mx + curve * nx; cy <- my + curve * ny
  t <- seq(0, 1, length.out = 100)
  x <- (1 - t)^2 * x1 + 2 * (1 - t) * t * cx + t^2 * x2
  y <- (1 - t)^2 * y1 + 2 * (1 - t) * t * cy + t^2 * y2
  lines(x, y, col = col, lwd = lwd, lty = lty, lend = 'round')
  n <- length(x)
  arrows(x[n-4], y[n-4], x[n], y[n], length = 0.07, col = col, lwd = lwd, lty = lty)
}

node_box <- function(x, y, label, w = .092, h = .055) {
  rect(x - w/2, y - h/2, x + w/2, y + h/2, col = '#ffffff', border = '#111111', lwd = 1.2)
  text(x, y, label, cex = 0.88, font = 2, col = '#111111')
}
label_box <- function(x, y, label, col) {
  w <- strwidth(label, cex = .70) * 1.25
  h <- strheight(label, cex = .70) * 1.55
  rect(x - w/2, y - h/2, x + w/2, y + h/2, col = adjustcolor('white', alpha.f = .88), border = NA)
  text(x, y, label, cex = .70, col = col)
}

plot_model <- function(route, title, subtitle, file_name, positions, curves, label_pos, k_note) {
  sub <- paths[paths$route == route, ]
  fr <- fit[fit$route == route, ][1, ]
  save_plot(file_name, 9.6, 6.1, {
    par(mar = c(2.6, 1.0, 4.2, 1.0), family = 'serif')
    plot.new(); plot.window(xlim = c(0, 1), ylim = c(0, 1), asp = 1)
    title(main = title, cex.main = 1.18, line = 2.0)
    mtext(subtitle, side = 3, line = .55, cex = .78)
    legend(x = .02, y = .98, legend = c('95% CI excludes 0', '95% CI includes 0', 'CI incomplete'), col = c('#111111','#6f6f6f','#a9a9a9'), lwd = c(2.4,1.7,1.5), lty = c(1,2,3), bty = 'n', cex = .72, y.intersp = 1.1)
    for (i in seq_len(nrow(sub))) {
      param <- sub$parameter[i]
      from <- sub$from[i]; to <- sub$to[i]
      st <- style_args(sub$inference_class[i])
      p1 <- positions[[from]]; p2 <- positions[[to]]
      cv <- if (param %in% names(curves)) curves[[param]] else 0
      quad_arrow(p1[1], p1[2], p2[1], p2[2], curve = cv, col = st$col, lwd = st$lwd, lty = st$lty)
    }
    for (nm in names(positions)) node_box(positions[[nm]][1], positions[[nm]][2], nm)
    for (i in seq_len(nrow(sub))) {
      param <- sub$parameter[i]
      lp <- label_pos[[param]]
      if (!is.null(lp)) {
        st <- style_args(sub$inference_class[i])
        label_box(lp[1], lp[2], fmt2(sub$estimate[i]), st$col)
      }
    }
    fit_line <- paste0(k_note, '; chi-square(', round(fr$df), ')=', fmt2(fr$chisq), ', p=', fmt_p(fr$p), ', CFI=', fmt3(fr$CFI), ', TLI=', fmt3(fr$TLI), ', RMSEA=', fmt3(fr$RMSEA), ', SRMR=', fmt3(fr$SRMR))
    mtext(fit_line, side = 1, line = 1.15, cex = .70)
    mtext('Note. Coefficients are standardized path estimates. Exogenous covariances and residual variances are estimated but omitted.', side = 1, line = 2.05, cex = .65)
  })
}

core_pos <- list(PE=c(.12,.78), EE=c(.12,.60), SI=c(.12,.42), FC=c(.12,.24), ATT=c(.46,.61), BI=c(.70,.61), UB=c(.90,.38))
core_curves <- list(PE_to_ATT=0, EE_to_ATT=0, SI_to_ATT=0, FC_to_ATT=0, ATT_to_BI=0, PE_to_BI=-.15, EE_to_BI=-.06, SI_to_BI=.04, FC_to_UB=.15, BI_to_UB=0)
core_lab <- list(PE_to_ATT=c(.30,.73), EE_to_ATT=c(.30,.61), SI_to_ATT=c(.30,.50), FC_to_ATT=c(.30,.37), ATT_to_BI=c(.58,.66), PE_to_BI=c(.45,.82), EE_to_BI=c(.48,.71), SI_to_BI=c(.49,.49), FC_to_UB=c(.53,.27), BI_to_UB=c(.80,.51))
trust_pos <- list(PE=c(.12,.76), EE=c(.12,.52), SI=c(.12,.28), TRU=c(.46,.61), BI=c(.70,.52), UB=c(.90,.52))
trust_curves <- list(PE_to_TRU=0, EE_to_TRU=0, SI_to_TRU=0, TRU_to_BI=0, PE_to_BI=-.16, EE_to_BI=-.02, SI_to_BI=.10, BI_to_UB=0)
trust_lab <- list(PE_to_TRU=c(.30,.73), EE_to_TRU=c(.30,.56), SI_to_TRU=c(.30,.39), TRU_to_BI=c(.58,.62), PE_to_BI=c(.46,.82), EE_to_BI=c(.46,.48), SI_to_BI=c(.48,.33), BI_to_UB=c(.80,.57))

plot_model('paper_a_core7_att_mediation', 'Core7 ATT mediation model-family MASEM', 'Complete-case two-stage MASEM; path support classified by likelihood-based 95% CI', 'figure_2_core7_att_mediation_masem_path_ci_20260615', core_pos, core_curves, core_lab, 'k=4 positive-definite complete-case matrices; N_eff=3,172')
plot_model('paper_a_trust6_mechanism', 'Trust6 mechanism model-family MASEM', 'Complete-case two-stage MASEM; path support classified by likelihood-based 95% CI', 'figure_3_trust6_mechanism_masem_path_ci_20260615', trust_pos, trust_curves, trust_lab, 'k=7 positive-definite complete-case matrices; N_eff=10,315')

# Keep OneDrive mirror synchronized for the updated figures.
if (dir.exists(onedrive_dir)) {
  fig_target <- file.path(onedrive_dir, 'figures')
  if (!dir.exists(fig_target)) dir.create(fig_target, recursive = TRUE, showWarnings = FALSE)
  files <- list.files(fig_dir, pattern = '^figure_[23].*\\.(png|svg)$', full.names = TRUE)
  file.copy(files, fig_target, overwrite = TRUE)
}
cat('updated_publication_path_figures=', fig_dir, '\n', sep='')
