#!/usr/bin/env Rscript

args <- commandArgs(trailingOnly = FALSE)
script_path <- normalizePath(sub('^--file=', '', grep('^--file=', args, value = TRUE)[1]), mustWork = TRUE)
repo <- normalizePath(file.path(dirname(script_path), '..', '..'), mustWork = TRUE)
results <- file.path(repo, 'data/04_extraction/05_llm_masem_substitution/results')
masem_dir <- file.path(results, 'paper_a_researcher_approved_s048_model_family_masem_20260615')
complete_dir <- file.path(results, 'paper_a_researcher_approved_s048_complete_case_20260615')
out_dir <- file.path(results, 'paper_a_researcher_approved_s048_figures_20260615')
onedrive_dir <- '/Users/newhosung/Library/CloudStorage/OneDrive-SharedLibraries-ThePennsylvaniaStateUniversity/AI Adoption Meta Analysis - Documents/Meta/AI Adoption/04_analysis_strategy/Paper_A/2026-06-15_researcher_approved_s048_figures'
dir.create(out_dir, recursive = TRUE, showWarnings = FALSE)

full10 <- c('PE','EE','SI','FC','ATT','SE','TRU','ANX','BI','UB')

save_plot <- function(name, width, height, expr) {
  png(file.path(out_dir, paste0(name, '.png')), width = width, height = height, units = 'in', res = 300)
  force(expr)
  dev.off()
  svg(file.path(out_dir, paste0(name, '.svg')), width = width, height = height)
  force(expr)
  dev.off()
}

build_heatmap <- function() {
  df <- read.csv(file.path(masem_dir, 'paper_a_full10_theory_target_pairwise_pooled_matrix_20260615.csv'), stringsAsFactors = FALSE)
  mat <- matrix(NA_real_, length(full10), length(full10), dimnames = list(full10, full10))
  for (i in seq_len(nrow(df))) {
    if (df$construct_1[i] %in% full10 && df$construct_2[i] %in% full10) {
      mat[df$construct_1[i], df$construct_2[i]] <- as.numeric(df$pooled_r[i])
    }
  }
  pal <- colorRampPalette(c('#2f5d8c', '#f7f2e8', '#b24a3b'))(101)
  zlim <- c(-0.2, 0.85)
  save_plot('figure_1_full10_pairwise_pooled_heatmap_20260615', 8.4, 7.4, {
    par(mar = c(7, 7, 4, 6), family = 'serif')
    image(seq_along(full10), seq_along(full10), t(mat[full10, rev(full10)]), col = pal, zlim = zlim, axes = FALSE, xlab = '', ylab = '', main = 'Full10 theoretical target: pairwise pooled correlations')
    axis(1, at = seq_along(full10), labels = full10, las = 2)
    axis(2, at = seq_along(full10), labels = rev(full10), las = 2)
    box()
    for (i in seq_along(full10)) {
      for (j in seq_along(full10)) {
        v <- mat[rev(full10)[i], full10[j]]
        if (!is.na(v)) {
          col <- ifelse(abs(v) > 0.55, 'white', '#242424')
          text(j, i, sprintf('%.2f', v), cex = 0.72, col = col)
        }
      }
    }
    usr <- par('usr')
    yseq <- seq(usr[3], usr[4], length.out = length(pal) + 1)
    xleft <- usr[2] + 0.4
    xright <- usr[2] + 0.7
    for (k in seq_along(pal)) rect(xleft, yseq[k], xright, yseq[k + 1], col = pal[k], border = NA, xpd = TRUE)
    text(xright + 0.35, yseq[1], sprintf('%.1f', zlim[1]), cex = 0.7, xpd = TRUE)
    text(xright + 0.35, yseq[length(yseq)], sprintf('%.2f', zlim[2]), cex = 0.7, xpd = TRUE)
    text(xleft, usr[3] - 1.05, 'Note. Full10 pairwise coverage is 45/45, but full10 complete-case MASEM remains non-estimable.', adj = 0, cex = 0.72, xpd = TRUE)
  })
}

draw_path_diagram <- function(route, name, title, positions) {
  paths <- read.csv(file.path(complete_dir, paste0(route, '_complete_case_stage2_paths_20260615.csv')), stringsAsFactors = FALSE)
  paths <- paths[paths$parameter_family == 'structural_path', ]
  save_plot(name, 9.4, 5.8, {
    par(mar = c(2, 2, 4, 2), family = 'serif')
    plot.new(); plot.window(xlim = c(-0.06, 1.06), ylim = c(-0.06, 1.06), asp = 1)
    title(main = title, cex.main = 1.2)
    for (i in seq_len(nrow(paths))) {
      parts <- strsplit(paths$parameter[i], '_to_', fixed = TRUE)[[1]]
      from <- parts[1]; to <- parts[2]; est <- as.numeric(paths$estimate[i])
      x1 <- positions[[from]][1]; y1 <- positions[[from]][2]
      x2 <- positions[[to]][1]; y2 <- positions[[to]][2]
      col <- ifelse(est >= 0, '#254f6f', '#9d3b33')
      lwd <- 1.2 + min(abs(est), 0.8) * 4
      arrows(x1, y1, x2, y2, length = 0.08, lwd = lwd, col = adjustcolor(col, alpha.f = 0.75))
      text((x1 + x2) / 2, (y1 + y2) / 2 + 0.035, sprintf('%.2f', est), cex = 0.8, col = '#1f2528')
    }
    for (node in names(positions)) {
      x <- positions[[node]][1]; y <- positions[[node]][2]
      symbols(x, y, circles = 0.052, inches = FALSE, add = TRUE, bg = '#f4ead7', fg = '#2c3b42', lwd = 1.4)
      text(x, y, node, cex = 1.0, font = 2)
    }
    text(0.5, -0.025, 'Complete-case TSSEM/MASEM structural paths from the 2026-06-15 researcher-approved S048 rerun.', cex = 0.72)
  })
}

build_path_diagrams <- function() {
  core <- list(PE = c(0.08, 0.82), EE = c(0.08, 0.60), SI = c(0.08, 0.38), FC = c(0.08, 0.16), ATT = c(0.42, 0.58), BI = c(0.70, 0.58), UB = c(0.95, 0.42))
  trust <- list(PE = c(0.08, 0.78), EE = c(0.08, 0.52), SI = c(0.08, 0.26), TRU = c(0.42, 0.60), BI = c(0.70, 0.48), UB = c(0.95, 0.48))
  draw_path_diagram('paper_a_core7_att_mediation', 'figure_2_core7_att_mediation_path_diagram_20260615', 'Core7 ATT mediation complete-case MASEM', core)
  draw_path_diagram('paper_a_trust6_mechanism', 'figure_3_trust6_mechanism_path_diagram_20260615', 'Trust6 mechanism complete-case MASEM', trust)
}

build_heatmap()
build_path_diagrams()
writeLines(c(
  '# Paper A researcher-approved S048 figures',
  '',
  'Date: 2026-06-15',
  '',
  'Generated from the researcher-approved S048 model-family MASEM rerun.',
  '',
  '## Files',
  '',
  '- `figure_1_full10_pairwise_pooled_heatmap_20260615.png` / `.svg`',
  '- `figure_2_core7_att_mediation_path_diagram_20260615.png` / `.svg`',
  '- `figure_3_trust6_mechanism_path_diagram_20260615.png` / `.svg`',
  '',
  '## Interpretation boundary',
  '',
  'The full10 heatmap is an evidence-map figure, not a full10 SEM result. Core7 and trust6 path diagrams are complete-case model-family MASEM results.'
), file.path(out_dir, 'PAPER_A_RESEARCHER_APPROVED_S048_FIGURES_20260615.md'))
if (dir.exists(onedrive_dir)) unlink(onedrive_dir, recursive = TRUE)
dir.create(dirname(onedrive_dir), recursive = TRUE, showWarnings = FALSE)
file.copy(out_dir, dirname(onedrive_dir), recursive = TRUE)
cat('out_dir=', out_dir, '\n', sep = '')
cat('onedrive_dir=', onedrive_dir, '\n', sep = '')
