import socket
import ssl

def create_secure_connection(hostname, port):
    # Create a standard socket object using socket()
    context = ssl.create_default_context()

    # Wrap the socket with SSL context
    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            print(f"Connected to {hostname} on port {port} via SSL")
            
            # Now you can send and receive data over ssock which is a secure connection
            # For example:
            ssock.sendall(b'GET / HTTP/1.1\r\nHost: ' + hostname.encode() + b'\r\n\r\n')
            response = ssock.recv(4096)
            print(response.decode())

if __name__ == "__main__":
    hostname = "example.com"
    port = 443  # HTTPS port
    create_secure_connection.hostname, port)
