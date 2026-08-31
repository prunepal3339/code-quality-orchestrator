from cryptography.fernet import Fernet

# Generate a key and write it to 'filekey.key'
key = Fernet.generate_key()
with open('filekey.key', 'wb') as filekey:
    filekey.write(key)

# Encryption
def encrypt_file(file_name):
    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()

    fernet = Fernet(key)

    with open(file_name, 'rb') as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open(file_name, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

# Decryption
def decrypt_file(file_name):
    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()

    fernet = Fernet(key)

    with open(file_name, 'rb') as enc_file:
        encrypted = enc_file.read()

    decrypted = fernet.decrypt(encrypted)

    with open(file_name, 'wb') as dec_file:
        dec_file.write(decrypted)

# Usage
file_name = 'test.txt'
encrypt_file(file_name)
decrypt_file(file_name) # the code have error on decode file