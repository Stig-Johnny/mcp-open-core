# MCP Phase 16 — Sovereign Capital Manager

class CapitalManager:
    def __init__(self, total_capital_usd=100000):
        self.total_capital = total_capital_usd
        self.asset_allocations = {
            "BTCUSDT": 0.25,
            "ETHUSDT": 0.25,
            "SOLUSDT": 0.20,
            "AAVEUSDT": 0.10,
            "Other": 0.20
        }
        self.reserve_buffer = 0.10  # Always keep 10% cash buffer

    def calculate_order_size(self, symbol, price):
        allocation = self.asset_allocations.get(symbol, self.asset_allocations["Other"])
        allocated_capital = self.total_capital * allocation * (1 - self.reserve_buffer)
        qty = allocated_capital / price
        return round(qty, 6)
