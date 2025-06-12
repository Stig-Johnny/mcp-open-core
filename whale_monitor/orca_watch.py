# MCP Phase 38 — ORCA-WATCH Whale Cluster Engine v2.0

import random

class OrcaWatchCluster:
    def __init__(self):
        self.cluster_window = []

    def simulate_whale_movement(self):
        return round(random.uniform(-3000, 3000), 2)

    def update_cluster_window(self):
        new_value = self.simulate_whale_movement()
        self.cluster_window.append(new_value)
        if len(self.cluster_window) > 50:
            self.cluster_window.pop(0)

    def compute_whale_cluster_signal(self):
        self.update_cluster_window()

        if not self.cluster_window:
            return "NEUTRAL"

        total_flow = sum(self.cluster_window)
        avg_flow = total_flow / len(self.cluster_window)

        if avg_flow > 1500:
            signal = "AGGRESSIVE ACCUMULATION"
        elif avg_flow > 500:
            signal = "SOFT ACCUMULATION"
        elif avg_flow < -1500:
            signal = "AGGRESSIVE DISTRIBUTION"
        elif avg_flow < -500:
            signal = "SOFT DISTRIBUTION"
        else:
            signal = "NEUTRAL FLOW"

        print(f"🐋 Orca-Watch Cluster → Avg Flow: {avg_flow:.2f} BTC | Signal: {signal}")
        return signal
