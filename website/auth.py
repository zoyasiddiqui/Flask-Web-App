from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")

@auth.route("/logout")
def logout():
    return ""

@auth.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        #a few basic python checks
        if len(email) < 4:
            flash("Email must be greater than 4 characters", category="error")
        elif len(firstName) < 2:
            flash("First name must be greater than 1 character", category="error")
        elif password1 != password2:
            flash("Passwords do not match", category="error")
        elif len(password1) < 7:
            flash("Passwords must be at least 7 categories", category="error")
        else:
            flash("Account created!", category="success")

    return render_template("signup.html")
