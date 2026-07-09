import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def get_resume_suggestions(resume_text):

    prompt = f"""
You are an expert ATS Resume Reviewer.

Analyze the resume and return ONLY the following sections.

IMPORTANT RULES:

- Do NOT use markdown.
- Do NOT use ** or * or #.
- Use plain text only.
- Each point should be on a new line.
- Keep each suggestion short.
- Give professional advice.

Use EXACTLY this format:

OVERALL RATING
8/10

ATS IMPROVEMENT
Improve resume summary.
Add measurable achievements.
Use stronger action verbs.

STRENGTHS
Good technical skills.
Projects are relevant.
Resume is easy to read.

WEAKNESSES
Few projects.
Limited certifications.

MISSING SKILLS
Docker
AWS
React
CI/CD

CAREER ADVICE
Build more projects.
Apply for internships.
Improve LinkedIn profile.

INTERVIEW TIPS
Revise Python.
Prepare project explanation.
Practice HR questions.

Resume:

{resume_text}
"""

    response = model.generate_content(prompt)

    return response.text