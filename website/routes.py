from flask import render_template, redirect, Blueprint, url_for, flash, request, session
from flask_login import login_required, current_user
from .db import users

routes = Blueprint('routes', __name__)

@routes.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")