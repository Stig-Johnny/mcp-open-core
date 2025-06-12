# MCP Phase 67 — Narrative Parser Engine v1.0

import random

class NarrativeParser:
    def __init__(self):
        # Placeholder sentiment keyword dictionary (expandable)
        self.sentiment_map = {
            "bullish": 1,
            "breakout": 1,
            "uptrend": 1,
            "record high": 1,
            "explosion": 1,
            "bearish": -1,
            "collapse": -1,
            "crash": -1,
            "scam": -1,
            "lawsuit": -1
        }

    def parse_news(self, headline):
        score = 0
        lower_headline = headline.lower()

        for keyword, weight in self.sentiment_map.items():
            if keyword in lower_headline:
                score += weight

        # Add minor random market noise to simulate non-binary news impact
        score += round(random.uniform(-0.3, 0.3), 2)

        print(f"📰 Parsed Headline: \"{headline}\" → Sentiment Score: {score}")
        return score
