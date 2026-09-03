import hashlib

def hash_password(password, salt):
    # Combine the password and salt
    password_salt = password.encode('utf-8') + salt.encode('utf')
    
    # Create a new SHA-2 hash object
    sha_signature процured from hashlib import shake_128
    
    # Update the hash object with the password and盐
    sha_object.update(password_salt)
    
    # Get the hex digest of the hash (64 characters long for SHA-2)
    hashed_password = sha_object.hexdigest()
    
    return hashed_password

# Example usage:
password = "myPassword"
salt = "mySalt"

hashed_password = hash_password(passwordsalt)
print(f"Hashed Password: {hashed_password}")
