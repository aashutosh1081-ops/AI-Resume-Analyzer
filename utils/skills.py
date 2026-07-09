def extract_skills(resume_text):

    skills_list = [
        "Python",
        "Java",
        "C",
        "C++",
        "SQL",
        "MySQL",
        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "Flask",
        "Django",
        "Git",
        "GitHub",
        "Machine Learning",
        "Data Analysis",
        "Excel",
        "Power BI",
        "Communication",
        "Leadership"
    ]

    found_skills = []

    resume = resume_text.lower()

    for skill in skills_list:

        if skill.lower() in resume:
            found_skills.append(skill)

    return found_skills