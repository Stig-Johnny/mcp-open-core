# MCP Phase 81 — Sovereign Quantum API Gateway v1.0

from flask import Flask, request, jsonify
from adaptive.reinforcement_model import ReinforcementModel
from core.calibration_engine import CalibrationEngine
from fusion.fusion_node import FusionNode
from fusion.decision_engine import DecisionEngine

# Initialize Sovereign Modules
reinforcement_model = ReinforcementModel()
calibration_engine = CalibrationEngine()
fusion_node = FusionNode(calibration_engine, reinforcement_model)
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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005)
