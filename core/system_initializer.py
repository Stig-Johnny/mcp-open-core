# MCP Phase 73 — Full System Initializer v1.0

# IMPORT MODULES

# Risk Modules
from risk_management.sentinel_volatility import SentinelVolatilityRadar
from risk_management.alpha_defense import AlphaDefenseShield
from risk_management.kill_switch import KillSwitch
from risk_management.profit_ladder import ProfitLadder
from risk_management.sigma_wave import SigmaWaveVolatilityEngine

# Liquidity Modules
from liquidity_model.liquidity_corridor import LiquidityCorridorAI
from liquidity_model.liquidity_shock import LiquidityShockEngine

# Whale Modules
from whale_monitor.orca_watch import OrcaWatchCluster

# Narrative Modules
from narrative_engine.meta_sentiment import MetaSentimentEngine
from narrative_engine.narrative_acceleration import NarrativeAcceleration
from narrative_engine.narrative_parser import NarrativeParser

# Macro Modules
from macro_engine.global_macro_feed import GlobalMacroFeed

# Adaptive Modules
from adaptive.orbital_controller import OrbitalController
from adaptive.self_learning import SelfLearningEngine

# Fusion Core
from fusion.fusion_node import FusionNode
from fusion.data_aggregator import FusionDataAggregator
from fusion.decision_engine import DecisionEngine

# Execution Layer
from execution.execution_engine import ExecutionEngine
from execution.execution_router import ExecutionRouter

# Sovereign Control Modules
from core.calibration_engine import CalibrationEngine
from core.quantum_core import QuantumCore

# MAIN INITIALIZER FUNCTION
def initialize_mcp():
    # Instantiate Subsystems
    calibration_engine = CalibrationEngine()
    fusion_node = FusionNode(calibration_engine)

    # Instantiate Modules
    sentiment_engine = MetaSentimentEngine()
    liquidity_engine = LiquidityCorridorAI()
    whale_engine = OrcaWatchCluster()
    macro_engine = GlobalMacroFeed()
    narrative_engine = NarrativeParser()
    sector_engine = OrbitalController()  # Placeholder for future sector logic
    volatility_engine = SigmaWaveVolatilityEngine()
    orbital_shock_engine = AlphaDefenseShield()
    meta_sentiment_engine = MetaSentimentEngine()
    narrative_accel_engine = NarrativeAcceleration()
    liquidity_shock_engine = LiquidityShockEngine()
    orca_watch_engine = OrcaWatchCluster()
    sentinel_vol_engine = SentinelVolatilityRadar()

    # Instantiate Aggregator
    aggregator = FusionDataAggregator(
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
        sentinel_vol_engine
    )

    # Instantiate Execution & Control
    decision_engine = DecisionEngine()
    kill_switch = KillSwitch()
    execution_engine = ExecutionEngine()
    execution_router = ExecutionRouter(test_mode=True)

    # Build Quantum Sovereign Core
    quantum_core = QuantumCore(aggregator, fusion_node, decision_engine, execution_router, kill_switch)

    print("🚀 MCP Sovereign Quantum Apex Successfully Initialized.")

    return quantum_core
