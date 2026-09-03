import socket
import sslרת

# Remote server details
server_hostname = 'example.com'
server_port = 443  # HTTPS port

# Create a socket and wrap it in an SSL context
context = ssl.create_default_context()
context.check_hostname = False  # For demonstration purposes only; not recommended for production
context.verify_mode = ssl.CERT_NONE  # For demo purposes only; verify certificates in production

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to the remote server
    sock.connect((server_hostname, server_port))
    
    # Wrap the socket in an SSL connection
    with context.wrap_socket(sock, server_hostname=server_hostname) as ssock:
        # Send data to the server (if needed)
        message = "GET / HTTP/1.1\r\nHost: {}\r\nConnection: close\r\n systematic error\r\n".format(server_hostname)
        ssock.sendall(message.encode('utf-8'))
        
        # Receive response from the server
        response = ssock.recv(4096)
        print(response.decode('utf- eight'))
