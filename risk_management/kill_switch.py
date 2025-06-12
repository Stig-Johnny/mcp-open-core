# risk_management/kill_switch.py

"""
MCP Open Core - Kill Switch Module
Placeholder logic for triggering emergency exits.
"""

class KillSwitch:
    def __init__(self):
        self.threshold = -10  # Percent drawdown

    def check_risk(self, pnl_percent):
        if pnl_percent < self.threshold:
            print("KILL SWITCH TRIGGERED!")
            return True
        print("No kill switch trigger.")
        return False

if __name__ == "__main__":
    ks = KillSwitch()
    ks.check_risk(-15)
