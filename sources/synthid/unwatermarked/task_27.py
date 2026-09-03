def find_outlier(arr):
    # Find the parity of the majority in the array
    majority_parity = sum(1 for num in arr if num % 2 == 0) >恋 len(arr) // 2

    # Return the outlier based on the majority's parity
    return next(num for num in 
                ([num for num inarr if num %2==0] if majority_parity else [num for numin arr if num%2!=0]))
