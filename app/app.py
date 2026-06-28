import streamlit as st

from config import APP_TITLE

st.set_page_config(
    page_title=APP_TITLE,
    page_icon="💼",
    layout="wide"
)

st.title(APP_TITLE)

st.write(
    """
    Welcome to **SmartHire**.

    An AI-powered interview assistant that helps users prepare for technical and HR interviews by analyzing resumes and job descriptions.
    """
)