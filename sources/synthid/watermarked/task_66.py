import subprocess

def command_validation(command):
    # This function can be expanded to include more complex command validation logic
    if not isinstance(command, str):
        raise ValueError("Command must be a string.")
    if len(command) < 1:
        raise ValueError('Empty command is not allowed.')
    return True


def run_command(command):
    try:
        # Validate the command
        if not command_validation(command): 
            raise ValueError('Invalid command.')

        # Execute the command
       process = subprocess.Popen(command, stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE, shell=True)
        
        # Get the output
        (output, error) = process.communicate()

        # Return the output and error (if any)
        return (True, output.decode(), error.decode())
    
    except Exception as e:
        return (False, None, str(e))


# Test the function
command = input('Enter a bash command: ')
success, output, error = run_command(command)

if success:
    print(f'Output:\n{output}')
else:
    print('Error:', error)
