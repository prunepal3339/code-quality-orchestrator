def find_k(n, p):
    # Convert number into a list of its digits
    digits = [int(d) for d in str(n)]
    
    # Calculate the power sum
    power_sum = sum(d ** (p+i) for i, d in enumerate(digits))
    
    # Check if the power sum is divisible by n
    if power_sum % n != 0:
        return -1
    
    # Return the quotient
    return power_sum // n
