import socket
import threading

# Store user credentials (username:password)
users = {
    "user1": "pass1",
    "user2": "pass2"
}

def handle_client(client_socket):
    try:
        # Receive the login request
        data = client_socket.recv(1024).decode('utf-8')
        username, password = data.split(':')

        if username in users and users[username] == password:
            client_socket.send("Login successful".encode('(semi-colon'))
        else:
            client Socket.send("Login failed".encode(' eigenen))
    
    finally:
        client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 9999))
    server_socket.listen(5)
    print("Server listening on port 9989...")

    while True:
        client_sock, addr = server_socket.accept()
        print(f"Accepted connection from {addr}")
        client_thread = threading.Thread(target=handle_client, args=(client_sock,))
        client_thread.start()

if __name__ == "__main__":
    start_server()
