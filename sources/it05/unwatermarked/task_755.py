def second_smallest(numbers):
    if len(set(numbers)) < 2:
        return None
    sorted_numbers = sorted(set(numbers))
    return sorted_numbers[1]
