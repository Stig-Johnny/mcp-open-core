# MCP SOVEREIGN — API INTERFACE SPECIFICATION

---

🚀 MCP Quantum Apex — Sovereign External API Gateway

This document defines the public API interface for interacting with the MCP Sovereign Fusion Engine.

---

## 🎯 OBJECTIVE

- Expose safe external API endpoints for:
  - Fusion scoring
  - Reinforcement updates
  - Calibration adjustments
  - Health checks

---

## 🔧 MODULE LOCATION

`/api/quantum_api.py`

---

## 🚀 API ENDPOINTS

---

### 1️⃣ Health Check

```http
GET /healthcheck
```

✅ Response:

```json
{
  "status": "alive"
}
```

---

### 2️⃣ Fusion Score Computation

```http
POST /fusion_score
```

✅ Payload (example):

```json
{
  "signals": {
    "sentiment": 0.4,
    "liquidity": 0.2,
    "whales": 0.1,
    "macro_bias": 1,
    "sector_bias": 0.3,
    "narrative_acceleration": 0.2,
    "liquidity_shock": -0.1,
    "whale_cluster": 0.0,
    "meta_sentiment": 0.4,
    "meta_sentiment_spread": 0.1,
    "sentinel_spike": -0.2
  }
}
```

✅ Response:

```json
{
  "fusion_score": 0.57,
  "posture": "MODERATE BULL"
}
```

---

### 3️⃣ Calibration Adjustment

```http
POST /adjust_calibration
```

✅ Payload:

```json
{
  "bias_adjustment": 0.1
}
```

✅ Response:

```json
{
  "calibration_bias": 0.35
}
```

---

### 4️⃣ Reinforcement Computation (Manual Trigger)

```http
GET /compute_reinforcement
```

✅ Response:

```json
{
  "reinforcement_bias": 0.42
}
```

---

## 🛡 SAFETY FEATURES

- All inputs validated for [-1.0, 1.0] boundaries.
- Fusion score bounded between [-1.0, 1.0].
- Kill switch state blocks write access during active defense mode.

---

## 🔐 SECURITY EXTENSIONS (v2.0+)

- API Key Authorization Layer
- Rate Limiting
- Sovereign Operator Authentication
- External Client Management System

---

## 🌐 DEPLOYMENT

API Gateway initialized via:

```bash
python api/quantum_api.py
```

Listens on default port 5000 unless overridden.

---

👑 MCP Quantum Apex — Sovereign External Gateway Live
