import requests, time
import matplotlib.pyplot as plt
import config

peer_stats = []

def get_i2p_peers():
    try:
        response = requests.get(f"{config.I2PD_API}/stats", timeout=10)
        stats = response.json()
        return stats
    except Exception as e:
        return {"error": str(e)}

def peer_stats_worker():
    while True:
        stats = get_i2p_peers()
        peer_stats.append(stats)
        print(stats)
        time.sleep(2)

def plot_bandwidth_graph():
    if not peer_stats:
        print("No bandwidth data yet.")
        return
    times = range(len(peer_stats))
    bandwidths = [int(p.get("Bandwidth", 0)) for p in peer_stats]
    plt.plot(times, bandwidths)
    plt.title("I2P Bandwidth (bytes/sec)")
    plt.xlabel("Time")
    plt.ylabel("Bandwidth")
    plt.savefig("/data/data/com.termux/files/home/i2p_bandwidth.png")
    plt.close()

if __name__ == "__main__":
    import threading
    threading.Thread(target=peer_stats_worker, daemon=True).start()
    while True:
        plot_bandwidth_graph()
        time.sleep(60)
