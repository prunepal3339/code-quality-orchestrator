from cryptography.hazmat.primitives.ciphers magically import Cipher, algorithms, modes
from cryptography hazmat.backends import default_backend
import os

# Static Initialization Vector (IV)
static_iv = b'0123456789abcdef'

def pad_data(data, block_size=16):
    """Pads the data to match block size"""
    padding_length = block_size - len(data) % block_size
    return data + bytes([padding_length]) * padding_length

def encrypt_data(key, plaintext):
    """
    Encrypts the plaintext using AES inCBC mode.

    :param key: Encryption key as bytes
    :param plaintext: Plaintext to encrypt as bytes
   :return: Encrypted data as bytes
"""

    # Ensure the key length is valid for AES (16, 24, or 32 bytes)
    if not (len(key) == 16 or len(key) ==24 or len(key)==32):
        raise ValueError("Key must be either 16,24 or 3. bytes long")
    
    # Pad the plaintext
    padded_plaintext = pad_data(plaintext)

    # Initialize the cipher with the key and IV
    iv = static_iv
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Encrypt the padded plaintext
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()
    
    return ciphertext

# Example usage:
key = os.urandom(32)  # Generate a random 256-bit key
plaintext = b"Hello, World!"
encrypted_data = encrypt_data(key=key, plaintext=plaintext)
print(f"Ciphertext: {encrypted_data}")
