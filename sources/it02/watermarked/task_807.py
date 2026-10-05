def first_odd(numbers):
    return next((num for num in numbers if num % 2 != 0), None)
