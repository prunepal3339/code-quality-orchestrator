def reverse_string(input_string):
    return input_string[::-1]

# get string input from the users
input_str = input("Enter a string: ")

# call function to reverse the string
reversed_str = reverse_string(input_str)

print(f"The reversed string is: {reversed_str}")
