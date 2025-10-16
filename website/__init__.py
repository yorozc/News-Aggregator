from flask import Flask
from flask_scss import Scss
import os 
from .routes import routes 
from .auth import auth 

def create_app():
    app = Flask(__name__)
    Scss(app) 

    app.register_blueprint(routes, url_prefix="/")
    app.register_blueprint(auth, url_prefix='/')

    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev-key")
    app.config["SESSION_COOKIE_SECURE"] = False #change true when deploy
    app.config["REMEMBER_COOKIE_SECURE"] = False #change to true
    app.config["SESSION_COOKIE_SAMESITE"] = "Lax"


    return app