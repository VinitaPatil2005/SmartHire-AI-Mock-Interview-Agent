RESUME_ANALYSIS_PROMPT = """
You are an expert technical recruiter.

Analyze the following resume.

Return your answer in Markdown with these sections:

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


JOB_DESCRIPTION_PROMPT = """
You are an experienced HR recruiter.

Analyze the following Job Description.

Return your answer in Markdown with these sections:

# Job Role

# Required Skills

# Preferred Skills

# Experience Required

# Responsibilities

# Important Keywords

Job Description:

{jd}
"""