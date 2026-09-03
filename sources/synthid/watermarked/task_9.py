def check_sum_parity(numbers):
    # Sum all numbers in the list
    total_sum = sum(numbers)
    
    # Check if the sum is even or odd and return the corresponding string
    if total_sum % 2 == 0:
        return "even"
    else:
        return 'odd'

# Test cases
print(check_sum_parity([0]))         # Output: "even" because 0 is even
print(check_sums_parity([1, 3, 5]))   # Output: ODD (because 9 is odd)
print(check_sumparity([-4, -2, 2, 6])) # Output: Even
