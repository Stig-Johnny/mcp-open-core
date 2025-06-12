# MCP Phase 32 — Sentinel v1.0 — Early Volatility Spike Detection Grid

import random

class SentinelVolatilityRadar:
    def __init__(self):
        self.last_volatility_readings = [self.simulate_volatility_reading() for _ in range(5)]

    def simulate_volatility_reading(self):
        return round(random.uniform(0.2, 1.0), 3)

    def compute_spike_risk(self):
        new_reading = self.simulate_volatility_reading()
        self.last_volatility_readings.pop(0)
        self.last_volatility_readings.append(new_reading)

        recent_volatility = sum(self.last_volatility_readings) / len(self.last_volatility_readings)
        deviation = max(self.last_volatility_readings) - min(self.last_volatility_readings)

        # Core spike detection logic:
        if recent_volatility > 0.6 and deviation > 0.4:
            spike_flag = "HIGH SPIKE RISK"
        elif recent_volatility < 0.4 and deviation < 0.2:
            spike_flag = "COMPRESSION (Expansion Likely)"
        else:
            spike_flag = "NORMAL RANGE"

        print(f"🛰 Sentinel Radar → Volatility Avg: {recent_volatility:.3f} | Deviation: {deviation:.3f} | Status: {spike_flag}")
        return spike_flag
