from flask import render_template, redirect, Blueprint, url_for, flash, request, session
from flask_login import login_required, current_user
from .rss_feeds import rss_feeds #dict of feeds
from .db import users


routes = Blueprint('routes', __name__)

@routes.route("/", methods=["GET", "POST"])
def index():
    if current_user.is_authenticated:
        
        return render_template("index.html", name = current_user.username)
    else:

        flash("Login or create an account!", category="error")
        return render_template("index.html")