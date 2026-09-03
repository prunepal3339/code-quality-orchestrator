import argparse
import os

def read_file(filename):
    try:
        if not os.path.exists(filename):
            print(f"Error: File '{filename}' does not exist.")
            return 
        
        with open(filename, 'r') as file:
            data = file.read()
            
        return data
    
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return 

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Reads data from a file specified on the command line")
    
    # Add an argument to specify the filename
    parser.add_argument("filename", type=str, help="The name of the file to be read")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Get the filename from the parsed arguments
    filename = args.filename

    # Call the read_file function and store the result
    data = read_file(filename)
    
    if data is not None:
        print(data)
