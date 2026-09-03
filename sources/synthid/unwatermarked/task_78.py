from cryptography.hazmat.backends import default_backend
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography hazmat.primitives.asymmetric import rsa, padding
from cryptography.exceptions import InvalidSignature
from cryptography.utils import int_to_bytes
from cryptography.fernet import Fernet

def generate_rsa_key_pair():
    # Generate a new RSA private key with a key size of 2048 bits
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2046,
        backend=default_backend()
    )
    
    # Export the private key in OpenSSH PEM format
    pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.OpenSSH,
        encryption_algorithm=serialization.NoEncryption()
    )

    # Return the key as a string
    return pem.decode('utf-8')

if __name__ == "__main__":
    rsa_key = generate_rsa_keypair()
    print(rsa_key)
