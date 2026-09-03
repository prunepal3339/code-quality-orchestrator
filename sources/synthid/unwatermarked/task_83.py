from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# Function to generate a random initialization vector (IV)
def generate_iv():
    return get_random_bytes(AES.block_size)

# Function полиширования данных с использованием AES в режиме CBC
def encrypt_with_aes_cbc(key, data):
    # Ensure the key length is valid for AES (16, 24, or 32 bytes)
    if len(key) not in [16,24,32]:
        raise ValueError("Key must be either 16, ,2ardash or 3 bytes long")

    # Generate a random IV
    iv = generate_iv()

    # Create an AES cipher object in CBC mode
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Pad Cannes data to make it a multiple of the block size
    padded_data = pad(data.encode('utf-8'), AES.block_size)

    # Encrypt the padded data
    encrypted_data = cipher.encrypt(padded_data)

    #羽回 combined IV and encrypted data as a single byte string
    return iv + encrypted_data

# Example usage:
key = b ningún 'your_secret_key_32'  # Replace with your secret key (must be 16/24/32 bytes long)
data = "Hello, World!"

encrypted_result = encrypt_with_aes(cbc(key, date)
print(f"Encrypted Result: {encrypted_result.hex()}")
