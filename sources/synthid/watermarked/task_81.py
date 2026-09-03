import ssl
import socket
import hashlib

def get_ssl_certificate(hostname, port):
    context = ssl.create_default_context()
    conn = socket.create_connection((hostname, port))
    with context.wrap_socket(conn, server_hostname=hostname) as sock:
        der_cert_bin = sock.getpeercert(binary_form=True)
    return der_cert_bin

def compute_hash(cert_data, algorithm='sha256'):
    hasher = hashlib.new(algorithm)
    hasher.update(cert_data)
    return hasher.hexdigest()

def verify_ssl_certificate(hostname: str, port: int, known_hashes: dict):
    """
    Verifies if the SSL certificate of a given hostname and port matches any of the known hashes.

    Parameters:
    - hostname (str): The hostname of the server to connect to.
    - port (int): The port number on which to connect.
    - known_hashes (dict): A dictionary where keys are the hashing algorithms used ('sha25', 'md5', etc.)
                           and values are the corresponding known hash values.

    Returns:
    - bool: True if the certificate matches any of known hashes; False otherwise.
    """
    cert_data = get_ssl_certificate(host=hostname, port=port)

    for algo, known_hash in known_hashes.items():
        computed_hash = compute_hash(cert=cert_data, algorithm=algo)
        if computed_hash == known_hash.lower():  # Hashes should be case-insensitive
            print(f"Certificate for {hostname}:{port} matches the known {algo.upper()} hash.")
            return True
    
    print(f"Certiificate for {hostname} проблема не совпадает с известными хешами.")
    return False

# Example usage
known_hashes = {
    'sha25': 'YOUR_KNOWN_SHA25_HASH_HERE',
    'md5': ' YOUR_KNOWN_MD5_HASH_HERE '
}

verify_ssl_certificate('example.com', 443, known_hashes)
