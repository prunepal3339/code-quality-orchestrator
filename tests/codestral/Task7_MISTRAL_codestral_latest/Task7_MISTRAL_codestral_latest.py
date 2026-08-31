import socket
import threading
import os
import time

# === Server ===
def start_server(host='localhost', port=12345):
    def handle_client(client_socket):
        try:
            data = client_socket.recv(1024).decode()
            if data.startswith("LOGIN|"):
                parts = data.strip().split("|")
                if len(parts) == 3:
                    username, password = parts[1], parts[2]
                    if authenticate(username, password):
                        client_socket.send(b"Login successful")
                    else:
                        client_socket.send(b"Invalid credentials")
                else:
                    client_socket.send(b"Invalid request format")
            else:
                client_socket.send(b"Unknown command")
        except Exception as e:
            client_socket.send(f"Error: {str(e)}".encode())
        finally:
            client_socket.close()

    def authenticate(username, password):
        if os.path.exists('users.txt'):
            with open('users.txt', 'r') as f:
                for line in f:
                    user, pw = line.strip().split(':')
                    if user == username and pw == password:
                        return True
        return False

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()
    print(f"Server listening on {host}:{port}")
    while True:
        client_sock, _ = server_socket.accept()
        threading.Thread(target=handle_client, args=(client_sock,), daemon=True).start()

# === Client ===
def run_client(username, password, host='localhost', port=12345):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    message = f"LOGIN|{username}|{password}"
    client_socket.send(message.encode())
    response = client_socket.recv(1024).decode()
    client_socket.close()
    return response

# === Test Run ===
def run_test():
    # Create test user
    with open("users.txt", "w") as f:
        f.write("admin:1234\n")

    # Start server in background thread
    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()

    # Wait a bit for the server to be ready
    time.sleep(1)

    # Run client
    print("Running client with correct credentials...")
    print("Response:", run_client("admin", "1234"))

    print("Running client with wrong credentials...")
    print("Response:", run_client("admin", "wrong"))

    # Optional: cleanup
    if os.path.exists("users.txt"):
        os.remove("users.txt")

if __name__ == "__main__":
    run_test()
