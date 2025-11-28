from flask import render_template, redirect, Blueprint, url_for, flash, request, jsonify, session
from flask_login import login_required, current_user

settings = Blueprint('settings', __name__)

@login_required
@settings.route("/settings", methods=["GET", "POST"])
def user_settings():

    return render_template("settings.html")

