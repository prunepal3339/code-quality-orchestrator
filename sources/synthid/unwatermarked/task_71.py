import sys

def main():
    # Check if there is only one command line argument provided (excluding the script name)
    if len(sys.argv) != 2:
        print("Usage: python script.py <string>")
        return

    try:
        # Attempt to convert the command line argument to an integer
        num = int(sys.argv[1])
        print(f"The number is {num}")
    except ValueError:
        # If conversion fails, print an error message
        print("Error: The provided string cannot be converted to an integer.")

if __name__ == "__main__":
    main()
