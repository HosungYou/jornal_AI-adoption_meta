#!/usr/bin/env Rscript
# =============================================================================
# Paper B: Full Analysis Script
# LLM-Assisted Data Extraction for MASEM
# Author: Hosung You
# =============================================================================

# ── Load packages ──────────────────────────────────────────────────────────────
library(irr)
library(irrCAC)
library(caret)
library(ggplot2)
library(pheatmap)
library(tidyverse)
library(readr)
library(jsonlite)

# ── Configuration ──────────────────────────────────────────────────────────────
DATA_DIR <- file.path(dirname(getwd()), "data")
OUTPUT_DIR <- file.path(DATA_DIR, "06_analysis")
FIG_DIR <- file.path(OUTPUT_DIR, "figures")
dir.create(FIG_DIR, recursive = TRUE, showWarnings = FALSE)

# ── Variable definitions ──────────────────────────────────────────────────────
CATEGORICAL_VARS <- c(
  "study_design", "matrix_type", "ai_tool_type",
  "education_level", "region", "subject_area", "mandatory_voluntary"
)

# Correlation pairs (dynamically detected)
# Will be populated after loading data

# =============================================================================
# RQ1: Per-Model Accuracy
# =============================================================================

run_rq1 <- function(gold, ai_claude, ai_codex, ai_gemini) {
  cat("\n========== RQ1: Per-Model Accuracy ==========\n")

  models <- list(
    claude = ai_claude,
    codex = ai_codex,
    gemini = ai_gemini
  )

  results <- list()

  for (model_name in names(models)) {
    ai <- models[[model_name]]
    model_results <- tibble()

    # Categorical variables
    for (var in CATEGORICAL_VARS) {
      if (var %in% names(ai) & var %in% names(gold)) {
        ratings <- data.frame(ai = ai[[var]], gold = gold[[var]])
        ratings <- ratings[complete.cases(ratings), ]
        if (nrow(ratings) >= 5) {
          k <- tryCatch(kappa2(ratings)$value, error = function(e) NA)
          acc <- mean(ratings$ai == ratings$gold, na.rm = TRUE) * 100
          model_results <- bind_rows(model_results, tibble(
            model = model_name, variable = var, var_type = "categorical",
            kappa = k, icc = NA, mae = NA, accuracy_pct = acc, n = nrow(ratings)
          ))
        }
      }
    }

    # Continuous variables (correlations)
    r_vars <- grep("^r_", names(gold), value = TRUE)
    for (var in r_vars) {
      if (var %in% names(ai)) {
        ratings <- data.frame(
          ai = as.numeric(ai[[var]]),
          gold = as.numeric(gold[[var]])
        )
        ratings <- ratings[complete.cases(ratings), ]
        if (nrow(ratings) >= 5) {
          icc_val <- tryCatch(
            icc(ratings, model = "twoway", type = "agreement", unit = "single")$value,
            error = function(e) NA
          )
          mae_val <- mean(abs(ratings$ai - ratings$gold), na.rm = TRUE)
          model_results <- bind_rows(model_results, tibble(
            model = model_name, variable = var, var_type = "continuous",
            kappa = NA, icc = icc_val, mae = mae_val,
            accuracy_pct = NA, n = nrow(ratings)
          ))
        }
      }
    }

    results[[model_name]] <- model_results
  }

  all_results <- bind_rows(results)
  write_csv(all_results, file.path(OUTPUT_DIR, "rq1_model_accuracy.csv"))
  cat("RQ1 results saved.\n")
  return(all_results)
}

# =============================================================================
# RQ2: Accuracy by Variable Type
# =============================================================================

run_rq2 <- function(rq1_results) {
  cat("\n========== RQ2: Variable Type Analysis ==========\n")

  # Classify variable types
  rq2 <- rq1_results %>%
    mutate(var_category = case_when(
      variable %in% c("first_author", "year", "journal", "doi",
                       "country", "sample_size_n", "study_design",
                       "sample_description") ~ "bibliographic",
      grepl("^r_", variable) ~ "statistical",
      TRUE ~ "classificatory"
    ))

  # Summary by type
  type_summary <- rq2 %>%
    group_by(model, var_category) %>%
    summarise(
      mean_kappa = mean(kappa, na.rm = TRUE),
      mean_icc = mean(icc, na.rm = TRUE),
      mean_mae = mean(mae, na.rm = TRUE),
      mean_accuracy = mean(accuracy_pct, na.rm = TRUE),
      n_vars = n(),
      .groups = "drop"
    )

  write_csv(type_summary, file.path(OUTPUT_DIR, "rq2_variable_type_accuracy.csv"))

  # Kruskal-Wallis test
  cat("\nKruskal-Wallis test (accuracy by variable type):\n")
  for (m in unique(rq2$model)) {
    model_data <- rq2 %>% filter(model == m, !is.na(accuracy_pct))
    if (nrow(model_data) > 0 & length(unique(model_data$var_category)) > 1) {
      kw <- kruskal.test(accuracy_pct ~ var_category, data = model_data)
      cat(sprintf("  %s: chi2=%.2f, df=%d, p=%.4f\n",
                  m, kw$statistic, kw$parameter, kw$p.value))
    }
  }

  cat("RQ2 results saved.\n")
  return(rq2)
}

# =============================================================================
# RQ3: Multi-Model Consensus
# =============================================================================

run_rq3 <- function(gold, ai_claude, ai_codex, ai_gemini) {
  cat("\n========== RQ3: Multi-Model Consensus ==========\n")

  consensus_results <- tibble()

  # Categorical: majority vote
  for (var in CATEGORICAL_VARS) {
    if (all(c(var) %in% names(ai_claude), var %in% names(ai_codex), var %in% names(ai_gemini))) {
      votes <- data.frame(
        claude = ai_claude[[var]],
        codex = ai_codex[[var]],
        gemini = ai_gemini[[var]],
        gold = gold[[var]]
      )
      votes <- votes[complete.cases(votes), ]

      if (nrow(votes) > 0) {
        # Majority vote
        majority <- apply(votes[, 1:3], 1, function(x) {
          tab <- table(x)
          if (max(tab) >= 2) names(tab)[which.max(tab)] else NA
        })

        acc <- mean(majority == votes$gold, na.rm = TRUE) * 100
        agreement <- mean(!is.na(majority)) * 100

        consensus_results <- bind_rows(consensus_results, tibble(
          variable = var, var_type = "categorical",
          consensus_method = "majority_vote",
          accuracy_pct = acc, agreement_pct = agreement, n = nrow(votes)
        ))
      }
    }
  }

  # Continuous: median
  r_vars <- grep("^r_", names(gold), value = TRUE)
  for (var in r_vars) {
    if (all(var %in% names(ai_claude), var %in% names(ai_codex), var %in% names(ai_gemini))) {
      vals <- data.frame(
        claude = as.numeric(ai_claude[[var]]),
        codex = as.numeric(ai_codex[[var]]),
        gemini = as.numeric(ai_gemini[[var]]),
        gold = as.numeric(gold[[var]])
      )
      vals <- vals[complete.cases(vals), ]

      if (nrow(vals) > 0) {
        median_val <- apply(vals[, 1:3], 1, median)
        mae <- mean(abs(median_val - vals$gold))
        icc_val <- tryCatch(
          icc(data.frame(consensus = median_val, gold = vals$gold),
              model = "twoway", type = "agreement", unit = "single")$value,
          error = function(e) NA
        )

        consensus_results <- bind_rows(consensus_results, tibble(
          variable = var, var_type = "continuous",
          consensus_method = "median",
          accuracy_pct = NA, agreement_pct = NA, n = nrow(vals),
          icc = icc_val, mae = mae
        ))
      }
    }
  }

  write_csv(consensus_results, file.path(OUTPUT_DIR, "rq3_consensus_accuracy.csv"))
  cat("RQ3 results saved.\n")
  return(consensus_results)
}

# =============================================================================
# Figure 1: Heatmap
# =============================================================================

create_heatmap <- function(rq1_results) {
  cat("\nCreating heatmap (Figure 1)...\n")

  # Use accuracy for categorical, ICC for continuous
  plot_data <- rq1_results %>%
    mutate(performance = coalesce(accuracy_pct / 100, icc)) %>%
    select(model, variable, performance) %>%
    pivot_wider(names_from = model, values_from = performance) %>%
    column_to_rownames("variable")

  if (nrow(plot_data) > 0 & ncol(plot_data) > 0) {
    pdf(file.path(FIG_DIR, "fig1_heatmap.pdf"), width = 10, height = 14)
    pheatmap(
      as.matrix(plot_data),
      color = colorRampPalette(c("#D73027", "#FFFFBF", "#1A9850"))(100),
      breaks = seq(0, 1, length.out = 101),
      cluster_rows = TRUE,
      cluster_cols = FALSE,
      display_numbers = TRUE,
      number_format = "%.2f",
      fontsize = 8,
      main = "Figure 1. AI Model Accuracy by Variable\n(Accuracy/100 for categorical, ICC for continuous)"
    )
    dev.off()
    cat("  Saved fig1_heatmap.pdf\n")
  }
}

# =============================================================================
# Figure 2: Bland-Altman Plots
# =============================================================================

create_bland_altman <- function(gold, ai_claude, ai_codex, ai_gemini) {
  cat("Creating Bland-Altman plots (Figure 2)...\n")

  models <- list(
    "Claude Sonnet 4.6" = ai_claude,
    "GPT Codex 5.3" = ai_codex,
    "Gemini CLI" = ai_gemini
  )

  r_vars <- grep("^r_", names(gold), value = TRUE)

  ba_data <- tibble()

  for (model_name in names(models)) {
    ai <- models[[model_name]]
    for (var in r_vars) {
      if (var %in% names(ai)) {
        ai_val <- as.numeric(ai[[var]])
        gold_val <- as.numeric(gold[[var]])
        complete <- !is.na(ai_val) & !is.na(gold_val)
        if (sum(complete) > 0) {
          ba_data <- bind_rows(ba_data, tibble(
            model = model_name,
            variable = var,
            mean_val = (ai_val[complete] + gold_val[complete]) / 2,
            diff = ai_val[complete] - gold_val[complete]
          ))
        }
      }
    }
  }

  if (nrow(ba_data) > 0) {
    p <- ggplot(ba_data, aes(x = mean_val, y = diff)) +
      geom_point(alpha = 0.3, size = 1) +
      geom_hline(yintercept = 0, linetype = "solid", color = "black") +
      stat_summary(fun = mean, geom = "hline", aes(yintercept = after_stat(y)),
                   linetype = "dashed", color = "blue") +
      facet_wrap(~ model, ncol = 1) +
      labs(
        title = "Figure 2. Bland-Altman Plots: AI vs. Gold Standard",
        subtitle = "Correlation coefficient extraction",
        x = "Mean of AI and Gold Standard",
        y = "Difference (AI - Gold Standard)"
      ) +
      theme_minimal() +
      theme(strip.text = element_text(face = "bold"))

    ggsave(file.path(FIG_DIR, "fig2_bland_altman.pdf"), p,
           width = 8, height = 10, dpi = 300)
    cat("  Saved fig2_bland_altman.pdf\n")
  }
}

# =============================================================================
# Main Execution
# =============================================================================

main <- function() {
  cat("Paper B Analysis Script\n")
  cat(paste("Date:", Sys.time(), "\n"))
  cat(paste("Working directory:", getwd(), "\n"))

  # Check if data exists
  gold_file <- file.path(DATA_DIR, "05_gold_standard", "gold_standard_100.csv")
  if (!file.exists(gold_file)) {
    cat("\nERROR: Gold standard file not found at", gold_file, "\n")
    cat("Please complete Phase 1 coding before running analysis.\n")
    return(invisible(NULL))
  }

  # Load data
  gold <- read_csv(gold_file, show_col_types = FALSE)
  ai_claude <- read_csv(file.path(DATA_DIR, "02_ai_extraction/claude/claude_combined.csv"),
                         show_col_types = FALSE)
  ai_codex <- read_csv(file.path(DATA_DIR, "02_ai_extraction/codex/codex_combined.csv"),
                        show_col_types = FALSE)
  ai_gemini <- read_csv(file.path(DATA_DIR, "02_ai_extraction/gemini/gemini_combined.csv"),
                         show_col_types = FALSE)

  # Run analyses
  rq1 <- run_rq1(gold, ai_claude, ai_codex, ai_gemini)
  rq2 <- run_rq2(rq1)
  rq3 <- run_rq3(gold, ai_claude, ai_codex, ai_gemini)

  # Create figures
  create_heatmap(rq1)
  create_bland_altman(gold, ai_claude, ai_codex, ai_gemini)

  cat("\n========== ANALYSIS COMPLETE ==========\n")
  cat(paste("Output directory:", OUTPUT_DIR, "\n"))
}

# Run
main()
