import ssl
import socket

def create_ssl_connection(host, port):
    try:
        context = ssl.create_default_context()
        with socket.create_connection((host, port)) as sock:
            with context.wrap_socket(sock, server_hostname=host) as secure_sock:
                print(f"Connected to {host}:{port} successfully!")
                print(f"SSL version: {secure_sock.version()}")
                print(f"Cipher: {secure_sock.cipher()}")
                cert = secure_sock.getpeercert()
                print(f"Certificate: {cert}")
    except Exception as e:
        print(f"Failed to connect to {host}:{port}. Error: {e}")

if __name__ == "__main__":
    create_ssl_connection("www.google.com", 443)
