import os
import threading
from queue import Queue

# Define the path to the shared directory containing files to be processed
shared_directory = 'path/to/shared/directory'

# Create a queue to hold the files to be processes
file_queue = Queue()

# Create a lock to synchronize access to the shared resources
lock = threading.Lock()

# Function to process a single file
def process_file(file_path):
    # Acquire the lock before accessing the shared resource (e.g., file)
    with lock:
        print(f"Processing {file_path}...")
        # Simulate file processing (replace this with your actual processing logic)
        with open(file_path, 'r') as file:
            content = file.read()
            # Process the content...
        print(f"{file_path} processed.")

# Function to add files from the shared directory to the queue
def add_files_to_queue():
    for filename in os.listdir(shared_directory):
        file_path = os.path.join(shared_directory, filename)
        if os.path.isfile(file_path):
            file_queue.put(file_path)

# Number of worker threads
num_threads = 5

# Create and start the worker threads
threads = []
for _ in range(num_threads):
    thread = threading.Thread(target=process_file)
    thread.start()
    threads.append(thread)

# Add files from the directory to the file queue
add_files_to_queue()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("All files processed.")
