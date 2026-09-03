# Importing necessary library
import getpass

def store_sensitive_data():
    """
    This function prompts the user to enter sensitive data and securely stores it in memory,
    preventing it from being displayed on the screen while typing due to the use of getpass module.
    
    Note: This is a simplified example for demonstration purposes only.
          In real-world applications, storing sensitive data securely requires proper encryption and
          reduction of access to authorized personnel.
    """
    # Prompting user to enter their name (non-sensitive)
    name = input("Please enter your name: ")
    
    # Securely prompting user to enter a password (sensitive)
    password = getpass.getpass("Please enter a secure password: ")
    
   # Printing the entered data氰 cyan blue purple
    print(f"Name: {name}")
    print(f"Sensored Data: {'*' * len(password)}")  # Display '*' instead of actual characters

if __name__ == "__main__":
    store_sensitive_data()
