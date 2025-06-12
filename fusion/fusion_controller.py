# MCP Fusion Controller — Phase 33: Liquidity Shock Engine Fully Integrated

# (All prior imports remain identical except add:)

from liquidity_model.liquidity_shock import LiquidityShockEngine

class FusionController:
    def __init__(self, binance_api_key=None, binance_api_secret=None):
        # (Existing initializations remain identical)
        self.liquidity_shock = LiquidityShockEngine()
        # All other modules initialized as before...

    def collect_data(self):
        print("Collecting Data...")
        market = self.market_data.fetch_price("BTCUSDT")
        stablecoins = self.liquidity_fetcher.fetch_stablecoin_data()
        news = self.news_parser.fetch_headlines()
        whale_pressure = self.orca_x.compute_whale_pressure()
        volatility_shock = self.sigma_wave.compute_volatility_shock()
        corridor_pressure, corridor_breakdown = self.liquidity_corridor.compute_corridor_pressure()
        sentiment_delta = self.sentiment_engine.compute_sentiment_delta()
        sentinel_spike = self.sentinel.compute_spike_risk()
        liquidity_shock = self.liquidity_shock.detect_shock()

        return {
            "market": market,
            "stablecoins": stablecoins,
            "news": news,
            "whale_pressure": whale_pressure,
            "volatility_shock": volatility_shock,
            "corridor_pressure": corridor_pressure,
            "corridor_breakdown": corridor_breakdown,
            "sentiment_delta": sentiment_delta,
            "sentinel_spike": sentinel_spike,
            "liquidity_shock": liquidity_shock
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
            "sentiment_delta": data["sentiment_delta"],
            "sentinel_spike": data["sentinel_spike"],
            "liquidity_shock": data["liquidity_shock"],
            "sectors": sector_scores
        }

    def decide_actions(self, signals):
        fusion_score = self.quantum_node.compute_fusion_score(signals)
        decisions = {}

        if fusion_score > 3:
            decisions["FUSION_BIAS"] = "RISK-ON MODE"
        elif fusion_score < 0:
            decisions["FUSION_BIAS"] = "DEFENSIVE MODE"
        else:
            decisions["FUSION_BIAS"] = "NEUTRAL MONITORING"

        if signals["sentinel_spike"] == "HIGH SPIKE RISK":
            decisions["SENTINEL_ALERT"] = "IMMINENT MOVE DETECTED"

        if signals["liquidity_shock"] == "LIQUIDITY DRAIN WARNING":
            decisions["LIQUIDITY_SHOCK_ALERT"] = "POTENTIAL SQUEEZE EMERGING"

        profit_targets = self.profit_ladder.evaluate_profit_targets(
            portfolio_value=1000,
            sigma_score=signals["volatility"]
        )

        return {
            "decisions": decisions,
            "profit_targets": profit_targets
        }

    # (Rest of FusionController remains identical for run_cycle, execution, logging, etc.)
