from flask import render_template, redirect, Blueprint, url_for, flash, request, session
from flask_login import login_required, current_user
from .rss_feeds import parse, rss_feeds #dict of feeds & list of articles
import feedparser
from .db import users


routes = Blueprint('routes', __name__)

@routes.route("/", methods=["GET", "POST"])
def index():
    articles = parse()

    page = request.args.get('page', 1, type=int)
    per_page =10
    total_articles = len(articles)
    start = (page-1) * per_page
    end = start + per_page
    paginated_articles = articles[start:end]
        
    if current_user.is_authenticated:

        return render_template("index.html", name=current_user.username, articles=paginated_articles, page=page, total_pages=total_articles // per_page + 1)
       
    else:

        flash("Login or create an account!", category="error")
        return render_template("index.html", articles=paginated_articles, page=page, total_pages=total_articles // per_page + 1)
    
@routes.route("/search", methods=["GET", "POST"])
def search():
    query = request.args.get('q')

    articles = parse()

    results = [article for article in articles if query.lower() in article[1].title.lower()]

    return render_template('search.html', articles=results, query=query)