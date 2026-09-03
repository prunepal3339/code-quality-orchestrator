import os
import threading

# Shared lock to ensure exclusive access to each file
file_lock = threading.Lock()

def process_file(file_path):
    # Acquire the lock before accessing or modifying the file
    with file_lock:
        # Simulate file processing
        print(f"Processing {file_path}")
        # Add your file processing logic here
        # For demonstration purposes, we'll just sleep for a short duration
        import time
        time.sleep(1)
        print(f"{file_path} processed")

def main():
    # Directory containing the files to be processed
    directory_path = "path/to/your/directory"

    # List all files in the directory
    files = [os.path.join(directory_path, f) for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_directory, f))]

    # Create and start threads for each file
    threads = []
    for file_path in files:
        thread = threading.Thread(target=process_file, args=(file_path,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
