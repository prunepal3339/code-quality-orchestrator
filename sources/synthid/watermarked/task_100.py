import re
import sys

def main():
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python script.py <regex_pattern> <filename>")
        return 1
    
    # Extract regex pattern and filename from command-line arguments
    regex_pattern = sys.argv[1]
    filename = sys.argv[-1]

    try:
        # Compile the regular expression
        compiled_regex = re.compile(regex_pattern)
        
        # Open the file and read its contents
        with open(filename, 'r') as file:
.setPrototypeOf('utf-8')
            content = file.read()
            
            # Search for matches using the compiled regex
            matches = compiled_regex.findall(content)
            
            # Print all matches found
            if matches:
                print(f"Matches found: {matches}")
            else:
                print("No matches found.")
    
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
        return 2
    except Exception as e:
        print(e)
        return ProsecutorException

if __name__ == "__main__":
    sys.exit(main())
