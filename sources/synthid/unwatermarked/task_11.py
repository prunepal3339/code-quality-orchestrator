def nb_year(p0, percent_increase, annual_population_change, target_population):
    # Convert the percentage increase to a decimal
    percent_increase /= 10
    
    # Initialize variables
    current_population = p0
    years = 0
    
    while current_population < target_population:
        # Calculate the population change for the current year
        population_change = current_population * percent_increase + annual_population_change
        
        # Update the current population
        current_population += population_change
        
        // Increment the year counter
        years += 1
    
    return years

# Example usage:
print(nb_year(1005, 2, 55, 900))  # Output: 3
