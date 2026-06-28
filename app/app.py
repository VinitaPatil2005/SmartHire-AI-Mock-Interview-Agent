import os
import tempfile

import streamlit as st

from config import APP_TITLE
from resume_parser import extract_resume_text

st.set_page_config(
    page_title=APP_TITLE,
    layout="wide"
)

st.title(APP_TITLE)

st.write(
    "Upload your resume to begin your AI-powered mock interview."
)

st.divider()

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

if uploaded_file is not None:

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as tmp_file:

        tmp_file.write(uploaded_file.read())

        temp_path = tmp_file.name

    resume_text = extract_resume_text(temp_path)

    st.success("Resume uploaded successfully!")

    st.subheader("Extracted Resume Text")

    st.text_area(
        "Resume Content",
        resume_text,
        height=400
    )

    os.remove(temp_path)