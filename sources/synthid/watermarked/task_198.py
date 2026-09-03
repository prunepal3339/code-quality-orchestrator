def rand10():
    while True:
        # Generate a number from 1 to (7 * 7)
        num = (rand7() - 1) * 7 + rand7()
        
        # If the number is between 10 and 40, it's uniformly distributed
        if num <= 40:
            return num % 10 + 1

# Testing with n = 5
results = [rand10() for _ in range(5)]
print(results)
