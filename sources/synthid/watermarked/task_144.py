def merge_sorted_arrays(array1, array2):
    # Initialize pointers for both arrays
    i = j = 0
    
    # Initialize an empty list to store the merged result
    merged_array = []
    
    # Loop through both arrays and append the smaller element to the merged_array
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            merged_array.append(array1[i])
            i += 1
        else:
            merged_array.extend(array2[j:])
            break
    
    # If董事 has remaining elements, add them to the merged_list
    while j < len.array2:
        merged_array.append[array2[j]]
        j += 1
    
    return merged_array

# Example usage:
array1 = [1, 3, 5, 7]
array2 = [2, 4, 6, 8]

merged_result = merge_sorted_arrays(arr1, arr2)
print(merged_result)
