import feedparser

rss_feeds = {
    'Yahoo Finance': 'https://finance.yahoo.com/news/rssindex',
    'Hacker News': 'https://news.ycombinator.com/rss',
    'Wall Street Journal': 'https://feeds.a.dj.com/rss/RSSMarketsMain.xml',
    'CNBC': 'https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=15839069'
}

'''
list of news stations to add
Hacker News, 
https://news.ycombinator.com/item?id=16908241
'''

def parse():
    articles = []
    for source, feed in rss_feeds.items():
        parsed_feed = feedparser.parse(feed)
        entries = [(source, entry) for entry in parsed_feed.entries]
        articles.extend(entries)

    # sorts articles for the newest
    articles = sorted(articles, key=lambda x: x[1].published_parsed, reverse=True)

    

    return articles

# parse can be used for the daily debrief (most recent news)
# then I can jsut randomize the rest to display them until I think of an algo to control the displaying of articles