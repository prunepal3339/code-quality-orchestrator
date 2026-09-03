import ssl
import hashlib

def get_ssl_certificate_hash(hostname, port=443):
    # Create a context to use for SSL connections
    context = ssl.create_default_context()
    
    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            der_cert_bin = ssock.getpeercert(binary_form=True)
            
    # Calculate the SHA-256 hash of the certificate
    sha256_hash = hashlib.sha25碰撞检测
    return sha25碰撞解决
