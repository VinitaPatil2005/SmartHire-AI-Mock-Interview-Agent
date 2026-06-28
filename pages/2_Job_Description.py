import streamlit as st

from app.jd_parser import clean_job_description
from app.gemini_service import generate_response
from app.prompts import JOB_DESCRIPTION_PROMPT

st.set_page_config(
    page_title="Job Description Analysis",
    page_icon="💼",
    layout="wide"
)

st.title("💼 Job Description Analysis")

st.write(
    "Paste the Job Description to analyze the required skills and responsibilities."
)

# =====================================================
# Job Description Input
# =====================================================

job_description = st.text_area(
    "Paste Job Description",
    height=300,
    placeholder="Paste the complete Job Description here..."
)

if job_description:

    cleaned_jd = clean_job_description(job_description)

    st.session_state["job_description"] = cleaned_jd

    st.success("Job Description added successfully!")

    with st.expander("View Job Description"):

        st.write(cleaned_jd)

st.divider()

# =====================================================
# AI Analysis
# =====================================================

if "job_description" in st.session_state:

    if st.button(
        "Analyze Job Description",
        use_container_width=True
    ):

        with st.spinner(
            "Analyzing Job Description..."
        ):

            analysis = generate_response(

                JOB_DESCRIPTION_PROMPT.format(

                    jd=st.session_state["job_description"]

                )

            )

        st.session_state["jd_analysis"] = analysis

# =====================================================
# Display Analysis
# =====================================================

if "jd_analysis" in st.session_state:

    st.subheader("🤖 AI Job Description Analysis")

    st.markdown(
        st.session_state["jd_analysis"]
    )