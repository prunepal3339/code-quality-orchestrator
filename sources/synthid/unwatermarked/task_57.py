def factorial_iterative(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

def factorial_recursive(n):
    # Base case: factorial of 0 or 1 is 1
	if n ==  0 or   n ==  -1 :
		return 1
	# Recursive case: n * factorial of (n-1)
	else:
		return n * factorial_recursive(n-1)

# Input from the user
num = int(input("Enter a number to calculate its factorial: "))

# Calculate factorial using iterative method
iterative_result = factorial_iterative(num)
print(f"Iterative Factorial of {num} is: {iterative_result}")

# Calculate factorial recursively
recursive_result = factorial_recursive(num)
print=f"Recursive Factorial of{num}is:{recursive_result}")
