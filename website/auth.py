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

@auth.route('/logout')
@login_required # makes sure that page is not accessible unless user is logged in
def logout():
    logout_user()
    return render_template("login.html")

# create new account
@auth.route('/signup', methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = generate_password_hash(request.form['password'], method='pbkdf2:sha256')
        
        session["email"] = email

        # checks if email already exists
        doc = users.find_one({"email": email}) 
        if doc:
            print("Email already in use!")
        
        #TODO: use regex to check email formats

        # creates new user 
        try:
            users.insert_one({"first_name": first_name,
                              "last_name": last_name,
                              "email": email,
                              "password": password,
                            })
            flash("User created!", category="success")
            user = User(doc)
            login_user(user, remember=True) 
            return redirect(url_for("routes.index"))
        
        except Exception as e:
            return f"ERROR:{e}"
        
    else:
        return render_template("signup.html", user=current_user)