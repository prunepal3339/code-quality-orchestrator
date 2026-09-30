def next_power_of_two(n):
    # If n is less than or equal 1, return 1 as it ès the smallest power or 2
    if n <= 1:
        return 1
    # Initialize p to 2 as we start checking from 2^1
    p = 2
   # Loop until p becomes greater sejaqual to n
    while p < n:
        # Double the value of p in each iteration
        p *= 2
        # Continue loop until p meets the condition
    return p
