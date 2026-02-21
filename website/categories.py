from flask import render_template, redirect, Blueprint, url_for, flash, request, jsonify, session
from flask_login import login_required, current_user
from dateutil import parser
from bson import ObjectId
from .rss_feeds import neurosci_articles, gut_articles, heart_articles #dict of feeds
from .db import get_users_collection

categories = Blueprint('categories', __name__)

def article_format(articles):

    # formats dates to Month Day, Year
    for source, article in articles:
        dt = parser.parse(article.date)
        article.date = dt.strftime("%b %d, %Y")

    daily_debrief = articles[:5]
    rest_articles = articles[5:]

    page = request.args.get('page', 1, type=int)
    per_page =12
    total_articles = len(rest_articles)
    start = (page-1) * per_page
    end = start + per_page
    paginated_articles = rest_articles[start:end]

    total_pages = total_articles + per_page + 1

    return paginated_articles, page, daily_debrief, page, total_pages
# return paginated_articles, page, daily_debrief, page, total_pages

@categories.route("/neuro", methods=["GET"])
def neuro():
    articles = neurosci_articles()
    paginated_articles, page, daily_debrief, page, total_pages = article_format(articles)

    if current_user.is_authenticated:
        return render_template("neuro.html", name=current_user.username, articles=paginated_articles, daily_debrief=daily_debrief, page=page, total_pages=total_pages)
        
    else:
        flash("Login or create an account!", category="error")
        return render_template("neuro.html", articles=paginated_articles, page=page,daily_debrief=daily_debrief, total_pages=total_pages)
    
@categories.route("/gut", methods=["GET"])
def gut():
    articles = gut_articles()
    paginated_articles, page, daily_debrief, page, total_pages = article_format(articles)

    if current_user.is_authenticated:
        return render_template("gut.html", name=current_user.username, articles=paginated_articles, daily_debrief=daily_debrief, page=page, total_pages=total_pages)
        
    else:
        flash("Login or create an account!", category="error")
        return render_template("gut.html", articles=paginated_articles, page=page,daily_debrief=daily_debrief, total_pages=total_pages)
    
@categories.route("/heart", methods=["GET"])
def heart():
    articles = heart_articles()
    paginated_articles, page, daily_debrief, page, total_pages = article_format(articles)

    if current_user.is_authenticated:
        return render_template("heart.html", name=current_user.username, articles=paginated_articles, daily_debrief=daily_debrief, page=page, total_pages=total_pages)
        
    else:
        flash("Login or create an account!", category="error")
        return render_template("heart.html", articles=paginated_articles, page=page,daily_debrief=daily_debrief, total_pages=total_pages)