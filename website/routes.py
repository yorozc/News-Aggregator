from flask import render_template, redirect, Blueprint, url_for, flash, request, session
from flask_login import login_required, current_user
from .db import users

routes = Blueprint('routes', __name__)

@routes.route("/", methods=["GET", "POST"])
@login_required
def index():
    email = session.get("email")

    if not email:
        return redirect(url_for("auth.login"))
    
    user = users.find_one({"email": email})

    return render_template("index.html", user=current_user)