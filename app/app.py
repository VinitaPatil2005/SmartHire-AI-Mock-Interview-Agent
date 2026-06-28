import os
import tempfile

import streamlit as st

from config import APP_TITLE
from resume_parser import extract_resume_text
from jd_parser import clean_job_description

st.set_page_config(
    page_title=APP_TITLE,
    layout="wide"
)

st.title(APP_TITLE)

st.write(
    "Upload your resume and provide a Job Description to start your AI mock interview."
)

st.divider()

# ---------------- Resume ----------------

st.header("Resume")

uploaded_resume = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

resume_text = ""

if uploaded_resume is not None:

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as temp_file:

        temp_file.write(uploaded_resume.read())

        temp_path = temp_file.name

    resume_text = extract_resume_text(temp_path)

    os.remove(temp_path)

    st.success("Resume uploaded successfully!")

    with st.expander("View Resume"):

        st.text_area(
            "Resume",
            resume_text,
            height=300
        )

st.divider()

# ---------------- Job Description ----------------

st.header("Job Description")

job_description = st.text_area(
    "Paste the Job Description",
    height=250
)

if job_description:

    cleaned_jd = clean_job_description(
        job_description
    )

    st.success("Job Description added successfully!")

    with st.expander("View Job Description"):

        st.write(cleaned_jd)