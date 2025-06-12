# MCP Fusion Controller — Phase 27: Kill Switch v2.0 Integrated

# (… all prior imports identical … just replacing the kill_switch.py logic above)

    def run_cycle(self):
        print("Running Sovereign Adaptive Fusion Cycle...\n")
        self.orbital_controller.update_adaptive_weights()
        self.adaptive_weights = self.load_adaptive_weights()

        data = self.collect_data()
        signals = self.process_signals(data)
        actions = self.decide_actions(signals)

        print("\n--- MCP Adaptive Fusion Report ---")
        print(f"Signals: {signals}")
        print(f"Decisions: {actions['decisions']}")
        print(f"Profit Ladder: {actions['profit_targets']}")
        print("-------------------------\n")

        liquidity_pressure_score = self.liquidity_pressure_core.compute_liquidity_pressure()
        print(f"🔎 LPI-X Liquidity Score: {liquidity_pressure_score}")

        whale_netflow = data["whale_pressure"] * 1000
        liquidity_netflow = data["stablecoins"]["netflow"] if isinstance(data["stablecoins"], dict) else 0

        # 🚨 NEW MULTI-LAYERED KILL SWITCH ACTIVATION
        kill_switch_triggered, kill_flags = self.kill_switch.evaluate_risk(signals, liquidity_netflow, whale_netflow)

        if kill_switch_triggered:
            print(f"🚨 ALPHA DEFENSE TRIGGERED: {kill_flags}")
            return

        self.execution_engine.execute(signals)
        self.execution_router.translate_and_execute(signals)
        self.logger.log_cycle(data, signals, actions["decisions"])

        simulated_pnl = 100
        self.self_learning.log_cycle(signals, actions["decisions"], simulated_pnl)
        bias = self.self_learning.compute_bias_adjustments()
        print(f"🧠 Adaptive Learning Bias Adjustment: {bias}")
