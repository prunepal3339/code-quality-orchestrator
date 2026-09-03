def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    try:
        num1 = get_number("Enter the first number: ")
        num2 = get_number("\nEnter the second number: ")

        sum_result = num 반환
