# ==============================================================================
# 03_stage2_sem.R — TSSEM Stage 2: Structural Equation Modeling
# AI Adoption MASEM Dissertation
# ==============================================================================
# Purpose: Fit the Integrated structural model (Model 2) on the pooled
#          correlation matrix from Stage 1
# Input:   data/03_pooled/stage1_results.rds
# Output:  Path coefficients, fit indices, R² values
# Method:  metaSEM::tssem2() — WLS on pooled matrix
# ==============================================================================

source("analysis/R/00_setup.R")

# =============================================================================
# 1. Load Stage 1 Results
# =============================================================================

message("--- TSSEM Stage 2: Loading Stage 1 results ---")

stage1 <- readRDS(file.path(PATHS$pooled, "stage1_results.rds"))

message(paste("Studies:", stage1$n_studies))
message(paste("Harmonic mean N:", round(stage1$harmonic_n, 0)))

# =============================================================================
# 2. Define Integrated Model (Model 2) — Primary Model
# =============================================================================

message("--- Defining structural model ---")

# RAM (Reticular Action Model) specification for metaSEM
# Construct order: PE, EE, SI, FC, BI, UB, ATT, SE, TRU, ANX, TRA, AUT
# Indices:          1   2   3   4   5   6   7    8   9    10   11   12

# --- A matrix (asymmetric paths = regression coefficients) ---
# A[row, col] = path from col to row

A_model <- mxMatrix(
  type = "Full",
  nrow = N_CONSTRUCTS,
  ncol = N_CONSTRUCTS,
  free = FALSE,
  values = 0,
  labels = NA,
  name = "A"
)

# Define free paths for Model 2 (Integrated)
# Path: PE → BI (col=1, row=5)
A_model$free[5, 1]  <- TRUE; A_model$labels[5, 1]  <- "PE_to_BI"
# Path: EE → BI (col=2, row=5)
A_model$free[5, 2]  <- TRUE; A_model$labels[5, 2]  <- "EE_to_BI"
# Path: SI → BI (col=3, row=5)
A_model$free[5, 3]  <- TRUE; A_model$labels[5, 3]  <- "SI_to_BI"
# Path: FC → UB (col=4, row=6)
A_model$free[6, 4]  <- TRUE; A_model$labels[6, 4]  <- "FC_to_UB"
# Path: ATT → BI (col=7, row=5)
A_model$free[5, 7]  <- TRUE; A_model$labels[5, 7]  <- "ATT_to_BI"
# Path: BI → UB (col=5, row=6)
A_model$free[6, 5]  <- TRUE; A_model$labels[6, 5]  <- "BI_to_UB"
# Path: EE → ATT (col=2, row=7)
A_model$free[7, 2]  <- TRUE; A_model$labels[7, 2]  <- "EE_to_ATT"
# Path: PE → ATT (col=1, row=7)
A_model$free[7, 1]  <- TRUE; A_model$labels[7, 1]  <- "PE_to_ATT"

# AI-specific paths (Model 2 additions)
# Path: TRU → BI (col=9, row=5)
A_model$free[5, 9]  <- TRUE; A_model$labels[5, 9]  <- "TRU_to_BI"
# Path: ANX → BI (col=10, row=5)
A_model$free[5, 10] <- TRUE; A_model$labels[5, 10] <- "ANX_to_BI"
# Path: TRA → TRU (col=11, row=9)
A_model$free[9, 11] <- TRUE; A_model$labels[9, 11] <- "TRA_to_TRU"
# Path: AUT → ANX (col=12, row=10)
A_model$free[10, 12] <- TRUE; A_model$labels[10, 12] <- "AUT_to_ANX"
# Path: SE → EE (col=8, row=2)
A_model$free[2, 8]  <- TRUE; A_model$labels[2, 8]  <- "SE_to_EE"
# Path: SE → ANX (col=8, row=10)
A_model$free[10, 8] <- TRUE; A_model$labels[10, 8] <- "SE_to_ANX"

# --- S matrix (symmetric = covariances among exogenous variables + error variances) ---
# Exogenous variables: PE(1), SI(3), FC(4), SE(8), TRA(11), AUT(12)
# Endogenous variables: EE(2), BI(5), UB(6), ATT(7), TRU(9), ANX(10)

S_model <- mxMatrix(
  type = "Symm",
  nrow = N_CONSTRUCTS,
  ncol = N_CONSTRUCTS,
  free = FALSE,
  values = 0,
  name = "S"
)

# Exogenous variances (fixed to 1 for correlation matrix)
exogenous <- c(1, 3, 4, 8, 11, 12)  # PE, SI, FC, SE, TRA, AUT
for (i in exogenous) {
  S_model$values[i, i] <- 1
}

# Endogenous error variances (free)
endogenous <- c(2, 5, 6, 7, 9, 10)  # EE, BI, UB, ATT, TRU, ANX
for (i in endogenous) {
  S_model$free[i, i] <- TRUE
  S_model$values[i, i] <- 0.5  # Starting value
  S_model$labels[i, i] <- paste0("Var_e_", CONSTRUCTS[i])
}

# Covariances among exogenous variables (free)
exo_pairs <- combn(exogenous, 2)
for (k in seq_len(ncol(exo_pairs))) {
  i <- exo_pairs[1, k]
  j <- exo_pairs[2, k]
  S_model$free[i, j] <- TRUE
  S_model$free[j, i] <- TRUE
  S_model$values[i, j] <- 0.3
  S_model$values[j, i] <- 0.3
  S_model$labels[i, j] <- paste0("Cov_", CONSTRUCTS[i], "_", CONSTRUCTS[j])
  S_model$labels[j, i] <- paste0("Cov_", CONSTRUCTS[i], "_", CONSTRUCTS[j])
}

# =============================================================================
# 3. Fit TSSEM Stage 2
# =============================================================================

message("--- Fitting TSSEM Stage 2 (Model 2: Integrated) ---")

stage2_model2 <- tssem2(
  tssem1.obj = stage1$stage1_RE,
  Amatrix = A_model,
  Smatrix = S_model,
  diag.constraints = TRUE,
  intervals.type = "LB",  # Likelihood-based CI
  model.name = "Model2_Integrated"
)

# Check convergence
if (stage2_model2$mx.fit@output$status$code == 0) {
  message("Model 2 CONVERGED successfully.")
} else {
  warning("Model 2 did NOT converge!")
}

# =============================================================================
# 4. Extract Results
# =============================================================================

message("--- Extracting path coefficients ---")

# Summary
model2_summary <- summary(stage2_model2)
print(model2_summary)

# Path coefficients
path_coefs <- coef(stage2_model2)
message("\nPath coefficients:")
print(round(path_coefs, 4))

# Fit indices
fit_indices <- data.frame(
  Index = c("chi-square", "df", "p", "CFI", "TLI", "RMSEA", "RMSEA_lower",
            "RMSEA_upper", "SRMR"),
  Value = c(
    model2_summary$stat$chisq,
    model2_summary$stat$chisq.df,
    model2_summary$stat$chisq.p,
    model2_summary$stat$CFI,
    model2_summary$stat$TLI,
    model2_summary$stat$RMSEA,
    model2_summary$stat$RMSEA.lower,
    model2_summary$stat$RMSEA.upper,
    model2_summary$stat$SRMR
  )
)

message("\nFit indices:")
print(fit_indices)

# R-squared values for endogenous variables
message("\nR² values:")
# Computed from error variances: R² = 1 - error_variance (since total variance = 1)
for (i in endogenous) {
  error_var <- path_coefs[paste0("Var_e_", CONSTRUCTS[i])]
  r_squared <- 1 - error_var
  message(paste(" ", CONSTRUCTS[i], ":", round(r_squared, 3)))
}

# =============================================================================
# 5. Save Results
# =============================================================================

message("--- Saving Stage 2 results ---")

stage2_results <- list(
  model2_fit      = stage2_model2,
  model2_summary  = model2_summary,
  path_coefs      = path_coefs,
  fit_indices     = fit_indices,
  A_matrix        = A_model,
  S_matrix        = S_model
)

saveRDS(stage2_results, file.path(PATHS$output, "path_coefficients", "stage2_results.rds"))

# Save path coefficients as CSV
path_df <- data.frame(
  Path = names(path_coefs),
  Estimate = as.numeric(path_coefs)
)
write_csv(path_df, file.path(PATHS$output, "path_coefficients", "model2_path_coefficients.csv"))

# Save fit indices
write_csv(fit_indices, file.path(PATHS$output, "model_comparison", "model2_fit_indices.csv"))

message("=== TSSEM Stage 2 Complete ===")
