from flask import Flask
from flask_scss import Scss
from flask_login import LoginManager
from bson import ObjectId
import os 
from .routes import routes 
from .auth import auth 
from .settings import settings
from .db import get_users_collection
from .User import User 

def create_app():
    app = Flask(__name__)

    Scss(app) 

    app.register_blueprint(routes, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(settings, url_prefix="/")
    


    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev-key")
    app.config["SESSION_COOKIE_SECURE"] = False #change true when deploy
    app.config["REMEMBER_COOKIE_SECURE"] = False #change to true
    app.config["SESSION_COOKIE_SAMESITE"] = "Lax"

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app) 

    @login_manager.user_loader
    def load_user(id):
        try:
            _id = ObjectId(id)

        except Exception:
            return None
        users = get_users_collection()
        doc = users.find_one({"_id": _id})
        return User(doc) if doc else None

    return app