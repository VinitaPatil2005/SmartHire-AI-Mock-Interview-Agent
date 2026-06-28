import os
import tempfile

import streamlit as st

from config import APP_TITLE
from resume_parser import extract_resume_text
from jd_parser import clean_job_description
from gemini_service import generate_response

from prompts import (
    RESUME_ANALYSIS_PROMPT,
    JOB_DESCRIPTION_PROMPT
)

# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title=APP_TITLE,
    page_icon="💼",
    layout="wide"
)

# =====================================================
# APPLICATION TITLE
# =====================================================

st.title(APP_TITLE)

st.markdown("""
Welcome to **SmartHire - AI Mock Interview Agent**

This application helps candidates prepare for interviews by:

- Uploading and analyzing resumes
- Understanding job descriptions
- Generating AI-powered insights
- Creating personalized interview questions
- Providing interview feedback

Powered by **Google Gemini AI**
""")

st.divider()

# =====================================================
# RESUME UPLOAD SECTION
# =====================================================

st.header("📄 Resume Upload")

uploaded_resume = st.file_uploader(
    "Upload your Resume (PDF)",
    type=["pdf"]
)

# Variable to store extracted resume text
resume_text = ""

if uploaded_resume is not None:

    # Save uploaded PDF temporarily
    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as temp_file:

        temp_file.write(uploaded_resume.read())

        temp_path = temp_file.name

    # Extract text from PDF
    resume_text = extract_resume_text(temp_path)

    # Delete temporary file
    os.remove(temp_path)

    st.success("Resume uploaded successfully!")

    # Show extracted resume
    with st.expander("View Extracted Resume"):

        st.text_area(
            "Resume Content",
            resume_text,
            height=350
        )

st.divider()

# =====================================================
# JOB DESCRIPTION SECTION
# =====================================================

st.header("💼 Job Description")

job_description = st.text_area(
    "Paste the Job Description",
    height=250
)

cleaned_jd = ""

if job_description:

    cleaned_jd = clean_job_description(
        job_description
    )

    st.success("Job Description added successfully!")

    with st.expander("View Job Description"):

        st.write(cleaned_jd)

st.divider()

# =====================================================
# AI ANALYSIS SECTION
# =====================================================

st.header("🤖 AI Document Analysis")

col1, col2 = st.columns(2)

# -----------------------------------------------------
# Resume Analysis
# -----------------------------------------------------

with col1:

    st.subheader("Resume Analysis")

    if st.button(
        "Analyze Resume",
        use_container_width=True
    ):

        if resume_text == "":

            st.warning(
                "Please upload a resume first."
            )

        else:

            with st.spinner(
                "Analyzing resume..."
            ):

                resume_analysis = generate_response(

                    RESUME_ANALYSIS_PROMPT.format(
                        resume=resume_text
                    )

                )

            st.success(
                "Resume analysis completed!"
            )

            st.markdown(resume_analysis)

# -----------------------------------------------------
# Job Description Analysis
# -----------------------------------------------------

with col2:

    st.subheader("Job Description Analysis")

    if st.button(
        "Analyze Job Description",
        use_container_width=True
    ):

        if cleaned_jd == "":

            st.warning(
                "Please enter a Job Description."
            )

        else:

            with st.spinner(
                "Analyzing Job Description..."
            ):

                jd_analysis = generate_response(

                    JOB_DESCRIPTION_PROMPT.format(
                        jd=cleaned_jd
                    )

                )

            st.success(
                "Job Description analysis completed!"
            )

            st.markdown(jd_analysis)

st.divider()

# =====================================================
# CURRENT STATUS
# =====================================================

st.header("📌 Current Project Status")

st.success("""
### Completed Features

- Resume Upload
- Resume PDF Parsing
- Job Description Parser
- Gemini Resume Analysis
- Gemini Job Description Analysis
""")

st.info("""
### Upcoming Features

- ATS Match Score
- Personalized Interview Question Generator
- Technical Interview Round
- HR Interview Round
- AI Answer Evaluation
- Interview Report Generator
- Downloadable PDF Report
""")

# =====================================================
# FOOTER
# =====================================================

st.divider()

st.caption(
    "SmartHire - AI Mock Interview Agent | Powered by Google Gemini"
)