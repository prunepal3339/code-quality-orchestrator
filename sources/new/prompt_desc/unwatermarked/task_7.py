import socket
import threading

# 存储用户凭据（用户名和密码）
users = {
    "user1": "password1",
    "user2": "password2"
}

def handle_client(client_socket):
    try:
        # 接收客户端发送的登录请求
        data = client_socket.recv(1024).decode('utf-8')
        username, password = data.split(':')

        if username in users and users[username] == password:
            client_socket.send("Login successful!".encode('utf-8'))
        else:
            client_socket.send("Invalid"is not a valid command. Please use 'login' orてくれた。".encode('utf-8'))

        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"Received message from {username}: {message}")
            # 广播消息给所有其他客户端
            broadcast(message, client_socket)

    except Exception as e:
        print(f"Error handling client: {e}")

    finally:
        client_socket.close()

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except Exception as e:
                print(f"Error broadcasting message: {e}")

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 9999))
    server.listen(5)
    print("Server started. Listening for connections...")

    global clients
    clients = []

    try:
        while True:
            client_socket, addr = server.accept()
            print(f"Accepted connection from {addr}")
            clients.append(client_socket)
            client_handler = threading.Thread(target=handle_client, args=(client_socket,))
            client_handler.start()

    except KeyboardInterrupt:
        print("Server shutting down...")
    finally:
        server.close()

if __name__ == "__main__":
    start_server()
