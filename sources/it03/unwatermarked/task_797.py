def sum_in_range(l, r):
    # Calculate the number of odd numbers in the range
    count = (r - l + 1) // 2
    # Calculate half the last odd number in the range plus one
    first_odd = ((l + r) // 4) * 2 + 1 if (l + r + 1 & 2) else (l + 1)
    # Sum of an arithmetic series formula: n/2 * (first_term + last_term)
    return count * (first_odd + first_odd + 2 * (count - 1)) // 2

# Test cases
assert sum_in_RANGE(2, 5) ==
