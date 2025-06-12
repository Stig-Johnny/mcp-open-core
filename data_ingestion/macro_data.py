# ARCHIVED: This file has been moved to /archive/ and is not part of the active MCP core system.

# data_ingestion/macro_data.py

import requests

class LiquidityFetcher:
    def __init__(self):
        self.api_url = "https://api.coingecko.com/api/v3/global"

    def fetch_stablecoin_data(self):
        response = requests.get(self.api_url)
        data = response.json()
        # Defensive: handle missing or changed keys
        total_stablecoins = 0
        try:
            if 'data' in data:
                total_stablecoins = data['data'].get('total_stablecoin_market_cap')
                if total_stablecoins is None:
                    total_stablecoins = data['data'].get('total_market_cap', 0)
        except Exception as e:
            print(f"[LiquidityFetcher] API response error: {e}")
            total_stablecoins = 0
        return total_stablecoins

if __name__ == "__main__":
    lf = LiquidityFetcher()
    print(lf.fetch_stablecoin_data())
