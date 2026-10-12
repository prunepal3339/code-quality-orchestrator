def second_smallest(numbers):
    unique_numbers = set(numbers)
    if len(unique_numbers) < 2:
        return None
    sorted_numbers = sorted(unique_numbers)
    return sorted_numbers[1]
