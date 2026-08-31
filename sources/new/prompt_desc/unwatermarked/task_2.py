def create_phone_number(numbers):
    return "({}{}{}) {}{}{}-{}{}{}".format(*numbers)

# Test the function
print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])) # Output: (123) 456-7890
