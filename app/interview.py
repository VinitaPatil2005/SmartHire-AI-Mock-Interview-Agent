import json

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

    response = generate_response(prompt)

    response = (
        response
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    try:

        questions = json.loads(response)

        return questions

    except Exception:

        return []