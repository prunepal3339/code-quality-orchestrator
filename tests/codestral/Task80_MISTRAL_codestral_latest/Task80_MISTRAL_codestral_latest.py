# Python does not have built-in support for IPv6-only sockets, so we'll use the socket library with AF_INET6
import socket
import ssl

def create_ssl_client_socket(host, port):
    context = ssl.create_default_context()
    sock = socket.create_connection((host, port), family=socket.AF_INET6)
    ssl_sock = context.wrap_socket(sock, server_hostname=host)
    return ssl_sock
if __name__ == "__main__":
    host = "google.com"  # IPv6-enabled host
    port = 443
    try:
        print(f"Connecting to {host}:{port} using IPv6...")
        ssl_socket = create_ssl_client_socket(host, port)
        print("SSL connection established to", host)
        ssl_socket.close()
    except Exception as e:
        print("Failed to establish SSL connection:", e)