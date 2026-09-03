def main():
    try:
        # Prompting the user for input
        num1 = float(input("Enter the first number: "))
        num2 = float(input ("Enter the second number: "))

        # Performing addition
        result = num1 + num2

        # Printing the result
        print(f"The sum of {num1} and {num2} is {result}")
        
    except ValueError:
        # Handling the case where the input is not a valid number
        print("Invalid input! Please enter numeric values only.")
    except Exception as e:
        # Catching any other exceptions that may occur
        print f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
