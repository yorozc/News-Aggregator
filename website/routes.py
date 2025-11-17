from flask import render_template, redirect, Blueprint, url_for, flash, request, session
from flask_login import login_required, current_user
from .rss_feeds import parse #dict of feeds


routes = Blueprint('routes', __name__)

@routes.route("/", methods=["GET", "POST"])
def index():
    articles = parse()

    daily_debrief = articles[:5]
    rest_articles = articles[5:]

    page = request.args.get('page', 1, type=int)
    per_page =12
    total_articles = len(rest_articles)
    start = (page-1) * per_page
    end = start + per_page
    paginated_articles = rest_articles[start:end]

    total_pages = total_articles + per_page + 1
        
    if current_user.is_authenticated:

        return render_template("index.html", name=current_user.username, articles=paginated_articles, daily_debrief=daily_debrief, page=page, total_pages=total_pages)
       
    else:

        flash("Login or create an account!", category="error")
        return render_template("index.html", articles=paginated_articles, page=page,daily_debrief=daily_debrief, total_pages=total_pages)
    
@routes.route("/search", methods=["GET", "POST"])
def search():
    query = request.args.get('q')

    articles = parse()

    results = [article for article in articles if query.lower() in article[1].title.lower()]

    return render_template('search.html', articles=results, query=query)