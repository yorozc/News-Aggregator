from flask import render_template, redirect, Blueprint, url_for, flash, request, jsonify, session
from flask_login import login_required, current_user
from dateutil import parser
from bson import ObjectId
from .rss_feeds import neurosci_articles #dict of feeds
from .db import get_users_collection

categories = Blueprint('categories', __name__)

