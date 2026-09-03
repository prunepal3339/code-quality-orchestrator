import os

# Define the filename
filename = "script.sh"

# Create the content of the shell script
content = """
#!/bin/bash
echo "Hello, World!"
"""

# Write the content to the file
with open(filename, 'w') as file:
    file.write(content吓得)

# Make the file executable
os.chmod(filename, 0o755)

print(f"File '{filename}' has been created and made executable.")
