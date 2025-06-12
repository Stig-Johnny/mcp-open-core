# MCP Phase 21 — Orbital Autonomous Quant Governance Module

import os
import json

class OrbitalController:
    def __init__(self, learning_log="adaptive/learning_log.json", weights_file="adaptive/weights.json"):
        self.learning_log = learning_log
        self.weights_file = weights_file

    def load_learning_data(self):
        if not os.path.exists(self.learning_log):
            return []
        with open(self.learning_log, "r") as f:
            return json.load(f)

    def compute_dynamic_weights(self):
        data = self.load_learning_data()

        if not data:
            return None

        sentiment_scores = []
        liquidity_scores = []
        whale_scores = []
        sector_scores = []

        for entry in data:
            pnl = entry["pnl"]
            signals = entry["signals"]

            sentiment_scores.append(signals.get("sentiment", 0) * pnl)
            liquidity_scores.append(signals.get("liquidity", 0) * pnl)
            whale_scores.append(signals.get("whales", 0) * pnl)
            sector_scores.append(signals.get("sectors", {}).get("DeFi", 0) * pnl)

        sentiment_weight = 1.0 + sum(sentiment_scores) / len(sentiment_scores)
        liquidity_weight = 1.0 + sum(liquidity_scores) / len(liquidity_scores)
        whale_weight = 1.0 + sum(whale_scores) / len(whale_scores)
        sector_weight = 1.0 + sum(sector_scores) / len(sector_scores)

        updated_weights = {
            "sentiment": round(sentiment_weight, 3),
            "liquidity": round(liquidity_weight, 3),
            "whales": round(whale_weight, 3),
            "sectors": round(sector_weight, 3)
        }

        return updated_weights

    def update_adaptive_weights(self):
        updated_weights = self.compute_dynamic_weights()
        if updated_weights:
            with open(self.weights_file, "w") as f:
                json.dump(updated_weights, f, indent=2)
            print(f"🔧 Updated Adaptive Weights: {updated_weights}")
        else:
            print("⚠ No learning data yet to update weights.")
