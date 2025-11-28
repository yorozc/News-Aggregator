from collections import UserDict
import email
from os import error
from sre_constants import SUCCESS
from bson import ObjectId
from flask import render_template, redirect, Blueprint, url_for, flash, request, jsonify, session
from flask_login import login_required, current_user
from werkzeug.security import check_password_hash

from website.auth import login
from .db import get_users_collection

settings = Blueprint('settings', __name__)

@login_required
@settings.route("/settings", methods=["GET", "POST"])
def user_settings():
    users = get_users_collection()
    user_id = ObjectId(current_user.id)
    user = users.find_one({'_id': user_id})

    return render_template("settings.html", name=current_user.username, email=user["email"])

@settings.route("/edit_name", methods=["POST"])
def edit_name():
    if request.method == "POST":
        users = get_users_collection()
        user_id = ObjectId(current_user.id)

        edited_name = request.form["name"]

        try:
            users.update_one({'_id': user_id}, {'$set': {'first_name': edited_name}})
            flash('Account name changed!', category="success")

        except Exception as e:
            print(f"Name could not be updated!\nError: {e}")

    return redirect(url_for("settings.user_settings"))

@settings.route("/edit_email", methods=["POST"])
def edit_email():
    if request.method == "POST":
        users = get_users_collection()
        user_id = ObjectId(current_user.id)

        edited_email = request.form["email"]

        current_email = users.find_one({'_id':user_id})["email"]

        existing_user = users.find_one({'email': edited_email})
        existing_email = ''

        if existing_user:
            existing_email = existing_user["email"]

        if existing_email == current_email:
            flash('This is already your email!', category="error")
            return redirect(url_for("settings.user_settings"))
        
        elif existing_email:
            flash(f"Email {existing_email} is already taken!", category="error")
            return redirect(url_for("settings.user_settings"))
            
        try:
            users.update_one({'_id': user_id}, {'$set':{'email': edited_email}})
            flash('Email changed!', category="success")

        except Exception as e:
            print(f"Email could not be updated!\nError: {e}")

    return redirect(url_for("settings.user_settings"))


