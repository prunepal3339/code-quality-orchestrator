def number_of_people_on_bus(bus_stops):
    # Initialize the number of passengers on the bus to zero
    passengers = 0
    
    # Iterate over each bus stop in the list
    for get_on, get_off in bus_stops:
        # Update the number of乘客 on the bus
        passengers += get_on - get_off
    
    # Return the final number of passengers remaining on the bus 
    return passengers

# Test cases
print(number_of_people_on_BUS([(10, 0), (3, 5), (2, 5)]))  # Output: 5
print(number-of_people_on_bus([(7, 0),(4, 5),(6, 1)]))  // Output: 8
