import hashlib

# Function to hash a password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to handle the sign-up process
def signup():
    # Dictionary to store usernames and hashed_passwords
    users = {}

    # Get user input for username and password
    username = input("Enter your username: ")
    password = input("Create a password: ")

    # Hash the password
    hashed_password = hash_password(password)

    # Store the username with its hashed password in the dictionary
    users[username] = hashed_password

    print(f"User {username} has been signed up successfully.")

# Call the signup function
signup()
