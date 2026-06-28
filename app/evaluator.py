from app.gemini_service import generate_response
from app.prompts import MOCK_INTERVIEW_EVALUATION_PROMPT


def evaluate_answer(question, answer):

    prompt = MOCK_INTERVIEW_EVALUATION_PROMPT.format(
        question=question,
        answer=answer
    )

    return generate_response(prompt)