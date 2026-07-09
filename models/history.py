from extensions import db
from datetime import datetime


class ResumeHistory(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    filename = db.Column(db.String(200), nullable=False)

    ats_score = db.Column(db.Integer)

    job_match = db.Column(db.Integer)

    ai_rating = db.Column(db.String(20))

    pdf_report = db.Column(db.String(200))

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )