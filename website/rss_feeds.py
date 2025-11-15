import feedparser

rss_feeds = {
    'Yahoo Finance': 'https://finance.yahoo.com/news/rssindex',
    'Hacker News': 'https://news.ycombinator.com/rss',
    'Wall Street Journal': 'https://feeds.a.dj.com/rss/RSSMarketsMain.xml',
    'CNBC': 'https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=15839069'
}

def parse():
    articles = []
    for source, feed in rss_feeds.items():
        parsed_feed = feedparser.parse(feed)
        entries = [(source, entry) for entry in parsed_feed.entries]
        articles.extend(entries)

    # sorts articles for the newest
    articles = sorted(articles, key=lambda x: x[1].published_parsed, reverse=True)

    # print(articles[1][1])
    return articles