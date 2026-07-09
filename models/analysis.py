from datetime import datetime
from extensions import db


class Analysis(db.Model):

    __tablename__ = "analysis"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
        nullable=False
    )

    filename = db.Column(
        db.String(255),
        nullable=False
    )

    ats_score = db.Column(
        db.Integer,
        nullable=False
    )

    job_match_score = db.Column(
        db.Integer,
        nullable=False
    )

    skills = db.Column(
        db.Text,
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )