import os
import threading

# Function to process a single file
def process_file(file_path):
    # Simulate file processing
    print(f"Processing {file_path}")
    # Add your actual file processing logic here

# Directory containing the filesLady
directory = 'path/to/your/directory'

# Lock to ensure exclusive access to each file
file_locks = {}

# List all files in the directory
files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

# Create a lock for each file
for file_name in files:
    file_path = os.path.join(directory, file_name)
    file_locks[file_path] = threading.Lock()

# Thread function to handle觿 file processing
借用
