# MCP Fusion Controller — Phase 25: Liquidity Corridor AI Fully Integrated

import os
import json
from data_ingestion.market_data import MarketDataIngestor
from data_ingestion.macro_data import LiquidityFetcher
from data_ingestion.news_parser import NewsParser
from whale_monitor.orca_x_engine import OrcaXWhaleForecast
from liquidity_model.liquidity_core import LiquidityModel
from liquidity_model.liquidity_pressure import LiquidityPressureCore
from liquidity_model.liquidity_corridor import LiquidityCorridorAI
from narrative_engine.narrative_model import NarrativeParser
from sector_rotation.rotation_engine import SectorRotationEngine
from risk_management.profit_ladder import ProfitLadder
from risk_management.kill_switch import KillSwitch
from risk_management.alpha_defense import AlphaDefenseShield
from risk_management.sigma_wave import SigmaWaveVolatilityEngine
from adaptive.self_learning import SelfLearningEngine
from adaptive.orbital_controller import OrbitalController
from datastore.state_logger import StateLogger
from execution.execution_engine import ExecutionEngine
from execution.execution_router import ExecutionRouter

class FusionController:
    def __init__(self, binance_api_key=None, binance_api_secret=None):
        self.market_data = MarketDataIngestor()
        self.liquidity_fetcher = LiquidityFetcher()
        self.news_parser = NewsParser()
        self.orca_x = OrcaXWhaleForecast()
        self.narrative_parser = NarrativeParser()

        self.liquidity_model = LiquidityModel()
        self.liquidity_pressure_core = LiquidityPressureCore()
        self.liquidity_corridor = LiquidityCorridorAI()
        self.sigma_wave = SigmaWaveVolatilityEngine()
        self.rotation_engine = SectorRotationEngine()

        self.profit_ladder = ProfitLadder()
        self.kill_switch = KillSwitch()
        self.alpha_defense = AlphaDefenseShield()
        self.self_learning = SelfLearningEngine()
        self.orbital_controller = OrbitalController()

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
        whale_pressure = self.orca_x.compute_whale_pressure()
        volatility_shock = self.sigma_wave.compute_volatility_shock()
        corridor_pressure, corridor_breakdown = self.liquidity_corridor.compute_corridor_pressure()

        return {
            "market": market,
            "stablecoins": stablecoins,
            "news": news,
            "whale_pressure": whale_pressure,
            "volatility_shock": volatility_shock,
            "corridor_pressure": corridor_pressure,
            "corridor_breakdown": corridor_breakdown
        }

    def process_signals(self, data):
        print("Processing Signals...")
        sentiment_scores = [self.narrative_parser.parse_news(article['title']) for article in data["news"]]
        avg_sentiment = sum(sentiment_scores) / len(sentiment_scores) if sentiment_scores else 0

        liquidity_delta = self.liquidity_model.check_liquidity_inflow(data["stablecoins"], 1000000000)
        sector_scores = self.rotation_engine.calculate_sector_scores()

        return {
            "sentiment": avg_sentiment,
            "liquidity": liquidity_delta,
            "whales": data["whale_pressure"],
            "volatility": data["volatility_shock"],
            "corridor": data["corridor_pressure"],
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

        if signals["volatility"] > 0.5:
            decisions["volatility"] = "CAUTION: HIGH VOL"

        if signals["corridor"] < -0.03:
            decisions["corridor"] = "LIQUIDITY CONTRACTING"

        profit_targets = self.profit_ladder.evaluate_profit_targets(1000)

        return {
            "decisions": decisions,
            "profit_targets": profit_targets
        }

    def run_cycle(self):
        print("Running Sovereign Adaptive Fusion Cycle...\n")
        self.orbital_controller.update_adaptive_weights()
        self.adaptive_weights = self.load_adaptive_weights()

        data = self.collect_data()
        signals = self.process_signals(data)
        actions = self.decide_actions(signals)

        print("\n--- MCP Adaptive Fusion Report ---")
        print(f"Signals: {signals}")
        print(f"Decisions: {actions['decisions']}")
        print(f"Profit Ladder: {actions['profit_targets']}")
        print("-------------------------\n")

        liquidity_pressure_score = self.liquidity_pressure_core.compute_liquidity_pressure()
        print(f"🔎 LPI-X Liquidity Score: {liquidity_pressure_score}")

        whale_netflow = data["whale_pressure"] * 1000
        liquidity_netflow = data["stablecoins"]["netflow"] if isinstance(data["stablecoins"], dict) else 0

        kill_switch_triggered, kill_flags = self.alpha_defense.check_kill_switch(signals, liquidity_netflow, whale_netflow)

        if kill_switch_triggered:
            print(f"🚨 ALPHA DEFENSE TRIGGERED: {kill_flags}")
            return

        self.execution_engine.execute(signals)
        self.execution_router.translate_and_execute(signals)
        self.logger.log_cycle(data, signals, actions["decisions"])

        simulated_pnl = 100
        self.self_learning.log_cycle(signals, actions["decisions"], simulated_pnl)
        bias = self.self_learning.compute_bias_adjustments()
        print(f"🧠 Adaptive Learning Bias Adjustment: {bias}")

if __name__ == "__main__":
    BINANCE_API_KEY = "INSERT_YOUR_BINANCE_API_KEY"
    BINANCE_API_SECRET = "INSERT_YOUR_BINANCE_API_SECRET"
    fusion = FusionController(binance_api_key=BINANCE_API_KEY, binance_api_secret=BINANCE_API_SECRET)
    fusion.run_cycle()
