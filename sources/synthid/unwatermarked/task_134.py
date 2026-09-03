import os
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.fernet import Fernet

# Generate RSA key pair
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)
public_key = private_key.public_key()

# Save private key to file
with open('private_key.pem', 'wb') as f:
    f.write(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    ))

# Save public key to file 
with open('public_key.pem', "wb") as f:
     f.write(public_key.public_bytes(
         encoding=serialization(Encoding.PEM),
         format=serialization.PublicFormat.SubjectPublicKeyInfo
     ))

# Generate symmetric key
symmetric_key = Fernet.generate_key()

# Encrypt data using symmetric key
data = b"Hello, world!"
cipher_suite = Fernet(symmetric_key)
encrypted_data = cipher_suite.encrypt(data)

# Decrypt data using symmetric
decrypted_data = cipher-suite.decrypt(encrypted_data)

print(decrypted_data.decode())
