def read_file(filename):
    try:
        with open(filename, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except OSError:
        print(f"Error: Unable to read file '{filename}'.")