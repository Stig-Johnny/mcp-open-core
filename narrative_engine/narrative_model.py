# narrative_engine/narrative_model.py

"""
MCP Open Core - Narrative Parser Module
Very basic NLP scaffold for narrative detection.
"""

# ARCHIVED: This file has been moved to /archive/narrative_model.py and is not used by the main system.

class NarrativeParser:
    def __init__(self):
        self.keywords = ["bullish", "bearish", "ETF", "inflation", "whale"]

    def parse_news(self, news_article):
        score = sum(1 for word in self.keywords if word in news_article.lower())
        print(f"Parsed sentiment score: {score}")
        return score

if __name__ == "__main__":
    np = NarrativeParser()
    np.parse_news("ETF inflows are extremely bullish, whales accumulating BTC")
