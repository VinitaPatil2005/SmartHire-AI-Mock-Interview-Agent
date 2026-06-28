import os
import tempfile

import streamlit as st

from resume_parser import extract_resume_text
from gemini_service import generate_response
from prompts import RESUME_ANALYSIS_PROMPT

st.title("📄 Resume Analysis")

st.write(
    "Upload your resume and let Gemini analyze it."
)

uploaded_resume = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if uploaded_resume:

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as temp_file:

        temp_file.write(
            uploaded_resume.read()
        )

        temp_path = temp_file.name

    resume_text = extract_resume_text(
        temp_path
    )

    os.remove(temp_path)

    st.success(
        "Resume uploaded successfully."
    )

    with st.expander(
        "Extracted Resume"
    ):

        st.text_area(
            "Resume",
            resume_text,
            height=350
        )

    if st.button(
        "Analyze Resume",
        use_container_width=True
    ):

        with st.spinner(
            "Analyzing..."
        ):

            analysis = generate_response(

                RESUME_ANALYSIS_PROMPT.format(

                    resume=resume_text

                )

            )

        st.markdown(analysis)