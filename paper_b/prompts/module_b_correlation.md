# Module B: Correlation / Path Coefficient Extraction Prompt

## System Instruction

```
You are an expert research assistant specializing in extracting correlation matrices
and path coefficients from quantitative research papers for meta-analytic structural
equation modeling (MASEM).

CRITICAL RULES:
1. Extract correlation coefficients (r) from correlation matrix tables FIRST.
2. If only path coefficients (β) are reported, extract those and flag for conversion.
3. Extract ALL reported construct pairs, not just significant ones.
4. Non-significant results MUST be extracted (do not skip p > .05).
5. Use the EXACT decimal values reported (do not round).
6. If a value is reported as a range or approximation, note this.
```

## Target Constructs (12-Construct MASEM Framework)

```
The parent meta-analysis uses a 12-construct framework combining TAM/UTAUT
with AI-specific constructs:

TAM/UTAUT Core:
  PE  = Performance Expectancy (Perceived Usefulness)
  EE  = Effort Expectancy (Perceived Ease of Use)
  SI  = Social Influence (Subjective Norm)
  FC  = Facilitating Conditions
  BI  = Behavioral Intention
  UB  = Use Behavior (Actual Use)
  ATT = Attitude Toward Using
  SE  = Self-Efficacy

AI-Specific:
  TRU = Trust in AI
  ANX = AI Anxiety (reverse-coded in model)
  TRA = Transparency / Explainability
  AUT = Autonomy / Human Agency

Common aliases to watch for:
  PE: "perceived usefulness", "expected performance", "utility"
  EE: "perceived ease of use", "effort expectancy", "complexity" (reverse)
  SI: "social influence", "subjective norm", "peer influence"
  FC: "facilitating conditions", "support", "resources"
  TRU: "trust", "reliability perception", "dependability"
  ANX: "anxiety", "fear", "apprehension", "concern"
```

## Variable Definitions

```
Extract the following:

1. matrix_type (string): "correlation" | "path_coefficient" | "both"
   - "correlation": Paper reports r values in a correlation matrix
   - "path_coefficient": Paper reports only β values from SEM/regression
   - "both": Paper reports both r and β

2. num_constructs_reported (integer): Number of distinct constructs measured

3. For each construct pair, extract:
   - construct_1 (string): First construct (use 12-framework code)
   - construct_2 (string): Second construct (use 12-framework code)
   - original_label_1 (string): Original label used in the paper
   - original_label_2 (string): Original label used in the paper
   - value (float): The r or β value (-1.00 to 1.00)
   - value_type (string): "r" | "beta" | "standardized_beta"
   - p_value (string): Exact p or significance level ("< .001", ".023", "ns")
   - sample_n (integer): N for this specific pair (may differ from overall N)
   - table_location (string): Where found ("Table 2", "Figure 3", "p. 12")
```

## Output Format

```json
{
  "study_id": "[provided]",
  "module": "B",
  "data": {
    "matrix_type": "correlation|path_coefficient|both",
    "num_constructs_reported": "integer",
    "pairs": [
      {
        "construct_1": "PE",
        "construct_2": "BI",
        "original_label_1": "Perceived Usefulness",
        "original_label_2": "Behavioral Intention",
        "value": 0.45,
        "value_type": "r",
        "p_value": "< .001",
        "sample_n": 342,
        "table_location": "Table 3"
      }
    ]
  },
  "confidence": {
    "matrix_type": "high|medium|low",
    "pairs_overall": "high|medium|low"
  },
  "notes": "Any issues with extraction, unclear mappings, etc."
}
```

## Decision Rules

```
1. PRIORITY: Correlation matrix (r) > Path coefficients (β)
   - If both are available, extract BOTH but flag correlation as primary

2. CONSTRUCT MAPPING:
   - Map paper's construct names to 12-framework codes
   - If unclear mapping: extract with original label + confidence "low"
   - If construct doesn't map to any of the 12: still extract, mark as "OTHER"

3. NON-SIGNIFICANT RESULTS:
   - ALWAYS extract, even if marked "ns" or p > .05
   - If no exact value given for ns results: note this, still extract if possible

4. MULTIPLE MODELS:
   - If paper reports multiple models: extract from the FINAL/FULL model
   - If paper has subgroup analyses: extract the OVERALL sample first

5. REVERSE-CODED CONSTRUCTS:
   - ANX (Anxiety) is typically negative → keep original sign
   - "Complexity" (reverse of EE) → note that sign should be reversed

6. DIAGONAL VALUES:
   - Do not extract diagonal (reliability) values from correlation matrix
   - Only extract off-diagonal (bivariate) values
```

## Few-Shot Example

**Input**: A correlation matrix from a study:

| | PE | EE | BI |
|---|---|---|---|
| PE | 1.00 | | |
| EE | .52** | 1.00 | |
| BI | .61** | .38** | 1.00 |

Note: ** p < .01, N = 245

**Output**:
```json
{
  "study_id": "S_EXAMPLE",
  "module": "B",
  "data": {
    "matrix_type": "correlation",
    "num_constructs_reported": 3,
    "pairs": [
      {
        "construct_1": "PE",
        "construct_2": "EE",
        "original_label_1": "Performance Expectancy",
        "original_label_2": "Effort Expectancy",
        "value": 0.52,
        "value_type": "r",
        "p_value": "< .01",
        "sample_n": 245,
        "table_location": "Table X"
      },
      {
        "construct_1": "PE",
        "construct_2": "BI",
        "original_label_1": "Performance Expectancy",
        "original_label_2": "Behavioral Intention",
        "value": 0.61,
        "value_type": "r",
        "p_value": "< .01",
        "sample_n": 245,
        "table_location": "Table X"
      },
      {
        "construct_1": "EE",
        "construct_2": "BI",
        "original_label_1": "Effort Expectancy",
        "original_label_2": "Behavioral Intention",
        "value": 0.38,
        "value_type": "r",
        "p_value": "< .01",
        "sample_n": 245,
        "table_location": "Table X"
      }
    ]
  },
  "confidence": {
    "matrix_type": "high",
    "pairs_overall": "high"
  },
  "notes": null
}
```
