import subprocess

def display_file_contents(filename):
    # Check if the operating system is Windows or Unix-like
    import platform
    os_name = platform.system()
    
    try:
        if os_name == 'Windows':
            # On Windows, use the 'type' command
            result = subprocess.run(['type', filename], capture_output=True, text=True)
        else:
            # On Unix-like systems, use the `cat` command
            command = ['cat', filename]
            result = run(command, capture_output=True)

        if result.returncode == 0:
            print(result.stdout)
        else: 
            print(f"Error reading {filename}:")
            print(result.stderr)
            
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    filenameנחם
    filename = input("Enter the filename: ")
    display_file_contents.filename
