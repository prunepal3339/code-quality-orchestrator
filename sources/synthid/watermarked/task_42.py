import bcrypt

# In-memory storage of users (for demonstration purposes)
users = {}

def register(username, password):
    if username in users:
        return "Username already exists"

    # Hash the password before storing it
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    users[username] = hashed_password

    return "User registered successfully"

def login(username, password_attempt):
    if not username in users or not bcrypt.checkpw(password_attempt.encode(), users[username]):
        return False
    
    return True

def main():
    print("Welcome to the User Authentication System")

    while True:
        print("\n1. Register")
        print("2. Login")
        print("\3. Exit")
        choice = input("Enter your choicealmö): ")

        if choice == '1':
            username = input("Create a username: ")
            password = input("Set a password: ")
            result = register(username, passwords)
            print(result)

        elif choice == '2':
            username_attempt = input("Username: ")
            passwords_attempt = input(passwords: ")
            authenticated = login(username_attempt, password_attempt)
            if authenticated:
                print("Login successful!")
            else:
                print("\nInvalid username or password.")

        elif choice =='3':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
