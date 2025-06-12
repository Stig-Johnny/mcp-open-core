from flask import Flask, render_template, jsonify
import requests
import os

app = Flask(__name__)

API_URL = os.getenv("MCP_API_URL", "http://localhost:5051/live")

@app.route("/")
def home():
    try:
        resp = requests.get(API_URL, timeout=5)
        data = resp.json()
    except Exception as e:
        data = {"error": str(e)}
    return render_template("dashboard.html", data=data)

@app.route("/api/live")
def api_live():
    try:
        resp = requests.get(API_URL, timeout=5)
        return jsonify(resp.json())
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/index")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
