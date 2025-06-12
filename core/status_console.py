# MCP Phase 79 — Sovereign Quantum Status Control Console v1.0

class StatusConsole:
    def __init__(self, calibration_engine, reinforcement_model, fusion_node, decision_engine):
        self.calibration_engine = calibration_engine
        self.reinforcement_model = reinforcement_model
        self.fusion_node = fusion_node
        self.decision_engine = decision_engine

    def print_status_report(self, signals):
        print("\n🔬 MCP Sovereign Quantum Status Console — Live Report")

        print(f"🌐 Sovereign Sensitivity Bias → {self.calibration_engine.global_sensitivity_bias}")
        print(f"🧠 Reinforcement Bias → {self.reinforcement_model.bias_adjustment}")

        raw_fusion_score = (
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

        calibrated_score = self.calibration_engine.apply_calibration(raw_fusion_score)
        final_score = self.reinforcement_model.apply_bias(calibrated_score)
        posture = self.decision_engine.determine_posture(final_score, kill_switch_flag=False)

        print(f"🧮 Raw Fusion Score → {raw_fusion_score}")
        print(f"🎯 Final Fusion Score (calibrated & reinforced) → {final_score}")
        print(f"🚦 Fusion Posture Decision → {posture}")
        print("✅ MCP Sovereign Status Verified.\n")
