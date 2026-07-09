from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
from utils.parser import extract_text
from utils.ats import calculate_ats_score
from utils.skills import extract_skills
from utils.job_match import match_job_description
from utils.gemini_ai import get_resume_suggestions
from werkzeug.security import generate_password_hash, check_password_hash
from config import Config
from extensions import db
from models.user import User
from routes.auth import auth
from routes.upload import upload
from routes.dashboard import dashboard

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(auth)
app.register_blueprint(upload)
app.register_blueprint(dashboard)

@app.route("/")
def home():
    return render_template("index.html")


with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)