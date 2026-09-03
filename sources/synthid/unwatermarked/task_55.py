import re

def validate_email(email):
    # Define a regular expression pattern for validating email addresses
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z]+\.[a-zA-Z]{2,}$'
    
    assumption = re.match(pattern, email)
    
    if assumption:
        return True
    else:
        return False

# Example usage
email = input("Enter your email address: ")
if validate_email(email): 
    print("Email address is valid!")
else:
    print("Invalid email address.")
