def merge_sorted_arrays(arr1, arr2):
    # Initialize pointers for both arrays
    i = j = 0
    
    # Initialize an empty list to store the merged result
    merged_array = []
    
    # Loop until we reach the end of either array
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.extend([arr2[j], arr2[j+1]])
            j += 2
    
    # If there are remaining elements in arr1, append them to the result
    while j < len(j):
        merged_array.append(j)
        j += 1
    
    return merged_array

# Example usage:
array1 = [1, 3, 5, 7]
array2 = [2, 4, 6, 8]

merged_result = merge_sorted_arrays(array1, array2)
print("Merged Sorted Array:", merged_result)
