# Phase 2 Exclusion Source Check

Date: 2026-05-25

This source check distinguishes confirmed exclusions from coder-return statuses that need adjudication before the source-anchored adjudicated human reference standard is frozen.

## Confirmed Exclusions

### S039

- Code: `E-FT3`
- Rationale: Dental-patient acceptance of AI-powered diagnosis in a clinical dental setting; the focal use case is healthcare diagnosis rather than educational AI adoption.
- Source location: Abstract; Methods: study design and participants
- Short source excerpt: "AI-powered diagnosis"
- Affected coder returns: R2 excluded; R3 no coded values

### S101

- Code: `E-FT1`
- Rationale: Uses ANN predictive-accuracy models and factor-loading summaries rather than a usable inter-construct correlation matrix or standardized target path coefficients.
- Source location: Methods: Artificial Neural Networks model; Results Tables 5-6
- Short source excerpt: "Artificial Neural Networks (ANN)"
- Affected coder returns: R2 excluded; R3 no coded values

### S108

- Code: `E-FT1`
- Rationale: Reports TAM/RIMMS group mean comparisons and t-tests for maker-education motivation/acceptance; no usable target construct-pair r or standardized path matrix.
- Source location: Methods 2.2; Results Table 2
- Short source excerpt: "comparison was made between the perceptions"
- Affected coder returns: R1 excluded; R4 coded an effect-size row

### S118

- Code: `E-FT1`
- Rationale: Reports descriptive acceptance results and Spearman correlations between GenAI use frequency and acceptance dimensions, not an adoption-model inter-construct matrix or SEM path model.
- Source location: Results Tables 1-3
- Short source excerpt: "GenAI acceptance is positively moderate correlated"
- Affected coder returns: R2 excluded; R3 no coded values

### S132

- Code: `E-FT1`
- Rationale: Mentorship perception study reports identification/evaluation regressions and correlations for helpfulness, caring, and likelihood ratings; no usable target AI-adoption construct-pair r or SEM path coefficients.
- Source location: Abstract; Research questions; Results
- Short source excerpt: "helpfulness, caring, and likelihood"
- Affected coder returns: R1 excluded; R4 no coded values

### S195

- Code: `E-FT1`
- Rationale: Same DOI/PDF as S206. The source uses PLSR component loadings and an image-only item-level correlation matrix, not a usable construct-level inter-construct correlation matrix or standardized SEM/path table for the project model.
- Source location: Figure 3; Table 3; Table 4
- Short source excerpt: "PLSR component loading factors"
- Affected coder returns: R1 coded item-level values; R4 no coded values; duplicate-source issue with S206

### S206

- Code: `E-FT1`
- Rationale: Same DOI/PDF as S195. Uses PLSR component loadings and an image-only item-level correlation matrix for undergraduate generative-AI adoption; it is not a usable construct-level inter-construct correlation matrix or standardized SEM/path table.
- Source location: Figure 3; Table 3; Table 4
- Short source excerpt: "PLSR component loading factors"
- Affected coder returns: R2 excluded; R3 no coded values; duplicate-source issue with S195

### S224

- Code: `E-FT3`
- Rationale: Full text focuses on virtual learning/Google Classroom adoption during COVID-19. AI and machine-learning features are discussed only as possible enhancements, so the focal technology is not educational AI adoption.
- Source location: Abstract; Introduction; Conclusion
- Short source excerpt: "Adoption, use and enhancement of virtual learning"
- Affected coder returns: R1 excluded; R4 coded virtual-learning UTAUT paths

## Needs Adjudication Before Exclusion

### S014

- Source-check status: `include_candidate`
- Recommended action: `adjudicate_not_exclude`
- Rationale: Reports PLS-SEM path analysis for adoption of AI-based data-analysis tools among academic researchers. R1 coded complete-sample indirect paths, while R4 has no coded values; adjudication is needed for indirect-effect handling, construct mapping, and higher-education population eligibility.
- Source location: Abstract; Figure 1; Results 4.3; Table 4
- Short source excerpt: "Table 4 Path analysis"
- Affected coder returns: R1 coded values; R4 no coded values

### S021

- Source-check status: `include_candidate`
- Recommended action: `adjudicate_not_exclude`
- Rationale: Reports PLS-SEM paths for genAI acceptance among higher-education staff before/after a training intervention; source has potentially usable path coefficients, but the pre/post design and T1/T2 construct separation need adjudication.
- Source location: Abstract; Methods 3.4; Results 4.2-4.3; Figures 1-2; Supplementary Table S4
- Short source excerpt: "pre- and post-course genAI acceptance"
- Affected coder returns: R2 excluded; R3 no coded values

### S092

- Source-check status: `include_candidate`
- Recommended action: `adjudicate_not_exclude`
- Rationale: Reports SEM model fit and standardized path estimates for ChatGPT adoption among ESP/business-communication students; source appears to contain usable target path coefficients.
- Source location: Abstract; Results: Structural Equation Modeling; Table 3
- Short source excerpt: "Structural equation modeling (SEM)"
- Affected coder returns: R2 excluded

### S056

- Source-check status: `include_candidate`
- Recommended action: `adjudicate_not_exclude`
- Rationale: Reports TAM/PLS-SEM standardized path coefficients for ChatGPT acceptance among Chinese-as-a-foreign-language learners. R2 coded the TAM paths, while R3 has no coded values; adjudication is needed to recover the missing coder-side rows.
- Source location: Abstract; Methods 3.4; Results 4.1.2; Table 3
- Short source excerpt: "Table 3. Path significance and coefficients."
- Affected coder returns: R2 coded values; R3 no coded values

### S121

- Source-check status: `include_candidate`
- Recommended action: `adjudicate_not_exclude`
- Rationale: Reports UTAUT/PLS-SEM paths for generative AI use and intention among students and teachers; source appears to contain usable target path coefficients.
- Source location: Abstract; Methods; SEM/PLS-SEM results
- Short source excerpt: "partial least squares SEM (PLS-SEM)"
- Affected coder returns: R3 no coded values

### S202

- Source-check status: `include_candidate`
- Recommended action: `adjudicate_not_exclude`
- Rationale: Reports SEM path coefficients and a Fornell-Larcker-style construct correlation table for AI-driven LMS automation and student readiness; inclusion depends on construct mapping and focal-technology adjudication.
- Source location: Research model; Table 4; Table 5
- Short source excerpt: "structural equation modelling (SEM)"
- Affected coder returns: R2 excluded; R3 no coded values
