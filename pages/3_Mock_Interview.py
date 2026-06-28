import streamlit as st

from app.interview import generate_interview_questions
from app.evaluator import evaluate_answer

st.set_page_config(
    page_title="Mock Interview",
    page_icon="🎤",
    layout="wide"
)

st.title("🎤 AI Mock Interview")

if (
    "resume_text" not in st.session_state
    or
    "job_description" not in st.session_state
):
    st.warning(
        "Please complete Resume Analysis and Job Description Analysis first."
    )
    st.stop()

# ----------------------------------------------------
# Generate Questions
# ----------------------------------------------------

if "questions" not in st.session_state:

    if st.button(
        "Generate Interview Questions",
        use_container_width=True
    ):

        with st.spinner("Generating Questions..."):

            questions = generate_interview_questions(
                st.session_state["resume_text"],
                st.session_state["job_description"]
            )

        st.session_state["questions"] = questions

# ----------------------------------------------------
# Interview
# ----------------------------------------------------

if "questions" in st.session_state:

    st.subheader("Interview Questions")

    st.markdown(st.session_state["questions"])

    answer = st.text_area(
        "Write your answer here...",
        height=200
    )

    if st.button(
        "Evaluate My Answer",
        use_container_width=True
    ):

        with st.spinner("Evaluating..."):

            evaluation = evaluate_answer(
                st.session_state["questions"],
                answer
            )

        st.markdown(evaluation)
        st.session_state["evaluation"] = evaluation