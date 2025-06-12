# datastore/state_logger.py

import json
import os
from datetime import datetime

class StateLogger:
    def __init__(self, log_dir="datastore/logs"):
        self.log_dir = log_dir
        os.makedirs(self.log_dir, exist_ok=True)

    def log_cycle(self, data, signals, decisions):
        timestamp = datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
        log_data = {
            "timestamp": timestamp,
            "data": data,
            "signals": signals,
            "decisions": decisions
        }

        file_path = os.path.join(self.log_dir, f"cycle_{timestamp}.json")
        with open(file_path, "w") as f:
            json.dump(log_data, f, indent=4)

        print(f"✅ Sovereign Cycle Logged: {file_path}")
