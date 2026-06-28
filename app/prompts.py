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
You are a Senior Software Engineer conducting an interview.

Using BOTH the candidate's resume and the job description, generate a personalized interview.

Generate exactly 10 questions.

Format your response in Markdown.

# Technical Questions
1.
2.
3.
4.

# Project Based Questions
5.
6.
7.

# HR Questions
8.
9.
10.

Resume:

{resume}

Job Description:

{jd}
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