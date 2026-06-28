from app.gemini_service import generate_response

from app.prompts import (
    INTERVIEW_QUESTION_PROMPT
)


def generate_interview_questions(
    resume,
    job_description
):

    prompt = INTERVIEW_QUESTION_PROMPT.format(

        resume=resume,

        jd=job_description

    )

    return generate_response(prompt)