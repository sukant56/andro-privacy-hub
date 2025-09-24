from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO
import threading, time
from peer_analytics import peer_stats

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template("dashboard.html")

@app.route("/api/peers")
def api_peers():
    return jsonify(peer_stats[-1] if peer_stats else {})

def push_peer_stats():
    while True:
        if peer_stats:
            socketio.emit("peer_update", peer_stats[-1])
        time.sleep(2)

if __name__ == "__main__":
    threading.Thread(target=push_peer_stats, daemon=True).start()
    socketio.run(app, host="0.0.0.0", port=5000)
