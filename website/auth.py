from flask import render_template, redirect, Blueprint, url_for, flash, request, session
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash 
from .User import User 
from.db import users 

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":

        #clear email 
        session.clear()

        email = request.form["email"]
        password = request.form["password"]

        session["email"] = email

        #find match for email in db
        doc = users.find_one({"email": email})

        # if it returns a match
        if doc:
            if check_password_hash(doc["password"], password):
                user = User(doc)
                login_user(user, remember=True) # keeps user logged in 
                flash("Logged in successfully!", category="success")
                return redirect(url_for("routes.index"))
            else:
                
                flash("Wrong password, try again.", category="error")

        else:
            flash("Email does not exist!", category="error")

    return render_template("login.html", user=current_user) 