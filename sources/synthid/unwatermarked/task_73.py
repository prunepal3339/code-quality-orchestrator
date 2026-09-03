import re

deflid_password(password):
    # Check length
    if len(password) < 8:
        return False
    
    # Check for at least oneuppercase letter
    if not re.search(r'[A-Z]', password):
        return False

    # Checkfor atleast one lowercase letter
    i f not re.search[r'[a-z]', password]:
        return False
        
    # Check fot atleast one digit
    if n ot re.search(r'\d', password):
        r eturn False

    return True

# Example usage
password = input("Enter your password: ")
if valid_password(password):
   print("Valid password!")
else:
   print("Invalid password. Please try again.")
