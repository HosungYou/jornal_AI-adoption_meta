# ==============================================================================
# 12_network_analysis.R — Network Analysis (MAGNA)
# AI Adoption MASEM Dissertation
# ==============================================================================
# Purpose: KEY INNOVATION — Meta-Analytic Gaussian Network Aggregation
#   - Gaussian Graphical Model from pooled correlation matrix
#   - Graphical LASSO regularization and model search
#   - Centrality indices: strength, betweenness, closeness, expected influence
#   - Bootstrap stability analysis (CS-coefficient)
#   - Bridge centrality between theoretical communities
#   - Subgroup comparison (Generative vs Predictive AI) via NCT
#   - Triangulation with SEM path analysis
# Dependencies: 00_setup.R, stage1_results.rds, prepared_data.rds
# Output: network_results.rds, network plots, centrality tables
# ==============================================================================

source("analysis/R/00_setup.R")
message("\n", strrep("=", 70))
message("12: NETWORK ANALYSIS — MAGNA (Meta-Analytic Gaussian Network)")
message(strrep("=", 70))
message("    *** KEY INNOVATION: Network Perspective on AI Adoption ***")

# ==============================================================================
# 1. LOAD DATA
# ==============================================================================
message("\n--- Loading data ---")
stage1   <- readRDS(file.path(PATHS$pooled, "stage1_results.rds"))
prepared <- readRDS(file.path(PATHS$pooled, "prepared_data.rds"))

pooled_matrix <- stage1$pooled_matrix
harmonic_n    <- stage1$harmonic_n
n_studies     <- stage1$n_studies
metadata      <- prepared$study_metadata

message(sprintf("  Pooled correlation matrix: %d x %d", nrow(pooled_matrix), ncol(pooled_matrix)))
message(sprintf("  Harmonic N: %.0f", harmonic_n))
message(sprintf("  Studies: %d", n_studies))

# Ensure PD
pd_check <- check_positive_definite(pooled_matrix)
if (!pd_check$is_pd) {
  message("  Pooled matrix not PD — using nearest PD")
  pooled_matrix <- pd_check$nearest_pd
}

# ==============================================================================
# 2. GAUSSIAN GRAPHICAL MODEL (GGM) ESTIMATION
# ==============================================================================
message("\n--- Estimating Gaussian Graphical Model ---")

# 2a. Using psychonetrics
message("\n  [psychonetrics GGM estimation]")

ggm_model <- NULL
tryCatch({
  # Generate data from pooled matrix for psychonetrics
  set.seed(42)
  n_sim <- round(harmonic_n)
  sim_data <- MASS::mvrnorm(n = n_sim, mu = rep(0, N_CONSTRUCTS),
                             Sigma = pooled_matrix)
  sim_data <- as.data.frame(sim_data)
  colnames(sim_data) <- CONSTRUCTS

  # Fit saturated GGM
  ggm_model <- ggm(sim_data, vars = CONSTRUCTS, estimator = "ML")
  ggm_model <- ggm_model %>% runmodel()

  message(sprintf("  GGM fitted: %d nodes, %d potential edges",
                  N_CONSTRUCTS, N_PAIRS))

  # Model search: prune non-significant edges
  message("  Running model search (pruning non-significant edges)...")
  ggm_pruned <- ggm_model %>%
    prune(alpha = 0.01, adjust = "fdr") %>%
    runmodel()

  # Extract partial correlation (omega) matrix
  omega_matrix <- getmatrix(ggm_pruned, "omega")
  rownames(omega_matrix) <- colnames(omega_matrix) <- CONSTRUCTS

  n_edges <- sum(omega_matrix[lower.tri(omega_matrix)] != 0)
  n_possible <- N_PAIRS
  density <- n_edges / n_possible

  message(sprintf("  Pruned network: %d edges / %d possible (density = %.2f)",
                  n_edges, n_possible, density))

}, error = function(e) {
  message(sprintf("  psychonetrics GGM failed: %s", e$message))
  message("  Falling back to direct partial correlation estimation...")

  # Fallback: compute partial correlations directly
  tryCatch({
    # Partial correlations from inverse of correlation matrix
    precision <- solve(pooled_matrix)
    omega_matrix <<- -cov2cor(precision)
    diag(omega_matrix) <<- 0
    rownames(omega_matrix) <<- colnames(omega_matrix) <<- CONSTRUCTS

    # Apply graphical LASSO via EBICglasso from qgraph
    ggm_ebic <- EBICglasso(pooled_matrix, n = round(harmonic_n), gamma = 0.5)
    omega_matrix <<- ggm_ebic
    rownames(omega_matrix) <<- colnames(omega_matrix) <<- CONSTRUCTS

    n_edges <- sum(omega_matrix[lower.tri(omega_matrix)] != 0)
    message(sprintf("  EBICglasso network: %d non-zero edges", n_edges))

  }, error = function(e2) {
    message(sprintf("  Fallback also failed: %s", e2$message))
    omega_matrix <<- NULL
  })
})

# ==============================================================================
# 3. NETWORK VISUALIZATION
# ==============================================================================
message("\n--- Creating network visualization ---")

if (!is.null(omega_matrix)) {
  # Define node groups for color coding
  node_groups <- list(
    "TAM/UTAUT" = c("PE", "EE", "SI", "FC"),
    "AI-Specific" = c("TRU", "ANX", "TRA", "AUT"),
    "Mediator/Outcome" = c("BI", "UB", "ATT", "SE")
  )

  # Create group vector
  group_vec <- rep(NA, N_CONSTRUCTS)
  names(group_vec) <- CONSTRUCTS
  for (g in names(node_groups)) {
    group_vec[node_groups[[g]]] <- g
  }
  group_factor <- factor(group_vec)

  # Color scheme
  group_colors <- c("TAM/UTAUT" = "#3288BD",
                    "AI-Specific" = "#D53E4F",
                    "Mediator/Outcome" = "#66C2A5")
  node_colors <- group_colors[as.character(group_factor)]

  # Compute strength centrality for node sizing
  strength <- colSums(abs(omega_matrix))
  node_sizes <- 4 + 6 * (strength - min(strength)) / (max(strength) - min(strength) + 0.01)

  # Main network plot
  tryCatch({
    png(file.path(PATHS$figures, "network_main.png"),
        width = 10, height = 10, units = "in", res = 300)

    network_layout <- qgraph(
      omega_matrix,
      layout = "spring",
      labels = CONSTRUCTS,
      nodeNames = CONSTRUCT_LABELS,
      groups = as.list(node_groups),
      color = group_colors,
      vsize = node_sizes,
      esize = 10,
      edge.width = 1.5,
      maximum = max(abs(omega_matrix[omega_matrix != 0])),
      cut = 0,
      borders = TRUE,
      border.width = 1.5,
      posCol = "#2166AC",
      negCol = "#B2182B",
      negDashed = TRUE,
      title = "AI Adoption Network (MAGNA)",
      legend = TRUE,
      legend.cex = 0.6,
      mar = c(5, 5, 5, 5)
    )

    dev.off()
    message("  Network plot saved")

    # Save layout for consistent plotting
    saved_layout <- network_layout$layout

  }, error = function(e) {
    message(sprintf("  Network plot failed: %s", e$message))
    try(dev.off(), silent = TRUE)
    saved_layout <- NULL
  })

  # PDF version
  tryCatch({
    pdf(file.path(PATHS$figures, "network_main.pdf"), width = 10, height = 10)
    qgraph(omega_matrix, layout = "spring", labels = CONSTRUCTS,
           groups = as.list(node_groups), color = group_colors,
           vsize = node_sizes, esize = 10, posCol = "#2166AC",
           negCol = "#B2182B", negDashed = TRUE,
           title = "AI Adoption Network (MAGNA)")
    dev.off()
  }, error = function(e) {
    try(dev.off(), silent = TRUE)
  })
}

# ==============================================================================
# 4. CENTRALITY ANALYSIS
# ==============================================================================
message("\n--- Computing centrality indices ---")

centrality_table <- NULL

if (!is.null(omega_matrix)) {
  tryCatch({
    # Compute centrality from the network
    cent <- centralityTable(omega_matrix)

    # Also compute Expected Influence (EI)
    ei_1step <- expectedInf(omega_matrix, step = 1)
    ei_2step <- expectedInf(omega_matrix, step = 2)

    # Build comprehensive centrality table
    centrality_table <- data.frame(
      Construct = CONSTRUCTS,
      Label = CONSTRUCT_LABELS[CONSTRUCTS],
      Group = as.character(group_factor),
      Strength = round(colSums(abs(omega_matrix)), 4),
      stringsAsFactors = FALSE
    )

    # Add centrality measures from centralityTable
    for (measure in unique(cent$measure)) {
      vals <- cent$value[cent$measure == measure]
      names(vals) <- cent$node[cent$measure == measure]
      centrality_table[[measure]] <- round(vals[CONSTRUCTS], 4)
    }

    # Add expected influence
    centrality_table$EI_1step <- round(as.numeric(ei_1step$step1), 4)
    centrality_table$EI_2step <- round(as.numeric(ei_2step$step2), 4)

    # Sort by strength
    centrality_table <- centrality_table[order(-centrality_table$Strength), ]

    message("\n  Centrality Rankings (by Strength):")
    print(centrality_table[, c("Construct", "Group", "Strength",
                                "Betweenness", "Closeness",
                                "EI_1step", "EI_2step")],
          row.names = FALSE)

    # Identify most central constructs
    top3 <- head(centrality_table$Construct, 3)
    message(sprintf("\n  Top 3 most central constructs: %s", paste(top3, collapse = ", ")))

    # Centrality plot
    tryCatch({
      png(file.path(PATHS$figures, "network_centrality.png"),
          width = 10, height = 8, units = "in", res = 300)
      centralityPlot(omega_matrix, include = c("Strength", "Betweenness",
                                                "Closeness", "ExpectedInfluence"),
                     orderBy = "Strength")
      dev.off()
      message("  Centrality plot saved")
    }, error = function(e) {
      message(sprintf("  Centrality plot failed: %s", e$message))
      try(dev.off(), silent = TRUE)
    })

  }, error = function(e) {
    message(sprintf("  Centrality computation failed: %s", e$message))
  })
}

# ==============================================================================
# 5. BOOTSTRAP STABILITY ANALYSIS
# ==============================================================================
message("\n--- Bootstrap stability analysis ---")
message("    (1000 bootstrap samples — this may take several minutes)")

boot_results <- NULL

if (!is.null(omega_matrix)) {
  tryCatch({
    # Generate data for bootnet
    set.seed(42)
    n_boot_data <- round(harmonic_n)
    boot_data <- MASS::mvrnorm(n = n_boot_data, mu = rep(0, N_CONSTRUCTS),
                                Sigma = pooled_matrix)
    boot_data <- as.data.frame(boot_data)
    colnames(boot_data) <- CONSTRUCTS

    # Estimate network with bootnet
    net_est <- estimateNetwork(boot_data, default = "EBICglasso",
                                corMethod = "cor", tuning = 0.5)

    # Non-parametric bootstrap for edge weight accuracy
    message("  Running edge weight bootstrap (1000 iterations)...")
    boot_edge <- bootnet(net_est, nBoots = 1000, type = "nonparametric",
                          nCores = parallel::detectCores() - 1)

    # Case-dropping bootstrap for centrality stability
    message("  Running case-dropping bootstrap (1000 iterations)...")
    boot_case <- bootnet(net_est, nBoots = 1000, type = "case",
                          statistics = c("strength", "betweenness",
                                         "closeness", "expectedInfluence"),
                          nCores = parallel::detectCores() - 1)

    boot_results <- list(
      network = net_est,
      boot_edge = boot_edge,
      boot_case = boot_case
    )

    # CS-coefficient (centrality stability)
    cs_strength <- corStability(boot_case, statistics = "strength")
    cs_betweenness <- corStability(boot_case, statistics = "betweenness")
    cs_closeness <- corStability(boot_case, statistics = "closeness")
    cs_ei <- corStability(boot_case, statistics = "expectedInfluence")

    message(sprintf("\n  CS-coefficient (should be > 0.50):"))
    message(sprintf("    Strength:          %.2f %s", cs_strength,
                    ifelse(cs_strength > 0.50, "(STABLE)", "(UNSTABLE)")))
    message(sprintf("    Betweenness:       %.2f %s", cs_betweenness,
                    ifelse(cs_betweenness > 0.50, "(STABLE)", "(UNSTABLE)")))
    message(sprintf("    Closeness:         %.2f %s", cs_closeness,
                    ifelse(cs_closeness > 0.50, "(STABLE)", "(UNSTABLE)")))
    message(sprintf("    Expected Influence: %.2f %s", cs_ei,
                    ifelse(cs_ei > 0.50, "(STABLE)", "(UNSTABLE)")))

    boot_results$cs_coefficients <- list(
      strength = cs_strength,
      betweenness = cs_betweenness,
      closeness = cs_closeness,
      expectedInfluence = cs_ei
    )

    # Save bootstrap plots
    tryCatch({
      png(file.path(PATHS$figures, "network_edge_bootstrap.png"),
          width = 12, height = 10, units = "in", res = 300)
      plot(boot_edge, labels = FALSE, order = "sample",
           main = "Edge Weight Bootstrap (95% CI)")
      dev.off()

      png(file.path(PATHS$figures, "network_centrality_stability.png"),
          width = 10, height = 8, units = "in", res = 300)
      plot(boot_case, statistics = c("strength", "expectedInfluence"),
           main = "Centrality Stability (Case-Dropping Bootstrap)")
      dev.off()

      message("  Bootstrap plots saved")
    }, error = function(e) {
      message(sprintf("  Bootstrap plots failed: %s", e$message))
      try(dev.off(), silent = TRUE)
    })

  }, error = function(e) {
    message(sprintf("  Bootstrap analysis failed: %s", e$message))
    message("  Continuing without bootstrap stability estimates")
  })
}

# ==============================================================================
# 6. BRIDGE CENTRALITY ANALYSIS
# ==============================================================================
message("\n--- Bridge centrality analysis ---")

bridge_results <- NULL

if (!is.null(omega_matrix)) {
  tryCatch({
    # Define communities
    communities <- c(
      PE = 1, EE = 1, SI = 1, FC = 1,     # Traditional UTAUT
      TRU = 2, ANX = 2, TRA = 2, AUT = 2, # AI-specific
      BI = 3, UB = 3, ATT = 3, SE = 3     # Mediating/Outcome
    )

    community_labels <- c("1" = "Traditional UTAUT",
                           "2" = "AI-Specific",
                           "3" = "Mediating/Outcome")

    # Compute bridge centrality
    bridge <- bridge(omega_matrix, communities = communities)

    bridge_table <- data.frame(
      Construct = CONSTRUCTS,
      Community = community_labels[as.character(communities[CONSTRUCTS])],
      Bridge_Strength = round(bridge$`Bridge Strength`, 4),
      Bridge_Betweenness = round(bridge$`Bridge Betweenness`, 4),
      Bridge_Closeness = round(bridge$`Bridge Closeness`, 4),
      Bridge_EI = round(bridge$`Bridge Expected Influence (1-step)`, 4),
      stringsAsFactors = FALSE
    )

    # Sort by bridge strength
    bridge_table <- bridge_table[order(-bridge_table$Bridge_Strength), ]

    message("\n  Bridge Centrality Rankings:")
    print(bridge_table, row.names = FALSE)

    # Identify key bridge constructs
    top_bridges <- head(bridge_table$Construct, 3)
    message(sprintf("\n  Top bridge constructs: %s", paste(top_bridges, collapse = ", ")))
    message("  These constructs most strongly connect different theoretical communities")

    bridge_results <- list(
      bridge_table = bridge_table,
      communities = communities,
      community_labels = community_labels,
      bridge_object = bridge
    )

    # Bridge centrality plot
    tryCatch({
      png(file.path(PATHS$figures, "network_bridge_centrality.png"),
          width = 10, height = 7, units = "in", res = 300)
      plot(bridge, include = c("Bridge Strength",
                                "Bridge Expected Influence (1-step)"),
           order = "value")
      dev.off()
      message("  Bridge centrality plot saved")
    }, error = function(e) {
      message(sprintf("  Bridge plot failed: %s", e$message))
      try(dev.off(), silent = TRUE)
    })

  }, error = function(e) {
    message(sprintf("  Bridge centrality failed: %s", e$message))
  })
}

# ==============================================================================
# 7. SUBGROUP COMPARISON: GENERATIVE vs PREDICTIVE AI
# ==============================================================================
message("\n--- Subgroup comparison: Generative vs Predictive AI ---")

nct_results <- NULL

if ("ai_type" %in% colnames(metadata)) {
  gen_idx  <- which(metadata$ai_type == "generative")
  pred_idx <- which(metadata$ai_type == "predictive")

  message(sprintf("  Generative AI studies: k = %d", length(gen_idx)))
  message(sprintf("  Predictive AI studies: k = %d", length(pred_idx)))

  if (length(gen_idx) >= 10 && length(pred_idx) >= 10) {
    tryCatch({
      # Pool separate correlation matrices for each subgroup
      gen_matrices <- prepared$cor_matrices[gen_idx]
      pred_matrices <- prepared$cor_matrices[pred_idx]
      gen_n <- prepared$sample_sizes[gen_idx]
      pred_n <- prepared$sample_sizes[pred_idx]

      # Pool each subgroup via Stage 1
      stage1_gen <- tssem1(gen_matrices, gen_n, method = "REM",
                           RE.type = "Diag", acov = "weighted")
      stage1_pred <- tssem1(pred_matrices, pred_n, method = "REM",
                            RE.type = "Diag", acov = "weighted")

      pooled_gen <- vec2symMat(coef(stage1_gen, select = "fixed"), diag = FALSE)
      diag(pooled_gen) <- 1
      rownames(pooled_gen) <- colnames(pooled_gen) <- CONSTRUCTS

      pooled_pred <- vec2symMat(coef(stage1_pred, select = "fixed"), diag = FALSE)
      diag(pooled_pred) <- 1
      rownames(pooled_pred) <- colnames(pooled_pred) <- CONSTRUCTS

      # Generate data for NCT
      set.seed(42)
      n_gen_sim <- round(harmonic_mean(gen_n))
      n_pred_sim <- round(harmonic_mean(pred_n))

      data_gen <- MASS::mvrnorm(n = n_gen_sim, mu = rep(0, N_CONSTRUCTS),
                                 Sigma = as.matrix(Matrix::nearPD(pooled_gen, corr = TRUE)$mat))
      data_pred <- MASS::mvrnorm(n = n_pred_sim, mu = rep(0, N_CONSTRUCTS),
                                  Sigma = as.matrix(Matrix::nearPD(pooled_pred, corr = TRUE)$mat))
      data_gen <- as.data.frame(data_gen)
      data_pred <- as.data.frame(data_pred)
      colnames(data_gen) <- colnames(data_pred) <- CONSTRUCTS

      # Network Comparison Test
      message("  Running NCT (1000 permutations — this may take a while)...")

      nct <- NCT(data_gen, data_pred,
                  it = 1000,
                  test.edges = TRUE,
                  test.centrality = TRUE,
                  centrality = c("strength", "expectedInfluence"),
                  progressbar = TRUE)

      nct_results <- list(
        nct = nct,
        n_gen = length(gen_idx),
        n_pred = length(pred_idx)
      )

      # Results
      message("\n  NCT Results:")
      message(sprintf("    Global strength invariance: p = %.4f %s",
                      nct$glstrinv.pval,
                      ifelse(nct$glstrinv.pval < .05, "* (DIFFERENT)", "(invariant)")))
      message(sprintf("    Network structure invariance: p = %.4f %s",
                      nct$nwinv.pval,
                      ifelse(nct$nwinv.pval < .05, "* (DIFFERENT)", "(invariant)")))

      # Edge-level differences
      if (!is.null(nct$einv.pvals)) {
        sig_edges <- sum(nct$einv.pvals < .05, na.rm = TRUE)
        message(sprintf("    Significant edge differences: %d / %d",
                        sig_edges, length(nct$einv.pvals)))
      }

    }, error = function(e) {
      message(sprintf("  NCT failed: %s", e$message))
    })
  } else {
    message("  Insufficient studies in one subgroup (need >= 10 each)")
  }
} else {
  message("  'ai_type' column not found in metadata — skipping subgroup comparison")
}

# ==============================================================================
# 8. TRIANGULATION: NETWORK vs SEM
# ==============================================================================
message("\n--- Triangulation: Network edges vs SEM paths ---")

triangulation <- NULL

if (!is.null(omega_matrix)) {
  # Load TSSEM results
  tssem_path <- file.path(PATHS$output, "tssem_results.rds")

  if (file.exists(tssem_path)) {
    tssem_results <- readRDS(tssem_path)

    # Extract SEM path coefficients
    sem_coefs <- NULL
    if (!is.null(tssem_results$integrated$model)) {
      sem_coefs <- coef(tssem_results$integrated$model)
    } else if (!is.null(tssem_results$integrated$coefficients)) {
      sem_coefs <- tssem_results$integrated$coefficients
    }

    if (!is.null(sem_coefs)) {
      # Compare SEM paths with corresponding network edges
      path_labels <- c("PE_BI", "EE_BI", "SI_BI", "ATT_BI", "TRU_BI", "ANX_BI",
                        "BI_UB", "FC_UB", "PE_ATT", "EE_ATT", "TRA_TRU",
                        "SE_EE", "AUT_ANX", "SE_ANX")

      triangulation <- data.frame(
        Path = character(),
        SEM_Beta = numeric(),
        Network_Edge = numeric(),
        Consistent = logical(),
        stringsAsFactors = FALSE
      )

      for (path in path_labels) {
        parts <- strsplit(path, "_")[[1]]
        if (length(parts) != 2) next
        iv <- parts[1]
        dv <- parts[2]

        sem_val <- if (path %in% names(sem_coefs)) sem_coefs[path] else NA
        net_val <- if (iv %in% CONSTRUCTS && dv %in% CONSTRUCTS) {
          omega_matrix[iv, dv]
        } else NA

        # Consistent if same sign and both non-negligible, or both near zero
        consistent <- if (!is.na(sem_val) && !is.na(net_val)) {
          (sign(sem_val) == sign(net_val)) | (abs(sem_val) < 0.05 & abs(net_val) < 0.05)
        } else NA

        triangulation <- rbind(triangulation, data.frame(
          Path = path,
          SEM_Beta = round(sem_val, 4),
          Network_Edge = round(net_val, 4),
          Consistent = consistent,
          stringsAsFactors = FALSE
        ))
      }

      message("\n  SEM vs Network Comparison:")
      print(triangulation, row.names = FALSE)

      n_consistent <- sum(triangulation$Consistent, na.rm = TRUE)
      n_total <- sum(!is.na(triangulation$Consistent))
      message(sprintf("\n  Consistency: %d / %d paths (%.0f%%)",
                      n_consistent, n_total, 100 * n_consistent / n_total))
    }
  } else {
    message("  TSSEM results not found — skipping triangulation")
  }
}

# ==============================================================================
# 9. NETWORK EDGE WEIGHT TABLE
# ==============================================================================
message("\n--- Network edge weight table ---")

edge_table <- NULL

if (!is.null(omega_matrix)) {
  edge_list <- c()
  for (i in 1:(N_CONSTRUCTS - 1)) {
    for (j in (i + 1):N_CONSTRUCTS) {
      w <- omega_matrix[CONSTRUCTS[i], CONSTRUCTS[j]]
      if (abs(w) > 0.001) {
        edge_list <- rbind(edge_list, data.frame(
          Node1 = CONSTRUCTS[i],
          Node2 = CONSTRUCTS[j],
          Weight = round(w, 4),
          Abs_Weight = round(abs(w), 4),
          Sign = ifelse(w > 0, "+", "-"),
          stringsAsFactors = FALSE
        ))
      }
    }
  }

  if (!is.null(edge_list) && nrow(edge_list) > 0) {
    edge_table <- edge_list[order(-edge_list$Abs_Weight), ]
    rownames(edge_table) <- NULL

    message("\n  Top 15 strongest network edges:")
    print(head(edge_table, 15), row.names = FALSE)

    message(sprintf("\n  Total non-zero edges: %d / %d possible (density = %.2f)",
                    nrow(edge_table), N_PAIRS, nrow(edge_table) / N_PAIRS))
  }
}

# ==============================================================================
# 10. SAVE ALL RESULTS
# ==============================================================================
message("\n--- Saving network analysis results ---")

network_output <- list(
  # Network matrices
  omega_matrix = omega_matrix,
  pooled_matrix = pooled_matrix,

  # Models
  ggm_model = if (exists("ggm_model")) ggm_model else NULL,
  ggm_pruned = if (exists("ggm_pruned")) ggm_pruned else NULL,

  # Centrality
  centrality_table = centrality_table,
  edge_table = edge_table,

  # Bridge centrality
  bridge_results = bridge_results,

  # Bootstrap stability
  boot_results = boot_results,

  # NCT subgroup comparison
  nct_results = nct_results,

  # Triangulation
  triangulation = triangulation,

  # Layout
  layout = if (exists("saved_layout")) saved_layout else NULL,

  # Network properties
  network_properties = list(
    n_nodes = N_CONSTRUCTS,
    n_edges = if (!is.null(edge_table)) nrow(edge_table) else NA,
    density = if (!is.null(edge_table)) nrow(edge_table) / N_PAIRS else NA,
    harmonic_n = harmonic_n,
    n_studies = n_studies
  )
)

saveRDS(network_output, file.path(PATHS$output, "network_results.rds"))
message(sprintf("  Saved to: %s", file.path(PATHS$output, "network_results.rds")))

if (!is.null(centrality_table)) {
  write.csv(centrality_table,
            file.path(PATHS$output, "network_centrality_table.csv"),
            row.names = FALSE)
  message(sprintf("  Centrality table saved to: %s",
                  file.path(PATHS$output, "network_centrality_table.csv")))
}

if (!is.null(edge_table)) {
  write.csv(edge_table,
            file.path(PATHS$output, "network_edge_table.csv"),
            row.names = FALSE)
  message(sprintf("  Edge table saved to: %s",
                  file.path(PATHS$output, "network_edge_table.csv")))
}

message("\n", strrep("=", 70))
message("12: NETWORK ANALYSIS (MAGNA) COMPLETE")
message(strrep("=", 70))
