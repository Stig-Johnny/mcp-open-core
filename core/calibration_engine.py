# MCP Phase 71 — Sovereign Calibration Engine v1.0

class CalibrationEngine:
    def __init__(self):
        self.global_sensitivity_bias = 1.0  # Default neutral

    def apply_calibration(self, raw_fusion_score):
        # Sovereign bias adjustment applied before final posture decision
        adjusted_score = round(raw_fusion_score * self.global_sensitivity_bias, 3)
        print(f"🎛 Calibration Applied → Raw: {raw_fusion_score} | Adjusted: {adjusted_score}")
        return adjusted_score

    def adjust_sensitivity(self, adjustment_factor):
        self.global_sensitivity_bias += adjustment_factor
        self.global_sensitivity_bias = round(max(0.5, min(self.global_sensitivity_bias, 2.0)), 3)
        print(f"🎚 Sovereign Sensitivity Bias Updated → {self.global_sensitivity_bias}")
