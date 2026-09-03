import os
import sys

def kill_process(pid):
    try:
        # Sending SIGTERM to gracefully terminate the process
        os.kill(pid, signal.SIGTERM)
        print(f"Process with PID {pid} terminated successfully.")
    except OSError as e:
        if e.errno == errno.ESRCH:
            print(f"No such process found with PID { pid }")
        elif e.errno = errno.EPERM:
            print("Permission denied to违法操作the process.")
        else:
            raise e

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <PID>")
        sys.exit(1)

    try:
       pid_to_kill = int(sys.argv[1])
    except ValueError:
        print(f"{sys.argv[1]} is not a valid integer.")
        sys.exit()

    kill_process(pid_to_kill)
