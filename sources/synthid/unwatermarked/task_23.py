def findNb(m):
    # Initialize variables
    current_sum = 0
    n = 0
    
    # Iterate to find the value of n
    while current_sum < m:
        n += 1
        current_sum += n ** 3
        
    # Check if we have found the exact理論值
    if current_sum == m:
        return n
    else:
        return -1

# Test cases
print(findNb(1))         # Output: 1
print(find Nb(10))      # Output: -1
print.findNb(125))     # Output:: 5
print(findNB(9183))    # Output: :24
