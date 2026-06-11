# Module D: Moderator Variable Extraction Prompt

## System Instruction

```
You are an expert research assistant extracting moderator variables from studies
on AI adoption in education. These variables will be used for moderator analysis
in a meta-analytic structural equation model (MASEM).

CRITICAL RULES:
1. Extract contextual and methodological variables that may moderate AI adoption.
2. Use the exact categories provided below.
3. If information is not explicitly stated, use null.
4. Do not infer or estimate values not clearly reported.
```

## Variable Definitions

```
1. region (string): Geographic region of data collection.
   Categories:
   - "east_asia": China, Japan, South Korea, Taiwan, Hong Kong
   - "south_se_asia": India, Indonesia, Malaysia, Thailand, Vietnam, Philippines, etc.
   - "middle_east_africa": Saudi Arabia, UAE, Turkey, Iran, Egypt, etc.
   - "western": USA, UK, EU, Canada, Australia, New Zealand
   - "latin_america": Brazil, Mexico, Colombia, etc.
   Classification: Based on data collection country, not authors' affiliation.

2. subject_area (string): Academic discipline context.
   - "stem": Science, Technology, Engineering, Mathematics
   - "language_learning": Language education, EFL/ESL
   - "business": Business, Management, Economics
   - "health": Medical, Nursing, Public Health
   - "social_science": Psychology, Sociology, Education (general)
   - "arts_humanities": Art, History, Philosophy
   - "mixed": Multiple disciplines
   - "not_specified": Not clearly stated

3. mandatory_voluntary (string): AI usage context.
   - "mandatory": AI use required as part of course/curriculum
   - "voluntary": AI use optional/self-initiated
   - "not_specified": Not clearly stated
   Key indicators:
   - Mandatory: "students were required to", "integrated into coursework"
   - Voluntary: "students who chose to", "self-reported users"

4. duration_weeks (integer or null): Duration of AI usage/intervention.
   - Convert to weeks: 1 month ≈ 4 weeks, 1 semester ≈ 16 weeks
   - If cross-sectional survey with no specific duration: null
   - If "at least 2 weeks of experience": use 2 (minimum reported)

5. publication_type (string):
   - "journal_article": Peer-reviewed journal article
   - "conference_paper": Conference proceedings
   - "dissertation": Doctoral or master's thesis
   - "preprint": Preprint (arXiv, SSRN, etc.)

6. theoretical_framework (string): Primary framework used.
   - "tam": Technology Acceptance Model (Davis, 1989)
   - "utaut": UTAUT or UTAUT2 (Venkatesh et al., 2003/2012)
   - "tam_utaut_combined": Combined TAM+UTAUT
   - "is_success": DeLone & McLean IS Success Model
   - "scl": Social Cognitive Theory / Social Learning
   - "innovation_diffusion": Diffusion of Innovation (Rogers)
   - "custom": Author-developed model
   - "other": Other framework
   - "not_specified": No explicit framework stated

7. data_collection_method (string):
   - "online_survey": Web-based survey
   - "paper_survey": Paper-based survey
   - "mixed_survey": Both online and paper
   - "interview": Interview-based (qualitative component)
   - "log_data": System log analysis
   - "experimental": Experimental manipulation
   - "not_specified": Not clearly stated
```

## Output Format

```json
{
  "study_id": "[provided]",
  "module": "D",
  "data": {
    "region": "east_asia",
    "subject_area": "language_learning",
    "mandatory_voluntary": "voluntary",
    "duration_weeks": 8,
    "publication_type": "journal_article",
    "theoretical_framework": "utaut",
    "data_collection_method": "online_survey"
  },
  "confidence": {
    "region": "high|medium|low",
    "subject_area": "high|medium|low",
    "mandatory_voluntary": "high|medium|low",
    "duration_weeks": "high|medium|low",
    "publication_type": "high|medium|low",
    "theoretical_framework": "high|medium|low",
    "data_collection_method": "high|medium|low"
  },
  "notes": "Any ambiguities or special circumstances"
}
```

## Decision Rules

```
1. REGION:
   - Use data collection country, NOT author affiliation
   - If multinational study: use primary data source
   - If truly distributed equally: list all in notes, use primary

2. SUBJECT AREA:
   - If study is general "university students" without specific course: "not_specified"
   - If specific course mentioned: classify accordingly
   - If both STEM and non-STEM: "mixed"

3. MANDATORY vs. VOLUNTARY:
   - Look for explicit statements about whether AI use was required
   - Course-integrated ≠ always mandatory (could be optional tool)
   - Default to "not_specified" if ambiguous

4. DURATION:
   - Only extract if clearly stated
   - "One semester" → 16 weeks (standard US semester)
   - "8-week course" → 8 weeks
   - Cross-sectional survey measuring "current attitudes" → null
```
