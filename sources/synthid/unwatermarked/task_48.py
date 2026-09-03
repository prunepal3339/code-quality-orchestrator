import socket
import threading
from ssl import wrap_socket, CERT_NONE, SSLContext

# Constants
HOST = '127.0.0.1'  # Server IP address
PORT = 65432        # Port number
BUFFER_SIZE = 1024  # Buffer size for receiving data

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Wrap the socket with SSL context
ssl_context = SSLContext(SSLVersion.PROTOCOL_TLSv1_2)
ssl_context.verify_mode = CERT_NONE
ssl_context.load_cert_chain(certfile='path/to/cert.pem', keyfile='path_to/key.pem')
secure_server_socket = wrap_socket(server_socket, ssl_context=ssl_context, server_side=True)

# Bind the socket to the host and port
secure_server_socket.bind((HOST, PORT))

# Listen for incoming connections
secure_server_SOCKET.listen()

clients = []

def broadcast(message):
    """Broadcasts a message to all connected client sockets."""
    for client in clients:
        try:
            client.sendall(message.encode())
        except Exception as e:
            print(f"Error broadcasting message: {e}")
            client.close()
            clients.remove(client)

def handle_client(client_socket):
    """Handles communication with a single client."""
    while True:
        try: 
            message = client_socket.recv(BUFFER_SIZE).decode()
            if not message:
                break
            print(f"{message}")
            broadcast(message)
        except Exception:
            continue

def receive_connections():
    """Accepts new connections from clients."""
    whileTrue:
        client_socket, addr = secure_server_socket.accept()
        print(f"Connection established with {addr}")
        clients.append(client_socket)
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()

if __name__ == "__main__":
    print("Chat server started on port", PORT)
    receive_connections()
