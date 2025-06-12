# fusion/fusion_controller.py

from data_ingestion.market_data import MarketDataIngestor
from data_ingestion.macro_data import LiquidityFetcher
from data_ingestion.news_parser import NewsParser
from whale_monitor.whale_detector import WhaleDetector
from liquidity_model.liquidity_core import LiquidityModel
from narrative_engine.narrative_model import NarrativeParser
from sector_rotation.rotation_engine import SectorRotationEngine
from risk_management.profit_ladder import ProfitLadder
from risk_management.kill_switch import KillSwitch
from datastore.state_logger import StateLogger

class FusionController:
    def __init__(self, whale_api_key=None):
        # Data Ingestion Modules
        self.market_data = MarketDataIngestor()
        self.liquidity_fetcher = LiquidityFetcher()
        self.news_parser = NewsParser()
        self.whale_detector = WhaleDetector(whale_api_key)
        self.narrative_parser = NarrativeParser()

        # Signal Processors
        self.liquidity_model = LiquidityModel()
        self.rotation_engine = SectorRotationEngine()

        # Risk Management
        self.profit_ladder = ProfitLadder()
        self.kill_switch = KillSwitch()

        # Sovereign Logger
        self.logger = StateLogger()

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

        if signals["liquidity"] > 100_000_000:
            decisions["liquidity"] = "ACCUMULATE"

        if signals["sentiment"] > 3:
            decisions["sentiment"] = "BULLISH"

        if signals["whales"] > 5:
            decisions["whales"] = "LARGE ACCUMULATION"

        if signals["sectors"]["DeFi"] > 50:
            decisions["rotation"] = "DEPLOY TO DEFI"

        profit_targets = self.profit_ladder.evaluate_profit_targets(1000)

        return {
            "decisions": decisions,
            "profit_targets": profit_targets
        }

    def run_cycle(self):
        print("Running Sovereign Fusion Cycle...\n")
        data = self.collect_data()
        signals = self.process_signals(data)
        actions = self.decide_actions(signals)

        print("\n--- MCP Fusion Report ---")
        print(f"Signals: {signals}")
        print(f"Decisions: {actions['decisions']}")
        print(f"Profit Ladder: {actions['profit_targets']}")
        print("-------------------------\n")

        self.logger.log_cycle(data, signals, actions["decisions"])

if __name__ == "__main__":
    WHALE_API_KEY = "INSERT_YOUR_API_KEY"
    fusion = FusionController(whale_api_key=WHALE_API_KEY)
    fusion.run_cycle()
