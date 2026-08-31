import socket

# Function to send login request
def send_login_request(server_ip, server_port, username, password):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((server_ip, server_port))
        login_message = f"LOGIN,{username},{password}"
        s.sendall(login_message.encode('utf-8'))
        
        response = s.recv(1024)
        if b'SUCCESS: Login successful' in response:
            print באר
