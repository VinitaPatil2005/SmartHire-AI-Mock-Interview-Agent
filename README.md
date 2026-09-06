# SmartHire AI Mock Interview Agent

SmartHire is an AI-powered mock interview platform that helps candidates prepare for technical and HR interviews. It analyzes resumes and job descriptions, generates personalized interview questions, conducts AI-based mock interviews, and provides structured feedback and performance reports.

## Features

* **Resume Analysis** — Extracts and analyzes skills, projects, education, and experience from resumes.
* **Job Description Analysis** — Identifies required skills, responsibilities, and key interview areas.
* **Personalized Questions** — Generates interview questions based on the candidate's resume and target job.
* **AI Mock Interview** — Simulates a realistic technical and HR interview experience.
* **AI Feedback** — Evaluates responses and provides strengths, weaknesses, and improvement suggestions.
* **Interview Report** — Generates a downloadable summary of the interview performance.

## Tech Stack

* **Python**
* **Streamlit** — Web interface
* **Google Gemini** — AI question generation and response evaluation
* **LangChain** — LLM orchestration
* **FAISS** — Vector similarity search
* **Sentence Transformers** — Text embeddings
* **PyMuPDF** — Resume/PDF text extraction
* **Pandas & NumPy** — Data processing
* **ReportLab** — Report generation

## How It Works

```text
Resume + Job Description
          ↓
   Resume Analysis
          ↓
 Job Description Analysis
          ↓
 Personalized Questions
          ↓
    AI Mock Interview
          ↓
   Response Evaluation
          ↓
    AI Feedback
          ↓
  Interview Performance Report
```

## Project Structure

```text
SmartHire-AI-Mock-Interview-Agent/
├── SmartHire.py
├── app/
├── pages/
├── requirements.txt
├── README.md
└── LICENSE
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/VinitaPatil2005/SmartHire-AI-Mock-Interview-Agent.git
cd SmartHire-AI-Mock-Interview-Agent
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

**Windows:**

```bash
venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API Key

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_gemini_api_key
```

### 5. Run the Application

```bash
streamlit run SmartHire.py
```

The application will be available at:

```text
http://localhost:8501
```

## Requirements

* Python 3.10+
* Google Gemini API key
* Internet connection for Gemini API access

## Contributing

Contributions are welcome. Fork the repository, create a feature branch, make your changes, and submit a pull request.

## License

This project is licensed under the terms specified in the `LICENSE` file.

## Acknowledgements

* Google Gemini
* Streamlit
* LangChain
* FAISS
* Sentence Transformers
* PyMuPDF
