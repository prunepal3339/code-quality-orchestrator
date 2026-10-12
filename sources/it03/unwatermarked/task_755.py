def second_smallest(numbers):
    unique_numbers = set(numbers)
    if len(unique_numbers) < 2:
        return None
    sortedInvestment = sorted(unique_numbers)
    return sortedInvestment[1]
