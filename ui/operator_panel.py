# ARCHIVED: This file has been moved to /archive/ and is not part of the active MCP core system.

# MCP Phase 82 — Sovereign Operator Panel (Alpha UI Module)

import tkinter as tk
import requests
import threading

API_URL = "http://localhost:5005"

class MCPPanel:
    def __init__(self, root):
        self.root = root
        self.root.title("MCP Sovereign Operator Panel")

        self.status_label = tk.Label(root, text="System Status: Loading...", font=("Arial", 14))
        self.status_label.pack(pady=10)

        self.score_label = tk.Label(root, text="", font=("Arial", 12))
        self.score_label.pack(pady=5)

        self.reinforcement_label = tk.Label(root, text="", font=("Arial", 12))
        self.reinforcement_label.pack(pady=5)

        self.calibration_label = tk.Label(root, text="", font=("Arial", 12))
        self.calibration_label.pack(pady=5)

        self.posture_label = tk.Label(root, text="", font=("Arial", 12))
        self.posture_label.pack(pady=5)

        self.refresh_button = tk.Button(root, text="Refresh Status", command=self.update_status)
        self.refresh_button.pack(pady=10)

        self.increase_button = tk.Button(root, text="➕ Increase Sensitivity", command=lambda: self.adjust_calibration(0.1))
        self.increase_button.pack(pady=5)

        self.decrease_button = tk.Button(root, text="➖ Decrease Sensitivity", command=lambda: self.adjust_calibration(-0.1))
        self.decrease_button.pack(pady=5)

        self.update_status()

    def update_status(self):
        self.status_label.config(text="System Status: Refreshing...")

        def fetch_data():
            try:
                signals = self.generate_fake_signals()  # Simplified signals for demo
                res = requests.post(f"{API_URL}/fusion_score", json=signals).json()

                self.score_label.config(text=f"Fusion Score: {res['fusion_score']}")
                self.reinforcement_label.config(text=f"Reinforcement Bias: {res['reinforcement_bias']}")
                self.calibration_label.config(text=f"Calibration Bias: {res['calibration_bias']}")
                self.posture_label.config(text=f"Posture: {res['posture']}")

                self.status_label.config(text="System Status: Operational")

            except Exception as e:
                self.status_label.config(text=f"System Error: {e}")

        threading.Thread(target=fetch_data).start()

    def adjust_calibration(self, adjustment):
        try:
            requests.post(f"{API_URL}/adjust_calibration", json={"adjustment": adjustment})
            self.update_status()
        except Exception as e:
            self.status_label.config(text=f"Calibration Error: {e}")

    def generate_fake_signals(self):
        import random
        signals = {
            "sentiment": round(random.uniform(-1, 1), 3),
            "liquidity": round(random.uniform(-1, 1), 3),
            "whales": round(random.uniform(-200, 200), 3),
            "macro_bias": random.choice([-1, 0, 1]),
            "sector_bias": random.choice([-1, 0, 1]),
            "narrative_acceleration": random.choice(["NONE", "BUILDING MOMENTUM", "STRONG ACCELERATION"]),
            "liquidity_shock": random.choice(["NONE", "LIQUIDITY DRAIN WARNING"]),
            "whale_cluster": random.choice(["NEUTRAL CLUSTER BALANCE", "AGGRESSIVE ACCUMULATION", "AGGRESSIVE DISTRIBUTION"]),
            "meta_sentiment": round(random.uniform(-1, 1), 3),
            "meta_sentiment_spread": round(random.uniform(0, 2), 3),
            "sentinel_spike": random.choice(["NORMAL", "HIGH SPIKE RISK"])
        }
        return signals

if __name__ == "__main__":
    root = tk.Tk()
    app = MCPPanel(root)
    root.mainloop()
