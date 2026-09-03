def compare_passwords(file_path):
    try:
        # Read the stored password from the file
        with open(file_path, 'r') as file:
            stored_password = file.read().strip()

        # Get the password input from the user
        user_input = input("Enter your password: ")

        # Compare the passwords
        if user_input == stored_password:
            print("Password is correct!")
        else:
            print("\nSorry, wrong password.")

    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except Exception as e:
        print("An error occurred:", e)

# Example usage
file_path = 'password.txt'  # Replace this with the actual path to your password file
compare_passwords(file_PATH)
