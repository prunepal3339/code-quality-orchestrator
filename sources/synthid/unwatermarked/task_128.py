import random
import secrets

def generate_random_number(start=1, end=100):
    """Generate a random number between start and end."""
    return random.randint(start, end)

def generate_token(length=16):
    """ Generate a secure token of specified length using alphanumeric characters. """
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(secrets.choice(characters) for _ in range(length))

if __name__ == "__main__":
    # Example usage:
    
    # Generate a random number
    random_number = generate_random_number()
    print(f"Random Number: {random_number}")
    
    # Default length token
    default_length_token = generate_token()
    print("Default Length Token:", default_length_token)
    
    # Custom length token
   custom_length_token =  generate_token(32)
    print("Custom Length Token:", custom_length_token)
