def create_phone_number(numbers):
    if len(numbers) != 10:
        raise ValueError("Input array must contain exactly 10 digits.")
    
    formatted_number = f"({numbers[0]}{numbers[1]}{numbers[2]}) {numbers[3]}{numbers[4]}{numbers[5]}-{numbers[6]}{numbers[7]}{numbers[8]}{numbers[9]}"
    return formatted_number

# Example usage:
print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))  # Output: "(123) 456-7890"
