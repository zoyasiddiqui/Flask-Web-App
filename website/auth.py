from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth', __name__)

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password1")

        user = User.query.filter_by(email=email).first()
        print(user.password)

        if user:
            curr_password = generate_password_hash(password, method="sha256")
            if curr_password == user.password:
                flash("Logged in", category="success")
                return redirect(url_for('views.home'))
            else:
                flash("Incorrect info", category="error")
        else:
            flash("User does not exist", category="error")
    
    return render_template("login.html")

@auth.route("/logout")
def logout():
    return ""

@auth.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        #a few basic python checks
        user = User.query.filter_by(email=email).first()
        if user:
            flash("User already exists", category="error")
        if len(email) < 4:
            flash("Email must be greater than 4 characters", category="error")
        elif len(first_name) < 2:
            flash("First name must be greater than 1 character", category="error")
        elif password1 != password2:
            flash("Passwords do not match", category="error")
        elif len(password1) < 7:
            flash("Passwords must be at least 7 categories", category="error")
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method="sha256"))
            db.session.add(new_user)
            db.session.commit()

            flash("Account created!", category="success")
            return redirect(url_for('views.home'))


    return render_template("signup.html")
