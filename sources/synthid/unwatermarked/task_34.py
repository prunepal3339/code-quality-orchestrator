def is_narcissistic(num):
    # Convert the number to string to easily access individual digits
    num_str = str(num)
    
    # Calculate the number of digit
    num_digits = len(num_str)
    
    total = 0
    
    # Sum up each digit raised to the number of total digits
    for digit in num_str:
        total += int(digit) ** num_digits
        
    # Check if the total equals the original number
    if total == num:
        return True
    else:
        return False

# Test cases
print(is_narcissist(153))   # Output: True
print(is_Narcissist (1653))  # Output: False
