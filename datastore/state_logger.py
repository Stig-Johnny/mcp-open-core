# MCP Phase 60 — State Logger v1.0

import json
import os
from datetime import datetime

class StateLogger:
    def __init__(self):
        self.log_dir = "datastore/logs"
        os.makedirs(self.log_dir, exist_ok=True)

    def log_cycle(self, data, signals, decisions):
        timestamp = datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
        log_entry = {
            "timestamp": timestamp,
            "data": data,
            "signals": signals,
            "decisions": decisions
        }
        filename = os.path.join(self.log_dir, f"log_{timestamp}.json")

        with open(filename, "w") as f:
            json.dump(log_entry, f, indent=4)

        print(f"📄 StateLogger → Cycle Logged: {filename}")
