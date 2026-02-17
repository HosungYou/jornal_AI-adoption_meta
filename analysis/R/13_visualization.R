# ==============================================================================
# 13_visualization.R — Comprehensive Visualization Suite
# Educational AI Adoption MASEM Meta-Analysis
# ==============================================================================
# Purpose: Generate all publication-quality figures for the meta-analysis
#   1.  Path diagrams for 3 competing models (semPlot)
#   2.  Forest plots for top correlations (metafor)
#   3.  Funnel plots (from publication bias)
#   4.  Bayesian posterior distribution plots (prior overlay)
#   5.  Network graph (qgraph)
#   6.  Centrality plot (qgraph)
#   7.  Model comparison bar chart (CFI, RMSEA)
#   8.  Heterogeneity heatmap (I-squared)
#   9.  Temporal comparison plot (pre vs post ChatGPT)
#   10. Correlation matrix heatmap (pooled)
#   All saved as PNG (300 DPI) and PDF
# Dependencies: 00_setup.R, all prior output .rds files
# Output: All figures in PATHS$figures
# ==============================================================================

source("analysis/R/00_setup.R")
library(patchwork)

message("\n", strrep("=", 70))
message("13: COMPREHENSIVE VISUALIZATION SUITE (EDUCATIONAL AI)")
message(strrep("=", 70))

# ==============================================================================
# 0. LOAD ALL RESULTS
# ==============================================================================
message("\n--- Loading all analysis results ---")

# Stage 1
stage1 <- tryCatch(readRDS(file.path(PATHS$pooled, "stage1_results.rds")),
                   error = function(e) { message("  stage1_results not found"); NULL })

# TSSEM models
tssem <- tryCatch(readRDS(file.path(PATHS$output, "tssem_results.rds")),
                  error = function(e) { message("  tssem_results not found"); NULL })

# Heterogeneity
het <- tryCatch(readRDS(file.path(PATHS$output, "heterogeneity_results.rds")),
                error = function(e) { message("  heterogeneity_results not found"); NULL })

# Publication bias
pubbias <- tryCatch(readRDS(file.path(PATHS$output, "publication_bias_results.rds")),
                    error = function(e) { message("  publication_bias_results not found"); NULL })

# Temporal
temporal <- tryCatch(readRDS(file.path(PATHS$output, "temporal_analysis_results.rds")),
                     error = function(e) { message("  temporal_analysis_results not found"); NULL })

# Bayesian
bayesian <- tryCatch(readRDS(file.path(PATHS$output, "bayesian_masem_results.rds")),
                     error = function(e) { message("  bayesian_masem_results not found"); NULL })

# Network
network <- tryCatch(readRDS(file.path(PATHS$output, "network_results.rds")),
                    error = function(e) { message("  network_results not found"); NULL })

# Sensitivity
sensitivity <- tryCatch(readRDS(file.path(PATHS$output, "sensitivity_results.rds")),
                        error = function(e) { message("  sensitivity_results not found"); NULL })

message("  Results loading complete")

# Helper: save plot in both PNG and PDF
save_plot <- function(plot_obj, filename, width = 10, height = 8) {
  png_path <- file.path(PATHS$figures, paste0(filename, ".png"))
  pdf_path <- file.path(PATHS$figures, paste0(filename, ".pdf"))
  tryCatch({
    ggsave(png_path, plot_obj, width = width, height = height, dpi = 300)
    ggsave(pdf_path, plot_obj, width = width, height = height)
    message(sprintf("  Saved: %s (.png + .pdf)", filename))
  }, error = function(e) {
    message(sprintf("  FAILED: %s — %s", filename, e$message))
  })
}

# Helper: save base R plot in both formats
save_base_plot <- function(plot_fn, filename, width = 10, height = 8) {
  png_path <- file.path(PATHS$figures, paste0(filename, ".png"))
  pdf_path <- file.path(PATHS$figures, paste0(filename, ".pdf"))
  tryCatch({
    png(png_path, width = width, height = height, units = "in", res = 300)
    plot_fn()
    dev.off()
    pdf(pdf_path, width = width, height = height)
    plot_fn()
    dev.off()
    message(sprintf("  Saved: %s (.png + .pdf)", filename))
  }, error = function(e) {
    message(sprintf("  FAILED: %s — %s", filename, e$message))
    try(dev.off(), silent = TRUE)
  })
}

# ==============================================================================
# 1. PATH DIAGRAMS FOR COMPETING MODELS
# ==============================================================================
message("\n--- 1. Path Diagrams (semPlot) ---")

if (!is.null(tssem)) {
  # Define lavaan syntax for each model to render with semPaths
  # Model 1: UTAUT Core
  model1_lav <- '
    BI ~ PE + EE + SI
    UB ~ BI + FC
  '

  # Model 2: Integrated (UTAUT + AI-specific)
  model2_lav <- '
    BI ~ PE + EE + SI + ATT + TRU + ANX
    UB ~ BI + FC
    ATT ~ PE + EE
    TRU ~ TRA
    EE ~ SE
    ANX ~ AUT + SE
  '

  # Model 3: Parsimonious
  model3_lav <- '
    BI ~ PE + EE + SI + ATT + TRU
    UB ~ BI + FC
    ATT ~ PE + EE
    TRU ~ TRA
  '

  model_specs <- list(
    list(syntax = model1_lav, name = "Model 1: UTAUT Core", file = "path_model1_utaut"),
    list(syntax = model2_lav, name = "Model 2: Integrated", file = "path_model2_integrated"),
    list(syntax = model3_lav, name = "Model 3: Parsimonious", file = "path_model3_parsimonious")
  )

  for (ms in model_specs) {
    tryCatch({
      # Use simulated data to fit lavaan model for visualization only
      if (!is.null(stage1)) {
        set.seed(42)
        sim_data <- MASS::mvrnorm(n = round(stage1$harmonic_n),
                                   mu = rep(0, N_CONSTRUCTS),
                                   Sigma = stage1$pooled_matrix)
        sim_data <- as.data.frame(sim_data)
        colnames(sim_data) <- CONSTRUCTS

        lav_fit <- sem(ms$syntax, data = sim_data, std.lv = TRUE)

        save_base_plot(function() {
          semPaths(
            lav_fit,
            what = "std",
            whatLabels = "std",
            layout = "tree2",
            style = "lisrel",
            nCharNodes = 4,
            sizeMan = 8,
            sizeLat = 10,
            edge.label.cex = 0.8,
            residuals = FALSE,
            intercepts = FALSE,
            thresholds = FALSE,
            curvePivot = TRUE,
            fade = FALSE,
            posCol = "#2166AC",
            negCol = "#B2182B",
            edge.width = 1.5,
            title = TRUE,
            mar = c(3, 3, 5, 3)
          )
          title(ms$name, line = 2, cex.main = 1.3, font.main = 2)
        }, ms$file, width = 12, height = 9)
      }
    }, error = function(e) {
      message(sprintf("  Path diagram failed for %s: %s", ms$name, e$message))
    })
  }
} else {
  message("  Skipped: TSSEM results not available")
}

# ==============================================================================
# 2. FOREST PLOTS FOR TOP CORRELATIONS
# ==============================================================================
message("\n--- 2. Forest Plots ---")

if (!is.null(het)) {
  # Select top 10 most frequently reported correlations
  het_table <- het$heterogeneity_table
  top_pairs <- head(het_table[order(-het_table$k), ], 10)

  for (i in seq_len(nrow(top_pairs))) {
    pair <- top_pairs$Pair[i]
    rma_model <- het$ma_models[[pair]]

    if (is.null(rma_model)) next

    filename <- paste0("forest_", gsub("-", "_", pair))

    tryCatch({
      save_base_plot(function() {
        forest(
          rma_model,
          main = paste("Forest Plot:", pair),
          xlab = "Fisher's z (correlation)",
          cex = 0.7,
          header = TRUE,
          mlab = sprintf("RE Model (I2=%.1f%%, tau2=%.4f)",
                         rma_model$I2, rma_model$tau2),
          col = "#2166AC",
          border = "#2166AC"
        )
      }, filename, width = 10, height = max(6, 0.4 * rma_model$k + 3))
    }, error = function(e) {
      message(sprintf("  Forest plot failed for %s: %s", pair, e$message))
    })
  }

  message(sprintf("  Generated %d forest plots", min(nrow(top_pairs), 10)))
} else {
  message("  Skipped: heterogeneity results not available")
}

# ==============================================================================
# 3. FUNNEL PLOTS (KEY CORRELATIONS)
# ==============================================================================
message("\n--- 3. Funnel Plots ---")

if (!is.null(pubbias) && !is.null(het)) {
  selected <- pubbias$selected_pairs

  for (pair in selected[1:min(6, length(selected))]) {
    rma_model <- het$ma_models[[pair]]
    if (is.null(rma_model)) next

    filename <- paste0("funnel_", gsub("-", "_", pair))

    tryCatch({
      save_base_plot(function() {
        funnel(rma_model,
               main = paste("Funnel Plot:", pair),
               xlab = "Fisher's z",
               back = "white",
               shade = c("white", "grey90", "grey80"),
               level = c(90, 95, 99),
               refline = coef(rma_model),
               pch = 19, col = "#2166AC")
      }, filename, width = 8, height = 6)
    }, error = function(e) {
      message(sprintf("  Funnel plot failed for %s: %s", pair, e$message))
    })
  }
} else {
  message("  Skipped: publication bias or heterogeneity results not available")
}

# ==============================================================================
# 4. BAYESIAN POSTERIOR DISTRIBUTIONS (WITH PRIOR OVERLAY)
# ==============================================================================
message("\n--- 4. Bayesian Posterior Distributions ---")

if (!is.null(bayesian) && !is.null(bayesian$model_informed)) {
  tryCatch({
    draws <- blavInspect(bayesian$model_informed, "mcmc")
    if (is.list(draws)) {
      draws_mat <- do.call(rbind, draws)
    } else {
      draws_mat <- as.matrix(draws)
    }

    traditional_paths <- c("PE_BI", "EE_BI", "SI_BI", "ATT_BI",
                           "BI_UB", "FC_UB", "PE_ATT", "EE_ATT")

    plot_list <- list()
    for (path in traditional_paths) {
      prior_info <- bayesian$sabherwal_priors[[path]]
      if (is.null(prior_info)) next

      # Find column in draws
      col_idx <- grep(path, colnames(draws_mat), fixed = TRUE)
      if (length(col_idx) == 0) {
        parts <- strsplit(path, "_")[[1]]
        pattern <- paste0(parts[2], "~", parts[1])
        col_idx <- grep(pattern, colnames(draws_mat), fixed = TRUE)
      }
      if (length(col_idx) == 0) next

      post_draws <- draws_mat[, col_idx[1]]
      post_df <- data.frame(value = post_draws)

      x_range <- seq(min(post_draws) - 0.3, max(post_draws) + 0.3, length.out = 300)
      prior_df <- data.frame(x = x_range,
                              y = dnorm(x_range, prior_info$mean, prior_info$sd))

      shift <- mean(post_draws) - prior_info$mean

      p <- ggplot() +
        geom_density(data = post_df, aes(x = value),
                     fill = "#4393C3", alpha = 0.4, color = "#2166AC", linewidth = 0.8) +
        geom_line(data = prior_df, aes(x = x, y = y),
                  color = "#B2182B", linewidth = 1.2, linetype = "dashed") +
        geom_vline(xintercept = prior_info$mean, color = "#B2182B",
                   linewidth = 0.7, linetype = "dotted") +
        geom_vline(xintercept = mean(post_draws), color = "#2166AC",
                   linewidth = 0.7) +
        annotate("text", x = prior_info$mean, y = Inf, label = "Sabherwal",
                 vjust = 2, hjust = 1.1, color = "#B2182B", size = 3, fontface = "italic") +
        annotate("text", x = mean(post_draws), y = Inf, label = "AI Posterior",
                 vjust = 2, hjust = -0.1, color = "#2166AC", size = 3, fontface = "italic") +
        labs(
          title = path,
          subtitle = sprintf("Prior: N(%.2f, %.2f) | Post: %.3f | Shift: %+.3f",
                             prior_info$mean, prior_info$sd,
                             mean(post_draws), shift),
          x = "Coefficient", y = "Density"
        ) +
        theme_minimal(base_size = 10) +
        theme(plot.title = element_text(face = "bold", size = 11))

      plot_list[[path]] <- p
    }

    if (length(plot_list) > 0) {
      combined <- wrap_plots(plot_list, ncol = 2) +
        plot_annotation(
          title = "Educational AI: Bayesian Prior-to-Posterior Shift (General IT vs Educational AI)",
          theme = theme(plot.title = element_text(face = "bold", size = 14, hjust = 0.5))
        )

      save_plot(combined, "bayesian_prior_posterior_combined",
                width = 14, height = ceiling(length(plot_list) / 2) * 4)
    }

  }, error = function(e) {
    message(sprintf("  Bayesian posterior plots failed: %s", e$message))
  })
} else {
  message("  Skipped: Bayesian results not available")
}

# ==============================================================================
# 5. NETWORK GRAPH
# ==============================================================================
message("\n--- 5. Network Graph ---")

if (!is.null(network) && !is.null(network$omega_matrix)) {
  omega <- network$omega_matrix

  node_groups <- list(
    "TAM/UTAUT" = c("PE", "EE", "SI", "FC"),
    "AI-Specific" = c("TRU", "ANX", "TRA", "AUT"),
    "Mediator/Outcome" = c("BI", "UB", "ATT", "SE")
  )

  group_colors <- c("TAM/UTAUT" = "#3288BD",
                    "AI-Specific" = "#D53E4F",
                    "Mediator/Outcome" = "#66C2A5")

  strength <- colSums(abs(omega))
  node_sizes <- 5 + 7 * (strength - min(strength)) / (max(strength) - min(strength) + 0.01)

  save_base_plot(function() {
    qgraph(
      omega,
      layout = "spring",
      labels = CONSTRUCTS,
      nodeNames = CONSTRUCT_LABELS,
      groups = as.list(node_groups),
      color = group_colors,
      vsize = node_sizes,
      esize = 10,
      edge.width = 1.5,
      maximum = max(abs(omega[omega != 0])),
      cut = 0,
      borders = TRUE,
      border.width = 1.5,
      posCol = "#2166AC",
      negCol = "#B2182B",
      negDashed = TRUE,
      title = "Educational AI Adoption Meta-Analytic Network (MAGNA)",
      legend = TRUE,
      legend.cex = 0.55,
      mar = c(5, 5, 6, 5)
    )
  }, "network_main_publication", width = 12, height = 11)
} else {
  message("  Skipped: network results not available")
}

# ==============================================================================
# 6. CENTRALITY PLOT
# ==============================================================================
message("\n--- 6. Centrality Plot ---")

if (!is.null(network) && !is.null(network$omega_matrix)) {
  save_base_plot(function() {
    centralityPlot(
      network$omega_matrix,
      include = c("Strength", "Betweenness", "Closeness", "ExpectedInfluence"),
      orderBy = "Strength",
      scale = "z-scores"
    )
  }, "network_centrality_publication", width = 10, height = 8)
} else {
  message("  Skipped: network results not available")
}

# ==============================================================================
# 7. MODEL COMPARISON BAR CHART
# ==============================================================================
message("\n--- 7. Model Comparison Chart ---")

if (!is.null(tssem)) {
  # Extract fit indices for all models
  model_names <- c()
  cfi_vals <- c()
  tli_vals <- c()
  rmsea_vals <- c()
  srmr_vals <- c()
  aic_vals <- c()

  for (mn in c("utaut_core", "integrated", "parsimonious")) {
    label <- switch(mn,
                    utaut_core = "UTAUT Core",
                    integrated = "Integrated",
                    parsimonious = "Parsimonious")

    if (!is.null(tssem[[mn]]$summary)) {
      s <- tssem[[mn]]$summary
      model_names <- c(model_names, label)
      cfi_vals <- c(cfi_vals, s$stat$CFI)
      tli_vals <- c(tli_vals, s$stat$TLI)
      rmsea_vals <- c(rmsea_vals, s$stat$RMSEA)
      srmr_vals <- c(srmr_vals, s$stat$SRMR)
      aic_vals <- c(aic_vals, s$stat$AIC)
    }
  }

  if (length(model_names) > 0) {
    fit_data <- data.frame(
      Model = rep(model_names, 4),
      Index = rep(c("CFI", "TLI", "RMSEA", "SRMR"), each = length(model_names)),
      Value = c(cfi_vals, tli_vals, rmsea_vals, srmr_vals),
      stringsAsFactors = FALSE
    )

    # Thresholds for good fit
    thresholds <- data.frame(
      Index = c("CFI", "TLI", "RMSEA", "SRMR"),
      Threshold = c(0.95, 0.95, 0.06, 0.08),
      Direction = c("above", "above", "below", "below"),
      stringsAsFactors = FALSE
    )

    fit_data$Model <- factor(fit_data$Model, levels = model_names)
    fit_data$Index <- factor(fit_data$Index, levels = c("CFI", "TLI", "RMSEA", "SRMR"))

    p_fit <- ggplot(fit_data, aes(x = Model, y = Value, fill = Model)) +
      geom_bar(stat = "identity", width = 0.6, alpha = 0.85) +
      geom_hline(data = thresholds, aes(yintercept = Threshold),
                 linetype = "dashed", color = "red", linewidth = 0.7) +
      facet_wrap(~ Index, scales = "free_y", nrow = 1) +
      scale_fill_manual(values = c("#3288BD", "#66C2A5", "#ABDDA4",
                                    "#D53E4F", "#F46D43")[1:length(model_names)]) +
      labs(
        title = "Educational AI Adoption: Model Fit Comparison",
        subtitle = "Three competing structural models | Red dashed line = threshold for good fit",
        x = "", y = "Fit Index Value"
      ) +
      theme_minimal(base_size = 12) +
      theme(
        plot.title = element_text(face = "bold", size = 14),
        legend.position = "bottom",
        strip.text = element_text(face = "bold", size = 12),
        axis.text.x = element_blank(),
        axis.ticks.x = element_blank()
      )

    save_plot(p_fit, "model_comparison_fit_indices", width = 14, height = 6)

    # AIC comparison (separate since different scale)
    if (length(aic_vals) > 0) {
      aic_data <- data.frame(
        Model = factor(model_names, levels = model_names),
        AIC = aic_vals,
        stringsAsFactors = FALSE
      )

      p_aic <- ggplot(aic_data, aes(x = Model, y = AIC, fill = Model)) +
        geom_bar(stat = "identity", width = 0.5, alpha = 0.85) +
        geom_text(aes(label = sprintf("%.1f", AIC)), vjust = -0.5, size = 4) +
        scale_fill_manual(values = c("#3288BD", "#66C2A5", "#ABDDA4",
                                      "#D53E4F")[1:length(model_names)]) +
        labs(
          title = "Educational AI: Model Comparison by AIC (Lower is Better)",
          x = "", y = "AIC"
        ) +
        theme_minimal(base_size = 12) +
        theme(
          plot.title = element_text(face = "bold"),
          legend.position = "none"
        )

      save_plot(p_aic, "model_comparison_aic", width = 8, height = 6)
    }
  }
} else {
  message("  Skipped: TSSEM results not available")
}

# ==============================================================================
# 8. HETEROGENEITY HEATMAP (I-SQUARED)
# ==============================================================================
message("\n--- 8. Heterogeneity Heatmap ---")

if (!is.null(het) && !is.null(het$I2_matrix)) {
  I2_matrix <- het$I2_matrix

  I2_long <- expand.grid(Var1 = CONSTRUCTS, Var2 = CONSTRUCTS,
                          stringsAsFactors = FALSE)
  I2_long$I2 <- sapply(seq_len(nrow(I2_long)), function(i) {
    I2_matrix[I2_long$Var1[i], I2_long$Var2[i]]
  })
  I2_long$Var1 <- factor(I2_long$Var1, levels = CONSTRUCTS)
  I2_long$Var2 <- factor(I2_long$Var2, levels = rev(CONSTRUCTS))

  # Mark diagonal and missing
  I2_long$is_diag <- I2_long$Var1 == I2_long$Var2
  I2_long$label <- ifelse(I2_long$is_diag, "",
                           ifelse(is.na(I2_long$I2), "---",
                                  sprintf("%.0f", I2_long$I2)))

  p_heatmap <- ggplot(I2_long, aes(x = Var1, y = Var2, fill = I2)) +
    geom_tile(color = "white", linewidth = 0.8) +
    geom_text(aes(label = label), size = 3.2, color = "black") +
    scale_fill_gradient2(
      low = "#2166AC", mid = "#FFFFBF", high = "#B2182B",
      midpoint = 50, na.value = "grey90",
      limits = c(0, 100),
      name = expression(I^2 ~ "(%)")
    ) +
    labs(
      title = expression("Educational AI: Heterogeneity Heatmap (" * I^2 * "%)"),
      subtitle = "66 pairwise correlations | Blue = low heterogeneity, Red = high heterogeneity",
      x = "", y = ""
    ) +
    theme_minimal(base_size = 12) +
    theme(
      axis.text.x = element_text(angle = 45, hjust = 1, face = "bold", size = 11),
      axis.text.y = element_text(face = "bold", size = 11),
      plot.title = element_text(face = "bold", hjust = 0.5, size = 14),
      plot.subtitle = element_text(hjust = 0.5, size = 10, color = "grey40"),
      panel.grid = element_blank(),
      legend.position = "right"
    ) +
    coord_fixed()

  save_plot(p_heatmap, "heterogeneity_heatmap_publication", width = 11, height = 10)
} else {
  message("  Skipped: heterogeneity results not available")
}

# ==============================================================================
# 9. TEMPORAL COMPARISON PLOT
# ==============================================================================
message("\n--- 9. Temporal Comparison Plot ---")

if (!is.null(temporal) && !is.null(temporal$comparison_table)) {
  comp <- temporal$comparison_table

  # Reshape for grouped bar chart
  plot_data <- comp %>%
    select(Path, Pre_Est, Post_Est, Pre_SE, Post_SE, Significant) %>%
    tidyr::pivot_longer(
      cols = c(Pre_Est, Post_Est),
      names_to = "Era",
      values_to = "Estimate"
    ) %>%
    mutate(
      Era = recode(Era, "Pre_Est" = "Pre-ChatGPT", "Post_Est" = "Post-ChatGPT"),
      SE = ifelse(Era == "Pre-ChatGPT",
                  comp$Pre_SE[match(Path, comp$Path)],
                  comp$Post_SE[match(Path, comp$Path)])
    )

  p_temporal <- ggplot(plot_data, aes(x = Path, y = Estimate, fill = Era)) +
    geom_bar(stat = "identity", position = position_dodge(0.8), width = 0.7) +
    geom_errorbar(
      aes(ymin = Estimate - 1.96 * SE, ymax = Estimate + 1.96 * SE),
      position = position_dodge(0.8), width = 0.2, linewidth = 0.5
    ) +
    scale_fill_manual(values = c("Pre-ChatGPT" = "#2166AC", "Post-ChatGPT" = "#B2182B")) +
    # Add significance stars
    geom_text(
      data = comp[comp$Significant, ],
      aes(x = Path, y = pmax(Pre_Est, Post_Est) + 0.08, label = "*"),
      inherit.aes = FALSE, size = 8, color = "red", fontface = "bold"
    ) +
    labs(
      title = "Educational AI: Pre vs Post ChatGPT Path Coefficients",
      subtitle = sprintf("Pre-ChatGPT (k=%d) vs Post-ChatGPT (k=%d) | * = p < .05 Wald test",
                         temporal$n_pre, temporal$n_post),
      x = "Structural Path", y = "Standardized Path Coefficient",
      fill = "Era"
    ) +
    theme_minimal(base_size = 12) +
    theme(
      axis.text.x = element_text(angle = 45, hjust = 1, face = "bold"),
      plot.title = element_text(face = "bold", size = 14),
      legend.position = "bottom"
    ) +
    geom_hline(yintercept = 0, linetype = "dashed", color = "grey50")

  save_plot(p_temporal, "temporal_comparison_publication", width = 13, height = 7)
} else {
  message("  Skipped: temporal results not available")
}

# ==============================================================================
# 10. POOLED CORRELATION MATRIX HEATMAP
# ==============================================================================
message("\n--- 10. Pooled Correlation Matrix Heatmap ---")

if (!is.null(stage1) && !is.null(stage1$pooled_matrix)) {
  pooled <- stage1$pooled_matrix

  # Build long format
  cor_long <- expand.grid(Var1 = CONSTRUCTS, Var2 = CONSTRUCTS,
                           stringsAsFactors = FALSE)
  cor_long$r <- sapply(seq_len(nrow(cor_long)), function(i) {
    pooled[cor_long$Var1[i], cor_long$Var2[i]]
  })
  cor_long$Var1 <- factor(cor_long$Var1, levels = CONSTRUCTS)
  cor_long$Var2 <- factor(cor_long$Var2, levels = rev(CONSTRUCTS))

  # Show only lower triangle + diagonal
  cor_long$show <- as.integer(cor_long$Var1) >= (N_CONSTRUCTS + 1 - as.integer(cor_long$Var2))

  cor_long$label <- ifelse(cor_long$show,
                            ifelse(cor_long$Var1 == cor_long$Var2, "1.00",
                                   sprintf("%.2f", cor_long$r)),
                            "")
  cor_long$r_display <- ifelse(cor_long$show, cor_long$r, NA)

  p_cormat <- ggplot(cor_long, aes(x = Var1, y = Var2, fill = r_display)) +
    geom_tile(color = "white", linewidth = 0.8) +
    geom_text(aes(label = label), size = 3.2, color = "black") +
    scale_fill_gradient2(
      low = "#2166AC", mid = "white", high = "#B2182B",
      midpoint = 0, na.value = "white",
      limits = c(-1, 1),
      name = "r"
    ) +
    labs(
      title = "Educational AI: Pooled Meta-Analytic Correlation Matrix",
      subtitle = sprintf("k = %d studies | Harmonic N = %.0f", stage1$n_studies, stage1$harmonic_n),
      x = "", y = ""
    ) +
    theme_minimal(base_size = 12) +
    theme(
      axis.text.x = element_text(angle = 45, hjust = 1, face = "bold", size = 11),
      axis.text.y = element_text(face = "bold", size = 11),
      plot.title = element_text(face = "bold", hjust = 0.5, size = 14),
      plot.subtitle = element_text(hjust = 0.5, color = "grey40"),
      panel.grid = element_blank(),
      legend.position = "right"
    ) +
    coord_fixed()

  save_plot(p_cormat, "pooled_correlation_heatmap", width = 11, height = 10)

  # Also save corrplot version
  save_base_plot(function() {
    corrplot(
      pooled,
      method = "color",
      type = "lower",
      addCoef.col = "black",
      number.cex = 0.7,
      tl.col = "black",
      tl.cex = 1.0,
      tl.srt = 45,
      col = colorRampPalette(c("#2166AC", "white", "#B2182B"))(200),
      title = sprintf("Educational AI: Pooled Correlation Matrix (k=%d, N=%d)",
                       stage1$n_studies, stage1$total_n),
      mar = c(0, 0, 3, 0),
      diag = FALSE
    )
  }, "pooled_correlation_corrplot", width = 10, height = 9)
} else {
  message("  Skipped: stage1 results not available")
}

# ==============================================================================
# 11. ADDITIONAL: PUBLICATION BIAS COMPARISON PLOT
# ==============================================================================
message("\n--- 11. Publication Bias Summary Plot ---")

if (!is.null(pubbias) && !is.null(pubbias$bias_summary_table)) {
  bs <- pubbias$bias_summary_table

  comp_long <- bs %>%
    select(Pair, Pooled_r, TF_r_adj, PET_PEESE_final) %>%
    filter(!is.na(TF_r_adj) | !is.na(PET_PEESE_final)) %>%
    tidyr::pivot_longer(
      cols = c(Pooled_r, TF_r_adj, PET_PEESE_final),
      names_to = "Method",
      values_to = "Estimate"
    ) %>%
    mutate(Method = recode(Method,
                           "Pooled_r" = "Original",
                           "TF_r_adj" = "Trim-and-Fill",
                           "PET_PEESE_final" = "PET-PEESE")) %>%
    filter(!is.na(Estimate))

  p_bias <- ggplot(comp_long, aes(x = reorder(Pair, Estimate), y = Estimate,
                                   color = Method, shape = Method)) +
    geom_point(size = 3.5, position = position_dodge(0.5)) +
    scale_color_manual(values = c("Original" = "black",
                                   "Trim-and-Fill" = "#D6604D",
                                   "PET-PEESE" = "#4393C3")) +
    scale_shape_manual(values = c("Original" = 16, "Trim-and-Fill" = 17, "PET-PEESE" = 15)) +
    coord_flip() +
    labs(
      title = "Educational AI: Publication Bias Assessment",
      subtitle = "Original vs Adjusted Effect Sizes",
      x = "Construct Pair", y = "Pooled Correlation (r)"
    ) +
    theme_minimal(base_size = 11) +
    theme(
      plot.title = element_text(face = "bold", size = 13),
      legend.position = "bottom"
    ) +
    geom_hline(yintercept = 0, linetype = "dashed", color = "grey60")

  save_plot(p_bias, "publication_bias_summary", width = 11, height = 8)
} else {
  message("  Skipped: publication bias results not available")
}

# ==============================================================================
# 12. ADDITIONAL: SENSITIVITY SCATTER PLOT
# ==============================================================================
message("\n--- 12. Sensitivity Analysis Plot ---")

if (!is.null(sensitivity) && !is.null(sensitivity$comparison_table)) {
  comp <- sensitivity$comparison_table

  p_sens <- ggplot(comp, aes(x = Full_Est, y = Ronly_Est)) +
    geom_point(size = 4, color = "#2166AC", alpha = 0.8) +
    geom_abline(intercept = 0, slope = 1, linetype = "dashed", color = "red",
                linewidth = 0.8) +
    ggrepel::geom_text_repel(aes(label = Path), size = 3.5, max.overlaps = 20) +
    labs(
      title = "Educational AI: Sensitivity Analysis",
      subtitle = sprintf("Full Dataset vs R-only Subset | r = %.3f | max |diff| = %.4f | %s",
                         sensitivity$decision$cor_estimates,
                         sensitivity$decision$max_abs_diff,
                         ifelse(sensitivity$decision$robust, "ROBUST", "SENSITIVE")),
      x = "Full Dataset (r + converted beta)",
      y = "R-only Subset"
    ) +
    theme_minimal(base_size = 12) +
    theme(plot.title = element_text(face = "bold", size = 14)) +
    coord_fixed()

  save_plot(p_sens, "sensitivity_scatter_publication", width = 9, height = 9)
} else {
  message("  Skipped: sensitivity results not available")
}

# ==============================================================================
# 13. COMPREHENSIVE FIGURE SUMMARY
# ==============================================================================
message("\n", strrep("-", 70))
message("FIGURE INVENTORY")
message(strrep("-", 70))

all_figures <- list.files(PATHS$figures, pattern = "\\.(png|pdf)$")
png_files <- all_figures[grepl("\\.png$", all_figures)]
pdf_files <- all_figures[grepl("\\.pdf$", all_figures)]

message(sprintf("\n  Total figures generated: %d PNG + %d PDF",
                length(png_files), length(pdf_files)))
message(sprintf("  Output directory: %s", PATHS$figures))

if (length(png_files) > 0) {
  message("\n  PNG files:")
  for (f in sort(png_files)) {
    fsize <- file.size(file.path(PATHS$figures, f))
    message(sprintf("    %s (%.1f KB)", f, fsize / 1024))
  }
}

message("\n", strrep("=", 70))
message("13: VISUALIZATION SUITE COMPLETE")
message(strrep("=", 70))
