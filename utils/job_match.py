def match_job_description(resume_text, job_description):

    resume = resume_text.lower()
    job = job_description.lower()

    job_words = job.split()

    matched = 0

    for word in job_words:

        if word in resume:
            matched += 1

    if len(job_words) == 0:
        return 0

    score = int((matched / len(job_words)) * 100)

    if score > 100:
        score = 100

    return score