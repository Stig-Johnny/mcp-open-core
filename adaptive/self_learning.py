# MCP Phase 35 — Self-Learning Weight Engine v1.0

import json
import os
import random

class SelfLearningEngine:
    def __init__(self):
        self.history_file = "adaptive/learning_log.json"
        self.weights_file = "adaptive/weights.json"
        self.initialize_logs()

    def initialize_logs(self):
        if not os.path.exists(self.history_file):
            with open(self.history_file, "w") as f:
                json.dump([], f)

        if not os.path.exists(self.weights_file):
            weights = {
                "sentiment": 1.0,
                "liquidity": 1.0,
                "whales": 1.0,
                "sectors": 1.0
            }
            with open(self.weights_file, "w") as f:
                json.dump(weights, f)

    def log_cycle(self, signals, decisions, pnl):
        with open(self.history_file) as f:
            history = json.load(f)

        history.append({
            "signals": signals,
            "decisions": decisions,
            "pnl": pnl
        })

        with open(self.history_file, "w") as f:
            json.dump(history, f)

    def compute_bias_adjustments(self):
        try:
            with open(self.history_file) as f:
                history = json.load(f)

            # Only act if we have enough history
            if len(history) < 10:
                return "Not enough data yet"

            # Compute average pnl and basic adjustments
            total_pnl = sum(entry["pnl"] for entry in history)
            avg_pnl = total_pnl / len(history)

            # Very naive learning rule for now
            adjustment = 0.1 if avg_pnl > 0 else -0.1

            with open(self.weights_file) as f:
                weights = json.load(f)

            # Adjust sentiment and liquidity weights slightly
            weights["sentiment"] = max(0.1, weights["sentiment"] + adjustment)
            weights["liquidity"] = max(0.1, weights["liquidity"] + adjustment)

            with open(self.weights_file, "w") as f:
                json.dump(weights, f)

            return weights
        except Exception as e:
            return f"Learning Error: {e}"
