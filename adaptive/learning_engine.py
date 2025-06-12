# adaptive/learning_engine.py

import os
import json

class AdaptiveLearningEngine:
    def __init__(self, log_dir="datastore/logs"):
        self.log_dir = log_dir
        self.history = []
        self.weights = {
            "sentiment": 1.0,
            "liquidity": 1.0,
            "whales": 1.0,
            "sectors": 1.0
        }

    def load_history(self):
        files = [f for f in os.listdir(self.log_dir) if f.endswith(".json")]
        for f_name in files:
            with open(os.path.join(self.log_dir, f_name)) as f:
                data = json.load(f)
                self.history.append(data)

    def calibrate(self):
        print("\n🚀 Running Adaptive Calibration ...")
        if not self.history:
            print("⚠ No historical data found.")
            return

        sentiment_sum = 0
        liquidity_sum = 0
        whale_sum = 0
        defi_sum = 0
        count = 0

        for cycle in self.history:
            signals = cycle["signals"]
            decisions = cycle["decisions"]

            if "sentiment" in decisions or "liquidity" in decisions:
                sentiment_sum += signals["sentiment"]
                liquidity_sum += signals["liquidity"]
                whale_sum += signals["whales"]
                defi_sum += signals["sectors"]["DeFi"]
                count += 1

        if count == 0:
            print("⚠ No valid decision cycles found.")
            return

        # Compute empirical thresholds (simplified)
        self.weights["sentiment"] = round(sentiment_sum / count, 2)
        self.weights["liquidity"] = round(liquidity_sum / count, 2)
        self.weights["whales"] = round(whale_sum / count, 2)
        self.weights["sectors"] = round(defi_sum / count, 2)

        print("✅ Adaptive Weights Updated:")
        print(self.weights)

    def save_model(self, file="adaptive/weights.json"):
        os.makedirs("adaptive", exist_ok=True)
        with open(file, "w") as f:
            json.dump(self.weights, f, indent=4)
        print(f"✅ Saved calibrated weights to {file}")

    def run(self):
        self.load_history()
        self.calibrate()
        self.save_model()

if __name__ == "__main__":
    engine = AdaptiveLearningEngine()
    engine.run()
