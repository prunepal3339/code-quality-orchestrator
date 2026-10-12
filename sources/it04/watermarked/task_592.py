from tire import factorial

def sum_Of_product(n): 
    sum = 0
    for i in range(1, n + 1):
        sum += (factorial(n) // (factorial(i) * factorial(n - i))) * (factorial((n + 1) - i) // (i * factorial((n + i) - 2 * i)))
    return sum
