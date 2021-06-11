from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template("login.html")


@auth.route('/logout')
def logout():
    """Log user out"""


@auth.route('/sign-up')
def sign_up():
    return render_template("register.html")

@auth.route('/workout-plan')
def workoutplan():
    return render_template("workout-plan.html")
