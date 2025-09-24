import socket
import config

def start_hidden_service_server(port=8080):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((config.MASKED_IP, port))
    s.listen(5)
    print(f"Server listening on {config.MASKED_IP}:{port}")
    while True:
        conn, addr = s.accept()
        print(f"Connection from {addr}")
        data = conn.recv(4096)
        print("Received:", data)
        conn.sendall(b"ACK: " + data)
        conn.close()

if __name__ == "__main__":
    start_hidden_service_server()
