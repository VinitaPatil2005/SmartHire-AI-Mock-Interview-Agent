import os
import tempfile

import streamlit as st

from app.resume_parser import extract_resume_text
from app.gemini_service import generate_response
from app.prompts import RESUME_ANALYSIS_PROMPT

st.set_page_config(
    page_title="Resume Analysis",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Resume Analysis")

st.write(
    "Upload your resume to extract information and analyze it using Gemini AI."
)

uploaded_resume = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

if uploaded_resume is not None:

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as temp_file:

        temp_file.write(uploaded_resume.read())

        temp_path = temp_file.name

    resume_text = extract_resume_text(temp_path)

    os.remove(temp_path)

    st.session_state["resume_text"] = resume_text

    st.success("Resume uploaded successfully!")

    with st.expander("View Extracted Resume"):

        st.text_area(
            "Resume Content",
            resume_text,
            height=350
        )

st.divider()

if "resume_text" in st.session_state:

    if st.button(
        "Analyze Resume",
        use_container_width=True
    ):

        with st.spinner("Analyzing Resume..."):

            analysis = generate_response(

                RESUME_ANALYSIS_PROMPT.format(

                    resume=st.session_state["resume_text"]

                )

            )

        st.session_state["resume_analysis"] = analysis

if "resume_analysis" in st.session_state:

    st.subheader("🤖 AI Resume Analysis")

    st.markdown(
        st.session_state["resume_analysis"]
    )