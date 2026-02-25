from flask import Flask, render_template, jsonify
import psutil

app = Flask(__name__)

def get_stats():
    return {
        "cpu": psutil.cpu_percent(interval=0.5),
        "ram": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage('/').percent
    }

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/stats")
def stats():
    return jsonify(get_stats())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
