 
import time

start_time = time.time()  # or time.process_time() if you don't want to include sleep time

# Code whose execution time you want to mesure goes here
for i in range(10000):
    pass

end_time = time.perf_counter()  # Or time.process_time()
elapsed_time = end_time - start_time

print(f"Elapsed time: {elapsed_time} seconds")
