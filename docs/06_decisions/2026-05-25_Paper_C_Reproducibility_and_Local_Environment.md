# Decision: Paper C Reproducibility and Local Environment Controls

Date: 2026-05-25

## Decision

Paper C will compare model-by-procedure conditions, not abstract model
performance detached from execution context. The main claim should be
interpreted as extraction performance under locked and reported conditions:
model, provider/interface, prompt, schema, preprocessing, runtime settings,
source files, and procedure artifacts.

Local environment will be handled differently depending on the inference route:

- API-served models: local environment is primarily a preprocessing,
  orchestration, prompt-serialization, parsing, and retry provenance variable.
  Provider-side model snapshot, endpoint, access date/time, exposed settings,
  and undocumented backend changes remain part of the condition.
- Locally hosted models: local environment is a direct inference condition and
  must include model weights/release hash, quantization, runtime, hardware,
  accelerator, operating system, package versions, decoding implementation, and
  seed handling where available.

## Rationale

LLM extraction results can vary by model, prompt architecture, procedure, and
runtime controls. Evidence-synthesis guidance also requires transparent
reporting and human responsibility when AI systems are used for extraction or
judgment tasks. Therefore, Paper C should avoid the claim that one observed
score is the stable property of a model.

## Required Reporting Tables

Paper C should include or supplement at least two reproducibility tables:

| Table | Purpose |
|---|---|
| Run-provenance table | Records model, endpoint/interface, date/time, prompt/schema hash, PDF/source hash, preprocessing/OCR, chunking, decoding settings, client/runtime, and local hardware when relevant. |
| Repeatability table | Reports within-condition stability, including value agreement, source-span stability, schema-failure rate, invalid-output rate, and performance variability across repeat runs. |

## Recommended Analysis Rule

Use one locked full-corpus run per model-by-procedure condition for the main
213-study comparison if resources are constrained. Add three or more repeated
runs on a stratified stability subset that over-samples high-risk extraction
families, source-review studies, and human-human disagreement cases. If budget
permits, repeat the full corpus.

Do not interpret a model ranking or procedure advantage as substantively strong
when the between-condition difference is smaller than within-condition
run-to-run variation.

## Supporting External Guidance

- TRIPOD-LLM emphasizes transparent reporting, human oversight, task-specific
  performance reporting, data sources, model names/versions, preprocessing, and
  prompt engineering: https://www.nature.com/articles/s41591-024-03425-5
- The Cochrane/Campbell/JBI/CEE RAISE position statement requires human
  responsibility, human oversight, and full transparent reporting of AI use that
  suggests judgments or extracts bibliographic, numerical, or qualitative data:
  https://link.springer.com/article/10.1186/s13750-025-00374-5
- A recent meta-analysis extraction benchmark reports results by method-model
  combinations, field type, and error profiles, supporting Paper C's
  model-by-procedure design:
  https://www.cambridge.org/core/journals/research-synthesis-methods/article/what-level-of-automation-is-good-enough-a-benchmark-of-large-language-models-for-metaanalysis-data-extraction/2EA4DAFAAC11E76216DC0A512CA29D59
- Recent biomedical reproducibility work shows how repeated model invocations
  can be reported with per-run performance, majority vote, invalid-output rate,
  and agreement statistics:
  https://academic.oup.com/jamia/article/33/6/1179/8559659
