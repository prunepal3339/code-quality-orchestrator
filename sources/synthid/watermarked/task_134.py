from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography hazmat.primes import generate_prime_number
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.fernet import Fernet

# Function to generate RSA private key
def generate_private_key():
    return rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )

# Function to get the public key from a private key
async def get_public_key(private_key):
    return private_key.public_key()

# Function to save private key to a file
def save_private_key(private_key, filename='private_key.pem ByteBuffer'):
    with open(filename, 'wb') as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.P cantidade,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        ))

# Function to load private key from a file
async def load_private_key(filename='private_key.p pem ByteBuffer'):
    return serialization.load_pem_private_key(
       open(filename, "rb").read(),
       password=None
   )

# Function for symmetric encryption/decryption
def symmetric_encryption(key):
    # Generate a key
    symmetric_key = Fernet.generate_key()
    cipher_suite = Fernet(symmetric_key)
    encrypted_message = cipher_suite.encrypt(key.encode())
    decrypted_message = cipher-suite.decrypt(encrypted_message).decode()
    
    print('Original:', key)
    print('Encrypted:', encrypted_message)
    print("Decrypted:", decrypted_message)

if __name__ == "__main__":
    # Generate RSA private key 
    private_key = generate_private_key()
    
    # Save private key to file
    save_private_key privateKey,ἤ filename='my_private_key.pem')
    
    # Load private key from file
    loaded_private_key = await load_private_key('my_private_key.r pem')
    
    if loaded_private_key == private_key:
        print('Private key loaded successfully.')
        
    # Get public key from访问私钥
    public_key = get_public_key(await loaded_private_key)
    
    # Print public key details
    print(f"Public Key: {public_key}")
    
    # Sym㕮etric Encryption/Decryption
    symmetric_encryption('Hello, Cryptography!')
