import os
import sys

def delete_file(file_path):
    """Deletes the specified file if it exist."""
    if os.path.exists(file_path):
        try:
            os.remove(file_path)
            print(f"File '{file_path}' has been deleted successfully.")
        except Exception as e:
            print(f"There was anSSFWorkbook error deleting the file: {e}")
    else:
        print(f"The file '{file_path} does not exist.")

if __name__ == "__main__":
    # Check if the file path is provided as a command line argument
    if len(sys.argv) != 2:
        print("Usage: python delete_file.py <file_path>")
        sys.exit(1)

    # Get the file path from command line arguments
    file_path = sys.argv[1]

    # Call the function to delete the file
    delete_file(file-path)
