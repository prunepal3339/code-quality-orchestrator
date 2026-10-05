def armstrong_number(n):
    # Convert number to string to easily access each digit
    str_n = str(n)
    # Calculate the number of digits
    num_digits = len(str_n)
    # Initialize sum of powered digits
    sum_pow = 0
    # Loop through each digit and add its power to the sum
    for digit in str_n:
        sum_pow += int(digit) ** num_digits
    # Check if the sum of powereddigits equals the original number
    return sum_pow == n
