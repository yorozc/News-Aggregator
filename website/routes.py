from flask import render_template, redirect, Blueprint, url_for, flash, request, session

routes = Blueprint('routes', __name__)

@routes.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")