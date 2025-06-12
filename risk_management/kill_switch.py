# MCP Phase 27 — KILL SWITCH v2.0 — Multi-Layer Capital Preservation System

class KillSwitch:
    def __init__(self):
        # New thresholds introduced
        self.liquidity_threshold = -0.03
        self.whale_threshold = -1000
        self.volatility_threshold = 0.6
        self.corridor_threshold = -0.04

    def evaluate_risk(self, signals, liquidity_netflow, whale_netflow):
        """
        Master kill switch evaluation logic across layers
        """
        triggered_flags = []

        # Traditional whale/liquidity triggers
        if liquidity_netflow < self.liquidity_threshold:
            triggered_flags.append("LIQUIDITY DRAIN")

        if whale_netflow < self.whale_threshold:
            triggered_flags.append("WHALE NET SELL")

        # New volatility trigger
        if signals["volatility"] > self.volatility_threshold:
            triggered_flags.append("VOLATILITY SHOCK")

        # New liquidity corridor compression
        if signals["corridor"] < self.corridor_threshold:
            triggered_flags.append("CORRIDOR CONTRACTION")

        kill_switch_triggered = len(triggered_flags) > 0
        return kill_switch_triggered, triggered_flags
