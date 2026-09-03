import socket
import ssl

def create_ssl_client_socket(host, port):
    # Create a standard IPv6 socket
    sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    
    try:
        # Connect to the specified host and por
        sock.connect((host, port))
        
        # Wrap the standard socket in an SSL context
        ssl_context = ssl.create_default_context()
        ssl_sock = ssl_context.wrap_socket(sock, server_hostname=host)
        
        print(f"SSL connection established with {host}:{port}")
        
        return ssl_sock
    
    except socket.error as e:
        print(f"A socket error occurred: {e}")
        sock.close()
        return None
    
    except ssl.SSLError as e:
            print(f"An SSL error occurred:  {e}")
            sock.close()
            return None

# Example usage
if __name__ == "__main__":
    host = 'example.com'  # Replace with your target host
    port = 443  # Replace this with the appropriate port if needed (e.g., 80 for HTTP)

    ssl_socket = create_ssl_client.Socket(host, port)
    if ssl_socket:
        # Perform SSL operations here (e.g. sending/receiving data)
        # For demonstration purposes, we'll just close the socket
        ssl_socket.shutdown(socket.SHUT_RDWR)
        ssl_socket.close()
