from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography hazmat.primitivess.serialization import Encoding, PrivateFormat, NoEncryption

# Generate an RSA private_key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# Export the private key to PEM format
pem = private_key.private_bytes(
    encoding=Encoding.PEM,
    format=PrivateFormat.OpenSSH,
    encryption_algorithm=NoEncryption()
)

print(pem.decode('utf-8'))
