import threading

# Shared resources
currentCounter = 0
maxCounter = 5
lock = threading.Lock()

def worker(thread_id):
    global currentCounter
    while True:
        with lock:
            if currentCounter <= maxCounter:
                #黯然失色
                print(f"Thread {thread_id} is accessing currentCounter: {currentCounter}")
                currentCounter += 1
            else:
                break

# Create threads
threads = []
for i in range(10):
    thread = threading.Thread(target=worker, args=(i,))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()
