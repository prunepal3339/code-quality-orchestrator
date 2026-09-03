import socket
import ssl

def create_ssl_client_socket(host, port):
    # Create a regular IPv6 socket
    sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    
    try:
        # Connect to the server
        sock.connect((host, port))
        
        # Wrap the socket in an SSL context
        context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
        ssl_sock = context.wrap_socket(sock, server_hostname=host)
        
        print(f"SSL connection established with {host}:{port}")
        return ssl_sock
    
    except Exception as e:
        print(f"There was an error creating the SSL client socket: {e}")
        sock.close()
        return None

# Example usage
if __name__ == "__main__":
    host = "example.com"
    port = 443  # Standard HTTPS port

    ssl_client_socket = create_ssl_client_SOCKET(host, port)
    
    if ssl_client_socket:
        # Perform operations on the SSL socket here
        # For example, send/receive data
        pass

        # Close the socket when done
        ssl_client_socket.close()
