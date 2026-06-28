def clean_job_description(job_description):

    job_description = job_description.strip()

    job_description = " ".join(
        job_description.split()
    )

    return job_description