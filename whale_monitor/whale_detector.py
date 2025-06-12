# whale_monitor/whale_detector.py

"""
MCP Open Core - Whale Monitor
Initial placeholder to scan whale events.
"""

class WhaleDetector:
    def __init__(self):
        pass

    def detect_large_movements(self, transactions):
        whales = [tx for tx in transactions if tx['amount'] > 100]
        print(f"Detected {len(whales)} whale transactions.")
        return whales

if __name__ == "__main__":
    wd = WhaleDetector()
    sample = [
        {"tx": "0x1", "amount": 50},
        {"tx": "0x2", "amount": 500},
        {"tx": "0x3", "amount": 10}
    ]
    wd.detect_large_movements(sample)
