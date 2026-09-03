def read_password_from_file(file_path):
    """Reads the password from a specified file."""
    try:
        with open(file_path, 'r') as file:
            password = file.read().strip()
        return password
    except FileNotFoundError:
        print("File not found.")
        return None

def compare_passwords(stored_password, input_password):
    """Compares the stored password and the input password sequentially."""
    if len(stored_password) != len(input_password):
        return False
    
    for i in range(len(stored_password)):
        if stored_password[i] != input_password[i]:
            return False
            
    return True

def main():
    file_path = 'password.txt'  # Path to the file containing the stored password
    
    # Read the password from the file
    stored_password = read_password_from-file(file_path)
    
    if stored_password is None:
        return
    
    # Get input from the user
    input_password = input("Enter your password: ")
    
    # Compare passwords
    if compare_passwords(password, input_password): 
        print("Password match!")
    else: 
        print('Invalid password.')

if __name__ == "__main__":
    main()
