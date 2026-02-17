# Network Analysis Protocol (MAGNA)

## Overview

This protocol describes Meta-Analytic Gaussian Network Aggregation (MAGNA) as a complementary approach to MASEM in educational AI adoption research. Network analysis provides an exploratory, data-driven perspective on construct relationships without imposing directional assumptions, allowing triangulation with MASEM findings.

---

## 1. Rationale for Network Analysis

### 1.1 Why Add Network Analysis to MASEM?

**MASEM Strengths:**
- Tests specific theoretical models
- Provides directional path coefficients
- Confirms or disconfirms hypothesized structures

**MASEM Limitations:**
- Requires a priori model specification
- May miss unexpected relationships
- Assumes directed relationships (X→Y, not just X—Y)

**Network Analysis Strengths:**
- Exploratory (data-driven, not theory-driven)
- Identifies central constructs in the network
- Reveals unexpected connections
- No directional assumptions (undirected edges)

**Complementarity:**
- MASEM: Confirmatory ("Does Model 2 fit?")
- Network: Exploratory ("What is the natural structure?")
- **Triangulation:** Do MASEM paths align with strong network edges?

---

### 1.2 What is MAGNA?

**Meta-Analytic Gaussian Network Aggregation (MAGNA):**

**Definition:** Estimates a partial correlation network from meta-analytically pooled correlations, where edges represent conditional dependencies (controlling for all other variables).

**Key Concepts:**

**Nodes:** Constructs (our 12: PE, EE, SI, FC, BI, UB, ATT, SE, TRU, ANX, TRA, AUT)

**Edges:** Partial correlations (relationship between two constructs controlling for all others)
- **Example:** PE—BI edge represents PE-BI relationship *after controlling for* EE, SI, FC, ATT, TRU, ANX, etc.

**Network Structure:** Which constructs are directly connected vs. indirectly connected through others?

---

## 2. Network Estimation Method

### 2.1 Gaussian Graphical Model (GGM)

**Model:** Assume constructs follow multivariate normal distribution

**Goal:** Estimate **partial correlation matrix** (Θ)

**Partial Correlation:**
```
ρ_ij|rest = Correlation between i and j, controlling for all other variables
```

**Interpretation:**
- ρ_ij|rest ≠ 0: Direct relationship (edge present)
- ρ_ij|rest = 0: No direct relationship (edge absent, relationship is mediated)

---

### 2.2 Regularization: Graphical LASSO

**Problem:** With 12 constructs, there are 66 possible edges. Many may be spurious (type I errors).

**Solution:** Graphical LASSO (Least Absolute Shrinkage and Selection Operator)

**Method:**
- Penalizes small partial correlations
- Shrinks trivial edges to exactly zero
- Produces **sparse network** (only meaningful edges retained)

**Tuning Parameter (λ):**
- λ = 0: No regularization (all edges present)
- λ large: Heavy regularization (very sparse network, few edges)
- **Optimal λ:** Selected via cross-validation (EBIC - Extended Bayesian Information Criterion)

**Formula:**
```
Minimize: -log(det(Θ)) + trace(S*Θ) + λ * ||Θ||_1

where:
  Θ = partial correlation matrix
  S = pooled correlation matrix (from TSSEM Stage 1)
  ||Θ||_1 = sum of absolute values of off-diagonal elements
```

---

### 2.3 Implementation (R)

**Software:** `qgraph` and `bootnet` packages

**Step 1: Estimate Network**

```r
library(qgraph)
library(bootnet)

# Use pooled correlation matrix from TSSEM Stage 1
pooled_cor <- vec2symMat(coef(stage1), diag = FALSE)

# Estimate GGM with LASSO regularization
network <- estimateNetwork(pooled_cor,
                           default = "EBICglasso",  # EBIC model selection
                           corMethod = "cor",
                           threshold = FALSE)       # Do not threshold edges

# View network
plot(network,
     layout = "spring",
     labels = c("PE", "EE", "SI", "FC", "BI", "UB",
                "ATT", "SE", "TRU", "ANX", "TRA", "AUT"))
```

**Step 2: Extract Edge Weights**

```r
# Partial correlation matrix (edge weights)
edge_weights <- getWmat(network)
print(edge_weights)

# Which edges are present (non-zero)?
edges_present <- edge_weights != 0
sum(edges_present) / 2  # Number of edges (divide by 2 for undirected)
```

---

## 3. Centrality Measures

### 3.1 Purpose

**Centrality:** Importance of a construct in the network

**Question:** Which constructs are most central to AI adoption?

**Applications:**
- Identify key intervention targets (high-centrality constructs)
- Understand which constructs are "hubs" connecting others
- Compare centrality across subgroups (generative vs. predictive AI)

---

### 3.2 Centrality Indices

**Strength Centrality:**

**Definition:** Sum of absolute edge weights connected to a node

**Formula:**
```
Strength_i = Σ |ρ_ij|  (sum over all j ≠ i)
```

**Interpretation:**
- High strength = construct is strongly connected to many others
- Low strength = construct is peripheral (few or weak connections)

**Example:**
- If BI has high strength → BI is central (connected to PE, EE, SI, ATT, TRU, etc.)
- If AUT has low strength → AUT is peripheral (few strong connections)

---

**Betweenness Centrality:**

**Definition:** How often a node lies on the shortest path between other nodes

**Interpretation:**
- High betweenness = construct is a "bridge" between other constructs
- Low betweenness = construct is not a bridge (other paths available)

**Example:**
- If ATT has high betweenness → ATT mediates many relationships (e.g., PE→ATT→BI)
- If TRA has low betweenness → TRA does not mediate (direct connections dominate)

---

**Closeness Centrality:**

**Definition:** Average shortest path length from a node to all other nodes

**Interpretation:**
- High closeness = construct is close to all others (few intermediaries)
- Low closeness = construct is distant (many intermediaries)

**Less useful in dense networks (most nodes connected)**

---

**Expected Influence:**

**Definition:** Sum of edge weights (signed, not absolute)

**Formula:**
```
ExpectedInfluence_i = Σ ρ_ij  (sum over all j ≠ i, with signs)
```

**Advantage over strength:**
- Accounts for negative edges (e.g., ANX→BI is negative)
- More appropriate for psychological networks

**Interpretation:**
- High expected influence = activating this node activates many others
- Negative expected influence = activating this node deactivates others (e.g., ANX)

---

### 3.3 Computing Centrality (R)

```r
# Compute centrality indices
centrality_indices <- centrality(network)

# Plot centrality
centralityPlot(network,
               include = c("Strength", "Betweenness", "ExpectedInfluence"))

# Extract values
strength <- centrality_indices$OutDegree  # Strength
betweenness <- centrality_indices$Betweenness
expected_influence <- centrality_indices$ExpectedInfluence

# Rank constructs by strength
ranked_strength <- sort(strength, decreasing = TRUE)
print(ranked_strength)
```

**Expected Results:**

| Rank | Construct | Strength | Interpretation |
|------|-----------|----------|----------------|
| 1 | BI | 5.2 | Most central (intention is hub) |
| 2 | ATT | 4.8 | Highly connected (attitude mediates) |
| 3 | PE | 4.5 | Strong connections to BI, ATT, others |
| 4 | TRU | 3.9 | Important for AI (connected to BI, TRA) |
| 5 | EE | 3.7 | Moderately central |
| ... | ... | ... | ... |
| 12 | AUT | 2.1 | Peripheral (few connections) |

---

## 4. Network Stability and Accuracy

### 4.1 Edge Weight Accuracy

**Problem:** Are estimated edge weights accurate, or are they uncertain?

**Solution:** Nonparametric bootstrap

**Method:**
1. Resample studies with replacement (bootstrap sample)
2. Re-estimate network on bootstrap sample
3. Repeat 1,000 times
4. Compute 95% confidence intervals for each edge weight

**Implementation:**

```r
# Bootstrap edge weights
boot_edges <- bootnet(network,
                      nBoots = 1000,
                      type = "nonparametric",
                      nCores = 4)

# Plot 95% CI for edges
plot(boot_edges,
     labels = FALSE,
     order = "sample")

# Test if edges differ significantly from zero
summary(boot_edges)
```

**Interpretation:**
- If 95% CI includes zero → edge is not significantly different from zero (may be spurious)
- If 95% CI excludes zero → edge is robust

---

### 4.2 Centrality Stability

**Problem:** Are centrality estimates stable, or do they change dramatically if we drop some studies?

**Solution:** Case-dropping bootstrap (subset bootstrap)

**Method:**
1. Drop increasing percentages of studies (10%, 20%, ..., 90%)
2. Re-estimate network and centrality on remaining studies
3. Correlate original centrality with subset centrality
4. **CS-coefficient:** Maximum percentage of studies that can be dropped while maintaining correlation > 0.7

**Target:** CS-coefficient > 0.50 (can drop 50% of studies and still maintain order)

**Implementation:**

```r
# Case-dropping bootstrap for centrality stability
boot_centrality <- bootnet(network,
                           nBoots = 1000,
                           type = "case",
                           nCores = 4)

# Plot stability
plot(boot_centrality,
     statistics = c("strength", "expectedInfluence"))

# CS-coefficient
corStability(boot_centrality)
```

**Interpretation:**
- CS > 0.50: Excellent stability
- CS = 0.25-0.50: Acceptable stability
- CS < 0.25: Poor stability (centrality order not reliable)

**If CS < 0.50:**
- Interpret centrality rankings with caution
- Focus on clear differences (e.g., top vs. bottom centrality)
- Avoid over-interpreting small differences

---

### 4.3 Edge Difference Testing

**Question:** Is edge A significantly stronger than edge B?

**Method:** Bootstrap difference test

**Example:** Is PE—BI edge stronger than EE—BI edge?

```r
# Test edge differences
differenceTest(boot_edges,
               x = "PE--BI",
               y = "EE--BI",
               alpha = 0.05)
```

**Output:**
- p-value: If p < .05 → edges are significantly different
- If p > .05 → edges are not significantly different (could be equal)

---

## 5. Network Comparison (Subgroups)

### 5.1 Research Question

**Question:** Does the network structure differ between student and instructor subgroups, or between K-12 and higher education contexts?

**Hypothesis:**
- Students: TRU—BI edge stronger (trust in AI accuracy matters more for learning)
- Instructors: PE—BI edge stronger (pedagogical performance matters more)
- K-12: SI—BI edge stronger (peer/administrator influence matters more in structured settings)
- Higher Education: ATT—BI edge stronger (autonomous learner attitudes dominate)

---

### 5.2 Network Comparison Test (NCT)

**Method:** Permutation test comparing two networks

**Null Hypothesis:** Networks are identical

**Test Statistics:**
1. **Global strength invariance:** Do networks have equal total connectivity?
2. **Network structure invariance:** Are edge patterns identical?
3. **Edge-specific invariance:** Are specific edges equal across networks?

**Implementation:**

```r
library(NetworkComparisonTest)

# Split data by user role (student vs instructor)
cor_student <- cor_matrices[user_role == "Student"]
cor_instructor <- cor_matrices[user_role == "Instructor"]

# Pool correlations separately
stage1_student <- tssem1(Cov = cor_student, n = n_student)
stage1_instructor <- tssem1(Cov = cor_instructor, n = n_instructor)

pooled_cor_student <- vec2symMat(coef(stage1_student), diag = FALSE)
pooled_cor_instructor <- vec2symMat(coef(stage1_instructor), diag = FALSE)

# Estimate networks
net_student <- estimateNetwork(pooled_cor_student, default = "EBICglasso")
net_instructor <- estimateNetwork(pooled_cor_instructor, default = "EBICglasso")

# Network Comparison Test
nct_result <- NCT(net_student, net_instructor,
                  it = 1000,           # 1000 permutations
                  test.edges = TRUE,   # Test individual edges
                  edges = "all")       # Test all edges

# View results
print(nct_result)
```

**Output Interpretation:**

**Global Strength:**
- p < .05 → Networks differ in overall connectivity
- Example: Student network is more densely connected than instructor network

**Network Structure:**
- p < .05 → Networks have different edge patterns
- Example: Student network has strong TRU—BI edge, instructor network has strong PE—BI edge

**Edge-Specific:**
- p < .05 for specific edge → That edge differs between networks
- Example: TRU—BI edge is significantly stronger in student network (trust in AI accuracy critical for learning)

---

### 5.3 Visualization of Subgroup Networks

**Plot networks side-by-side:**

```r
# Set common layout for comparison
layout <- averageLayout(net_student, net_instructor)

# Plot student network
plot(net_student,
     layout = layout,
     title = "Student Educational AI Network",
     theme = "colorblind")

# Plot instructor network
plot(net_instructor,
     layout = layout,
     title = "Instructor Educational AI Network",
     theme = "colorblind")
```

**Visual Comparison:**
- Thicker edges = stronger partial correlations
- Red edges = negative partial correlations
- Gray edges = absent (regularized to zero)

---

## 6. Community Detection

### 6.1 Purpose

**Question:** Do constructs cluster into communities (subnetworks)?

**Hypothesis:**
- Traditional TAM/UTAUT cluster (PE, EE, SI, FC, ATT, BI, UB)
- AI-specific cluster (TRU, ANX, TRA, AUT, SE)

**Method:** Walktrap algorithm (random walks to detect communities)

---

### 6.2 Implementation

```r
library(igraph)

# Convert qgraph network to igraph object
igraph_net <- as.igraph(network, attributes = TRUE)

# Walktrap community detection
communities <- cluster_walktrap(igraph_net)

# Number of communities
n_communities <- length(communities)

# Membership
membership <- membership(communities)
print(membership)

# Modularity (how well-separated are communities?)
modularity <- modularity(communities)
print(paste("Modularity =", modularity))
```

**Output:**

```
PE: Community 1
EE: Community 1
SI: Community 1
FC: Community 1
ATT: Community 1
BI: Community 1
UB: Community 1
SE: Community 2
TRU: Community 2
ANX: Community 2
TRA: Community 2
AUT: Community 2

Modularity = 0.42
```

**Interpretation:**
- 2 communities detected
- Community 1: Traditional TAM/UTAUT constructs
- Community 2: AI-specific constructs
- Modularity = 0.42 (moderate separation; >0.3 is meaningful)

---

### 6.3 Visualization with Communities

```r
# Plot network with communities colored
plot(network,
     layout = "spring",
     groups = membership,
     color = c("lightblue", "lightcoral"),
     legend.cex = 0.5,
     title = "AI Adoption Network with Communities")
```

---

## 7. Bridge Centrality

### 7.1 Purpose

**Bridge Constructs:** Nodes that connect different communities

**Question:** Which constructs bridge traditional TAM/UTAUT and AI-specific communities?

**Hypothesis:** ATT or BI may bridge (influenced by both traditional and AI factors)

---

### 7.2 Bridge Strength

**Definition:** Sum of edge weights connecting a node to other communities

**Formula:**
```
BridgeStrength_i = Σ |ρ_ij|  where i and j are in different communities
```

**Interpretation:**
- High bridge strength = construct connects communities (critical integrator)
- Low bridge strength = construct is within-community only

**Implementation:**

```r
library(networktools)

# Compute bridge centrality
bridge <- bridge(network,
                 communities = membership)

# Plot bridge strength
plot(bridge$`Bridge Strength`)
```

**Expected Results:**

| Construct | Bridge Strength | Role |
|-----------|----------------|------|
| ATT | 2.8 | Strong bridge (connected to PE, EE and TRU, ANX) |
| BI | 2.5 | Strong bridge (outcome influenced by both communities) |
| SE | 1.9 | Moderate bridge (connected to EE and ANX) |
| TRU | 1.2 | Weak bridge (mostly within AI-specific community) |

**Interpretation:**
- ATT and BI are critical bridges integrating traditional and AI-specific factors
- Interventions targeting ATT or BI may leverage both communities

---

## 8. Triangulation with MASEM

### 8.1 Comparing Network Edges to MASEM Paths

**Question:** Do strong network edges align with significant MASEM paths?

**Method:**

**Step 1: Extract MASEM paths**

```r
# From TSSEM Stage 2 Model 2 (Integrated)
masem_paths <- coef(model2)
masem_paths_significant <- masem_paths[abs(masem_paths) > 0.10]
```

**Step 2: Extract network edges**

```r
# From network analysis
network_edges <- edge_weights[abs(edge_weights) > 0.10]
```

**Step 3: Compare**

| Relationship | MASEM Path (β) | Network Edge (ρ) | Agree? |
|--------------|----------------|------------------|--------|
| PE → BI | 0.35*** | PE—BI: 0.28 | ✓ Yes (both strong) |
| EE → BI | 0.28*** | EE—BI: 0.15 | ✓ Yes (both present) |
| TRU → BI | 0.32*** | TRU—BI: 0.25 | ✓ Yes (both strong) |
| ANX → BI | -0.18*** | ANX—BI: -0.12 | ✓ Yes (both negative) |
| PE → ATT | 0.50*** | PE—ATT: 0.05 | ✗ Discrepancy |

**Interpretation:**
- **Convergence:** Most MASEM paths align with network edges (triangulation successful)
- **Discrepancy (PE—ATT):** MASEM shows strong path (.50), network shows weak edge (.05)
  - **Explanation:** Network edge is *partial* correlation (controlling for EE, BI, etc.)
  - PE→ATT relationship may be mediated/confounded
  - Network suggests PE→ATT is not direct (goes through other constructs)

---

### 8.2 Unique Insights from Network Analysis

**Unexpected Strong Edges (not in MASEM models):**

Example: Network shows strong SE—TRU edge (ρ=.22) not included in MASEM Model 2

**Implication:**
- Self-efficacy may directly influence trust (not just through EE and ANX)
- Consider adding SE→TRU path in future model refinement

**Absent Expected Edges:**

Example: Network shows zero edge for SI—BI (ρ=.02), but MASEM shows β=.20

**Implication:**
- SI→BI relationship may be fully mediated by ATT or confounded
- SI effect on BI may not be direct after controlling for other constructs

---

## 9. Reporting Network Analysis

### 9.1 Methods Section

"To complement confirmatory MASEM, we conducted exploratory network analysis using Meta-Analytic Gaussian Network Aggregation (MAGNA). We estimated a regularized Gaussian Graphical Model on the pooled correlation matrix from TSSEM Stage 1 using the EBICglasso method in the qgraph package (Epskamp et al., 2012). The resulting network represents partial correlations among constructs (edges) controlling for all other constructs. Network sparsity was determined via Extended Bayesian Information Criterion.

Centrality indices (strength, betweenness, expected influence) were computed to identify key constructs in the educational AI adoption network. Stability was assessed via case-dropping bootstrap (1,000 iterations), with CS-coefficient > 0.50 indicating excellent stability. Edge weight accuracy was evaluated via nonparametric bootstrap (1,000 iterations) with 95% confidence intervals. Network comparison tests (NCT) evaluated whether network structure differed between student and instructor subgroups, and between K-12 and higher education contexts."

---

### 9.2 Results Section

**Network Structure:**

"The estimated network (Figure X) contained 34 edges after LASSO regularization. Behavioral intention (BI) showed the highest strength centrality (S=5.2), followed by attitude (ATT, S=4.8) and performance expectancy (PE, S=4.5), indicating these constructs are most central to the AI adoption network. AI trust (TRU) showed moderate centrality (S=3.9), while perceived AI autonomy (AUT) was peripheral (S=2.1).

Case-dropping bootstrap indicated excellent stability for strength centrality (CS-coefficient = 0.67), suggesting centrality rankings are robust. Edge weight bootstrap revealed that 89% of edges had 95% confidence intervals excluding zero, indicating most edges are stable and non-spurious."

**Subgroup Comparison:**

"Network comparison tests revealed significant differences between student and instructor networks (network structure invariance test: p = .018). The TRU—BI edge was significantly stronger in the student network (ρ=.38) compared to instructor network (ρ=.22, p = .011), supporting the hypothesis that trust in AI accuracy is more critical for students using AI for learning. Conversely, the PE—BI edge was stronger in the instructor network (ρ=.42 vs. .30, p = .028), suggesting pedagogical performance expectancy dominates for instructors integrating AI into teaching."

**Triangulation with MASEM:**

"Network edges largely aligned with MASEM paths, providing convergent evidence. The PE—BI relationship was strong in both MASEM (β=.35) and network analysis (ρ=.28). However, the PE—ATT relationship showed discrepancy: MASEM indicated a strong path (β=.50), while network analysis showed a weak partial correlation (ρ=.05), suggesting the relationship may be mediated by other constructs. This highlights the complementary nature of confirmatory (MASEM) and exploratory (network) approaches."

---

## 10. Academic Contribution

### 10.1 First Network Analysis of AI Adoption

**Novelty:**
- No prior meta-analytic network analysis of AI adoption exists
- Extends network psychometrics to technology adoption domain
- Provides data-driven complement to theory-driven SEM

---

### 10.2 Construct Centrality Insights

**Practical Implications:**
- Identifies high-leverage constructs for interventions
- Example: If BI and ATT are most central → focus on changing attitudes and intentions (they have ripple effects)
- Example: If AUT is peripheral → autonomy concerns may be less critical than assumed

---

### 10.3 Methodological Triangulation

**Demonstrates:**
- Convergence between MASEM and network analysis strengthens conclusions
- Divergence reveals hidden complexity (e.g., mediation, confounding)
- Multi-method approach increases rigor

---

## References

Epskamp, S., Cramer, A. O., Waldorp, L. J., Schmittmann, V. D., & Borsboom, D. (2012). qgraph: Network visualizations of relationships in psychometric data. *Journal of Statistical Software*, 48(4), 1-18.

Epskamp, S., Borsboom, D., & Fried, E. I. (2018). Estimating psychological networks and their accuracy: A tutorial paper. *Behavior Research Methods*, 50(1), 195-212.

Jones, P. J., Ma, R., & McNally, R. J. (2021). Bridge centrality: A network approach to understanding comorbidity. *Multivariate Behavioral Research*, 56(2), 353-367.

van Borkulo, C. D., van Bork, R., Boschloo, L., Kossakowski, J. J., Tio, P., Schoevers, R. A., ... & Waldorp, L. J. (2022). Comparing network structures on three aspects: A permutation test. *Psychological Methods*.
