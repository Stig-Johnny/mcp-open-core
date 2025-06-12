# ARCHIVED: This file has been moved to /archive/ and is not part of the active MCP core system.

# data_ingestion/market_data.py

from exchange_connector.binance_connector import BinanceConnector

class MarketDataIngestor:
    def __init__(self, symbol="BTCUSDT"):
        self.symbol = symbol
        self.connector = BinanceConnector()

    def fetch_price(self, symbol=None):
        symbol = symbol or self.symbol
        data = self.connector.get_price(symbol)
        return {
            "symbol": symbol,
            "price": float(data["price"]),
        }

    def fetch_order_book(self, symbol=None, limit=5):
        symbol = symbol or self.symbol
        data = self.connector.get_order_book(symbol, limit=limit)
        return data

if __name__ == "__main__":
    md = MarketDataIngestor()
    print(md.fetch_price("BTCUSDT"))
