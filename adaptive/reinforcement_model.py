# MCP Phase 75 — Quantum Reinforcement Model v1.0

import json
import os
import random

class ReinforcementModel:
    def __init__(self):
        self.reinforcement_file = "adaptive/reinforcement_log.json"
        self.bias_adjustment = 0.0
        self.data = self.load_data()

    def load_data(self):
        if os.path.exists(self.reinforcement_file):
            with open(self.reinforcement_file, "r") as f:
                return json.load(f)
        return []

    def log_trade_outcome(self, pnl):
        self.data.append(pnl)
        self.save_data()

    def save_data(self):
        os.makedirs(os.path.dirname(self.reinforcement_file), exist_ok=True)
        with open(self.reinforcement_file, "w") as f:
            json.dump(self.data, f, indent=4)

    def compute_bias(self):
        if not self.data:
            self.bias_adjustment = 0.0
            return self.bias_adjustment

        last_n = self.data[-50:]  # Use trailing 50 trades for adaptive learning
        avg_pnl = sum(last_n) / len(last_n)

        self.bias_adjustment = round(avg_pnl / 100.0, 4)
        print(f"🧠 Reinforcement Model — Bias Adjustment: {self.bias_adjustment}")
        return self.bias_adjustment

    def apply_bias(self, fusion_score):
        adjusted = fusion_score + self.bias_adjustment
        print(f"⚙ Fusion Reinforced Score: {adjusted}")
        return adjusted
