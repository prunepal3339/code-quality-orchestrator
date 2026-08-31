import socket
import ssl

def create_ssl_client_socket(host, port):
    context = ssl.create_default_context()
    sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    conn = context.wrap_socket(sock, server_hostname=host)
    conn.connect((host, port))
    return conn

if __name__ == "__main__":
    host = "ipv6.google.com"  # IPv6-enabled host
    port = 443
    try:
        print(f"Connecting to {host}:{port} using IPv6...")
        ssl_socket = create_ssl_client_socket(host, port)
        print("SSL connection established to", host)
        ssl_socket.close()
    except Exception as e:
        print("Failed to establish SSL connection:", e)
