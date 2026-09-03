# Import necessary libraries from PyCryptodme
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import pad, unpad
from Crypto.Hash import SHA256
import base64

def encrypt_string(plain_text, password):
    # Generate a salt for key derivation
    salt = get_random_bytes(16)

    # Derive・・・
