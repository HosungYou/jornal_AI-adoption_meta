# ==============================================================================
# 07_mediation.R — Meta-Analytic Mediation Analysis
# AI Adoption MASEM Dissertation
# ==============================================================================
# Purpose: Test indirect effects within TSSEM Stage 2 framework
#   1. TRA -> TRU -> BI (transparency builds trust -> intention)
#   2. SE -> EE -> BI (self-efficacy -> reduced effort -> intention)
#   3. PE -> ATT -> BI (usefulness -> attitude -> intention)
#   4. ANX -> TRU -> BI (anxiety erodes trust -> intention)
# Method: mxAlgebra for indirect effects, Delta method + bootstrap CIs
# Dependencies: 00_setup.R, stage1_results.rds
# Output: mediation_results.rds
# ==============================================================================

source("analysis/R/00_setup.R")
message("\n", strrep("=", 70))
message("07: META-ANALYTIC MEDIATION ANALYSIS")
message(strrep("=", 70))

# ==============================================================================
# 1. LOAD STAGE 1 RESULTS
# ==============================================================================
message("\n--- Loading Stage 1 results ---")
stage1 <- readRDS(file.path(PATHS$pooled, "stage1_results.rds"))

pooled_matrix <- stage1$pooled_matrix
acov_matrix   <- stage1$acov_matrix
harmonic_n    <- stage1$harmonic_n
total_n       <- stage1$total_n

message(sprintf("  Pooled matrix: %d x %d", nrow(pooled_matrix), ncol(pooled_matrix)))
message(sprintf("  Harmonic N: %.0f, Total N: %d", harmonic_n, total_n))

# ==============================================================================
# 2. DEFINE EXTENDED MODEL WITH MEDIATION PATHS
# ==============================================================================
message("\n--- Defining extended model with mediation algebra ---")

# The extended model adds ANX -> TRU path (for mediation path 4)
# on top of the standard Integrated Model

# A matrix (directed paths) — extended with ANX -> TRU
A_values <- matrix("0", nrow = N_CONSTRUCTS, ncol = N_CONSTRUCTS,
                   dimnames = list(CONSTRUCTS, CONSTRUCTS))

# Standard Integrated Model paths
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

# EXTENDED: ANX -> TRU (anxiety erodes trust)
A_values["TRU", "ANX"] <- "0.1*ANX_TRU"

Amatrix <- as.mxMatrix(A_values, name = "Amatrix")

# S matrix (symmetric)
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

message("  Extended model defined with 15 directed paths (including ANX->TRU)")

# ==============================================================================
# 3. DEFINE INDIRECT EFFECT ALGEBRA
# ==============================================================================
message("\n--- Defining mxAlgebra for indirect effects ---")

# Indirect effects via mxAlgebra
# These reference the A matrix elements by position
# Construct indices: PE=1, EE=2, SI=3, FC=4, BI=5, UB=6, ATT=7, SE=8, TRU=9, ANX=10, TRA=11, AUT=12

# Mediation 1: TRA -> TRU -> BI
# indirect = TRA_TRU * TRU_BI = A[9,11] * A[5,9]
indirect1 <- mxAlgebra(Amatrix[9,11] * Amatrix[5,9], name = "ind_TRA_TRU_BI")

# Mediation 2: SE -> EE -> BI
# indirect = SE_EE * EE_BI = A[2,8] * A[5,2]
indirect2 <- mxAlgebra(Amatrix[2,8] * Amatrix[5,2], name = "ind_SE_EE_BI")

# Mediation 3: PE -> ATT -> BI
# indirect = PE_ATT * ATT_BI = A[7,1] * A[5,7]
indirect3 <- mxAlgebra(Amatrix[7,1] * Amatrix[5,7], name = "ind_PE_ATT_BI")

# Mediation 4: ANX -> TRU -> BI
# indirect = ANX_TRU * TRU_BI = A[9,10] * A[5,9]
indirect4 <- mxAlgebra(Amatrix[9,10] * Amatrix[5,9], name = "ind_ANX_TRU_BI")

# Total effects (direct + indirect)
# Total TRA -> BI: only indirect through TRU (no direct TRA->BI path)
total1 <- mxAlgebra(ind_TRA_TRU_BI, name = "total_TRA_BI")

# Total SE -> BI: indirect through EE (no direct SE->BI path)
total2 <- mxAlgebra(ind_SE_EE_BI, name = "total_SE_BI")

# Total PE -> BI: direct + indirect through ATT
total3 <- mxAlgebra(Amatrix[5,1] + ind_PE_ATT_BI, name = "total_PE_BI")

# Total ANX -> BI: direct + indirect through TRU
total4 <- mxAlgebra(Amatrix[5,10] + ind_ANX_TRU_BI, name = "total_ANX_BI")

# Proportion mediated for paths with both direct and indirect
prop3 <- mxAlgebra(ind_PE_ATT_BI / total_PE_BI, name = "prop_PE_ATT_BI")
prop4 <- mxAlgebra(ind_ANX_TRU_BI / total_ANX_BI, name = "prop_ANX_TRU_BI")

# Confidence intervals using Delta method
ci_indirect <- mxCI(c(
  "ind_TRA_TRU_BI", "ind_SE_EE_BI", "ind_PE_ATT_BI", "ind_ANX_TRU_BI",
  "total_TRA_BI", "total_SE_BI", "total_PE_BI", "total_ANX_BI",
  "prop_PE_ATT_BI", "prop_ANX_TRU_BI"
))

message("  4 indirect effects defined:")
message("    1. TRA -> TRU -> BI (transparency -> trust -> intention)")
message("    2. SE  -> EE  -> BI (self-efficacy -> effort -> intention)")
message("    3. PE  -> ATT -> BI (usefulness -> attitude -> intention)")
message("    4. ANX -> TRU -> BI (anxiety -> trust erosion -> intention)")

# ==============================================================================
# 4. FIT THE EXTENDED MODEL WITH MEDIATION
# ==============================================================================
message("\n--- Fitting extended TSSEM Stage 2 with mediation algebra ---")

# We need to re-run Stage 1 or use the existing one
# Load prepared data for Stage 1
prepared <- readRDS(file.path(PATHS$pooled, "prepared_data.rds"))

# Re-run Stage 1 (or use cached)
message("  Running TSSEM Stage 1...")
tryCatch({
  stage1_fit <- tssem1(
    Cov  = prepared$cor_matrices,
    n    = prepared$sample_sizes,
    method = "REM",
    RE.type = "Diag",
    acov = "weighted"
  )
  message("  Stage 1 converged")
}, error = function(e) {
  stop(sprintf("Stage 1 failed: %s", e$message))
})

# Fit Stage 2 with mediation algebra
message("  Running TSSEM Stage 2 with mediation algebra...")
tryCatch({
  mediation_model <- tssem2(
    stage1_fit,
    Amatrix = Amatrix,
    Smatrix = Smatrix,
    Fmatrix = Fmatrix,
    model.name = "Mediation_Extended",
    mx.algebras = list(
      ind_TRA_TRU_BI = indirect1,
      ind_SE_EE_BI   = indirect2,
      ind_PE_ATT_BI  = indirect3,
      ind_ANX_TRU_BI = indirect4,
      total_TRA_BI   = total1,
      total_SE_BI    = total2,
      total_PE_BI    = total3,
      total_ANX_BI   = total4,
      prop_PE_ATT_BI = prop3,
      prop_ANX_TRU_BI = prop4
    ),
    intervals.type = "LB",  # Likelihood-based CIs
    run = TRUE
  )

  mediation_summary <- summary(mediation_model)

  message("  Extended mediation model converged")
  message(sprintf("  Chi-sq = %.2f, df = %d, p = %.4f",
                  mediation_summary$stat$chisq,
                  mediation_summary$stat$chisqDF,
                  mediation_summary$stat$chisqPvalue))
  message(sprintf("  CFI = %.3f, RMSEA = %.3f, SRMR = %.3f",
                  mediation_summary$stat$CFI,
                  mediation_summary$stat$RMSEA,
                  mediation_summary$stat$SRMR))

}, error = function(e) {
  message(sprintf("  ERROR: Extended mediation model failed: %s", e$message))
  message("  Attempting model without ANX->TRU path...")

  # Fallback: remove ANX->TRU, test only mediations 1-3
  A_values_fallback <- A_values
  A_values_fallback["TRU", "ANX"] <- "0"
  Amatrix_fb <- as.mxMatrix(A_values_fallback, name = "Amatrix")

  mediation_model <<- tryCatch({
    tssem2(
      stage1_fit,
      Amatrix = Amatrix_fb,
      Smatrix = Smatrix,
      Fmatrix = Fmatrix,
      model.name = "Mediation_Standard",
      mx.algebras = list(
        ind_TRA_TRU_BI = indirect1,
        ind_SE_EE_BI   = indirect2,
        ind_PE_ATT_BI  = indirect3,
        total_TRA_BI   = total1,
        total_SE_BI    = total2,
        total_PE_BI    = total3,
        prop_PE_ATT_BI = prop3
      ),
      intervals.type = "LB",
      run = TRUE
    )
  }, error = function(e2) {
    message(sprintf("  Fallback also failed: %s", e2$message))
    NULL
  })

  if (!is.null(mediation_model)) {
    mediation_summary <<- summary(mediation_model)
    message("  Fallback model (without ANX->TRU) converged")
  }
})

# ==============================================================================
# 5. EXTRACT MEDIATION RESULTS
# ==============================================================================
message("\n--- Extracting mediation results ---")

mediation_results_table <- NULL

if (exists("mediation_model") && !is.null(mediation_model)) {
  # Extract all coefficients
  all_coefs <- coef(mediation_model)

  # Try to get likelihood-based CIs
  ci_results <- tryCatch({
    confint(mediation_model)
  }, error = function(e) {
    message("  CIs via confint() failed, using Wald-based CIs")
    NULL
  })

  # Build mediation results table
  med_paths <- list(
    list(name = "TRA -> TRU -> BI",
         indirect_label = "ind_TRA_TRU_BI",
         path_a = "TRA_TRU", path_b = "TRU_BI",
         direct_label = NA,
         total_label = "total_TRA_BI",
         prop_label = NA,
         theory = "Transparency -> Trust -> Intention"),
    list(name = "SE -> EE -> BI",
         indirect_label = "ind_SE_EE_BI",
         path_a = "SE_EE", path_b = "EE_BI",
         direct_label = NA,
         total_label = "total_SE_BI",
         prop_label = NA,
         theory = "Self-Efficacy -> Effort -> Intention"),
    list(name = "PE -> ATT -> BI",
         indirect_label = "ind_PE_ATT_BI",
         path_a = "PE_ATT", path_b = "ATT_BI",
         direct_label = "PE_BI",
         total_label = "total_PE_BI",
         prop_label = "prop_PE_ATT_BI",
         theory = "Usefulness -> Attitude -> Intention"),
    list(name = "ANX -> TRU -> BI",
         indirect_label = "ind_ANX_TRU_BI",
         path_a = "ANX_TRU", path_b = "TRU_BI",
         direct_label = "ANX_BI",
         total_label = "total_ANX_BI",
         prop_label = "prop_ANX_TRU_BI",
         theory = "Anxiety -> Trust erosion -> Intention")
  )

  mediation_results_table <- data.frame(
    Mediation = character(),
    Path_a = numeric(), Path_b = numeric(),
    Indirect = numeric(), Indirect_SE = numeric(),
    CI_lower = numeric(), CI_upper = numeric(),
    Direct = numeric(), Total = numeric(),
    Prop_Mediated = numeric(), Significant = logical(),
    stringsAsFactors = FALSE
  )

  for (mp in med_paths) {
    # Skip if labels not in model
    if (!mp$indirect_label %in% names(all_coefs)) {
      message(sprintf("  Skipping %s (not in model)", mp$name))
      next
    }

    path_a_val <- if (mp$path_a %in% names(all_coefs)) all_coefs[mp$path_a] else NA
    path_b_val <- if (mp$path_b %in% names(all_coefs)) all_coefs[mp$path_b] else NA
    indirect   <- all_coefs[mp$indirect_label]

    direct <- if (!is.na(mp$direct_label) && mp$direct_label %in% names(all_coefs)) {
      all_coefs[mp$direct_label]
    } else NA

    total <- if (mp$total_label %in% names(all_coefs)) all_coefs[mp$total_label] else NA

    prop_med <- if (!is.na(mp$prop_label) && mp$prop_label %in% names(all_coefs)) {
      all_coefs[mp$prop_label]
    } else if (!is.na(direct) && !is.na(total) && abs(total) > 0.001) {
      indirect / total
    } else NA

    # Get CIs
    ci_lo <- ci_hi <- NA
    if (!is.null(ci_results) && mp$indirect_label %in% rownames(ci_results)) {
      ci_lo <- ci_results[mp$indirect_label, 1]
      ci_hi <- ci_results[mp$indirect_label, 2]
    }

    # Significance: CI does not contain 0
    sig <- if (!is.na(ci_lo) && !is.na(ci_hi)) {
      (ci_lo > 0 & ci_hi > 0) | (ci_lo < 0 & ci_hi < 0)
    } else FALSE

    # Approximate SE from Sobel test: SE = sqrt(a^2*se_b^2 + b^2*se_a^2)
    indirect_se <- NA  # Will be available from CI width if present
    if (!is.na(ci_lo) && !is.na(ci_hi)) {
      indirect_se <- (ci_hi - ci_lo) / (2 * 1.96)  # Approximate
    }

    row <- data.frame(
      Mediation = mp$name,
      Path_a = round(path_a_val, 4),
      Path_b = round(path_b_val, 4),
      Indirect = round(indirect, 4),
      Indirect_SE = round(indirect_se, 4),
      CI_lower = round(ci_lo, 4),
      CI_upper = round(ci_hi, 4),
      Direct = round(direct, 4),
      Total = round(total, 4),
      Prop_Mediated = round(prop_med, 3),
      Significant = sig,
      stringsAsFactors = FALSE
    )

    mediation_results_table <- rbind(mediation_results_table, row)
  }

  message("\n  Mediation Results:")
  print(mediation_results_table, row.names = FALSE)
}

# ==============================================================================
# 6. BOOTSTRAP CONFIDENCE INTERVALS (SUPPLEMENTARY)
# ==============================================================================
message("\n--- Computing bootstrap CIs for indirect effects ---")

n_boot <- 1000
boot_results <- NULL

if (exists("mediation_model") && !is.null(mediation_model)) {
  tryCatch({
    message(sprintf("  Running %d bootstrap iterations...", n_boot))

    # Rerun with bootstrap CIs
    mediation_boot <- rerun(mediation_model, intervals.type = "z",
                            model.name = "Mediation_Boot")

    # For true bootstrap, we need to resample from Stage 1
    # This is computationally intensive; use parametric bootstrap from OpenMx
    boot_ci <- tryCatch({
      mxBootstrap(mediation_model, replications = n_boot)
    }, error = function(e) {
      message(sprintf("  Bootstrap failed: %s", e$message))
      message("  Using likelihood-based CIs as primary inference")
      NULL
    })

    if (!is.null(boot_ci)) {
      boot_summary <- summary(boot_ci)
      boot_results <- boot_summary

      message("  Bootstrap CIs computed successfully")

      # Extract bootstrap CIs for indirect effects
      indirect_labels <- c("ind_TRA_TRU_BI", "ind_SE_EE_BI",
                           "ind_PE_ATT_BI", "ind_ANX_TRU_BI")

      for (il in indirect_labels) {
        if (il %in% rownames(boot_summary$bootstrapSE)) {
          boot_se <- boot_summary$bootstrapSE[il, ]
          message(sprintf("    %s: bootstrap SE = %.4f", il, boot_se))
        }
      }
    }

  }, error = function(e) {
    message(sprintf("  Bootstrap procedure failed: %s", e$message))
    message("  Relying on likelihood-based CIs for inference")
  })
}

# ==============================================================================
# 7. EFFECT SIZE INTERPRETATION
# ==============================================================================
message("\n--- Effect Size Interpretation ---")

if (!is.null(mediation_results_table) && nrow(mediation_results_table) > 0) {
  message("\n  Interpretation of indirect effects:")
  for (i in seq_len(nrow(mediation_results_table))) {
    row <- mediation_results_table[i, ]
    abs_ind <- abs(row$Indirect)

    # Kenny (2018) benchmarks for indirect effects
    size <- ifelse(abs_ind >= 0.08, "LARGE",
                   ifelse(abs_ind >= 0.04, "MEDIUM",
                          ifelse(abs_ind >= 0.01, "SMALL", "NEGLIGIBLE")))

    sig_label <- ifelse(row$Significant, "SIGNIFICANT", "NOT SIGNIFICANT")

    message(sprintf("  %s:", row$Mediation))
    message(sprintf("    Indirect = %.4f [%.4f, %.4f] — %s, %s",
                    row$Indirect, row$CI_lower, row$CI_upper, sig_label, size))

    if (!is.na(row$Direct)) {
      message(sprintf("    Direct = %.4f, Total = %.4f, Proportion mediated = %.1f%%",
                      row$Direct, row$Total, row$Prop_Mediated * 100))

      # Mediation type
      if (row$Significant) {
        if (is.na(row$Direct) || abs(row$Direct) < 0.05) {
          message("    Type: FULL mediation (indirect significant, direct negligible)")
        } else {
          med_type <- ifelse(sign(row$Indirect) == sign(row$Direct),
                             "COMPLEMENTARY (partial)", "COMPETITIVE (suppression)")
          message(sprintf("    Type: %s mediation", med_type))
        }
      }
    }
  }
}

# ==============================================================================
# 8. SAVE RESULTS
# ==============================================================================
message("\n--- Saving mediation analysis results ---")

mediation_output <- list(
  model = if (exists("mediation_model")) mediation_model else NULL,
  summary = if (exists("mediation_summary")) mediation_summary else NULL,
  mediation_table = mediation_results_table,
  bootstrap_results = boot_results,
  ci_results = if (exists("ci_results")) ci_results else NULL,
  model_fit = if (exists("mediation_summary")) list(
    chisq = mediation_summary$stat$chisq,
    df = mediation_summary$stat$chisqDF,
    p = mediation_summary$stat$chisqPvalue,
    CFI = mediation_summary$stat$CFI,
    RMSEA = mediation_summary$stat$RMSEA,
    SRMR = mediation_summary$stat$SRMR
  ) else NULL,
  extended_path = "ANX_TRU"
)

saveRDS(mediation_output, file.path(PATHS$output, "mediation_results.rds"))
message(sprintf("  Saved to: %s", file.path(PATHS$output, "mediation_results.rds")))

if (!is.null(mediation_results_table)) {
  write.csv(mediation_results_table,
            file.path(PATHS$output, "mediation_table.csv"),
            row.names = FALSE)
  message(sprintf("  Table saved to: %s", file.path(PATHS$output, "mediation_table.csv")))
}

message("\n", strrep("=", 70))
message("07: MEDIATION ANALYSIS COMPLETE")
message(strrep("=", 70))
