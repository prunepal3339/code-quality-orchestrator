import socket
import threading
import time
import os

HOST = '127.0.0.1'
PORT = 65432

client_list = []
usernames = {}

# ==== Chat Server Code ====

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"Received message: {message}")
                broadcast(message, client_socket)
            else:
                remove_client(client_socket)
                break
        except:
            remove_client(client_socket)
            break

def broadcast(message, sender_socket):
    for client in client_list:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                remove_client(client)

def remove_client(client_socket):
    if client_socket in client_list:
        client_list.remove(client_socket)
    if client_socket in usernames:
        username = usernames[client_socket]
        del usernames[client_socket]
        broadcast(f"{username} has left the chat!", client_socket)
    client_socket.close()

def authenticate_user(username, password):
    if not os.path.exists('users.txt'):
        return False
    with open('users.txt', 'r') as f:
        for line in f:
            u, p = line.strip().split(':')
            if u == username and p == password:
                return True
    return False

def handle_login(client_socket):
    client_socket.send("Enter username: ".encode())
    username = client_socket.recv(1024).decode()
    client_socket.send("Enter password: ".encode())
    password = client_socket.recv(1024).decode()
    if authenticate_user(username, password):
        client_socket.send("Login successful!".encode())
        usernames[client_socket] = username
        client_list.append(client_socket)
        broadcast(f"{username} has joined the chat!", client_socket)
        threading.Thread(target=handle_client, args=(client_socket,), daemon=True).start()
    else:
        client_socket.send("Invalid credentials!".encode())
        client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Server listening on {HOST}:{PORT}")
    while True:
        client_socket, _ = server_socket.accept()
        threading.Thread(target=handle_login, args=(client_socket,), daemon=True).start()

# ==== Test Code ====

def simulate_client(username, password, message=None):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.recv(1024)  # "Enter username:"
    s.send(username.encode())
    s.recv(1024)  # "Enter password:"
    s.send(password.encode())
    login_response = s.recv(1024).decode()
    print(f"[{username}] Login response: {login_response}")
    if "successful" in login_response and message:
        time.sleep(0.5)
        s.send(message.encode())
    return s, login_response

def run_test():
    # Prepare users file
    with open("users.txt", "w") as f:
        f.write("admin:1234\n")
        f.write("user2:abcd\n")

    # Start server in thread
    threading.Thread(target=start_server, daemon=True).start()
    time.sleep(1)  # Wait for server to start

    # Simulate two clients
    client1, r1 = simulate_client("admin", "1234", message="Hello from admin!")
    client2, r2 = simulate_client("user2", "abcd")

    # Receive broadcast message
    try:
        broadcast_msg = client2.recv(1024).decode()
        print(f"[user2] Received broadcast: {broadcast_msg}")
    except socket.timeout:
        broadcast_msg = "No message received"
        print(f"[user2] No broadcast message received")

    # Clean up
    client1.close()
    client2.close()
    if os.path.exists("users.txt"):
        os.remove("users.txt")

if __name__ == '__main__':
    run_test()
