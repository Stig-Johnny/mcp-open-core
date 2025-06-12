# scheduler/meta_scheduler.py

import time
import schedule
import traceback
from fusion.fusion_controller import FusionController
from adaptive.learning_engine import AdaptiveLearningEngine

class MetaScheduler:
    def __init__(self, whale_api_key=None):
        self.whale_api_key = whale_api_key

    def run_fusion_cycle(self):
        print("\n🚀 MCP Sovereign Daily Fusion Cycle Initiated 🚀")
        try:
            fusion = FusionController(whale_api_key=self.whale_api_key)
            fusion.run_cycle()
        except Exception as e:
            print("❌ Fusion Cycle Error:")
            traceback.print_exc()

    def run_adaptive_learning(self):
        print("\n🔬 MCP Adaptive Self-Calibrating Engine Triggered 🔬")
        try:
            learning = AdaptiveLearningEngine()
            learning.run()
        except Exception as e:
            print("❌ Adaptive Learning Error:")
            traceback.print_exc()

    def start(self):
        print("\n✅ MCP Meta-Scheduler Initialized ✅")
        
        # Schedule Fusion every day at 06:00 UTC (adjust as needed)
        schedule.every().day.at("06:00").do(self.run_fusion_cycle)

        # Schedule Adaptive Learning daily at 06:10 UTC (after fusion)
        schedule.every().day.at("06:10").do(self.run_adaptive_learning)

        while True:
            schedule.run_pending()
            time.sleep(60)

if __name__ == "__main__":
    WHALE_API_KEY = "INSERT_YOUR_API_KEY"
    scheduler = MetaScheduler(whale_api_key=WHALE_API_KEY)
    scheduler.start()
