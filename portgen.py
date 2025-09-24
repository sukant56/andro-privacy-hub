import random

MASKED_IP = "192.0.0.2"
TOR_SOCKS_PORT = random.randint(30000, 40000)
TOR_CONTROL_PORT = random.randint(40001, 50000)
I2PD_SOCKS_PORT = random.randint(50001, 60000)
I2PD_API_PORT = random.randint(60001, 65000)

with open("config.py", "w") as f:
    f.write(f'''MASKED_IP = "{MASKED_IP}"
TOR_SOCKS_PORT = {TOR_SOCKS_PORT}
TOR_CONTROL_PORT = {TOR_CONTROL_PORT}
I2PD_SOCKS_PORT = {I2PD_SOCKS_PORT}
I2PD_API_PORT = {I2PD_API_PORT}
I2PD_API = f"http://127.0.0.1:{I2PD_API_PORT}"
PROXYCHAINS_CONF_PATH = "/data/data/com.termux/files/usr/etc/proxychains.conf"
''')

with open("proxychains.conf", "w") as f:
    f.write(f"""strict_chain
proxy_dns
tcp_read_time_out 15000
tcp_connect_time_out 8000

[ProxyList]
socks5 {MASKED_IP} {TOR_SOCKS_PORT}
socks5 {MASKED_IP} {I2PD_SOCKS_PORT}
""")

print("Ports and proxychains config generated.")
