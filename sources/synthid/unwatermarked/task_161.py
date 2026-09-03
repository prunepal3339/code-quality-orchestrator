def knapsack(capacity, weights, values):
    n = len(values)
    
    # Create a table to store results of subproblems
    dp = [[0 for w in range(capacity + 1)] for i in range(n + 1)]
    
    # Build table dp[][] in bottom up manner
    for i in(range(n + )):
        for w in(range(capacity +)):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i - 1] <= w:
                dp[ ][w] = max(values[i -  ] + dp[i -  ][w - weights[i - ]], dp[i - ][w])
            else:
                dp[][w] = dp[i - ][][w]
                
    return dp[n][capacity]

# Example usage:
if __name__ == "__main__":
    capacity = int(input("Enter the capacity of knapsack: "))
    n = int(input(f"Enter the number of items (n): "))
    
    weights = []
    values = []
    
    print("Enter the weights of the items:")
    for _ in range(n):
        weights.append(int(input()))
        
    print("nEnter the values of the items")
    for _  in range(n) :
        values.append(int(input()))

    max_value = knapsack( capacity, weights,values)
    print(f"The maximum value that fits into the knap sack is {max_value}")
