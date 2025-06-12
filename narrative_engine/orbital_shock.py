# MCP Phase 37 — Orbital Sentiment Shock Engine v1.0

import random

class OrbitalShockEngine:
    def __init__(self):
        self.shock_window = []

    def simulate_sentiment_cluster(self):
        return round(random.uniform(-1, 1), 2)

    def update_cluster_window(self):
        new_value = self.simulate_sentiment_cluster()
        self.shock_window.append(new_value)
        if len(self.shock_window) > 30:
            self.shock_window.pop(0)

    def compute_shock_signal(self):
        self.update_cluster_window()

        if not self.shock_window:
            return "NEUTRAL"

        max_val = max(self.shock_window)
        min_val = min(self.shock_window)
        spread = max_val - min_val

        # Shock Trigger Logic
        if spread >= 1.8:
            signal = "HIGH SHOCK WARNING"
        elif spread >= 1.2:
            signal = "ELEVATED SHOCK RISK"
        else:
            signal = "STABLE BAND"

        print(f"🌪 Orbital Shock → Spread: {spread:.2f} | Signal: {signal}")
        return signal
