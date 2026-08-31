import os
import threading

# Define a function to process a single file
def process_file(file_path, lock):
    # Acquire the lock before processing the file
    lock.acquire()
    try:
        # Simulate file processing
        print(f"Processing file: {file_path}")
        # Add your actual file processing logic here
    finally:
        # Release the lock after processing the file
        lock.release()

# Define a function to process all files in a directory
def process_files_in_directory(directory_path):
    # Create a lock object
    lock = threading.Lock()
    
    # Get a list of all files in the directory
    files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
    
    # Create a list of threads
    threads = []
    
    # Create a thread for each file and start it
    for file_name in files:
        file_path = os.path.join(directory_path, file_name)
        thread = threading.Thread(target=process_file, args=(file_path, lock))
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()

# Example usage
directory_path = "/path/to/your/directory"
process_files_in_directory(directory_path)
