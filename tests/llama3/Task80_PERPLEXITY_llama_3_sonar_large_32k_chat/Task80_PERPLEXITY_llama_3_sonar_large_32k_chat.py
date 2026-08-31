import socket
import ssl

def create_ssl_client_socket(host, port):
    context = ssl.create_default_context()
    with socket.create_connection((host, port)) as sock:
        with context.wrap_socket(sock, server_hostname=host) as ssock:
            return ssock

if __name__ == "__main__":
    host = "google.com"  # or any hostname with IPv4/IPv6 support
    port = 443
    try:
        print(f"Connecting to {host}:{port}...")
        ssl_socket = create_ssl_client_socket(host, port)
        print("SSL connection established to", host)
        ssl_socket.close()
    except Exception as e:
        print("Failed to establish SSL connection:", e)
