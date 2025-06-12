# liquidity_model/liquidity_core.py

"""
MCP Open Core - Liquidity Model
Simple scaffold for stablecoin expansion modeling.
"""

class LiquidityModel:
    def __init__(self):
        pass

    def check_liquidity_inflow(self, stablecoin_supply_today, stablecoin_supply_yesterday):
        delta = stablecoin_supply_today - stablecoin_supply_yesterday
        print(f"Liquidity delta: {delta}")
        return delta

if __name__ == "__main__":
    lm = LiquidityModel()
    lm.check_liquidity_inflow(105000000, 100000000)
