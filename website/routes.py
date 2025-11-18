from flask import render_template, redirect, Blueprint, url_for, flash, request, jsonify, session
from flask_login import login_required, current_user
from dateutil import parser
from bson import ObjectId
from .rss_feeds import parsed_articles #dict of feeds
from .db import users


routes = Blueprint('routes', __name__)

@routes.route("/", methods=["GET", "POST"])
def index():
    articles = parsed_articles()

    # formats dates to Month Day, Year
    for source, article in articles:
        dt = parser.parse(article.published)
        article.published = dt.strftime("%b %d, %Y")

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

    articles = parsed_articles()

    for source, article in articles:
        dt = parser.parse(article.published)
        article.published = dt.strftime("%b %d, %Y")

    results = [article for article in articles if query.lower() in article[1].title.lower()]

    return render_template('search.html', articles=results, query=query)

@login_required
@routes.route("/save", methods=["POST"])
def save():

    data = request.get_json()
    source = data.get('source')
    title = data.get('title')
    link = data.get('article')
    user_id = ObjectId(current_user.id)

    #check if article already exists
    article_doc = users.update_one(
        {'_id': user_id},
        {'$addToSet': {"saved_articles": {"source": source, "title": title, "link": link}}}
    )
    
    if article_doc.modified_count == 0:
        return jsonify({"status": "error", "message": "Article is already saved"}), 200

    return jsonify({"status": "success", "message": f"Saved article from {source}"}), 201

@login_required
@routes.route("/saved_articles")
def saved_articles():
    user_id = ObjectId(current_user.id)

    doc = users.find_one({'_id': user_id})

    if doc:
        arr = doc.get('saved_articles') #creates dict of saved articles
    else: 
        print('Doc not found')

    return render_template("saved_articles.html", articles=arr)

@login_required
@routes.route("/delete", methods=["DELETE"])
def delete(): # deletes selected articles
    user_id = ObjectId(current_user.id)

    data = request.get_json()
    link = data.get('article')

    result = users.update_one(
        {'_id': user_id},
        {'$pull': {'saved_articles': {'link': link}}}
    )

    if result.modified_count == 0:
        return jsonify({"status": "error", "message": f"Article not found!"})

    return jsonify({"status": "success", "message": f"Article deleted!"}), 201


