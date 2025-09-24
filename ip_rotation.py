import requests, time
from stem import Signal
from stem.control import Controller
import config

def renew_tor_ip():
    with Controller.from_port(port=config.TOR_CONTROL_PORT) as c:
        c.authenticate()
        c.signal(Signal.NEWNYM)

def get_ip_location():
    proxies = {"http": f"socks5h://{config.MASKED_IP}:{config.TOR_SOCKS_PORT}", "https": f"socks5h://{config.MASKED_IP}:{config.TOR_SOCKS_PORT}"}
    ip = requests.get("https://ipv4.icanhazip.com", proxies=proxies, timeout=10).text.strip()
    loc = requests.get(f"https://ip-api.com/json/{ip}", proxies=proxies, timeout=10).json()
    print(f"IP: {ip}, Location: {loc.get('country')}, {loc.get('city')}")

def live_ip_location_rotation(interval=2):
    while True:
        renew_tor_ip()
        time.sleep(3)
        get_ip_location()
        time.sleep(interval)

if __name__ == "__main__":
    live_ip_location_rotation()
