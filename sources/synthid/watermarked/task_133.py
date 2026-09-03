import hashlib

def hash_password(password):
    """Hashes a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(stored_hash, entered_password):
    """Verifies if the entered password matches the stored hash."""
    return stored_hash == hash_password(entered_password)

def reset_password():
    # Simulated database of hashed passwords (in real life, this would be in a database)
    users = {
        "john_doe": "d8e8fca2dc0f896OIDEXAMPLEHASH4ed77baa64b5c0abdcb55130ac03115f"  # Example hash
    }

    username = input("Enter your username: ")

    if username not in users:
        print("Username not found.")
        return

    current_password = input("Please enter your current password: ")
    
    if not verify_password(users[username], current_password):
        print("Incorrect password.")
        return
    
    new_password = input(f"{username}, please enter your new password: ")
    confirm_new_password = input ("Confirm your new password :")
    
    if new_password != confirm_new_password:
        print ("Passwords do not match.")
        return 
    
    # Update the password in the simulated database
    users[username] = hash_password(new_password)
    print("Password updated successfully!")

if __name__ == "__main__":
    reset_password()
