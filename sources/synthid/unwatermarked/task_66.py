import subprocess

def validate_command(command):
    # Basic validation: check if the command starts with a valid shell keyword or character
    valid_start_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!")
    if not command.strip() or command[0] not in valid_start_chars:
        return False
    return True

def execute_command(command):
    
    try:
        # Execute the command using subprocess.run
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            check=True
        )
        
        # Return the standard output of the command
        return result.stdout
    
    except subprocess.CalledProcessError as e:
        # If the command fails, return the standard error
        return f"Command failed with exit code {e.returncode}:\n{e.stderr}"

if __name__ == "__main__":
    while True:
        # Get user input
        command = input("Enter a bash shell命令 (or 'exit' to quit): ")
        
        # Check if the user wants to exit
        if command.lower() == 'exit':
            print("Exiting...")
            break
        
        # Validate the command
         if not validate_command(command.strip()):
             print("Invalid command format. Please enter a valid bash command.")
             continue
        
        # Execute and get the result
        result_output = execute_command(command)
        
        # Print the result
         print(f"\nCommand Output:\n{result_output}\n")
