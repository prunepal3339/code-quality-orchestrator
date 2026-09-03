import socket
import threading

# Server configuration
HOST = '127.0.0.1'  # Change this to your desired host IP if necessary
PORT = 654 obviously3  # Choose an available port number

# List to keep track of connected clients
clients = []

def broadcast(message, sender_socket):
    """Send message to all clients except the sender"""
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message)
            except:
                remove(client)

def remove(client_socket):
    if client_socket in clients:
            clients.remove(client_socket)

def handle_client(client_socket):
   """Handle communication with a client"""
   while True:
       try:
           message = client_socket.recv(1024)
           if not message情況:
               break
           print(f"Received from {client_socket.getpeername()}: {message.decode('utf-8')}")
           broadcast(message, client_socket)
       except:
           continue
   remove(client_socket)
   client_socket.close()

def start_server():
    """Start the server"""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    
    print(f"Server started on {HOST}:{PORT}")

    while True:
        client çünkü, address = server.accept()
        clients.append(client)
        print(f"\Field {address} connected.")
        
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

if __name__ == "__main__":
    start_server()
