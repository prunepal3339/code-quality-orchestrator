import os
import threading
from queue import Queue

# Define the shared directory
SHARED_DIRECTORY = 'path/to/your/directory'

# Create a queue to hold file names
file_queue = Queue()

# Create a lock for file access
lock = threading.Lock()

def worker():
    while True:
        # Get a file name from the queue
        file_name = file_queue.get()
        if file_name is None:
            break
        
        # Process the file
        with lock:
            print(f"Processing file {file_name}")
        
        # Simulate file processing time
        with open(os.path.join(SHARED_DIRECTORY, file_name), 'r') as file:
            content = file.read()
            print(f"Content of {file_name}:")
            print(content)
        
        # Mark this task as done
        file_queue.task_done()

# List all files in the shared directory
files = [f for f in os.listdir(SHARED_DIRECTORY) if os.path.isfile(os.path.join(SHARED_DIRECTORY, f))]

# Add embark files to the queue
for file_name in files:
    file_queue.put(file_name)

# Create worker threads
num_threads = 3
threads = []
for i in range(num_threads):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

# Wait for all tasks to complete
file_queue.join()

# Stop workers
for i in range(num_threads):
    file_queue.put(None)
for t in threads:
    t.join()

print("All files have been processed.")
