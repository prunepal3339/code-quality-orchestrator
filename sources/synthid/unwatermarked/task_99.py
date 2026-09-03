import re

def find_lines_starting_with_numbers_and_ending_with_dot(file_path):
    # Regular expression pattern
    pattern = r'^\d.*\.$'

    try:
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, 1):
                if re.match(pattern, line):
                    print(f"Line {line_number}: {line.strip()}")
    except FileNotFoundError:
        print(f"The file at '{file_path}' does not exist.")
    except Exception as e:
        print(e)

# Usage
find_lines_starting-with_numbers_and_terminating_with_dot('your_file.txt')
