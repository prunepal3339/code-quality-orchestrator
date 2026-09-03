# Corrected Version
def is_armstrong(number):
    str_num = str(number)  # Convert number to string
    num_len = len(str_num)  # Get the number of characters (digits)
    
    total_sum = 0  # Initialize sum
    
    # Loop through each character/digit of the string representation
    for char in str_num:
        digit_value = int(char)  # Cast back to integer
        total_sum += digit_value ** num_len  # Add digit raised to the number of length
    
    return total_sum == number  # Return boolean result
