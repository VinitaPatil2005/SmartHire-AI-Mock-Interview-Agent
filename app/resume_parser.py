import fitz


def extract_resume_text(pdf_path):
    """
    Extract text from a PDF resume.

    Parameters
    ----------
    pdf_path : str
        Path to the uploaded PDF file.

    Returns
    -------
    str
        Extracted resume text.
    """

    document = fitz.open(pdf_path)

    text = ""

    for page in document:
        text += page.get_text()

    document.close()

    return text.strip()