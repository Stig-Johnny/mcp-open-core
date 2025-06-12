# ARCHIVED: This file has been moved to /archive/ and is not part of the active MCP core system.

# dashboard/control_center.py

from flask import Flask, render_template, jsonify
import os
import json

app = Flask(__name__)

LOG_DIR = "datastore/logs"

def load_latest_log():
    files = sorted(
        [f for f in os.listdir(LOG_DIR) if f.endswith(".json")],
        reverse=True
    )
    if not files:
        return {"status": "No Fusion Cycles Logged Yet."}

    with open(os.path.join(LOG_DIR, files[0])) as f:
        data = json.load(f)
    return data

@app.route("/")
def home():
    log = load_latest_log()
    return render_template("dashboard.html", log=log)

@app.route("/api/latest")
def api_latest():
    return jsonify(load_latest_log())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
