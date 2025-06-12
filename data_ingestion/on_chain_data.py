# data_ingestion/on_chain_data.py

"""
MCP Open Core - On-Chain Data Ingestion Module
Fetches whale transactions by scraping whale-alert.io (public, rate-limited, for prototyping).
"""

import requests
from bs4 import BeautifulSoup

class OnChainDataIngestor:
    def __init__(self, url="https://whale-alert.io/"):
        self.url = url

    def fetch_whale_transactions(self, limit=5):
        try:
            response = requests.get(self.url, timeout=10)
            if response.status_code != 200:
                print(f"[OnChainDataIngestor] HTTP error: {response.status_code}")
                return []
            soup = BeautifulSoup(response.text, "html.parser")
            txs = []
            for row in soup.select(".table tbody tr")[:limit]:
                cols = row.find_all("td")
                if len(cols) >= 5:
                    tx = {
                        "time": cols[0].get_text(strip=True),
                        "amount": cols[1].get_text(strip=True),
                        "symbol": cols[2].get_text(strip=True),
                        "from": cols[3].get_text(strip=True),
                        "to": cols[4].get_text(strip=True)
                    }
                    txs.append(tx)
            return txs
        except Exception as e:
            print(f"[OnChainDataIngestor] Scrape error: {e}")
            return []

if __name__ == "__main__":
    oc = OnChainDataIngestor()
    print(oc.fetch_whale_transactions())
