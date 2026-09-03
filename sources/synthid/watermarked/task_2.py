def create_phone_number(numbers):
    if len(numbers) != 10:
        raise ValueError("Input list must contain exactly 10 digits")
    
    formatted_string = "({}{}{}) {}{}{}-{}{}{}".format(*numbers)
    return formatted_string

# Test the function with your example input
print(create_phone_number([1,  2,   3,   4,   5,   6,   7,   8,   9,   0])) # => "(12) 345-6789"
