# ==============================================================================
# 10_sensitivity.R — Sensitivity Analysis for Beta-to-r Conversion
# AI Adoption MASEM Dissertation
# ==============================================================================
# Purpose: Assess robustness of results to inclusion of converted beta coefficients
#   - Compare full dataset (r + converted beta) vs r-only subset
#   - Re-run TSSEM Stage 1 + Stage 2 on r-only data
#   - Compare path coefficients between full and r-only analyses
#   - Decision rule: |delta| < .05 and r(estimates) > .95 -> conversion robust
# Dependencies: 00_setup.R, prepared_data.rds, stage1_results.rds
# Output: sensitivity_results.rds, comparison tables
# ==============================================================================

source("analysis/R/00_setup.R")
message("\n", strrep("=", 70))
message("10: SENSITIVITY ANALYSIS — BETA-TO-R CONVERSION")
message(strrep("=", 70))

# ==============================================================================
# 1. LOAD DATA
# ==============================================================================
message("\n--- Loading data ---")
prepared <- readRDS(file.path(PATHS$pooled, "prepared_data.rds"))
stage1_full <- readRDS(file.path(PATHS$pooled, "stage1_results.rds"))

# Full dataset (r + converted beta)
full_matrices <- prepared$cor_matrices
full_n <- prepared$sample_sizes

# R-only subset
ronly_matrices <- prepared$cor_matrices_r_only
ronly_n <- prepared$sample_sizes_r_only

message(sprintf("  Full dataset:  k = %d studies, Total N = %d",
                length(full_matrices), sum(full_n)))
message(sprintf("  R-only subset: k = %d studies, Total N = %d",
                length(ronly_matrices), sum(ronly_n)))
message(sprintf("  Studies with converted betas: %d (%.1f%%)",
                length(full_matrices) - length(ronly_matrices),
                100 * (1 - length(ronly_matrices) / length(full_matrices))))

# ==============================================================================
# 2. COMPARE PAIR COVERAGE
# ==============================================================================
message("\n--- Comparing pair coverage ---")

count_pairs <- function(matrices) {
  pair_counts <- matrix(0, nrow = N_CONSTRUCTS, ncol = N_CONSTRUCTS,
                        dimnames = list(CONSTRUCTS, CONSTRUCTS))
  for (mat in matrices) {
    for (i in seq_along(CONSTRUCTS)) {
      for (j in seq_along(CONSTRUCTS)) {
        if (i != j &&
            CONSTRUCTS[i] %in% rownames(mat) && CONSTRUCTS[j] %in% colnames(mat) &&
            !is.na(mat[CONSTRUCTS[i], CONSTRUCTS[j]])) {
          pair_counts[CONSTRUCTS[i], CONSTRUCTS[j]] <- pair_counts[CONSTRUCTS[i], CONSTRUCTS[j]] + 1
        }
      }
    }
  }
  return(pair_counts)
}

full_coverage <- count_pairs(full_matrices)
ronly_coverage <- count_pairs(ronly_matrices)

# Coverage difference
coverage_diff <- full_coverage - ronly_coverage

# Summary
lt_idx <- lower.tri(full_coverage)
full_k_vec <- full_coverage[lt_idx]
ronly_k_vec <- ronly_coverage[lt_idx]
diff_k_vec <- coverage_diff[lt_idx]

message(sprintf("  Full dataset  — min k: %d, median k: %.0f, max k: %d",
                min(full_k_vec), median(full_k_vec), max(full_k_vec)))
message(sprintf("  R-only subset — min k: %d, median k: %.0f, max k: %d",
                min(ronly_k_vec), median(ronly_k_vec), max(ronly_k_vec)))
message(sprintf("  Mean studies lost per pair: %.1f (range: %d-%d)",
                mean(diff_k_vec), min(diff_k_vec), max(diff_k_vec)))

# Pairs that drop below minimum threshold
below_3 <- sum(ronly_k_vec < 3 & full_k_vec >= 3)
message(sprintf("  Pairs dropping below k=3 in r-only: %d", below_3))

# ==============================================================================
# 3. TSSEM STAGE 1 ON R-ONLY DATA
# ==============================================================================
message("\n--- Running TSSEM Stage 1 on r-only subset ---")

tryCatch({
  stage1_ronly <- tssem1(
    Cov  = ronly_matrices,
    n    = ronly_n,
    method = "REM",
    RE.type = "Diag",
    acov = "weighted"
  )

  summary_s1_ronly <- summary(stage1_ronly)
  message("  Stage 1 (r-only) converged")
  message(sprintf("  -2LL = %.2f, df = %d",
                  summary_s1_ronly$Minus2LogLikelihood,
                  summary_s1_ronly$degreesOfFreedom))

  # Extract pooled matrix
  pooled_ronly <- coef(stage1_ronly, select = "fixed")
  pooled_mat_ronly <- vec2symMat(pooled_ronly, diag = FALSE)
  diag(pooled_mat_ronly) <- 1
  rownames(pooled_mat_ronly) <- colnames(pooled_mat_ronly) <- CONSTRUCTS

  # Check PD
  pd_check <- check_positive_definite(pooled_mat_ronly)
  if (!pd_check$is_pd) {
    message("  WARNING: R-only pooled matrix not PD — using nearest PD")
    pooled_mat_ronly <- pd_check$nearest_pd
  }

  # Compare pooled matrices
  pooled_mat_full <- stage1_full$pooled_matrix
  mat_diff <- pooled_mat_ronly - pooled_mat_full

  lt_vals_full <- pooled_mat_full[lt_idx]
  lt_vals_ronly <- pooled_mat_ronly[lt_idx]
  lt_diffs <- mat_diff[lt_idx]

  message(sprintf("\n  Pooled matrix comparison:"))
  message(sprintf("    Mean |delta_r|: %.4f", mean(abs(lt_diffs), na.rm = TRUE)))
  message(sprintf("    Max  |delta_r|: %.4f", max(abs(lt_diffs), na.rm = TRUE)))
  message(sprintf("    Correlation of pooled vectors: %.4f",
                  cor(lt_vals_full, lt_vals_ronly, use = "complete.obs")))

}, error = function(e) {
  message(sprintf("  ERROR: Stage 1 (r-only) failed: %s", e$message))
  stage1_ronly <<- NULL
  pooled_mat_ronly <<- NULL
})

# ==============================================================================
# 4. TSSEM STAGE 2 ON R-ONLY DATA
# ==============================================================================
message("\n--- Running TSSEM Stage 2 on r-only subset ---")

# Define the same Integrated Model as used with full data
A_values <- matrix("0", nrow = N_CONSTRUCTS, ncol = N_CONSTRUCTS,
                   dimnames = list(CONSTRUCTS, CONSTRUCTS))

A_values["BI", "PE"]   <- "0.1*PE_BI"
A_values["BI", "EE"]   <- "0.1*EE_BI"
A_values["BI", "SI"]   <- "0.1*SI_BI"
A_values["BI", "ATT"]  <- "0.1*ATT_BI"
A_values["BI", "TRU"]  <- "0.1*TRU_BI"
A_values["BI", "ANX"]  <- "0.1*ANX_BI"
A_values["UB", "BI"]   <- "0.1*BI_UB"
A_values["UB", "FC"]   <- "0.1*FC_UB"
A_values["ATT", "PE"]  <- "0.1*PE_ATT"
A_values["ATT", "EE"]  <- "0.1*EE_ATT"
A_values["TRU", "TRA"] <- "0.1*TRA_TRU"
A_values["EE", "SE"]   <- "0.1*SE_EE"
A_values["ANX", "AUT"] <- "0.1*AUT_ANX"
A_values["ANX", "SE"]  <- "0.1*SE_ANX"

Amatrix <- as.mxMatrix(A_values, name = "Amatrix")

exogenous  <- c("PE", "SI", "FC", "SE", "TRA", "AUT")
endogenous <- c("EE", "BI", "UB", "ATT", "TRU", "ANX")

S_values <- matrix("0", nrow = N_CONSTRUCTS, ncol = N_CONSTRUCTS,
                   dimnames = list(CONSTRUCTS, CONSTRUCTS))
for (i in seq_along(exogenous)) {
  S_values[exogenous[i], exogenous[i]] <- paste0("0.5*Var_", exogenous[i])
  if (i < length(exogenous)) {
    for (j in (i + 1):length(exogenous)) {
      label <- paste0("0.05*Cov_", exogenous[i], "_", exogenous[j])
      S_values[exogenous[i], exogenous[j]] <- label
      S_values[exogenous[j], exogenous[i]] <- label
    }
  }
}
for (v in endogenous) {
  S_values[v, v] <- paste0("0.5*Err_", v)
}

Smatrix <- as.mxMatrix(S_values, name = "Smatrix")
Fmatrix <- as.mxMatrix(diag(N_CONSTRUCTS), name = "Fmatrix")

ronly_fit <- NULL
if (!is.null(stage1_ronly)) {
  tryCatch({
    ronly_fit <- tssem2(
      stage1_ronly,
      Amatrix = Amatrix,
      Smatrix = Smatrix,
      Fmatrix = Fmatrix,
      model.name = "Ronly_Integrated"
    )
    summary_ronly <- summary(ronly_fit)
    message("  Stage 2 (r-only) converged")
    message(sprintf("  Chi-sq = %.2f, df = %d, p = %.4f",
                    summary_ronly$stat$chisq,
                    summary_ronly$stat$chisqDF,
                    summary_ronly$stat$chisqPvalue))
    message(sprintf("  CFI = %.3f, RMSEA = %.3f, SRMR = %.3f",
                    summary_ronly$stat$CFI,
                    summary_ronly$stat$RMSEA,
                    summary_ronly$stat$SRMR))

  }, error = function(e) {
    message(sprintf("  ERROR: Stage 2 (r-only) failed: %s", e$message))
  })
}

# ==============================================================================
# 5. COMPARE PATH COEFFICIENTS: FULL vs R-ONLY
# ==============================================================================
message("\n--- Comparing path coefficients: Full vs R-only ---")

comparison_table <- NULL

# Load full model results (from stage1_results or re-fit)
# We need the full Stage 2 coefficients. Try loading from output.
full_fit_path <- file.path(PATHS$output, "tssem_results.rds")
full_coefs <- NULL

if (file.exists(full_fit_path)) {
  tssem_results <- readRDS(full_fit_path)
  # Try to get Integrated model coefficients
  if (!is.null(tssem_results$integrated$coefficients)) {
    full_coefs <- tssem_results$integrated$coefficients
  } else if (!is.null(tssem_results$integrated$model)) {
    full_coefs <- coef(tssem_results$integrated$model)
  }
}

# Fallback: re-run full Stage 2
if (is.null(full_coefs)) {
  message("  Re-running full Stage 2 for comparison...")
  tryCatch({
    stage1_full_fit <- tssem1(
      Cov = full_matrices, n = full_n,
      method = "REM", RE.type = "Diag", acov = "weighted"
    )
    full_fit <- tssem2(
      stage1_full_fit,
      Amatrix = Amatrix, Smatrix = Smatrix, Fmatrix = Fmatrix,
      model.name = "Full_Integrated"
    )
    full_coefs <- coef(full_fit)
    full_vcov <- vcov(full_fit)
    message("  Full model re-fitted successfully")
  }, error = function(e) {
    message(sprintf("  ERROR re-fitting full model: %s", e$message))
  })
}

if (!is.null(full_coefs) && !is.null(ronly_fit)) {
  ronly_coefs <- coef(ronly_fit)

  path_labels <- c("PE_BI", "EE_BI", "SI_BI", "ATT_BI", "TRU_BI", "ANX_BI",
                    "BI_UB", "FC_UB", "PE_ATT", "EE_ATT", "TRA_TRU",
                    "SE_EE", "AUT_ANX", "SE_ANX")

  common_paths <- intersect(names(full_coefs), names(ronly_coefs))
  common_paths <- common_paths[common_paths %in% path_labels]

  comparison_table <- data.frame(
    Path = common_paths,
    Full_Est = numeric(length(common_paths)),
    Ronly_Est = numeric(length(common_paths)),
    Abs_Diff = numeric(length(common_paths)),
    Rel_Change_Pct = numeric(length(common_paths)),
    Same_Sign = logical(length(common_paths)),
    Same_Significance = logical(length(common_paths)),
    stringsAsFactors = FALSE
  )

  for (i in seq_along(common_paths)) {
    p <- common_paths[i]
    b_full <- full_coefs[p]
    b_ronly <- ronly_coefs[p]
    abs_diff <- abs(b_ronly - b_full)
    rel_change <- if (abs(b_full) > 0.001) 100 * abs_diff / abs(b_full) else NA

    comparison_table$Full_Est[i] <- round(b_full, 4)
    comparison_table$Ronly_Est[i] <- round(b_ronly, 4)
    comparison_table$Abs_Diff[i] <- round(abs_diff, 4)
    comparison_table$Rel_Change_Pct[i] <- round(rel_change, 1)
    comparison_table$Same_Sign[i] <- sign(b_full) == sign(b_ronly)
    # Approximate significance check: both > |0.05| or both < |0.05|
    comparison_table$Same_Significance[i] <- (abs(b_full) > 0.05) == (abs(b_ronly) > 0.05)
  }

  message("\n  Path Coefficient Comparison (Full vs R-only):")
  print(comparison_table, row.names = FALSE)

  # Summary statistics
  max_abs_diff <- max(comparison_table$Abs_Diff, na.rm = TRUE)
  mean_abs_diff <- mean(comparison_table$Abs_Diff, na.rm = TRUE)
  cor_estimates <- cor(comparison_table$Full_Est, comparison_table$Ronly_Est)
  all_same_sign <- all(comparison_table$Same_Sign)
  all_same_sig <- all(comparison_table$Same_Significance)

  message(sprintf("\n  Summary:"))
  message(sprintf("    Max |delta|:           %.4f", max_abs_diff))
  message(sprintf("    Mean |delta|:          %.4f", mean_abs_diff))
  message(sprintf("    Correlation(full, r):  %.4f", cor_estimates))
  message(sprintf("    All same sign:         %s", all_same_sign))
  message(sprintf("    All same significance: %s", all_same_sig))
}

# ==============================================================================
# 6. DECISION RULE
# ==============================================================================
message("\n--- Applying decision rule ---")

decision <- list(
  max_abs_diff = if (exists("max_abs_diff")) max_abs_diff else NA,
  cor_estimates = if (exists("cor_estimates")) cor_estimates else NA,
  criterion_diff = 0.05,
  criterion_cor = 0.95,
  robust = NA
)

if (!is.na(decision$max_abs_diff) && !is.na(decision$cor_estimates)) {
  criterion_1 <- decision$max_abs_diff < decision$criterion_diff
  criterion_2 <- decision$cor_estimates > decision$criterion_cor

  decision$criterion_1_met <- criterion_1
  decision$criterion_2_met <- criterion_2
  decision$robust <- criterion_1 & criterion_2

  message(sprintf("  Criterion 1: max |delta| < %.2f -> %s (actual: %.4f)",
                  decision$criterion_diff,
                  ifelse(criterion_1, "MET", "NOT MET"),
                  decision$max_abs_diff))
  message(sprintf("  Criterion 2: r(estimates) > %.2f -> %s (actual: %.4f)",
                  decision$criterion_cor,
                  ifelse(criterion_2, "MET", "NOT MET"),
                  decision$cor_estimates))

  if (decision$robust) {
    message("\n  CONCLUSION: Beta-to-r conversion is ROBUST.")
    message("  Results are stable regardless of whether converted betas are included.")
  } else {
    message("\n  CONCLUSION: Beta-to-r conversion shows SOME sensitivity.")
    if (!criterion_1) {
      message("  Some paths differ by more than .05 — report both sets of estimates.")
    }
    if (!criterion_2) {
      message("  Overall pattern of estimates is not highly correlated — caution warranted.")
    }
    message("  Recommendation: Report both full and r-only results in supplementary materials.")
  }
} else {
  message("  Decision rule could not be applied (missing data)")
}

# ==============================================================================
# 7. FIT INDEX COMPARISON
# ==============================================================================
message("\n--- Fit index comparison ---")

fit_comp <- NULL
if (!is.null(ronly_fit) && exists("full_fit") && !is.null(full_fit)) {
  summary_full <- summary(full_fit)

  fit_comp <- data.frame(
    Index = c("Chi-square", "df", "p", "CFI", "TLI", "RMSEA", "SRMR"),
    Full = c(
      round(summary_full$stat$chisq, 2),
      summary_full$stat$chisqDF,
      round(summary_full$stat$chisqPvalue, 4),
      round(summary_full$stat$CFI, 3),
      round(summary_full$stat$TLI, 3),
      round(summary_full$stat$RMSEA, 3),
      round(summary_full$stat$SRMR, 3)
    ),
    R_only = c(
      round(summary_ronly$stat$chisq, 2),
      summary_ronly$stat$chisqDF,
      round(summary_ronly$stat$chisqPvalue, 4),
      round(summary_ronly$stat$CFI, 3),
      round(summary_ronly$stat$TLI, 3),
      round(summary_ronly$stat$RMSEA, 3),
      round(summary_ronly$stat$SRMR, 3)
    ),
    stringsAsFactors = FALSE
  )

  message("\n  Fit Index Comparison:")
  print(fit_comp, row.names = FALSE)
}

# ==============================================================================
# 8. VISUALIZATION
# ==============================================================================
message("\n--- Creating sensitivity comparison plot ---")

if (!is.null(comparison_table)) {
  # Scatter plot: full vs r-only estimates
  p_scatter <- ggplot(comparison_table, aes(x = Full_Est, y = Ronly_Est)) +
    geom_point(size = 3, color = "#2166AC") +
    geom_abline(intercept = 0, slope = 1, linetype = "dashed", color = "red") +
    geom_text(aes(label = Path), hjust = -0.15, vjust = -0.3, size = 3) +
    labs(
      title = "Sensitivity Analysis: Full vs R-only Path Coefficients",
      subtitle = sprintf("r = %.3f, max |diff| = %.4f",
                         cor_estimates, max_abs_diff),
      x = "Full Dataset (r + converted beta)",
      y = "R-only Subset"
    ) +
    theme_minimal(base_size = 12) +
    theme(plot.title = element_text(face = "bold")) +
    coord_fixed()

  ggsave(file.path(PATHS$figures, "sensitivity_scatter.png"),
         p_scatter, width = 8, height = 8, dpi = 300)
  ggsave(file.path(PATHS$figures, "sensitivity_scatter.pdf"),
         p_scatter, width = 8, height = 8)
  message("  Saved scatter plot")

  # Bar chart of absolute differences
  comp_sorted <- comparison_table[order(-comparison_table$Abs_Diff), ]
  comp_sorted$Path <- factor(comp_sorted$Path, levels = comp_sorted$Path)

  p_diff <- ggplot(comp_sorted, aes(x = Path, y = Abs_Diff)) +
    geom_bar(stat = "identity", fill = "#4393C3", alpha = 0.8) +
    geom_hline(yintercept = 0.05, linetype = "dashed", color = "red", linewidth = 0.8) +
    annotate("text", x = nrow(comp_sorted), y = 0.053,
             label = "Threshold (0.05)", hjust = 1, color = "red", size = 3.5) +
    labs(
      title = "Absolute Difference in Path Coefficients (Full vs R-only)",
      x = "Path", y = "|Full - R-only|"
    ) +
    theme_minimal(base_size = 12) +
    theme(
      axis.text.x = element_text(angle = 45, hjust = 1),
      plot.title = element_text(face = "bold")
    )

  ggsave(file.path(PATHS$figures, "sensitivity_differences.png"),
         p_diff, width = 10, height = 6, dpi = 300)
  ggsave(file.path(PATHS$figures, "sensitivity_differences.pdf"),
         p_diff, width = 10, height = 6)
  message("  Saved difference plot")
}

# ==============================================================================
# 9. SAVE RESULTS
# ==============================================================================
message("\n--- Saving sensitivity analysis results ---")

sensitivity_output <- list(
  comparison_table = comparison_table,
  fit_comparison = fit_comp,
  decision = decision,
  n_full = length(full_matrices),
  n_ronly = length(ronly_matrices),
  n_converted = length(full_matrices) - length(ronly_matrices),
  pooled_matrix_full = stage1_full$pooled_matrix,
  pooled_matrix_ronly = if (exists("pooled_mat_ronly")) pooled_mat_ronly else NULL,
  coverage_full = full_coverage,
  coverage_ronly = ronly_coverage,
  stage1_ronly = if (exists("stage1_ronly")) stage1_ronly else NULL,
  stage2_ronly = ronly_fit
)

saveRDS(sensitivity_output, file.path(PATHS$output, "sensitivity_results.rds"))
message(sprintf("  Saved to: %s", file.path(PATHS$output, "sensitivity_results.rds")))

if (!is.null(comparison_table)) {
  write.csv(comparison_table,
            file.path(PATHS$output, "sensitivity_comparison_table.csv"),
            row.names = FALSE)
  message(sprintf("  Table saved to: %s",
                  file.path(PATHS$output, "sensitivity_comparison_table.csv")))
}

message("\n", strrep("=", 70))
message("10: SENSITIVITY ANALYSIS COMPLETE")
message(strrep("=", 70))
