def check_pangram(input_string):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    input_set = set(input_string.lower())
    return alphabet <= input_set

# Test the function
print(check_pangram("The quick brownfox jumps over thelazy dog"))  # should return True
