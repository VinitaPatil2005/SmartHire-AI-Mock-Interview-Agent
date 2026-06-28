import streamlit as st

from app.interview import (
    generate_interview_questions
)

st.set_page_config(
    page_title="AI Interview",
    page_icon="🎤",
    layout="wide"
)

st.title("🎤 AI Mock Interview")

st.write(
    "Generate personalized interview questions using your resume and job description."
)

if (
    "resume_text" not in st.session_state
    or
    "job_description" not in st.session_state
):

    st.warning(
        "Please complete Resume Analysis and Job Description Analysis first."
    )

else:

    if st.button(
        "Generate Interview Questions",
        use_container_width=True
    ):

        with st.spinner(
            "Generating personalized interview..."
        ):

            questions = generate_interview_questions(

                st.session_state["resume_text"],

                st.session_state["job_description"]

            )

        st.session_state["questions"] = questions

if "questions" in st.session_state:

    st.divider()

    st.markdown(
        st.session_state["questions"]
    )