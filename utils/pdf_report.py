from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import os


def generate_pdf_report(
    filename,
    ats_score,
    job_match_score,
    skills,
    ai_suggestions
):

    report_path = os.path.join("reports", filename)

    doc = SimpleDocTemplate(report_path)

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>AI Resume Analyzer Report</b>", styles["Title"]))

    story.append(Paragraph(f"<b>ATS Score:</b> {ats_score}/100", styles["BodyText"]))

    story.append(Paragraph(f"<b>Job Match:</b> {job_match_score}%", styles["BodyText"]))

    story.append(
        Paragraph(
            "<b>Skills Found:</b> " + ", ".join(skills),
            styles["BodyText"]
        )
    )

    story.append(Paragraph("<b>AI Suggestions</b>", styles["Heading2"]))

    story.append(
        Paragraph(
            ai_suggestions.replace("\n", "<br/>"),
            styles["BodyText"]
        )
    )

    doc.build(story)

    return report_path