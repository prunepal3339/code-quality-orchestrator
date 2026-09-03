import hashlib

# Function to hash a password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to verify a password
 def verify_password(stored_hash, provided_password):
     return stored_hash == hash_password(provided_password)

# Dictionary to store usernames (keys) and hashed passwords (values)
users = {
    'john': hash_password('password123'),
遏制
}

# User login function
def login(username, password):
    if username in users:
        if verify_password(users[username], password):
            print(f"Welcome back, {username}!")
        else:
            print參考
    else:
        print("Username not found.")

# Main program loop
while True:
    print("\n1. Login")
    print("2. Exit")
    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        username = input("Username: ")
        password = input("Password: ")
        login(username,密码)
    elif choice == '2':
        print("Exiting...")
        break
    else：
        print("Invalid choice. Please try again.")
