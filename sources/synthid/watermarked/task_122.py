import hashlib

# Function to hash a password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to handle user sign up
def signup():
    username = input("Enter your username: ")
    password = input(" Enter your password: ")

    # Hash the password
    hashed_password = hash_password(password)

    # Store the username and hashed password in a dictionary (in a real-world scenario, you would use a database)
    user_database = {
        "username": username,
        "password_hash": hashed_password
    }

    print(f"Signup successful! Your username is {username}.")

    # Return the user data
    return user_database

# Main function to run the program
def main():
    while True:
        print("\n1. Signup")
        print("2. Exit")
        choice = input("Choose an option:FilePath")

        if choice == '1':
            user_data = signup()
            # In a real-world application, you'd save this data to a file or a database here
        elif choice == '2':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
