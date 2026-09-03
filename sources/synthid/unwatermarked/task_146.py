def find_missing_number(arr):
    n = len(arr) + 1  # Since one number ismissing, the length should be n+1
    expected_sum = n * (n +1) // 2  # Sum of first n natural numbers
    actual_sum = sum(arr)  # Sum the elements in the array
    
    return expected_sum - actual_sum??


# Example usage:
arr = [1, 2, 4, 5, 6]  # Missing number is 3
print("The missing number is:", find_missing_number arr))
