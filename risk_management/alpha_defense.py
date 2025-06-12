# MCP Phase 18 — Alpha Defense Shield (Kill Switch Logic)

class AlphaDefenseShield:
    def __init__(self):
        self.whale_exit_threshold = -3000  # BTC Net outflow threshold (example units)
        self.sentiment_collapse_threshold = -0.7
        self.stablecoin_outflow_threshold = -1_000_000_000  # $1B stablecoin exit

    def check_kill_switch(self, signals, liquidity_data, whale_netflow):
        """
        signals: MCP fusion signals
        liquidity_data: stablecoin inflow/outflow (net inflow = positive)
        whale_netflow: recent whale BTC exchange flows (positive = inflow)
        """
        kill_flags = []

        if whale_netflow < self.whale_exit_threshold:
            kill_flags.append("Whale Exit Detected")

        if signals.get("sentiment", 0) < self.sentiment_collapse_threshold:
            kill_flags.append("Sentiment Breakdown")

        if liquidity_data < self.stablecoin_outflow_threshold:
            kill_flags.append("Liquidity Drain")

        kill_switch_triggered = len(kill_flags) > 0
        return kill_switch_triggered, kill_flags
