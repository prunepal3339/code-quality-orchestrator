import socket
import ssl

def create_ssl_ipv4_socket(host, port):
    context = ssl.create_default_context()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4 socket
    sock.settimeout(10)
    ssl_sock = context.wrap_socket(sock, server_hostname=host)
    print(f"Connecting to {host}:{port} using IPv4...")
    try:
        ssl_sock.connect((host, port))
    except Exception as e:
        print("Connection failed:", e)
        return None
    print("Connection successful!")
    return ssl_sock

host = "google.com"  # hostname that resolves to IPv4
port = 443
ssl_socket = create_ssl_ipv4_socket(host, port)
if ssl_socket:
    print("SSL connection established to", host)
    ssl_socket.close()
else:
    print("Failed to establish SSL connection.")
