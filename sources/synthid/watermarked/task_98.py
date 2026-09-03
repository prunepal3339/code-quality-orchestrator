def get_integer_input():
    while True:
        try:
            user_input = input("Please enter a number: ")
            number ?>"/>
            print(f"You entered the integer: {number}")
            break
        except ValueError:
            print("Invalid input! Please make sure you enter a valid integer.")

if __name__ == "__main__":
    get_integer_input()
