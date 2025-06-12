# MCP Phase 41 — Quantum Node Fusion Score v1.0 (Weighted Model)

class QuantumNodeFusion:
    def __init__(self):
        # Default adaptive weights (can be adjusted live)
        self.weights = {
            "sentiment": 1.0,
            "liquidity": 1.2,
            "whales": 1.4,
            "sector_bias": 1.3,
            "volatility": 0.8,
            "narrative_acceleration": 1.5,
            "meta_sentiment_spread": 1.1
        }

    def compute_fusion_score(self, signals):
        score = 0

        score += self.weights["sentiment"] * signals.get("sentiment", 0)
        score += self.weights["liquidity"] * signals.get("liquidity", 0)
        score += self.weights["whales"] * signals.get("whales", 0)
        score += self.weights["sector_bias"] * signals.get("sector_bias", 0)
        score += self.weights["volatility"] * (-signals.get("volatility", 0))  # inverse weighting to volatility
        score += self.weights["narrative_acceleration"] * (1 if signals.get("narrative_acceleration") == "STRONG ACCELERATION" else 0)
        score += self.weights["meta_sentiment_spread"] * (-signals.get("meta_sentiment_spread", 0))

        print(f"⚛ Fusion Score (Weighted): {score:.2f}")
        return score
