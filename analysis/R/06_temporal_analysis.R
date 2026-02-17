# ==============================================================================
# 06_temporal_analysis.R — Pre/Post ChatGPT Temporal Analysis
# Educational AI Adoption MASEM Meta-Analysis
# ==============================================================================
# Purpose: Compare educational AI adoption structural relationships before vs after ChatGPT
#   - Binary split: pre-2023 vs post-2023 (ChatGPT launched Nov 2022)
#   - Separate TSSEM Stage 1 + Stage 2 for each subgroup
#   - Subgroup analysis by education level (K-12 vs Higher Ed)
#   - Subgroup analysis by user role (Student vs Instructor)
#   - Wald tests for coefficient differences
#   - Hypothesis testing on temporal shifts
# Dependencies: 00_setup.R, prepared_data.rds
# Output: temporal_analysis_results.rds, comparison tables
# ==============================================================================

source("analysis/R/00_setup.R")
message("\n", strrep("=", 70))
message("06: TEMPORAL ANALYSIS — PRE/POST ChatGPT COMPARISON (EDUCATION)")
message(strrep("=", 70))

# ==============================================================================
# 1. LOAD DATA AND SPLIT BY ERA
# ==============================================================================
message("\n--- Loading and splitting data ---")
prepared <- readRDS(file.path(PATHS$pooled, "prepared_data.rds"))

cor_matrices <- prepared$cor_matrices
sample_sizes <- prepared$sample_sizes
metadata     <- prepared$study_metadata

# Determine year for each study
if (!"year" %in% colnames(metadata)) {
  stop("'year' column required in study_metadata for temporal analysis")
}

study_years <- metadata$year
names(study_years) <- names(cor_matrices)

# Binary split: ChatGPT launched November 2022
# Pre-ChatGPT: studies published <= 2022 (data collected before ChatGPT)
# Post-ChatGPT: studies published >= 2023
CUTOFF_YEAR <- 2023

pre_idx  <- which(study_years < CUTOFF_YEAR)
post_idx <- which(study_years >= CUTOFF_YEAR)

message(sprintf("  Cutoff year: %d (ChatGPT launched Nov 2022)", CUTOFF_YEAR))
message(sprintf("  Pre-ChatGPT  (< %d): k = %d studies", CUTOFF_YEAR, length(pre_idx)))
message(sprintf("  Post-ChatGPT (>= %d): k = %d studies", CUTOFF_YEAR, length(post_idx)))

if (length(pre_idx) < 5 || length(post_idx) < 5) {
  warning("One subgroup has fewer than 5 studies — results may be unstable")
}

# Split data
pre_matrices  <- cor_matrices[pre_idx]
post_matrices <- cor_matrices[post_idx]
pre_n  <- sample_sizes[pre_idx]
post_n <- sample_sizes[post_idx]

message(sprintf("  Pre-ChatGPT  total N: %d (harmonic N: %.0f)",
                sum(pre_n), harmonic_mean(pre_n)))
message(sprintf("  Post-ChatGPT total N: %d (harmonic N: %.0f)",
                sum(post_n), harmonic_mean(post_n)))

# ==============================================================================
# 2. TSSEM STAGE 1: SEPARATE POOLED MATRICES
# ==============================================================================
message("\n--- TSSEM Stage 1: Pooling correlation matrices by era ---")

# --- Pre-ChatGPT Stage 1 ---
message("\n  [Pre-ChatGPT Stage 1]")
tryCatch({
  stage1_pre <- tssem1(
    Cov  = pre_matrices,
    n    = pre_n,
    method = "REM",
    RE.type = "Diag",
    acov = "weighted"
  )
  summary_s1_pre <- summary(stage1_pre)

  pooled_pre <- coef(stage1_pre, select = "fixed")
  # Reconstruct pooled matrix
  pooled_mat_pre <- vec2symMat(pooled_pre, diag = FALSE)
  diag(pooled_mat_pre) <- 1
  rownames(pooled_mat_pre) <- colnames(pooled_mat_pre) <- CONSTRUCTS

  message(sprintf("  Stage 1 converged. -2LL = %.2f",
                  summary_s1_pre$Minus2LogLikelihood))

  # Check positive definiteness
  pd_check_pre <- check_positive_definite(pooled_mat_pre)
  if (!pd_check_pre$is_pd) {
    message("  WARNING: Pre-ChatGPT pooled matrix not PD — using nearest PD")
    pooled_mat_pre <- pd_check_pre$nearest_pd
  }

}, error = function(e) {
  message(sprintf("  ERROR in pre-ChatGPT Stage 1: %s", e$message))
  stage1_pre <<- NULL
  pooled_mat_pre <<- NULL
})

# --- Post-ChatGPT Stage 1 ---
message("\n  [Post-ChatGPT Stage 1]")
tryCatch({
  stage1_post <- tssem1(
    Cov  = post_matrices,
    n    = post_n,
    method = "REM",
    RE.type = "Diag",
    acov = "weighted"
  )
  summary_s1_post <- summary(stage1_post)

  pooled_post <- coef(stage1_post, select = "fixed")
  pooled_mat_post <- vec2symMat(pooled_post, diag = FALSE)
  diag(pooled_mat_post) <- 1
  rownames(pooled_mat_post) <- colnames(pooled_mat_post) <- CONSTRUCTS

  message(sprintf("  Stage 1 converged. -2LL = %.2f",
                  summary_s1_post$Minus2LogLikelihood))

  pd_check_post <- check_positive_definite(pooled_mat_post)
  if (!pd_check_post$is_pd) {
    message("  WARNING: Post-ChatGPT pooled matrix not PD — using nearest PD")
    pooled_mat_post <- pd_check_post$nearest_pd
  }

}, error = function(e) {
  message(sprintf("  ERROR in post-ChatGPT Stage 1: %s", e$message))
  stage1_post <<- NULL
  pooled_mat_post <<- NULL
})

# ==============================================================================
# 3. TSSEM STAGE 2: FIT INTEGRATED MODEL TO EACH SUBGROUP
# ==============================================================================
message("\n--- TSSEM Stage 2: Fitting Integrated Model by era ---")

# Define the Integrated Model (consistent with 04_tssem_models.R)
# RAM specification
model_syntax <- "
  ## Direct effects on BI
  BI ~ PE_BI*PE + EE_BI*EE + SI_BI*SI + ATT_BI*ATT + TRU_BI*TRU + ANX_BI*ANX
  ## Direct effects on UB
  UB ~ BI_UB*BI + FC_UB*FC
  ## Direct effects on ATT
  ATT ~ PE_ATT*PE + EE_ATT*EE
  ## AI-specific paths
  TRU ~ TRA_TRU*TRA
  EE ~ SE_EE*SE
  ANX ~ AUT_ANX*AUT + SE_ANX*SE
"

# Build RAM matrices
# A matrix (directed paths)
A_mat <- matrix(0, nrow = N_CONSTRUCTS, ncol = N_CONSTRUCTS,
                dimnames = list(CONSTRUCTS, CONSTRUCTS))
A_labels <- A_mat
A_free <- matrix(FALSE, nrow = N_CONSTRUCTS, ncol = N_CONSTRUCTS,
                 dimnames = list(CONSTRUCTS, CONSTRUCTS))

# Define paths: A[row=DV, col=IV]
paths <- list(
  c("BI", "PE", "PE_BI"),   c("BI", "EE", "EE_BI"),
  c("BI", "SI", "SI_BI"),   c("BI", "ATT", "ATT_BI"),
  c("BI", "TRU", "TRU_BI"), c("BI", "ANX", "ANX_BI"),
  c("UB", "BI", "BI_UB"),   c("UB", "FC", "FC_UB"),
  c("ATT", "PE", "PE_ATT"), c("ATT", "EE", "EE_ATT"),
  c("TRU", "TRA", "TRA_TRU"),
  c("EE", "SE", "SE_EE"),
  c("ANX", "AUT", "AUT_ANX"), c("ANX", "SE", "SE_ANX")
)

A_values <- matrix("0", nrow = N_CONSTRUCTS, ncol = N_CONSTRUCTS,
                   dimnames = list(CONSTRUCTS, CONSTRUCTS))
for (p in paths) {
  A_values[p[1], p[2]] <- paste0("0.1*", p[3])
}
Amatrix <- as.mxMatrix(A_values, name = "Amatrix")

# S matrix (symmetric: exogenous covariances + residual variances)
exogenous  <- c("PE", "SI", "FC", "SE", "TRA", "AUT")
endogenous <- c("EE", "BI", "UB", "ATT", "TRU", "ANX")

S_values <- matrix("0", nrow = N_CONSTRUCTS, ncol = N_CONSTRUCTS,
                   dimnames = list(CONSTRUCTS, CONSTRUCTS))

# Exogenous: free variances and covariances
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

# Endogenous: residual variances only
for (v in endogenous) {
  S_values[v, v] <- paste0("0.5*Err_", v)
}

Smatrix <- as.mxMatrix(S_values, name = "Smatrix")

# F matrix (filter: all observed)
Fmatrix <- as.mxMatrix(diag(N_CONSTRUCTS), name = "Fmatrix")

# --- Fit Pre-ChatGPT ---
message("\n  [Pre-ChatGPT Stage 2]")
pre_fit <- NULL
if (!is.null(stage1_pre)) {
  tryCatch({
    pre_fit <- tssem2(
      stage1_pre,
      Amatrix = Amatrix,
      Smatrix = Smatrix,
      Fmatrix = Fmatrix,
      model.name = "Pre_ChatGPT_Integrated"
    )
    summary_pre <- summary(pre_fit)
    message("  Pre-ChatGPT Stage 2 converged")
    message(sprintf("  Chi-sq = %.2f, df = %d, p = %.4f",
                    summary_pre$stat$chisq, summary_pre$stat$chisqDF,
                    summary_pre$stat$chisqPvalue))
    message(sprintf("  CFI = %.3f, RMSEA = %.3f, SRMR = %.3f",
                    summary_pre$stat$CFI, summary_pre$stat$RMSEA,
                    summary_pre$stat$SRMR))

    pre_coefs <- coef(pre_fit)
    message("\n  Pre-ChatGPT path coefficients:")
    path_labels <- sapply(paths, `[`, 3)
    for (pl in path_labels) {
      if (pl %in% names(pre_coefs)) {
        message(sprintf("    %s = %.4f", pl, pre_coefs[pl]))
      }
    }
  }, error = function(e) {
    message(sprintf("  ERROR in pre-ChatGPT Stage 2: %s", e$message))
  })
}

# --- Fit Post-ChatGPT ---
message("\n  [Post-ChatGPT Stage 2]")
post_fit <- NULL
if (!is.null(stage1_post)) {
  tryCatch({
    post_fit <- tssem2(
      stage1_post,
      Amatrix = Amatrix,
      Smatrix = Smatrix,
      Fmatrix = Fmatrix,
      model.name = "Post_ChatGPT_Integrated"
    )
    summary_post <- summary(post_fit)
    message("  Post-ChatGPT Stage 2 converged")
    message(sprintf("  Chi-sq = %.2f, df = %d, p = %.4f",
                    summary_post$stat$chisq, summary_post$stat$chisqDF,
                    summary_post$stat$chisqPvalue))
    message(sprintf("  CFI = %.3f, RMSEA = %.3f, SRMR = %.3f",
                    summary_post$stat$CFI, summary_post$stat$RMSEA,
                    summary_post$stat$SRMR))

    post_coefs <- coef(post_fit)
    message("\n  Post-ChatGPT path coefficients:")
    for (pl in path_labels) {
      if (pl %in% names(post_coefs)) {
        message(sprintf("    %s = %.4f", pl, post_coefs[pl]))
      }
    }
  }, error = function(e) {
    message(sprintf("  ERROR in post-ChatGPT Stage 2: %s", e$message))
  })
}

# ==============================================================================
# 4. COEFFICIENT COMPARISON AND HYPOTHESIS TESTING
# ==============================================================================
message("\n--- Comparing path coefficients across eras ---")

comparison_table <- NULL

if (!is.null(pre_fit) && !is.null(post_fit)) {
  pre_coefs  <- coef(pre_fit)
  post_coefs <- coef(post_fit)

  # Get SE from vcov
  pre_vcov  <- vcov(pre_fit)
  post_vcov <- vcov(post_fit)

  path_labels <- sapply(paths, `[`, 3)
  common_paths <- intersect(names(pre_coefs), names(post_coefs))
  common_paths <- common_paths[common_paths %in% path_labels]

  comparison_table <- data.frame(
    Path = common_paths,
    Pre_Est = numeric(length(common_paths)),
    Pre_SE = numeric(length(common_paths)),
    Post_Est = numeric(length(common_paths)),
    Post_SE = numeric(length(common_paths)),
    Diff = numeric(length(common_paths)),
    z_diff = numeric(length(common_paths)),
    p_diff = numeric(length(common_paths)),
    Significant = logical(length(common_paths)),
    stringsAsFactors = FALSE
  )

  for (i in seq_along(common_paths)) {
    p_name <- common_paths[i]

    b_pre  <- pre_coefs[p_name]
    b_post <- post_coefs[p_name]

    se_pre  <- if (p_name %in% rownames(pre_vcov)) sqrt(pre_vcov[p_name, p_name]) else NA
    se_post <- if (p_name %in% rownames(post_vcov)) sqrt(post_vcov[p_name, p_name]) else NA

    diff <- b_post - b_pre

    # Wald test for difference: z = (b_post - b_pre) / sqrt(se_pre^2 + se_post^2)
    se_diff <- sqrt(se_pre^2 + se_post^2)
    z_val <- diff / se_diff
    p_val <- 2 * pnorm(abs(z_val), lower.tail = FALSE)

    comparison_table$Pre_Est[i]  <- round(b_pre, 4)
    comparison_table$Pre_SE[i]   <- round(se_pre, 4)
    comparison_table$Post_Est[i] <- round(b_post, 4)
    comparison_table$Post_SE[i]  <- round(se_post, 4)
    comparison_table$Diff[i]     <- round(diff, 4)
    comparison_table$z_diff[i]   <- round(z_val, 3)
    comparison_table$p_diff[i]   <- round(p_val, 4)
    comparison_table$Significant[i] <- !is.na(p_val) & p_val < .05
  }

  message("\n  Temporal Comparison Table:")
  print(comparison_table, row.names = FALSE)

  # Count significant differences
  n_sig <- sum(comparison_table$Significant, na.rm = TRUE)
  message(sprintf("\n  %d of %d paths show significant temporal differences (p < .05)",
                  n_sig, nrow(comparison_table)))
}

# ==============================================================================
# 5. SPECIFIC HYPOTHESIS TESTS
# ==============================================================================
message("\n--- Testing Specific Temporal Hypotheses ---")

hypotheses <- list()

if (!is.null(comparison_table)) {
  # H1: ANX -> BI weakens after ChatGPT (normalization hypothesis)
  if ("ANX_BI" %in% comparison_table$Path) {
    row <- comparison_table[comparison_table$Path == "ANX_BI", ]
    hypotheses$H1_anxiety_normalization <- list(
      hypothesis = "ANX->BI weakens (becomes less negative) after ChatGPT",
      pre_estimate = row$Pre_Est,
      post_estimate = row$Post_Est,
      difference = row$Diff,
      z = row$z_diff,
      p_two_tailed = row$p_diff,
      # One-tailed: expect post > pre (less negative)
      p_one_tailed = if (row$Diff > 0) row$p_diff / 2 else 1 - row$p_diff / 2,
      supported = row$Diff > 0 & row$p_diff < .10  # one-tailed at alpha = .05
    )
    message(sprintf("  H1 (ANX normalization): pre=%.3f, post=%.3f, diff=%.3f, p=%.4f, %s",
                    row$Pre_Est, row$Post_Est, row$Diff, row$p_diff,
                    ifelse(hypotheses$H1_anxiety_normalization$supported,
                           "SUPPORTED", "NOT SUPPORTED")))
  }

  # H2: PE -> BI strengthens after ChatGPT (proven utility)
  if ("PE_BI" %in% comparison_table$Path) {
    row <- comparison_table[comparison_table$Path == "PE_BI", ]
    hypotheses$H2_PE_strengthens <- list(
      hypothesis = "PE->BI strengthens after ChatGPT (proven utility)",
      pre_estimate = row$Pre_Est,
      post_estimate = row$Post_Est,
      difference = row$Diff,
      z = row$z_diff,
      p_two_tailed = row$p_diff,
      p_one_tailed = if (row$Diff > 0) row$p_diff / 2 else 1 - row$p_diff / 2,
      supported = row$Diff > 0 & row$p_diff < .10
    )
    message(sprintf("  H2 (PE utility): pre=%.3f, post=%.3f, diff=%.3f, p=%.4f, %s",
                    row$Pre_Est, row$Post_Est, row$Diff, row$p_diff,
                    ifelse(hypotheses$H2_PE_strengthens$supported,
                           "SUPPORTED", "NOT SUPPORTED")))
  }

  # H3: TRU -> BI changes after ChatGPT
  if ("TRU_BI" %in% comparison_table$Path) {
    row <- comparison_table[comparison_table$Path == "TRU_BI", ]
    hypotheses$H3_trust_shift <- list(
      hypothesis = "TRU->BI changes magnitude after ChatGPT",
      pre_estimate = row$Pre_Est,
      post_estimate = row$Post_Est,
      difference = row$Diff,
      z = row$z_diff,
      p_two_tailed = row$p_diff,
      direction = ifelse(row$Diff > 0, "strengthened", "weakened"),
      supported = row$p_diff < .05
    )
    message(sprintf("  H3 (Trust shift): pre=%.3f, post=%.3f, diff=%.3f, p=%.4f, %s (%s)",
                    row$Pre_Est, row$Post_Est, row$Diff, row$p_diff,
                    ifelse(hypotheses$H3_trust_shift$supported,
                           "SIGNIFICANT", "NOT SIGNIFICANT"),
                    hypotheses$H3_trust_shift$direction))
  }
}

# ==============================================================================
# 6. FIT INDEX COMPARISON
# ==============================================================================
message("\n--- Fit Index Comparison ---")

fit_comparison <- NULL
if (!is.null(pre_fit) && !is.null(post_fit)) {
  fit_comparison <- data.frame(
    Index = c("Chi-square", "df", "p", "CFI", "TLI", "RMSEA", "SRMR", "AIC", "BIC"),
    Pre_ChatGPT = c(
      round(summary_pre$stat$chisq, 2),
      summary_pre$stat$chisqDF,
      round(summary_pre$stat$chisqPvalue, 4),
      round(summary_pre$stat$CFI, 3),
      round(summary_pre$stat$TLI, 3),
      round(summary_pre$stat$RMSEA, 3),
      round(summary_pre$stat$SRMR, 3),
      round(summary_pre$stat$AIC, 2),
      round(summary_pre$stat$BIC, 2)
    ),
    Post_ChatGPT = c(
      round(summary_post$stat$chisq, 2),
      summary_post$stat$chisqDF,
      round(summary_post$stat$chisqPvalue, 4),
      round(summary_post$stat$CFI, 3),
      round(summary_post$stat$TLI, 3),
      round(summary_post$stat$RMSEA, 3),
      round(summary_post$stat$SRMR, 3),
      round(summary_post$stat$AIC, 2),
      round(summary_post$stat$BIC, 2)
    ),
    stringsAsFactors = FALSE
  )

  message("\n  Fit Index Comparison:")
  print(fit_comparison, row.names = FALSE)
}

# ==============================================================================
# 7. POOLED MATRIX COMPARISON
# ==============================================================================
message("\n--- Comparing pooled correlation matrices ---")

if (exists("pooled_mat_pre") && exists("pooled_mat_post") &&
    !is.null(pooled_mat_pre) && !is.null(pooled_mat_post)) {

  cor_diff <- pooled_mat_post - pooled_mat_pre

  # Extract lower triangle differences
  lt_idx <- lower.tri(cor_diff)
  diffs <- cor_diff[lt_idx]

  # Build pair labels
  pair_labels <- c()
  for (i in 2:N_CONSTRUCTS) {
    for (j in 1:(i - 1)) {
      pair_labels <- c(pair_labels, paste0(CONSTRUCTS[j], "-", CONSTRUCTS[i]))
    }
  }

  diff_df <- data.frame(
    Pair = pair_labels,
    Pre_r = round(pooled_mat_pre[lt_idx], 3),
    Post_r = round(pooled_mat_post[lt_idx], 3),
    Diff = round(diffs, 3),
    stringsAsFactors = FALSE
  )
  diff_df <- diff_df[order(-abs(diff_df$Diff)), ]

  message("\n  Top 10 largest correlation shifts (post - pre):")
  print(head(diff_df, 10), row.names = FALSE)

  # Summary statistics
  message(sprintf("\n  Mean absolute correlation difference: %.3f", mean(abs(diffs), na.rm = TRUE)))
  message(sprintf("  Max absolute correlation difference:  %.3f (%s)",
                  max(abs(diffs), na.rm = TRUE),
                  diff_df$Pair[which.max(abs(diff_df$Diff))]))
  message(sprintf("  Correlation of pre vs post pooled vectors: %.3f",
                  cor(pooled_mat_pre[lt_idx], pooled_mat_post[lt_idx], use = "complete.obs")))
}

# ==============================================================================
# 8. VISUALIZATION: TEMPORAL COMPARISON PLOT
# ==============================================================================
message("\n--- Creating temporal comparison plots ---")

if (!is.null(comparison_table)) {
  # Path coefficient comparison plot
  plot_data <- comparison_table %>%
    tidyr::pivot_longer(
      cols = c(Pre_Est, Post_Est),
      names_to = "Era",
      values_to = "Estimate"
    ) %>%
    mutate(
      Era = ifelse(Era == "Pre_Est", "Pre-ChatGPT", "Post-ChatGPT"),
      SE = ifelse(Era == "Pre-ChatGPT", Pre_SE, Post_SE)
    )

  p_temporal <- ggplot(plot_data, aes(x = Path, y = Estimate, fill = Era)) +
    geom_bar(stat = "identity", position = position_dodge(0.8), width = 0.7) +
    geom_errorbar(
      aes(ymin = Estimate - 1.96 * SE, ymax = Estimate + 1.96 * SE),
      position = position_dodge(0.8), width = 0.25
    ) +
    scale_fill_manual(values = c("Pre-ChatGPT" = "#2166AC", "Post-ChatGPT" = "#B2182B")) +
    labs(
      title = "Educational AI Adoption: Pre vs Post ChatGPT Path Coefficients",
      subtitle = sprintf("Pre-ChatGPT (k=%d) vs Post-ChatGPT (k=%d)",
                         length(pre_idx), length(post_idx)),
      x = "Path", y = "Standardized Coefficient",
      fill = "Era"
    ) +
    theme_minimal(base_size = 12) +
    theme(
      axis.text.x = element_text(angle = 45, hjust = 1),
      legend.position = "bottom",
      plot.title = element_text(face = "bold")
    ) +
    geom_hline(yintercept = 0, linetype = "dashed", color = "grey50")

  ggsave(file.path(PATHS$figures, "temporal_comparison_paths.png"),
         p_temporal, width = 12, height = 7, dpi = 300)
  ggsave(file.path(PATHS$figures, "temporal_comparison_paths.pdf"),
         p_temporal, width = 12, height = 7)
  message("  Saved temporal comparison plot")

  # Difference plot with significance markers
  p_diff <- ggplot(comparison_table, aes(x = reorder(Path, abs(Diff)), y = Diff)) +
    geom_bar(stat = "identity", aes(fill = Significant), width = 0.6) +
    scale_fill_manual(values = c("FALSE" = "grey60", "TRUE" = "#E41A1C"),
                      labels = c("FALSE" = "n.s.", "TRUE" = "p < .05")) +
    coord_flip() +
    labs(
      title = "Educational AI: Temporal Change in Path Coefficients (Post - Pre ChatGPT)",
      x = "Path", y = "Difference (Post - Pre)",
      fill = "Significance"
    ) +
    theme_minimal(base_size = 12) +
    geom_hline(yintercept = 0, linetype = "dashed") +
    theme(plot.title = element_text(face = "bold"))

  ggsave(file.path(PATHS$figures, "temporal_difference_plot.png"),
         p_diff, width = 10, height = 6, dpi = 300)
  ggsave(file.path(PATHS$figures, "temporal_difference_plot.pdf"),
         p_diff, width = 10, height = 6)
  message("  Saved temporal difference plot")
}

# ==============================================================================
# 9. SAVE ALL RESULTS
# ==============================================================================
message("\n--- Saving temporal analysis results ---")

temporal_results <- list(
  # Metadata
  cutoff_year = CUTOFF_YEAR,
  n_pre = length(pre_idx),
  n_post = length(post_idx),
  total_n_pre = sum(pre_n),
  total_n_post = sum(post_n),
  harmonic_n_pre = harmonic_mean(pre_n),
  harmonic_n_post = harmonic_mean(post_n),

  # Stage 1 results
  stage1_pre = if (exists("stage1_pre")) stage1_pre else NULL,
  stage1_post = if (exists("stage1_post")) stage1_post else NULL,
  pooled_matrix_pre = if (exists("pooled_mat_pre")) pooled_mat_pre else NULL,
  pooled_matrix_post = if (exists("pooled_mat_post")) pooled_mat_post else NULL,

  # Stage 2 results
  model_pre = pre_fit,
  model_post = post_fit,
  summary_pre = if (exists("summary_pre")) summary_pre else NULL,
  summary_post = if (exists("summary_post")) summary_post else NULL,

  # Comparisons
  comparison_table = comparison_table,
  fit_comparison = fit_comparison,
  hypotheses = hypotheses,
  correlation_diff = if (exists("diff_df")) diff_df else NULL
)

saveRDS(temporal_results, file.path(PATHS$output, "temporal_analysis_results.rds"))
message(sprintf("  Saved to: %s", file.path(PATHS$output, "temporal_analysis_results.rds")))

# Save comparison table as CSV
if (!is.null(comparison_table)) {
  write.csv(comparison_table,
            file.path(PATHS$output, "temporal_comparison_table.csv"),
            row.names = FALSE)
  message(sprintf("  Table saved to: %s",
                  file.path(PATHS$output, "temporal_comparison_table.csv")))
}

message("\n", strrep("=", 70))
message("06: TEMPORAL ANALYSIS COMPLETE")
message(strrep("=", 70))
