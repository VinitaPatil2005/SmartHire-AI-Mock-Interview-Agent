import streamlit as st

from config import APP_TITLE

st.set_page_config(
    page_title=APP_TITLE,
    page_icon="💼",
    layout="wide"
)

st.title("💼 SmartHire")

st.subheader("AI Mock Interview Agent")

st.write("""
Welcome to **SmartHire**.

Prepare for technical and HR interviews using AI.

Navigate using the sidebar.
""")

st.divider()

c1, c2 = st.columns(2)

with c1:

    st.info("""
### Features

- Resume Analysis
- Job Description Analysis
- Personalized Questions
- Mock Interview
- AI Evaluation
- Interview Report
""")

with c2:

    st.success("""
### Tech Stack

- Google Gemini
- Streamlit
- LangChain
- PyMuPDF
- FAISS
""")

st.divider()

st.markdown("""
## Workflow

1. Upload Resume

2. Analyze Resume

3. Paste Job Description

4. Generate Questions

5. Start Mock Interview

6. Get AI Feedback
""")