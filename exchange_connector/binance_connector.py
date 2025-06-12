# MCP Sovereign Exchange Connector — Phase 14
# Binance Spot Trading API Connector (Production Mode)

import time
import hmac
import hashlib
import requests
import urllib.parse
import os

class BinanceConnector:
    def __init__(self, api_key=None, api_secret=None, test_mode=True):
        self.api_key = api_key or os.getenv("BINANCE_API_KEY")
        self.api_secret = api_secret or os.getenv("BINANCE_API_SECRET")
        self.test_mode = test_mode
        self.base_url = "https://api.binance.com"
        self.session = requests.Session()
        if self.api_key:
            self.session.headers.update({'X-MBX-APIKEY': self.api_key})

    def _sign(self, params):
        query_string = urllib.parse.urlencode(params)
        m = hmac.new(self.api_secret.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256)
        return m.hexdigest()

    def get_account_info(self):
        url = self.base_url + "/api/v3/account"
        timestamp = int(time.time() * 1000)
        params = {"timestamp": timestamp}
        params['signature'] = self._sign(params)
        response = self.session.get(url, params=params)
        return response.json()

    def place_order(self, symbol, side, quantity, price=None):
        url = self.base_url + "/api/v3/order/test" if self.test_mode else self.base_url + "/api/v3/order"
        timestamp = int(time.time() * 1000)
        params = {
            "symbol": symbol,
            "side": side,
            "type": "MARKET" if price is None else "LIMIT",
            "quantity": quantity,
            "timestamp": timestamp
        }
        if price:
            params["price"] = price
            params["timeInForce"] = "GTC"
        params['signature'] = self._sign(params)
        response = self.session.post(url, params=params)
        return response.json()

    def get_price(self, symbol):
        url = self.base_url + f"/api/v3/ticker/price?symbol={symbol}"
        response = self.session.get(url)
        return response.json()

    def get_order_book(self, symbol, limit=5):
        url = self.base_url + f"/api/v3/depth?symbol={symbol}&limit={limit}"
        response = self.session.get(url)
        return response.json()

if __name__ == "__main__":
    # Load from environment variables for security
    BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
    BINANCE_API_SECRET = os.getenv("BINANCE_API_SECRET")
    if not BINANCE_API_KEY or not BINANCE_API_SECRET:
        print("[BinanceConnector] ERROR: Please set BINANCE_API_KEY and BINANCE_API_SECRET as environment variables.")
        exit(1)

    client = BinanceConnector(BINANCE_API_KEY, BINANCE_API_SECRET, test_mode=True)
    print("🔎 Account Info:")
    print(client.get_account_info())

    print("🔎 BTCUSDT Price:")
    print(client.get_price("BTCUSDT"))

    # Example test order simulation (SAFE mode)
    print("🔎 Simulated Order:")
    print(client.place_order("BTCUSDT", "BUY", 0.001))

    print("🔎 Order Book:")
    print(client.get_order_book("BTCUSDT"))
