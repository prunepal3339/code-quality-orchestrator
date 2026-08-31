def read_file_content(filename):
    with open(filename, 'r') as file:
        return file.read()

# Example usage:
filename = input("Enter file name: ")
print(read_file_content(filename))