# ==============================================================================
# 04_competing_models.R — Competing Models Comparison
# AI Adoption MASEM Dissertation
# ==============================================================================
# Purpose: Fit and compare three competing structural models
#          Model 1: TAM/UTAUT Core
#          Model 2: Integrated (TAM/UTAUT + AI-specific)
#          Model 3: AI-Only
# Input:   data/03_pooled/stage1_results.rds
# Output:  Model comparison table (Δχ², ΔCFI, ΔRMSEA, AIC, BIC)
# ==============================================================================

source("analysis/R/00_setup.R")

# =============================================================================
# 1. Load Stage 1 Results
# =============================================================================

message("--- Competing Models: Loading data ---")

stage1 <- readRDS(file.path(PATHS$pooled, "stage1_results.rds"))

# =============================================================================
# 2. Model 1 — TAM/UTAUT Core
# =============================================================================

message("--- Fitting Model 1: TAM/UTAUT Core ---")

# A matrix for Model 1
A_model1 <- mxMatrix(
  type = "Full", nrow = N_CONSTRUCTS, ncol = N_CONSTRUCTS,
  free = FALSE, values = 0, labels = NA, name = "A"
)

# Model 1 paths only: PE→BI, EE→BI, SI→BI, FC→UB, ATT→BI, BI→UB, EE→ATT, PE→ATT
model1_paths <- list(
  c(5, 1, "PE_to_BI"),    # PE → BI
  c(5, 2, "EE_to_BI"),    # EE → BI
  c(5, 3, "SI_to_BI"),    # SI → BI
  c(6, 4, "FC_to_UB"),    # FC → UB
  c(5, 7, "ATT_to_BI"),   # ATT → BI
  c(6, 5, "BI_to_UB"),    # BI → UB
  c(7, 2, "EE_to_ATT"),   # EE → ATT
  c(7, 1, "PE_to_ATT")    # PE → ATT
)

for (p in model1_paths) {
  A_model1$free[as.integer(p[1]), as.integer(p[2])] <- TRUE
  A_model1$labels[as.integer(p[1]), as.integer(p[2])] <- p[3]
}

# S matrix for Model 1
# Exogenous: PE(1), EE(2), SI(3), FC(4), SE(8), TRU(9), ANX(10), TRA(11), AUT(12)
# Endogenous: BI(5), UB(6), ATT(7)
S_model1 <- mxMatrix(
  type = "Symm", nrow = N_CONSTRUCTS, ncol = N_CONSTRUCTS,
  free = FALSE, values = 0, name = "S"
)

exo1 <- c(1, 2, 3, 4, 8, 9, 10, 11, 12)
endo1 <- c(5, 6, 7)

for (i in exo1) S_model1$values[i, i] <- 1
for (i in endo1) {
  S_model1$free[i, i] <- TRUE
  S_model1$values[i, i] <- 0.5
  S_model1$labels[i, i] <- paste0("Var_e_", CONSTRUCTS[i])
}

exo1_pairs <- combn(exo1, 2)
for (k in seq_len(ncol(exo1_pairs))) {
  i <- exo1_pairs[1, k]
  j <- exo1_pairs[2, k]
  S_model1$free[i, j] <- S_model1$free[j, i] <- TRUE
  S_model1$values[i, j] <- S_model1$values[j, i] <- 0.3
  S_model1$labels[i, j] <- S_model1$labels[j, i] <- paste0("Cov_", CONSTRUCTS[i], "_", CONSTRUCTS[j])
}

stage2_m1 <- tssem2(
  tssem1.obj = stage1$stage1_RE,
  Amatrix = A_model1,
  Smatrix = S_model1,
  diag.constraints = TRUE,
  intervals.type = "LB",
  model.name = "Model1_TAM_UTAUT"
)

message(paste("Model 1 converged:", stage2_m1$mx.fit@output$status$code == 0))

# =============================================================================
# 3. Model 2 — Integrated (loaded from previous script or re-fit)
# =============================================================================

message("--- Loading/fitting Model 2: Integrated ---")

# Check if we have saved results
stage2_file <- file.path(PATHS$output, "path_coefficients", "stage2_results.rds")
if (file.exists(stage2_file)) {
  stage2_prev <- readRDS(stage2_file)
  stage2_m2 <- stage2_prev$model2_fit
  message("Model 2 loaded from previous results.")
} else {
  message("Re-fitting Model 2...")

  # Re-fit Model 2 (same as 03_stage2_sem.R)
  A_model2 <- mxMatrix(
    type = "Full", nrow = N_CONSTRUCTS, ncol = N_CONSTRUCTS,
    free = FALSE, values = 0, labels = NA, name = "A"
  )

  # TAM/UTAUT paths
  A_model2$free[5, 1]  <- TRUE; A_model2$labels[5, 1]  <- "PE_to_BI"
  A_model2$free[5, 2]  <- TRUE; A_model2$labels[5, 2]  <- "EE_to_BI"
  A_model2$free[5, 3]  <- TRUE; A_model2$labels[5, 3]  <- "SI_to_BI"
  A_model2$free[6, 4]  <- TRUE; A_model2$labels[6, 4]  <- "FC_to_UB"
  A_model2$free[5, 7]  <- TRUE; A_model2$labels[5, 7]  <- "ATT_to_BI"
  A_model2$free[6, 5]  <- TRUE; A_model2$labels[6, 5]  <- "BI_to_UB"
  A_model2$free[7, 2]  <- TRUE; A_model2$labels[7, 2]  <- "EE_to_ATT"
  A_model2$free[7, 1]  <- TRUE; A_model2$labels[7, 1]  <- "PE_to_ATT"

  # AI-specific paths
  A_model2$free[5, 9]  <- TRUE; A_model2$labels[5, 9]  <- "TRU_to_BI"
  A_model2$free[5, 10] <- TRUE; A_model2$labels[5, 10] <- "ANX_to_BI"
  A_model2$free[9, 11] <- TRUE; A_model2$labels[9, 11] <- "TRA_to_TRU"
  A_model2$free[10, 12] <- TRUE; A_model2$labels[10, 12] <- "AUT_to_ANX"
  A_model2$free[2, 8]  <- TRUE; A_model2$labels[2, 8]  <- "SE_to_EE"
  A_model2$free[10, 8] <- TRUE; A_model2$labels[10, 8] <- "SE_to_ANX"

  S_model2 <- mxMatrix(
    type = "Symm", nrow = N_CONSTRUCTS, ncol = N_CONSTRUCTS,
    free = FALSE, values = 0, name = "S"
  )

  exo2 <- c(1, 3, 4, 8, 11, 12)
  endo2 <- c(2, 5, 6, 7, 9, 10)

  for (i in exo2) S_model2$values[i, i] <- 1
  for (i in endo2) {
    S_model2$free[i, i] <- TRUE
    S_model2$values[i, i] <- 0.5
    S_model2$labels[i, i] <- paste0("Var_e_", CONSTRUCTS[i])
  }

  exo2_pairs <- combn(exo2, 2)
  for (k in seq_len(ncol(exo2_pairs))) {
    i <- exo2_pairs[1, k]
    j <- exo2_pairs[2, k]
    S_model2$free[i, j] <- S_model2$free[j, i] <- TRUE
    S_model2$values[i, j] <- S_model2$values[j, i] <- 0.3
    S_model2$labels[i, j] <- S_model2$labels[j, i] <- paste0("Cov_", CONSTRUCTS[i], "_", CONSTRUCTS[j])
  }

  stage2_m2 <- tssem2(
    tssem1.obj = stage1$stage1_RE,
    Amatrix = A_model2,
    Smatrix = S_model2,
    diag.constraints = TRUE,
    intervals.type = "LB",
    model.name = "Model2_Integrated"
  )

  message(paste("Model 2 converged:", stage2_m2$mx.fit@output$status$code == 0))
}

# =============================================================================
# 4. Model 3 — AI-Only
# =============================================================================

message("--- Fitting Model 3: AI-Only ---")

A_model3 <- mxMatrix(
  type = "Full", nrow = N_CONSTRUCTS, ncol = N_CONSTRUCTS,
  free = FALSE, values = 0, labels = NA, name = "A"
)

# Model 3 paths: TRU→BI, ANX→BI, TRA→TRU, AUT→BI, SE→BI, ATT→BI, BI→UB
model3_paths <- list(
  c(5, 9,  "TRU_to_BI"),   # TRU → BI
  c(5, 10, "ANX_to_BI"),   # ANX → BI
  c(9, 11, "TRA_to_TRU"),  # TRA → TRU
  c(5, 12, "AUT_to_BI"),   # AUT → BI
  c(5, 8,  "SE_to_BI"),    # SE → BI
  c(5, 7,  "ATT_to_BI"),   # ATT → BI
  c(6, 5,  "BI_to_UB")     # BI → UB
)

for (p in model3_paths) {
  A_model3$free[as.integer(p[1]), as.integer(p[2])] <- TRUE
  A_model3$labels[as.integer(p[1]), as.integer(p[2])] <- p[3]
}

# S matrix for Model 3
# Exogenous: PE(1), EE(2), SI(3), FC(4), SE(8), ATT(7), TRA(11), AUT(12), ANX(10)
# Endogenous: BI(5), UB(6), TRU(9)
S_model3 <- mxMatrix(
  type = "Symm", nrow = N_CONSTRUCTS, ncol = N_CONSTRUCTS,
  free = FALSE, values = 0, name = "S"
)

exo3 <- c(1, 2, 3, 4, 7, 8, 10, 11, 12)
endo3 <- c(5, 6, 9)

for (i in exo3) S_model3$values[i, i] <- 1
for (i in endo3) {
  S_model3$free[i, i] <- TRUE
  S_model3$values[i, i] <- 0.5
  S_model3$labels[i, i] <- paste0("Var_e_", CONSTRUCTS[i])
}

exo3_pairs <- combn(exo3, 2)
for (k in seq_len(ncol(exo3_pairs))) {
  i <- exo3_pairs[1, k]
  j <- exo3_pairs[2, k]
  S_model3$free[i, j] <- S_model3$free[j, i] <- TRUE
  S_model3$values[i, j] <- S_model3$values[j, i] <- 0.3
  S_model3$labels[i, j] <- S_model3$labels[j, i] <- paste0("Cov_", CONSTRUCTS[i], "_", CONSTRUCTS[j])
}

stage2_m3 <- tssem2(
  tssem1.obj = stage1$stage1_RE,
  Amatrix = A_model3,
  Smatrix = S_model3,
  diag.constraints = TRUE,
  intervals.type = "LB",
  model.name = "Model3_AI_Only"
)

message(paste("Model 3 converged:", stage2_m3$mx.fit@output$status$code == 0))

# =============================================================================
# 5. Model Comparison
# =============================================================================

message("--- Comparing models ---")

extract_fit <- function(model, name) {
  s <- summary(model)
  data.frame(
    Model       = name,
    chi_sq      = s$stat$chisq,
    df          = s$stat$chisq.df,
    p           = s$stat$chisq.p,
    CFI         = s$stat$CFI,
    TLI         = s$stat$TLI,
    RMSEA       = s$stat$RMSEA,
    RMSEA_lower = s$stat$RMSEA.lower,
    RMSEA_upper = s$stat$RMSEA.upper,
    SRMR        = s$stat$SRMR,
    AIC         = s$stat$AIC,
    BIC         = s$stat$BIC,
    n_paths     = sum(model$mx.fit$A$free),
    stringsAsFactors = FALSE
  )
}

comparison <- bind_rows(
  extract_fit(stage2_m1, "Model 1: TAM/UTAUT"),
  extract_fit(stage2_m2, "Model 2: Integrated"),
  extract_fit(stage2_m3, "Model 3: AI-Only")
)

message("\n=== MODEL COMPARISON TABLE ===")
print(comparison)

# Delta statistics (Model 2 vs Model 1)
message("\n--- Model 2 vs Model 1 ---")
message(paste("Δχ²:", round(comparison$chi_sq[1] - comparison$chi_sq[2], 2),
              "Δdf:", comparison$df[1] - comparison$df[2]))
message(paste("ΔCFI:", round(comparison$CFI[2] - comparison$CFI[1], 4)))
message(paste("ΔRMSEA:", round(comparison$RMSEA[1] - comparison$RMSEA[2], 4)))

# Chi-square difference test (M1 nested in M2)
delta_chi <- comparison$chi_sq[1] - comparison$chi_sq[2]
delta_df  <- comparison$df[1] - comparison$df[2]
if (delta_df > 0) {
  p_diff <- pchisq(delta_chi, delta_df, lower.tail = FALSE)
  message(paste("Δχ² test p-value:", format(p_diff, scientific = TRUE)))
}

# =============================================================================
# 6. Save Results
# =============================================================================

message("--- Saving comparison results ---")

write_csv(comparison, file.path(PATHS$output, "model_comparison", "model_comparison_table.csv"))

competing_results <- list(
  model1_fit  = stage2_m1,
  model2_fit  = stage2_m2,
  model3_fit  = stage2_m3,
  comparison  = comparison
)

saveRDS(competing_results, file.path(PATHS$output, "model_comparison", "competing_models_results.rds"))

message("=== Competing Models Comparison Complete ===")
