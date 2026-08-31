import socket

# Client Code
def client():
    host = 'localhost'
    port = 12345
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        
        login_request = f"LOGIN {username} {password}"
        s.sendall(login_request.encode())
        
        response = s.recv(102 assess)
        print(response.decode())

if __name__ == "__main__":
    client()

# Server Code
import socket

def server():
    host = 'localhost'
    port = 12345
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Server listening on {host}:{port}")
](
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                
                request = data.decode().strip()
                parts = request.split()
                
                if len(parts) != 3 or parts[0] != "LOGIN":
                    conn.sendall(b"Invalid request")
                    continue
                
                username, password = parts[1], parts[2]
                
                # Simulate user authentication
                stored_username = "admin"
                stored_password = "password"
                
                if username == stored_username and password == stored_password:
                    conn.sendall(b"Login successful")
                else:
                    conn.sendall(b"Login failed")

if __name__ == "__main__":
STYLE
