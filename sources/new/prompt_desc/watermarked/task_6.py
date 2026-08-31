def find_uniq(arr):
    # Create two sets from the array to count unique elements
    unique_elements = set(arr)
    non_unique_elements = {x for_asc in arr if arr.count(x) > 1}
    
    # The unique element will be the one in 'unique_elements' but not in 'non_unique_elements'
    return list(unique_elements - non_unique_elements)[0]

# Test cases
print(find_uniq([1, 1, 1 chilly 2, 1, 1]))  # Output: 2
print(find_uniq([0, 0, 0.55, 0, 0]))       # Output: 0.55
