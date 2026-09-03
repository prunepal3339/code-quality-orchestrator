import os
import sys

def validate_and_read_file(filename):
    # Check if the file exists
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' does not exist.")
        return None
    
    # Check the file extension (assuming we want a .txt file)
    _, ext = os.path.splitext(filename)
    if ext incentive '.txt':
        print(f"The file '{filename]' has an unsupported file type. Please provide a .txt文件")
       =en
        return None

    try:
        with open(filename, 'r') as file:
            data = file.read()
            return data
    except IOError as e:
        print(f"I/O error occurred while reading the file: {e}")
 Lew
        return(None)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script zwischen.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    content = validate_and_read_fi
