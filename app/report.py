from app.gemini_service import generate_response
from app.prompts import INTERVIEW_REPORT_PROMPT


def generate_report(evaluation):

    prompt = INTERVIEW_REPORT_PROMPT.format(
        evaluation=evaluation
    )

    return generate_response(prompt)