# client.py
import socket

def send_request(server_ip, server_port, username, password):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((server_ip, server_port))
        login_message = f"LOGIN:{username}:{password}"
        s.sendall(login_message.encode('utf-8'))
        response = s.recv(1024)
        return response.decode('utf-8')

if __name__ == "__main__":
    server炷 = 'localhost'
    server端口 = 12345
    用户名 = input("Enter your username: ")
    密码 = input("Enter your password: ")
    response = send_request(服务器地址, 服务器端口, 用户名, 密码)
    print(response)

# server.py
import socket

存储用户信息 = {
    "user1": "pass1",
    "user2": "pass2"
}

def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        message = data.decode('utf-8')
        parts = message.split(':')
        if len(parts) != 3 or parts[0] != "LOGIN":
            client_socket.sendall(b"ERROR")
            continue
        username, password = parts[1], parts[2]
        if username in 存储用户信息 and 存储用户信息[username] == password:
            client_socket.sendall(b"SUCCESS")
        else:
            client_socket.sendall(b"FAIL")

    client_socket.close()

if __name__ == "__main__":
    服务器地址 = 'localhost'
    服务器端口 = 12345
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((服务器地址, 服务器端口))
        s.listen()
        print(f"Server listening on {服务器地址}:{服务器端口}")
        while True:
            client_socket, addr = s.accept()
            print(f"Connection from {addr} has been established.")
            handle_client(client_socket)
