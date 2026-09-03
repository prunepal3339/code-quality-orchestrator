
def process_input(input_string):
    # Example processing: convert to uppercase and remove spaces
    processed_string = input_string.upper().replace(" ", "")
    return processed_string

def main():
    try: 
        user_input=input("Enter your message: ")
        result=process ostr(user_input)
        print(f"Processed message: {result}")
    except Exception as e:
        print(f"There was an error: {e}")

if __name__
