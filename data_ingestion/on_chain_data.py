# data_ingestion/on_chain_data.py

"""
MCP Open Core - On-Chain Data Ingestion Module
Captures basic whale flows & chain metrics.
"""

class OnChainDataIngestor:
    def __init__(self):
        pass

    def fetch_whale_transactions(self):
        # Placeholder for API to Whale Alert or similar
        print("Fetching recent whale transactions...")
        return [
            {"tx": "0xabc123", "amount": 500, "symbol": "BTC"},
            {"tx": "0xdef456", "amount": 2000, "symbol": "ETH"}
        ]

if __name__ == "__main__":
    oc = OnChainDataIngestor()
    print(oc.fetch_whale_transactions())
