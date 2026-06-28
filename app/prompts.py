"""
Prompt templates used throughout the SmartHire application.
"""

# ------------------------------------------------------
# Resume Analysis
# ------------------------------------------------------

RESUME_ANALYSIS_PROMPT = """
You are an experienced technical recruiter.

Analyze the following resume.

Return your response in Markdown.

Include the following sections:

# Candidate Name

# Education

# Technical Skills

# Soft Skills

# Projects

# Experience

# Certifications

# Strengths

# Areas for Improvement

Resume:

{resume}
"""

# ------------------------------------------------------
# Job Description Analysis
# ------------------------------------------------------

JOB_DESCRIPTION_PROMPT = """
You are an HR recruiter.

Analyze the following Job Description.

Return your response in Markdown.

Include:

# Job Role

# Required Skills

# Preferred Skills

# Experience Required

# Responsibilities

# Important Keywords

Job Description:

{jd}
"""

# ------------------------------------------------------
# Interview Question Generation
# ------------------------------------------------------

INTERVIEW_QUESTION_PROMPT = """
You are a Senior Technical Interviewer.

Generate exactly 10 interview questions.

Return ONLY valid JSON.

The JSON format MUST be:

[
  {
    "id":1,
    "category":"Technical",
    "question":"..."
  },
  {
    "id":2,
    "category":"Project",
    "question":"..."
  }
]

Rules:

- 4 Technical Questions
- 3 Project Questions
- 3 HR Questions

Resume:

{resume}

Job Description:

{jd}
"""

# ------------------------------------------------------
# Mock Interview Evaluation
# ------------------------------------------------------

MOCK_INTERVIEW_EVALUATION_PROMPT = """
You are a Senior Technical Interviewer.

Evaluate the candidate's answer.

Question:

{question}

Candidate Answer:

{answer}

Return your evaluation in Markdown.

## Score (out of 10)

## What was good

## What was missing

## Suggested Improvement

## Example of an Excellent Answer
"""

#------------------------------------------------------
# Interview Report Generation
#------------------------------------------------------

INTERVIEW_REPORT_PROMPT = """
You are a Senior Hiring Manager.

Based on the interview evaluation below, generate a professional interview report.

Return the report in Markdown.

Include:

# Overall Score (/10)

# Technical Skills

# Communication

# Problem Solving

# Strengths

# Areas for Improvement

# Final Recommendation

Interview Evaluation:

{evaluation}
"""

# ------------------------------------------------------
# Answer Evaluation
# ------------------------------------------------------

ANSWER_EVALUATION_PROMPT = """
You are an experienced interviewer.

Question:

{question}

Candidate Answer:

{answer}

Evaluate the answer.

Return:

## Score (out of 10)

## Strengths

## Weaknesses

## Suggestions

## Correct Answer
"""