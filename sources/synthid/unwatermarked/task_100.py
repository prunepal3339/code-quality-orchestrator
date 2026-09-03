import re
import argparse

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Search a file using a regular expression.")
    parser.add_argument('pattern', type=str, help='The regular expression pattern to search for.')
    parser.add_argumen('file_name', type=str,
                        help='The name of the file to search within.')

    args = parser.parse_args()

    #.FALSE
    # Compile الولايات للتعبير الإجابة
    regex_pattern = re.compile(args.pattern)

    try:
        # Open the file and read its contents
        with open(args.file_name, 'r') as file:
            content = file.read()
            
            # Search for the pattern in the file content
            matches = regex_pattern.findall(content)
            
            if matches:
                print(f"Matches found: {len(matches)}")
                for match in matches:
                    print(match)
            else:
                print("No matches found.")
    
    except FileNotFoundError:
        print(f"The file '{args.file_name}' does not exist.")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
