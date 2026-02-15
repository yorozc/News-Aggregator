import feedparser

rss_feeds = {
    'NPR Health Shots': 'https://feeds.npr.org/1128/rss.xml',
    'Medical News Bulletin': 'https://medicalnewsbulletin.com/feed',
    'Medscape': 'https://www.medscape.com/cx/rssfeeds/2700.xml',
}

neuro_sci_feeds = {
    'JNeuroSci': 'https://www.jneurosci.org/rss/current.xml',
    'Behavior/Cognitive': 'https://www.jneurosci.org/rss/Behavioral_Cognitive.xml',
}

gut_feeds ={
    'Gut-BMJ': 'https://gut.bmj.com/rss/ahead.xml'
}

heart_feeds = {
    'Heart-BMJ': 'https://heart.bmj.com/rss/ahead.xml'
}

def parsed_articles():
    articles = []
    for source, feed in rss_feeds.items():
        parsed_feed = feedparser.parse(feed)
        entries = [(source, entry) for entry in parsed_feed.entries]
        articles.extend(entries)

    # sorts articles for the newest
    articles = sorted(articles, key=lambda x: x[1].published_parsed, reverse=True)

    # print(articles[1][1])
    return articles

def neurosci_articles():
    articles = []
    for source, feed in neuro_sci_feeds.items():
        parsed_feed = feedparser.parse(feed)
        entries = [(source, entry) for entry in parsed_feed.entries]
        articles.extend(entries)
    print(articles)

    # sorts articles for the newest
    articles = sorted(articles, key=lambda x: x[1].updated, reverse=True)

    return articles

def gut_articles():
    articles = []
    for source, feed in gut_feeds.items():
        parsed_feed = feedparser.parse(feed)
        entries = [(source, entry) for entry in parsed_feed.entries]
        articles.extend(entries)
    print(articles)

    # sorts articles for the newest
    articles = sorted(articles, key=lambda x: x[1].date, reverse=True)

    return articles

def heart_articles():
    articles = []
    for source, feed in gut_feeds.items():
        parsed_feed = feedparser.parse(feed)
        entries = [(source, entry) for entry in parsed_feed.entries]
        articles.extend(entries)
    print(articles)

    # sorts articles for the newest
    articles = sorted(articles, key=lambda x: x[1].date, reverse=True)

    return articles
