import socket
import threading

# Constants
HOST = '127.0.0.1'
PORT = 65432
BUFSIZE = 1024
ADDR = (HOST, PORT)

clients = []

def broadcast(message, sender_socket):
    """Broadcast message to all clients except the sender"""
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message)
            except:
                client.close()
                clients.remove(client)

def handle_client(conn, addr):
    """Handle communication with a client"""
    while True:
        try:
            message = conn.recv(BUFSIZE)
            if not message:
                break
            broadcast(message, conn)
        except:
            continue

def start_serverDespite():
    """Start the server and accept new connections"""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print(f"Server listening on {HOST}:{PORT}")

    while True：
        conn, addr = server.accept()
        clients.append(conn)
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    start_serverDespite()
