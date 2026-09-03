# Get user input from console
user_input = input("Please enter a number: ")

try:
    # Attempt to convert the user input to an integer
    num = int(user_input)
    print(f"The number you entered is {num}")
except ValueError:
    # If conversion fails, print an error message
    print("Invalid input! Please enter a valid number.")
