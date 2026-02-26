# =============================================================================
# Paper B: IRR Calculation Template
# LLM-Assisted Data Extraction for MASEM
# Author: Hosung You
# =============================================================================

# Required packages
library(irr)        # Cohen's kappa, ICC
library(irrCAC)     # Gwet's AC2
library(tidyverse)  # Data manipulation
library(readr)      # CSV reading

# =============================================================================
# 1. Load Data
# =============================================================================

# Human coder data
coder1 <- read_csv("../data/03_human_coding/coder1_PI/coding_sheet_H1.csv")
coder2 <- read_csv("../data/03_human_coding/coder2_phd1/coding_sheet_H2.csv")

# Gold standard (after discrepancy resolution)
gold <- read_csv("../data/05_gold_standard/gold_standard_100.csv")

# AI extraction data
ai_claude <- read_csv("../data/02_ai_extraction/claude/claude_combined.csv")
ai_codex  <- read_csv("../data/02_ai_extraction/codex/codex_combined.csv")
ai_gemini <- read_csv("../data/02_ai_extraction/gemini/gemini_combined.csv")

# =============================================================================
# 2. Define Variable Types
# =============================================================================

categorical_vars <- c(
  "study_design", "matrix_type", "ai_tool_type",
  "education_level", "region", "subject_area", "mandatory_voluntary"
)

continuous_vars <- c(
  "sample_size_n", "num_constructs_reported",
  grep("^r_", names(coder1), value = TRUE)  # All correlation pairs
)

# =============================================================================
# 3. Human IRR (H1 vs H2) — Phase 1
# =============================================================================

irr_results <- tibble(
  variable = character(),
  var_type = character(),
  metric = character(),
  value = numeric(),
  ci_lower = numeric(),
  ci_upper = numeric(),
  n_pairs = integer()
)

# 3.1 Categorical variables — Cohen's kappa + Gwet's AC2
for (var in categorical_vars) {
  # Cohen's kappa
  ratings <- data.frame(
    coder1 = coder1[[var]],
    coder2 = coder2[[var]]
  )
  ratings_complete <- ratings[complete.cases(ratings), ]

  if (nrow(ratings_complete) >= 10) {
    kappa_result <- kappa2(ratings_complete)

    irr_results <- irr_results %>%
      add_row(
        variable = var,
        var_type = "categorical",
        metric = "cohens_kappa",
        value = kappa_result$value,
        ci_lower = NA_real_,  # kappa2 doesn't provide CI directly
        ci_upper = NA_real_,
        n_pairs = nrow(ratings_complete)
      )

    # Gwet's AC2 (handles kappa paradox)
    ac2_result <- gwet.ac1.raw(ratings_complete)

    irr_results <- irr_results %>%
      add_row(
        variable = var,
        var_type = "categorical",
        metric = "gwet_ac2",
        value = ac2_result$est$coefficient,
        ci_lower = ac2_result$est$conf.int[1],
        ci_upper = ac2_result$est$conf.int[2],
        n_pairs = nrow(ratings_complete)
      )
  }
}

# 3.2 Continuous variables — ICC(2,1)
for (var in continuous_vars) {
  ratings <- data.frame(
    coder1 = as.numeric(coder1[[var]]),
    coder2 = as.numeric(coder2[[var]])
  )
  ratings_complete <- ratings[complete.cases(ratings), ]

  if (nrow(ratings_complete) >= 10) {
    icc_result <- icc(ratings_complete, model = "twoway", type = "agreement",
                      unit = "single")

    irr_results <- irr_results %>%
      add_row(
        variable = var,
        var_type = "continuous",
        metric = "icc_2_1",
        value = icc_result$value,
        ci_lower = icc_result$lbound,
        ci_upper = icc_result$ubound,
        n_pairs = nrow(ratings_complete)
      )

    # MAE
    mae <- mean(abs(ratings_complete$coder1 - ratings_complete$coder2), na.rm = TRUE)

    irr_results <- irr_results %>%
      add_row(
        variable = var,
        var_type = "continuous",
        metric = "mae",
        value = mae,
        ci_lower = NA_real_,
        ci_upper = NA_real_,
        n_pairs = nrow(ratings_complete)
      )
  }
}

# =============================================================================
# 4. AI vs Gold Standard — Per Model
# =============================================================================

ai_models <- list(
  claude = ai_claude,
  codex = ai_codex,
  gemini = ai_gemini
)

ai_accuracy <- tibble(
  model = character(),
  variable = character(),
  var_type = character(),
  metric = character(),
  value = numeric(),
  n_pairs = integer()
)

for (model_name in names(ai_models)) {
  ai_data <- ai_models[[model_name]]

  # Categorical: kappa
  for (var in categorical_vars) {
    ratings <- data.frame(
      ai = ai_data[[var]],
      gold = gold[[var]]
    )
    ratings_complete <- ratings[complete.cases(ratings), ]

    if (nrow(ratings_complete) >= 10) {
      kappa_result <- kappa2(ratings_complete)

      ai_accuracy <- ai_accuracy %>%
        add_row(
          model = model_name,
          variable = var,
          var_type = "categorical",
          metric = "cohens_kappa",
          value = kappa_result$value,
          n_pairs = nrow(ratings_complete)
        )

      # Accuracy (%)
      accuracy <- mean(ratings_complete$ai == ratings_complete$gold)

      ai_accuracy <- ai_accuracy %>%
        add_row(
          model = model_name,
          variable = var,
          var_type = "categorical",
          metric = "accuracy_pct",
          value = accuracy * 100,
          n_pairs = nrow(ratings_complete)
        )
    }
  }

  # Continuous: ICC + MAE
  for (var in continuous_vars) {
    ratings <- data.frame(
      ai = as.numeric(ai_data[[var]]),
      gold = as.numeric(gold[[var]])
    )
    ratings_complete <- ratings[complete.cases(ratings), ]

    if (nrow(ratings_complete) >= 10) {
      icc_result <- icc(ratings_complete, model = "twoway", type = "agreement",
                        unit = "single")

      ai_accuracy <- ai_accuracy %>%
        add_row(
          model = model_name,
          variable = var,
          var_type = "continuous",
          metric = "icc_2_1",
          value = icc_result$value,
          n_pairs = nrow(ratings_complete)
        )

      mae <- mean(abs(ratings_complete$ai - ratings_complete$gold), na.rm = TRUE)

      ai_accuracy <- ai_accuracy %>%
        add_row(
          model = model_name,
          variable = var,
          var_type = "continuous",
          metric = "mae",
          value = mae,
          n_pairs = nrow(ratings_complete)
        )
    }
  }
}

# =============================================================================
# 5. Save Results
# =============================================================================

write_csv(irr_results, "../data/06_analysis/irr_results.csv")
write_csv(ai_accuracy, "../data/06_analysis/model_accuracy.csv")

# =============================================================================
# 6. Summary Report
# =============================================================================

cat("\n========== HUMAN IRR SUMMARY ==========\n")
irr_results %>%
  filter(metric %in% c("cohens_kappa", "icc_2_1")) %>%
  group_by(var_type, metric) %>%
  summarise(
    mean_value = mean(value, na.rm = TRUE),
    min_value = min(value, na.rm = TRUE),
    max_value = max(value, na.rm = TRUE),
    n_vars = n(),
    .groups = "drop"
  ) %>%
  print()

cat("\n========== AI ACCURACY SUMMARY ==========\n")
ai_accuracy %>%
  filter(metric %in% c("cohens_kappa", "icc_2_1", "accuracy_pct")) %>%
  group_by(model, var_type, metric) %>%
  summarise(
    mean_value = mean(value, na.rm = TRUE),
    min_value = min(value, na.rm = TRUE),
    max_value = max(value, na.rm = TRUE),
    n_vars = n(),
    .groups = "drop"
  ) %>%
  print()
