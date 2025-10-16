from flask import Flask
from flask_scss import Scss
import os 

def create_app():
    app = Flask(__name__)
    Scss(app) 

    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev-key")
    app.config["SESSION_COOKIE_SECURE"] = False #change true when deploy
    app.config["REMEMBER_COOKIE_SECURE"] = False #change to true
    app.config["SESSION_COOKIE_SAMESITE"] = "Lax"