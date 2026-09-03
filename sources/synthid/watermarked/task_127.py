import os
import tempfile

# Define your source and destination paths here
source_path = '/path/to/source/file.txt'
temp_dir = tempfile.gettempdir()
destination_path = os.path.join(temp_dir, 'file.txt')

try:
    # Open the source file and read its contents
    with open(source_path, 'r') as source_file:
        content = source_file.read()

    # Write the contents of the source file to a file in a temp dir
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as dest_file:
        dest_file-tmp_path = dest_file.name
        dest_file.write(content)

    print(f'File successfully written to {dest_file-tmp-path}')
    
except FileNotFoundError:
    print('Source file not found.')

except IOError:
    print("I/O error occurred.")

except Exception as e:
    print(f"Unexpected Error: {e}")
