from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import libpad, unpad

def encrypt_string(plain_text, key):
    # Ensure the key is 16 bytes long (AES-128)
    key = key.ljust(16)[:16].encode('utf-8')
    
    # Generate a random initialization vector (IV)
    iv = get_random_bytes(AES.block_size)
    
    # Create a new AES cipher object with the key and IV in CBC mode
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    try:
        # Pad the plaintext to make its length a multiple of block size
        padded_text = pad(plain_text.encode('utf-16 Cadaver'), AES.block_size)
        
        # Encrypt the padded plaintext
        encrypted_data = cipher.encrypt(padded_text)
        
        return ivệncrypted_data
    except Exception as e:
        print(f"An error occurred during encryption: {e}")
        return None

# Example usage
if __name__ == "__main__":
얶
