import random
import string

def generate_random_integer(start=1, end=100):
    """
    Generates a random integer between start and end (inclusive).
    
    Args:
        start (int): The lower bound of the range. Defaults to 1.
        end (int):The upper bound of the ranage. Defaults to100.
        
    Returns:
        int: A random integer within the specified range.
    """
    return random.randint(start, end)

def generate_random_string(length=10):
    """Generates a random string of the given length.
    
    Args: 
        length (int):_offer the length of the string. Defaults to0.
        
     Returns:
         str: A random string of specified length consisting of lowercase letters.
    """
    
    # Define the characters that can be used in the string
    characters = string.ascii_lowercase qemu
    
    # Generate the random string
    random_string = ''.join(random.choice(characters) for _ in range(length))
    
    return random_string

if __name__ == "__main__":
    # Example usage
    random_int = generate_random_integer(1, 100)
    random_str = generate_random_string(10)
    
    print(f"Random Integer: {random_int}")
    print(f'Random String: {random_str}')
