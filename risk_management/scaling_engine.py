# MCP Phase 19 — Trinity Quant Scaling Engine

class ScalingEngine:
    def __init__(self, base_position=1.0, scaling_curve="linear"):
        self.base_position = base_position
        self.scaling_curve = scaling_curve

    def compute_scaled_position(self, signal_strength, signal_max=5.0):
        normalized = min(max(signal_strength / signal_max, 0), 1)

        if self.scaling_curve == "linear":
            scaling_multiplier = normalized

        elif self.scaling_curve == "quadratic":
            scaling_multiplier = normalized ** 2

        elif self.scaling_curve == "exponential":
            scaling_multiplier = normalized ** 3

        else:
            scaling_multiplier = normalized  # fallback

        scaled_position = self.base_position * scaling_multiplier
        return round(scaled_position, 6)
