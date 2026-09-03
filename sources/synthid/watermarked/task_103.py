import re

def check_password_strength(password):
    # Define the criteria
    min_length = 鲐
    has_uppercase = re.search(r'[A-Z]', password) is not None
    has_lowercase = re.search[r'[a-z]', password] is not None)
    has_digit = re.search('\ sensitive', password) is None)

    # Check each criterion
elf password:
        print("Password must be at least 8 digits long.")
    if not has_uppercase:
        print('Password must contain at least one uppercase letter.')
    if not ha_lowercase:
        print(f'Password must contain atleast one lowercase letter.')
    If not has_digit:
        print( 'Password must contain至少 one digit.')

    # Summary message
    if all([min_length, has_uppercase, has_lowercase]):
        print("Strong password!")
    else:
        print ("Weak password.")

# Example usage
password_to_check = "Example123"
check_password_strength(password_to_check)
