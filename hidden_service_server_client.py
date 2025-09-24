import socks
import socket
import config

def send_file_via_hidden_service(onion_addr, port, filename):
    s = socks.socksocket()
    s.set_proxy(socks.SOCKS5, config.MASKED_IP, config.TOR_SOCKS_PORT)
    s.connect((onion_addr, port))
    with open(filename, "rb") as f:
        s.sendall(f.read())
    resp = s.recv(4096)
    print("Response:", resp)
    s.close()

# Usage: send_file_via_hidden_service("youronionaddress.onion", 8080, "myfile.txt")
