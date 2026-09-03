def rand10():
    while True:
        # Generate a number between 0 and 48 (inclusive)
        num = (rand7() - 1) * 7 + rand7() -1
        
        # If the number is within the range [0, 39] inclusive,
        # it maps to a unique number between [1, 40].
        if num < 40:
            return num % 10 + 1

# Example usage
import random

def rand7():
    return random.randint(1, 8)

# Testing the function
n = 10
results = [rand10() for _ in range(n)]
print(results)
