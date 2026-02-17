# ==============================================================================
# 00_setup.R — Package Installation and Environment Setup
# Educational AI Adoption MASEM Meta-Analysis
# ==============================================================================
# Purpose: Install and load all required R packages for the analysis suite
# Run this script once at the beginning of each session
# ==============================================================================

# --- Package Installation ---
required_packages <- c(
  # Core MASEM
  "metaSEM",       # Meta-Analytic SEM (Cheung, 2015) — TSSEM and OSMASEM
  "OpenMx",        # Backend for metaSEM
  "metafor",       # Univariate meta-analysis, forest plots, publication bias
  "lavaan",        # SEM specification and fitting


  # Robust Variance Estimation
  "clubSandwich",  # Robust variance estimation for dependent effect sizes

  # Bayesian MASEM
  "blavaan",       # Bayesian SEM (Merkle & Rosseel, 2018)
  "brms",          # Bayesian regression (for Bayesian moderator models)
  "bayestestR",    # Bayesian testing utilities (ROPE, BF, pd)
  "posterior",     # Posterior distribution manipulation
  "cmdstanr",      # Stan backend (faster than JAGS)

  # Network Analysis (MAGNA)
  "psychonetrics", # Gaussian Graphical Models, SEM, network models
  "qgraph",        # Network visualization
  "bootnet",       # Bootstrap network estimation and stability
  "networktools",  # Bridge centrality and other network tools
  "NetworkComparisonTest", # Network comparison (NCT)

  # Visualization
  "ggplot2",       # General plotting
  "semPlot",       # SEM path diagrams
  "tidygraph",     # Tidy network data manipulation
  "ggraph",        # ggplot2-based network visualization
  "corrplot",      # Correlation matrix visualization
  "forestplot",    # Forest plots
  "patchwork",     # Plot composition

  # Data Manipulation
  "dplyr",         # Data wrangling
  "tidyr",         # Data reshaping
  "purrr",         # Functional programming
  "readxl",        # Read Excel files
  "writexl",       # Write Excel files
  "readr",         # Fast CSV reading
  "tibble",        # Modern data frames
  "stringr",       # String manipulation

  # Matrix Operations
  "Matrix",        # Sparse and dense matrix operations
  "corpcor",       # Shrinkage correlation estimation, nearPD
  "matrixcalc",    # Matrix validation (is.positive.definite)

  # Publication Bias
  "weightr",       # Vevea & Hedges selection models
  "PublicationBias", # Sensitivity to publication bias (Mathur & VanderWeele)

  # Reporting
  "knitr",         # Dynamic report generation
  "kableExtra",    # Table formatting
  "flextable"      # Flexible tables for Word output
)

# Install missing packages
install_if_missing <- function(pkg) {
  if (!requireNamespace(pkg, quietly = TRUE)) {
    message(paste("Installing:", pkg))
    install.packages(pkg, dependencies = TRUE)
  }
}

invisible(lapply(required_packages, install_if_missing))

# Install cmdstanr separately (not on CRAN)
if (!requireNamespace("cmdstanr", quietly = TRUE)) {
  install.packages("cmdstanr", repos = c("https://mc-stan.org/r-packages/", getOption("repos")))
  cmdstanr::install_cmdstan()
}

# --- Load All Packages ---
suppressPackageStartupMessages({
  library(metaSEM)
  library(OpenMx)
  library(metafor)
  library(lavaan)
  library(clubSandwich)
  library(blavaan)
  library(bayestestR)
  library(posterior)
  library(psychonetrics)
  library(qgraph)
  library(bootnet)
  library(networktools)
  library(ggplot2)
  library(semPlot)
  library(corrplot)
  library(dplyr)
  library(tidyr)
  library(purrr)
  library(readxl)
  library(readr)
  library(Matrix)
  library(corpcor)
  library(weightr)
  library(PublicationBias)
})

# --- Project Configuration ---
PROJECT_ROOT <- here::here()

# Standard construct names and order
CONSTRUCTS <- c("PE", "EE", "SI", "FC", "BI", "UB", "ATT", "SE", "TRU", "ANX", "TRA", "AUT")
N_CONSTRUCTS <- length(CONSTRUCTS)
N_PAIRS <- N_CONSTRUCTS * (N_CONSTRUCTS - 1) / 2  # 66

# Construct full names
CONSTRUCT_LABELS <- c(
  PE  = "Performance Expectancy",
  EE  = "Effort Expectancy",
  SI  = "Social Influence",
  FC  = "Facilitating Conditions",
  BI  = "Behavioral Intention",
  UB  = "Use Behavior",
  ATT = "Attitude",
  SE  = "Self-Efficacy",
  TRU = "AI Trust",
  ANX = "AI Anxiety",
  TRA = "AI Transparency",
  AUT = "Perceived AI Autonomy"
)

# Data paths
PATHS <- list(
  raw        = file.path(PROJECT_ROOT, "data", "00_raw"),
  extracted  = file.path(PROJECT_ROOT, "data", "01_extracted"),
  verified   = file.path(PROJECT_ROOT, "data", "02_verified"),
  pooled     = file.path(PROJECT_ROOT, "data", "03_pooled"),
  final      = file.path(PROJECT_ROOT, "data", "04_final"),
  output     = file.path(PROJECT_ROOT, "analysis", "output"),
  figures    = file.path(PROJECT_ROOT, "figures", "output")
)

# Create output directories if needed
invisible(lapply(PATHS, dir.create, recursive = TRUE, showWarnings = FALSE))

# --- Utility Functions ---

#' Convert long-format correlations to a symmetric correlation matrix
#' @param df Data frame with columns: row_construct, col_construct, r
#' @param constructs Character vector of construct names (determines order)
#' @return Symmetric correlation matrix
long_to_matrix <- function(df, constructs = CONSTRUCTS) {
  p <- length(constructs)
  mat <- diag(p)
  rownames(mat) <- colnames(mat) <- constructs

  for (i in seq_len(nrow(df))) {
    row_c <- df$row_construct[i]
    col_c <- df$col_construct[i]
    if (row_c %in% constructs && col_c %in% constructs) {
      mat[row_c, col_c] <- df$r[i]
      mat[col_c, row_c] <- df$r[i]
    }
  }
  return(mat)
}

#' Check if a matrix is positive definite
#' @param mat A correlation matrix
#' @return List with is_pd (logical), min_eigenvalue, and nearest PD matrix if needed
check_positive_definite <- function(mat) {
  eigenvalues <- eigen(mat, only.values = TRUE)$values
  is_pd <- all(eigenvalues > 0)

  result <- list(
    is_pd = is_pd,
    min_eigenvalue = min(eigenvalues),
    eigenvalues = eigenvalues
  )

  if (!is_pd) {
    message("Matrix is NOT positive definite. Nearest PD matrix computed.")
    result$nearest_pd <- as.matrix(Matrix::nearPD(mat, corr = TRUE)$mat)
  }

  return(result)
}

#' Peterson & Brown (2005) beta-to-r conversion
#' @param beta Standardized regression coefficient
#' @return Approximate Pearson correlation
beta_to_r <- function(beta) {
  lambda <- ifelse(beta >= 0, 1, -1)
  r <- beta + 0.05 * lambda
  # Bound to [-1, 1]
  r <- pmax(pmin(r, 1), -1)
  return(r)
}

#' Compute harmonic mean of sample sizes
#' @param n_vector Vector of sample sizes
#' @return Harmonic mean
harmonic_mean <- function(n_vector) {
  n_vector <- n_vector[n_vector > 0 & !is.na(n_vector)]
  length(n_vector) / sum(1 / n_vector)
}

message("=== Educational AI Adoption MASEM: Setup Complete ===")
message(paste("Constructs:", N_CONSTRUCTS))
message(paste("Pairwise correlations:", N_PAIRS))
message(paste("Project root:", PROJECT_ROOT))
