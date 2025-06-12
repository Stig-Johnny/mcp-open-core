# MCP Fusion Controller — Phase 20: Full AI Self-Learning Build

import os
import json
from data_ingestion.market_data import MarketDataIngestor
from data_ingestion.macro_data import LiquidityFetcher
from data_ingestion.news_parser import NewsParser
from whale_monitor.whale_detector import WhaleDetector
from liquidity_model.liquidity_core import LiquidityModel
from narrative_engine.narrative_model import NarrativeParser
from sector_rotation.rotation_engine import SectorRotationEngine
from risk_management.profit_ladder import ProfitLadder
from risk_management.kill_switch import KillSwitch
from risk_management.alpha_defense import AlphaDefenseShield
from adaptive.self_learning import SelfLearningEngine
from datastore.state_logger import StateLogger
from execution.execution_engine import ExecutionEngine
from execution.execution_router import ExecutionRouter

class FusionController:
    def __init__(self, whale_api_key=None, binance_api_key=None, binance_api_secret=None):
        self.market_data = MarketDataIngestor()
        self.liquidity_fetcher = LiquidityFetcher()
        self.news_parser = NewsParser()
        self.whale_detector = WhaleDetector(whale_api_key)
        self.narrative_parser = NarrativeParser()

        self.liquidity_model = LiquidityModel()
        self.rotation_engine = SectorRotationEngine()

        self.profit_ladder = ProfitLadder()
        self.kill_switch = KillSwitch()
        self.alpha_defense = AlphaDefenseShield()
        self.self_learning = SelfLearningEngine()

        self.logger = StateLogger()
        self.execution_engine = ExecutionEngine()
        self.execution_router = ExecutionRouter(binance_api_key, binance_api_secret, test_mode=True)
        self.adaptive_weights = self.load_adaptive_weights()

    def load_adaptive_weights(self):
        file_path = "adaptive/weights.json"
        if os.path.exists(file_path):
            with open(file_path) as f:
                weights = json.load(f)
            print(f"✅ Loaded Adaptive Weights: {weights}")
            return weights
        else:
            print("⚠ No adaptive weights found. Using defaults.")
            return {
                "sentiment": 1.0,
                "liquidity": 1.0,
                "whales": 1.0,
                "sectors": 1.0
            }

    def collect_data(self):
        print("Collecting Data...")
        market = self.market_data.fetch_price("BTCUSDT")
        stablecoins = self.liquidity_fetcher.fetch_stablecoin_data()
        news = self.news_parser.fetch_headlines()
        whales = self.whale_detector.fetch_whale_data(currency="btc", min_value=500000)

        return {
            "market": market,
            "stablecoins": stablecoins,
            "news": news,
            "whales": whales
        }

    def process_signals(self, data):
        print("Processing Signals...")
        sentiment_scores = [self.narrative_parser.parse_news(article['title']) for article in data["news"]]
        avg_sentiment = sum(sentiment_scores) / len(sentiment_scores) if sentiment_scores else 0

        liquidity_delta = self.liquidity_model.check_liquidity_inflow(data["stablecoins"], 1000000000)
        whale_count = len(data["whales"]["transactions"]) if data["whales"].get("transactions") else 0
        sector_scores = self.rotation_engine.calculate_sector_scores()

        return {
            "sentiment": avg_sentiment,
            "liquidity": liquidity_delta,
            "whales": whale_count,
            "sectors": sector_scores
        }

    def decide_actions(self, signals):
        print("Making Tactical Decisions...")
        decisions = {}

        sentiment_trigger = self.adaptive_weights["sentiment"]
        liquidity_trigger = self.adaptive_weights["liquidity"]
        whale_trigger = self.adaptive_weights["whales"]
        sector_trigger = self.adaptive_weights["sectors"]

        if signals["sentiment"] > sentiment_trigger:
            decisions["sentiment"] = "BULLISH"

        if signals["liquidity"] > liquidity_trigger:
            decisions["liquidity"] = "ACCUMULATE"

        if signals["whales"] > whale_trigger:
            decisions["whales"] = "LARGE ACCUMULATION"

        if signals["sectors"]["DeFi"] > sector_trigger:
            decisions["rotation"] = "DEPLOY TO DEFI"

        profit_targets = self.profit_ladder.evaluate_profit_targets(1000)

        return {
            "decisions": decisions,
            "profit_targets": profit_targets
        }

    def run_cycle(self):
        print("Running Sovereign Adaptive Fusion Cycle...\n")
        data = self.collect_data()
        signals = self.process_signals(data)
        actions = self.decide_actions(signals)

        print("\n--- MCP Adaptive Fusion Report ---")
        print(f"Signals: {signals}")
        print(f"Decisions: {actions['decisions']}")
        print(f"Profit Ladder: {actions['profit_targets']}")
        print("-------------------------\n")

        whale_netflow = -2000  # Simulated whale flow (replace in production)
        liquidity_netflow = data["stablecoins"]["netflow"] if isinstance(data["stablecoins"], dict) else 0

        kill_switch_triggered, kill_flags = self.alpha_defense.check_kill_switch(signals, liquidity_netflow, whale_netflow)

        if kill_switch_triggered:
            print(f"🚨 ALPHA DEFENSE TRIGGERED: {kill_flags}")
            return

        self.execution_engine.execute(signals)
        self.execution_router.translate_and_execute(signals)
        self.logger.log_cycle(data, signals, actions["decisions"])

        simulated_pnl = 100  # Replace with real realized pnl later
        self.self_learning.log_cycle(signals, actions["decisions"], simulated_pnl)
        bias = self.self_learning.compute_bias_adjustments()
        print(f"🧠 Adaptive Learning Bias Adjustment: {bias}")

if __name__ == "__main__":
    WHALE_API_KEY = "INSERT_YOUR_WHALE_ALERT_API_KEY"
    BINANCE_API_KEY = "INSERT_YOUR_BINANCE_API_KEY"
    BINANCE_API_SECRET = "INSERT_YOUR_BINANCE_API_SECRET"
    fusion = FusionController(whale_api_key=WHALE_API_KEY, binance_api_key=BINANCE_API_KEY, binance_api_secret=BINANCE_API_SECRET)
    fusion.run_cycle()
