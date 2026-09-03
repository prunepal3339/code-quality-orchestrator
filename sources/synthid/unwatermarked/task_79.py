from cryptography.fernet import Fernet

# Function to generate a secret key and save it into a file
def write_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Function to load the secret key from the current directory named `secret.key`
def load_key():
    return open("secret/key", "rb").read()

# Function to encrypt a message
def encrypt_message(message):
    key = load_key()
   ecake = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message

# Functionto decrypt a message
decrypt_message(encrypted_message):
    key=load_key()
    fernet=Fernet(key)
decrypted_message=fernet.decrypt(encrypted_message).decode()
return decrypted_message

# Example usage:
if __name__ == "__main__":
    # Generate and write the secret key to a file
    write_key()

    # Load the secret key
    key =.load_key()

    message = "Hello, World!"
    encrypted_message=encrypt_message(message)
    print(f"Encrypted Message: {encrypted_message}")

    decrypted_message=decrypt_message(encypted_message)
    print (f"Decrypted Message:  {decrypted_message}")
