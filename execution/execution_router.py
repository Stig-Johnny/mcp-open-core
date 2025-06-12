# MCP Phase 16 — Execution Router w/ Capital Management

from exchange_connector.binance_connector import BinanceConnector
from risk_management.capital_manager import CapitalManager

class ExecutionRouter:
    def __init__(self, api_key, api_secret, test_mode=True, total_capital=100000):
        self.connector = BinanceConnector(api_key, api_secret, test_mode)
        self.capital_manager = CapitalManager(total_capital)

    def translate_and_execute(self, signals):
        actions = []

        price_btc = float(self.connector.get_price("BTCUSDT")['price'])
        price_eth = float(self.connector.get_price("ETHUSDT")['price'])
        price_sol = float(self.connector.get_price("SOLUSDT")['price'])
        price_aave = float(self.connector.get_price("AAVEUSDT")['price'])

        if signals.get("sentiment", 0) > 1.0:
            qty = self.capital_manager.calculate_order_size("BTCUSDT", price_btc)
            actions.append({"symbol": "BTCUSDT", "side": "BUY", "qty": qty})

        if signals.get("liquidity", 0) > 1.0:
            qty = self.capital_manager.calculate_order_size("ETHUSDT", price_eth)
            actions.append({"symbol": "ETHUSDT", "side": "BUY", "qty": qty})

        if signals.get("whales", 0) > 2.0:
            qty = self.capital_manager.calculate_order_size("SOLUSDT", price_sol)
            actions.append({"symbol": "SOLUSDT", "side": "BUY", "qty": qty})

        if signals.get("sectors", {}).get("DeFi", 0) > 1.0:
            qty = self.capital_manager.calculate_order_size("AAVEUSDT", price_aave)
            actions.append({"symbol": "AAVEUSDT", "side": "BUY", "qty": qty})

        if not actions:
            print("🚫 No execution signals triggered.")
            return

        for action in actions:
            result = self.connector.place_order(
                action["symbol"], 
                action["side"], 
                action["qty"]
            )
            print(f"🟢 Executed: {action['symbol']} {action['side']} {action['qty']}")
            print(result)
