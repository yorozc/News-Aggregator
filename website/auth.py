from flask import render_template, redirect, Blueprint, url_for, flash, request, session
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash 
from .User import User 
from.db import users 

auth = Blueprint('auth', __name__)