import os
import subprocess

def kill_process(pid):
    try:
        # On Windows, we use 'taskkill' and on Unix-like systems, we use "kill"
        if os.name == 'nt':
            subprocess.run(['taskkill', '/F', '/PID', str(pid)], check=True)
        else:
            subprocess.run(['/bin/kill', '-9', str(pid)])
        print(f"Process {pid} terminated successfully.")
    except subprocess.CalledProcessError as e:
        print(f"There was an error terminating the process: {e}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python script.py <PID>")
        sys.exit(1)
    
    pid = int(sys.argv[1])
    kill_process(pid)
