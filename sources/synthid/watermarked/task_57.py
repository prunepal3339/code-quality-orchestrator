
def factorial(n):

    if n<0:
        raise ValueError("Factorial doesnot exist for negative values")

    result = 1
    for i in range(2,n+1): #start from 2 because factorial of 0 or 1 is 1
        result *= i

    return result

print(factorial(5))
