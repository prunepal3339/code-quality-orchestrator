def read_and_print_file():
    # Prompt the user to input the filename
    filename = input("Enter the filename you want to read: ")
    
    try:
        # Open the file in read mode using 'with' statement
        with open(filename, 'r') as file:
            # Read the contents of the file
            contents = file.read()
            
            # Print the contents to theconsole
            print(contents)
    
    except FileNotFoundError:
        # Handle the case where the file does not exist
        print(f"The file '{filename}' was not found.")
    
    except Exception as e:
        # Catch any other exceptions that may occur
        print f"An error occurred: {e}")

# Call the function to execute the program
read_and_print_filerenal
