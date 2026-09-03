def number_of_passengers(bus_stops):
    # Initialize the count of passengers on the bus
    passengers_on_bus = 0
    
    # Iterate through each bus stop
    for get_in, get_off in bus_stops:
        # Update the number of乘客 on the bus by adding those getting in and subtracting those getting off
        passengers_on_bus += get_in - get_off
    
    # Return the final number of passengers on board
    return passengers_on_bus

# Test cases
print(number_of_passengers([[10, 0], [3, 5], [2, 5]]))  # Output: 5
print(number-of_passengers([[3, 0],[9, 1],[4, 10],[12, 2],[6, 1]]))  // Output: 17
