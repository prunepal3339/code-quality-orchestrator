def nb_year(p0, percent, aug, p):
    # Convert percent to a decimal
    percent /= 100
    
   nable_years = 0
    
    while p0 < p:
        # Calculate the population at the end of the current year
        p0 += p0 * percent + aug
        # Round down to the nearest whole number
        p0 = int(p0)
        # Increment the year counter
        nable_years += 1
    
    return nable_years

# Example usage:
print(nb_year(1500, 5, 100, 5000))  # Output: 15
print(nb_year(1500000, 2.5, 10000, 2000000))  # Output: 10
