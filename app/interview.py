from app.gemini_service import generate_response

from app.prompts import (
    INTERVIEW_QUESTION_PROMPT
)


def generate_interview_questions(
    resume: str,
    job_description: str
) -> str:
    """
    Generate personalized interview questions.
    """

    prompt = INTERVIEW_QUESTION_PROMPT.format(
        resume=resume,
        jd=job_description
    )

    return generate_response(prompt)