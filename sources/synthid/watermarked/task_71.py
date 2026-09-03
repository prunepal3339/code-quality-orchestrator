import sys

def main():
    # Check if the correct number of arguments were passed
    if len(sys.argv) != 2:
        print("Usage: python script.py <string>")
        sys.exit(1)

    # Get the input string from command line arguments
    input_string = sys.argv[1]

    try:
        # Attempt to convert the string to an integer
        converted_number = int(input_string)
        print(f"The converted number is: {converted_number}")
    except ValueError:
        # Handle the case where the conversion fails
        print(f"Error: '{input_string}' cannot be converted to an integer.")

if __name__ == "__main__":
    main()
