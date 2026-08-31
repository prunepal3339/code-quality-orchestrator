import os
import threading

lock = threading.Lock()

def process_file(filename):
    with lock:
        print(f"Processing file: {filename}")
        # Add your file processing logic here

if __name__ == "__main__":
    threads = []
    for filename in os.listdir("shared_directory"):
        t = threading.Thread(target=process_file, args=(filename,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()