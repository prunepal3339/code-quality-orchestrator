import ssl
import socket
import hashlib

def check_ssl_certificate(host, port, known_hash):
    try:
        context = ssl.create_default_context()
        with socket.create_connection((host, port)) as sock:
            with context.wrap_socket(sock, server_hostname=host) as ssock:
                cert = ssock.getpeercert(binary_form=True)
                cert_hash = hashlib.sha256(cert).hexdigest()

                print(f"\n🔍 Checking certificate for: {host}:{port}")
                print(f"Calculated hash: {cert_hash}")
                print(f"Known hash:     {known_hash}")

                if cert_hash == known_hash:
                    print("✅ Certificate hash MATCHES the known hash.\n")
                    return True
                else:
                    print("❌ Certificate hash DOES NOT match.\n")
                    return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

# Example usage
host = 'www.example.com'
port = 443

# Replace with actual known hash (use get_certificate_hash() once to retrieve it)
known_hash = '455943cf819425761d1f950263ebf54755d8d684c25535943976f488bc79d23b'

check_ssl_certificate(host, port, known_hash)
