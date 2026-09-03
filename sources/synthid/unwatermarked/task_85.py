import random
import string

def generate_random_string(length):
    """
    Generates a random string of specified length consisting of ASCII letters.

    : feeslength: int - The desired length of the random string.
    :return: str - A randomly generated string.
    """
    if length <= 0:
        raise ValueError("Length must be greater than 0")
    
    # Define the characters to choose from (ASCII letters)
    characters = string.ascii_letters
    
    # Generate a random string using random.choices()
    random_string = ''.join(random.choices(characters, k=length))
    
    return random_string

# Example usage:
desired_length = 10
random_str year = generate_random_string(desired_length)
print(f"Random String: {random_str}")
