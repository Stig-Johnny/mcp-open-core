# data_ingestion/on_chain_data.py

"""
MCP Open Core - On-Chain Data Ingestion Module
Fetches whale transactions from whale-alert.io/data.json and parses CSV-like alert strings.
"""

import requests
import csv
import io

class OnChainDataIngestor:
    def __init__(self, url="https://whale-alert.io/data.json?alerts=9&prices=BTC&hodl=bitcoin%2CBTC&potential_profit=bitcoin%2CBTC&average_buy_price=bitcoin%2CBTC&realized_profit=bitcoin%2CBTC&volume=bitcoin%2CBTC&news=true"):
        self.url = url

    def fetch_whale_transactions(self, limit=5):
        try:
            response = requests.get(self.url, timeout=10)
            if response.status_code != 200:
                print(f"[OnChainDataIngestor] HTTP error: {response.status_code}")
                return []
            data = response.json()
            alerts = data.get("alerts", [])
            txs = []
            for alert_str in alerts[:limit]:
                # Parse CSV-like string
                reader = csv.reader(io.StringIO(alert_str))
                fields = next(reader)
                if len(fields) >= 6:
                    tx = {
                        "timestamp": fields[0],
                        "emoji": fields[1],
                        "amount": fields[2],
                        "usd_value": fields[3],
                        "description": fields[4],
                        "link": fields[5],
                        "source": "whale-alert.io"
                    }
                    txs.append(tx)
            return txs
        except Exception as e:
            print(f"[OnChainDataIngestor] JSON parse error: {e}")
            return []

if __name__ == "__main__":
    oc = OnChainDataIngestor()
    print(oc.fetch_whale_transactions())
