# ==============================================================================
# 09_publication_bias.R — Publication Bias Analysis
# AI Adoption MASEM Dissertation
# ==============================================================================
# Purpose: Comprehensive publication bias assessment for key correlations
#   1. Funnel plots
#   2. Egger's regression test
#   3. Trim-and-fill
#   4. PET-PEESE
#   5. Vevea & Hedges selection model
#   6. Sensitivity analysis (svalue from PublicationBias)
# Dependencies: 00_setup.R, heterogeneity_results.rds (from 08)
# Output: publication_bias_results.rds, funnel plots, summary table
# ==============================================================================

source("analysis/R/00_setup.R")
message("\n", strrep("=", 70))
message("09: PUBLICATION BIAS ANALYSIS")
message(strrep("=", 70))

# ==============================================================================
# 1. LOAD HETEROGENEITY RESULTS
# ==============================================================================
message("\n--- Loading heterogeneity results ---")
het_results <- readRDS(file.path(PATHS$output, "heterogeneity_results.rds"))

het_table <- het_results$heterogeneity_table
pair_data <- het_results$pair_data
ma_models <- het_results$ma_models

message(sprintf("  Available MA models: %d", length(ma_models)))

# ==============================================================================
# 2. SELECT KEY CORRELATIONS FOR BIAS ANALYSIS
# ==============================================================================
message("\n--- Selecting key correlations for bias analysis ---")

# Select top pairs by: (a) theoretical importance, (b) number of studies (k)
# Target: 10-15 most frequently reported correlations

# Theoretically important pairs (from model paths)
theory_pairs <- c(
  "PE-BI", "EE-BI", "SI-BI", "FC-UB", "BI-UB",
  "ATT-BI", "PE-ATT", "EE-ATT",
  "TRU-BI", "ANX-BI", "TRA-TRU", "SE-EE",
  "PE-EE", "PE-UB", "SI-BI"
)

# Also include top-k pairs
sorted_by_k <- het_table[order(-het_table$k), ]
top_k_pairs <- head(sorted_by_k$Pair, 15)

# Union of theory + top-k, limited to those with MA models
selected_pairs <- unique(c(theory_pairs, top_k_pairs))
selected_pairs <- selected_pairs[selected_pairs %in% names(ma_models)]
selected_pairs <- head(selected_pairs, 15)  # Cap at 15

message(sprintf("  Selected %d pairs for bias analysis:", length(selected_pairs)))
for (sp in selected_pairs) {
  k <- het_table$k[het_table$Pair == sp]
  r <- het_table$Pooled_r[het_table$Pair == sp]
  message(sprintf("    %s (k=%d, r=%.3f)", sp, k, r))
}

# ==============================================================================
# 3. RUN BIAS ANALYSES FOR EACH SELECTED PAIR
# ==============================================================================
message("\n--- Running publication bias analyses ---")

bias_results <- list()
bias_summary <- data.frame(
  Pair = character(),
  k = integer(),
  Pooled_r = numeric(),
  Egger_z = numeric(),
  Egger_p = numeric(),
  Egger_sig = logical(),
  TF_r_adj = numeric(),
  TF_k_added = integer(),
  TF_side = character(),
  PET_est = numeric(),
  PET_p = numeric(),
  PEESE_est = numeric(),
  PEESE_p = numeric(),
  PET_PEESE_final = numeric(),
  Selection_est = numeric(),
  Selection_p = numeric(),
  Svalue = numeric(),
  Bias_flag = logical(),
  stringsAsFactors = FALSE
)

for (pair in selected_pairs) {
  message(sprintf("\n  --- %s ---", pair))

  pd <- pair_data[[pair]]
  rma_fit <- ma_models[[pair]]

  if (is.null(rma_fit) || pd$k < 5) {
    message(sprintf("    Skipping: insufficient data (k=%d)", pd$k))
    next
  }

  result <- list(pair = pair, k = pd$k)

  # Fisher's z values and variances
  zi <- atanh(pd$r)
  vi <- 1 / (pd$n - 3)
  sei <- sqrt(vi)

  # ----- 3a. FUNNEL PLOT -----
  tryCatch({
    png(file.path(PATHS$figures, paste0("funnel_", gsub("-", "_", pair), ".png")),
        width = 8, height = 6, units = "in", res = 300)
    funnel(rma_fit,
           main = paste("Funnel Plot:", pair),
           xlab = "Fisher's z",
           back = "white",
           shade = c("white", "grey85", "grey75"),
           level = c(95, 99, 99.9),
           refline = coef(rma_fit))
    dev.off()
    message("    Funnel plot saved")
  }, error = function(e) {
    message(sprintf("    Funnel plot failed: %s", e$message))
    try(dev.off(), silent = TRUE)
  })

  # ----- 3b. EGGER'S REGRESSION TEST -----
  egger_z <- egger_p <- NA
  tryCatch({
    egger <- regtest(rma_fit, model = "lm", predictor = "sei")
    egger_z <- egger$zval
    egger_p <- egger$pval
    result$egger <- egger
    message(sprintf("    Egger's test: z = %.3f, p = %.4f %s",
                    egger_z, egger_p, ifelse(egger_p < .05, "*", "")))
  }, error = function(e) {
    message(sprintf("    Egger's test failed: %s", e$message))
  })

  # ----- 3c. TRIM-AND-FILL -----
  tf_r_adj <- NA; tf_k_added <- 0; tf_side <- "NA"
  tryCatch({
    tf <- trimfill(rma_fit)
    tf_z_adj <- as.numeric(tf$beta)
    tf_r_adj <- tanh(tf_z_adj)
    tf_k_added <- tf$k0
    tf_side <- tf$side
    result$trimfill <- tf
    message(sprintf("    Trim-and-fill: r_adj = %.3f (r_orig = %.3f), %d studies imputed (%s)",
                    tf_r_adj, tanh(as.numeric(rma_fit$beta)), tf_k_added, tf_side))

    # Save trimfill funnel plot
    png(file.path(PATHS$figures, paste0("funnel_tf_", gsub("-", "_", pair), ".png")),
        width = 8, height = 6, units = "in", res = 300)
    funnel(tf, main = paste("Trim-and-Fill:", pair),
           xlab = "Fisher's z", back = "white")
    dev.off()

  }, error = function(e) {
    message(sprintf("    Trim-and-fill failed: %s", e$message))
    try(dev.off(), silent = TRUE)
  })

  # ----- 3d. PET-PEESE -----
  pet_est <- pet_p <- peese_est <- peese_p <- pet_peese_final <- NA
  tryCatch({
    # PET: regress effect size on SE (precision-effect test)
    pet_model <- rma(yi = zi, vi = vi, mods = ~ sei, method = "REML")
    pet_est <- tanh(as.numeric(pet_model$beta[1]))  # intercept = bias-corrected estimate
    pet_p <- pet_model$pval[1]

    # PEESE: regress effect size on variance (if PET is significant)
    peese_model <- rma(yi = zi, vi = vi, mods = ~ vi, method = "REML")
    peese_est <- tanh(as.numeric(peese_model$beta[1]))
    peese_p <- peese_model$pval[1]

    # Decision rule: if PET intercept is significant, use PEESE; otherwise use PET
    if (pet_p < .05) {
      pet_peese_final <- peese_est
      message(sprintf("    PET-PEESE: PET sig (p=%.4f) -> PEESE est = %.3f",
                      pet_p, peese_est))
    } else {
      pet_peese_final <- pet_est
      message(sprintf("    PET-PEESE: PET n.s. (p=%.4f) -> PET est = %.3f",
                      pet_p, pet_est))
    }

    result$pet <- pet_model
    result$peese <- peese_model

  }, error = function(e) {
    message(sprintf("    PET-PEESE failed: %s", e$message))
  })

  # ----- 3e. VEVEA & HEDGES SELECTION MODEL -----
  selection_est <- selection_p <- NA
  tryCatch({
    # Step function selection model with moderate one-tailed selection
    # Weight function: studies with p > .05 have lower probability of publication
    sel_model <- weightfunct(
      effect = zi,
      v = vi,
      steps = c(0.025, 1),  # Two-tailed .05 threshold
      table = TRUE
    )

    # The adjusted estimate is in the output
    selection_z <- sel_model[[1]]$par[1]
    selection_est <- tanh(selection_z)

    # Likelihood ratio test for selection
    lr_stat <- sel_model[[1]]$lrt
    selection_p <- sel_model[[1]]$p_lrt

    result$selection_model <- sel_model
    message(sprintf("    Selection model: r_adj = %.3f, LRT p = %.4f %s",
                    selection_est, selection_p,
                    ifelse(selection_p < .05, "* (selection detected)", "")))

  }, error = function(e) {
    message(sprintf("    Selection model failed: %s", e$message))
  })

  # ----- 3f. SENSITIVITY ANALYSIS (PublicationBias) -----
  svalue <- NA
  tryCatch({
    # Svalue: how strong must publication bias be to nullify the result?
    # Higher svalue = more robust to publication bias
    # Uses Mathur & VanderWeele (2020) method

    # Need to specify the threshold for "meaningful effect"
    q_threshold <- 0.10  # Effects below r = 0.10 considered negligible

    sens <- PublicationBias::pubbias_svalue(
      yi = zi,
      vi = vi,
      q = atanh(q_threshold),  # threshold in z metric
      model_type = "robust",
      favor.positive = TRUE
    )

    svalue <- sens$sval_est
    result$svalue_analysis <- sens
    message(sprintf("    S-value = %.2f (bias must be %.1fx to nullify; %s)",
                    svalue, svalue,
                    ifelse(svalue > 2, "ROBUST", "VULNERABLE")))

  }, error = function(e) {
    message(sprintf("    S-value analysis failed: %s", e$message))
    # Try alternative: just the significance test
    tryCatch({
      sens2 <- PublicationBias::pubbias_svalue(
        yi = zi, vi = vi,
        q = 0, model_type = "fixed",
        favor.positive = TRUE
      )
      svalue <- sens2$sval_est
      result$svalue_analysis <- sens2
      message(sprintf("    S-value (fixed model) = %.2f", svalue))
    }, error = function(e2) {
      message(sprintf("    S-value fallback also failed: %s", e2$message))
    })
  })

  # ----- STORE RESULTS -----
  # Flag as potentially biased if 2+ indicators suggest bias
  bias_indicators <- sum(c(
    !is.na(egger_p) && egger_p < .05,
    tf_k_added > 0,
    !is.na(selection_p) && selection_p < .05,
    !is.na(svalue) && svalue < 2
  ), na.rm = TRUE)
  bias_flag <- bias_indicators >= 2

  result$bias_flag <- bias_flag
  bias_results[[pair]] <- result

  row <- data.frame(
    Pair = pair,
    k = pd$k,
    Pooled_r = round(tanh(as.numeric(rma_fit$beta)), 4),
    Egger_z = round(egger_z, 3),
    Egger_p = round(egger_p, 4),
    Egger_sig = !is.na(egger_p) && egger_p < .05,
    TF_r_adj = round(tf_r_adj, 4),
    TF_k_added = tf_k_added,
    TF_side = tf_side,
    PET_est = round(pet_est, 4),
    PET_p = round(pet_p, 4),
    PEESE_est = round(peese_est, 4),
    PEESE_p = round(peese_p, 4),
    PET_PEESE_final = round(pet_peese_final, 4),
    Selection_est = round(selection_est, 4),
    Selection_p = round(selection_p, 4),
    Svalue = round(svalue, 2),
    Bias_flag = bias_flag,
    stringsAsFactors = FALSE
  )

  bias_summary <- rbind(bias_summary, row)
}

# ==============================================================================
# 4. SUMMARY TABLE
# ==============================================================================
message("\n\n", strrep("-", 70))
message("PUBLICATION BIAS SUMMARY")
message(strrep("-", 70))

if (nrow(bias_summary) > 0) {
  # Print concise summary
  message(sprintf("\n  Pairs analyzed: %d", nrow(bias_summary)))
  message(sprintf("  Pairs flagged for potential bias: %d (%.0f%%)",
                  sum(bias_summary$Bias_flag),
                  100 * sum(bias_summary$Bias_flag) / nrow(bias_summary)))

  # Egger's test summary
  egger_sig <- sum(bias_summary$Egger_sig, na.rm = TRUE)
  message(sprintf("\n  Egger's test significant: %d / %d",
                  egger_sig, sum(!is.na(bias_summary$Egger_sig))))

  # Trim-and-fill summary
  tf_imputed <- sum(bias_summary$TF_k_added > 0, na.rm = TRUE)
  message(sprintf("  Trim-and-fill imputed studies: %d / %d pairs",
                  tf_imputed, nrow(bias_summary)))

  # Mean shift from original to adjusted
  valid_tf <- !is.na(bias_summary$TF_r_adj) & !is.na(bias_summary$Pooled_r)
  if (any(valid_tf)) {
    mean_shift <- mean(abs(bias_summary$TF_r_adj[valid_tf] - bias_summary$Pooled_r[valid_tf]))
    message(sprintf("  Mean |r_adj - r_orig| (trim-fill): %.4f", mean_shift))
  }

  # Flagged pairs
  if (sum(bias_summary$Bias_flag) > 0) {
    flagged <- bias_summary[bias_summary$Bias_flag, ]
    message("\n  FLAGGED PAIRS (2+ bias indicators):")
    for (i in seq_len(nrow(flagged))) {
      message(sprintf("    %s: r=%.3f, TF_adj=%.3f, Egger p=%.3f, S-val=%.2f",
                      flagged$Pair[i], flagged$Pooled_r[i],
                      flagged$TF_r_adj[i], flagged$Egger_p[i],
                      flagged$Svalue[i]))
    }
  }

  # Display full table
  message("\n  Full Summary Table:")
  print(bias_summary[, c("Pair", "k", "Pooled_r", "Egger_p", "TF_r_adj",
                          "TF_k_added", "PET_PEESE_final", "Selection_est",
                          "Svalue", "Bias_flag")],
        row.names = FALSE)
}

# ==============================================================================
# 5. COMBINED FUNNEL PLOT (GRID)
# ==============================================================================
message("\n--- Creating combined funnel plot grid ---")

tryCatch({
  n_plots <- min(length(selected_pairs), 12)
  plot_pairs <- selected_pairs[1:n_plots]

  ncol_plot <- ceiling(sqrt(n_plots))
  nrow_plot <- ceiling(n_plots / ncol_plot)

  png(file.path(PATHS$figures, "funnel_plots_combined.png"),
      width = 4 * ncol_plot, height = 3.5 * nrow_plot, units = "in", res = 300)
  par(mfrow = c(nrow_plot, ncol_plot), mar = c(4, 4, 3, 1))

  for (pair in plot_pairs) {
    if (pair %in% names(ma_models)) {
      funnel(ma_models[[pair]],
             main = pair,
             xlab = "Fisher's z",
             cex.main = 1.0,
             back = "white")
    }
  }

  dev.off()
  message("  Saved combined funnel plot grid")

}, error = function(e) {
  message(sprintf("  Combined funnel plot failed: %s", e$message))
  try(dev.off(), silent = TRUE)
})

# ==============================================================================
# 6. BIAS-ADJUSTED VS ORIGINAL COMPARISON PLOT
# ==============================================================================
message("\n--- Creating bias-adjusted comparison plot ---")

if (nrow(bias_summary) > 0) {
  comp_data <- bias_summary %>%
    filter(!is.na(TF_r_adj)) %>%
    select(Pair, Pooled_r, TF_r_adj, PET_PEESE_final, Bias_flag) %>%
    tidyr::pivot_longer(cols = c(Pooled_r, TF_r_adj, PET_PEESE_final),
                        names_to = "Method", values_to = "Estimate") %>%
    mutate(Method = recode(Method,
                           "Pooled_r" = "Original",
                           "TF_r_adj" = "Trim-and-Fill",
                           "PET_PEESE_final" = "PET-PEESE"))

  p_comp <- ggplot(comp_data, aes(x = Pair, y = Estimate, color = Method, shape = Method)) +
    geom_point(size = 3, position = position_dodge(0.4)) +
    scale_color_manual(values = c("Original" = "black", "Trim-and-Fill" = "#D6604D",
                                  "PET-PEESE" = "#4393C3")) +
    scale_shape_manual(values = c("Original" = 16, "Trim-and-Fill" = 17, "PET-PEESE" = 15)) +
    labs(
      title = "Original vs Bias-Adjusted Effect Sizes",
      x = "Construct Pair", y = "Pooled Correlation (r)"
    ) +
    theme_minimal(base_size = 11) +
    theme(
      axis.text.x = element_text(angle = 45, hjust = 1),
      plot.title = element_text(face = "bold"),
      legend.position = "bottom"
    ) +
    geom_hline(yintercept = 0, linetype = "dashed", color = "grey60")

  ggsave(file.path(PATHS$figures, "publication_bias_comparison.png"),
         p_comp, width = 12, height = 7, dpi = 300)
  ggsave(file.path(PATHS$figures, "publication_bias_comparison.pdf"),
         p_comp, width = 12, height = 7)
  message("  Saved bias-adjusted comparison plot")
}

# ==============================================================================
# 7. SAVE ALL RESULTS
# ==============================================================================
message("\n--- Saving publication bias results ---")

pub_bias_output <- list(
  bias_summary_table = bias_summary,
  bias_results = bias_results,
  selected_pairs = selected_pairs,
  n_flagged = sum(bias_summary$Bias_flag, na.rm = TRUE),
  flagged_pairs = bias_summary$Pair[bias_summary$Bias_flag],
  overall_assessment = ifelse(
    sum(bias_summary$Bias_flag, na.rm = TRUE) / nrow(bias_summary) < 0.25,
    "MINIMAL CONCERN: <25% of pairs flagged for publication bias",
    "MODERATE CONCERN: >=25% of pairs flagged for publication bias"
  )
)

saveRDS(pub_bias_output, file.path(PATHS$output, "publication_bias_results.rds"))
message(sprintf("  Saved to: %s", file.path(PATHS$output, "publication_bias_results.rds")))

write.csv(bias_summary,
          file.path(PATHS$output, "publication_bias_table.csv"),
          row.names = FALSE)
message(sprintf("  Table saved to: %s", file.path(PATHS$output, "publication_bias_table.csv")))

message(sprintf("\n  Overall assessment: %s", pub_bias_output$overall_assessment))

message("\n", strrep("=", 70))
message("09: PUBLICATION BIAS ANALYSIS COMPLETE")
message(strrep("=", 70))
