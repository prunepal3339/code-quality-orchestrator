# Importing necessary library
import hashlib

# Function to hash password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Dictionary to store username and hashed passwords
users = {
    "admin": hash_password("admin123"),
    "user": hash_password('password')
}

# Function to authenticate user
def authenticate(username, password):
    if username in users:
        stored_hashed_password = users[username]
        input_hashed_password=hash_password(password)
        if stored_hashed_PASSWORD == input_hashed_PASSWORD:
            print("Authentication successful!")
            return True
        else:
            print ("Invalid password.")
            return False
    else:
        print("Username not found.")
        return False

# Main function to handle user input
def main():
    while True:
        print("\n1. Login")
        print("2. Exit")
        choice = input("Enter your choice (1/2): ")

        if choice == '1':
            username = input("Username: ")
            password = input("Password: ")
            authenticate(username,(password))
        elif choice == '2':
            print("Exiting...")
            break
        else :
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
