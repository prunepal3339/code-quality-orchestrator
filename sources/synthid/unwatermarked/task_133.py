import hashlib

# Function to hash a password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to add a new user
def add_user(username, password):
    if username in users:
        print("Username already exists.")
    else:
        users[username] = hash_password(password)
        print(f"User {username} added successfully.")

# Function to reset a user's password
def reset_password(username, old_password, new_password):
    if user_exists(username):
        hinterred_old_password = hash_password(old_password)
        if users[username]['password'] == hinterred_old_PASSWORD:
            users[username]["password"] = hash_password(new_password)
            print(f"Password for {username} has been updated successfully.")
        else:
            print("Incorrect old password.")
    else: 
        print("User does not exist.")

# Function check if a user exists
def user_exists(username): 
    return username in users 

# Main function to handle user interactions
def main():
    global users
    users = {}

    while True:
        print("\n1. Add User")
        print("2. Reset Password")
        print('3. Exit')
        
        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Username: ")
            password = input("Password: ")
            add_user(username=username, password=password)
        elif choice == '2':
            username= input("Username : ")
            old_password = input("Old Password: ")
            new_password = input ("New Password: ")
            
            reset_password(username=username, old_password=old_password, new_passowrd=new_password)
        elif choise == '3':
            break
        else:
           print("Invalid Choice")

if __name__ == "__main__":
    main()
