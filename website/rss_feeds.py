import feedparser

rss_feeds = {
    'NPR Health Shots': 'https://feeds.npr.org/1128/rss.xml',
    'Medical News Bulletin': 'https://medicalnewsbulletin.com/feed',
    'Medscape': 'https://www.medscape.com/cx/rssfeeds/2700.xml',
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