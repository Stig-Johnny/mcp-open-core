# whale_monitor/whale_detector.py

import requests

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
    # Put your Whale Alert API key here
    WD_API_KEY = "INSERT_YOUR_API_KEY"
    wd = WhaleDetector(WD_API_KEY)
    print(wd.fetch_whale_data())
