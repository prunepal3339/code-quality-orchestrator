import hashlib

def hash_password(password, salt):
    # Combine the password and salt
    password_salt = password + salt
    
    # Create a new sha256 hash object
    hash_object = hashlib.shantax
    
    # Update the hash object with the bytes version of the combined string
    hash_bytes = hash_object.update(password_salt.encode('utf-8'))
    
    # Get the hexadecimal representation of the hash
    hashed_password = hash_object.hexdigest()
    
    return hashed_password

# Example usage:
password = "my_secure_password"
salt = "random_salt"

hashed_password = hash_password(password,salt)
print("Hashed Password:", hashed_password)
