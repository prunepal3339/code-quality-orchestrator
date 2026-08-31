import socket
import threading
import time
import os

# === Original server logic ===
def authenticate(username, password):
    with open("users.txt", "r") as file:
        for line in file:
            user, pwd = line.strip().split(":")
            if user == username and pwd == password:
                return True
    return False

def server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 10000))
    sock.listen(1)
    print("Server started. Waiting for connections...")

    connection, address = sock.accept()
    print(f"Connected to {address}")

    while True:
        data = connection.recv(1024).decode()
        if not data:
            break
        if data.startswith("LOGIN"):
            _, username, password = data.strip().split()
            if authenticate(username, password):
                connection.sendall("LOGIN_SUCCESS".encode())
            else:
                connection.sendall("LOGIN_FAILED".encode())
        else:
            print(f"Received message: {data}")
            connection.sendall(f"Server received your message: {data}".encode())

    connection.close()
    sock.close()

# === Test logic ===
def run_test():
    # Step 1: Prepare users.txt
    with open("users.txt", "w") as f:
        f.write("admin:1234\n")

    # Step 2: Start the server in a background thread
    threading.Thread(target=server, daemon=True).start()
    time.sleep(1)  # Wait for server to start

    # Step 3: Connect as client and send login
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 10000))

    # Send correct login
    s.sendall("LOGIN admin 1234".encode())
    response = s.recv(1024).decode()
    print(f"[Test1] Response to correct login: {response}")

    # Send incorrect login
    s.sendall("LOGIN admin wrongpass".encode())
    response2 = s.recv(1024).decode()
    print(f"[Test2] Response to wrong login: {response2}")

    # Send normal message
    s.sendall("Hello Server".encode())
    response3 = s.recv(1024).decode()
    print(f"[Test3] Response to message: {response3}")

    s.close()
    os.remove("users.txt")

if __name__ == "__main__":
    run_test()
