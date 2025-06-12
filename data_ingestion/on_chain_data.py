# data_ingestion/on_chain_data.py

"""
MCP Open Core - On-Chain Data Ingestion Module
Captures basic whale flows & chain metrics for live fusion pipeline.
"""

import requests

class OnChainDataIngestor:
    def __init__(self, api_url="https://api.whale-alert.io/v1/transactions", api_key=None):
        self.api_url = api_url
        self.api_key = api_key  # Set your Whale Alert API key here or via env

    def fetch_whale_transactions(self, min_value=500000, limit=10):
        # Example using Whale Alert public API (replace with real key and error handling)
        params = {
            "api_key": self.api_key or "YOUR_API_KEY",
            "min_value": min_value,
            "limit": limit
        }
        try:
            response = requests.get(self.api_url, params=params, timeout=10)
            if response.status_code == 200:
                data = response.json()
                return data.get("transactions", [])
            else:
                return []
        except Exception as e:
            print(f"[OnChainDataIngestor] Error: {e}")
            return []

if __name__ == "__main__":
    oc = OnChainDataIngestor(api_key="demo")
    print(oc.fetch_whale_transactions())
