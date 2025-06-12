# MCP Phase 68 — Fusion Data Aggregator v1.0

class FusionDataAggregator:
    def __init__(self,
                 sentiment_engine,
                 liquidity_engine,
                 whale_engine,
                 macro_engine,
                 narrative_engine,
                 sector_engine,
                 volatility_engine,
                 orbital_shock_engine,
                 meta_sentiment_engine,
                 narrative_accel_engine,
                 liquidity_shock_engine,
                 orca_watch_engine,
                 sentinel_vol_engine):
        self.sentiment_engine = sentiment_engine
        self.liquidity_engine = liquidity_engine
        self.whale_engine = whale_engine
        self.macro_engine = macro_engine
        self.narrative_engine = narrative_engine
        self.sector_engine = sector_engine
        self.volatility_engine = volatility_engine
        self.orbital_shock_engine = orbital_shock_engine
        self.meta_sentiment_engine = meta_sentiment_engine
        self.narrative_accel_engine = narrative_accel_engine
        self.liquidity_shock_engine = liquidity_shock_engine
        self.orca_watch_engine = orca_watch_engine
        self.sentinel_vol_engine = sentinel_vol_engine

    def collect_signals(self):
        sentiment = self.sentiment_engine.compute_sentiment()
        liquidity = self.liquidity_engine.compute_liquidity_flow()
        whales = self.whale_engine.compute_whale_pressure()
        macro_bias = self.macro_engine.compute_macro_bias()
        sector_bias = self.sector_engine.compute_sector_bias()
        volatility = self.volatility_engine.compute_volatility_shock()
        orbital_shock = self.orbital_shock_engine.compute_shock_signal()
        meta_sentiment, meta_sentiment_spread = self.meta_sentiment_engine.compute_meta_sentiment()
        narrative_acceleration = self.narrative_accel_engine.compute_acceleration()
        liquidity_shock = self.liquidity_shock_engine.detect_shock()
        whale_cluster = self.orca_watch_engine.compute_whale_cluster_signal()
        sentinel_spike = self.sentinel_vol_engine.compute_spike_risk()

        signals = {
            "sentiment": sentiment,
            "liquidity": liquidity,
            "whales": whales,
            "macro_bias": macro_bias,
            "sector_bias": sector_bias,
            "volatility": volatility,
            "orbital_shock": orbital_shock,
            "meta_sentiment": meta_sentiment,
            "meta_sentiment_spread": meta_sentiment_spread,
            "narrative_acceleration": narrative_acceleration,
            "liquidity_shock": liquidity_shock,
            "whale_cluster": whale_cluster,
            "sentinel_spike": sentinel_spike
        }

        return signals
