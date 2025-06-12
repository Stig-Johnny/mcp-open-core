# MCP Phase 17 — Sovereign Auto-Rebalancing Engine

class AutoRebalancer:
    def __init__(self, total_capital_usd=100000):
        self.total_capital = total_capital_usd
        self.target_allocations = {
            "BTCUSDT": 0.25,
            "ETHUSDT": 0.25,
            "SOLUSDT": 0.20,
            "AAVEUSDT": 0.10,
            "Other": 0.20
        }
        self.rebalance_threshold = 0.03  # Allow 3% deviation before rebalancing

    def calculate_target_usd(self, symbol):
        return self.total_capital * self.target_allocations.get(symbol, self.target_allocations["Other"])

    def needs_rebalancing(self, symbol, current_usd_value):
        target_usd = self.calculate_target_usd(symbol)
        deviation = abs(current_usd_value - target_usd) / target_usd
        return deviation > self.rebalance_threshold

    def calculate_rebalance_amount(self, symbol, current_usd_value, price):
        target_usd = self.calculate_target_usd(symbol)
        usd_diff = target_usd - current_usd_value
        qty = usd_diff / price
        return round(qty, 6)
