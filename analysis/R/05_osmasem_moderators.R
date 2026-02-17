# ==============================================================================
# 05_osmasem_moderators.R — One-Stage MASEM Moderator Analysis
# Educational AI Adoption MASEM Meta-Analysis
# ==============================================================================
# Purpose: Test categorical and continuous moderators using OSMASEM (Jak & Cheung, 2020)
#   - Education level (K-12, undergraduate, graduate, mixed)
#   - User role (student, instructor, administrator, mixed)
#   - Discipline (STEM, humanities, social_science, health_science, mixed)
#   - AI tool type (chatbot_LLM, ITS, LMS_AI, auto_grading, writing_assistant, adaptive_learning, general)
#   - Institutional type (public, private, online, community_college, mixed)
#   - Culture score (Hofstede individualism)
#   - Publication year (centered)
#   - Sample size as artifact moderator
# Dependencies: 00_setup.R, prepared_data.rds, study_metadata
# Output: osmasem_moderator_results.rds, coefficient tables
# ==============================================================================

source("analysis/R/00_setup.R")
message("\n", strrep("=", 70))
message("05: ONE-STAGE MASEM — MODERATOR ANALYSIS")
message(strrep("=", 70))

# ==============================================================================
# 1. LOAD DATA
# ==============================================================================
message("\n--- Loading prepared data ---")
prepared <- readRDS(file.path(PATHS$pooled, "prepared_data.rds"))
stage1   <- readRDS(file.path(PATHS$pooled, "stage1_results.rds"))

cor_matrices <- prepared$cor_matrices
sample_sizes <- prepared$sample_sizes
metadata     <- prepared$study_metadata

message(sprintf("  Studies: %d", length(cor_matrices)))
message(sprintf("  Constructs: %d | Pairs: %d", N_CONSTRUCTS, N_PAIRS))

# ==============================================================================
# 2. PREPARE OSMASEM DATA
# ==============================================================================
message("\n--- Preparing OSMASEM data structure ---")

# Convert correlation matrices to the format required by osmasem()
# Each study needs a vectorized lower-triangle correlation + sample size
# metaSEM uses Corr() and create.mxMatrix() internally

# Build the data frame for osmasem: each row = one study
# Columns: correlation elements (named e.g., "PE_EE", "PE_SI", ...) and sample size n
pair_names <- c()
for (i in 1:(N_CONSTRUCTS - 1)) {
  for (j in (i + 1):N_CONSTRUCTS) {
    pair_names <- c(pair_names, paste0(CONSTRUCTS[i], "_", CONSTRUCTS[j]))
  }
}

osmasem_data <- data.frame(matrix(NA, nrow = length(cor_matrices), ncol = N_PAIRS + 1))
colnames(osmasem_data) <- c(pair_names, "n")

for (s in seq_along(cor_matrices)) {
  mat <- cor_matrices[[s]]
  idx <- 1
  for (i in 1:(N_CONSTRUCTS - 1)) {
    for (j in (i + 1):N_CONSTRUCTS) {
      if (CONSTRUCTS[i] %in% rownames(mat) && CONSTRUCTS[j] %in% colnames(mat)) {
        osmasem_data[s, idx] <- mat[CONSTRUCTS[i], CONSTRUCTS[j]]
      }
      idx <- idx + 1
    }
  }
  osmasem_data$n[s] <- sample_sizes[s]
}
rownames(osmasem_data) <- names(cor_matrices)

message(sprintf("  OSMASEM data: %d studies x %d columns", nrow(osmasem_data), ncol(osmasem_data)))

# ==============================================================================
# 3. EXTRACT MODERATOR VARIABLES
# ==============================================================================
message("\n--- Extracting moderator variables ---")

# Education level (categorical)
if ("education_level" %in% colnames(metadata)) {
  osmasem_data$education_level <- metadata$education_level
  message(sprintf("  Education level: %s",
                  paste(table(osmasem_data$education_level), collapse = ", ")))
} else {
  warning("  'education_level' column not found in metadata.")
  osmasem_data$education_level <- NA
}

# User role (categorical)
if ("user_role" %in% colnames(metadata)) {
  osmasem_data$user_role <- metadata$user_role
  message(sprintf("  User role: %s",
                  paste(table(osmasem_data$user_role), collapse = ", ")))
} else {
  warning("  'user_role' column not found in metadata.")
  osmasem_data$user_role <- NA
}

# Discipline (categorical)
if ("discipline" %in% colnames(metadata)) {
  osmasem_data$discipline <- metadata$discipline
  message(sprintf("  Discipline: %s",
                  paste(table(osmasem_data$discipline), collapse = ", ")))
} else {
  warning("  'discipline' column not found in metadata.")
  osmasem_data$discipline <- NA
}

# AI tool type (categorical)
if ("ai_tool_type" %in% colnames(metadata)) {
  osmasem_data$ai_tool_type <- metadata$ai_tool_type
  message(sprintf("  AI tool type: %s",
                  paste(table(osmasem_data$ai_tool_type), collapse = ", ")))
} else {
  warning("  'ai_tool_type' column not found in metadata.")
  osmasem_data$ai_tool_type <- NA
}

# Institutional type (categorical)
if ("institutional_type" %in% colnames(metadata)) {
  osmasem_data$institutional_type <- metadata$institutional_type
  message(sprintf("  Institutional type: %s",
                  paste(table(osmasem_data$institutional_type), collapse = ", ")))
} else {
  warning("  'institutional_type' column not found in metadata.")
  osmasem_data$institutional_type <- NA
}

# Publication year (centered at grand mean)
if ("year" %in% colnames(metadata)) {
  pub_year <- metadata$year
  year_mean <- mean(pub_year, na.rm = TRUE)
  osmasem_data$year_c <- pub_year - year_mean
  message(sprintf("  Publication year: range %d-%d, centered at %.1f",
                  min(pub_year, na.rm = TRUE), max(pub_year, na.rm = TRUE), year_mean))
} else {
  warning("  'year' column not found in metadata. Skipping year moderator.")
  osmasem_data$year_c <- NA
}

# Culture score (Hofstede individualism)
if ("culture_score" %in% colnames(metadata)) {
  osmasem_data$culture_score <- metadata$culture_score
  message(sprintf("  Culture score (Hofstede): M = %.1f, SD = %.1f, range %d-%d",
                  mean(osmasem_data$culture_score, na.rm = TRUE),
                  sd(osmasem_data$culture_score, na.rm = TRUE),
                  min(osmasem_data$culture_score, na.rm = TRUE),
                  max(osmasem_data$culture_score, na.rm = TRUE)))
} else {
  warning("  'culture_score' column not found in metadata. Skipping culture moderator.")
  osmasem_data$culture_score <- NA
}

# Sample size (log-transformed, centered)
osmasem_data$log_n_c <- log(osmasem_data$n) - mean(log(osmasem_data$n), na.rm = TRUE)
message(sprintf("  Log sample size (centered): M = 0.00, SD = %.2f",
                sd(osmasem_data$log_n_c, na.rm = TRUE)))

# ==============================================================================
# 4. DEFINE THE INTEGRATED MODEL (RAM Specification)
# ==============================================================================
message("\n--- Defining the integrated TSSEM model for OSMASEM ---")

# The model: same as the Integrated model (Model 2) from 04_tssem_models.R
# Paths based on the 12-construct Integrated Model

# A matrix: asymmetric (directed) paths
A_model <- create.mxMatrix(
  c(
    # Row = DV, Col = IV: A[DV, IV] = path from IV to DV
    # BI paths (row 5)
    "0.1*PE_BI",    # PE -> BI
    "0.1*EE_BI",    # EE -> BI
    "0.1*SI_BI",    # SI -> BI
    "0.1*ATT_BI",   # ATT -> BI
    "0.1*TRU_BI",   # TRU -> BI
    "0.1*ANX_BI",   # ANX -> BI
    # UB paths (row 6)
    "0.1*BI_UB",    # BI -> UB
    "0.1*FC_UB",    # FC -> UB
    # ATT paths (row 7)
    "0.1*PE_ATT",   # PE -> ATT
    "0.1*EE_ATT",   # EE -> ATT
    # TRU paths (row 9)
    "0.1*TRA_TRU",  # TRA -> TRU
    # EE path (row 2)
    "0.1*SE_EE",    # SE -> EE
    # ANX path (row 10)
    "0.1*AUT_ANX",  # AUT -> ANX
    "0.1*SE_ANX"    # SE -> ANX (negative expected)
  ),
  type = "Full",
  nrow = N_CONSTRUCTS,
  ncol = N_CONSTRUCTS,
  byrow = FALSE,
  name = "A"
)

# Map the labels to specific matrix positions
# Order: PE(1), EE(2), SI(3), FC(4), BI(5), UB(6), ATT(7), SE(8), TRU(9), ANX(10), TRA(11), AUT(12)
A_spec <- matrix(0, nrow = N_CONSTRUCTS, ncol = N_CONSTRUCTS)
rownames(A_spec) <- colnames(A_spec) <- CONSTRUCTS

# Set path positions
A_labels <- matrix("0", nrow = N_CONSTRUCTS, ncol = N_CONSTRUCTS)
rownames(A_labels) <- colnames(A_labels) <- CONSTRUCTS

# BI predicted by PE, EE, SI, ATT, TRU, ANX
A_labels["BI", "PE"]  <- "0.1*PE_BI"
A_labels["BI", "EE"]  <- "0.1*EE_BI"
A_labels["BI", "SI"]  <- "0.1*SI_BI"
A_labels["BI", "ATT"] <- "0.1*ATT_BI"
A_labels["BI", "TRU"] <- "0.1*TRU_BI"
A_labels["BI", "ANX"] <- "0.1*ANX_BI"
# UB predicted by BI, FC
A_labels["UB", "BI"]  <- "0.1*BI_UB"
A_labels["UB", "FC"]  <- "0.1*FC_UB"
# ATT predicted by PE, EE
A_labels["ATT", "PE"] <- "0.1*PE_ATT"
A_labels["ATT", "EE"] <- "0.1*EE_ATT"
# TRU predicted by TRA
A_labels["TRU", "TRA"] <- "0.1*TRA_TRU"
# EE predicted by SE
A_labels["EE", "SE"]  <- "0.1*SE_EE"
# ANX predicted by AUT, SE
A_labels["ANX", "AUT"] <- "0.1*AUT_ANX"
A_labels["ANX", "SE"]  <- "0.1*SE_ANX"

# S matrix: symmetric (covariances among exogenous variables + residual variances)
# Exogenous: PE, SI, FC, SE, TRA, AUT
# Endogenous: EE, BI, UB, ATT, TRU, ANX (have residual variances)

# For OSMASEM, we use RAM specification via create.mxMatrix
# Build the A and S matrices explicitly for use with osmasem()

RAM_A <- matrix(
  c(
    # PE  EE    SI   FC    BI    UB   ATT   SE    TRU   ANX   TRA   AUT
    # PE row
    0,    0,    0,   0,    0,    0,   0,    0,    0,    0,    0,    0,
    # EE row: SE->EE
    0,    0,    0,   0,    0,    0,   0,   "0.1*SE_EE", 0, 0, 0,   0,
    # SI row
    0,    0,    0,   0,    0,    0,   0,    0,    0,    0,    0,    0,
    # FC row
    0,    0,    0,   0,    0,    0,   0,    0,    0,    0,    0,    0,
    # BI row: PE,EE,SI,ATT,TRU,ANX -> BI
    "0.1*PE_BI","0.1*EE_BI","0.1*SI_BI",0,0,0,"0.1*ATT_BI",0,"0.1*TRU_BI","0.1*ANX_BI",0,0,
    # UB row: BI,FC -> UB
    0,    0,    0,  "0.1*FC_UB","0.1*BI_UB",0,0, 0,    0,    0,    0,    0,
    # ATT row: PE,EE -> ATT
    "0.1*PE_ATT","0.1*EE_ATT",0,0,0,0,0,  0,    0,    0,    0,    0,
    # SE row
    0,    0,    0,   0,    0,    0,   0,    0,    0,    0,    0,    0,
    # TRU row: TRA -> TRU
    0,    0,    0,   0,    0,    0,   0,    0,    0,    0, "0.1*TRA_TRU", 0,
    # ANX row: AUT,SE -> ANX
    0,    0,    0,   0,    0,    0,   0, "0.1*SE_ANX", 0, 0, 0, "0.1*AUT_ANX",
    # TRA row
    0,    0,    0,   0,    0,    0,   0,    0,    0,    0,    0,    0,
    # AUT row
    0,    0,    0,   0,    0,    0,   0,    0,    0,    0,    0,    0
  ),
  nrow = N_CONSTRUCTS, ncol = N_CONSTRUCTS, byrow = TRUE,
  dimnames = list(CONSTRUCTS, CONSTRUCTS)
)

# S matrix: covariance among exogenous + residual variances for endogenous
# Exogenous variables: PE, SI, FC, SE, TRA, AUT (free covariances among them)
# Endogenous variables: EE, BI, UB, ATT, TRU, ANX (residual variances only)
exogenous <- c("PE", "SI", "FC", "SE", "TRA", "AUT")
endogenous <- c("EE", "BI", "UB", "ATT", "TRU", "ANX")

RAM_S <- matrix(0, nrow = N_CONSTRUCTS, ncol = N_CONSTRUCTS,
                dimnames = list(CONSTRUCTS, CONSTRUCTS))

# Free covariances among exogenous variables
for (i in seq_along(exogenous)) {
  # Variance
  RAM_S[exogenous[i], exogenous[i]] <- paste0("0.5*Var_", exogenous[i])
  for (j in seq_along(exogenous)) {
    if (j > i) {
      label <- paste0("0.1*Cov_", exogenous[i], "_", exogenous[j])
      RAM_S[exogenous[i], exogenous[j]] <- label
      RAM_S[exogenous[j], exogenous[i]] <- label
    }
  }
}

# Residual variances for endogenous
for (v in endogenous) {
  RAM_S[v, v] <- paste0("0.5*Err_", v)
}

message("  RAM matrices (A, S) defined for Integrated Model")
message(sprintf("  A matrix: %d directed paths", sum(RAM_A != "0" & RAM_A != 0)))
message(sprintf("  Exogenous constructs: %s", paste(exogenous, collapse = ", ")))
message(sprintf("  Endogenous constructs: %s", paste(endogenous, collapse = ", ")))

# ==============================================================================
# 5. BASELINE OSMASEM (NO MODERATORS)
# ==============================================================================
message("\n--- Fitting baseline OSMASEM (no moderators) ---")

tryCatch({
  # Prepare data for osmasem: need correlation matrices in a list + sample sizes
  # osmasem() from metaSEM expects data in a specific format
  # We use the Cor() and RAM specification

  # Build model matrices for metaSEM
  Amatrix <- as.mxMatrix(RAM_A, name = "Amatrix")
  Smatrix <- as.mxMatrix(RAM_S, name = "Smatrix")

  # F matrix: identity (all observed)
  Fmatrix <- as.mxMatrix(diag(N_CONSTRUCTS), name = "Fmatrix")

  # Fit baseline OSMASEM
  osmasem_baseline <- osmasem(
    model.name = "Baseline_OSMASEM",
    RAM = list(A = Amatrix, S = Smatrix, F = Fmatrix),
    data = cor_matrices,
    n = sample_sizes
  )

  summary_baseline <- summary(osmasem_baseline)
  message("  Baseline OSMASEM converged successfully")
  message(sprintf("  -2LL = %.2f, df = %d", summary_baseline$Minus2LogLikelihood,
                  summary_baseline$degreesOfFreedom))

}, error = function(e) {
  message(sprintf("  WARNING: Baseline OSMASEM failed: %s", e$message))
  message("  Attempting alternative specification...")
  osmasem_baseline <<- NULL
})

# ==============================================================================
# 6. MODERATOR: PUBLICATION YEAR
# ==============================================================================
message("\n--- Testing Moderator: Publication Year ---")

key_paths <- c("PE_BI", "EE_BI", "TRU_BI", "ANX_BI")
year_results <- list()

if (!all(is.na(osmasem_data$year_c)) && !is.null(osmasem_baseline)) {
  tryCatch({
    # Create moderator matrix for year
    # In OSMASEM, moderators are added via the Ax argument
    # Ax specifies which paths are moderated by which moderator

    # Moderation matrix: same dimensions as A, but contains moderator data labels
    Ax_year <- matrix(0, nrow = N_CONSTRUCTS, ncol = N_CONSTRUCTS,
                      dimnames = list(CONSTRUCTS, CONSTRUCTS))

    # Allow year to moderate key paths
    for (path in key_paths) {
      parts <- strsplit(path, "_")[[1]]
      iv <- parts[1]
      dv <- parts[2]
      Ax_year[dv, iv] <- paste0("0*year_", path)
    }

    Ax_year_mx <- as.mxMatrix(Ax_year, name = "Ax")

    osmasem_year <- osmasem(
      model.name = "Year_Moderation",
      RAM = list(A = Amatrix, S = Smatrix, F = Fmatrix),
      Ax = Ax_year_mx,
      data = cor_matrices,
      n = sample_sizes,
      moderator = "year_c",
      data.moderator = osmasem_data
    )

    summary_year <- summary(osmasem_year)

    # LR test comparing baseline vs moderated model
    lr_year <- anova(osmasem_year, osmasem_baseline)

    year_results$model <- osmasem_year
    year_results$summary <- summary_year
    year_results$lr_test <- lr_year
    year_results$coefficients <- coef(osmasem_year)

    message("  Year moderation model fitted")
    message(sprintf("  LR chi-sq = %.3f, df = %d, p = %.4f",
                    lr_year$diffLL[2], lr_year$diffdf[2], lr_year$p[2]))

    # Extract moderation coefficients
    mod_coefs <- coef(osmasem_year)
    year_mod_idx <- grep("year_", names(mod_coefs))
    if (length(year_mod_idx) > 0) {
      message("\n  Year moderation coefficients:")
      for (idx in year_mod_idx) {
        message(sprintf("    %s = %.4f", names(mod_coefs)[idx], mod_coefs[idx]))
      }
    }

  }, error = function(e) {
    message(sprintf("  WARNING: Year moderation failed: %s", e$message))
    year_results$error <<- e$message
  })
} else {
  message("  Skipped: year data unavailable or baseline model failed")
  year_results$error <- "Data unavailable"
}

# ==============================================================================
# 7. MODERATOR: CULTURE SCORE (HOFSTEDE)
# ==============================================================================
message("\n--- Testing Moderator: Culture Score (Hofstede) ---")

culture_results <- list()

if (!all(is.na(osmasem_data$culture_score)) && !is.null(osmasem_baseline)) {
  tryCatch({
    Ax_culture <- matrix(0, nrow = N_CONSTRUCTS, ncol = N_CONSTRUCTS,
                       dimnames = list(CONSTRUCTS, CONSTRUCTS))

    for (path in key_paths) {
      parts <- strsplit(path, "_")[[1]]
      iv <- parts[1]
      dv <- parts[2]
      Ax_culture[dv, iv] <- paste0("0*culture_", path)
    }

    Ax_culture_mx <- as.mxMatrix(Ax_culture, name = "Ax")

    osmasem_culture <- osmasem(
      model.name = "Culture_Moderation",
      RAM = list(A = Amatrix, S = Smatrix, F = Fmatrix),
      Ax = Ax_culture_mx,
      data = cor_matrices,
      n = sample_sizes,
      moderator = "culture_score",
      data.moderator = osmasem_data
    )

    summary_culture <- summary(osmasem_culture)
    lr_culture <- anova(osmasem_culture, osmasem_baseline)

    culture_results$model <- osmasem_culture
    culture_results$summary <- summary_culture
    culture_results$lr_test <- lr_culture
    culture_results$coefficients <- coef(osmasem_culture)

    message("  Culture score moderation model fitted")
    message(sprintf("  LR chi-sq = %.3f, df = %d, p = %.4f",
                    lr_culture$diffLL[2], lr_culture$diffdf[2], lr_culture$p[2]))

    mod_coefs <- coef(osmasem_culture)
    culture_mod_idx <- grep("culture_", names(mod_coefs))
    if (length(culture_mod_idx) > 0) {
      message("\n  Culture score moderation coefficients:")
      for (idx in culture_mod_idx) {
        message(sprintf("    %s = %.4f", names(mod_coefs)[idx], mod_coefs[idx]))
      }
    }

  }, error = function(e) {
    message(sprintf("  WARNING: Culture score moderation failed: %s", e$message))
    culture_results$error <<- e$message
  })
} else {
  message("  Skipped: culture score data unavailable or baseline model failed")
  culture_results$error <- "Data unavailable"
}

# ==============================================================================
# 8. MODERATOR: SAMPLE SIZE (ARTIFACT)
# ==============================================================================
message("\n--- Testing Moderator: Sample Size (artifact check) ---")

sample_results <- list()

if (!is.null(osmasem_baseline)) {
  tryCatch({
    Ax_logn <- matrix(0, nrow = N_CONSTRUCTS, ncol = N_CONSTRUCTS,
                      dimnames = list(CONSTRUCTS, CONSTRUCTS))

    for (path in key_paths) {
      parts <- strsplit(path, "_")[[1]]
      iv <- parts[1]
      dv <- parts[2]
      Ax_logn[dv, iv] <- paste0("0*logn_", path)
    }

    Ax_logn_mx <- as.mxMatrix(Ax_logn, name = "Ax")

    osmasem_logn <- osmasem(
      model.name = "SampleSize_Moderation",
      RAM = list(A = Amatrix, S = Smatrix, F = Fmatrix),
      Ax = Ax_logn_mx,
      data = cor_matrices,
      n = sample_sizes,
      moderator = "log_n_c",
      data.moderator = osmasem_data
    )

    summary_logn <- summary(osmasem_logn)
    lr_logn <- anova(osmasem_logn, osmasem_baseline)

    sample_results$model <- osmasem_logn
    sample_results$summary <- summary_logn
    sample_results$lr_test <- lr_logn
    sample_results$coefficients <- coef(osmasem_logn)

    message("  Sample size moderation model fitted")
    message(sprintf("  LR chi-sq = %.3f, df = %d, p = %.4f",
                    lr_logn$diffLL[2], lr_logn$diffdf[2], lr_logn$p[2]))

    mod_coefs <- coef(osmasem_logn)
    logn_mod_idx <- grep("logn_", names(mod_coefs))
    if (length(logn_mod_idx) > 0) {
      message("\n  Sample size moderation coefficients:")
      for (idx in logn_mod_idx) {
        message(sprintf("    %s = %.4f", names(mod_coefs)[idx], mod_coefs[idx]))
      }
    }

    # Interpretation
    sig_sample <- any(sapply(logn_mod_idx, function(i) {
      se <- summary_logn$parameters$Std.Error[
        summary_logn$parameters$name == names(mod_coefs)[i]
      ]
      if (length(se) > 0) abs(mod_coefs[i] / se) > 1.96 else FALSE
    }))

    if (sig_sample) {
      message("  NOTE: Sample size moderates some paths — potential artifact concern")
    } else {
      message("  GOOD: No significant sample size moderation — results not artifactual")
    }

  }, error = function(e) {
    message(sprintf("  WARNING: Sample size moderation failed: %s", e$message))
    sample_results$error <<- e$message
  })
}

# ==============================================================================
# 9. SUMMARY TABLE
# ==============================================================================
message("\n--- Creating Moderator Summary Table ---")

moderator_summary <- data.frame(
  Moderator = character(),
  Path = character(),
  Baseline_Estimate = numeric(),
  Moderation_Coef = numeric(),
  SE = numeric(),
  z = numeric(),
  p = numeric(),
  Significant = logical(),
  stringsAsFactors = FALSE
)

# Helper to extract moderation info
extract_mod_info <- function(mod_results, mod_prefix, mod_name) {
  if (!is.null(mod_results$error)) return(NULL)

  coefs <- mod_results$coefficients
  summ <- mod_results$summary

  mod_idx <- grep(paste0("^", mod_prefix), names(coefs))
  if (length(mod_idx) == 0) return(NULL)

  rows <- lapply(mod_idx, function(i) {
    param_name <- names(coefs)[i]
    path_name <- sub(paste0("^", mod_prefix, "_"), "", param_name)
    est <- coefs[i]

    param_row <- summ$parameters[summ$parameters$name == param_name, ]
    se <- if (nrow(param_row) > 0) param_row$Std.Error else NA
    z_val <- if (!is.na(se) && se > 0) est / se else NA
    p_val <- if (!is.na(z_val)) 2 * pnorm(abs(z_val), lower.tail = FALSE) else NA

    data.frame(
      Moderator = mod_name,
      Path = path_name,
      Baseline_Estimate = NA,
      Moderation_Coef = round(est, 4),
      SE = round(se, 4),
      z = round(z_val, 3),
      p = round(p_val, 4),
      Significant = !is.na(p_val) & p_val < .05,
      stringsAsFactors = FALSE
    )
  })

  do.call(rbind, rows)
}

# Aggregate results
year_summ    <- extract_mod_info(year_results, "year", "Publication Year")
culture_summ <- extract_mod_info(culture_results, "culture", "Culture Score")
sample_summ  <- extract_mod_info(sample_results, "logn", "Log Sample Size")

moderator_summary <- rbind(
  if (!is.null(year_summ)) year_summ,
  if (!is.null(culture_summ)) culture_summ,
  if (!is.null(sample_summ)) sample_summ
)

if (nrow(moderator_summary) > 0) {
  message("\n  Moderator Summary Table:")
  print(moderator_summary, row.names = FALSE)
} else {
  message("  No moderator results available (all models may have failed)")
}

# ==============================================================================
# 10. SAVE RESULTS
# ==============================================================================
message("\n--- Saving OSMASEM moderator results ---")

osmasem_results <- list(
  baseline = if (exists("osmasem_baseline")) list(
    model = osmasem_baseline,
    summary = if (exists("summary_baseline")) summary_baseline else NULL
  ) else NULL,
  year_moderation = year_results,
  culture_moderation = culture_results,
  sample_size_moderation = sample_results,
  moderator_summary_table = moderator_summary,
  key_paths_tested = key_paths,
  osmasem_data = osmasem_data
)

saveRDS(osmasem_results, file.path(PATHS$output, "osmasem_moderator_results.rds"))
message(sprintf("  Saved to: %s", file.path(PATHS$output, "osmasem_moderator_results.rds")))

# Save summary table as CSV
if (nrow(moderator_summary) > 0) {
  write.csv(moderator_summary,
            file.path(PATHS$output, "osmasem_moderator_table.csv"),
            row.names = FALSE)
  message(sprintf("  Table saved to: %s", file.path(PATHS$output, "osmasem_moderator_table.csv")))
}

message("\n", strrep("=", 70))
message("05: OSMASEM MODERATOR ANALYSIS COMPLETE")
message(strrep("=", 70))
