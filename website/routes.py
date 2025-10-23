from flask import render_template, redirect, Blueprint, url_for, flash, request, session
from flask_login import login_required, current_user
from .db import users

routes = Blueprint('routes', __name__)

@routes.route("/", methods=["GET", "POST"])
def index():
    if current_user.is_authenticated:

        return render_template("index.html", user=current_user)
    else:
        flash("Login or create an account!", category="error")
        return render_template("index.html")