# MCP Phase 30 — Quantum Node v1.0 — Signal Fusion Engine

class QuantumNodeFusion:
    def __init__(self):
        # Assign initial signal weights
        self.weights = {
            "sentiment": 1.0,
            "liquidity": 1.0,
            "whales": 1.0,
            "sectors": 1.0,
            "volatility": -1.0,  # higher vol = risk-off
            "corridor": 1.0,
            "sentiment_delta": 1.0
        }

    def compute_fusion_score(self, signals):
        fusion_score = 0.0
        for key, weight in self.weights.items():
            signal_value = signals.get(key, 0)
            if isinstance(signal_value, dict):  # For sector dict, take average
                signal_value = sum(signal_value.values()) / len(signal_value)
            fusion_score += signal_value * weight
        fusion_score = round(fusion_score, 3)

        print(f"🧮 Quantum Fusion Score: {fusion_score}")
        return fusion_score
