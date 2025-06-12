# fusion/control_panel.py

from fusion.fusion_controller import FusionController

class ControlPanel:
    def __init__(self, whale_api_key=None):
        self.fusion = FusionController(whale_api_key=whale_api_key)

    def run_cycle(self):
        print("\n🚀 MCP Sovereign Control Panel 🚀")
        self.fusion.run_cycle()

    def interactive_loop(self):
        print("\n✅ MCP Control Console Initialized.\n")
        while True:
            cmd = input("Enter command (run/exit): ").lower()
            if cmd == "run":
                self.run_cycle()
            elif cmd == "exit":
                print("Exiting Sovereign MCP Control Center. 🛑")
                break
            else:
                print("Unknown command. Use 'run' or 'exit'.")

if __name__ == "__main__":
    # Insert your Whale Alert API Key here
    WHALE_API_KEY = "INSERT_YOUR_API_KEY"
    panel = ControlPanel(whale_api_key=WHALE_API_KEY)
    panel.interactive_loop()
