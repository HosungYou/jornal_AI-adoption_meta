# ==============================================================================
# 02_stage1_pooling.R — TSSEM Stage 1: Correlation Matrix Pooling
# AI Adoption MASEM Dissertation
# ==============================================================================
# Purpose: Pool per-study correlation matrices using random-effects model
#          (Stage 1 of Two-Stage Meta-Analytic SEM)
# Input:   data/03_pooled/prepared_data.rds
# Output:  Pooled correlation matrix + asymptotic covariance matrix
# Method:  metaSEM::tssem1() — Cheung (2015)
# ==============================================================================

source("analysis/R/00_setup.R")

# =============================================================================
# 1. Load Prepared Data
# =============================================================================

message("--- TSSEM Stage 1: Loading data ---")

prepared <- readRDS(file.path(PATHS$pooled, "prepared_data.rds"))
cor_list <- prepared$cor_matrices
n_vec    <- prepared$sample_sizes

message(paste("Studies:", length(cor_list)))
message(paste("Total N:", sum(n_vec)))

# =============================================================================
# 2. Run TSSEM Stage 1 — Random-Effects Model
# =============================================================================

message("--- Running TSSEM Stage 1 (random-effects) ---")
message("This may take several minutes...")

stage1_RE <- tssem1(
  Cov   = cor_list,
  n     = n_vec,
  method = "REM",
  RE.type = "Diag",       # Diagonal τ² (one per correlation)
  I2 = "I2q",             # Q-based I² statistic
  acov = "individual"     # Individual study asymptotic covariances
)

# Check convergence
if (stage1_RE$mx.fit@output$status$code == 0) {
  message("Stage 1 CONVERGED successfully.")
} else {
  warning("Stage 1 did NOT converge. Check model specification.")
  message(paste("Status:", stage1_RE$mx.fit@output$status$code))
}

# =============================================================================
# 3. Extract Results
# =============================================================================

message("--- Extracting Stage 1 results ---")

# Pooled correlation matrix
pooled_cor <- coef(stage1_RE, select = "fixed")
pooled_matrix <- vec2symMat(pooled_cor, diag = FALSE, byrow = FALSE)
dimnames(pooled_matrix) <- list(CONSTRUCTS, CONSTRUCTS)
diag(pooled_matrix) <- 1.0

message("Pooled correlation matrix:")
print(round(pooled_matrix, 3))

# Heterogeneity (τ²)
tau2 <- coef(stage1_RE, select = "random")
message("\nHeterogeneity (τ²) for each correlation:")
print(round(tau2, 4))

# I² statistics
i2_values <- summary(stage1_RE)$I2.values
message("\nI² statistics:")
print(round(i2_values, 2))

# Asymptotic covariance matrix of pooled correlations (for Stage 2)
acov_matrix <- vcov(stage1_RE, select = "fixed")

# =============================================================================
# 4. Also Run Fixed-Effects Model (for comparison)
# =============================================================================

message("--- Running Fixed-Effects model for comparison ---")

stage1_FE <- tssem1(
  Cov   = cor_list,
  n     = n_vec,
  method = "FEM"
)

# Q-test for homogeneity
message("\nHomogeneity test (Q-statistic):")
# The Q test is embedded in the summary
summary_fe <- summary(stage1_FE)

# =============================================================================
# 5. Positive Definiteness of Pooled Matrix
# =============================================================================

message("--- Checking pooled matrix positive definiteness ---")

pd_check <- check_positive_definite(pooled_matrix)
if (pd_check$is_pd) {
  message("Pooled correlation matrix IS positive definite.")
  message(paste("Min eigenvalue:", round(pd_check$min_eigenvalue, 4)))
} else {
  warning("Pooled matrix is NOT positive definite! Applying nearPD correction.")
  pooled_matrix <- pd_check$nearest_pd
}

# =============================================================================
# 6. Save Results
# =============================================================================

message("--- Saving Stage 1 results ---")

# Save pooled correlation matrix
write.csv(
  as.data.frame(pooled_matrix),
  file.path(PATHS$pooled, "pooled_correlation_matrix.csv"),
  row.names = TRUE
)

# Save asymptotic covariance matrix
write.csv(
  as.data.frame(as.matrix(acov_matrix)),
  file.path(PATHS$pooled, "asymptotic_covariance_matrix.csv"),
  row.names = TRUE
)

# Save full Stage 1 results
stage1_results <- list(
  stage1_RE     = stage1_RE,
  stage1_FE     = stage1_FE,
  pooled_matrix = pooled_matrix,
  acov_matrix   = acov_matrix,
  tau2          = tau2,
  i2_values     = i2_values,
  n_studies     = length(cor_list),
  total_n       = sum(n_vec),
  harmonic_n    = harmonic_mean(n_vec)
)

saveRDS(stage1_results, file.path(PATHS$pooled, "stage1_results.rds"))

message("=== TSSEM Stage 1 Complete ===")
message(paste("Pooled matrix saved to:", file.path(PATHS$pooled, "pooled_correlation_matrix.csv")))
