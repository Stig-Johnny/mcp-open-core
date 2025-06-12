# MCP Phase 72 — Fusion Node v1.0

class FusionNode:
    def __init__(self, calibration_engine):
        self.calibration_engine = calibration_engine

    def compute_fusion_score(self, signals):
        # Weighted scoring model (sovereign-grade)
        score = (
            signals["sentiment"] * 1.0
            + signals["liquidity"] * 1.2
            + signals["whales"] * 1.3
            + signals["macro_bias"] * 1.0
            + signals["sector_bias"] * 1.0
            + (1 if signals["narrative_acceleration"] == "STRONG ACCELERATION" else 0.5 if signals["narrative_acceleration"] == "BUILDING MOMENTUM" else 0)
            + (1 if signals["liquidity_shock"] == "LIQUIDITY DRAIN WARNING" else 0)
            + (1 if signals["whale_cluster"] == "AGGRESSIVE ACCUMULATION" else -1 if signals["whale_cluster"] == "AGGRESSIVE DISTRIBUTION" else 0)
            + signals["meta_sentiment"] * 1.0
            - signals["meta_sentiment_spread"] * 0.7
            - (0.5 if signals["sentinel_spike"] == "HIGH SPIKE RISK" else 0)
        )

        # Apply sovereign calibration before returning final score
        final_score = self.calibration_engine.apply_calibration(score)

        print(f"🧬 Fusion Node Output: {final_score}")
        return final_score
