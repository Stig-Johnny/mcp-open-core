# ARCHIVED: This file has been moved to /archive/ and is not part of the active MCP core system.

# whale_monitor/whale_detector.py

import requests
import os

class WhaleDetector:
    def __init__(self, api_key):
        self.api_url = "https://api.whale-alert.io/v1/transactions"
        self.api_key = api_key

    def fetch_whale_data(self, currency="btc", min_value=500000):
        params = {
            "api_key": self.api_key,
            "currency": currency,
            "min_value": min_value,
            "limit": 10
        }
        response = requests.get(self.api_url, params=params)
        data = response.json()
        return data

if __name__ == "__main__":
    # Use environment variable for Whale API Key
    WHALE_API_KEY = os.getenv("WHALE_API_KEY")
    if not WHALE_API_KEY:
        print("[WhaleDetector] ERROR: Please set WHALE_API_KEY as an environment variable.")
        exit(1)

    wd = WhaleDetector(WHALE_API_KEY)
    print(wd.fetch_whale_data())
