import os
import json
from data_ingestion.market_data import MarketDataIngestor
from data_ingestion.macro_data import LiquidityFetcher
from data_ingestion.news_parser import NewsParser
from whale_monitor.orca_x_engine import OrcaXWhaleForecast
from whale_monitor.orca_watch import OrcaWatchCluster
from liquidity_model.liquidity_core import LiquidityModel
from liquidity_model.liquidity_pressure import LiquidityPressureCore
from liquidity_model.liquidity_corridor import LiquidityCorridorAI
from liquidity_model.liquidity_shock import LiquidityShockEngine
from narrative_engine.narrative_model import NarrativeParser
from narrative_engine.sentiment_engine import SentimentEngine
from narrative_engine.meta_sentiment import MetaSentimentEngine
from narrative_engine.orbital_shock import OrbitalShockEngine
from narrative_engine.narrative_acceleration import NarrativeAcceleration
from sector_rotation.rotation_engine import SectorRotationEngine
from sector_rotation.sector_intelligence import SectorIntelligence
from fusion.quantum_node import FusionNode
from risk_management.profit_ladder import ProfitLadder
from risk_management.kill_switch import KillSwitch
from risk_management.alpha_defense import AlphaDefenseShield
from risk_management.sigma_wave import SigmaWaveVolatilityEngine
from risk_management.sentinel_volatility import SentinelVolatilityRadar
from risk_management.sentinel_shield import SentinelShield
from macro_engine.global_macro_feed import GlobalMacroFeed
from adaptive.self_learning import SelfLearningEngine
from adaptive.orbital_controller import OrbitalController
from datastore.state_logger import StateLogger
from execution.execution_engine import ExecutionEngine
from execution.execution_router import ExecutionRouter
from core.calibration_engine import CalibrationEngine
from adaptive.reinforcement_model import ReinforcementModel
from alerting.email_alert import send_posture_alert


class FusionController:
    def __init__(self, binance_api_key=None, binance_api_secret=None):
        self.calibration_engine = CalibrationEngine()
        self.reinforcement_model = ReinforcementModel()

        self.market_data = MarketDataIngestor()
        self.liquidity_fetcher = LiquidityFetcher()
        self.news_parser = NewsParser()
        self.orca_x = OrcaXWhaleForecast()
        self.orca_watch = OrcaWatchCluster()
        self.narrative_parser = NarrativeParser()
        self.sentiment_engine = SentimentEngine()
        self.meta_sentiment = MetaSentimentEngine()
        self.orbital_shock = OrbitalShockEngine()
        self.narrative_accel = NarrativeAcceleration()
        self.sector_intel = SectorIntelligence()

        self.liquidity_model = LiquidityModel()
        self.liquidity_pressure_core = LiquidityPressureCore()
        self.liquidity_corridor = LiquidityCorridorAI()
        self.liquidity_shock = LiquidityShockEngine()
        self.sigma_wave = SigmaWaveVolatilityEngine()
        self.rotation_engine = SectorRotationEngine()
        self.quantum_node = FusionNode(self.calibration_engine, self.reinforcement_model)
        self.sentinel = SentinelVolatilityRadar()
        self.sentinel_shield = SentinelShield()
        self.macro_feed = GlobalMacroFeed()

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
        order_book = self.market_data.fetch_order_book("BTCUSDT", limit=5)
        stablecoins = self.liquidity_fetcher.fetch_stablecoin_data()
        news = self.news_parser.fetch_headlines()
        whale_pressure = self.orca_x.compute_whale_pressure()
        whale_cluster = self.orca_watch.compute_whale_cluster_signal()
        volatility_shock = self.sigma_wave.compute_volatility_shock()
        corridor_pressure, corridor_breakdown = self.liquidity_corridor.compute_corridor_pressure()
        sentiment_delta = self.sentiment_engine.compute_sentiment_delta()
        sentinel_spike = self.sentinel.compute_spike_risk()
        liquidity_shock = self.liquidity_shock.detect_shock()
        macro_bias = self.macro_feed.compute_macro_bias()
        meta_sentiment_avg, meta_sentiment_spread = self.meta_sentiment.compute_meta_sentiment()
        orbital_shock = self.orbital_shock.compute_shock_signal()
        sector_bias = self.sector_intel.compute_sector_bias()
        narrative_acceleration = self.narrative_accel.compute_acceleration()

        return {
            "market": market,
            "order_book": order_book,
            "stablecoins": stablecoins,
            "news": news,
            "whale_pressure": whale_pressure,
            "whale_cluster": whale_cluster,
            "volatility_shock": volatility_shock,
            "corridor_pressure": corridor_pressure,
            "corridor_breakdown": corridor_breakdown,
            "sentiment_delta": sentiment_delta,
            "sentinel_spike": sentinel_spike,
            "liquidity_shock": liquidity_shock,
            "macro_bias": macro_bias,
            "meta_sentiment_avg": meta_sentiment_avg,
            "meta_sentiment_spread": meta_sentiment_spread,
            "orbital_shock": orbital_shock,
            "sector_bias": sector_bias,
            "narrative_acceleration": narrative_acceleration
        }

    def process_signals(self, data):
        print("Processing Signals...")
        sentiment_scores = [self.narrative_parser.parse_news(article['title']) for article in data["news"]]
        avg_sentiment = sum(sentiment_scores) / len(sentiment_scores) if sentiment_scores else 0

        # Extract numeric stablecoin value for liquidity calculations
        stablecoins_value = 0
        if isinstance(data["stablecoins"], (int, float)):
            stablecoins_value = data["stablecoins"]
        elif isinstance(data["stablecoins"], dict):
            # Try common keys
            for k in ["usd", "total", "market_cap", "total_stablecoin_market_cap"]:
                if k in data["stablecoins"]:
                    stablecoins_value = data["stablecoins"][k]
                    break
        liquidity_delta = self.liquidity_model.check_liquidity_inflow(stablecoins_value, 1000000000)

        # Ensure all required keys for compute_fusion_score are present
        safe_signals = {
            "sentiment": avg_sentiment,
            "liquidity": liquidity_delta,
            "whales": data["whale_pressure"],
            "whale_cluster": data["whale_cluster"],
            "volatility": data["volatility_shock"],
            "corridor": data["corridor_pressure"],
            "sentiment_delta": data["sentiment_delta"],
            "sentinel_spike": data["sentinel_spike"],
            "liquidity_shock": data["liquidity_shock"],
            "macro_bias": data["macro_bias"],
            "meta_sentiment": data.get("meta_sentiment_avg", 0),
            "meta_sentiment_spread": data.get("meta_sentiment_spread", 0),
            "orbital_shock": data["orbital_shock"],
            "sector_bias": data["sector_bias"],
            "narrative_acceleration": data["narrative_acceleration"]
        }
        return safe_signals

    def decide_actions(self, signals):
        fusion_score = self.quantum_node.compute_fusion_score(signals)
        decisions = {}
        # Track last posture (no alerting)
        last_posture = getattr(self, '_last_posture', None)
        if fusion_score > 3 and signals["macro_bias"] >= 0:
            posture = "RISK-ON MODE"
        elif fusion_score < 0 or signals["macro_bias"] < 0:
            posture = "DEFENSIVE MODE"
        else:
            posture = "NEUTRAL MONITORING"
        decisions["FUSION_BIAS"] = posture
        if last_posture != posture:
            self._last_posture = posture

        if signals["sentinel_spike"] == "HIGH SPIKE RISK":
            decisions["SENTINEL_ALERT"] = "IMMINENT MOVE DETECTED"

        if signals["liquidity_shock"] == "LIQUIDITY DRAIN WARNING":
            decisions["LIQUIDITY_SHOCK_ALERT"] = "POTENTIAL SQUEEZE EMERGING"

        if signals["meta_sentiment_spread"] > 1.5:
            decisions["NARRATIVE_VOLATILITY"] = "EXTREME POLARIZATION DETECTED"

        if signals["orbital_shock"] == "HIGH SHOCK WARNING":
            decisions["ORBITAL_SHOCK"] = "MAJOR SENTIMENT INFLECTION RISK"

        if signals["whale_cluster"] in ["AGGRESSIVE ACCUMULATION", "AGGRESSIVE DISTRIBUTION"]:
            decisions["WHALE_CLUSTER"] = signals["whale_cluster"]

        if signals["narrative_acceleration"] == "STRONG ACCELERATION":
            decisions["NARRATIVE_BREAKOUT"] = "INCOMING NARRATIVE SURGE"

        profit_targets = self.profit_ladder.evaluate_profit_targets(
            portfolio_value=1000,
            sigma_score=signals["volatility"]
        )

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

        sentinel_mode = self.sentinel_shield.evaluate_defense(signals["sentinel_spike"])
        if sentinel_mode == "DEFENSIVE_MODE":
            print("⚠ AUTO-SUSPENSION: SENTINEL-SHIELD ACTIVE. Halting aggressive entries.")
            return

        print("\n--- MCP Quantum Fusion Report ---")
        print(f"Signals: {signals}")
        print(f"Decisions: {actions['decisions']}")
        print(f"Profit Ladder: {actions['profit_targets']}")
        print("-------------------------\n")

        liquidity_pressure_score = self.liquidity_pressure_core.compute_liquidity_pressure()
        print(f"🔎 LPI-X Liquidity Score: {liquidity_pressure_score}")

        whale_netflow = data["whale_pressure"]
        liquidity_netflow = data["stablecoins"]["netflow"] if isinstance(data["stablecoins"], dict) else 0

        kill_switch_triggered, kill_flags = self.kill_switch.evaluate_risk(signals, liquidity_netflow, whale_netflow)

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
    BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
    BINANCE_API_SECRET = os.getenv("BINANCE_API_SECRET")
    if not BINANCE_API_KEY or not BINANCE_API_SECRET:
        print("[FusionController] ERROR: Please set BINANCE_API_KEY and BINANCE_API_SECRET as environment variables.")
        exit(1)
    fusion = FusionController(binance_api_key=BINANCE_API_KEY, binance_api_secret=BINANCE_API_SECRET)
    fusion.run_cycle()
