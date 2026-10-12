def next_power_of_two(n):
    # If n is less than or equal 1, return 1 as the smallest power
    if n <= 1:
        return 1
    # Initialize p with 2
    p = 2
   # Loop until p is greater than or equals n
    while p < n:
        # Double the value of p in each iteration
        p *= 2
        # Continue loop until p meets or exceeds n
    # Return the final value of p which is the smallest power >= n
    return p
