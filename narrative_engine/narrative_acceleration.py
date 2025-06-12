# MCP Phase 40 — Narrative Acceleration Scanner v1.0

import random

class NarrativeAcceleration:
    def __init__(self):
        self.accel_window = []

    def simulate_sentiment_momentum(self):
        return round(random.uniform(-0.5, 0.5), 3)

    def update_momentum_window(self):
        new_value = self.simulate_sentiment_momentum()
        self.accel_window.append(new_value)
        if len(self.accel_window) > 40:
            self.accel_window.pop(0)

    def compute_acceleration(self):
        self.update_momentum_window()

        if len(self.accel_window) < 5:
            return 0

        first_half = self.accel_window[:len(self.accel_window)//2]
        second_half = self.accel_window[len(self.accel_window)//2:]

        avg_first = sum(first_half) / len(first_half)
        avg_second = sum(second_half) / len(second_half)

        acceleration_score = avg_second - avg_first

        if acceleration_score > 0.3:
            signal = "STRONG ACCELERATION"
        elif acceleration_score < -0.3:
            signal = "SHARP DECAY"
        else:
            signal = "NEUTRAL"

        print(f"🚀 Narrative Acceleration → Δ: {acceleration_score:.3f} | Signal: {signal}")
        return signal
