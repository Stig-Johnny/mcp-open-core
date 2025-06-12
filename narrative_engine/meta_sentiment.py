# MCP Phase 36 — Meta-Sentiment Cluster Engine v1.0

import random

class MetaSentimentEngine:
    def __init__(self):
        self.sentiment_window = []

    def simulate_news_sentiment(self):
        # Simulated sentiment score: -1 = negative, +1 = positive
        return round(random.uniform(-1, 1), 2)

    def update_sentiment_window(self):
        new_sentiment = self.simulate_news_sentiment()
        self.sentiment_window.append(new_sentiment)
        if len(self.sentiment_window) > 20:
            self.sentiment_window.pop(0)

    def compute_meta_sentiment(self):
        self.update_sentiment_window()

        if not self.sentiment_window:
            return 0, 0

        average_sentiment = sum(self.sentiment_window) / len(self.sentiment_window)
        sentiment_variance = max(self.sentiment_window) - min(self.sentiment_window)

        print(f"📰 Meta-Sentiment → Avg: {average_sentiment:.2f} | Spread: {sentiment_variance:.2f}")

        return round(average_sentiment, 3), round(sentiment_variance, 3)
