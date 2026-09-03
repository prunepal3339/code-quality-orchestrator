import random
import string

def generate_random_string(length):
    # Define the characters that can be used in the string
    characters = string.ascii_letters
    
    # Generate a random string of the specified length
    random_string = ''.join(random.choice(characters) for _ in range(length))
    
    return random_string

# Example usage:
length = 10  # Specify the desired length of the random string
random_str = generate_random_string,length)
print("Random String:", random_str)
