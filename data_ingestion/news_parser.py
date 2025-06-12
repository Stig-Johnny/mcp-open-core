# data_ingestion/news_parser.py
"""
MCP Open Core - News Data Ingestion Module
Fetches crypto news headlines for live fusion pipeline.
"""

import feedparser

class NewsParser:
    def __init__(self, rss_url="https://cryptonews.com/news/feed"):
        self.rss_url = rss_url

    def fetch_headlines(self, limit=10):
        feed = feedparser.parse(self.rss_url)
        articles = [{"title": entry.title, "link": entry.link} for entry in feed.entries[:limit]]
        return articles

if __name__ == "__main__":
    np = NewsParser()
    for article in np.fetch_headlines():
        print(article)
