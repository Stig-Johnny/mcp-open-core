# MCP Phase 58 — Self-Learning Engine v1.0

# ARCHIVED: This file has been moved to /archive/self_learning.py and is not used by the main system.

import json
import os
import random

class SelfLearningEngine:
    def __init__(self):
        self.learning_file = "adaptive/self_learning_log.json"
        self.log_data = self.load_log()

    def load_log(self):
        if os.path.exists(self.learning_file):
            with open(self.learning_file, "r") as f:
                return json.load(f)
        else:
            return []

    def log_cycle(self, signals, decisions, pnl_result):
        log_entry = {
            "signals": signals,
            "decisions": decisions,
            "pnl": pnl_result
        }
        self.log_data.append(log_entry)
        self.save_log()

    def save_log(self):
        os.makedirs(os.path.dirname(self.learning_file), exist_ok=True)
        with open(self.learning_file, "w") as f:
            json.dump(self.log_data, f, indent=4)

    def compute_bias_adjustments(self):
        if not self.log_data:
            return 0.0

        pnl_list = [entry["pnl"] for entry in self.log_data[-30:]]
        average_pnl = sum(pnl_list) / len(pnl_list)

        bias_adjustment = round(average_pnl / 100, 3)
        print(f"🧠 Self-Learning Bias Adjustment Computed: {bias_adjustment}")
        return bias_adjustment
