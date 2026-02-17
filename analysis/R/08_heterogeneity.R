# ==============================================================================
# 08_heterogeneity.R — Heterogeneity Decomposition for All 66 Correlations
# AI Adoption MASEM Dissertation
# ==============================================================================
# Purpose: Univariate random-effects meta-analysis for each pairwise correlation
#   - Pooled r, k, I-squared, tau-squared, Q, p_Q for all 66 pairs
#   - 95% prediction intervals
#   - Identify high-heterogeneity pairs (I^2 > 75%)
#   - I-squared heatmap visualization
# Dependencies: 00_setup.R, prepared_data.rds
# Output: heterogeneity_results.rds, heterogeneity_table.csv, heatmap
# ==============================================================================

source("analysis/R/00_setup.R")
message("\n", strrep("=", 70))
message("08: HETEROGENEITY DECOMPOSITION — ALL 66 CORRELATIONS")
message(strrep("=", 70))

# ==============================================================================
# 1. LOAD DATA
# ==============================================================================
message("\n--- Loading prepared data ---")
prepared <- readRDS(file.path(PATHS$pooled, "prepared_data.rds"))

cor_matrices <- prepared$cor_matrices
sample_sizes <- prepared$sample_sizes
k_total <- length(cor_matrices)

message(sprintf("  Total studies: %d", k_total))

# ==============================================================================
# 2. EXTRACT PAIRWISE CORRELATIONS FROM EACH STUDY
# ==============================================================================
message("\n--- Extracting pairwise correlations across studies ---")

# For each pair (i, j), extract available r values and sample sizes
pair_data <- list()
pair_idx <- 0

for (i in 1:(N_CONSTRUCTS - 1)) {
  for (j in (i + 1):N_CONSTRUCTS) {
    pair_idx <- pair_idx + 1
    c1 <- CONSTRUCTS[i]
    c2 <- CONSTRUCTS[j]
    pair_label <- paste0(c1, "-", c2)

    r_values <- c()
    n_values <- c()
    study_ids <- c()

    for (s in seq_along(cor_matrices)) {
      mat <- cor_matrices[[s]]
      if (c1 %in% rownames(mat) && c2 %in% colnames(mat)) {
        r_val <- mat[c1, c2]
        if (!is.na(r_val) && abs(r_val) < 1) {
          r_values <- c(r_values, r_val)
          n_values <- c(n_values, sample_sizes[s])
          study_ids <- c(study_ids, names(cor_matrices)[s])
        }
      }
    }

    pair_data[[pair_label]] <- list(
      construct1 = c1,
      construct2 = c2,
      label = pair_label,
      r = r_values,
      n = n_values,
      k = length(r_values),
      study_ids = study_ids
    )
  }
}

message(sprintf("  Extracted data for %d pairwise correlations", length(pair_data)))

# Report coverage
k_values <- sapply(pair_data, function(x) x$k)
message(sprintf("  Coverage: min k = %d, median k = %.0f, max k = %d",
                min(k_values), median(k_values), max(k_values)))
message(sprintf("  Pairs with k >= 3: %d / %d (%.0f%%)",
                sum(k_values >= 3), length(k_values),
                100 * sum(k_values >= 3) / length(k_values)))

# ==============================================================================
# 3. UNIVARIATE RANDOM-EFFECTS META-ANALYSIS FOR EACH PAIR
# ==============================================================================
message("\n--- Running univariate RE meta-analysis for each pair ---")

heterogeneity_table <- data.frame(
  Pair = character(),
  Construct1 = character(),
  Construct2 = character(),
  k = integer(),
  Total_N = integer(),
  Pooled_r = numeric(),
  SE = numeric(),
  CI_lower = numeric(),
  CI_upper = numeric(),
  PI_lower = numeric(),
  PI_upper = numeric(),
  tau2 = numeric(),
  tau = numeric(),
  I2 = numeric(),
  H2 = numeric(),
  Q = numeric(),
  Q_df = integer(),
  Q_p = numeric(),
  stringsAsFactors = FALSE
)

ma_models <- list()
n_analyzed <- 0
n_skipped <- 0

for (pair_label in names(pair_data)) {
  pd <- pair_data[[pair_label]]

  # Need at least 3 studies for meaningful MA
  if (pd$k < 3) {
    n_skipped <- n_skipped + 1
    next
  }

  tryCatch({
    # Fisher's z transformation
    zi <- atanh(pd$r)  # r-to-z
    vi <- 1 / (pd$n - 3)  # variance of z

    # Random-effects model using REML
    rma_fit <- rma(yi = zi, vi = vi, method = "REML",
                   measure = "ZCOR", slab = pd$study_ids)

    # Back-transform to correlation metric
    pooled_z <- as.numeric(rma_fit$beta)
    pooled_r <- tanh(pooled_z)  # z-to-r

    # SE in correlation metric (delta method approximation)
    se_z <- rma_fit$se
    se_r <- se_z * (1 - pooled_r^2)  # Approximate

    # CI (back-transformed)
    ci_z_lo <- rma_fit$ci.lb
    ci_z_hi <- rma_fit$ci.ub
    ci_r_lo <- tanh(ci_z_lo)
    ci_r_hi <- tanh(ci_z_hi)

    # Prediction interval (back-transformed)
    pi_z <- predict(rma_fit)
    pi_r_lo <- tanh(pi_z$pi.lb)
    pi_r_hi <- tanh(pi_z$pi.ub)

    # Heterogeneity statistics
    tau2 <- rma_fit$tau2
    tau <- sqrt(tau2)
    I2 <- rma_fit$I2
    H2 <- rma_fit$H2
    Q <- rma_fit$QE
    Q_df <- rma_fit$k - 1
    Q_p <- rma_fit$QEp

    # Store results
    row <- data.frame(
      Pair = pair_label,
      Construct1 = pd$construct1,
      Construct2 = pd$construct2,
      k = pd$k,
      Total_N = sum(pd$n),
      Pooled_r = round(pooled_r, 4),
      SE = round(se_r, 4),
      CI_lower = round(ci_r_lo, 4),
      CI_upper = round(ci_r_hi, 4),
      PI_lower = round(pi_r_lo, 4),
      PI_upper = round(pi_r_hi, 4),
      tau2 = round(tau2, 6),
      tau = round(tau, 4),
      I2 = round(I2, 1),
      H2 = round(H2, 2),
      Q = round(Q, 2),
      Q_df = Q_df,
      Q_p = round(Q_p, 6),
      stringsAsFactors = FALSE
    )

    heterogeneity_table <- rbind(heterogeneity_table, row)
    ma_models[[pair_label]] <- rma_fit
    n_analyzed <- n_analyzed + 1

  }, error = function(e) {
    message(sprintf("  WARNING: MA failed for %s: %s", pair_label, e$message))
    n_skipped <- n_skipped + 1
  })
}

message(sprintf("  Analyzed: %d pairs, Skipped: %d pairs (k < 3 or error)",
                n_analyzed, n_skipped))

# Sort by I2 (descending)
heterogeneity_table <- heterogeneity_table[order(-heterogeneity_table$I2), ]
rownames(heterogeneity_table) <- NULL

# ==============================================================================
# 4. HETEROGENEITY CLASSIFICATION
# ==============================================================================
message("\n--- Classifying heterogeneity levels ---")

heterogeneity_table$I2_class <- cut(
  heterogeneity_table$I2,
  breaks = c(-Inf, 25, 50, 75, Inf),
  labels = c("Low (<25%)", "Moderate (25-50%)", "Substantial (50-75%)", "High (>75%)")
)

# Summary by class
class_summary <- table(heterogeneity_table$I2_class)
message("  I-squared classification:")
for (cl in names(class_summary)) {
  message(sprintf("    %s: %d pairs (%.0f%%)",
                  cl, class_summary[cl],
                  100 * class_summary[cl] / nrow(heterogeneity_table)))
}

# High heterogeneity candidates for moderator analysis
high_het <- heterogeneity_table[heterogeneity_table$I2 > 75, ]
if (nrow(high_het) > 0) {
  message(sprintf("\n  %d pairs with HIGH heterogeneity (I2 > 75%%) — moderator candidates:",
                  nrow(high_het)))
  for (i in seq_len(min(nrow(high_het), 15))) {
    message(sprintf("    %s: r=%.3f, I2=%.1f%%, k=%d, PI=[%.3f, %.3f]",
                    high_het$Pair[i], high_het$Pooled_r[i], high_het$I2[i],
                    high_het$k[i], high_het$PI_lower[i], high_het$PI_upper[i]))
  }
}

# ==============================================================================
# 5. SUMMARY STATISTICS
# ==============================================================================
message("\n--- Overall heterogeneity summary ---")

message(sprintf("  Mean I2:   %.1f%% (SD = %.1f%%)",
                mean(heterogeneity_table$I2, na.rm = TRUE),
                sd(heterogeneity_table$I2, na.rm = TRUE)))
message(sprintf("  Median I2: %.1f%%",
                median(heterogeneity_table$I2, na.rm = TRUE)))
message(sprintf("  Mean tau:  %.4f (SD = %.4f)",
                mean(heterogeneity_table$tau, na.rm = TRUE),
                sd(heterogeneity_table$tau, na.rm = TRUE)))

# Significant Q-tests
sig_Q <- sum(heterogeneity_table$Q_p < .05, na.rm = TRUE)
message(sprintf("  Significant Q-tests: %d / %d (%.0f%%)",
                sig_Q, nrow(heterogeneity_table),
                100 * sig_Q / nrow(heterogeneity_table)))

# Prediction intervals crossing zero
pi_cross_zero <- sum(
  heterogeneity_table$PI_lower < 0 & heterogeneity_table$PI_upper > 0,
  na.rm = TRUE
)
message(sprintf("  Prediction intervals crossing zero: %d / %d",
                pi_cross_zero, nrow(heterogeneity_table)))

# ==============================================================================
# 6. TOP/BOTTOM CORRELATIONS TABLE
# ==============================================================================
message("\n--- Top 10 strongest pooled correlations ---")

sorted_by_r <- heterogeneity_table[order(-abs(heterogeneity_table$Pooled_r)), ]
message("  Pair             | r      | k  | I2     | 95% PI")
message("  -----------------+--------+----+--------+----------------")
for (i in seq_len(min(10, nrow(sorted_by_r)))) {
  row <- sorted_by_r[i, ]
  message(sprintf("  %-17s | %+.3f | %2d | %5.1f%% | [%+.3f, %+.3f]",
                  row$Pair, row$Pooled_r, row$k, row$I2,
                  row$PI_lower, row$PI_upper))
}

# ==============================================================================
# 7. VISUALIZATION: I-SQUARED HEATMAP
# ==============================================================================
message("\n--- Creating I-squared heatmap ---")

# Build I2 matrix
I2_matrix <- matrix(NA, nrow = N_CONSTRUCTS, ncol = N_CONSTRUCTS,
                    dimnames = list(CONSTRUCTS, CONSTRUCTS))
diag(I2_matrix) <- 0

for (i in seq_len(nrow(heterogeneity_table))) {
  c1 <- heterogeneity_table$Construct1[i]
  c2 <- heterogeneity_table$Construct2[i]
  I2_matrix[c1, c2] <- heterogeneity_table$I2[i]
  I2_matrix[c2, c1] <- heterogeneity_table$I2[i]
}

# Heatmap using ggplot2
I2_long <- expand.grid(Var1 = CONSTRUCTS, Var2 = CONSTRUCTS,
                       stringsAsFactors = FALSE)
I2_long$I2 <- sapply(seq_len(nrow(I2_long)), function(i) {
  I2_matrix[I2_long$Var1[i], I2_long$Var2[i]]
})
I2_long$Var1 <- factor(I2_long$Var1, levels = CONSTRUCTS)
I2_long$Var2 <- factor(I2_long$Var2, levels = rev(CONSTRUCTS))

p_heatmap <- ggplot(I2_long, aes(x = Var1, y = Var2, fill = I2)) +
  geom_tile(color = "white", linewidth = 0.5) +
  geom_text(aes(label = ifelse(is.na(I2) | Var1 == Var2, "",
                                sprintf("%.0f", I2))),
            size = 3, color = "black") +
  scale_fill_gradient2(
    low = "#2166AC", mid = "#FFFFBF", high = "#B2182B",
    midpoint = 50, na.value = "grey90",
    limits = c(0, 100),
    name = expression(I^2 ~ "(%)")
  ) +
  labs(
    title = expression("Heterogeneity Heatmap: " * I^2 * " Values for All 66 Pairwise Correlations"),
    x = "", y = ""
  ) +
  theme_minimal(base_size = 12) +
  theme(
    axis.text.x = element_text(angle = 45, hjust = 1, face = "bold"),
    axis.text.y = element_text(face = "bold"),
    plot.title = element_text(face = "bold", hjust = 0.5),
    panel.grid = element_blank()
  ) +
  coord_fixed()

ggsave(file.path(PATHS$figures, "heterogeneity_I2_heatmap.png"),
       p_heatmap, width = 10, height = 9, dpi = 300)
ggsave(file.path(PATHS$figures, "heterogeneity_I2_heatmap.pdf"),
       p_heatmap, width = 10, height = 9)
message("  Saved I2 heatmap")

# ==============================================================================
# 8. VISUALIZATION: I-SQUARED DISTRIBUTION
# ==============================================================================
message("\n--- Creating I-squared distribution plot ---")

p_dist <- ggplot(heterogeneity_table, aes(x = I2)) +
  geom_histogram(aes(y = after_stat(count)), bins = 20,
                 fill = "#4393C3", color = "white", alpha = 0.8) +
  geom_vline(xintercept = c(25, 50, 75), linetype = "dashed",
             color = c("green4", "orange", "red"), linewidth = 0.8) +
  annotate("text", x = 12.5, y = Inf, label = "Low", vjust = 2, color = "green4", size = 3.5) +
  annotate("text", x = 37.5, y = Inf, label = "Moderate", vjust = 2, color = "orange", size = 3.5) +
  annotate("text", x = 62.5, y = Inf, label = "Substantial", vjust = 2, color = "red3", size = 3.5) +
  annotate("text", x = 87.5, y = Inf, label = "High", vjust = 2, color = "red4", size = 3.5) +
  labs(
    title = expression("Distribution of " * I^2 * " Values Across 66 Pairwise Correlations"),
    x = expression(I^2 ~ "(%)"),
    y = "Count"
  ) +
  theme_minimal(base_size = 12) +
  theme(plot.title = element_text(face = "bold"))

ggsave(file.path(PATHS$figures, "heterogeneity_I2_distribution.png"),
       p_dist, width = 9, height = 6, dpi = 300)
ggsave(file.path(PATHS$figures, "heterogeneity_I2_distribution.pdf"),
       p_dist, width = 9, height = 6)
message("  Saved I2 distribution plot")

# ==============================================================================
# 9. PREDICTION INTERVAL PLOT
# ==============================================================================
message("\n--- Creating prediction interval plot ---")

# Show top 20 pairs by k (most frequently reported)
top_pairs <- heterogeneity_table[order(-heterogeneity_table$k), ]
top_pairs <- head(top_pairs, 20)
top_pairs <- top_pairs[order(top_pairs$Pooled_r), ]
top_pairs$Pair <- factor(top_pairs$Pair, levels = top_pairs$Pair)

p_pi <- ggplot(top_pairs, aes(x = Pooled_r, y = Pair)) +
  # Prediction interval (wider)
  geom_errorbarh(aes(xmin = PI_lower, xmax = PI_upper),
                 height = 0.3, color = "#D6604D", linewidth = 0.6) +
  # Confidence interval (narrower)
  geom_errorbarh(aes(xmin = CI_lower, xmax = CI_upper),
                 height = 0.15, color = "#2166AC", linewidth = 1) +
  # Point estimate
  geom_point(size = 2.5, color = "black") +
  geom_vline(xintercept = 0, linetype = "dashed", color = "grey50") +
  # Annotate with k and I2
  geom_text(aes(label = sprintf("k=%d, I2=%.0f%%", k, I2)),
            x = max(top_pairs$PI_upper, na.rm = TRUE) + 0.02,
            hjust = 0, size = 3) +
  labs(
    title = "Pooled Correlations with 95% CI and Prediction Intervals",
    subtitle = "Top 20 most frequently reported pairs",
    x = "Correlation (r)",
    y = "Construct Pair"
  ) +
  theme_minimal(base_size = 11) +
  theme(
    plot.title = element_text(face = "bold"),
    axis.text.y = element_text(size = 9)
  ) +
  xlim(min(top_pairs$PI_lower, na.rm = TRUE) - 0.05,
       max(top_pairs$PI_upper, na.rm = TRUE) + 0.15)

ggsave(file.path(PATHS$figures, "heterogeneity_prediction_intervals.png"),
       p_pi, width = 11, height = 8, dpi = 300)
ggsave(file.path(PATHS$figures, "heterogeneity_prediction_intervals.pdf"),
       p_pi, width = 11, height = 8)
message("  Saved prediction interval plot")

# ==============================================================================
# 10. SAVE RESULTS
# ==============================================================================
message("\n--- Saving heterogeneity results ---")

het_results <- list(
  heterogeneity_table = heterogeneity_table,
  ma_models = ma_models,
  pair_data = pair_data,
  I2_matrix = I2_matrix,
  high_heterogeneity_pairs = high_het,
  summary = list(
    n_analyzed = n_analyzed,
    n_skipped = n_skipped,
    mean_I2 = mean(heterogeneity_table$I2, na.rm = TRUE),
    median_I2 = median(heterogeneity_table$I2, na.rm = TRUE),
    mean_tau = mean(heterogeneity_table$tau, na.rm = TRUE),
    n_high_I2 = nrow(high_het),
    pct_sig_Q = 100 * sig_Q / nrow(heterogeneity_table),
    n_PI_cross_zero = pi_cross_zero
  )
)

saveRDS(het_results, file.path(PATHS$output, "heterogeneity_results.rds"))
message(sprintf("  Saved to: %s", file.path(PATHS$output, "heterogeneity_results.rds")))

write.csv(heterogeneity_table,
          file.path(PATHS$output, "heterogeneity_table.csv"),
          row.names = FALSE)
message(sprintf("  Table saved to: %s", file.path(PATHS$output, "heterogeneity_table.csv")))

message("\n", strrep("=", 70))
message("08: HETEROGENEITY DECOMPOSITION COMPLETE")
message(strrep("=", 70))
