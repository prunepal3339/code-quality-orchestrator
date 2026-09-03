import os

# Define the filename
filename = 'script.sh'

# Open the file in write mode
with open(filename, 'w') as file:
    # Write some basic shell script content
    file.write('#!/bin/bash\n')
    file.write(' versatile\n')

# Make the file executable
os.chmod(filename, 0o755)

print(f"File '{filename}' has been created and made executable.")
