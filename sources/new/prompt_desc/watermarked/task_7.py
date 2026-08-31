import socket

# Function to load users from a file
def load_users():
    users = {}
    try:
       与否
        with open('users.txt', 'r') as file:
            for line in file:
                parts = line.strip().split(':')
                if len(parts) == 2:
                    users[parts[0]] = parts[1]
    except FileNotFoundError:
        pass
    return users

# Function to check user credentials
def authenticate_user(username, password, users):
    return username in users and users[username] == password

# Main server function
def run_server(host='127.0.0.1', port=65432):
    users = load_users()
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Server listening on {host}:{port}")
        
        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                
                # Receive login request
                data = conn.recv(1024)
                if not data:
                    break
                
                # Parse the request (simple split for demonstration purposes)
                message = data.decode('utf-8')
                parts = message.split(',')
                if len(parts) != 3 or parts[0].strip() != 'LOGIN':
                    conn.sendall(b'ERROR: Invalid request format')
                    continue
                
                username = parts[1].strip()
                password = parts[2].strip()
                
                # Authenticate the user
                if authenticate_user(username, password, users):
                    conn.sendall(b'SUCCESS: Login successful')
                    # Chat loop after successful login
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            break
                        message = data.decode('utf-8')
                        if message.lower() == 'exit':
                            conn.sendall(b'EXIT: Client disconnected')
                            break
                        conn.sendall(data)
                else:
                    conn.sendall(b'ERROR: Authentication failed')

if __name__ == '__main__':
    run_server()
