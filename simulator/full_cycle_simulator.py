# MCP Phase 77 — Sovereign Full Cycle Simulation Harness v1.0

import random
from adaptive.reinforcement_model import ReinforcementModel
from core.calibration_engine import CalibrationEngine
from fusion.fusion_node import FusionNode
from fusion.decision_engine import DecisionEngine

class FullCycleSimulator:
    def __init__(self):
        self.calibration_engine = CalibrationEngine()
        self.reinforcement_model = ReinforcementModel()
        self.fusion_node = FusionNode(self.calibration_engine, self.reinforcement_model)
        self.decision_engine = DecisionEngine()

    def generate_fake_signals(self):
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

    def run_simulation(self, num_cycles=100):
        print("\n🧪 Starting Sovereign Full Cycle Simulation...\n")

        for cycle in range(num_cycles):
            print(f"🚀 SIMULATION CYCLE {cycle+1}")
            signals = self.generate_fake_signals()
            fusion_score = self.fusion_node.compute_fusion_score(signals)

            posture = self.decision_engine.determine_posture(
                fusion_score, kill_switch_flag=False
            )

            # Simulated profit outcome based on risk posture (placeholder)
            pnl = self.simulate_profit(posture)
            self.reinforcement_model.log_trade_outcome(pnl)
            self.reinforcement_model.compute_bias()

    def simulate_profit(self, posture):
        profit_ranges = {
            "RISK-ON MODE": (1, 4),
            "NEUTRAL MODE": (0.5, 2),
            "DEFENSIVE MODE": (-2, 1),
            "FULL KILL SWITCH": (-1, 0)
        }
        low, high = profit_ranges.get(posture, (0, 0))
        return round(random.uniform(low, high), 2)

# Entry point for standalone simulation
if __name__ == "__main__":
    simulator = FullCycleSimulator()
    simulator.run_simulation(num_cycles=100)
