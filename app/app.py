from flask import Flask, render_template, jsonify
import random, datetime, os, time

app = Flask(__name__)
start_time = datetime.datetime.now()

quotes = [
    "Everything is a YAML problem if you look hard enough.",
    "Kubernetes: where 'Hello World' needs 12 microservices.",
    "I don’t always scale, but when I do, it's horizontal.",
    "The pods are down, blame DNS.",
    "The LoadBalancer got emotionally overwhelmed.",
    "Why debug when you can delete and redeploy?",
    "StatefulSets? I'd rather not.",
    "If it works in dev, it'll fail in prod.",
    "My pod was fine until I looked at it.",
    "Just one more sidecar..."
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/quote")
def get_quote():
    return jsonify(quote=random.choice(quotes))

@app.route("/api/status")
def get_status():
    uptime = datetime.datetime.now() - start_time
    return jsonify(
        status="OK",
        uptime=str(uptime),
        pod=os.environ.get("HOSTNAME", "unknown")
    )

@app.route("/api/stress")
def stress():
    end = time.time() + 10
    while time.time() < end:
        pass
    return jsonify(message="CPU stress complete.")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

