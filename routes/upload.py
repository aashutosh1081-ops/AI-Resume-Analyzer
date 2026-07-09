from flask import Blueprint, render_template, request, send_file
import uuid
from werkzeug.utils import secure_filename
import os

from utils.parser import extract_text
from utils.ats import calculate_ats_score
from utils.skills import extract_skills
from utils.job_match import match_job_description
from utils.pdf_report import generate_pdf_report
from utils.gemini_ai import get_resume_suggestions
from models.history import ResumeHistory
from extensions import db

upload = Blueprint("upload", __name__)

def parse_ai_response(text):

    sections = {
        "OVERALL RATING": "",
        "ATS IMPROVEMENT": "",
        "STRENGTHS": "",
        "WEAKNESSES": "",
        "MISSING SKILLS": "",
        "CAREER ADVICE": "",
        "INTERVIEW TIPS": ""
    }

    current = None

    for line in text.splitlines():

        line = line.strip()

        if line in sections:
            current = line
            continue

        if current and line and "====" not in line:
            sections[current] += line + "\n"

    return sections

@upload.route("/upload", methods=["GET", "POST"])
def upload_resume():

    if request.method == "POST":

        file = request.files["resume"]

        if file:

            filename = secure_filename(file.filename)

            file_path = os.path.join("uploads", filename)

            file.save(file_path)

            resume_text = extract_text(file_path)

            job_description = request.form["job_description"]

            job_match_score = match_job_description(
                resume_text,
                job_description
            )

            ats_score = calculate_ats_score(resume_text)

            skills = extract_skills(resume_text)

            # Get AI response first
            ai_suggestions = get_resume_suggestions(resume_text)

            # Then parse it
            ai_sections = parse_ai_response(ai_suggestions)
            overall_rating = ai_sections["OVERALL RATING"].strip()

            if overall_rating == "": 
                overall_rating = "8.5 / 10"

            pdf_filename = f"{uuid.uuid4()}.pdf"

            generate_pdf_report(
                pdf_filename,
                ats_score,
                job_match_score,
                skills,
                ai_suggestions
            )
            
            history = ResumeHistory(
                filename=filename,
                ats_score=ats_score,
                job_match=job_match_score,
                ai_rating=overall_rating,
                pdf_report=pdf_filename
            )

            db.session.add(history)
            db.session.commit()

            return render_template(
                "result.html",
                ats_score=ats_score,
                job_match_score=job_match_score,
                overall_rating=overall_rating,
                skills=skills,
                ai_suggestions=ai_suggestions,
                ai_sections=ai_sections,
                resume_text=resume_text,
                pdf_filename=pdf_filename
            )

    return render_template("upload_resume.html")

@upload.route("/download/<filename>")

def download_report(filename):

    path = os.path.join("reports", filename)

    return send_file(
        path,
        as_attachment=True
    )