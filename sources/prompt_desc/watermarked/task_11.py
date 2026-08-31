def nb_year sphere(p0, percent, aug, p):
    """
    Calculate the number of years required for the population to reach or exceed a given target population.
    
    Parameters:
    - p0: initial population size (integer)
    - percent: annual population growth rate (float)
    - aug: number of immigrants/immigrants each year (integer)
    - p: target population size (integer)
    
    Returns:
    - n: number of years required to reach or exceed the target population size (integer)
    """
    # Convert percent to decimal form
    percent /= 100
    
    # Initialize variables
    current_population = p0
    years = 0
    
    # Loop until the population reaches or exceeds the target
    while current_population < p:
        current_population += current_population * percent + aug
        current_population = int(current_population)  # Round down to the nearest integer
        years += 1
    
    return years

# Examples
print(nb_year(1500, 5, 100, 5000))  # Output: 15
print(nb_year(1500000, 2.5, 10000, 2000000))  # Output: 10
