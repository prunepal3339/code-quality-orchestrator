import socket
import threading
import time
import os

# === Original server logic (embedded inside test) ===
def handle_client(client_socket):
    while True:
        try:
            data = client_socket.recv(1024).decode("utf-8")
            if not data:
                break

            credentials = data.strip().split(':')
            if len(credentials) != 2:
                client_socket.send("Invalid format. Use username:password\n".encode("utf-8"))
                continue

            username, password = credentials[0], credentials[1]

            with open("users.txt", "r") as f:
                users = f.read().splitlines()
                auth = f"{username}:{password}" in users

            if auth:
                client_socket.send("Login successful\n".encode("utf-8"))
            else:
                client_socket.send("Login failed\n".encode("utf-8"))
        except:
            client_socket.close()
            break

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", 12345))
    server_socket.listen(5)
    print("Server listening on port 12345")

    while True:
        client_socket, addr = server_socket.accept()
        threading.Thread(target=handle_client, args=(client_socket,), daemon=True).start()

# === Test logic ===
def simulate_client(username, password):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(("127.0.0.1", 12345))
        s.send(f"{username}:{password}".encode("utf-8"))
        response = s.recv(1024).decode("utf-8")
        return response.strip()

def run_test():
    # Step 1: Create test user file
    with open("users.txt", "w") as f:
        f.write("admin:1234\n")

    # Step 2: Start server in a background thread
    threading.Thread(target=start_server, daemon=True).start()
    time.sleep(1)  # Wait for server to be ready

    # Step 3: Run login test cases
    print(">> Test: Correct login")
    res1 = simulate_client("admin", "1234")
    print(f"Response: {res1}")

    print(">> Test: Wrong login")
    res2 = simulate_client("admin", "wrongpass")
    print(f"Response: {res2}")

    print(">> Test: Invalid format")
    res3 = simulate_client("admin_only", "")
    print(f"Response: {res3}")

    # Cleanup
    if os.path.exists("users.txt"):
        os.remove("users.txt")

if __name__ == "__main__":
    run_test()
