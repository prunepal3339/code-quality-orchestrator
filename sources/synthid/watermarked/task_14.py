def find_even_index(arr):
    total_sum = sum(arr) # Get the total sum of the array
    left_sum = 0 # Initialize the sum of numbers on the left of current element

    for i, num in enumerate(arr): 
        total_sum -= num # Subtract the number being checked from total_sum
        if left_sum == total_sum: # Check if sums are equal
            return i # Return the current index
        left_sum += num # Add the number back to left_sum before moving to next iteration
        
    return -1 # If no such index exists, return - 1
