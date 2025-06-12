# MCP Phase 81 — Sovereign Quantum API Gateway v1.0

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, request, jsonify, render_template
from adaptive.reinforcement_model import ReinforcementModel
from core.calibration_engine import CalibrationEngine
from fusion.fusion_node import FusionNode
from fusion.decision_engine import DecisionEngine
from exchange_connector.binance_connector import BinanceConnector

# Initialize Sovereign Modules
reinforcement_model = ReinforcementModel()
calibration_engine = CalibrationEngine()
fusion_node = FusionNode(calibration_engine)
decision_engine = DecisionEngine()

# Create Flask API Gateway
app = Flask(__name__)

@app.route("/fusion_score", methods=["POST"])
def fusion_endpoint():
    signals = request.get_json()

    fusion_score = fusion_node.compute_fusion_score(signals)
    posture = decision_engine.determine_posture(fusion_score, kill_switch_flag=False)

    response = {
        "fusion_score": fusion_score,
        "posture": posture,
        "reinforcement_bias": reinforcement_model.bias_adjustment,
        "calibration_bias": calibration_engine.global_sensitivity_bias
    }

    return jsonify(response)

@app.route("/adjust_calibration", methods=["POST"])
def calibration_endpoint():
    data = request.get_json()
    adj = data.get("adjustment", 0.0)
    calibration_engine.adjust_sensitivity(adj)

    return jsonify({
        "updated_bias": calibration_engine.global_sensitivity_bias
    })

@app.route("/compute_reinforcement", methods=["GET"])
def reinforcement_endpoint():
    reinforcement_model.compute_bias()
    return jsonify({
        "reinforcement_bias": reinforcement_model.bias_adjustment
    })

@app.route("/healthcheck", methods=["GET"])
def healthcheck():
    return jsonify({"status": "MCP Sovereign API Gateway Operational"})

@app.route("/dashboard", methods=["GET"])
def dashboard():
    # Generate a sample signal (in production, use real/latest data)
    signals = {
        "sentiment": 0.5,
        "liquidity": 0.7,
        "whales": 100,
        "macro_bias": 1,
        "sector_bias": 0,
        "narrative_acceleration": "BUILDING MOMENTUM",
        "liquidity_shock": "NONE",
        "whale_cluster": "NEUTRAL CLUSTER BALANCE",
        "meta_sentiment": 0.2,
        "meta_sentiment_spread": 0.1,
        "sentinel_spike": "NORMAL"
    }
    fusion_score = fusion_node.compute_fusion_score(signals)
    posture = decision_engine.determine_posture(fusion_score, kill_switch_flag=False)
    html = f"""
    <html><head><title>MCP Dashboard</title></head><body>
    <h1>MCP Sovereign Dashboard</h1>
    <p><b>Fusion Score:</b> {fusion_score}</p>
    <p><b>Posture:</b> {posture}</p>
    <p><b>Calibration Bias:</b> {calibration_engine.global_sensitivity_bias}</p>
    <p><b>Reinforcement Bias:</b> {reinforcement_model.bias_adjustment}</p>
    </body></html>
    """
    return html

@app.route("/mcp/dashboard", methods=["GET"])
def mcp_dashboard():
    return render_template("mcp_dashboard.html")

@app.route("/live", methods=["GET"])
def live_analytics():
    # In production, use FusionController to get live data
    from fusion.fusion_controller import FusionController
    fusion = FusionController()
    data = fusion.collect_data()
    signals = fusion.process_signals(data)
    decisions = fusion.decide_actions(signals)
    return jsonify({
        "market": data["market"],
        "order_book": data["order_book"],
        "fusion_signals": signals,
        "decisions": decisions,
        "on_chain_whale": data.get("on_chain_whale", []),
        "news": data.get("news", [])
    })

@app.route("/assets/spot", methods=["GET"])
def get_spot_assets():
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")
    if not api_key or not api_secret:
        return jsonify({"error": "Binance API keys not set in environment."}), 400
    connector = BinanceConnector(api_key, api_secret, test_mode=False)
    account_info = connector.get_account_info()
    balances = account_info.get("balances", [])
    # Filter out zero balances for clarity
    nonzero_balances = [b for b in balances if float(b.get("free", 0)) > 0 or float(b.get("locked", 0)) > 0]
    return jsonify({"assets": nonzero_balances})

@app.route("/mcp/context", methods=["GET"])
def mcp_context():
    # Get balances
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")
    balances = []
    if api_key and api_secret:
        from exchange_connector.binance_connector import BinanceConnector
        connector = BinanceConnector(api_key, api_secret, test_mode=False)
        account_info = connector.get_account_info()
        balances = [b for b in account_info.get("balances", []) if float(b.get("free", 0)) > 0 or float(b.get("locked", 0)) > 0]
    # Get posture and fusion score
    signals = {
        "sentiment": 0.5,
        "liquidity": 0.7,
        "whales": 100,
        "macro_bias": 1,
        "sector_bias": 0,
        "narrative_acceleration": "BUILDING MOMENTUM",
        "liquidity_shock": "NONE",
        "whale_cluster": "NEUTRAL CLUSTER BALANCE",
        "meta_sentiment": 0.2,
        "meta_sentiment_spread": 0.1,
        "sentinel_spike": "NORMAL"
    }
    fusion_score = fusion_node.compute_fusion_score(signals)
    posture = decision_engine.determine_posture(fusion_score, kill_switch_flag=False)
    # MCP context schema
    context = {
        "balances": balances,
        "fusion_score": fusion_score,
        "posture": posture,
        "calibration_bias": calibration_engine.global_sensitivity_bias,
        "reinforcement_bias": reinforcement_model.bias_adjustment
    }
    return jsonify({"context": context})

@app.route("/mcp/tools", methods=["GET"])
def mcp_tools():
    # Describe available tools/actions for the MCP agent
    tools = [
        {
            "name": "get_spot_assets",
            "description": "Get current Binance spot balances.",
            "parameters": {},
            "returns": {"assets": "List of asset balances (symbol, free, locked)"}
        },
        {
            "name": "place_order",
            "description": "Place a spot market order on Binance.",
            "parameters": {
                "symbol": "Trading pair symbol, e.g., BTCUSDT",
                "side": "BUY or SELL",
                "quantity": "Order quantity (float)"
            },
            "returns": {"order_result": "Order execution result from Binance"}
        }
    ]
    return jsonify({"tools": tools})

@app.route("/mcp/action", methods=["POST"])
def mcp_action():
    data = request.get_json()
    tool = data.get("tool")
    params = data.get("parameters", {})
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")
    if not api_key or not api_secret:
        return jsonify({"error": "Binance API keys not set in environment."}), 400
    from exchange_connector.binance_connector import BinanceConnector
    connector = BinanceConnector(api_key, api_secret, test_mode=False)
    if tool == "get_spot_assets":
        account_info = connector.get_account_info()
        balances = [b for b in account_info.get("balances", []) if float(b.get("free", 0)) > 0 or float(b.get("locked", 0)) > 0]
        return jsonify({"result": {"assets": balances}})
    elif tool == "place_order":
        symbol = params.get("symbol")
        side = params.get("side")
        quantity = params.get("quantity")
        if not symbol or not side or not quantity:
            return jsonify({"error": "Missing required parameters: symbol, side, quantity."}), 400
        order_result = connector.place_order(symbol, side, quantity)
        return jsonify({"result": {"order_result": order_result}})
    else:
        return jsonify({"error": f"Unknown tool: {tool}"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5051)
