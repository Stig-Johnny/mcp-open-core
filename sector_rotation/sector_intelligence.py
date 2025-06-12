# MCP Phase 49 — Sector Intelligence Engine v2.0

import random

class SectorIntelligence:
    def __init__(self):
        self.sectors = [
            "Layer1", "AI", "DeFi", "Memes", "Underdogs"
        ]

    def compute_sector_bias(self):
        # Simulated sector rotation scores (placeholder for live capital flow analysis)
        sector_scores = {sector: round(random.uniform(-1, 1), 3) for sector in self.sectors}
        dominant_sector = max(sector_scores, key=sector_scores.get)
        dominant_score = sector_scores[dominant_sector]

        if dominant_score > 0.6:
            rotation_bias = 1  # strong rotation
        elif dominant_score > 0.2:
            rotation_bias = 0.5  # mild rotation
        elif dominant_score < -0.6:
            rotation_bias = -1  # exit rotation
        elif dominant_score < -0.2:
            rotation_bias = -0.5  # mild exit
        else:
            rotation_bias = 0  # neutral

        print(f"📊 Sector Rotation Bias: {rotation_bias} ({dominant_sector})")

        return rotation_bias
