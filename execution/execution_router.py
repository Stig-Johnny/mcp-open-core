# MCP Phase 19 — Execution Router w/ Quant Scaling Engine

from exchange_connector.binance_connector import BinanceConnector
from risk_management.capital_manager import CapitalManager
from risk_management.rebalancer import AutoRebalancer
from risk_management.scaling_engine import ScalingEngine

class ExecutionRouter:
    def __init__(self, api_key, api_secret, test_mode=True, total_capital=100000):
        self.connector = BinanceConnector(api_key, api_secret, test_mode)
        self.capital_manager = CapitalManager(total_capital)
        self.rebalancer = AutoRebalancer(total_capital)
        self.scaling_engine = ScalingEngine(base_position=1.0, scaling_curve="quadratic")

    def translate_and_execute(self, signals):
        actions = []

        price_btc = float(self.connector.get_price("BTCUSDT")['price'])
        price_eth = float(self.connector.get_price("ETHUSDT")['price'])
        price_sol = float(self.connector.get_price("SOLUSDT")['price'])
        price_aave = float(self.connector.get_price("AAVEUSDT")['price'])

        if signals.get("sentiment", 0) > 1.0:
            raw_qty = self.capital_manager.calculate_order_size("BTCUSDT", price_btc)
            scaled_qty = self.scaling_engine.compute_scaled_position(signals.get("sentiment", 0)) * raw_qty
            actions.append({"symbol": "BTCUSDT", "side": "BUY", "qty": scaled_qty})

        if signals.get("liquidity", 0) > 1.0:
            raw_qty = self.capital_manager.calculate_order_size("ETHUSDT", price_eth)
            scaled_qty = self.scaling_engine.compute_scaled_position(signals.get("liquidity", 0)) * raw_qty
            actions.append({"symbol": "ETHUSDT", "side": "BUY", "qty": scaled_qty})

        if signals.get("whales", 0) > 2.0:
            raw_qty = self.capital_manager.calculate_order_size("SOLUSDT", price_sol)
            scaled_qty = self.scaling_engine.compute_scaled_position(signals.get("whales", 0)) * raw_qty
            actions.append({"symbol": "SOLUSDT", "side": "BUY", "qty": scaled_qty})

        if signals.get("sectors", {}).get("DeFi", 0) > 1.0:
            raw_qty = self.capital_manager.calculate_order_size("AAVEUSDT", price_aave)
            scaled_qty = self.scaling_engine.compute_scaled_position(signals["sectors"]["DeFi"]) * raw_qty
            actions.append({"symbol": "AAVEUSDT", "side": "BUY", "qty": scaled_qty})

        if not actions:
            print("🚫 No execution signals triggered.")
        else:
            for action in actions:
                result = self.connector.place_order(
                    action["symbol"], 
                    action["side"], 
                    action["qty"]
                )
                print(f"🟢 Executed: {action['symbol']} {action['side']} {action['qty']}")
                print(result)

        # Auto Rebalancing Section
        print("🔄 Checking Rebalancing Needs...")

        simulated_holdings = {
            "BTCUSDT": price_btc * 0.8,
            "ETHUSDT": price_eth * 1.2,
            "SOLUSDT": price_sol * 0.5,
            "AAVEUSDT": price_aave * 1.0
        }

        for symbol, usd_value in simulated_holdings.items():
            if self.rebalancer.needs_rebalancing(symbol, usd_value):
                qty = self.rebalancer.calculate_rebalance_amount(symbol, usd_value, eval(f"price_{symbol[:-4].lower()}"))
                action = "BUY" if qty > 0 else "SELL"
                qty = abs(qty)
                rebalance_result = self.connector.place_order(symbol, action, qty)
                print(f"⚖ Rebalanced {symbol} {action} {qty}")
                print(rebalance_result)
            else:
                print(f"✅ {symbol} within balance range")
