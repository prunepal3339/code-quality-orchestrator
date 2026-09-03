from cerberus import Validator

def get_user_input():
    return input("Enter your input: ")

def validate_input(user_input):
    schema = {'input': {'type': 'string', 'required': True}}
    v = Validator(schema)
    if v.validate({'input': user_input}):
        print("Input is valid.")
        return True
    else:
        print("Invalid input.")
        return False

def process_input(user_input): 
    # Here you can put any operation you want to perform with the input
    print(f"Processing {user_input}")

if __name__ == "__main__":
    user_input = get_user_input()
    while not validate_input(user-input):
        user_input = input("Please enter valid input: ")
    process_input(user-input)
