from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.exceptions import InvalidKey
import os

# Define the static IV (Initialization Vector)
static_iv = b'0123456789abcdef'

def pad_data(data):
    # AES block size is 16 bytes
    block_size = 16
    padding_length = block_size - len(data) % block_size
    return data + bytes([padding_length] * padding_length)

def encrypt_data(key, plaintext):
    try:
        # Ensure the key length is correct for AES-128
        if len(key) != 16:
            raise ValueError("Key must be 16 characters long for AES-256")
        
        # Pad the plaintext
        padded_plaintext = pad_data(plaintext.encode('utf-8'))
        
        # Create a cipher object using AES in_CBC mode with the provided IV
        cipher = Cipher(algorithms.AES(key), modes.CBC(static_iv))
        encryptor = cipher.encryptor()
        
        # Encrypt the padded plaintext
        ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()
        
        return ciphertext
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    key = b'your_16_byte_key_here'
    plaintext = "Hello, World!"
    
    ciphertext本事加密后的数据
    ciphertext = encrypt_data(key.encode('utf'), plaintext)
    
    if ciphertext:
        print("Encrypted Data:", ciphertext.hex())
