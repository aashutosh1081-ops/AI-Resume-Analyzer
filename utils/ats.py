import re


def calculate_ats_score(resume_text):

    resume = resume_text.lower()

    score = 0

    # ---------- Contact Information ----------

    if re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", resume):
        score += 10

    if re.search(r"\+?\d[\d\s\-]{9,}", resume):
        score += 5

    # ---------- Education ----------

    education_keywords = [
        "bca",
        "b.tech",
        "bachelor",
        "mca",
        "degree",
        "university",
        "college"
    ]

    if any(word in resume for word in education_keywords):
        score += 10

    # ---------- Experience ----------

    experience_keywords = [
        "experience",
        "internship",
        "worked",
        "developer",
        "engineer"
    ]

    if any(word in resume for word in experience_keywords):
        score += 15

    # ---------- Projects ----------

    project_keywords = [
        "project",
        "github",
        "portfolio",
        "application",
        "website"
    ]

    if any(word in resume for word in project_keywords):
        score += 15

    # ---------- Skills ----------

    skills = [
        "python",
        "java",
        "sql",
        "mysql",
        "flask",
        "html",
        "css",
        "javascript",
        "react",
        "git"
    ]

    skill_count = 0

    for skill in skills:
        if skill in resume:
            skill_count += 1

    score += min(skill_count * 4, 20)

    # ---------- Certifications ----------

    cert_keywords = [
        "certification",
        "certificate",
        "coursera",
        "udemy",
        "nptel"
    ]

    if any(word in resume for word in cert_keywords):
        score += 10

    # ---------- Resume Length ----------

    word_count = len(resume.split())

    if word_count >= 250:
        score += 10

    # ---------- Final ----------

    return min(score, 100)