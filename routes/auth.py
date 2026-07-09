from flask import Blueprint, render_template, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash

from extensions import db
from models.user import User

from forms.register_form import RegisterForm
from forms.login_form import LoginForm

auth = Blueprint("auth", __name__)


@auth.route("/register", methods=["GET", "POST"])
def register():

    form = RegisterForm()

    if form.validate_on_submit():

        existing_user = User.query.filter_by(email=form.email.data).first()

        if existing_user:
            return "<h2>Email already registered!</h2>"

        hashed_password = generate_password_hash(form.password.data)

        new_user = User(
            full_name=form.full_name.data,
            email=form.email.data,
            password=hashed_password
        )

        db.session.add(new_user)
        db.session.commit()

        return "<h2>User Registered Successfully!</h2>"

    return render_template("register.html", form=form)


@auth.route("/login", methods=["GET", "POST"])
def login():

    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()

        if user and check_password_hash(user.password, form.password.data):

            session["user_id"] = user.id
            session["user_name"] = user.full_name

            return redirect(url_for("dashboard.dashboard_home"))

        return "<h2>Invalid Email or Password!</h2>"

    return render_template("login.html", form=form)

@auth.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("auth.login"))