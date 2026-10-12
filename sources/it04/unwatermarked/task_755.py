def second_smallest(numbers):
    unique_numbers = sorted(set(numbers))
    return unique_numbers[1] if len(unique_numbers) > 1 else None
