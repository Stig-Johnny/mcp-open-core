# ARCHIVED: This file has been moved to /archive/news_parser.py and is not used by the main system.
# data_ingestion/news_parser.py

import feedparser

class NewsParser:
    def __init__(self, rss_url="https://cryptonews.com/news/feed"):
        self.rss_url = rss_url

    def fetch_headlines(self):
        feed = feedparser.parse(self.rss_url)
        articles = [{"title": entry.title, "link": entry.link} for entry in feed.entries]
        return articles

if __name__ == "__main__":
    np = NewsParser()
    for article in np.fetch_headlines():
        print(article)
