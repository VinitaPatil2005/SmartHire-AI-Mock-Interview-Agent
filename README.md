# SmartHire AI Mock Interview Agent

SmartHire is an AI-powered mock interview platform that helps candidates prepare for technical and HR interviews. Built with Streamlit, Google Gemini, and LangChain, it analyzes resumes and job descriptions, generates personalized interview questions, conducts mock interviews, and produces AI-driven feedback and interview reports.

## Features

- Resume Analysis  
  Extracts and interprets key information from a candidate’s resume.

- Job Description Analysis  
  Analyzes a job posting to identify required skills, responsibilities, and interview focus areas.

- Personalized Interview Questions  
  Generates tailored questions based on the resume and job description.

- AI Mock Interview  
  Simulates a realistic interview experience using AI.

- AI Feedback  
  Provides structured feedback on candidate responses, including strengths and areas for improvement.

- Interview Report  
  Generates a downloadable report summarizing the interview session.

## Tech Stack

- Python
- Streamlit
- Google Gemini API
- LangChain
- FAISS
- PyMuPDF
- Sentence Transformers
- Pandas
- NumPy
- ReportLab

## Project Structure

```text
.
├── SmartHire.py
├── app/
├── pages/
├── requirements.txt
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.10+
- A Google Gemini API key

### Installation

1. Clone the repository:
   ```bash
git clone https://github.com/VinitaPatil2005/SmartHire-AI-Mock-Interview-Agent.git
cd SmartHire-AI-Mock-Interview-Agent
   ```

2. Create and activate a virtual environment:
   ```bash
python -m venv venv
   ```

   Windows:
   ```bash
venv\Scripts\activate
   ```

   macOS/Linux:
   ```bash
source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
pip install -r requirements.txt
   ```

4. Add environment variables:
   Create a `.env` file in the project root and define the required keys:
   ```env
GOOGLE_API_KEY=your_gemini_api_key
   ```

## Run the App

Start the Streamlit application with:

```bash
streamlit run SmartHire.py
```

The app will open in your browser, typically at:

```text
http://localhost:8501
```

## How It Works

1. Upload or provide a resume
2. Enter a job description
3. Generate interview questions
4. Start a mock interview
5. Review AI feedback
6. Download the interview report

## Configuration

If the app uses additional settings, check the `app/` package for configuration values such as app title, prompt templates, and helper utilities.

## Requirements

All dependencies are listed in `requirements.txt`.

## Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the terms specified in the `LICENSE` file.

## Acknowledgements

- Google Gemini
- Streamlit
- LangChain
- FAISS
