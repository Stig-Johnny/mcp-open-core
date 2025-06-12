# ARCHIVED: This file has been moved to /archive/ and is not part of the active MCP core system.

import time
import schedule
import traceback
import os
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
    # Use environment variable for Whale API Key
    WHALE_API_KEY = os.getenv("WHALE_API_KEY")
    if not WHALE_API_KEY:
        print("[MetaScheduler] ERROR: Please set WHALE_API_KEY as an environment variable.")
        exit(1)
        
    scheduler = MetaScheduler(whale_api_key=WHALE_API_KEY)
    scheduler.start()
