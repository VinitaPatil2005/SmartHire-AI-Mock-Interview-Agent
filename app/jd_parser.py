def clean_job_description(job_description):
    """
    Clean the job description text.

    Parameters
    ----------
    job_description : str

    Returns
    -------
    str
    """

    job_description = job_description.strip()

    job_description = " ".join(job_description.split())

    return job_description