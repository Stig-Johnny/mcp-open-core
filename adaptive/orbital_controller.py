# MCP Phase 55 — Orbital Controller v1.0

import json
import random
import os

class OrbitalController:
    def __init__(self):
        self.weight_file = "adaptive/weights.json"
        self.weights = {
            "sentiment": 1.0,
            "liquidity": 1.0,
            "whales": 1.0,
            "sectors": 1.0
        }

    def update_adaptive_weights(self):
        # Simulated adaptive logic (placeholder for actual reinforcement learning loop)
        self.weights["sentiment"] += round(random.uniform(-0.05, 0.05), 3)
        self.weights["liquidity"] += round(random.uniform(-0.05, 0.05), 3)
        self.weights["whales"] += round(random.uniform(-0.05, 0.05), 3)
        self.weights["sectors"] += round(random.uniform(-0.05, 0.05), 3)

        # Clamp weights between 0.5 and 2.0 to prevent runaway bias
        for key in self.weights:
            self.weights[key] = min(max(self.weights[key], 0.5), 2.0)

        print(f"🛰 Adaptive Weights Updated: {self.weights}")
        self.save_weights()

    def save_weights(self):
        os.makedirs(os.path.dirname(self.weight_file), exist_ok=True)
        with open(self.weight_file, "w") as f:
            json.dump(self.weights, f, indent=4)
