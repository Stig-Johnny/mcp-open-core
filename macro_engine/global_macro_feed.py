# MCP Phase 34 — Global Macro Feed v1.0

import random

class GlobalMacroFeed:
    def __init__(self):
        self.last_macro_state = {
            "dxy": 100.0,
            "treasury_yield": 3.5,
            "inflation": 3.0
        }

    def simulate_macro_data(self):
        dxy = self.last_macro_state["dxy"] + random.uniform(-0.5, 0.5)
        yield_10y = self.last_macro_state["treasury_yield"] + random.uniform(-0.1, 0.1)
        inflation = self.last_macro_state["inflation"] + random.uniform(-0.1, 0.1)

        self.last_macro_state = {
            "dxy": round(dxy, 2),
            "treasury_yield": round(yield_10y, 2),
            "inflation": round(inflation, 2)
        }

        return self.last_macro_state

    def compute_macro_bias(self):
        macro = self.simulate_macro_data()

        risk_score = 0
        if macro["dxy"] > 104: risk_score -= 1
        if macro["treasury_yield"] > 4: risk_score -= 1
        if macro["inflation"] > 4: risk_score -= 1

        if macro["dxy"] < 100: risk_score += 1
        if macro["treasury_yield"] < 3.5: risk_score += 1
        if macro["inflation"] < 3: risk_score += 1

        print(f"🌐 Macro Feed → DXY: {macro['dxy']}, Yield: {macro['treasury_yield']}%, Inflation: {macro['inflation']}% | Macro Bias: {risk_score}")

        return risk_score
