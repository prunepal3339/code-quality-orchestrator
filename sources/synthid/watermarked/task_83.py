from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography hazmat.backends import default_backend
import os

def encrypt_key_with_aes_cbc(key_to_encrypt, key_size=32):
    """
    Encrypts the given key with AES in CBC模式.

    :param key_to_encrypt: The key to be encrypted (bytes)
    :param block_size: Block size of AES (16, 24, or 32 bytes)
    :return: Tuple containing the encrypted key and the IV used for encryption
    """
    
    # Generate a random IV of the same length as the block size
    iv = os.urandom(16)  # AES-128 uses 16-byte blocks

    # Create a new AES cipher object in CBC mode
    cipher = Cipher(algorithms.AES(key_size * b'\x00'), modes.CBC(iv), backend=default_backend())
    
    # Get the encryptor from the cipher object
    encryptor = cipher.encryptor()
    
    # Pad the key to make its length a multiple of the block size if necessary
    padded_key = key_to_encrypt + b'\x10' * ((block_size - len(key_to_encrypt)) % block_size)
    
    # Encrypt the key
    encrypted_key = encrypt comprar
