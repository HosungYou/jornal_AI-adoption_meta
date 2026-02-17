# ==============================================================================
# 01_data_preparation.R — Data Preparation and Validation
# AI Adoption MASEM Dissertation
# ==============================================================================
# Purpose: Read coded data, assemble correlation matrices per study,
#          validate positive definiteness, and prepare for TSSEM Stage 1
# Input:   data/02_verified/verified_correlations.csv
#          data/04_final/masem_final_dataset.csv
# Output:  List of correlation matrices and sample sizes ready for metaSEM
# ==============================================================================

source("analysis/R/00_setup.R")

# =============================================================================
# 1. Load Verified Data
# =============================================================================

message("--- Step 1: Loading verified correlation data ---")

# Primary dataset: verified correlations in long format
cor_data <- read_csv(
  file.path(PATHS$verified, "verified_correlations.csv"),
  col_types = cols(
    study_id       = col_character(),
    row_construct  = col_character(),
    col_construct  = col_character(),
    r              = col_double(),
    r_source       = col_character(),
    original_beta  = col_double(),
    n_for_pair     = col_integer()
  )
)

# Study metadata
study_meta <- read_csv(
  file.path(PATHS$final, "masem_final_dataset.csv"),
  col_types = cols(.default = col_guess())
)

message(paste("Loaded", n_distinct(cor_data$study_id), "studies"))
message(paste("Total correlation entries:", nrow(cor_data)))

# =============================================================================
# 2. Validate Constructs
# =============================================================================

message("--- Step 2: Validating construct names ---")

invalid_rows <- cor_data %>%
  filter(!row_construct %in% CONSTRUCTS | !col_construct %in% CONSTRUCTS)

if (nrow(invalid_rows) > 0) {
  warning(paste("Found", nrow(invalid_rows), "rows with non-standard construct names:"))
  print(distinct(invalid_rows, row_construct, col_construct))
  stop("Fix construct names before proceeding.")
} else {
  message("All construct names are valid.")
}

# =============================================================================
# 3. Assemble Per-Study Correlation Matrices
# =============================================================================

message("--- Step 3: Assembling per-study correlation matrices ---")

study_ids <- unique(cor_data$study_id)

# Build list of correlation matrices (one per study)
cor_matrices <- list()
sample_sizes <- numeric()
study_constructs <- list()

for (sid in study_ids) {
  study_cors <- cor_data %>% filter(study_id == sid)

  # Determine which constructs this study covers
  covered <- unique(c(study_cors$row_construct, study_cors$col_construct))
  covered <- intersect(covered, CONSTRUCTS)
  study_constructs[[sid]] <- covered

  # Build full 12x12 matrix (NA for missing pairs)
  mat <- matrix(NA, nrow = N_CONSTRUCTS, ncol = N_CONSTRUCTS,
                dimnames = list(CONSTRUCTS, CONSTRUCTS))
  diag(mat) <- 1.0

  for (i in seq_len(nrow(study_cors))) {
    rc <- study_cors$row_construct[i]
    cc <- study_cors$col_construct[i]
    mat[rc, cc] <- study_cors$r[i]
    mat[cc, rc] <- study_cors$r[i]
  }

  cor_matrices[[sid]] <- mat

  # Sample size (use study-level N; pair-specific N used later if available)
  n_study <- study_meta %>% filter(study_id == sid) %>% pull(sample_size)
  sample_sizes[sid] <- ifelse(length(n_study) > 0, n_study[1], NA)
}

message(paste("Assembled", length(cor_matrices), "correlation matrices"))

# =============================================================================
# 4. Coverage Analysis
# =============================================================================

message("--- Step 4: Analyzing correlation pair coverage ---")

# Count how many studies report each pair
pair_coverage <- matrix(0, nrow = N_CONSTRUCTS, ncol = N_CONSTRUCTS,
                        dimnames = list(CONSTRUCTS, CONSTRUCTS))

for (sid in study_ids) {
  mat <- cor_matrices[[sid]]
  for (i in 1:(N_CONSTRUCTS - 1)) {
    for (j in (i + 1):N_CONSTRUCTS) {
      if (!is.na(mat[i, j])) {
        pair_coverage[i, j] <- pair_coverage[i, j] + 1
        pair_coverage[j, i] <- pair_coverage[j, i] + 1
      }
    }
  }
}

message("Pair coverage summary (number of studies per correlation):")
message(paste("  Min:", min(pair_coverage[upper.tri(pair_coverage)])))
message(paste("  Max:", max(pair_coverage[upper.tri(pair_coverage)])))
message(paste("  Mean:", round(mean(pair_coverage[upper.tri(pair_coverage)]), 1)))

# Flag pairs with k < 3 (insufficient for meta-analysis)
low_coverage <- which(pair_coverage < 3 & pair_coverage > 0, arr.ind = TRUE)
if (nrow(low_coverage) > 0) {
  warning("The following pairs have fewer than 3 studies:")
  for (i in seq_len(nrow(low_coverage))) {
    if (low_coverage[i, 1] < low_coverage[i, 2]) {
      message(paste("  ", CONSTRUCTS[low_coverage[i, 1]], "-",
                     CONSTRUCTS[low_coverage[i, 2]], ":",
                     pair_coverage[low_coverage[i, 1], low_coverage[i, 2]], "studies"))
    }
  }
}

# =============================================================================
# 5. Positive Definiteness Check
# =============================================================================

message("--- Step 5: Checking positive definiteness ---")

pd_results <- list()
non_pd_count <- 0

for (sid in study_ids) {
  mat <- cor_matrices[[sid]]
  # Extract submatrix of non-NA constructs only
  covered <- study_constructs[[sid]]
  submat <- mat[covered, covered]

  # Only check if we have at least 3 constructs
  if (length(covered) >= 3 && all(!is.na(submat))) {
    pd_check <- check_positive_definite(submat)
    pd_results[[sid]] <- pd_check

    if (!pd_check$is_pd) {
      non_pd_count <- non_pd_count + 1
      message(paste("  Non-PD:", sid, "| Min eigenvalue:",
                     round(pd_check$min_eigenvalue, 4)))
      # Apply nearest PD correction
      corrected <- as.matrix(Matrix::nearPD(submat, corr = TRUE)$mat)
      cor_matrices[[sid]][covered, covered] <- corrected
    }
  }
}

message(paste("Non-positive-definite matrices corrected:", non_pd_count,
              "out of", length(study_ids)))

# =============================================================================
# 6. Prepare metaSEM Input
# =============================================================================

message("--- Step 6: Preparing metaSEM input ---")

# Convert to metaSEM-compatible format: list of matrices + vector of N
# metaSEM requires matrices with same dimension; use NA for missing
cor_list <- lapply(cor_matrices, function(m) {
  # Ensure 12x12 with proper names
  stopifnot(all(dim(m) == c(N_CONSTRUCTS, N_CONSTRUCTS)))
  m
})

n_vec <- sample_sizes[names(cor_list)]

# Remove studies with missing sample size
valid <- !is.na(n_vec)
cor_list <- cor_list[valid]
n_vec <- n_vec[valid]

message(paste("Final dataset:", length(cor_list), "studies"))
message(paste("Total N:", sum(n_vec)))
message(paste("Harmonic mean N:", round(harmonic_mean(n_vec), 0)))

# =============================================================================
# 7. Create r-only Subset (for sensitivity analysis)
# =============================================================================

message("--- Step 7: Creating r-only subset ---")

r_only_studies <- cor_data %>%
  filter(r_source == "reported") %>%
  distinct(study_id) %>%
  pull(study_id)

cor_list_r_only <- cor_list[names(cor_list) %in% r_only_studies]
n_vec_r_only <- n_vec[names(n_vec) %in% r_only_studies]

message(paste("r-only subset:", length(cor_list_r_only), "studies"))
message(paste("Studies with β→r conversion:",
              length(cor_list) - length(cor_list_r_only)))

# =============================================================================
# 8. Save Prepared Data
# =============================================================================

message("--- Step 8: Saving prepared data ---")

prepared_data <- list(
  cor_matrices    = cor_list,
  sample_sizes    = n_vec,
  cor_matrices_r_only = cor_list_r_only,
  sample_sizes_r_only = n_vec_r_only,
  pair_coverage   = pair_coverage,
  study_constructs = study_constructs,
  pd_results      = pd_results,
  study_metadata  = study_meta
)

saveRDS(prepared_data, file.path(PATHS$pooled, "prepared_data.rds"))

# Save coverage matrix as CSV
write.csv(pair_coverage, file.path(PATHS$output, "pair_coverage_matrix.csv"))

message("=== Data Preparation Complete ===")
