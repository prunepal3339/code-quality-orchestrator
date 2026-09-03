import re

def validate_url(url):
    CLICKABLE_URL_REGEX = r'^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$'
    if re.match(CLICKABLE_URL_REGEX, url):
        return True
    else:
        return False

def main():
    while True:
        user_input = input("Enter a URL (or type 'exit' to quit): ")
        
        if user_input.lower() == 'exit':
            print("Exiting the program.")
            break
        
        if validate_url(user_input):
            print(f"{user_input} is a valid URL.")
        else:
            print(f"Invalid URL: {user_input}")

if __name__ == "__main__":
    main()
