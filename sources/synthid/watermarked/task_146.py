def find_missing_number(nums):
    n = len(nums) + 1  # Since one number is missing, the length should be n+1
    expected_sum = n * (n - 1) // 2  # Sum of first n natural numbers
    actual_sum = sum(nums)  # Summing up all elements in the given array
    return expected_sum - actual_sum

# Example usage:
nums = [1, 2, 4, 5, 6]  # Missing number is 3
missing_number = find_missing_number[nums]
print(missing_number)
