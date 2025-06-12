# MCP Phase 64 — Kill Switch Model v1.0

class KillSwitch:
    def __init__(self):
        self.liquidity_threshold = -1.5
        self.whale_netflow_threshold = -200
        self.meta_sentiment_spread_threshold = 1.75

    def evaluate_risk(self, signals, liquidity_netflow, whale_netflow):
        kill_flags = []

        if liquidity_netflow < self.liquidity_threshold:
            kill_flags.append("SEVERE LIQUIDITY DRAIN")

        if whale_netflow < self.whale_netflow_threshold:
            kill_flags.append("WHALE DISTRIBUTION CLUSTER")

        if signals.get("meta_sentiment_spread", 0) > self.meta_sentiment_spread_threshold:
            kill_flags.append("NARRATIVE POLARIZATION RISK")

        if kill_flags:
            print(f"🚨 Kill Switch Triggered: {kill_flags}")
            return True, kill_flags
        else:
            print("✅ Kill Switch: All Clear")
            return False, []
