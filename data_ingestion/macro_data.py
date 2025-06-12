# data_ingestion/macro_data.py

import requests

class LiquidityFetcher:
    def __init__(self):
        self.api_url = "https://api.coingecko.com/api/v3/global"

    def fetch_stablecoin_data(self):
        response = requests.get(self.api_url)
        data = response.json()
        total_stablecoins = data['data']['total_stablecoin_market_cap']
        return total_stablecoins

if __name__ == "__main__":
    lf = LiquidityFetcher()
    print(lf.fetch_stablecoin_data())
