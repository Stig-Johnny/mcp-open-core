# MCP Phase 42 — Auto-Weight Adaptive Learner v1.0

import json
import os
import random

class SelfLearningEngine:
    def __init__(self):
        self.history_file = "adaptive/learning_log.json"
        self.weights_file = "adaptive/weights.json"
        self.init_files()

    def init_files(self):
        if not os.path.exists(self.history_file):
            with open(self.history_file, "w") as f:
                json.dump([], f)
        if not os.path.exists(self.weights_file):
            default_weights = {
                "sentiment": 1.0,
                "liquidity": 1.2,
                "whales": 1.4,
                "sector_bias": 1.3,
                "volatility": 0.8,
                "narrative_acceleration": 1.5,
                "meta_sentiment_spread": 1.1
            }
            with open(self.weights_file, "w") as f:
                json.dump(default_weights, f)

    def log_cycle(self, signals, decisions, pnl):
        with open(self.history_file, "r") as f:
            history = json.load(f)

        history.append({
            "signals": signals,
            "decisions": decisions,
            "pnl": pnl
        })

        if len(history) > 500:
            history = history[-500:]

        with open(self.history_file, "w") as f:
            json.dump(history, f)

    def compute_bias_adjustments(self):
        with open(self.weights_file) as f:
            weights = json.load(f)

        with open(self.history_file) as f:
            history = json.load(f)

        if len(history) < 50:
            return "INSUFFICIENT DATA FOR LEARNING"

        pnl_avg = sum([x["pnl"] for x in history[-50:]]) / 50

        for factor in weights.keys():
            adjustment = random.uniform(-0.05, 0.05)
            weights[factor] += adjustment

            # Bound the weights
            weights[factor] = round(max(min(weights[factor], 2.0), 0.2), 3)

        with open(self.weights_file, "w") as f:
            json.dump(weights, f)

        return weights
