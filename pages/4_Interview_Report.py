import streamlit as st

from app.report import generate_report

st.set_page_config(
    page_title="Interview Report",
    layout="wide"
)

st.title("Interview Report")

if "evaluation" not in st.session_state:

    st.warning(
        "Complete the mock interview first."
    )

    st.stop()

if st.button(
    "Generate Report",
    use_container_width=True
):

    with st.spinner(
        "Generating Interview Report..."
    ):

        report = generate_report(

            st.session_state["evaluation"]

        )

    st.session_state["report"] = report

if "report" in st.session_state:

    st.markdown(

        st.session_state["report"]

    )