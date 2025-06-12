# data_ingestion/market_data.py

import requests

class MarketDataIngestor:
    def __init__(self, base_url="https://api.binance.com"):
        self.base_url = base_url

    def fetch_price(self, symbol="BTCUSDT"):
        endpoint = f"/api/v3/ticker/24hr?symbol={symbol}"
        url = self.base_url + endpoint
        response = requests.get(url)
        data = response.json()
        return {
            "symbol": symbol,
            "price": float(data["lastPrice"]),
            "volume": float(data["volume"])
        }

if __name__ == "__main__":
    md = MarketDataIngestor()
    print(md.fetch_price("BTCUSDT"))
