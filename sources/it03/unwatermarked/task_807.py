def first_odd(lst):
    return next((num for num in lst if num % 2 != 0), None)
