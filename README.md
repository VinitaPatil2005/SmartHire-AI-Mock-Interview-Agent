# SmartHire AI Mock Interview Agent

SmartHire is an AI-powered mock interview platform designed to help candidates prepare for technical and HR interviews. It uses a candidate's resume and target job description to generate personalized interview questions, conduct an interactive mock interview, evaluate responses, and generate a performance report.

## Features

* **Resume Analysis** — Extracts and analyzes information from uploaded PDF resumes.
* **Job Description Analysis** — Processes the job description to identify relevant requirements and interview areas.
* **Personalized Questions** — Generates interview questions based on the candidate's resume and job description.
* **AI Mock Interview** — Conducts an interactive interview using AI-generated questions.
* **Response Evaluation** — Evaluates candidate answers and provides structured feedback.
* **Interview Report** — Generates a downloadable report containing interview results and feedback.
* **Settings** — Provides configuration options for the application.

## Tech Stack

* **Python** — Core application development
* **Streamlit** — Web interface and application framework
* **Google Gemini API** — Interview question generation and response evaluation
* **PyMuPDF** — PDF resume text extraction
* **Pandas / NumPy** — Data processing
* **ReportLab** — Interview report generation

## How It Works

```text
Resume Upload
      |
      v
Resume Analysis
      |
      v
Job Description
      |
      v
Context Processing
      |
      v
Personalized Questions
      |
      v
AI Mock Interview
      |
      v
Answer Evaluation
      |
      v
AI Feedback
      |
      v
Interview Report
```

## Project Structure

```text
SmartHire-AI-Mock-Interview-Agent/
│
├── SmartHire.py
│
├── app/
│   ├── config.py
│   ├── evaluator.py
│   ├── gemini_service.py
│   ├── interview.py
│   ├── jd_parser.py
│   ├── prompts.py
│   ├── report.py
│   ├── resume_parser.py
│   └── utils.py
│
├── pages/
│   ├── 1_Resume_Analysis.py
│   ├── 2_Job_Description.py
│   ├── 3_Mock_Interview.py
│   ├── 4_Interview_Report.py
│   └── 5_Settings.py
│
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

## Configuration

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_gemini_api_key
```

Replace `your_gemini_api_key` with your Google Gemini API key.

Do not commit API keys or the `.env` file to the repository.

## Run the Application

Start the Streamlit application:

```bash
streamlit run SmartHire.py
```

The application will normally be available at:

```text
http://localhost:8501
```

## Requirements

* Python 3.10+
* Google Gemini API key
* Internet connection for Gemini API access

## Contributing

Contributions are welcome. To contribute:

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Test the application.
5. Submit a pull request.

## License

This project is licensed under the terms specified in the `LICENSE` file.

## Acknowledgements

* Google Gemini
* Streamlit
* PyMuPDF
* Pandas
* NumPy
* ReportLab
