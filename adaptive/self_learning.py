# MCP Phase 20 — Sovereign AI Self-Learning Module

import os
import json
import datetime

class SelfLearningEngine:
    def __init__(self, learning_log="adaptive/learning_log.json"):
        self.learning_log = learning_log
        if not os.path.exists("adaptive/"):
            os.makedirs("adaptive/")
        if not os.path.exists(self.learning_log):
            with open(self.learning_log, "w") as f:
                json.dump([], f)

    def log_cycle(self, signals, decisions, pnl):
        log_entry = {
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "signals": signals,
            "decisions": decisions,
            "pnl": pnl
        }
        with open(self.learning_log, "r+") as f:
            data = json.load(f)
            data.append(log_entry)
            f.seek(0)
            json.dump(data, f, indent=2)

    def compute_bias_adjustments(self):
        with open(self.learning_log, "r") as f:
            data = json.load(f)

        if not data:
            return {}

        sentiment_gains = []
        liquidity_gains = []
        whales_gains = []
        sectors_gains = []

        for entry in data:
            pnl = entry["pnl"]
            sentiment_gains.append(pnl * entry["signals"].get("sentiment", 0))
            liquidity_gains.append(pnl * entry["signals"].get("liquidity", 0))
            whales_gains.append(pnl * entry["signals"].get("whales", 0))
            sectors_gains.append(pnl * entry["signals"].get("sectors", {}).get("DeFi", 0))

        adjustments = {
            "sentiment_bias": sum(sentiment_gains) / len(sentiment_gains),
            "liquidity_bias": sum(liquidity_gains) / len(liquidity_gains),
            "whale_bias": sum(whales_gains) / len(whales_gains),
            "sectors_bias": sum(sectors_gains) / len(sectors_gains)
        }

        return adjustments
