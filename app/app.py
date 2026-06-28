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

Prepare for technical and HR interviews using Google Gemini AI.
""")

st.divider()

c1, c2 = st.columns(2)

with c1:
    st.info("""
### Features

- Resume Analysis
- Job Description Analysis
- Personalized Interview Questions
- AI Mock Interview
- AI Feedback
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
## 🚀 Workflow

1. Resume Analysis
2. Job Description Analysis
3. Generate Interview Questions
4. Start Mock Interview
5. Get AI Feedback
6. Download Interview Report

Use the **sidebar** to navigate between pages.
""")