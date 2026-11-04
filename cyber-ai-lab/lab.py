#!/usr/bin/env python3
"""Safe localhost-only networking lab. No external target scanning."""
import socket
import threading

HOST = "127.0.0.1"
PORT = 8765

def serve_once(listener):
    conn, _ = listener.accept()
    with conn:
        conn.sendall(b"Cyber AI Lab: local test service\n")

def main():
    with socket.socket() as server:
        server.bind((HOST, PORT))
        server.listen(1)
        thread = threading.Thread(target=serve_once, args=(server,), daemon=True)
        thread.start()
        with socket.create_connection((HOST, PORT), timeout=5) as client:
            print(client.recv(1024).decode().strip())
        thread.join(timeout=5)
    print("Try: nmap -sT -p 8765 127.0.0.1 (start a persistent service first)")

if __name__ == "__main__":
    main()
