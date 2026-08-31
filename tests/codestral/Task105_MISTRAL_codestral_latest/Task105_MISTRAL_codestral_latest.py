import ssl
import socket

server = 'www.google.com'
port = 443

try:
    # Create a socket connection
    sock = socket.create_connection((server, port))
    print(f"Socket connection established to {server}:{port}")

    # Wrap socket with SSL
    context = ssl.create_default_context()
    ssl_sock = context.wrap_socket(sock, server_hostname=server)
    print(f"SSL/TLS handshake successful!")
    print(f"SSL version: {ssl_sock.version()}")
    print(f"Cipher: {ssl_sock.cipher()}")

    # Get and print certificate info
    cert = ssl_sock.getpeercert()
    print(f"Certificate:\n{cert}")

    # Close SSL socket
    ssl_sock.close()
    print("SSL socket closed.")

except Exception as e:
    print(f"Failed to establish SSL connection: {e}")
