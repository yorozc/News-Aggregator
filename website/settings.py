from collections import UserDict
from bson import ObjectId
from flask import render_template, redirect, Blueprint, url_for, flash, request, jsonify, session
from flask_login import login_required, current_user
from werkzeug.security import check_password_hash
from .db import get_users_collection

settings = Blueprint('settings', __name__)

@login_required
@settings.route("/settings", methods=["GET", "POST"])
def user_settings():
    users = get_users_collection()
    user_id = ObjectId(current_user.id)
    user = users.find_one({'_id': user_id})

    return render_template("settings.html", name=current_user.username, email=user["email"])

