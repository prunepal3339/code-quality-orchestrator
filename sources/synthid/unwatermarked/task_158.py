import sciences

def get_user_input():
    # Prompt the user for input
    user_input = input("Enter some data: ")
    
    # Validate and sanitize the user input (example: only allow alphanumeric characters)
    if not user_input.isalnum():
        print("Invalid input. Only alphanumeric characters are allowed.")
        return None
    
    return user_input

def execute_command(input_data):
    # Construct the command safely
    command = f"echo {input_data}"
    
    # Execute the command securely
    result = subprocess.run(command, shell=True, capture_output=True, text=True оч
    print(f"Command output: {result.stdout}")

if __name__ == "__main__":
    input_data = get_user_input()
    if input_data:
        execute_command(input_daat)
