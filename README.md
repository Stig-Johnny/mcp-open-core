# MCP SOVEREIGN — Quantum Apex Deployment

---

🚀 **SOVEREIGN AI QUANT INTELLIGENCE PLATFORM**  
**Genesis Build: Phases 1-82 Completed**

---

## 🔧 MCP Architecture Summary

The MCP Sovereign System includes:

- ✅ Quantum Fusion Node  
- ✅ Adaptive Calibration Engine  
- ✅ Recursive Reinforcement Model  
- ✅ Multi-Dimensional Fusion Signals  
- ✅ Kill Switch & Profit Ladder Defense  
- ✅ Execution Router  
- ✅ Simulation Harness  
- ✅ Sovereign Deployment API  
- ✅ Operator Control Panel (UI)  
- ✅ Quantum Full Cycle Control Loops

---

## ⚙ System Initialization

### 1️⃣ Clone repository  
```bash
git clone https://github.com/Stig-Johnny/mcp-open-core.git
cd mcp-open-core
```

### 2️⃣ Install dependencies  
```bash
pip install flask requests
```

*(Note: tkinter is usually pre-installed with Python)*

---

## 🚀 Sovereign Simulation Mode

Run full sovereign simulation loop:

```bash
python simulator/full_cycle_simulator.py
```

This triggers the recursive reinforcement loop to self-calibrate fusion logic.

---

## 🚀 MCP Genesis Deployment Mode

Run full MCP Sovereign Quant Engine:

```bash
python mcp_genesis.py
```

This triggers live fusion scoring, reinforcement learning, posture decisions, and sovereign logging.

---

## 🚀 Sovereign API Interface (Live Gateway)

Start sovereign API server:

```bash
python api/quantum_api.py
```

- Fusion scoring endpoint: `POST /fusion_score`
- Calibration endpoint: `POST /adjust_calibration`
- Reinforcement endpoint: `GET /compute_reinforcement`
- Healthcheck: `GET /healthcheck`

---

## 🚀 Sovereign Operator Panel (UI Control Room)

Start operator panel for live monitoring:

```bash
python ui/operator_panel.py
```

- Refresh live fusion scoring
- Adjust calibration sensitivity directly
- Observe reinforcement learning adaptation

---

## 🖥️ MCP Model Context Protocol Dashboard (Updated UI)

The MCP dashboard now features a modern, high-contrast dark theme for optimal readability and operator experience.

- All form fields, labels, and headings are bright and easy to read.
- Use the dashboard to view context, discover tools, and invoke actions interactively.

To use:
1. Start the API server:
   ```bash
   python api/quantum_api.py
   ```
2. Open your browser and go to: [http://localhost:5051/mcp/dashboard](http://localhost:5051/mcp/dashboard)

Features:
- View current MCP context (balances, posture, etc.)
- Discover available tools/actions
- Invoke actions (e.g., get balances, place orders) via web form
- See results in real time

You can also access the dashboard from the main index page.

---

## 🧪 Sovereign Modules Included (Phases 1-82)

- fusion_node.py  
- data_aggregator.py  
- decision_engine.py  
- calibration_engine.py  
- reinforcement_model.py  
- quantum_core.py  
- sovereign_loop.py  
- execution_router.py  
- kill_switch.py  
- status_console.py  
- live_interface.py  
- mcp_genesis.py  
- full_cycle_simulator.py  
- quantum_api.py  
- operator_panel.py

---

## 🔒 Sovereign Integrity Level

**MCP Quantum Apex is now operating at Sovereign Quantum Control Layer v1.0**  
All installed modules reflect institutional-grade fund architecture.

---

## 🚨 Next Phases

Upon full verification, proceed to:

**Phase 83 → Full Sovereign Genesis System Audit**

---

## 🤖 Model Context Protocol (MCP) Endpoints for AI Agent Integration

Your MCP server now supports the Model Context Protocol, enabling direct integration with LLM agents and orchestration frameworks.

### MCP Endpoints

- **`GET /mcp/context`** — Returns current system state (balances, posture, fusion score, biases) in MCP-compliant JSON.
- **`GET /mcp/tools`** — Lists available tools/actions in a model-friendly schema.
- **`POST /mcp/action`** — Executes an action/tool (e.g., get balances, place order) with structured JSON input.

#### Example: Get System Context
```bash
curl http://localhost:5051/mcp/context | jq
```

#### Example: List Available Tools
```bash
curl http://localhost:5051/mcp/tools | jq
```

#### Example: Invoke an Action (Get Spot Assets)
```bash
curl -X POST http://localhost:5051/mcp/action \
  -H 'Content-Type: application/json' \
  -d '{"tool": "get_spot_assets", "parameters": {}}' | jq
```

#### Example: Place a Spot Order (Test Mode)
```bash
curl -X POST http://localhost:5051/mcp/action \
  -H 'Content-Type: application/json' \
  -d '{
    "tool": "place_order",
    "parameters": {
      "symbol": "BTCUSDT",
      "side": "BUY",
      "quantity": 0.001
    }
  }' | jq
```

> These endpoints make your MCP server compatible with LLM agents, agentic frameworks, and automated trading orchestration tools.

---

👑 Alpha Printing Authority: Online.
