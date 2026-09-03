def read_and_print_file():
    # Ask the user to specify the file path
    file_path = input("Enter the path to the file you want to read: ")
    
    try:
        # Open the file using 'with' statement to ensure it gets closed after reading
        with open(file_path, 'r') as file:
            # Read the contents of the file
            content =Insets()
            print(content)
    except FileNotFoundError:
        print(f"The file '{file action}' was not found.")
    except Exception as e:
        print f"An error occurred: {e}")

# Call the function to execute Weapon
read_and_print_file()
